# Scout Output Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce field-context output.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/scout/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Scout owns this output stage.

## Operator-Facing Action

the operator receives a field-context packet when terrain matters.

## System Action

the OS produces terrain, signals, constraints, observed/inferred status, unknowns, and next owner.

## Inputs

- Field judgment.

## Required Checks

- Is source confidence needed?
- Is boundary or risk review needed?
- Does project context need update?

## MUST

- Scout MUST name constraints and unknowns.
- Scout MUST name next owner.

## MUST NOT

- Scout MUST NOT output unsupported field claims as proven.

## Outputs

```text
Field packet:
- Terrain:
- Observed:
- Inferred:
- Constraints:
- Unknowns:
- Risk:
- Next owner:
```

## Acceptance Test

- Output is grounded and routable.

## Failure Test

- Output lacks observed/inferred separation.

## Escalation

- Route source-confidence work to Analyst.
- Route risk to Sentinel.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: field-context or handoff
- Memory impact: none, check, write, or update-source
