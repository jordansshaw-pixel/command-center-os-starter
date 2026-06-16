# Project Folder Inheritance Template

Status: Root routing template
Date: 2026-06-06

## Purpose

This template defines the required inheritance pattern for active OS project folders.

It is used when creating, hardening, reviewing, or repairing:

```text
[PROJECT]/
```

Short rule:

```text
Project folders inherit root law, but project truth must stay project-local unless root law is actually changing.
```

## Owner

Conductor owns project routing, sequence, status labeling, and handoff path.

Librarian owns project findability, source pointers, and index placement.

Keeper owns project memory judgment.

Steward owns truth, proof, refusal, correction, and claim boundaries.

Warden owns credentials, live systems, regulated data, legal/compliance exposure, and external-system hard stops.

Marshal owns deterministic contract compliance for project-local inheritance files.

## Operator-Facing Action

the operator may name a project, client, workspace, resource lane, method engine, or opportunity in ordinary language.

the OS MUST inspect current source evidence and classify the folder as active, partial, dormant, provisional, method engine, resource lane, historical reference, placeholder, or undecided before asking the operator to choose an internal folder structure.

If project status or activation remains ambiguous after inspection, the OS MUST provide a decision packet with a recommended default and a specific approval or override question.

## System Action

the OS MUST use this template when defining or changing project-local inheritance.

the OS MUST preserve root law as pointers and project-specific truth as project-local state.

the OS MUST NOT create project execution lanes merely because a folder exists.

## Required Project Folder Minimum

An active project folder SHOULD eventually contain:

```text
[PROJECT]/
  CLAUDE.md
  CONTEXT.md
  ROUTING.md
  _governance/
    README.md
  _memory/
    project-memory.md
    decisions.md
  _connectivity/
    README.md
  references/
  setup/
  stages/
```

`SHOULD` is deliberate:

- Active project work needs this structure.
- Dormant, provisional, resource, method-engine, historical, or undecided folders may have a smaller structure.
- Missing folders MUST be labeled as gaps, not silently treated as complete.

## Project Status Labels

Every project inheritance review MUST choose one status label:

| Label | Meaning | Default Movement |
|---|---|---|
| active project | Current work can route here. | Use full inheritance minimum before broad cleanup. |
| active resource workspace | Current resource work can route here, but not necessarily full project execution. | Add only inheritance needed for resource work. |
| method engine | Reusable method/factory source, not runtime output container. | Runtime artifacts route to selected destination workspace. |
| dormant opportunity | Preserved for possible future use, not greenlit. | Block implementation/live/client/legal movement. |
| provisional workspace | Useful but not fully validated. | Inspect source before adding structure. |
| historical reference | Reference only. | Do not create active project lanes without approval. |
| placeholder | Folder exists but no project truth is established. | Do not scaffold as active without decision. |
| undecided | Status cannot be determined from current source. | Stop with decision packet. |

## Required Inheritance Files

### `CLAUDE.md`

Purpose:

- Project-local identity and root inheritance.

MUST include:

- Project identity.
- Project status label.
- Root inheritance pointers.
- Project-local authority boundaries.
- Legacy/stale path boundary.
- Live-system stop pointer.

MUST NOT:

- Duplicate root `CLAUDE.md`.
- Treat project existence as activation.
- Import legacy assumptions without source authority.

### `CONTEXT.md`

Purpose:

- Current project state.

MUST include:

- Current status.
- Current source truth.
- Active scope.
- Durable facts.
- Constraints.
- Open loops.
- Current next work.
- External implementation pointers, if any, labeled as reference-only unless approved.

MUST NOT:

- Store credentials.
- Treat old paths, archives, or generated artifacts as active truth without source authority.
- Hide unresolved decisions.

### `ROUTING.md`

Purpose:

- Project-local routing.

MUST include:

- Project routing defaults.
- Stage map or stage-spine pointer.
- Governance, memory, connectivity, reference, output, and handoff destinations.
- Stop conditions.
- Escalation owners.

MUST NOT:

- Override root routing, Steward, memory, or live-system rules.
- Route runtime artifacts into a method-engine folder unless that folder is the approved destination.

### `_governance/README.md`

Purpose:

- Project-local governance inheritance and claim/proof boundaries.

MUST include:

- Root Steward pointer.
- Project-local truth and claim boundaries.
- Approval-required claims.
- Project-specific refusal/correction conditions.

MUST NOT:

- Duplicate root Steward law.
- Generalize project-specific claims into root law without decision packet.

### `_memory/project-memory.md`

Purpose:

- Durable project facts, constraints, state, and open loops.

MUST include:

- Current project status.
- Migration or source facts when relevant.
- Durable facts.
- Durable constraints.
- Open loops.
- Memory destinations.

MUST NOT:

- Replace root decision log.
- Write project-specific truth as root law.

### `_memory/decisions.md`

Purpose:

- Project-local decision log.

MUST include:

- Timestamp rule inherited from root `_memory/log-rules.md`.
- Compact project decisions.
- Source pointers.
- Next owner.

MUST NOT:

- Fabricate timestamps.
- Duplicate root decisions unless recording a project-local application.

### `_connectivity/README.md`

Purpose:

- Project-local live-system pointers and permission boundaries.

MUST include:

- Root `_connectivity/` inheritance.
- Known systems table when systems are known.
- Permission class.
- Source.
- Allowed action.
- Blocked action.
- Required live-system packet.
- Credential handling rule.

MUST NOT:

- Store credentials, tokens, private keys, payment data, recovery codes, regulated data, or private client records.
- Treat a listed system as permission to act.
- Import old connectivity files wholesale.

## Template: Project `CLAUDE.md`

````markdown
# [PROJECT] Project Identity

Status: [active project | active resource workspace | method engine | dormant opportunity | provisional workspace | historical reference | placeholder | undecided]
Date: [YYYY-MM-DD]

## Purpose

[PROJECT] is [project/resource/method/opportunity description].

## Inherits

- Root identity: `../CLAUDE.md`
- Root context: `../CONTEXT.md`
- Root routing: `../ROUTING.md`
- Root Operator Canon: `../_operator/`
- Root Steward: `../_governance/steward.md`
- Root memory: `../_memory/`
- Root connectivity: `../_connectivity/`
- Root project folder inheritance template: `../_routing/project-folder-inheritance-template.md`

## Authority

This project may own:

- [Project-local truth or work type]

This project may not:

- Outrank root law.
- Turn project-specific truth into root law without a decision packet.
- Touch live systems without project/root connectivity review and approval.
- Treat legacy or external paths as active truth without source authority.

## Current Boundary

Active scope:

- [Current scope]

Out of scope:

- [Excluded scope]

## Stop Conditions

Stop when:

- Project status is undecided.
- The work requires business judgment, public/client commitment, legal/compliance, financial, live-system, credential, or risk score 3+ approval.
- Source truth conflicts with root law or project-local memory.
````

## Template: Project `CONTEXT.md`

````markdown
# [PROJECT] Context

Status: [current project status]
Date: [YYYY-MM-DD]

## Purpose

This file records current [PROJECT] state so work does not depend on chat memory.

## Current State

[Compact current state.]

## Durable Facts

- [Fact with source or confidence label]

## Constraints

- [Constraint]

## Open Loops

- [Open loop]

## Current Next Work

- [Next routed item]

## Source Boundaries

Active sources:

- [Path]

Historical/reference-only sources:

- [Path]

External implementation pointers:

- [Path or URL, permission class]

## Recovery Rule

Load:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `ROUTING.md`
4. `_memory/project-memory.md` when present
5. `_connectivity/README.md` when present
6. Relevant stage `CONTRACT.md`
````

## Template: Project `ROUTING.md`

````markdown
# [PROJECT] Routing

Status: Project-local routing
Date: [YYYY-MM-DD]

## Purpose

This file routes [PROJECT] work without duplicating root routing law.

## Inherits

- Root routing: `../ROUTING.md`
- Root destination map: `../_routing/destination-map.md`
- Root project folder inheritance template: `../_routing/project-folder-inheritance-template.md`
- Root project stage contract template: `../_routing/project-stage-contract-template.md`
- Root project stage spine template: `../_routing/project-stage-spine-template.md`

## Default Destinations

| Work Type | Destination |
|---|---|
| Current project truth | `CONTEXT.md` |
| Durable project memory | `_memory/project-memory.md` |
| Project decisions | `_memory/decisions.md` |
| Governance, proof, claim, refusal, correction | `_governance/README.md` |
| Connectivity, live systems, credentials, implementation pointers | `_connectivity/README.md` |
| Stable source material | `references/` |
| Stage work | `stages/[NN_stage-name]/` |
| Stage outputs | nearest stage `output/` |

## Stage Routing

Use:

- `_routing/project-stage-spine-template.md`
- `_routing/project-stage-contract-template.md`

Project stage map:

- [Stage]

## Stop Conditions

Stop when:

- Project status is undecided.
- A required inheritance source is missing and the work depends on it.
- The request would activate a dormant/provisional/placeholder workspace.
- Live-system, credential, legal/compliance, financial, public/client commitment, or risk score 3+ movement appears.

## Escalation

Escalate to Conductor for routing and sequence.

Escalate to Steward for truth, proof, claims, refusal, or correction.

Escalate to Keeper/Recorder/Librarian for memory, exact record, or findability.

Escalate to Warden for live systems and credentials.

Escalate to the operator with a decision packet when human authority is required.
````

## Template: Project `_governance/README.md`

````markdown
# [PROJECT] Governance Inheritance

Status: Project-local governance inheritance
Date: [YYYY-MM-DD]

Contract language standard:

- `../[relative-root]/_routing/deterministic-contract-language-standard.md`
- `../[relative-root]/_routing/project-folder-inheritance-template.md`

## Purpose

This folder carries [PROJECT] governance that inherits from root without duplicating root law.

## Inherits

- Root Operator Canon: `../[relative-root]/_operator/`
- Root Steward: `../[relative-root]/_governance/steward.md`
- Root routing: `../[relative-root]/ROUTING.md`
- Root memory: `../[relative-root]/_memory/`
- Root connectivity: `../[relative-root]/_connectivity/`

## Owner

Steward owns truth, proof, refusal, correction, and claim review.

Conductor owns routing and sequence.

Sentinel owns risk scoring.

Warden owns live-system and credential stops.

the operator owns business judgment, public/client commitments, project activation, and risk score 3+ approval.

## MUST

- Project governance MUST preserve the project boundary.
- Project governance MUST label public/client-facing claims as approved, inferred, draft, historical, external, or unresolved before movement.
- Project governance MUST route approval-required claims through the named approval owner.
- Project governance MUST route live-system movement through project/root connectivity.

## MUST NOT

- Project governance MUST NOT duplicate root Steward law.
- Project governance MUST NOT generalize project-specific truth into root law without a decision packet.
- Project governance MUST NOT treat legacy, archive, external, or generated material as current truth without source authority.

## Inputs

- Project claim reviews.
- Project proof-boundary questions.
- Project identity, positioning, public/client-facing, or governance corrections.

## Outputs

- Project-local governance notes.
- Claim/proof review outcomes.
- Refusal or correction packets.
- Root governance pointers when no local override exists.

## Acceptance Test

This layer passes when project work can identify inherited root law, project-local truth, proof boundaries, and approval state before movement.

## Failure Test

This layer fails when root law is duplicated, project truth is generalized to root without approval, or claims move without proof/approval labels.

## Escalation

Escalate to Steward for truth, proof, claims, refusal, or correction.

Escalate to the operator for public/client commitments, business judgment, project activation, or risk score 3+.
````

## Template: Project `_memory/project-memory.md`

````markdown
# [PROJECT] Project Memory

Status: Project-local memory
Date started: [YYYY-MM-DD]

## Purpose

This file preserves durable [PROJECT] state so work does not depend on chat memory.

## Inherits

- Root Memory Router: `../[relative-root]/_memory/MEMORY-ROUTER.md`
- Root decision source index: `../[relative-root]/_memory/decision-source-index.md`
- Root sync rules: `../[relative-root]/_memory/sync-rules.md`
- Root log rules: `../[relative-root]/_memory/log-rules.md`

## Current State

[Current project status and scope.]

## Durable Facts

- [Fact]

## Durable Constraints

- [Constraint]

## Open Loops

- [Open loop]

## Memory Destinations

Use:

- `_memory/decisions.md` for project-specific decisions.
- `CONTEXT.md` for compact current state.
- Stage `output/` folders for run-specific artifacts.

## Acceptance Test

This memory layer passes when a future agent can load project state, constraints, open loops, and source files without asking the operator to reconstruct the project.

## Failure Test

This memory layer fails when durable project facts remain only in chat or project-specific truth is written as root law without approval.
````

## Template: Project `_memory/decisions.md`

````markdown
# [PROJECT] Decision Log

Status: Project-local decision log
Date started: [YYYY-MM-DD]

## Purpose

This file records project-specific decisions that should survive chat and session context loss.

## Timestamp Rule

New entries MUST follow root `_memory/log-rules.md`.

Use:

```text
### YYYY-MM-DD HH:mm:ss +/-HH:MM - [Decision title]
```

## Decisions

### [YYYY-MM-DD HH:mm:ss +/-HH:MM] - [Decision title]

Status:

Decision:

Source:

Next owner:
````

## Template: Project `_connectivity/README.md`

````markdown
# [PROJECT] Connectivity

Status: Project-local connectivity pointer
Date: [YYYY-MM-DD]

Contract language standard:

- `../[relative-root]/_routing/deterministic-contract-language-standard.md`
- `../[relative-root]/_routing/project-folder-inheritance-template.md`

## Purpose

This folder records [PROJECT] live-system pointers and permission boundaries without storing credentials or granting action.

## Inherits

- Root connectivity lane: `../[relative-root]/_connectivity/`
- Root tool permissions: `../[relative-root]/_connectivity/tool-permissions.md`
- Root live-system risk rules: `../[relative-root]/_connectivity/live-system-risk-rules.md`
- Root connectivity registry: `../[relative-root]/_connectivity/connectivity-registry.md`

## Owner

Warden owns live-system and credential stops.

Conductor owns project routing.

Sentinel owns risk scoring.

the operator owns live-system approval.

## Known Systems

| System | Type | Current Status | Permission Class | Source | Allowed Action | Blocked Action |
|---|---|---|---|---|---|---|
| [System] | [Type] | [Status] | [reference-only | blocked | scoped-approved] | [Source] | [Allowed action] | [Blocked action] |

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

## Escalation

Escalate to Warden and the operator before changing any live system, credential, public site, repo, domain, DNS, form, automation, analytics, payment, client data, deployment, or public content.
````

## Required Checks

Before marking project folder inheritance complete, Marshal MUST verify:

- Project status label exists.
- Root inheritance pointers exist.
- Project-local `CLAUDE.md`, `CONTEXT.md`, and `ROUTING.md` exist or absence is labeled.
- Project-local `_governance/`, `_memory/`, and `_connectivity/` exist when the project is active, or absence is labeled with status reason.
- Memory destination exists or absence is routed.
- Connectivity boundary exists or absence is routed.
- Stage template pointers exist when `stages/` exists.
- Legacy/external path boundaries are labeled.
- Live-system action is blocked unless explicitly approved.

## MUST

- Project inheritance MUST preserve the distinction between root law and project-local truth.
- Project inheritance MUST classify project status before adding active structure.
- Project inheritance MUST label missing inheritance sources as gaps.
- Project inheritance MUST keep project-specific state inside the project workspace.
- Project inheritance MUST route reusable system lessons to root memory or governance only when they actually change OS law.

## MUST NOT

- Project inheritance MUST NOT duplicate root law.
- Project inheritance MUST NOT activate a placeholder, dormant, provisional, historical, or undecided folder by scaffolding it as active without a decision.
- Project inheritance MUST NOT treat project-local connectivity pointers as permission to act.
- Project inheritance MUST NOT import legacy, archive, or external implementation assumptions as active truth without source authority.
- Project inheritance MUST NOT ask the operator to design routine folder function before the OS proposes the inheritance pattern.

## Inputs

This template accepts:

- Existing project folders.
- New project workspace requests.
- Project rehome or migration work.
- Project cleanup requests.
- Project-local scaffold repair.

## Outputs

This template produces:

- A project inheritance recommendation.
- Project-local inheritance files.
- A missing-inheritance-source list.
- A project status decision packet when status is unclear.
- A handoff to project-stage templates when stage work is next.

## Acceptance Test

This template passes when a future agent can enter a project folder, identify its status, know what root law it inherits, know what project-local truth it owns, know where memory and decisions live, know where connectivity boundaries live, and know whether stage work may proceed.

## Failure Test

This template fails when a folder appears active because files exist, root law is copied into project files, project truth is stored only in root, live-system action is implied by a pointer, or the operator is asked to choose internal folder architecture before the OS proposes a source-backed route.

## Escalation

Escalate to Conductor for project status, routing, sequence, or destination conflicts.

Escalate to Librarian for project findability, index, and source-placement gaps.

Escalate to Keeper/Recorder for memory and exact-record gaps.

Escalate to Steward for truth, proof, claims, refusal, or correction.

Escalate to Warden for credentials, live systems, regulated data, legal/compliance, external systems, or implementation pointers.

Escalate to the operator only with a decision packet when project activation, risk ownership, business judgment, public/client commitment, or risk score 3+ requires human authority.
