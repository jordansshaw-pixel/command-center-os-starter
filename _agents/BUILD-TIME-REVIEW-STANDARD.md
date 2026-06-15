# Build-Time Review Standard

Status: Root operating standard
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

Fast-lane exception source:

- `_routing/low-risk-fast-lane-standard.md`

Generated interface acceptance source:

- `_routing/command-surface-acceptance-standard.md`

Multi-agent engagement source:

- `_routing/atx_fast_lane_gate.py`
- `_routing/multi-agent-engagement-standard.md`
- `_routing/atx_multi_agent_gate.py`
- `_routing/atx_hook_runner.py`
- `.githooks/pre-commit`

## Purpose

This standard defines how the OS invokes build-time architecture, theory, evidence, boundary, risk, and engineering roles before durable build work moves.

Short rule:

```text
Build work does not move until the right review lenses have named source, owner, risk, boundary, and next action.
```

## Owner

Conductor owns invocation, sequencing, and final routing of the build-time review layer.

Sentinel owns risk scoring.

Signal owns signal packaging.

Builder owns implementation after Conductor routes and review permits movement.

Current role availability:

```text
the OS now has active specialist roles for evidence architecture, boundary architecture, model coherence, engineering/build execution, repair, protocol, human/client intake, and field context: Analyst, Pathfinder, Theorist, Builder, Mechanic, Marshal, Liaison, and Scout.
```

## Operator-Facing Action

the operator asks for a build, scaffold, integration, workflow, automation, contract, interface, generated artifact, project structure, or implementation change.

the operator does not need to name the review roles.

## System Action

the OS MUST determine whether the request triggers build-time review. If it does, Conductor MUST invoke only currently active roles and source-inspection paths before authorizing Builder or any executor.

If the request crosses more than one authority boundary or requires multiple roles, the OS MUST use `_routing/multi-agent-engagement-standard.md` before execution.

## Trigger Conditions

Build-time review MUST run before execution when the request would create or change any of these:

- Durable root structure.
- Project scaffolds or inheritance.
- Agent contracts, role routing, or stage contracts.
- Connectivity, tool permissions, credentials policy, or live-system boundaries.
- Generated human-facing architecture interfaces.
- Reusable workflows, scripts, automations, or templates.
- Client/project-facing structure where stale path or scope drift is possible.
- Any build with risk score 2 or higher.

Build-time review MAY be skipped only when `_routing/low-risk-fast-lane-standard.md` permits fast-lane movement and all of these are true:

- The work is low risk.
- The work is reversible.
- The work does not create durable source truth.
- The work does not touch live systems, credentials, client commitments, public claims, legal/compliance, or project identity.
- Existing contracts already define the exact action.

For substantial fast-lane claims, `_routing/atx_fast_lane_gate.py` SHOULD validate the declared eligibility before execution. A passing deterministic gate does not replace Conductor routing, Sentinel risk judgment, Brand Guardian truth authority, or Warden live-system stops.

## Required Review Lenses

| Lens | Role | Required Output |
|---|---|---|
| Operating architecture | Conductor | Sequence, destination, owner, stage, handoff path, and whether the work belongs in the current pass. |
| Evidence/source check | Analyst | Evidence, assumptions, source confidence, and what is knowable before build. |
| Boundary architecture | Pathfinder | Boundary design, protective space, safe operating cover, and what must not be crossed. |
| Theory/model coherence | Theorist | The underlying model, abstraction risk, coherence, and whether the structure is elegant but impractical. |
| Risk | Sentinel | Risk score, main failure mode, review gate, and stop condition. |
| Signal | Signal | Review/build signal with active agent, active stage, audience, risk, status, next action, memory impact, and handoff need. |
| Engineering/build | Builder | Build plan, prototype, script, workflow, or implementation after review permits movement. |

## Specialist Status

Theorist is an active specialist role, not final architect.

Theorist protects model coherence, theory, abstraction risk, and impractical elegance. Theorist does not own final architecture, routing, evidence, boundaries, risk, or execution.

Model-coherence checks MUST route through Theorist when:

- The request depends on a new abstraction, framework, taxonomy, model, or operating theory.
- The system may be overfitting structure to one current example.
- The architecture is elegant but may be impractical.
- A model could drift away from project, field, or operator reality.

Theorist MUST NOT be invoked as a substitute for source inspection, Brand Guardian truth review, boundary checks, Sentinel risk, or Conductor routing.

## Queued Role Rule

Queued roles and lenses MUST be built before use.

the OS MUST NOT invoke, assign ownership to, route execution to, or treat as available any queued role or lens until its folder, `CONTRACT.md`, stage contracts, handoff path, and active role-index status exist.

## MUST

- Conductor MUST classify whether build-time review is required before execution.
- Conductor MUST check `_routing/multi-agent-engagement-standard.md` before build execution when the request crosses more than one authority boundary or requires multiple roles.
- Conductor MUST name which review lenses are invoked and why.
- Conductor MUST load `CLAUDE.md`, `CONTEXT.md`, `ROUTING.md`, `_agents/ROLE-INDEX.md`, this standard, and relevant project or stage contracts before routing substantial build work.
- Conductor MUST route evidence architecture to Analyst when evidence/source check is required.
- Conductor MUST route boundary architecture to Pathfinder when boundary review is required.
- Conductor MUST route model-coherence checks to Theorist when abstraction, theory, taxonomy, or impractical-elegance risk matters.
- Sentinel MUST score risk before durable build execution.
- Signal MUST package the review state before work moves between roles, stages, projects, or sessions.
- Mechanic MUST diagnose repeated failures or broken processes when repair is required.
- Marshal MUST check rules-as-written when protocol or deterministic compliance matters.
- Liaison MUST capture human/client intake signal when human context matters, while Librarian remains the library/index/retrieval role.
- Scout MUST capture field context when terrain or environmental truth matters.
- Builder MUST receive a build authorization, prototype authorization, hold, or stop signal before execution.
- Durable findings from the review layer MUST route through `_memory/MEMORY-ROUTER.md` before finalization.

## MUST NOT

- the OS MUST NOT create `_agents/architect/` or `_agents/engineer/` from this review layer.
- the OS MUST NOT let Theorist own final architecture.
- the OS MUST NOT route to any future queued role or lens when source, destination, owner, risk, boundary, folder, contract, stages, or handoff path is unclear or missing.
- the OS MUST NOT skip build-time review merely because a build request sounds simple if it changes durable structure.
- the OS MUST NOT treat a prototype as production truth without Sentinel risk review and required Brand Guardian or the operator approval.
- the OS MUST NOT ask the operator to name the review roles before the OS classifies the work.

## Inputs

This standard accepts:

- Build, scaffold, integration, workflow, automation, contract, interface, generated artifact, project structure, or implementation requests.
- Current workspace, project, stage, or file scope.
- Relevant root, project, stage, role, memory, routing, governance, and connectivity sources.
- Prior decisions and handoffs when applicable.

## Outputs

This standard produces:

```text
Build-time review:
- Trigger:
- Required lenses:
- Operating architecture:
- Evidence architecture:
- Boundary architecture:
- Theory/model coherence:
- Risk:
- Signal:
- Build route:
- Memory impact:
- Next action:
```

## Acceptance Test

This standard passes when:

- The request is classified as review-required or review-skipped with a named reason.
- Required lenses are named.
- Source, destination, owner, boundary, risk score, signal, build route, memory impact, and next action are named before execution.
- Builder receives an explicit build authorization, prototype authorization, hold, or stop signal.

## Failure Test

This standard fails when:

- Builder or another executor starts durable build work before required review output exists.
- The system asks the operator to choose review roles before the OS classifies the work.
- Theorist is treated as final architect.
- A durable build moves with implicit source, destination, owner, risk, or boundary.
- A prototype becomes production truth without required review.

## Escalation

Escalate to the operator when:

- Risk score is 3 or 4.
- The work creates or changes live-system, credential, legal/compliance, financial, public, client, or irreversible commitments.
- The model, evidence, boundary, or routing review cannot identify a safe default.
- A new named role would be created or retired.

Escalate to Brand Guardian when:

- The build changes root governance, oath, truth, proof, refusal, doctrine, brand, or public meaning.

Escalate to Warden when:

- The build touches live systems, credentials, secrets, access, permissions, or do-not-touch zones.

## Default Invocation Sequence

```text
Conductor classify
-> Keeper memory check when prior decisions may matter
-> Analyst evidence/source check when assumptions or sources matter
-> Pathfinder boundary check when safety, scope, or operating cover matters
-> Theorist model-coherence check when abstraction or model risk matters
-> Sentinel risk score
-> Signal signal
-> Builder build/prototype only if authorized
-> Memory/handoff as required
```

For low-risk throwaway prototypes, Conductor MAY authorize Builder earlier only if the work is labeled experimental and cannot become production truth without the full review path.
