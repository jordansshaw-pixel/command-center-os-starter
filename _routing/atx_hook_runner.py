#!/usr/bin/env python3
"""Hook-facing runner for deterministic the OS multi-agent engagement checks.

This wrapper is safe to call from future hooks or task runners. It does not
install hooks and does not perform agent judgment.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import atx_fast_lane_gate
import atx_multi_agent_gate


ROOT = Path(__file__).resolve().parents[1]


EVENT_DEFAULTS: dict[str, dict[str, Any]] = {
    "pre-task": {
        "trigger": "pre-task multi-agent engagement check",
        "memory_impact": "check",
        "require_build_approval": False,
    },
    "pre-build": {
        "trigger": "pre-build multi-agent engagement check",
        "memory_impact": "update-source",
        "require_build_approval": True,
    },
    "pre-finalize": {
        "trigger": "pre-finalize authority and memory check",
        "memory_impact": "check",
        "require_build_approval": False,
    },
    "context-recovery": {
        "trigger": "context recovery and context-bleed check",
        "memory_impact": "check",
        "require_build_approval": False,
        "work_type": "context-bleed",
    },
    "source-change": {
        "trigger": "source-change multi-agent engagement check",
        "memory_impact": "update-source",
        "require_build_approval": False,
    },
    "fast-lane-check": {
        "trigger": "fast-lane eligibility check",
        "memory_impact": "none",
        "require_build_approval": False,
        "fast_lane": True,
    },
}


def resolve_inside_root(path_text: str) -> Path:
    target = (ROOT / path_text).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"output path escapes the OS root: {path_text}") from exc
    return target


def gate_args(args: argparse.Namespace) -> argparse.Namespace:
    defaults = EVENT_DEFAULTS[args.event]
    return argparse.Namespace(
        request=args.request,
        work_type=args.work_type or defaults.get("work_type"),
        trigger=args.trigger or defaults["trigger"],
        scope=args.scope,
        workspace=args.workspace,
        risk=args.risk,
        memory_impact=args.memory_impact or defaults["memory_impact"],
        build_handoff_approved=args.allow_build_handoff,
    )


def hook_status(args: argparse.Namespace, packet: dict[str, Any]) -> dict[str, Any]:
    defaults = EVENT_DEFAULTS[args.event]
    missing = packet["validation"]["missingRequired"]
    build_allowed = packet["multi_agent_engagement"]["Build handoff allowed"] == "yes"
    if missing:
        return {
            "event": args.event,
            "status": "block",
            "reason": "Required roles are missing, non-invokable, or missing doctrine/contract/stage paths.",
            "nextAction": "Route to Conductor before movement.",
        }
    if defaults["require_build_approval"] and not build_allowed:
        return {
            "event": args.event,
            "status": "block",
            "reason": "Pre-build event requires explicit build handoff approval.",
            "nextAction": "Use --allow-build-handoff only after reviewed authorization exists.",
        }
    return {
        "event": args.event,
        "status": "pass",
        "reason": "Deterministic hook check completed.",
        "nextAction": "Use generated packets for agent judgment and Conductor synthesis.",
    }


def add_hook_result(args: argparse.Namespace, packet: dict[str, Any]) -> dict[str, Any]:
    packet["hook_result"] = hook_status(args, packet)
    packet["hook_result"]["deterministicOnly"] = True
    packet["hook_result"]["changedFiles"] = args.changed_file
    packet["hook_result"]["installedHook"] = False
    return packet


def render_markdown(packet: dict[str, Any]) -> str:
    base = atx_multi_agent_gate.render_markdown(packet)
    result = packet["hook_result"]
    lines = [
        base.rstrip(),
        "",
        "## Hook Result",
        f"- Event: {result['event']}",
        f"- Status: {result['status']}",
        f"- Reason: {result['reason']}",
        f"- Next action: {result['nextAction']}",
        f"- Deterministic only: {str(result['deterministicOnly']).lower()}",
        f"- Installed hook: {str(result['installedHook']).lower()}",
    ]
    if result["changedFiles"]:
        lines.append("- Changed files:")
        for path in result["changedFiles"]:
            lines.append(f"  - {path}")
    return "\n".join(lines) + "\n"


def write_packet(path_text: str, content: str) -> Path:
    target = resolve_inside_root(path_text)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")
    return target


def run_self_test() -> int:
    scenarios = [
        {
            "event": "pre-task",
            "request": "research source confidence",
            "expected_status": "pass",
        },
        {
            "event": "pre-build",
            "request": "build deterministic infrastructure",
            "expected_status": "block",
        },
        {
            "event": "pre-build",
            "request": "build deterministic infrastructure",
            "allow_build_handoff": True,
            "expected_status": "pass",
        },
        {
            "event": "context-recovery",
            "request": "recover after context bleed",
            "expected_work_type": "context-bleed",
            "expected_status": "pass",
        },
    ]
    for scenario in scenarios:
        args = argparse.Namespace(
            event=scenario["event"],
            request=scenario["request"],
            work_type=None,
            trigger=None,
            scope="root",
            workspace="root",
            risk=None,
            memory_impact=None,
            allow_build_handoff=scenario.get("allow_build_handoff", False),
            changed_file=[],
        )
        packet = add_hook_result(args, atx_multi_agent_gate.packet_for(gate_args(args)))
        actual_status = packet["hook_result"]["status"]
        if actual_status != scenario["expected_status"]:
            print(f"FAIL {scenario['event']} status {actual_status}", file=sys.stderr)
            return 1
        if not packet["multi_agent_engagement"]["Doctrine source files"]:
            print(f"FAIL {scenario['event']} missing doctrine sources", file=sys.stderr)
            return 1
        expected_work_type = scenario.get("expected_work_type")
        if expected_work_type and packet["multi_agent_engagement"]["Work type"] != expected_work_type:
            print(f"FAIL {scenario['event']} work type", file=sys.stderr)
            return 1
    fast_args = argparse.Namespace(
        event="fast-lane-check",
        request="fix internal typo",
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
        stop_condition="Stop if scope changes.",
        verification="Self-test packet.",
        next_action="Proceed.",
        changed_file=[],
    )
    for field, _reason in atx_fast_lane_gate.BLOCKING_FIELDS:
        setattr(fast_args, field, False)
    fast_packet = atx_fast_lane_gate.packet_for(fast_args)
    if fast_packet["fast_lane"]["Eligible"] != "yes":
        print("FAIL fast-lane-check eligible scenario", file=sys.stderr)
        return 1
    blocked_fast_args = argparse.Namespace(**vars(fast_args))
    blocked_fast_args.risk = 2
    blocked_fast_packet = atx_fast_lane_gate.packet_for(blocked_fast_args)
    if blocked_fast_packet["fast_lane"]["Eligible"] != "no":
        print("FAIL fast-lane-check risk 2 scenario", file=sys.stderr)
        return 1
    print("PASS hook-runner self-test")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run deterministic the OS hook/task checks.")
    parser.add_argument("--event", choices=sorted(EVENT_DEFAULTS), required=False, default="pre-task")
    parser.add_argument("--request", default="", help="Plain-language task or hook payload.")
    parser.add_argument("--work-type", choices=sorted(atx_multi_agent_gate.ROLE_SETS), help="Override work type.")
    parser.add_argument("--trigger", help="Override trigger summary.")
    parser.add_argument("--scope", default="root", help="Engagement scope.")
    parser.add_argument("--workspace", default="root", help="Workspace label.")
    parser.add_argument("--risk", type=int, choices=range(0, 5), help="Sentinel risk score override.")
    parser.add_argument("--memory-impact", choices=["none", "check", "write", "update-source"])
    parser.add_argument("--allow-build-handoff", action="store_true", help="Allow pre-build pass after approval.")
    parser.add_argument("--changed-file", action="append", default=[], help="Changed file path, repeatable.")
    parser.add_argument("--source", default="", help="Fast-lane source authority.")
    parser.add_argument("--destination", default="", help="Fast-lane destination.")
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
    for field, _reason in atx_fast_lane_gate.BLOCKING_FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", action="store_true")
    parser.add_argument("--write-packet", help="Optional the OS-root-relative packet output path.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-tests.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        return run_self_test()
    if EVENT_DEFAULTS[args.event].get("fast_lane"):
        packet = atx_fast_lane_gate.packet_for(args)
        if args.format == "json":
            content = json.dumps(packet, indent=2) + "\n"
        else:
            content = atx_fast_lane_gate.render_markdown(packet)
        if args.write_packet:
            target = write_packet(args.write_packet, content)
            print(str(target.relative_to(ROOT).as_posix()))
        else:
            print(content, end="")
        return 0 if packet["fast_lane"]["Eligible"] == "yes" else 2
    packet = add_hook_result(args, atx_multi_agent_gate.packet_for(gate_args(args)))
    if args.format == "json":
        content = json.dumps(packet, indent=2) + "\n"
    else:
        content = render_markdown(packet)
    if args.write_packet:
        target = write_packet(args.write_packet, content)
        print(str(target.relative_to(ROOT).as_posix()))
    else:
        print(content, end="")
    return 0 if packet["hook_result"]["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
