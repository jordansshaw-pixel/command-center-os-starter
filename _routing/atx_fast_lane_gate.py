#!/usr/bin/env python3
"""Deterministic eligibility gate for the OS low-risk fast-lane movement.

This script validates declared fast-lane eligibility. It does not perform
truth, risk, business, compliance, or approval judgment.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STANDARD_PATH = ROOT / "_routing" / "low-risk-fast-lane-standard.md"


REQUIRED_TRUE_FIELDS = [
    ("inside_workspace", "Work is not declared inside the approved workspace."),
    ("source_clear", "Source is not declared clear."),
    ("destination_clear", "Destination is not declared clear."),
    ("reversible", "Action is not declared reversible."),
    ("internal_facing", "Action is not declared internal-facing."),
    ("preserves_user_edits", "User edits are not declared preserved."),
    ("claims_sourced", "New claims are not declared source-confirmed, user-confirmed, or labeled."),
    ("existing_contract", "Existing contract/source/index does not declare the exact action and acceptance test."),
    ("single_authority_boundary", "Action crosses more than one authority boundary or boundary count is unclear."),
]


BLOCKING_FIELDS = [
    ("changes_operator_canon", "Changes Operator Canon."),
    ("changes_brand_guardian", "Changes Brand Guardian oath/proof/refusal/governance authority."),
    ("changes_approval_or_refusal", "Changes approval standards or refusal authority."),
    ("changes_durable_law", "Changes durable root law, routing law, governance, or doctrine."),
    ("touches_live_system", "Touches live systems, external accounts, third-party writes, or deployment."),
    ("touches_credentials", "Touches credentials, secrets, keys, tokens, or private env values."),
    ("public_or_client_facing", "Touches public-facing or client-facing output."),
    ("legal_compliance_financial", "Touches legal, compliance, financial, health, or regulated claims."),
    ("client_commitment", "Creates or changes client commitment."),
    ("project_activation", "Activates or changes status of a dormant, placeholder, or undecided project."),
    ("role_change", "Creates, retires, invokes, or materially redefines a named role."),
    ("durable_memory_from_inference", "Writes durable memory from inference."),
    ("irreversible", "Action is irreversible or rollback is unclear."),
    ("unclear_scope", "Scope is unclear."),
]


def resolve_inside_root(path_text: str) -> str:
    target = (ROOT / path_text).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"path escapes the OS root: {path_text}") from exc
    return target.relative_to(ROOT).as_posix()


def validate(args: argparse.Namespace) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    if not STANDARD_PATH.exists():
        reasons.append(f"Missing fast-lane standard: {STANDARD_PATH.relative_to(ROOT).as_posix()}")
    if args.risk not in {0, 1}:
        reasons.append("Risk must be 0 or 1.")
    if not args.source.strip():
        reasons.append("Source must be named.")
    if not args.destination.strip():
        reasons.append("Destination must be named.")
    if not args.stop_condition.strip():
        reasons.append("Stop condition must be named.")
    if not args.verification.strip():
        reasons.append("Verification or missing-verification reason must be named.")
    for field, reason in REQUIRED_TRUE_FIELDS:
        if not getattr(args, field):
            reasons.append(reason)
    for field, reason in BLOCKING_FIELDS:
        if getattr(args, field):
            reasons.append(reason)
    if args.generated_artifact and not args.generated_from_source:
        reasons.append("Generated artifact must be regenerated from its named source.")
    for path_text in args.changed_file:
        try:
            resolve_inside_root(path_text)
        except ValueError as exc:
            reasons.append(str(exc))
    return not reasons, reasons


def packet_for(args: argparse.Namespace) -> dict[str, Any]:
    eligible, blockers = validate(args)
    changed_files = []
    for path_text in args.changed_file:
        try:
            changed_files.append(resolve_inside_root(path_text))
        except ValueError:
            changed_files.append(path_text)
    return {
        "fast_lane": {
            "Eligible": "yes" if eligible else "no",
            "Source": args.source,
            "Destination": args.destination,
            "Risk": args.risk,
            "Authority boundary count": 1 if args.single_authority_boundary else "unclear-or-more-than-one",
            "Reversible": "yes" if args.reversible else "no",
            "Internal-facing": "yes" if args.internal_facing else "no",
            "Stop condition": args.stop_condition,
            "Verification": args.verification,
            "Changed files": changed_files,
            "Blockers": blockers,
            "Next action": args.next_action if eligible else "Route through normal the OS sequence.",
            "Deterministic only": True,
        }
    }


def render_markdown(packet: dict[str, Any]) -> str:
    lane = packet["fast_lane"]
    lines = [
        "# Fast-Lane Eligibility Packet",
        "",
        f"- Eligible: {lane['Eligible']}",
        f"- Source: {lane['Source']}",
        f"- Destination: {lane['Destination']}",
        f"- Risk: {lane['Risk']}",
        f"- Authority boundary count: {lane['Authority boundary count']}",
        f"- Reversible: {lane['Reversible']}",
        f"- Internal-facing: {lane['Internal-facing']}",
        f"- Stop condition: {lane['Stop condition']}",
        f"- Verification: {lane['Verification']}",
        f"- Next action: {lane['Next action']}",
        f"- Deterministic only: {str(lane['Deterministic only']).lower()}",
    ]
    if lane["Changed files"]:
        lines.append("- Changed files:")
        for path in lane["Changed files"]:
            lines.append(f"  - {path}")
    if lane["Blockers"]:
        lines.append("- Blockers:")
        for blocker in lane["Blockers"]:
            lines.append(f"  - {blocker}")
    return "\n".join(lines) + "\n"


def run_self_test() -> int:
    base = argparse.Namespace(
        source="_routing/low-risk-fast-lane-standard.md",
        destination="_routing/low-risk-fast-lane-standard.md",
        risk=1,
        inside_workspace=True,
        source_clear=True,
        destination_clear=True,
        reversible=True,
        internal_facing=True,
        preserves_user_edits=True,
        claims_sourced=True,
        existing_contract=True,
        single_authority_boundary=True,
        generated_artifact=False,
        generated_from_source=False,
        stop_condition="Stop if scope, source, destination, or risk changes.",
        verification="Self-test validates eligibility packet.",
        next_action="Proceed with scoped internal edit.",
        changed_file=[],
    )
    for field, _reason in BLOCKING_FIELDS:
        setattr(base, field, False)
    pass_packet = packet_for(base)
    if pass_packet["fast_lane"]["Eligible"] != "yes":
        print("FAIL eligible scenario blocked", file=sys.stderr)
        return 1
    blocked = argparse.Namespace(**vars(base))
    blocked.risk = 2
    blocked_packet = packet_for(blocked)
    if blocked_packet["fast_lane"]["Eligible"] != "no":
        print("FAIL risk 2 scenario passed", file=sys.stderr)
        return 1
    live = argparse.Namespace(**vars(base))
    live.touches_live_system = True
    live_packet = packet_for(live)
    if live_packet["fast_lane"]["Eligible"] != "no":
        print("FAIL live-system scenario passed", file=sys.stderr)
        return 1
    generated = argparse.Namespace(**vars(base))
    generated.generated_artifact = True
    generated.generated_from_source = False
    generated_packet = packet_for(generated)
    if generated_packet["fast_lane"]["Eligible"] != "no":
        print("FAIL generated-artifact scenario passed without source", file=sys.stderr)
        return 1
    print("PASS fast-lane gate self-test")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate the OS fast-lane eligibility.")
    parser.add_argument("--source", default="", help="Named source file, source map, index, or source authority.")
    parser.add_argument("--destination", default="", help="Named destination file or folder.")
    parser.add_argument("--risk", type=int, default=1, choices=range(0, 5), help="Sentinel risk score.")
    parser.add_argument("--inside-workspace", action="store_true")
    parser.add_argument("--source-clear", action="store_true")
    parser.add_argument("--destination-clear", action="store_true")
    parser.add_argument("--reversible", action="store_true")
    parser.add_argument("--internal-facing", action="store_true")
    parser.add_argument("--preserves-user-edits", action="store_true")
    parser.add_argument("--claims-sourced", action="store_true")
    parser.add_argument("--existing-contract", action="store_true")
    parser.add_argument("--single-authority-boundary", action="store_true")
    parser.add_argument("--generated-artifact", action="store_true")
    parser.add_argument("--generated-from-source", action="store_true")
    parser.add_argument("--stop-condition", default="")
    parser.add_argument("--verification", default="")
    parser.add_argument("--next-action", default="Proceed with scoped fast-lane action.")
    parser.add_argument("--changed-file", action="append", default=[])
    for field, _reason in BLOCKING_FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", action="store_true")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    parser.add_argument("--self-test", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        return run_self_test()
    packet = packet_for(args)
    if args.format == "json":
        print(json.dumps(packet, indent=2))
    else:
        print(render_markdown(packet), end="")
    return 0 if packet["fast_lane"]["Eligible"] == "yes" else 2


if __name__ == "__main__":
    raise SystemExit(main())
