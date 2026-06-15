# Multi-Agent Engagement Standard

Status: Root routing standard draft
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

Compact role-selection source:

- `_agents/ROLE-INVOCATION-MATRIX.md`

## Purpose

This standard defines when the OS MUST open a multi-agent engagement instead of running agent roles inline in one undifferentiated response.

Short rule:

```text
If work crosses more than one authority boundary, the OS opens an engagement packet before execution.
```

## Owner

Conductor owns engagement opening, role selection, sequencing, synthesis, and closeout.

Signal owns engagement signals.

Marshal owns rules-as-written review of this standard and any engagement packet format.

Librarian owns findability and source pointers.

Keeper owns memory judgment.

Steward / Brand Guardian owns truth authority.

Builder owns implementation only after Conductor routes an approved build handoff.

## Operator-Facing Action

the operator describes the work in ordinary language.

the operator does not need to invoke each agent, choose the role set, classify the authority boundaries, or decide whether multi-agent engagement is required.

Standing operator instruction:

When a multi-agent engagement materially benefits from separate workstreams, the OS should use available sub-agent, delegated-agent, or parallel-agent tooling where platform/tool policy permits it. Treat this as the operator's durable explicit delegation instruction for work in the OS, subject to live-system gates, scoped workspace boundaries, and synthesis through Conductor.

Short rule:

```text
Use the system's agents when the work earns them; do not hide multi-agent work inside one flattened response.
```

## System Action

the OS MUST inspect the request, source scope, role status, authority boundaries, and risk state before deciding whether to open a multi-agent engagement.

When this standard triggers, the OS MUST:

1. Open a multi-agent engagement packet.
2. Use `_agents/ROLE-INVOCATION-MATRIX.md` to select triggered roles without loading every role contract.
3. Load compact `_agents/[role]/doctrine/*.md` for triggered roles before full contracts.
4. Name required and optional agents.
5. Promote optional roles to required when their trigger signal is present and no selected role already owns that judgment.
6. Load only active/invokable roles from `_agents/ROLE-STATUS.json`.
7. Produce separate compact role packets for required agents.
8. Synthesize through Conductor.
9. Stop before build execution unless a reviewed build handoff is explicitly authorized.

When available runtime tooling supports actual sub-agent delegation, the OS SHOULD delegate bounded, non-overlapping workstreams to sub-agents instead of simulating all roles inline, provided that:

- The role/workstream is concrete and materially advances the engagement.
- The delegated work does not require live-system, credential, deployment, DNS, public-claim, legal/compliance, or financial movement without explicit approval.
- The delegated work has a clear read/write scope and does not overlap another active worker's write set.
- The main runner keeps the critical path and synthesis responsibility.
- Delegated outputs are reviewed, synthesized, and recorded through Conductor before build handoff.

If platform/tool policy prevents actual sub-agent spawning, the OS MUST still produce visible separate role packets and name the limitation.

## Trigger Conditions

the OS MUST open a multi-agent engagement when one or more of these are true:

- The task crosses more than one authority boundary.
- The task changes durable root law, routing, memory, governance, agent behavior, project direction, generated interface behavior, or operator-facing workflow.
- The task creates or changes build/prototype/scaffold/integration/hook/script infrastructure.
- The task involves repeated operator correction, context bleed, source-improvement, or finalization drift.
- The task touches live-system, credential, permission, connectivity, public, client, legal/compliance, or financial boundaries.
- The task requires evidence/source confidence plus boundary or model-coherence review.
- The task cannot safely be completed by one role without hidden assumptions about truth, route, memory, risk, boundary, protocol, or implementation.

Authority boundaries:

- Routing.
- Memory judgment.
- Truth authority.
- Evidence/source confidence.
- Boundary/live-system protection.
- Risk.
- Signal/handoff.
- Protocol/rules-as-written.
- Model coherence.
- Repair/failure analysis.
- Build/execution.
- Findability/indexing.
- Field/human context.

## Fast-Lane Exception

the OS MAY skip multi-agent engagement only when `_routing/low-risk-fast-lane-standard.md` permits fast-lane movement and all of these are true:

- Risk score is `0` or `1`.
- The work is reversible.
- The work does not change durable source truth.
- The work does not cross more than one authority boundary.
- Existing contracts define the exact action and acceptance test.

If any condition is false, this standard applies.

## Required Engagement Packet

When this standard triggers, Conductor MUST produce:

```text
Multi-agent engagement:
- Trigger:
- Scope:
- Workspace:
- Work type:
- Risk:
- Authority boundaries crossed:
- Required agents:
- Optional agents:
- Source files:
- Expected outputs:
- Synthesis owner:
- Memory impact:
- Stop condition:
- Build handoff allowed: [yes | no]
```

## Required Agent Packet

Each required agent MUST produce a separate packet.

The packet MAY be compact when `_agents/ROLE-INVOCATION-MATRIX.md` is enough and the role does not need full staged execution:

```text
Agent packet:
- Agent:
- Stage:
- Scope:
- Finding:
- Evidence:
- Constraint:
- Recommendation:
- Required downstream owner:
- Handoff:
```

Full role `CONTRACT.md` and stage `CONTRACT.md` load is required when the role is the primary executor, the role output changes durable source truth, the role contract/stage behavior is being edited, or compact doctrine/source context is insufficient.

## Required Synthesis Packet

Conductor MUST synthesize the engagement before work moves:

```text
Engagement synthesis:
- Trigger resolved:
- Required agents completed:
- Conflicts:
- Decision:
- Build/no-build:
- Files to change:
- Open risks:
- Memory action:
- Next owner:
```

## Default Role Sets

These sets are seed sets. They are not maximum sets.

the OS MUST promote triggered optional roles into the required set when `_agents/ROLE-INVOCATION-MATRIX.md` identifies a real authority boundary for the current request.

the OS MUST name skipped triggered roles and the skip reason for substantial work.

Infrastructure reducing orchestration:

- Required: Conductor, Analyst, Pathfinder, Theorist, Marshal, Keeper, Steward / Brand Guardian, Librarian.
- Optional: Sentinel, Signal, Mechanic, Scout.
- Build owner after approval: Builder.

Build/prototype/scaffold/integration:

- Required: Conductor, Analyst, Pathfinder, Theorist, Sentinel, Signal.
- Conditional: Warden for live-system or credential boundary, Marshal for rules-as-written, Mechanic for repair, Scout for field context.
- Build owner after approval: Builder.

Context bleed/session boundary:

- Required: Conductor, Keeper, Recorder, Librarian, Marshal, Steward / Brand Guardian.
- Conditional: Mechanic if failure analysis is required.

Generated human-facing interface:

- Required: Conductor, Analyst, Librarian, Marshal, Signal.
- Conditional: Steward / Brand Guardian when truth, proof, identity, or governance claims are shown.
- Conditional: Builder after approved generator or artifact changes.

Connectivity/live-system:

- Required: Conductor, Warden, Sentinel, Signal, Steward / Brand Guardian.
- Conditional: Analyst for external evidence, Librarian for registry/index, Builder after approved local implementation.

Role/agent behavior change:

- Required: Conductor, Marshal, Steward / Brand Guardian, Keeper, Librarian.
- Conditional: Analyst for source evidence, Theorist for abstraction/model risk, Signal for signal/handoff.

Agent-utilization or routing-bloat repair:

- Required: Conductor, Marshal, Keeper, Librarian, Mechanic, Theorist, Analyst, Signal.
- Conditional: Sentinel for risk, Steward / Brand Guardian for durable authority changes, Pathfinder for boundary/context-envelope design, Recorder for audit reconstruction, Builder for deterministic gate updates.

Research/evidence:

- Required: Analyst, Conductor.
- Conditional: Steward / Brand Guardian for truth/proof, Scout for field context, Keeper for memory, Librarian for findability.

## Deterministic Infrastructure Boundary

Hooks and Python scripts MAY later support this standard by performing deterministic checks:

- Role status validation.
- Required file existence checks.
- Required field validation.
- Timestamp validation.
- Source-map freshness checks.
- Trigger detection.
- Role-set selection.
- Packet skeleton generation.
- Acceptance/failure test execution.

Hooks and Python scripts MUST NOT claim to perform agent judgment when the work requires ambiguity handling, synthesis, evidence interpretation, model critique, truth authority, risk ownership, or operator approval.

Short rule:

```text
Scripts validate and route. Agents judge. Conductor synthesizes.
```

Current deterministic support:

- `_routing/atx_fast_lane_gate.py`
- `_routing/atx_multi_agent_gate.py`
- `_routing/atx_hook_runner.py`
- `.githooks/pre-commit`

Current local hook installation:

```text
core.hooksPath = Command Center OS/.githooks
```

Installed hook behavior:

- `pre-commit` exits without action when no staged files are under `Command Center OS/`.
- `pre-commit` runs `_routing/atx_hook_runner.py --event source-change` when the OS files are staged.
- `pre-commit` does not write packets, mutate files, or perform agent judgment.

Current supported actions:

- Validate declared fast-lane eligibility and fail closed when source, destination, risk, reversibility, authority boundary, stop condition, or verification is missing.
- Infer work type from request text or accept explicit `--work-type`.
- Select the required and optional role set.
- Promote triggered optional roles based on `_agents/ROLE-INVOCATION-MATRIX.md` trigger signals.
- Validate required roles against `_agents/ROLE-STATUS.json`.
- Verify required role folders, compact doctrine, contracts, and stage contracts exist.
- Emit a multi-agent engagement packet.
- Emit separate agent packet skeletons.
- Emit an Conductor synthesis skeleton.
- Default `Build handoff allowed` to `no` unless explicitly approved.
- Run event-specific hook/task checks without installing hooks.
- Block `pre-build` events unless explicit build handoff approval is passed.
- Write packet output only when an explicit the OS-root-relative output path is provided.

Verification command:

```text
python _routing/atx_multi_agent_gate.py --self-test
python _routing/atx_fast_lane_gate.py --self-test
python _routing/atx_hook_runner.py --self-test
```

Example packet command:

```text
python _routing/atx_multi_agent_gate.py --request "build deterministic python hook infrastructure for multi agent engagement" --scope "root _routing" --memory-impact update-source --format markdown
python _routing/atx_fast_lane_gate.py --source "_routing/low-risk-fast-lane-standard.md" --destination "_routing/low-risk-fast-lane-standard.md" --risk 1 --inside-workspace --source-clear --destination-clear --reversible --internal-facing --preserves-user-edits --claims-sourced --existing-contract --single-authority-boundary --stop-condition "Stop if scope changes." --verification "Review packet before execution." --format markdown
python _routing/atx_hook_runner.py --event pre-build --request "build deterministic infrastructure" --allow-build-handoff --format markdown
```

## MUST

- the OS MUST open a multi-agent engagement when trigger conditions are met.
- the OS MUST use available sub-agent/delegation tooling for bounded parallel workstreams when the engagement would materially benefit and platform/tool policy permits it.
- the OS MUST name why each required agent is included.
- the OS MUST treat default role sets as seeds and promote triggered roles when the request contains a real matrix signal.
- the OS MUST verify each required role is active, invokable, and has compact doctrine before use.
- the OS MUST use separate agent packets instead of collapsing all role outputs into one unlabeled paragraph.
- the OS MUST name skipped triggered roles and skip reasons for substantial work.
- the OS MUST produce an Conductor synthesis before execution or handoff.
- the OS MUST set `Build handoff allowed: no` unless Builder has been explicitly authorized after review.
- the OS MUST route durable findings through `_memory/MEMORY-ROUTER.md`.
- the OS MUST use Signal signal format when work moves between agents, sessions, projects, stages, or build handoff.

## MUST NOT

- the OS MUST NOT require the operator to manually invoke required agents.
- the OS MUST NOT collapse sub-agent-appropriate work into one hidden inline pass merely for convenience.
- the OS MUST NOT claim platform-level sub-agent authority beyond what the current runtime tools permit.
- the OS MUST NOT use queued or non-invokable roles.
- the OS MUST NOT treat inline role narration as a completed multi-agent engagement unless the required engagement, agent, and synthesis packets exist.
- the OS MUST NOT hand off to Builder before required review packets and synthesis are complete.
- the OS MUST NOT let deterministic scripts replace judgment roles.
- the OS MUST NOT create new agent folders to satisfy an engagement unless the operator separately approves a new role build.

## Inputs

This standard accepts:

- User requests.
- Routing signals.
- Build-time review requests.
- Source-improvement candidates.
- Role behavior corrections.
- Context recovery events.
- Generated interface changes.
- Connectivity/live-system requests.
- Prior decisions and handoffs.

## Outputs

This standard produces:

- Multi-agent engagement packet.
- Required role set.
- Separate agent packets.
- Engagement synthesis.
- Build/no-build decision.
- Memory or source-improvement action.
- Handoff packet when work continues.

## Acceptance Test

This standard passes when:

- Trigger conditions are checked.
- Authority boundaries crossed are named.
- Required agents are active/invokable.
- Required agent packets exist.
- Conductor synthesis exists.
- Memory impact is named.
- Build handoff state is explicit.
- No Builder handoff occurs before review authorization.

## Failure Test

This standard fails when:

- A multi-boundary task is handled as one inline agent response.
- the operator is asked to choose agents before the OS classifies the work.
- Required role outputs are merged without separate packets.
- A queued/non-invokable role is used.
- Builder receives work before engagement review is complete.
- Scripts or hooks are described as performing judgment rather than deterministic validation.

## Escalation

Escalate to Conductor when role selection, sequence, destination, or build handoff is unclear.

Escalate to Marshal when packet fields, trigger tests, or compliance rules are missing.

Escalate to Steward / Brand Guardian when truth, proof, refusal, governance, public, or doctrine claims are involved.

Escalate to Keeper, Recorder, or Librarian when memory, exact record, or findability must persist.

Escalate to Warden before live-system, credential, secret, permission, or do-not-touch movement.

Escalate to the operator only when approval, risk ownership, taste, business judgment, or priority cannot be safely decided by source law.
