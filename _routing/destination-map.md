# Destination Map

Status: Root destination map draft
Date: 2026-06-05

## Purpose

This file tells the OS where work belongs so findings, drafts, decisions, corrections, and project artifacts do not remain trapped in chat or drift into the wrong folder.

Root rule:

```text
Route to the source-of-truth folder first. Add pointers later only when useful.
```

## Root Destinations

| Destination | Owns |
|---|---|
| `CLAUDE.md` | Layer 0 identity, operator, purpose, high-level operating law. |
| `CONTEXT.md` | Current root state, active build focus, recovery context. |
| `ROUTING.md` | Root routing behavior and load order. |
| `_operator/` | the operator's operator truths, voice, judgment patterns, load standard, and approval standard. |
| `_intake/` | Operator drop zone for unsorted references and artifacts before classification. |
| `_governance/` | Oath, doctrine, Steward, proof, refusal, correction, brand law, voice, positioning. |
| `_routing/` | Router contracts, destination maps, routing patterns, handoff protocol. |
| `_memory/` | Memory routing, decisions, source improvement, sync rules, indexes, open loops. |
| `_connectivity/` | Tool registry, permissions, live-system boundaries, integration risk. |
| `_agents/` | Root role index, role-status registry, compact agent doctrine, operating-role contracts, specialist contracts, and agent stages. |
| `_handoffs/` | Role/session/project handoff packets and handoff log. |
| `[PROJECT]/` | Project-local identity, context, routing, references, stage work, outputs. |

## Operator Canon

Use `_operator/` for:

- `OPERATOR-TRUTHS.md`
- `OPERATOR-VOICE.md`
- `OPERATOR-JUDGMENT.md`
- `OPERATOR-LOAD-STANDARD.md`
- `OPERATOR-APPROVAL-STANDARD.md`

Operator Canon is upstream of governance. Steward inherits Operator truth and then applies proof, refusal, correction, and movement authority.

Do not put project-specific facts, client-specific claims, live-system state, or temporary drafts in `_operator/`.

## Root Governance

Use `_governance/` for:

- Steward law.
- Oath or constitution.
- Doctrine.
- Brand guide.
- Positioning canon.
- External-output review.
- Strategic drift audits.
- Root architecture research that affects OS law.

Current canonical file:

- `_governance/steward.md`

Current planning references:

- `_governance/atx-build-roadmap.md`
- `_governance/references/original-planning/planning-gap-analysis.md`
- `_governance/references/original-planning/autobot-archetype-research.md`
- `_governance/references/original-planning/icm-audience-structure-note.md`

Current source archive:

- `_governance/source-archive/2026-06-original-build/`

## Root Routing

Use `_routing/` for:

- `router-contract.md`
- `atx-command-architecture-blueprint.md`
- `command-surface-acceptance-standard.md`
- `generator-artifact-contract.md`
- `hello-command-standard.md`
- `atx_hello.py`
- `destination-map.md`
- `decision-packet.md`
- `architecture-map.json`
- `generate-architecture-wireframe.js`
- `proactive-action-standard.md`
- `low-risk-fast-lane-standard.md`
- `project-folder-inheritance-template.md`
- `new-project-intake-standard.md`
- `new_project_intake.py`
- `project-handoff-architecture-standard.md`
- `project-stage-contract-template.md`
- `project-stage-spine-template.md`
- Handoff protocol.
- Routing exceptions.
- Project routing inheritance rules.
- Stage transition rules.
- Generated human-interface source maps that describe the OS structure and routing state.
- Generator contracts and validation rules for source-backed artifact generation.

Root `ROUTING.md` is the short operating surface. `_routing/` contains the more detailed contracts.

Use `_handoffs/` for actual handoff packets and handoff logs after routing decides that work should move.

## Reference Placement

Use the nearest scope where the reference is true, reusable, and owned.

the OS, through Librarian and Conductor, should determine that scope from evidence before asking the operator. Do not ask the operator to classify a routine reference file from scratch.

Reference routing defaults:

| Reference Type | Destination |
|---|---|
| Operator truth, voice, judgment, load, or approval source | `_operator/` |
| Governance law, oath, doctrine, proof, refusal, correction, brand law, positioning, or root architecture research that affects OS law | `_governance/` |
| Routing maps, route patterns, decision packets, source maps, generator contracts, or generated-interface source truth | `_routing/` |
| Deterministic contract language, MUST/MUST NOT behavior, and anti-drift rules | `_routing/deterministic-contract-language-standard.md` |
| Memory rules, decision logs, indexes, source-improvement rules, or open loops | `_memory/` |
| Connectivity, tool permissions, credential boundaries, live-system risk, or implementation pointers | `_connectivity/` |
| Project-wide stable source material | `[PROJECT]/references/` |
| Stage-only support material | `[PROJECT]/stages/[NN_stage]/references/` when that stage has one, otherwise the project `references/` folder with a stage pointer |
| Current output, evaluation artifact, or one-run draft | Nearest `output/` folder or `_output/` when root review output is intended |

Short rule:

```text
A reference file belongs at the nearest truth scope, not the nearest convenient folder.
```

If a root-level reference is useful but does not change Operator Canon, governance, routing, memory, connectivity, or agent contracts, create a decision packet before creating a new root reference lane.

## Intake Lane

Use `_intake/` when the operator needs to put a file somewhere before the OS classifies it.

Use:

| Intake Type | Destination |
|---|---|
| Routine non-sensitive unsorted incoming files | `_intake/drop/` |

Librarian should inspect `_intake/drop/`, classify each file, update `_intake/INTAKE-INDEX.md`, and recommend move, index, hold, or decision packet.

`_intake/_classified/` is an internal holding lane for classification outcomes. It is not operator-facing.

Do not store secrets, credentials, private keys, payment data, regulated data, or live-system access material in `_intake/`.

Reference placement packet:

```text
Reference placement:
- File:
- Evidence inspected:
- Likely scope:
- Recommended destination:
- Owner:
- Approval state:
- Risk:
- Action: [place | index | hold | decision packet]
- If asking the operator, exact approval needed:
```

## Root Memory

Use `_memory/` for:

- `MEMORY-ROUTER.md`
- `memory-rules.md`
- `context-load-standard.md`
- `SESSION-BOOT-STATE.md`
- `decision-log.md`
- `source-improvement-rules.md`
- `sync-rules.md`
- Future indexes and open-loop trackers.

Memory routing split:

- Keeper: what matters.
- Recorder: what happened.
- Librarian: where it lives and how to find it.

## Root Connectivity

Use `_connectivity/` for:

- `README.md`
- `connectivity-registry.md`
- `tool-permissions.md`
- `live-system-risk-rules.md`
- Connectivity registry.
- Tool permissions.
- Live-system risk rules.
- Credential handling rules.
- External implementation pointers.

Do not store secrets in the OS markdown files.

## Agent Contracts

Use `_agents/[role]/doctrine/*.md` for compact role jurisdiction loaded during ordinary routing.

Use `_agents/[role]/CONTRACT.md` for roles that need a lived ICM operating room.

Use `_agents/[role]/stages/[stage]/CONTRACT.md` for the role's internal workflow:

- `01_intake`
- `02_judgment`
- `03_output`
- `04_handoff`

Initial root operating contracts now exist for:

- `steward` for oath / Steward embodiment.
- `conductor` for routing and handoff.
- `keeper` for memory judgment.
- `recorder` for exact record.
- `librarian` for findability.
- `sentinel` for risk.
- `signal` for signal packets.
- `warden` for hard boundaries.
- `voice` for voice/tone under Steward.

Do not build every specialist role folder merely because the role map exists. Specialist contracts should follow after the root operating contracts prove the pattern.

Do not replace role contracts with doctrine-only authority. Doctrine is the lean runtime pointer; contracts and stage contracts remain the deeper source when the role executes, edits durable source truth, or compact doctrine is insufficient.

## Project Folders

Active project folders should eventually contain:

- `CLAUDE.md`
- `CONTEXT.md`
- `ROUTING.md`
- `_governance/`
- `_memory/`
- `_connectivity/`
- `references/`
- `setup/`
- `stages/`

Project-local governance, memory, and connectivity should inherit from root. They should not duplicate root law unless declaring local overrides.

Project-specific operational findings, planning outputs, implementation state, connectivity facts, live-system boundaries, decisions, open loops, and stage truth belong inside the project workspace when the project needs them to operate. Root may keep command-center reference analysis that overlaps with projects, including gap analysis, but root must not become a required data or workflow dependency for a movable project.

## Current Project Status

| Folder | Status | Routing Rule |
|---|---|---|
| `ExampleAgency/` | Active material exists. | Do stale path cleanup only after root law exists. |
| `ExampleWeb/` | Active material exists. | Do stale path cleanup only after root law exists. |
| `ExampleNotes/` | Active the OS resource workspace. | Work from this the OS lane for the operator's your community resource / Clief Notes material; do not route new work back to `C:\ExampleLegacy\Clief Notes`. |
| `ExampleVideo/` | Placeholder. | Preserve as empty placeholder; do not create active structure without a new the operator decision. |
| `ExampleOps/` | Active the OS org/workspace container. | Holds migrated ExampleOps org material and `client-workspace/`; review before public brand, legal, finance, live-system, or current-business use. |
| `ExampleService/` | Dormant/provisional opportunity workspace. | Not greenlit; preserve for future value, but block implementation/live/client/legal moves until approval. |
| `ExampleFactory/` | Active the OS method-engine workspace. | Use as factory/method engine only; runtime outputs belong in the selected destination container. |

## Stale Path Rule

Legacy paths are reference material unless marked active:

- `C:\ExampleLegacy`
- `CLIENTS/...`
- `ExampleOps/...`
- `C:\Dev`
- restored archive material

When cleanup begins, mark old paths as:

- Historical reference.
- External implementation pointer.
- Stale assumption to remove.
- Active dependency, if the operator confirms it.

## When Destination Is Unclear

Ask for judgment only if a reasonable default would risk durable confusion and saved memory does not already answer the question.

Use a decision packet before asking. Preferred specific question:

```text
Should this become root law, project-local context, or a working output for this pass?
```
