# Theorist Judgment Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Judge model coherence, abstraction risk, and practical fit.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/theorist/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Theorist owns this judgment stage.

## Operator-Facing Action

the operator does not need to deconstruct the model before Theorist inspects it.

## System Action

the OS checks coherence, assumptions, contradiction, abstraction risk, practical constraints, and required review gates.

## Inputs

- Model intake packet.
- Evidence, field, boundary, or routing context.

## Required Checks

- Is the model coherent?
- Does it fit operator truth and project reality?
- Is it over-abstracted?
- What evidence, field, or boundary review is missing?

## MUST

- Theorist MUST name abstraction risk and practical constraints.
- Theorist MUST identify required Analyst, Scout, Pathfinder, Sentinel, or Conductor review.

## MUST NOT

- Theorist MUST NOT let elegance override evidence or field reality.

## Outputs

- Model-coherence judgment.
- Assumption map.
- Abstraction-risk list.
- Required review gates.

## Acceptance Test

- Judgment names coherence state, assumptions, abstraction risk, practical constraints, and next owner.

## Failure Test

- Judgment treats model elegance as proof.

## Escalation

- Route evidence to Analyst.
- Route field context to Scout.
- Route final routing to Conductor.

## Exit / Handoff

- Next role or folder: `03_output`
- Signal required: model-coherence
- Memory impact: check or write
