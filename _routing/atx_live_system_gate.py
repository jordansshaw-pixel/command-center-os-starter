#!/usr/bin/env python3
"""Deterministic completeness gate for the OS live-system packets.

This script reads JSON and validates packet completeness and internal
consistency only. It does not perform live-system work.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STANDARD_PATH = ROOT / "_connectivity" / "live-system-risk-rules.md"

REQUIRED_FIELDS = [
    "System",
    "Scope",
    "Requested action",
    "Current source",
    "Owner",
    "Permission class",
    "Risk score",
    "Approval required",
    "Approval status",
    "Credential handling",
    "Rollback path",
    "Blocked actions",
    "Allowed safe actions",
    "Next action",
]

ALLOWED_APPROVAL_STATUSES = {"blocked", "pending", "approved"}
NO_HANDLING_VALUES = {"", "none", "n/a", "na", "not applicable"}


def is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def normalized_text(value: Any) -> str:
    if isinstance(value, str):
        return value.strip().lower()
    return str(value).strip().lower()


def has_handling(value: Any) -> bool:
    if not is_non_empty(value):
        return False
    if isinstance(value, str):
        return normalized_text(value) not in NO_HANDLING_VALUES
    return True


def blocked_result(blockers: list[str], source: str = "") -> dict[str, Any]:
    result: dict[str, Any] = {
        "eligible": "no",
        "blockers": blockers,
        "deterministicOnly": True,
    }
    if source:
        result["source"] = source
    return result


def field_summary(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "requiredFields": REQUIRED_FIELDS,
        "fieldsPresent": [field for field in REQUIRED_FIELDS if field in packet and is_non_empty(packet[field])],
        "riskScore": packet.get("Risk score"),
        "approvalStatusField": "present" if is_non_empty(packet.get("Approval status")) else "missing",
    }


def validate_packet(packet: Any, source: str = "") -> dict[str, Any]:
    if not STANDARD_PATH.exists():
        return blocked_result(
            [f"Missing live-system risk standard: {STANDARD_PATH.relative_to(ROOT).as_posix()}"],
            source,
        )
    if not isinstance(packet, dict):
        return blocked_result(["Packet must be a JSON object."], source)

    blockers: list[str] = []
    missing_fields = [field for field in REQUIRED_FIELDS if field not in packet or not is_non_empty(packet[field])]
    for field in missing_fields:
        blockers.append(f"Missing or empty required field: {field}")

    risk_score = packet.get("Risk score")
    if isinstance(risk_score, bool) or not isinstance(risk_score, int) or risk_score not in range(0, 5):
        blockers.append("Risk score must be an integer from 0 to 4.")

    status_value = packet.get("Approval status")
    status = normalized_text(status_value) if is_non_empty(status_value) else ""
    if status and status not in ALLOWED_APPROVAL_STATUSES:
        blockers.append("Approval status has an unsupported value.")

    if status == "approved":
        for field in ["Approval required", "Owner", "Rollback path"]:
            if not is_non_empty(packet.get(field)):
                blockers.append(f"{field} must be present when Approval status indicates approved.")

    if risk_score == 4 and (
        not has_handling(packet.get("Blocked actions")) or not has_handling(packet.get("Allowed safe actions"))
    ):
        blockers.append("Risk score 4 requires non-empty Blocked actions and Allowed safe actions.")

    if blockers:
        result = blocked_result(blockers, source)
        result["fieldSummary"] = field_summary(packet)
        return result

    return {
        "eligible": "yes",
        "blockers": [],
        "fieldSummary": field_summary(packet),
        "deterministicOnly": True,
        **({"source": source} if source else {}),
    }


def result_for_text(text: str, source: str = "") -> dict[str, Any]:
    try:
        packet = json.loads(text)
    except json.JSONDecodeError as exc:
        return blocked_result([f"Malformed JSON: {exc.msg} at line {exc.lineno}, column {exc.colno}."], source)
    return validate_packet(packet, source)


def read_packet_text(args: argparse.Namespace) -> tuple[str, str]:
    if args.packet:
        target = Path(args.packet)
        return target.read_text(encoding="utf-8"), str(target)
    return sys.stdin.read(), "stdin"


def complete_packet() -> dict[str, Any]:
    return {
        "System": "Example deployment target",
        "Scope": "Local planning packet for a scoped live-system review",
        "Requested action": "Prepare a reviewed change packet",
        "Current source": "_connectivity/live-system-risk-rules.md",
        "Owner": "the operator",
        "Permission class": "live-action",
        "Risk score": 2,
        "Approval required": "Explicit the operator approval plus Warden review",
        "Approval status": "approved",
        "Credential handling": "No credentials in packet; use approved vault flow only",
        "Rollback path": "Revert the proposed change through the same live-system control surface",
        "Blocked actions": "No live change from this validation gate",
        "Allowed safe actions": "Validate packet completeness and prepare review handoff",
        "Next action": "Move to Warden and the operator review outside this gate",
    }


def expect_eligible(packet: Any, expected: str, label: str, expected_text: str | None = None) -> bool:
    result = validate_packet(packet, label)
    if result["eligible"] != expected:
        print(f"FAIL {label}: expected eligible {expected}, got {result['eligible']}", file=sys.stderr)
        return False
    if expected_text and expected_text not in "\n".join(result.get("blockers", [])):
        print(f"FAIL {label}: missing blocker text {expected_text!r}", file=sys.stderr)
        return False
    return True


def run_self_test() -> int:
    base = complete_packet()
    cases: list[tuple[str, dict[str, Any], str, str | None]] = []

    missing_rollback = dict(base)
    del missing_rollback["Rollback path"]
    cases.append(("missing rollback path", missing_rollback, "no", "Rollback path"))

    empty_owner = dict(base)
    empty_owner["Owner"] = ""
    cases.append(("approved status empty owner", empty_owner, "no", "Owner"))

    risk_four_no_handling = dict(base)
    risk_four_no_handling["Risk score"] = 4
    risk_four_no_handling["Blocked actions"] = "none"
    cases.append(("risk 4 missing handling", risk_four_no_handling, "no", "Risk score 4"))

    unknown_status = dict(base)
    unknown_status["Approval status"] = "ready"
    cases.append(("unknown approval status", unknown_status, "no", "Approval status"))

    if not expect_eligible(base, "yes", "complete approved packet"):
        return 1
    for label, packet, expected, expected_text in cases:
        if not expect_eligible(packet, expected, label, expected_text):
            return 1

    malformed = result_for_text("{", "malformed self-test")
    if malformed["eligible"] != "no" or "Malformed JSON" not in "\n".join(malformed.get("blockers", [])):
        print("FAIL malformed JSON did not return a readable blocker", file=sys.stderr)
        return 1

    print("PASS live-system gate self-test")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the OS live-system packet completeness.")
    parser.add_argument("--packet", help="JSON live-system packet path. Reads stdin when omitted.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-tests.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        return run_self_test()
    try:
        text, source = read_packet_text(args)
    except OSError as exc:
        result = blocked_result([f"Could not read packet: {exc}"], args.packet or "stdin")
    else:
        result = result_for_text(text, source)
    print(json.dumps(result, indent=2))
    return 0 if result["eligible"] == "yes" else 2


if __name__ == "__main__":
    raise SystemExit(main())
