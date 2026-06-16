#!/usr/bin/env python3

"""Deterministic gate for the OS multi-agent engagement packets.

This tool validates and routes. It does not perform agent judgment.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ROLE_STATUS_PATH = ROOT / "_agents" / "ROLE-STATUS.json"
STANDARD_PATH = ROOT / "_routing" / "multi-agent-engagement-standard.md"


ROLE_SETS: dict[str, dict[str, list[str]]] = {
    "infrastructure": {
        "required": [
            "Conductor",
            "Analyst",
            "Pathfinder",
            "Theorist",
            "Marshal",
            "Keeper",
            "Steward",
            "Librarian",
        ],
        "optional": ["Sentinel", "Signal", "Mechanic", "Scout"],
        "boundaries": [
            "routing",
            "memory judgment",
            "truth authority",
            "evidence/source confidence",
            "boundary/live-system protection",
            "protocol/rules-as-written",
            "model coherence",
            "findability/indexing",
            "build/execution",
        ],
    },
    "build": {
        "required": ["Conductor", "Analyst", "Pathfinder", "Theorist", "Sentinel", "Signal"],
        "optional": ["Warden", "Marshal", "Mechanic", "Scout"],
        "boundaries": [
            "routing",
            "evidence/source confidence",
            "boundary/live-system protection",
            "model coherence",
            "risk",
            "signal/handoff",
            "build/execution",
        ],
    },
    "context-bleed": {
        "required": ["Conductor", "Keeper", "Recorder", "Librarian", "Marshal", "Steward"],
        "optional": ["Mechanic"],
        "boundaries": [
            "routing",
            "memory judgment",
            "truth authority",
            "exact record",
            "findability/indexing",
            "protocol/rules-as-written",
            "repair/failure analysis",
        ],
    },
    "generated-interface": {
        "required": ["Conductor", "Analyst", "Librarian", "Marshal", "Signal"],
        "optional": ["Steward", "Builder"],
        "boundaries": [
            "routing",
            "evidence/source confidence",
            "findability/indexing",
            "protocol/rules-as-written",
            "signal/handoff",
            "truth authority",
            "build/execution",
        ],
    },
    "connectivity": {
        "required": ["Conductor", "Warden", "Sentinel", "Signal", "Steward"],
        "optional": ["Analyst", "Librarian", "Builder"],
        "boundaries": [
            "routing",
            "boundary/live-system protection",
            "risk",
            "signal/handoff",
            "truth authority",
            "evidence/source confidence",
            "findability/indexing",
            "build/execution",
        ],
    },
    "role-change": {
        "required": ["Conductor", "Marshal", "Steward", "Keeper", "Librarian"],
        "optional": ["Analyst", "Theorist", "Signal"],
        "boundaries": [
            "routing",
            "protocol/rules-as-written",
            "truth authority",
            "memory judgment",
            "findability/indexing",
            "evidence/source confidence",
            "model coherence",
            "signal/handoff",
        ],
    },
    "role-utilization": {
        "required": [
            "Conductor",
            "Marshal",
            "Keeper",
            "Librarian",
            "Mechanic",
            "Theorist",
            "Analyst",
            "Signal",
        ],
        "optional": [
            "Sentinel",
            "Steward",
            "Pathfinder",
            "Recorder",
            "Builder",
            "Warden",
            "Scout",
            "Liaison",
            "Voice",
        ],
        "boundaries": [
            "routing",
            "protocol/rules-as-written",
            "memory judgment",
            "findability/indexing",
            "repair/failure analysis",
            "model coherence",
            "evidence/source confidence",
            "signal/handoff",
        ],
    },
    "research": {
        "required": ["Analyst", "Conductor"],
        "optional": ["Steward", "Scout", "Keeper", "Librarian"],
        "boundaries": [
            "evidence/source confidence",
            "routing",
            "truth authority",
            "field/human context",
            "memory judgment",
            "findability/indexing",
        ],
    },
}


INFERENCE_RULES: list[tuple[str, list[str]]] = [
    ("context-bleed", ["context bleed", "session boundary", "context loss", "finalization drift"]),
    ("connectivity", ["credential", "secret", "live-system", "live system", "dns", "deployment", "crm"]),
    ("generated-interface", ["interface", "neural", "generated", "html", "source map"]),
    (
        "role-utilization",
        [
            "role utilization",
            "agent utilization",
            "agent engagement",
            "routing bloat",
            "context bloat",
            "wiring",
            "4 or 5",
            "four or five",
            "skipped role",
            "skipped agent",
        ],
    ),
    ("infrastructure", ["infrastructure", "hook", "script", "validator", "python", "orchestration"]),
    ("build", ["build", "prototype", "scaffold", "automation", "implementation"]),
    ("role-change", ["agent", "role", "contract", "stage", "skill invocation"]),
    ("research", ["research", "evidence", "source confidence", "analyst"]),
]


ROLE_TRIGGER_RULES: dict[str, list[str]] = {
    "Steward": ["truth", "proof", "oath", "refusal", "steward", "governance", "public meaning"],
    "Keeper": ["memory", "prior decision", "continuity", "context budget", "no-load"],
    "Recorder": ["exact record", "provenance", "timeline", "audit reconstruction", "timestamp"],
    "Librarian": ["findability", "index", "retrieval", "source map", "pointer"],
    "Sentinel": ["risk", "failure mode", "blast radius", "stop condition"],
    "Signal": ["signal", "handoff", "packet", "runner visibility"],
    "Warden": ["credential", "secret", "live-system", "live system", "permission", "external account"],
    "Voice": ["voice", "tone", "phrasing", "operator-aligned language"],
    "Analyst": ["evidence", "assumption", "source confidence", "research", "proof path", "knowable"],
    "Pathfinder": ["boundary", "operating cover", "safe movement", "workspace separation", "project separation"],
    "Theorist": ["model", "abstraction", "taxonomy", "theory", "coherence", "impractical"],
    "Builder": ["implementation patch", "script change", "generator change", "build handoff"],
    "Mechanic": ["failure", "broken process", "repair", "diagnosis", "drift", "skipped role", "skipped agent"],
    "Marshal": ["rules-as-written", "contract", "deterministic", "compliance", "checklist"],
    "Liaison": ["client intake", "human context", "messenger", "client-facing ask"],
    "Scout": ["field context", "terrain", "environmental truth", "real-world"],
}


def load_role_status() -> dict[str, Any]:
    with ROLE_STATUS_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def role_index(role_status: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {role["title"].lower(): role for role in role_status.get("roles", [])}


def infer_work_type(request: str) -> str:
    text = request.lower()
    for work_type, markers in INFERENCE_RULES:
        if any(marker in text for marker in markers):
            return work_type
    return "infrastructure"


def triggered_roles_for(request: str, seed_roles: list[str]) -> list[str]:
    text = request.lower()
    triggered: list[str] = []
    for role, markers in ROLE_TRIGGER_RULES.items():
        if role in seed_roles:
            continue
        if any(marker in text for marker in markers):
            triggered.append(role)
    return triggered


def merge_role_names(seed_roles: list[str], triggered_roles: list[str]) -> list[str]:
    merged: list[str] = []
    for role in [*seed_roles, *triggered_roles]:
        if role not in merged:
            merged.append(role)
    return merged


def validate_roles(names: list[str], roles_by_name: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    results = []
    for name in names:
        role = roles_by_name.get(name.lower())
        if not role:
            results.append({"name": name, "ok": False, "reason": "missing from ROLE-STATUS.json"})
            continue
        ok = role.get("invocationStatus") == "invokable-as-role"
        missing_paths = []
        doctrine_paths = doctrine_paths_for(role)
        missing_doctrine_paths = []
        for key in ["folderPath", "contractPath"]:
            value = role.get(key)
            if value and not (ROOT / value).exists():
                missing_paths.append(value)
        for value in role.get("stagePaths", []):
            if not (ROOT / value).exists():
                missing_paths.append(value)
        for value in doctrine_paths:
            if not (ROOT / value).exists():
                missing_doctrine_paths.append(value)
        if missing_paths:
            ok = False
        if missing_doctrine_paths:
            ok = False
        results.append(
            {
                "name": role.get("title", name),
                "ok": ok,
                "truthStatus": role.get("truthStatus"),
                "invocationStatus": role.get("invocationStatus"),
                "missingPaths": missing_paths,
                "doctrinePaths": doctrine_paths,
                "missingDoctrinePaths": missing_doctrine_paths,
            }
        )
    return results


def role_is_active_or_invokable(role: dict[str, Any]) -> bool:
    truth_status = str(role.get("truthStatus", ""))
    return truth_status.startswith("active-") or role.get("invocationStatus") == "invokable-as-role"


def validate_registry() -> dict[str, Any]:
    role_status = load_role_status()
    roles_by_name = role_index(role_status)
    role_names = [
        role.get("title", "")
        for role in role_status.get("roles", [])
        if role.get("title") and role_is_active_or_invokable(role)
    ]
    results = validate_roles(role_names, roles_by_name)
    failures = [item for item in results if not item["ok"]]
    return {
        "registry_validation": {
            "Status": "pass" if not failures else "block",
            "Role status path": ROLE_STATUS_PATH.relative_to(ROOT).as_posix(),
            "Roles checked": len(results),
            "Failures": failures,
        }
    }


def render_registry_validation_report(packet: dict[str, Any]) -> str:
    validation = packet["registry_validation"]
    failures = validation["Failures"]
    lines = [
        f"the OS registry validation: {validation['Status']}",
        f"Role status path: {validation['Role status path']}",
        f"Roles checked: {validation['Roles checked']}",
    ]
    if failures:
        lines.append("Failures:")
        for item in failures:
            lines.append(f"- {item['name']}")
            if item.get("invocationStatus") != "invokable-as-role":
                lines.append(f"  invocationStatus: {item.get('invocationStatus')}")
            for path in item.get("missingPaths", []):
                lines.append(f"  missing path: {path}")
            for path in item.get("missingDoctrinePaths", []):
                lines.append(f"  missing doctrine path: {path}")
    return "\n".join(lines) + "\n"


def doctrine_paths_for(role: dict[str, Any]) -> list[str]:
    configured = role.get("doctrinePaths")
    if configured:
        return list(configured)
    folder = role.get("folderPath")
    if not folder:
        return []
    doctrine_dir = ROOT / folder / "doctrine"
    if not doctrine_dir.exists():
        return [f"{folder}/doctrine/*.md"]
    paths = sorted(doctrine_dir.glob("*.md"))
    if not paths:
        return [f"{folder}/doctrine/*.md"]
    return [path.relative_to(ROOT).as_posix() for path in paths]


def source_files_for(work_type: str) -> list[str]:
    base = [
        "CLAUDE.md",
        "CONTEXT.md",
        "ROUTING.md",
        "_routing/multi-agent-engagement-standard.md",
        "_agents/ROLE-INDEX.md",
        "_agents/ROLE-STATUS.json",
        "_agents/ROLE-INVOCATION-MATRIX.md",
    ]
    if work_type in {"infrastructure", "build", "role-change", "role-utilization", "generated-interface"}:
        base.extend(["_agents/BUILD-TIME-REVIEW-STANDARD.md", "_routing/router-contract.md"])
    if work_type == "role-utilization":
        base.extend(["_agents/ROLE-UTILIZATION.md", "_agents/AGENT-RUN-LOG.md"])
    if work_type == "connectivity":
        base.extend(["_connectivity/README.md", "_connectivity/connectivity-registry.md"])
    return base


def packet_for(args: argparse.Namespace) -> dict[str, Any]:
    if not STANDARD_PATH.exists():
        raise FileNotFoundError(f"missing standard: {STANDARD_PATH}")
    role_status = load_role_status()
    roles_by_name = role_index(role_status)
    work_type = args.work_type or infer_work_type(args.request)
    if work_type not in ROLE_SETS:
        raise ValueError(f"unknown work type: {work_type}")
    role_set = ROLE_SETS[work_type]
    seed_required = role_set["required"]
    triggered_promotions = triggered_roles_for(args.request, seed_required)
    required_names = merge_role_names(seed_required, triggered_promotions)
    optional_names = [name for name in role_set["optional"] if name not in required_names]
    required_validation = validate_roles(required_names, roles_by_name)
    optional_validation = validate_roles(optional_names, roles_by_name)
    missing_required = [item for item in required_validation if not item["ok"]]
    doctrine_source_files = sorted(
        {
            path
            for item in required_validation
            if item["ok"]
            for path in item.get("doctrinePaths", [])
        }
    )
    risk = args.risk
    if risk is None:
        default_risk = {
            "build": 2,
            "connectivity": 4,
            "context-bleed": 2,
            "generated-interface": 2,
            "infrastructure": 2,
            "research": 1,
            "role-change": 2,
            "role-utilization": 2,
        }
        risk = default_risk[work_type]
    build_allowed = bool(args.build_handoff_approved and not missing_required)
    required_agents = [item["name"] for item in required_validation if item["ok"]]
    agent_packets = [
        {
            "Agent": item["name"],
            "Stage": "02_judgment",
            "Scope": args.scope,
            "Doctrine sources": item.get("doctrinePaths", []),
            "Contract escalation": "Load full CONTRACT.md only when route risk, source edit, primary execution, or compact doctrine gap requires it.",
            "Finding": "TBD by agent judgment; deterministic gate does not decide this field.",
            "Evidence": "TBD by agent judgment or cited source inspection.",
            "Constraint": "Stay within role doctrine, role contract when escalated, and engagement scope.",
            "Recommendation": "TBD by agent judgment.",
            "Required downstream owner": "Conductor",
            "Handoff": "Return packet to Conductor synthesis.",
        }
        for item in required_validation
        if item["ok"]
    ]
    return {
        "multi_agent_engagement": {
            "Trigger": args.trigger,
            "Scope": args.scope,
            "Workspace": args.workspace,
            "Work type": work_type,
            "Risk": risk,
            "Authority boundaries crossed": role_set["boundaries"],
            "Required agents": required_agents,
            "Optional agents": [item["name"] for item in optional_validation if item["ok"]],
            "Triggered role promotions": triggered_promotions,
            "Source files": source_files_for(work_type),
            "Doctrine source files": doctrine_source_files,
            "Expected outputs": [
                "multi-agent engagement packet",
                "separate agent packets",
                "Conductor synthesis",
            ],
            "Synthesis owner": "Conductor",
            "Memory impact": args.memory_impact,
            "Stop condition": "Stop if required role is missing, non-invokable, or missing doctrine/contract/stage path.",
            "Build handoff allowed": "yes" if build_allowed else "no",
        },
        "validation": {
            "requiredRoles": required_validation,
            "optionalRoles": optional_validation,
            "missingRequired": missing_required,
            "standardPath": STANDARD_PATH.relative_to(ROOT).as_posix(),
            "roleStatusPath": ROLE_STATUS_PATH.relative_to(ROOT).as_posix(),
        },
        "agent_packets": agent_packets,
        "engagement_synthesis": {
            "Trigger resolved": "TBD by Conductor after agent packets are complete.",
            "Required agents completed": [],
            "Conflicts": [],
            "Decision": "TBD by Conductor.",
            "Build/no-build": "build allowed" if build_allowed else "no build handoff from gate alone",
            "Files to change": [],
            "Open risks": [],
            "Memory action": args.memory_impact,
            "Next owner": "Conductor",
        },
    }


def render_markdown(packet: dict[str, Any]) -> str:
    engagement = packet["multi_agent_engagement"]
    lines = ["# Multi-Agent Engagement Packet", ""]
    for key, value in engagement.items():
        if isinstance(value, list):
            lines.append(f"- {key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Agent Packet Skeletons")
    for agent_packet in packet["agent_packets"]:
        lines.append("")
        lines.append(f"### {agent_packet['Agent']}")
        for key, value in agent_packet.items():
            if isinstance(value, list):
                lines.append(f"- {key}:")
                for item in value:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Validation")
    missing = packet["validation"]["missingRequired"]
    lines.append(f"- Missing required roles: {len(missing)}")
    lines.append(f"- Build handoff allowed: {engagement['Build handoff allowed']}")
    lines.append(f"- Doctrine sources traced: {len(engagement['Doctrine source files'])}")
    return "\n".join(lines) + "\n"


def run_self_test() -> int:
    scenarios = [
        ("build python hook infrastructure", "infrastructure", ["Conductor", "Analyst", "Pathfinder"]),
        ("context bleed finalization drift", "context-bleed", ["Recorder", "Marshal"]),
        ("generated neural interface update", "generated-interface", ["Signal", "Librarian"]),
        ("credential live system check", "connectivity", ["Warden", "Sentinel"]),
        ("agent utilization routing bloat skipped role pattern", "role-utilization", ["Mechanic", "Theorist"]),
    ]
    for request, expected_type, expected_roles in scenarios:
        args = argparse.Namespace(
            request=request,
            work_type=None,
            trigger="self-test",
            scope="self-test",
            workspace="root",
            risk=None,
            memory_impact="check",
            build_handoff_approved=False,
        )
        packet = packet_for(args)
        actual_type = packet["multi_agent_engagement"]["Work type"]
        if actual_type != expected_type:
            print(f"FAIL inferred {actual_type!r}, expected {expected_type!r}", file=sys.stderr)
            return 1
        actual_roles = set(packet["multi_agent_engagement"]["Required agents"])
        for role in expected_roles:
            if role not in actual_roles:
                print(f"FAIL missing expected role {role!r} for {expected_type}", file=sys.stderr)
                return 1
        doctrine_sources = packet["multi_agent_engagement"]["Doctrine source files"]
        if not doctrine_sources:
            print(f"FAIL no doctrine sources traced for {expected_type}", file=sys.stderr)
            return 1
        for agent_packet in packet["agent_packets"]:
            if not agent_packet["Doctrine sources"]:
                print(f"FAIL missing doctrine source on {agent_packet['Agent']}", file=sys.stderr)
                return 1
        if packet["multi_agent_engagement"]["Build handoff allowed"] != "no":
            print("FAIL build handoff should default to no", file=sys.stderr)
            return 1
    registry_packet = validate_registry()
    if registry_packet["registry_validation"]["Failures"]:
        print("FAIL registry validation mode found failures", file=sys.stderr)
        print(render_registry_validation_report(registry_packet), file=sys.stderr, end="")
        return 1
    print("PASS self-test")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a deterministic the OS multi-agent engagement packet.")
    parser.add_argument("--request", default="", help="Plain-language request to classify.")
    parser.add_argument("--work-type", choices=sorted(ROLE_SETS), help="Override deterministic work type.")
    parser.add_argument("--trigger", default="request crosses multi-agent engagement trigger", help="Trigger summary.")
    parser.add_argument("--scope", default="root", help="Engagement scope.")
    parser.add_argument("--workspace", default="root", help="Workspace label.")
    parser.add_argument("--risk", type=int, choices=range(0, 5), help="Sentinel risk score override.")
    parser.add_argument("--memory-impact", default="check", choices=["none", "check", "write", "update-source"])
    parser.add_argument("--build-handoff-approved", action="store_true", help="Mark build handoff allowed if roles validate.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    parser.add_argument("--self-test", action="store_true", help="Run built-in deterministic checks.")
    parser.add_argument("--validate-registry", action="store_true", help="Validate every active/invokable role path in ROLE-STATUS.json.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        return run_self_test()
    if args.validate_registry:
        packet = validate_registry()
        print(render_registry_validation_report(packet), end="")
        return 0 if not packet["registry_validation"]["Failures"] else 2
    packet = packet_for(args)
    if packet["validation"]["missingRequired"]:
        status = 2
    else:
        status = 0
    if args.format == "json":
        print(json.dumps(packet, indent=2))
    else:
        print(render_markdown(packet), end="")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
