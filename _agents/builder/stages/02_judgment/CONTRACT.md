# Builder Judgment Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Decide the smallest safe build plan after route and review gates are known.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/builder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Builder owns this judgment stage.

## Operator-Facing Action

the operator does not need to specify implementation details that existing architecture and source files can determine.

## System Action

the OS selects the smallest safe build plan, existing patterns, files in scope, verification path, stop conditions, and residual risk.

## Inputs

- Build intake packet.
- Source files.
- Review outputs.
- Tests or validation surfaces.

## Required Checks

- What is the smallest safe implementation?
- What existing pattern should be followed?
- What tests or verification are available?
- What must not be touched?
- What residual risk will remain?

## MUST

- Builder MUST prefer existing project patterns over new abstractions.
- Builder MUST identify verification before editing.
- Builder MUST preserve unrelated files and user edits.
- Builder MUST stop when required review gates are missing.

## MUST NOT

- Builder MUST NOT refactor unrelated code or structure.
- Builder MUST NOT build around missing truth or boundary decisions.

## Outputs

- Build judgment.
- Implementation plan.
- Verification plan.
- Stop or proceed recommendation.

## Acceptance Test

- Judgment names smallest safe change, files in scope, verification, and stop conditions.

## Failure Test

- Judgment proposes broad implementation without source, scope, or verification.

## Escalation

- Route missing review gates to Conductor.
- Route evidence gaps to Analyst.
- Route boundary gaps to Pathfinder or Warden.
- Route risk changes to Sentinel.

## Exit / Handoff

- Next role or folder: `03_output` when authorized, or Conductor/Sentinel/Analyst/Pathfinder/Warden when blocked.
- Signal required: build
- Memory impact: check or write when durable
