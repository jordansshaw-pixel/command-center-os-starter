# Project Stage Contract Template


Status: Root routing template
Date: 2026-06-06

## Purpose

This template defines the required structure for project stage contracts at:

```text
[PROJECT]/stages/[NN_stage-name]/CONTRACT.md
```

Short rule:

```text
A project stage is usable only when its contract defines what may enter, what must be judged, what may leave, and who owns the next movement.
```

## Owner

Conductor owns project-stage routing, sequencing, and handoff discipline.

Marshal owns deterministic contract compliance.

Steward owns truth, proof, refusal, correction, and public/client-facing claim boundaries.

Keeper owns memory judgment for durable project findings and decisions.

Librarian owns findability and source/index pointers.

Warden owns hard stops for credentials, live systems, regulated data, legal/compliance exposure, and external-system changes.

## Operator-Facing Action

the operator may request project work in ordinary language.

the OS MUST classify the request into the likely project and stage before asking the operator to choose an internal folder, taxonomy, or stage destination.

If classification remains ambiguous after source inspection, the OS MUST provide a decision packet with a recommended default and a specific approval or override question.

## System Action

the OS MUST use this template when creating, replacing, or hardening a project stage contract.

the OS MUST keep the stage contract project-local and source-backed.

the OS MUST point to root authority instead of duplicating root law inside the project.

## Inherits

Each project stage contract MUST inherit from the nearest available project sources first, then root sources:

- `[PROJECT]/CLAUDE.md`
- `[PROJECT]/CONTEXT.md`
- `[PROJECT]/ROUTING.md`
- `[PROJECT]/_governance/README.md` when present
- `[PROJECT]/_memory/project-memory.md` when present
- `[PROJECT]/_memory/decisions.md` when present
- `[PROJECT]/_connectivity/README.md` when present
- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- Root `_operator/`
- Root `_governance/steward.md`
- Root `_routing/deterministic-contract-language-standard.md`
- Root `_routing/project-stage-contract-template.md`
- Root `_memory/MEMORY-ROUTER.md`
- Root `_connectivity/`
- Root `_agents/ROLE-INDEX.md`

If a listed project-local source is absent, the contract MUST mark it as absent, partial, or not applicable. It MUST NOT pretend the source exists.

## Required Contract Fields

Every project stage `CONTRACT.md` MUST include these sections:

- Purpose.
- Owner.
- Operator-Facing Action.
- System Action.
- Inherits.
- Stage Scope.
- Entry Conditions.
- Inputs.
- Required Checks.
- MUST.
- MUST NOT.
- Outputs.
- Memory Rules.
- Connectivity And Live-System Boundary.
- Exit / Handoff.
- Acceptance Test.
- Failure Test.
- Escalation.

If any required section is missing, the stage contract is provisional and MUST NOT be treated as complete.

## Template

Copy this section into a project stage contract and replace bracketed fields.

````markdown
# Stage [NN] - [Stage Name] Contract

Status: [deterministic stage contract | provisional stage contract]
Date: [YYYY-MM-DD]

Contract language standard:

- [relative path to root `_routing/deterministic-contract-language-standard.md`]
- [relative path to root `_routing/project-stage-contract-template.md`]

## Purpose

This stage owns [project-specific responsibility] for [PROJECT] before [named downstream movement] occurs.

Short rule:

```text
[One sentence that makes the stage's movement boundary testable.]
```

## Owner

[Role] owns stage routing and sequence.

[Role] owns truth, proof, refusal, correction, or claim review when relevant.

[Role] owns risk scoring when stage movement affects [client | public | live-system | legal | financial | operator-load] risk.

[Role] owns hard stops when credentials, live systems, regulated data, legal/compliance, or external-system changes appear.

the operator owns final approval for business judgment, moral judgment, risk ownership, project activation, public/client commitments, and risk score 3+.

## Operator-Facing Action

the operator may ask for [ordinary-language examples] without naming this stage.

the OS MUST classify the request before asking the operator where it belongs.

## System Action

the OS MUST route work to this stage when the request creates, evaluates, updates, uses, or moves [stage-owned objects].

the OS MUST stop or reroute when the request belongs to [excluded stages, folders, or live-system paths].

## Inherits

- `[relative path]/CLAUDE.md`
- `[relative path]/CONTEXT.md`
- `[relative path]/ROUTING.md`
- `[relative path]/_governance/README.md` when present
- `[relative path]/_memory/project-memory.md` when present
- `[relative path]/_memory/decisions.md` when present
- `[relative path]/_connectivity/README.md` when present
- Root Steward: `[relative path]/_governance/steward.md`
- Root routing: `[relative path]/ROUTING.md`
- Root deterministic contract standard: `[relative path]/_routing/deterministic-contract-language-standard.md`

Absent project-local inheritance sources:

- [List absent expected sources, or write `none`]

## Stage Scope

This stage owns:

- [Owned scope item]

This stage does not own:

- [Excluded scope item]

## Entry Conditions

This stage may begin when:

- [Required source, approval, prior stage, or request condition]

This stage MUST NOT begin when:

- [Stop condition]

## Inputs

This stage accepts:

- [Project-level references]
- [Stage-level references]
- [Prior stage outputs]
- [Human-provided notes, corrections, or approvals]

This stage MUST label each input as:

- Approved.
- Current.
- Draft.
- Historical.
- Inferred.
- External reference.
- Unresolved.

## Required Checks

Before producing output, this stage MUST check:

- Project scope.
- Current project memory.
- Relevant prior decisions.
- Source authority for claims.
- Live-system and credential boundaries.
- Client/public/legal/compliance sensitivity.
- Required next stage or stop condition.

## MUST

- This stage MUST [required behavior].
- This stage MUST distinguish approved truth from inferred, draft, historical, external, or unresolved material.
- This stage MUST preserve project boundaries.
- This stage MUST route durable decisions to project memory.
- This stage MUST use `output/` for stage-run artifacts unless the project contract names another destination.
- This stage MUST name the next stage, handoff destination, or stop condition before closing substantial work.

## MUST NOT

- This stage MUST NOT treat legacy, archive, external, or cross-project material as current project truth without source authority.
- This stage MUST NOT advance public, client-facing, legal, compliance, financial, credential, or live-system movement without the required approval path.
- This stage MUST NOT change live systems, credentials, repos, domains, forms, automations, analytics, payment systems, client records, or public pages unless the project connectivity contract explicitly allows it and approval is recorded.
- This stage MUST NOT ask the operator to classify routine destination, source type, or stage placement before the OS inspects available sources.
- This stage MUST NOT move to the next stage without a handoff, output, memory update, or stop reason.

## Outputs

This stage produces:

- [Named output artifact or output class]
- [Decision packet when unresolved judgment is needed]
- [Handoff packet or next-stage signal]
- [Memory update when durable]

Default output destination:

- `output/`

## Memory Rules

This stage MUST write durable project decisions to:

- `[PROJECT]/_memory/decisions.md` when present.

This stage MUST update current project state in:

- `[PROJECT]/CONTEXT.md` when the current state changes.

If project memory files are absent, this stage MUST flag the absence and route to Conductor before pretending durable memory exists.

## Connectivity And Live-System Boundary

This stage MUST treat credentials, private keys, tokens, regulated data, legal/compliance material, production domains, DNS, repos, forms, automations, analytics, payment systems, client records, public pages, and external-system writes as live-system or boundary-sensitive unless the project connectivity contract says otherwise.

Live-system movement MUST route through:

- Project `_connectivity/` when present.
- Root `_connectivity/`.
- Warden.
- the operator approval when required.

## Exit / Handoff

Default next stage:

- [Stage NN - Stage Name]

Other valid handoffs:

- [Project governance]
- [Project memory]
- [Project connectivity]
- [Root role or folder]
- [Stop with decision packet]

Signal required:

- [none | Signal | handoff packet | decision packet]

Memory impact:

- [none | check | write | update-source]

## Acceptance Test

This contract passes when stage work has:

- A named project.
- A named stage.
- Named source files or source absence.
- Clear truth labels for inputs.
- Required checks completed.
- Outputs written to the approved destination.
- Durable findings routed to memory.
- Live-system risks stopped or routed.
- A next stage, handoff destination, or stop condition.

## Failure Test

This contract fails when:

- Work enters the stage without project or stage classification.
- Historical, inferred, external, or cross-project material is treated as approved current truth.
- the operator is asked to classify routine stage placement before the OS inspects sources.
- Public/client/legal/compliance/live-system movement advances without the required approval path.
- Output is written to an unapproved destination.
- Durable project decisions remain only in chat.

## Escalation

Escalate to Conductor for routing, sequence, destination, or stage boundary conflicts.

Escalate to Steward for truth, proof, claim, refusal, correction, or public/client-facing meaning.

Escalate to Keeper/Recorder/Librarian for memory judgment, exact record, or findability gaps.

Escalate to Sentinel for risk score changes.

Escalate to Warden for credentials, live systems, regulated data, legal/compliance exposure, or external-system writes.

Escalate to the operator for business judgment, moral judgment, risk ownership, project activation, public/client commitments, or risk score 3+.
````

## Required Checks

Before a project stage contract is marked deterministic, Marshal MUST verify:

- Owner is named.
- Operator-facing action is named.
- System action is named.
- MUST rules are testable.
- MUST NOT rules name forbidden interpretations.
- Inputs are defined.
- Outputs are defined.
- Acceptance test is observable.
- Failure test is observable.
- Escalation path is named.
- Operator-load failure is checked.
- Live-system boundary is checked.
- Memory destination is named or absence is flagged.

## MUST

- Project stage contracts MUST inherit root authority and project-local sources.
- Project stage contracts MUST separate approved, current, draft, historical, inferred, external, and unresolved material.
- Project stage contracts MUST define entry conditions and exit/handoff conditions.
- Project stage contracts MUST define memory and live-system behavior.
- Project stage contracts MUST keep project-specific truth inside the project workspace unless root law is actually changing.
- Project stage contracts MUST route missing project-local inheritance sources as gaps instead of pretending completion.

## MUST NOT

- Project stage contracts MUST NOT duplicate root law when a pointer is enough.
- Project stage contracts MUST NOT turn the operator into the classifier for routine stage placement.
- Project stage contracts MUST NOT let generated artifacts, visual interfaces, or old folders become truth without source authority.
- Project stage contracts MUST NOT authorize live-system writes by implication.
- Project stage contracts MUST NOT treat a folder's existence as proof that the project or stage is active.

## Inputs

This template accepts:

- New project stage definitions.
- Existing project stage contracts that need hardening.
- Project cleanup or inheritance work.
- Project handoff architecture.

## Outputs

This template produces:

- A deterministic project stage `CONTRACT.md`.
- A missing-field list when an existing stage is incomplete.
- A decision packet when project activation, scope, or risk ownership is unclear.

## Acceptance Test

This template passes when a project stage contract can be tested without asking the operator to interpret the stage's purpose, owner, inputs, output destination, memory behavior, live-system boundary, or next handoff.

## Failure Test

This template fails when a project stage contract allows more than one plausible destination, approval path, output path, memory path, or live-system interpretation without a deciding rule.

## Escalation

Escalate to Marshal when deterministic fields are missing.

Escalate to Conductor when stage routing or sequence is unclear.

Escalate to Steward when truth, proof, claim, refusal, or correction authority is implicated.

Escalate to Warden when live-system, credential, regulated-data, legal, compliance, or external-system movement appears.

Escalate to the operator only with a decision packet when project activation, risk ownership, business judgment, public/client commitment, or risk score 3+ requires human authority.
