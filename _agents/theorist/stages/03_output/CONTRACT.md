# Theorist Output Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce model-coherence output.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/theorist/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Theorist owns this output stage.

## Operator-Facing Action

the operator receives a model-coherence packet when theory or abstraction affects movement.

## System Action

the OS produces model, assumptions, coherence, abstraction risk, practical constraints, missing reviews, and next owner.

## Inputs

- Model-coherence judgment.

## Required Checks

- Is the model safe to use as-is?
- Is it held pending evidence/field/boundary review?
- Is it rejected or revised?

## MUST

- Theorist MUST state proceed, revise, hold, or reject.
- Theorist MUST name next owner.

## MUST NOT

- Theorist MUST NOT output final architecture authority.

## Outputs

```text
Model-coherence packet:
- Model:
- Intended use:
- Assumptions:
- Coherence:
- Abstraction risk:
- Practical constraints:
- Missing reviews:
- Status:
- Next owner:
```

## Acceptance Test

- Output gives Conductor enough to route without treating Theorist as final architect.

## Failure Test

- Output lacks status or next owner.

## Escalation

- Route truth/proof concerns to Steward.
- Route build implications to Conductor and Builder only after authorization.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: model-coherence or handoff
- Memory impact: none, check, write, or update-source
