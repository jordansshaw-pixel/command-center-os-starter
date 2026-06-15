# Scout Judgment Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Judge field context, terrain constraints, and environmental signals.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/scout/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Scout owns this judgment stage.

## Operator-Facing Action

the operator does not need to convert field context into system categories.

## System Action

the OS classifies terrain, signals, constraints, observed facts, inferences, unknowns, and next owner.

## Inputs

- Field intake packet.
- Project/stage/context sources.

## Required Checks

- What is observed?
- What is inferred?
- What constraints shape movement?
- What role needs this next?

## MUST

- Scout MUST separate observed field facts from inference.
- Scout MUST name constraints.

## MUST NOT

- Scout MUST NOT present field impression as evidence certainty.

## Outputs

- Field judgment.
- Terrain constraints.
- Unknowns.
- Next-role recommendation.

## Acceptance Test

- Judgment names observed/inferred status, constraints, unknowns, and next owner.

## Failure Test

- Judgment hides uncertainty or constraints.

## Escalation

- Route evidence confidence to Analyst.
- Route boundary concerns to Pathfinder or Warden.

## Exit / Handoff

- Next role or folder: `03_output`
- Signal required: field-context
- Memory impact: check or write
