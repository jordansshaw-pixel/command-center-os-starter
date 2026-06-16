# Liaison Handoff Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand human/client signal to routing, voice, memory, project owner, or another specialist.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/liaison/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Liaison owns this handoff stage.

## Operator-Facing Action

the operator receives next owner and any missing human-context question.

## System Action

the OS hands the human signal to the next role while preserving uncertainty and do-not-assume boundaries.

## Inputs

- Human signal.
- Next-role recommendation.

## Required Checks

- Who receives the signal?
- Is memory or project context update needed?
- Is any external action blocked?

## MUST

- Liaison MUST preserve uncertainty and next action in handoff.

## MUST NOT

- Liaison MUST NOT hand off as if external action is approved unless it is.

## Outputs

- Human signal handoff.
- Missing question.
- Next owner.

## Acceptance Test

- Handoff names receiver, uncertainty, blocked assumptions, memory impact, and next action.

## Failure Test

- Handoff loses the human-context signal.

## Escalation

- Route public/client commitments to Steward and the operator.

## Exit / Handoff

- Next role or folder: Conductor, Voice, Librarian, Scout, Sentinel, Steward, project owner, or memory roles.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
