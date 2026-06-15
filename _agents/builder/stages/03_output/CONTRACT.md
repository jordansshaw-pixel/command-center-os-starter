# Builder Output Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce the scoped build, prototype, tool, workflow, automation, or implementation output.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/builder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Builder owns this output stage.

## Operator-Facing Action

the operator receives the built output and verification summary when build work completes or stops.

## System Action

the OS implements the approved scope, verifies the change, and records result, residual risk, memory impact, and next owner.

## Inputs

- Build judgment.
- Approved implementation plan.
- Source files.
- Verification plan.

## Required Checks

- Are edits within scope?
- Did the implementation preserve existing patterns?
- Did verification run or is the reason it could not run explicit?
- Does any output need memory or handoff?

## MUST

- Builder MUST implement only the approved scope.
- Builder MUST verify the work or record why verification could not run.
- Builder MUST record files changed and result.

## MUST NOT

- Builder MUST NOT silently change adjacent systems.
- Builder MUST NOT leave required verification unstated.

## Outputs

```text
Build output:
- Route:
- Scope:
- Files changed:
- Verification:
- Result:
- Residual risk:
- Memory impact:
- Next owner:
```

## Acceptance Test

- Output includes changed files, verification result, residual risk, and next owner.

## Failure Test

- Output changes files without named verification or result.

## Escalation

- Route implementation blockers to Conductor.
- Route risk changes to Sentinel.
- Route live-system or credential concerns to Warden.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: build or handoff
- Memory impact: none, check, write, or update-source
