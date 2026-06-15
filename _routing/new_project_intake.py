#!/usr/bin/env python3
"""Ask first-step project intake questions and scaffold an the OS project."""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


STATUS_LABELS = [
    "active project",
    "active resource workspace",
    "method engine",
    "dormant opportunity",
    "provisional workspace",
    "historical reference",
    "placeholder",
    "undecided",
]


@dataclass
class IntakeAnswers:
    timestamp: str
    display_name: str
    folder_name: str
    status: str
    purpose: str
    active_scope: str
    out_of_scope: str
    source_material: str
    known_systems: list[str]
    sensitivity: str
    first_next_work: str


def timestamp() -> str:
    raw = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    return f"{raw[:-2]}:{raw[-2:]}"


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "-", value.strip())
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-_")
    return cleaned or "NewProject"


def split_list(value: str) -> list[str]:
    if value.strip().lower() in {"", "none", "no", "n/a", "na"}:
        return []
    parts = re.split(r"[,;\n]+", value)
    return [part.strip() for part in parts if part.strip()]


def prompt(label: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    if not value and default is not None:
        return default
    return value


def choose_status() -> str:
    print("Project status labels:")
    for index, label in enumerate(STATUS_LABELS, start=1):
        print(f"  {index}. {label}")
    value = prompt("Project status", "active project")
    if value.isdigit():
        index = int(value)
        if 1 <= index <= len(STATUS_LABELS):
            return STATUS_LABELS[index - 1]
    normalized = value.strip().lower()
    if normalized in STATUS_LABELS:
        return normalized
    raise ValueError(f"Unsupported project status: {value}")


def collect_answers() -> IntakeAnswers:
    display_name = prompt("Project display name")
    if not display_name:
        raise ValueError("Project display name is required.")
    folder_name = prompt("Root folder name", slugify(display_name))
    if not re.fullmatch(r"[A-Za-z0-9_-]+", folder_name):
        raise ValueError("Folder name may contain only letters, numbers, underscores, and hyphens.")
    status = choose_status()
    purpose = prompt("Purpose")
    active_scope = prompt("Active scope")
    out_of_scope = prompt("Out-of-scope boundary", "Live systems, credentials, public/client commitments, legal/compliance, and financial movement until approved")
    source_material = prompt("Starting source material or references", "none")
    known_systems = split_list(prompt("Known live systems or external tools", "none"))
    sensitivity = prompt("Public/client/legal/compliance/financial sensitivity", "none")
    first_next_work = prompt("First next work item")
    if not purpose or not active_scope or not first_next_work:
        raise ValueError("Purpose, active scope, and first next work item are required.")
    return IntakeAnswers(
        timestamp=timestamp(),
        display_name=display_name,
        folder_name=folder_name,
        status=status,
        purpose=purpose,
        active_scope=active_scope,
        out_of_scope=out_of_scope,
        source_material=source_material,
        known_systems=known_systems,
        sensitivity=sensitivity,
        first_next_work=first_next_work,
    )


def risk_score(answers: IntakeAnswers) -> int:
    if answers.status != "active project":
        return 2
    if answers.known_systems or answers.sensitivity.strip().lower() not in {"", "none", "no", "n/a", "na"}:
        return 2
    return 2


def systems_table(answers: IntakeAnswers) -> str:
    if not answers.known_systems:
        return "| none | none | no known systems | blocked | intake | none | Any live-system action until approved |"
    rows = []
    for system in answers.known_systems:
        rows.append(
            f"| {system} | unknown | intake pointer only | reference-only | setup intake | inspect and document only | Any live-system action until approved |"
        )
    return "\n".join(rows)


def bullet_list(value: str) -> str:
    items = split_list(value)
    if not items:
        return "- none"
    return "\n".join(f"- {item}" for item in items)


def packet(answers: IntakeAnswers, action: str) -> str:
    risk = risk_score(answers)
    approval = "create-mode requested by operator" if action == "create" else "needs approval before scaffold creation"
    stop_conditions = "Live-system, credential, public/client, legal/compliance, financial, or risk score 3+ movement."
    return f"""# New Project Intake - {answers.display_name}

Timestamp: {answers.timestamp}

## Packet

New project intake:
- Timestamp: {answers.timestamp}
- Project display name: {answers.display_name}
- Root folder: `{answers.folder_name}/`
- Requested status: {answers.status}
- Purpose: {answers.purpose}
- Active scope: {answers.active_scope}
- Out of scope: {answers.out_of_scope}
- Starting source material: {answers.source_material}
- Known systems: {", ".join(answers.known_systems) if answers.known_systems else "none"}
- Public/client/legal/compliance/financial sensitivity: {answers.sensitivity}
- First next work: {answers.first_next_work}
- Recommended scaffold: root project scaffold from `_routing/project-folder-inheritance-template.md`
- Risk: {risk}
- Approval state: {approval}
- Action: {action}
- Stop conditions: {stop_conditions}
"""


def project_claude(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Project Identity

Status: {answers.status}
Date: {answers.timestamp[:10]}

## Purpose

{answers.display_name} is {answers.purpose}

## Inherits

- Root identity: `../CLAUDE.md`
- Root context: `../CONTEXT.md`
- Root routing: `../ROUTING.md`
- Root Operator Canon: `../_operator/`
- Root Brand Guardian: `../_governance/brand-guardian.md`
- Root memory: `../_memory/`
- Root connectivity: `../_connectivity/`
- Root project folder inheritance template: `../_routing/project-folder-inheritance-template.md`
- New project intake standard: `../_routing/new-project-intake-standard.md`

## Authority

This project may own:

- Project-local truth, planning, references, memory, decisions, connectivity pointers, stage work, and outputs for {answers.display_name}.

This project may not:

- Outrank root law.
- Turn project-specific truth into root law without a decision packet.
- Touch live systems without project/root connectivity review and approval.
- Treat legacy or external paths as active truth without source authority.

## Current Boundary

Active scope:

- {answers.active_scope}

Out of scope:

- {answers.out_of_scope}

## Stop Conditions

Stop when:

- Project status is undecided.
- The work requires business judgment, public/client commitment, legal/compliance, financial, live-system, credential, or risk score 3+ approval.
- Source truth conflicts with root law or project-local memory.
"""


def project_context(answers: IntakeAnswers) -> str:
    systems = ", ".join(answers.known_systems) if answers.known_systems else "none"
    return f"""# {answers.display_name} Context

Status: {answers.status}
Date: {answers.timestamp[:10]}

## Purpose

This file records current {answers.display_name} state so work does not depend on chat memory.

## Current State

{answers.display_name} was created from the the OS new project intake on {answers.timestamp}.

## Durable Facts

- Purpose: {answers.purpose}
- Active scope: {answers.active_scope}
- Starting source material: {answers.source_material}
- Known systems at intake: {systems}
- Sensitivity at intake: {answers.sensitivity}

## Constraints

- {answers.out_of_scope}
- Live-system action is blocked until project/root connectivity review and the operator approval when required.
- Credentials, secrets, tokens, private keys, payment data, recovery codes, regulated data, legal/compliance material, and private client records must not be stored in project markdown.

## Open Loops

- Confirm or refine project stage spine after the first real work item is routed.
- Inspect any starting source material before treating it as current project truth.

## Current Next Work

- {answers.first_next_work}

## Source Boundaries

Active sources:

- `setup/new-project-intake.md`
- `CLAUDE.md`
- `CONTEXT.md`
- `ROUTING.md`
- `_memory/project-memory.md`
- `_connectivity/README.md`

Historical/reference-only sources:

- {answers.source_material}

External implementation pointers:

- {systems}

## Recovery Rule

Load:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `ROUTING.md`
4. `_memory/project-memory.md`
5. `_connectivity/README.md`
6. Relevant stage `CONTRACT.md` when present
"""


def project_routing(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Routing

Status: Project-local routing
Date: {answers.timestamp[:10]}

## Purpose

This file routes {answers.display_name} work without duplicating root routing law.

## Inherits

- Root routing: `../ROUTING.md`
- Root destination map: `../_routing/destination-map.md`
- Root project folder inheritance template: `../_routing/project-folder-inheritance-template.md`
- Root project stage contract template: `../_routing/project-stage-contract-template.md`
- Root project stage spine template: `../_routing/project-stage-spine-template.md`
- Root new project intake standard: `../_routing/new-project-intake-standard.md`

## Default Destinations

| Work Type | Destination |
|---|---|
| Current project truth | `CONTEXT.md` |
| Durable project memory | `_memory/project-memory.md` |
| Project decisions | `_memory/decisions.md` |
| Governance, proof, claim, refusal, correction | `_governance/README.md` |
| Connectivity, live systems, credentials, implementation pointers | `_connectivity/README.md` |
| Stable source material | `references/` |
| Setup and intake source | `setup/` |
| Stage work | `stages/[NN_stage-name]/` |
| Stage outputs | nearest stage `output/` |

## Stage Routing

Use:

- `../_routing/project-stage-spine-template.md`
- `../_routing/project-stage-contract-template.md`

Project stage map:

- No stage contracts have been created yet. Route the first stage from current source and the project stage spine template.

## Stop Conditions

Stop when:

- Project status is undecided.
- A required inheritance source is missing and the work depends on it.
- The request would activate a dormant/provisional/placeholder workspace.
- Live-system, credential, legal/compliance, financial, public/client commitment, or risk score 3+ movement appears.

## Escalation

Escalate to Conductor for routing and sequence.

Escalate to Steward / Brand Guardian for truth, proof, claims, refusal, or correction.

Escalate to Keeper/Recorder/Librarian for memory, exact record, or findability.

Escalate to Warden for live systems and credentials.

Escalate to the operator with a decision packet when human authority is required.
"""


def governance_readme(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Governance Inheritance

Status: Project-local governance inheritance
Date: {answers.timestamp[:10]}

Contract language standard:

- `../../_routing/deterministic-contract-language-standard.md`
- `../../_routing/project-folder-inheritance-template.md`

## Purpose

This folder carries {answers.display_name} governance that inherits from root without duplicating root law.

## Inherits

- Root Operator Canon: `../../_operator/`
- Root Brand Guardian: `../../_governance/brand-guardian.md`
- Root routing: `../../ROUTING.md`
- Root memory: `../../_memory/`
- Root connectivity: `../../_connectivity/`

## Claim Boundaries

- Intake sensitivity: {answers.sensitivity}
- Public/client-facing claims require proof and approval before movement.
- Project-specific claims must stay project-local unless a decision packet approves root movement.

## Acceptance Test

This layer passes when project work can identify inherited root law, project-local truth, proof boundaries, and approval state before movement.

## Failure Test

This layer fails when root law is duplicated, project truth is generalized to root without approval, or claims move without proof/approval labels.
"""


def memory_project(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Project Memory

Status: Project-local memory
Date started: {answers.timestamp[:10]}

## Purpose

This file preserves durable {answers.display_name} state so work does not depend on chat memory.

## Inherits

- Root Memory Router: `../../_memory/MEMORY-ROUTER.md`
- Root decision source index: `../../_memory/decision-source-index.md`
- Root sync rules: `../../_memory/sync-rules.md`
- Root log rules: `../../_memory/log-rules.md`

## Current State

{answers.status}: {answers.purpose}

## Durable Facts

- Created from the OS new project intake on {answers.timestamp}.
- Active scope: {answers.active_scope}
- Starting source material: {answers.source_material}

## Durable Constraints

- {answers.out_of_scope}
- Live-system action and credentials are blocked until the connectivity packet and approval path allow movement.

## Open Loops

- {answers.first_next_work}
- Confirm stage spine after the first routed project work item.

## Memory Destinations

Use:

- `_memory/decisions.md` for project-specific decisions.
- `CONTEXT.md` for compact current state.
- Stage `output/` folders for run-specific artifacts.
"""


def decisions_log(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Decision Log

Status: Project-local decision log
Date started: {answers.timestamp[:10]}

## Purpose

This file records project-specific decisions that should survive chat and session context loss.

## Timestamp Rule

New entries MUST follow root `_memory/log-rules.md`.

Use:

```text
### YYYY-MM-DD HH:mm:ss +/-HH:MM - [Decision title]
```

## Decisions

### {answers.timestamp} - Project scaffold created from intake

Status: Source-confirmed project-local scaffold decision

Decision:

the OS created the {answers.display_name} project scaffold from the new project intake setup.

Source:

- `setup/new-project-intake.md`
- `../../_routing/new-project-intake-standard.md`

Next owner:

- Conductor for first project routing.
"""


def connectivity_readme(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Connectivity

Status: Project-local connectivity pointer
Date: {answers.timestamp[:10]}

Contract language standard:

- `../../_routing/deterministic-contract-language-standard.md`
- `../../_routing/project-folder-inheritance-template.md`

## Purpose

This folder records {answers.display_name} live-system pointers and permission boundaries without storing credentials or granting action.

## Inherits

- Root connectivity lane: `../../_connectivity/`
- Root tool permissions: `../../_connectivity/tool-permissions.md`
- Root live-system risk rules: `../../_connectivity/live-system-risk-rules.md`
- Root connectivity registry: `../../_connectivity/connectivity-registry.md`

## Owner

Warden owns live-system and credential stops.

Conductor owns project routing.

Sentinel owns risk scoring.

the operator owns live-system approval.

## Known Systems

| System | Type | Current Status | Permission Class | Source | Allowed Action | Blocked Action |
|---|---|---|---|---|---|---|
{systems_table(answers)}

## MUST

- Connectivity work MUST classify permission before action.
- Live-system changes MUST use a live-system packet before movement.
- Credentials, tokens, private keys, payment data, recovery codes, regulated data, client records, and private legal/compliance material MUST NOT be stored in this folder.
- Listed systems MUST NOT imply permission to act.

## MUST NOT

- This folder MUST NOT store secrets.
- This folder MUST NOT authorize live-system action by listing a system.
- This folder MUST NOT import old connectivity files wholesale.
- This folder MUST NOT mix another project's systems into this project.

## Required Live-System Packet

```text
Live-system packet:
- System:
- Scope:
- Requested action:
- Current source:
- Owner:
- Permission class:
- Risk score:
- Approval required:
- Approval status:
- Credential handling:
- Rollback path:
- Blocked actions:
- Allowed safe actions:
- Next action:
```

## Acceptance Test

This folder passes when every known live-system pointer has a permission class, source, allowed action, blocked action, and approval boundary.

## Failure Test

This folder fails when a known system is treated as permission to act or credentials are stored in project markdown.
"""


def setup_readme(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Setup

Status: Project setup lane
Date: {answers.timestamp[:10]}

## Purpose

This folder stores setup packets and project-start records for {answers.display_name}.

## Files

- `new-project-intake.md`: first-step intake answers used to create this project scaffold.

## Boundary

Do not store secrets, credentials, tokens, private keys, payment data, recovery codes, regulated data, legal/compliance material, or private client records here.
"""


def references_readme(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} References

Status: Project reference lane
Date: {answers.timestamp[:10]}

## Purpose

This folder stores stable source material that belongs to {answers.display_name}.

## Starting Source Material

{bullet_list(answers.source_material)}

## Boundary

References must be inspected before they become current project truth.
"""


def stages_readme(answers: IntakeAnswers) -> str:
    return f"""# {answers.display_name} Stages

Status: Project stage lane placeholder
Date: {answers.timestamp[:10]}

## Purpose

This folder will hold project stage folders after the first real work route defines the stage spine.

## Source

- Root stage spine template: `../../_routing/project-stage-spine-template.md`
- Root stage contract template: `../../_routing/project-stage-contract-template.md`

## Current State

No stage contracts have been created yet.

## Next Action

- {answers.first_next_work}
"""


def render_files(answers: IntakeAnswers) -> dict[str, str]:
    return {
        "CLAUDE.md": project_claude(answers),
        "CONTEXT.md": project_context(answers),
        "ROUTING.md": project_routing(answers),
        "_governance/README.md": governance_readme(answers),
        "_memory/project-memory.md": memory_project(answers),
        "_memory/decisions.md": decisions_log(answers),
        "_connectivity/README.md": connectivity_readme(answers),
        "setup/README.md": setup_readme(answers),
        "setup/new-project-intake.md": packet(answers, "create"),
        "references/README.md": references_readme(answers),
        "stages/README.md": stages_readme(answers),
    }


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def update_handoff_state(root: Path, answers: IntakeAnswers) -> None:
    path = root / "_handoffs" / "PROJECT-HANDOFF-STATE.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    lane = f"`{answers.folder_name}/`"
    if lane in text:
        return
    row = (
        f"| `{answers.folder_name}/` | {answers.status} | Conductor | "
        f"`{answers.folder_name}/ROUTING.md`, then scoped stage | "
        f"`{answers.folder_name}/_memory/project-memory.md` and `_memory/decisions.md` | "
        f"`{answers.folder_name}/_governance/README.md` | "
        f"`{answers.folder_name}/_connectivity/README.md` | {answers.first_next_work} | "
        "Live-system, credential, public/client, legal/compliance, financial, or risk score 3+ movement requires approval. |"
    )
    lines = text.splitlines()
    insert_at = None
    in_table = False
    for index, line in enumerate(lines):
        if line.startswith("| Lane | Status |"):
            in_table = True
            continue
        if in_table and index > 0 and not line.startswith("|"):
            insert_at = index
            break
    if insert_at is None:
        lines.append(row)
    else:
        lines.insert(insert_at, row)
    lines = [
        f"Last verified: {answers.timestamp}" if line.startswith("Last verified:") else line
        for line in lines
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def create_project(root: Path, answers: IntakeAnswers) -> Path:
    if answers.status != "active project":
        raise ValueError("Create mode only builds a full scaffold for status `active project`.")
    project = root / answers.folder_name
    if project.exists():
        raise FileExistsError(f"Project folder already exists: {project}")
    for relative_path, content in render_files(answers).items():
        write_text(project / relative_path, content)
    update_handoff_state(root, answers)
    return project


def write_packet(root: Path, answers: IntakeAnswers) -> Path:
    safe_time = answers.timestamp.replace(":", "").replace(" ", "-")
    path = root / "_intake" / "drop" / f"new-project-intake-{answers.folder_name}-{safe_time}.md"
    write_text(path, packet(answers, "hold"))
    return path


def self_test() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "_handoffs").mkdir(parents=True)
        (root / "_handoffs" / "PROJECT-HANDOFF-STATE.md").write_text(
            "# Project Handoff State\n\nLast verified: 2026-06-06 00:00:00 -05:00\n\n"
            "## Current Lane States\n\n"
            "| Lane | Status | Default Receiving Owner | Default Receiving Folder / Stage | Memory Check | Governance Gate | Connectivity Gate | Current Next Action | Blockers / Stop Conditions |\n"
            "|---|---|---|---|---|---|---|---|---|\n\n"
            "## Missing Handoff Architecture\n",
            encoding="utf-8",
        )
        answers = IntakeAnswers(
            timestamp="2026-06-06 12:00:00 -05:00",
            display_name="Example Project",
            folder_name="ExampleProject",
            status="active project",
            purpose="a test project.",
            active_scope="Test local scaffold only.",
            out_of_scope="Live systems.",
            source_material="none",
            known_systems=["GitHub"],
            sensitivity="none",
            first_next_work="Route first stage.",
        )
        project = create_project(root, answers)
        required = [
            "CLAUDE.md",
            "CONTEXT.md",
            "ROUTING.md",
            "_governance/README.md",
            "_memory/project-memory.md",
            "_memory/decisions.md",
            "_connectivity/README.md",
            "setup/new-project-intake.md",
            "references/README.md",
            "stages/README.md",
        ]
        missing = [item for item in required if not (project / item).exists()]
        state = (root / "_handoffs" / "PROJECT-HANDOFF-STATE.md").read_text(encoding="utf-8")
        if missing or "`ExampleProject/`" not in state:
            raise AssertionError(f"Self-test failed. Missing={missing}")
    print("new_project_intake.py self-test passed")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]), help="the OS root path")
    parser.add_argument("--create", action="store_true", help="Create the active project scaffold after questions")
    parser.add_argument("--packet-only", action="store_true", help="Only write an intake packet to _intake/drop")
    parser.add_argument("--self-test", action="store_true", help="Run side-effect-free self-test")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.self_test:
        self_test()
        return 0
    root = Path(args.root).resolve()
    answers = collect_answers()
    print()
    print(packet(answers, "create" if args.create else "hold"))
    if answers.status != "active project":
        path = write_packet(root, answers)
        print(f"Creation held for status `{answers.status}`. Wrote intake packet: {path}")
        return 0
    if args.packet_only:
        path = write_packet(root, answers)
        print(f"Wrote intake packet: {path}")
        return 0
    create = args.create
    if not create:
        create = prompt("Create active project scaffold now? Type yes to create", "no").lower() == "yes"
    if create:
        project = create_project(root, answers)
        print(f"Created project scaffold: {project}")
    else:
        path = write_packet(root, answers)
        print(f"Creation held. Wrote intake packet: {path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print("\nStopped.")
        raise SystemExit(130)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
