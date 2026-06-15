# Command Architecture Blueprint

Status: Root architecture blueprint draft
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This blueprint defines the current the OS command architecture beneath any generated interface, cockpit, map, or command surface.

Short rule:

```text
The command surface may show the architecture. It must not replace the architecture.
```

## Evidence Basis

Source-confirmed inputs:

- `CLAUDE.md`
- `CONTEXT.md`
- `ROUTING.md`
- `_operator/OPERATOR-TRUTHS.md`
- `_governance/brand-guardian.md`
- `_governance/atx-build-roadmap.md`
- `_memory/MEMORY-ROUTER.md`
- `_agents/ROLE-INDEX.md`
- `_agents/BUILD-TIME-REVIEW-STANDARD.md`
- `_routing/low-risk-fast-lane-standard.md`
- `_routing/command-surface-acceptance-standard.md`
- `_routing/architecture-map.json`
- `_connectivity/connectivity-registry.md`

## Current Architecture State

| Architecture Layer | State | Source | Notes |
|---|---|---|---|
| Root identity | Built | `CLAUDE.md` | the OS purpose and root operating law exist. |
| Current context | Built | `CONTEXT.md` | Active build focus and recovery state exist. |
| Root routing | Built, still maturing | `ROUTING.md`, `_routing/` | Load order, destination logic, risk, signal, and fast lane exist. |
| Operator Canon | Built as draft | `_operator/` | Durable truth, voice, judgment, load, and approval layers exist. |
| Brand Guardian | Built as draft | `_governance/brand-guardian.md` | Oath, proof, refusal, and correction authority exist. |
| Memory architecture | Built as draft | `_memory/` | Memory router, decision log, sync, and source improvement exist. |
| Connectivity architecture | Built as boundary, partial as operations | `_connectivity/` | Registry and permission classes exist; live throughput remains constrained. |
| Root operating roles | Built as staged roles | `_agents/ROLE-INDEX.md`, role folders | Initial contracts/stages exist for root roles and all current specialist roles. |
| Project workspace architecture | Partially built | Project folders and `CONTEXT.md` | Several lanes are wired; handoff and runtime truth coverage still vary. |
| Execution architecture | Partial | Stage contracts, build-time review, fast lane | Safe movement exists; production specialist coverage is not complete. |
| Command surface | Draft only | `_routing/architecture-map.json`, `_output/` | Generated review artifact exists; not an operational control system. |

## Layer Model

the OS uses ICM as its structural substrate.

| Layer | Function | the OS Source |
|---|---|---|
| Layer 0 | Identity, oath, operator authority | `CLAUDE.md`, `_operator/`, `_governance/brand-guardian.md` |
| Layer 1 | Routing, destination, scope, sequence | `ROUTING.md`, `_routing/` |
| Layer 2 | Role, project, and stage contracts | `_agents/`, `[PROJECT]/`, `[PROJECT]/stages/` |
| Layer 3 | Governance, memory, connectivity, proof, references | `_governance/`, `_memory/`, `_connectivity/`, `references/` |
| Layer 4 | Current outputs, drafts, generated review artifacts | `_output/`, `[PROJECT]/stages/[stage]/output/` |

MUST rule:

Layer 4 output MUST NOT become source truth unless routed back to the correct Layer 0-3 source file with approval state labeled.

## Authority Architecture

Authority flows in this order:

```text
the operator
-> Operator Canon
-> Brand Guardian / Steward
-> Conductor routing
-> Memory / risk / signal / boundary roles
-> Role or project stage execution
-> Output, handoff, memory, source improvement
```

Authority map:

| Authority | Role / Source | Owns | Does Not Own |
|---|---|---|---|
| Final human authority | the operator | Business, moral, client, live-system, legal, financial, and high-risk judgment | Routine internal classification after the OS has enough evidence |
| Operator truth | `_operator/` | the operator's durable truths, voice, judgment, load, and approval standards | Project-specific facts unless local inheritance is explicit |
| Oath and proof | Brand Guardian / Steward | Truth, meaning, proof, refusal, correction, movement authority | Everyday task dispatch |
| Routing and sequence | Conductor | Destination, load order, handoff path, operating discipline | Final truth authority |
| Memory judgment | Keeper | Which prior truth matters now | Exact archive ownership |
| Exact record | Recorder | Dates, sources, provenance, version record | Routing decision |
| Findability | Librarian | Indexes, placement, retrieval | Proof authority |
| Risk | Sentinel | Risk score, failure mode, stop condition | Final approval |
| Signal | Signal | Status, audience, next action, handoff signal | Source truth |
| Boundary | Warden | Live-system, credential, do-not-touch enforcement | Ordinary production |
| Build execution | Builder | Prototypes, tools, automation, implementation after authorization | Architecture approval, role creation, or use of queued roles |

## Source-Of-Truth Architecture

| Truth Type | Primary Source | Notes |
|---|---|---|
| Root identity | `CLAUDE.md` | Canonical Layer 0 identity. |
| Codex loader and sync pointer | `AGENTS.md` | Must point to canonical root law rather than duplicate it. |
| Current root state | `CONTEXT.md` | Recovery and active build focus. |
| Root routing | `ROUTING.md`, `_routing/` | Destination, sequence, decision packets, fast lane, generated-interface source maps. |
| Operator truth | `_operator/` | Scope, source, owner, approval state required. |
| Oath, proof, refusal, correction | `_governance/brand-guardian.md` | Brand Guardian artifact is canonical; entity applies it. |
| Memory and decisions | `_memory/` | Durable findings, decisions, indexes, source improvement. |
| Connectivity and permissions | `_connectivity/` | Pointer does not equal permission. |
| Role contracts | `_agents/[role]/CONTRACT.md` | Live role needs folder, contract, stages, handoff path. |
| Role status registry | `_agents/ROLE-STATUS.json` | Machine-readable active, queued, provisional, runtime, and invocation status for generated surfaces and validation. |
| Stage contracts | `_agents/[role]/stages/[stage]/CONTRACT.md`, `[PROJECT]/stages/[stage]/CONTRACT.md` | Stage-specific intake, judgment, output, and handoff behavior. |
| Project runtime truth | `[PROJECT]/CONTEXT.md`, `[PROJECT]/_memory/`, `[PROJECT]/_connectivity/` | If a project needs it to run, save it in the project. |
| Generated interface source | `_routing/architecture-map.json` | Interface source, not whole architecture source. |
| Command-surface acceptance | `_routing/command-surface-acceptance-standard.md` | Defines when the interface is acceptable as a review surface and what would make it misleading. |
| Generator artifact contract | `_routing/generator-artifact-contract.md` | Defines source, owner, allowed output, validation, and failure rules for generated artifacts. |
| Generated review output | `_output/` | Reviewable artifacts only. |

MUST rule:

Every durable truth MUST carry scope, source, owner, and approval state when it can affect future action.

## Routing Architecture

Default operating loop:

```text
Intake
-> Conductor classifies scope and destination
-> Keeper checks memory when relevant
-> Sentinel scores risk
-> Signal packages signal
-> Brand Guardian / Warden / the operator gates when triggered
-> Route to role, project, stage, output, memory, or stop
-> Execute only after route is clear
-> Handoff or source improvement when work matters again
```

Fast-lane exception:

```text
Intake
-> Fast-lane triage
-> If risk 0-1, reversible, internal, source-clear, and destination-clear: execute scoped internal work
-> Verify
-> Report files changed
```

MUST rule:

Fast lane MUST NOT be used for live-system, credential, legal/compliance, financial, public, client-facing, role-creation, dormant-project activation, or irreversible action.

## Project And Workspace Lane Architecture

the OS project and resource lanes are portable operating units.

Minimum active project architecture:

```text
[PROJECT]/
  CLAUDE.md
  CONTEXT.md
  ROUTING.md
  _governance/
  _memory/
  _connectivity/
  references/
  setup/
  stages/
    NN_stage-name/
      CONTRACT.md
      references/
      output/
  _handoffs/
```

Lane classes:

| Lane Class | Meaning | Examples / Current State |
|---|---|---|
| Root command | Governs the OS itself | the OS root workspace |
| Active project | Project/client workspace that must carry local runtime truth | ExampleAgency, ExampleWeb |
| Resource lane | Useful workspace/reference lane, not necessarily a client project | ExampleNotes |
| Org/workspace container | Holds organization-level material and legacy/self-client lanes | ExampleOps |
| Dormant/provisional opportunity | Future-value lane, not greenlit for active execution | ExampleService |
| Method engine | Produces methods; runtime outputs route elsewhere | ExampleFactory |
| Placeholder folder | Empty folder preserved by decision; must not be scaffolded into active truth without a new decision | ExampleVideo |

MUST rule:

Root MUST NOT become required runtime memory, workflow state, data storage, or operational authority for a project.

## Role And Stage Architecture

Active root operating roles use this spine:

```text
_agents/[role]/
  CONTRACT.md
  stages/
    01_intake/CONTRACT.md
    02_judgment/CONTRACT.md
    03_output/CONTRACT.md
    04_handoff/CONTRACT.md
```

Role status:

| Role Type | State | Notes |
|---|---|---|
| Oath / Brand Guardian | Built as Steward contract | Governs truth, proof, refusal, correction. |
| Routing / chief of staff | Built as Conductor contract | Routes sequence, destination, handoff. |
| Memory roles | Built as Keeper, Recorder, Librarian contracts | Memory relevance, exact record, findability. |
| Risk and signal | Built as Sentinel and Signal contracts | Risk scoring and signal packets. |
| Boundaries and voice | Built as Warden and Voice contracts | Live-system protection and truth-aligned voice. |
| Production specialists | Built as staged roles | Analyst, Pathfinder, Theorist, Builder, Mechanic, Marshal, Liaison, and Scout are active specialist roles with contracts and stage spines. |

MUST rule:

No named role becomes live merely because it appears in a roadmap. A live role needs a folder, contract, stage spine, and handoff path.

## Execution Gate Architecture

| Gate | Trigger | Source | Result |
|---|---|---|---|
| Operator approval gate | Business, moral, client, live-system, legal, financial, public, role creation/retirement, or high-risk judgment | `_operator/OPERATOR-APPROVAL-STANDARD.md` | Decision packet or approval request |
| Brand Guardian gate | Truth, meaning, proof, refusal, doctrine, governance, external-facing or identity-sensitive work | `_governance/brand-guardian.md` | Proceed, caveat, needs proof, correction, refuse, or escalate |
| Memory gate | Prior decisions, reusable findings, corrections, open loops, persistence | `_memory/MEMORY-ROUTER.md` | Memory check, write, source improvement, or handoff |
| Build-time review gate | Durable build, scaffold, workflow, automation, generated interface, project structure, contracts | `_agents/BUILD-TIME-REVIEW-STANDARD.md` | Review signal before current session-runner build execution |
| Fast-lane gate | Reversible internal risk 0-1 work | `_routing/low-risk-fast-lane-standard.md` | Scoped execution without full build-time review |
| Connectivity gate | Tools, permissions, credentials, live systems, external accounts | `_connectivity/` | Reference, read-only, draft, staged, live, credential, blocked |
| Project-locality gate | Project runtime truth or local operational state | `_operator/OPERATOR-TRUTHS.md`, `_memory/MEMORY-ROUTER.md` | Save in project, not root, when project needs it to run |

## Command Surface Relationship

Current command surface:

- Acceptance standard: `_routing/command-surface-acceptance-standard.md`
- Source: `_routing/architecture-map.json`
- Role status registry: `_agents/ROLE-STATUS.json`
- Generator contract: `_routing/generator-artifact-contract.md`
- Generator: `_routing/generate-architecture-wireframe.js`
- Output: `_output/2026-06-06-atx-command-center-neural-interface.html`

The command surface is currently a review artifact.

It is not yet:

- A final architecture.
- A live operational dashboard.
- A control system.
- A source of truth for project runtime state.
- A substitute for local project memory, routing, or connectivity.

MUST rule:

The command surface MUST represent source-backed architecture state. It MUST NOT create new truth by visual implication.

MUST rule:

Generator output MUST fail before rendering when required source, contract, stage, runtime, or invocation status is missing for a displayed role or role-like lens.

## Built / Partial / Missing Summary

### Built Enough To Use

- Root identity and context.
- Root routing and destination map.
- Operator Canon draft.
- Brand Guardian draft.
- Memory router and decision sources.
- Connectivity boundary rules.
- Root operating role contracts for core roles.
- Build-time review standard.
- Low-risk fast-lane standard.
- Command-surface acceptance standard.
- Generator artifact contract.
- Generated review interface source and output.

### Partial

- Project-local scaffolds and handoff lanes.
- Specialist production roles.
- Project execution architecture.
- Command surface as operator-facing interface.
- Live connectivity throughput.
- Root doctrine/brand/voice/positioning artifacts beyond Brand Guardian and Operator Canon.

### Missing Or Undecided

- ExampleVideo non-placeholder movement remains blocked unless the operator approves a new status.
- Full project handoff architecture across all active lanes.
- Production specialist contracts.
- Live operational metrics and project execution lanes.
- Final command surface naming.
- Whether generated interface should remain "Neural Interface" or be renamed "Command Surface."

## Acceptance Test

This blueprint passes when:

- It names the authority stack.
- It names source-of-truth files by truth type.
- It distinguishes architecture from command surface.
- It labels current architecture layers as built, partial, missing, or undecided.
- It defines routing, project, role, stage, and execution gate architecture.
- It avoids claiming that the cockpit/command surface is fully built.

## Failure Test

This blueprint fails when:

- It treats generated HTML as the architecture.
- It treats root as project runtime memory.
- It activates undecided projects by implication.
- It gives production specialists live authority before contracts exist.
- It hides partial or missing layers.
- It lets speed bypass proof, memory, routing, or boundary gates.

## Next Build Sequence

Recommended sequence:

1. Run a current-build stabilization audit across root, routing, governance, memory, connectivity, agent, project, and output layers.
2. Finish or clearly label draft/partial current layers before adding new layers.
3. Finish project handoff architecture for active lanes.
4. Preserve ExampleVideo as approved placeholder unless the operator approves non-placeholder movement.
5. Prove active specialist handoffs under real work before adding more named roles.
6. Add project execution lanes or command-surface expansions only after project-local truth sources can support them.

Deferred:

- Command surface naming: `Command Surface` versus current `Neural Interface`.
- Richer project execution lanes.
- New specialist role contracts beyond the current stabilization pass.

## Handoff

What did we learn?

the OS has a truth foundation, routing scaffold, memory system, role spine, and draft command surface. It does not yet have a complete execution architecture or final operator command surface. The next work should stabilize the current draft build before moving forward.

Where was it saved?

`_routing/atx-command-architecture-blueprint.md`

What remains open?

- Final name for the operator-facing command surface.
- Handoff architecture across active project/resource lanes.
- Specialist production contracts.
- Project execution lanes backed by project-local truth.
- Current-build stabilization audit across all existing layers.

Which role should pick it up next?

Conductor should route the next pass. If the next pass is command-surface acceptance tests, Builder may build only after Conductor confirms source fields and review gates.
Current correction: Builder is active as a specialist role and may receive build routing only after required review gates permit movement.
