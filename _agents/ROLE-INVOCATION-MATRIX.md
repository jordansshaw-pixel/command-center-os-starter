# Role Invocation Matrix

Status: Root routing standard
Date: 2026-06-07
Timestamp: 2026-06-07 13:44:19 -05:00

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This matrix defines compact role-selection triggers so the OS can use active specialists without loading every role contract by default.

Short rule:

```text
Select roles from signal first. Load agent doctrine for triggered jurisdiction. Load full contracts only when the selected role must judge, output, or change durable source.
```

## Problem

the OS has active role folders, contracts, stages, and handoff paths, but practical runtime has concentrated around a small runner set.

Current utilization evidence is tracked in:

- `_agents/ROLE-UTILIZATION.md`

This is an architecture and routing problem, not a reason to flatten or retire roles.

## Owner

Conductor owns role selection and sequencing.

Keeper owns memory relevance and context-budget restraint.

Marshal owns rules-as-written enforcement.

Signal owns visible signal state.

Librarian owns findability and source pointers.

Mechanic owns failure diagnosis when agents are repeatedly skipped, over-loaded, or hidden behind ceremony.

## Compact Invocation Rule

the OS MUST use this matrix before loading role contracts for multi-agent, build-time review, role-change, context-bloat, routing-bloat, or source-improvement work.

the OS MUST NOT load all role contracts merely to decide which role applies.

the OS MAY invoke a role from this matrix using a compact role packet when all of these are true:

- The role is active and invokable in `_agents/ROLE-STATUS.json`.
- The trigger signal matches the request or source evidence.
- The role's compact doctrine file is enough to preserve its jurisdiction.
- The output needed is a short routing, review, or failure-finding packet.
- The work does not require editing the role contract or relying on detailed stage law.

the OS MUST load the full role `CONTRACT.md` and relevant stage `CONTRACT.md` when:

- The role is the primary executor.
- The role's judgment will change durable source truth.
- The role contract, stages, handoff behavior, or authority is being edited.
- The compact matrix and source context are insufficient to decide safely.

## Role Trigger Matrix

| Role | Primary Trigger Signals | Compact Output |
|---|---|---|
| Conductor | Routing, sequence, scope, destination, owner, handoff, next action | Route, sequence, receiving owner, stop condition |
| Steward / Brand Guardian | Truth, proof, oath, refusal, correction, governance, brand, public meaning | Truth gate, proof need, correction, refusal, approval state |
| Keeper | Memory relevance, prior decisions, context budget, continuity, no-load judgment | Memory check, no-load reason, persistence decision |
| Recorder | Exact record, provenance, timeline, audit reconstruction, quoted source state | Record check, source trace, timestamp or evidence pointer |
| Librarian | Findability, indexing, source maps, placement, retrieval, pointer hygiene | Destination/index pointer, source map update need |
| Sentinel | Risk, failure mode, blast radius, review gate, stop condition | Risk score, main failure mode, required gate |
| Signal | Signal, handoff packet, communication state, runner visibility | Signal packet, status, audience, next action |
| Warden | Live systems, credentials, secrets, permissions, external accounts, do-not-touch zones | Hard boundary, forbidden movement, approval requirement |
| Voice | Voice, tone, operator-aligned language, public phrasing after truth is settled | Voice pass, tone constraint, phrase risk |
| Analyst | Evidence, assumptions, source confidence, research, proof path, knowability | Evidence check, assumption split, source-confidence finding |
| Pathfinder | Boundaries, operating cover, safe movement envelope, workspace/project separation | Allowed/forbidden movement, boundary design, review-required zone |
| Theorist | Model, abstraction, taxonomy, theory, coherence, elegant-but-impractical risk | Model-coherence finding, abstraction risk, practical constraint |
| Builder | Build, implementation, script, generator, prototype, tooling after review | Build plan, implementation patch, verification result |
| Mechanic | Repeated failure, broken process, repair, diagnosis, drift, skipped-role pattern | Failure diagnosis, root cause, repair route |
| Marshal | Rules-as-written, contracts, deterministic language, compliance, checklists | Pass/fail rule check, required correction |
| Liaison | Human/client intake, messenger signal, client-facing ask, close-context capture | Human/client signal, intake summary, routing cue |
| Scout | Field context, terrain, environmental truth, real-world operating conditions | Field-context finding, reality constraint, terrain risk |

## Promotion Rule

Default role sets in `_routing/multi-agent-engagement-standard.md` and `_routing/atx_multi_agent_gate.py` are seed sets, not maximum sets.

If a trigger signal matches a role in this matrix, the OS MUST promote that role into the required engagement set unless:

- The role is not active/invokable.
- Another selected role already owns the same judgment for this pass.
- The role would increase context load without changing the decision.
- The role's trigger is only incidental language, not a real authority boundary.

When the OS skips a triggered role, it MUST name the skip reason in the run log or final summary for substantial work.

## Context Budget Rule

Role selection MUST NOT create the context bloat it is meant to solve.

For substantial work, the OS SHOULD use this sequence:

1. Load Tier 0.
2. Load `_agents/ROLE-STATUS.json`.
3. Load this matrix.
4. Select candidate roles.
5. Load triggered role doctrine files.
6. Load only the standards and role contracts needed for selected roles.
7. Produce compact role packets.
8. Load deeper role stages only when required by the selected output.

## Compact Role Packet

Use this packet when the matrix is enough and full staged role execution is unnecessary:

```text
Role invocation:
- Role:
- Trigger signal:
- Source checked:
- Finding:
- Constraint:
- Recommendation:
- Skip/full-load decision:
- Next owner:
```

## Acceptance Test

This matrix passes when:

- Role selection happens before broad contract loading.
- Triggered role doctrine loads before full contracts when doctrine is enough.
- Triggered active roles are promoted or explicitly skipped with reason.
- Specialist roles outside the usual runner set are considered when their trigger signals appear.
- Context load stays bounded to the selected role set.
- The final summary or run log names invoked roles and skipped triggered roles for substantial work.

## Failure Test

This matrix fails when:

- the OS uses only Conductor, Librarian, Builder, and Marshal by default while specialist trigger signals are present.
- Optional roles remain optional after their trigger signal appears.
- Full role contracts are loaded before selection without a source reason.
- A role is skipped silently because packet ceremony is too expensive.
- the operator is asked to choose agents before the OS classifies the trigger signals.

## Escalation

Escalate to Conductor when role sequence or ownership is unclear.

Escalate to Marshal when written rules conflict or the matrix lacks a deciding trigger.

Escalate to Mechanic when the same role-skipping or context-bloat failure recurs.

Escalate to the operator only when using, retiring, creating, or materially redefining a role requires human judgment or approval.
