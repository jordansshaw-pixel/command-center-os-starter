# Liaison Output Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce human/client intake signal output.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/liaison/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Liaison owns this output stage.

## Operator-Facing Action

the operator receives a human-context packet when needed.

## System Action

the OS produces a signal packet with context, need, uncertainty, and next owner.

## Inputs

- Human signal judgment.

## Required Checks

- Is the output internal only?
- Does Voice, Steward, Sentinel, or Librarian need review?

## MUST

- Liaison MUST name what must not be assumed.
- Liaison MUST name next owner.

## MUST NOT

- Liaison MUST NOT output external-facing language as final without review.

## Outputs

```text
Human signal:
- Speaker/context:
- Need:
- Salient details:
- Uncertainty:
- Do not assume:
- Risk:
- Next owner:
```

## Acceptance Test

- Output preserves human context and is routable.

## Failure Test

- Output becomes generic summary without uncertainty or next owner.

## Escalation

- Route final expression to Voice.
- Route proof/client risk to Steward.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: handoff
- Memory impact: none, check, write, or update-source
