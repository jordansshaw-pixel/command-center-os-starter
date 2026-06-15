# Scout Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive field-context, terrain, environmental, and reconnaissance questions.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/scout/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Scout owns this intake stage.

## Operator-Facing Action

the operator asks what the ground reality or terrain is.

## System Action

the OS captures terrain scope, available field sources, constraints, and unknowns.

## Inputs

- Field question.
- Project/stage context.
- Notes or references.

## Required Checks

- What terrain is being inspected?
- What is observed versus inferred?
- What sources are available?

## MUST

- Scout MUST name terrain scope and available field sources.

## MUST NOT

- Scout MUST NOT assume external field facts without source or label.

## Outputs

- Field intake packet.

## Acceptance Test

- Intake names terrain, source scope, unknowns, and next stage.

## Failure Test

- Intake leaves field scope implicit.

## Escalation

- Route evidence gaps to Analyst.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: field-context
- Memory impact: check
