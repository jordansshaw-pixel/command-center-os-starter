# Role Index


Status: Root role index
Date: 2026-06-05

## Purpose

This file makes the OS roles findable and routable.

Machine-readable role status lives in:

- `_agents/ROLE-STATUS.json`

Compact role-selection triggers live in:

- `_agents/ROLE-INVOCATION-MATRIX.md`

Role utilization evidence lives in:

- `_agents/ROLE-UTILIZATION.md`

Short rule:

```text
No agent should be only a name in a roadmap. A live role needs a folder, a contract, stages, and a handoff path.
```

Utilization rule:

```text
Availability is not utilization. the OS must use the invocation matrix to promote triggered active roles without loading every role contract by default.
```

## Load Order For Role Work

Before invoking or editing a role:

1. Load Runtime Tier 0 (`CLAUDE.md`, `CONTEXT.md`, `SESSION-BOOT-STATE.md`, `ROUTING-KERNEL.md`, `ROUTE-INDEX.md`, `MEMORY-KERNEL.md`, `LOAD-INDEX.md`). Do not load `_memory/context-load-standard.md` by default — it is a long canonical source, not a boot file.
2. Load `_governance/steward.md` when truth, proof, refusal, brand, voice, doctrine, or durable law is involved.
3. Load `_memory/MEMORY-ROUTER.md` when memory relevance may affect role routing.
4. Load `_memory/decision-source-index.md` or `_memory/decision-log.md` only when a specific prior decision must be checked.
5. Load this role index.
6. Load the specific role `CONTRACT.md`.
7. Load the relevant role stage `CONTRACT.md` when work is inside that role's workflow.

## Standard Agent Stage Spine

Active root operating roles use this staged ICM structure:

```text
_agents/[role]/
  CONTRACT.md
  doctrine/
    [jurisdiction].md
  stages/
    01_intake/CONTRACT.md
    02_judgment/CONTRACT.md
    03_output/CONTRACT.md
    04_handoff/CONTRACT.md
```

Stage meanings:

| Stage | Meaning |
|---|---|
| `01_intake` | Receive work and load required context. |
| `02_judgment` | Apply the role's authority, checks, and constraints. |
| `03_output` | Produce the role-specific artifact. |
| `04_handoff` | Move work to the next owner, folder, memory destination, or the operator. |

## Agent Doctrine

Agent doctrine files carry compact jurisdictional source rules for runtime use.

Short rule:

```text
Route cards select the role. The invoked role loads only its own doctrine when that jurisdiction is triggered.
```

Doctrine files MUST stay compact and point to canonical root/archive sources instead of copying full manuals.

## Active Root Operating Roles

The role-status registry MUST mark these as `active-root-operating-role` only while the listed folders, contracts, stages, and handoff paths exist.

| Role | Folder | Core Function | Status |
|---|---|---|---|
| Steward | `_agents/steward/` | Oath, Steward embodiment, truth/refusal authority | Initial contract plus stages |
| Conductor | `_agents/conductor/` | Chief of Staff, routing, sequence, handoff | Initial contract plus stages |
| Keeper | `_agents/keeper/` | Memory judgment and continuity | Initial contract plus stages |
| Recorder | `_agents/recorder/` | Exact record and source trace | Initial contract plus stages |
| Librarian | `_agents/librarian/` | Library, index, findability | Initial contract plus stages |
| Sentinel | `_agents/sentinel/` | Risk and tactical coherence — mandatory gate, fires on all non-trivial work | Initial contract, `RISK-STANDARD.md`, plus stages |
| Warden | `_agents/warden/` | Hard boundaries and live-system protection | Initial contract plus stages |
| Voice | `_agents/voice/` | Voice, tone, culture translation | Initial contract plus stages |

## Active Specialist Roles

The role-status registry MUST mark these as `active-specialist-role` only while the listed folders, contracts, stages, and handoff paths exist.

| Role | Folder | Core Function | Status |
|---|---|---|---|
| Analyst | `_agents/analyst/` | Evidence architecture, source confidence, research clarity | Initial specialist contract plus stages |
| Pathfinder | `_agents/pathfinder/` | Boundary architecture, operating cover, safe movement envelopes | Initial specialist contract plus stages |
| Theorist | `_agents/theorist/` | Model coherence, theory, abstraction risk, impractical-elegance review | Initial specialist contract plus stages |
| Builder | `_agents/builder/` | Build, prototype, tooling, workflow, automation, implementation | Initial specialist contract plus stages |
| Mechanic | `_agents/mechanic/` | Repair, diagnosis, failure analysis, process correction | Initial specialist contract plus stages |
| Marshal | `_agents/marshal/` | Protocol, rules-as-written enforcement, checklist compliance | Initial specialist contract plus stages |
| Liaison | `_agents/liaison/` | Human/client intake, messenger signal, close-to-ground context | Initial specialist contract plus stages |
| Scout | `_agents/scout/` | Field context, terrain, reconnaissance, environmental truth | Initial specialist contract plus stages |
| Signal | `_agents/signal/` | Signal packets and communication state — service role, no stop or truth authority | Initial specialist contract, `SIGNAL-STANDARD.md`, plus stages |

## Queued Specialist Roles

No roadmap-settled specialist roles remain queued after the all-agents build pass.

Current correction:

```text
Analyst, Pathfinder, Theorist, Builder, Mechanic, Marshal, Liaison, and Scout are now active specialist roles because their folders, contracts, stage spines, and handoff paths exist.
Any future queued role MUST be built before it is used.
```

Queued-role rule:

```text
A queued specialist may be displayed as queued, but MUST NOT be invoked, assigned ownership, routed execution, or treated as available until its folder, CONTRACT.md, stage spine, handoff path, and active role-index status exist.
```

The role-status registry MUST mark queued specialists as `queued-specialist` with `invocationStatus` set to `not-invokable`.

## Build-Time Review Layers

Source standard:

- `_agents/BUILD-TIME-REVIEW-STANDARD.md`

Architect is not a separate named operating role yet.

Architectural review is a build-time layer served by:

| Function | Role | What It Checks |
|---|---|---|
| Operating architecture | Conductor | Sequence, routing, destination, handoff path, and whether the work belongs in the current build pass. |
| Evidence/source check | Analyst | What is knowable, what proof exists, what assumptions need source support, and whether the model fits reality. |
| Boundary architecture | Pathfinder | Protective space, operating cover, boundary design, and whether the structure lets the system move safely. |
| Theory/model coherence | Theorist | The underlying model, abstraction risk, coherence, and whether the structure is elegant but impractical. |

Engineering/build execution is handled by Builder after Conductor routes the work and required review gates permit movement.

Do not create `_agents/architect/` or `_agents/engineer/` unless the operator later approves a new named role with its own contract, stages, and handoff path.

Repair routes to Mechanic.

Protocol and rules-as-written enforcement route to Marshal.

Human/client intake and messenger signal route to Liaison.

Field context and reconnaissance route to Scout.

## Handoff Rule

Role handoffs should use `_handoffs/HANDOFF-TEMPLATE.md`.

Every substantial handoff should identify:

- Active agent.
- Active stage.
- Source role.
- Receiving role.
- Work state.
- Files touched or reviewed.
- Decision status.
- Risk status.
- Memory impact.
- Next action.

## Stage Framework Sources

- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`
- `_agents/_templates/AGENT-STAGE-CONTRACT-TEMPLATE.md`

## Runner Visibility

When a role or stage is invoked, surface:

```text
[Active agent / Active stage]
```

Examples:

- `[Conductor / 01_intake]`
- `[Sentinel / 02_judgment]`
- `[Signal / 03_output]`
- `[Warden / 04_handoff]`
