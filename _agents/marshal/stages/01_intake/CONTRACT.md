# Marshal Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive work that needs protocol, rules-as-written, checklist, or deterministic contract review.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/marshal/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Marshal owns this intake stage.

## Operator-Facing Action

the operator asks for or implies a protocol check.

## System Action

the OS captures the rule source, action under review, and required procedure.

## Inputs

- Rule, contract, standard, or process.
- Proposed or completed action.

## Required Checks

- What written rule applies?
- What action is being checked?
- Is the rule source current?

## MUST

- Marshal MUST name the rule source and action under review.

## MUST NOT

- Marshal MUST NOT proceed when the rule source is unknown.

## Outputs

- Protocol intake packet.

## Acceptance Test

- Intake names rule source, action, and next stage.

## Failure Test

- Intake relies on memory of a rule without source.

## Escalation

- Route missing source to Librarian or Conductor.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: protocol
- Memory impact: check
