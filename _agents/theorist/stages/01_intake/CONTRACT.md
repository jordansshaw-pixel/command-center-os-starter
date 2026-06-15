# Theorist Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive models, theories, abstractions, taxonomies, and architecture concepts for coherence review.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/theorist/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Theorist owns this intake stage.

## Operator-Facing Action

the operator provides or implies a model, theory, abstraction, or conceptual structure.

## System Action

the OS captures the model, intended use, assumptions, and source scope.

## Inputs

- Model, taxonomy, theory, architecture concept, or build-time review question.

## Required Checks

- What model is being reviewed?
- What is it supposed to do?
- What assumptions support it?
- What evidence or field context is available?

## MUST

- Theorist MUST name the model and intended use.

## MUST NOT

- Theorist MUST NOT judge coherence before identifying assumptions.

## Outputs

- Model intake packet.

## Acceptance Test

- Intake names model, use, assumptions, source scope, and next stage.

## Failure Test

- Intake leaves the model implicit.

## Escalation

- Route source gaps to Analyst.
- Route field gaps to Scout.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: model-coherence
- Memory impact: check
