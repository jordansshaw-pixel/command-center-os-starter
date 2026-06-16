# Project Handoff Architecture Standard

Status: Root routing standard
Date: 2026-06-06

## Purpose

This standard defines what it means for the OS project handoff architecture to be finished enough for active lanes.

Short rule:

```text
A project lane is handoff-ready only when the next role, stage or folder, memory check, blockers, and live-system boundary are explicit.
```

## Owner

Conductor owns project handoff routing, sequence, and receiving owner.

Signal owns signal structure and handoff packet completeness.

Librarian owns project handoff findability and state indexes.

Keeper owns memory judgment and required memory checks.

Steward owns truth, proof, refusal, correction, and claim-boundary gates.

Warden owns credentials, live systems, regulated data, legal/compliance exposure, and external-system hard stops.

Marshal owns deterministic field compliance.

## Operator-Facing Action

the operator may ask to continue, resume, clean up, review, build, route, or work inside a project in ordinary language.

the OS MUST determine the likely project handoff state before asking the operator what folder, stage, or owner should receive the work.

If the project handoff state is absent, stale, or conflicting, the OS MUST inspect project sources and create or update the project handoff state before movement.

## System Action

the OS MUST use this standard when:

- Work moves into or out of a project.
- Work moves between project stages.
- Work is paused before project completion.
- A future session needs project state.
- A project is active, dormant, provisional, resource, method-engine, historical, placeholder, or undecided and the status affects routing.
- A project cleanup, stale-path review, implementation handoff, live-system review, or generated artifact could otherwise proceed from chat memory.

## Required Project Handoff State

Every project lane handoff state MUST answer:

- Project:
- Status label:
- Current route:
- Default receiving owner:
- Default receiving folder or stage:
- Current next action:
- Memory check required:
- Memory destination:
- Governance or truth gate:
- Connectivity or live-system boundary:
- Blockers:
- Stop conditions:
- Last verified source:
- Last verified timestamp:
- Handoff packet required:

If any field is unknown, the state MUST say `unknown` and name the inspection needed.

## Project Status Routing Defaults

| Status | Default Route | Default Handoff Behavior |
|---|---|---|
| active project | Project `ROUTING.md`, then current stage or `CONTEXT.md` next action | Create or update project handoff state before substantial movement. |
| active resource workspace | Project `ROUTING.md`, then named resource deliverable or package lane | Avoid full project execution assumptions unless scoped. |
| active org/workspace container | Project `ROUTING.md`, then scoped sub-workspace | Review governance/connectivity before public, legal, financial, brand, or live-system use. |
| method engine | Project `ROUTING.md`, then selected external destination container | Runtime output MUST NOT land in method-engine stages unless approved destination is the method engine itself. |
| dormant opportunity | Project `CONTEXT.md`, then decision packet for activation-sensitive movement | Block implementation, live-system, client/legal, or commitment movement. |
| provisional workspace | Project `CONTEXT.md`, then source inspection | Do not promote to active project without decision packet. |
| historical reference | Reference inspection only | Do not create active handoff without approval. |
| placeholder | No active handoff | Do not scaffold or route execution without decision packet. |
| undecided | Stop | Create decision packet. |

## Project Handoff Packet Fields

Project handoff packets MUST include the base `_handoffs/HANDOFF-TEMPLATE.md` fields plus:

```text
Project handoff:
- Project:
- Project status:
- Project route:
- Receiving folder:
- Receiving stage:
- Stage contract:
- Project memory checked:
- Project memory destination:
- Project decision destination:
- Governance gate:
- Connectivity gate:
- Live-system status:
- Source boundary:
- Legacy/stale path boundary:
- Output destination:
- Current next action:
- Blockers:
- Stop conditions:
```

## Current Project Handoff State Index

The root project handoff state index is:

```text
_handoffs/PROJECT-HANDOFF-STATE.md
```

Librarian owns findability for that index.

Conductor owns route correctness.

Signal owns whether each state is signal-complete.

The index is a routing aid, not a replacement for project-local source files.

## MUST

- Project handoff architecture MUST preserve project status labels before movement.
- Project handoff architecture MUST route through project-local `ROUTING.md` and `CONTEXT.md` when present.
- Project handoff architecture MUST name the receiving owner, folder, and stage or explain why none applies.
- Project handoff architecture MUST name memory and decision destinations.
- Project handoff architecture MUST name governance and connectivity gates.
- Project handoff architecture MUST distinguish active projects, resource workspaces, org/workspace containers, method engines, dormant opportunities, provisional workspaces, placeholders, and undecided folders.
- Project handoff architecture MUST update `_handoffs/PROJECT-HANDOFF-STATE.md` when a project lane's route, blocker, or next owner changes.
- Project handoff architecture MUST create or update a handoff packet when context loss would otherwise force reconstruction from chat.

## MUST NOT

- Project handoff architecture MUST NOT treat folder existence as project activation.
- Project handoff architecture MUST NOT route runtime artifacts into a method engine unless that method engine is the selected destination container.
- Project handoff architecture MUST NOT let project-specific state live only in root handoff files when the project needs the state to operate.
- Project handoff architecture MUST NOT skip governance, memory, or connectivity gates because the receiving folder is known.
- Project handoff architecture MUST NOT ask the operator to name routine receiving folders before the OS inspects source evidence.

## Inputs

This standard accepts:

- Project resume requests.
- Project cleanup requests.
- Project handoff requests.
- Stage transition requests.
- Project status reviews.
- Future-session recovery.
- Project implementation or live-system-adjacent requests.

## Outputs

This standard produces:

- A project handoff state update.
- A project handoff packet.
- A routing signal.
- A missing-state list.
- A decision packet when project status, activation, or risk ownership is unclear.

## Acceptance Test

This standard passes when a future session can open `_handoffs/PROJECT-HANDOFF-STATE.md`, identify the project status, receiving owner, receiving folder/stage, memory destination, blockers, and next action, then continue without asking the operator to reconstruct the project route.

## Failure Test

This standard fails when project work resumes from chat memory alone, when the receiving owner or folder is implicit, when live-system boundaries are not named, when a dormant or undecided project is treated as active, or when runtime output lands in the wrong container.

## Escalation

Escalate to Conductor for routing, sequence, project status, or receiving-owner conflicts.

Escalate to Signal for incomplete signals or handoff packets.

Escalate to Keeper/Recorder/Librarian for memory, exact record, or findability gaps.

Escalate to Steward for truth, proof, claim, refusal, correction, or public/client-facing meaning.

Escalate to Warden for credentials, live systems, regulated data, legal/compliance, external systems, implementation repos, domains, DNS, automations, analytics, or client records.

Escalate to the operator only with a decision packet when project activation, risk ownership, business judgment, public/client commitment, live-system approval, or risk score 3+ requires human authority.
