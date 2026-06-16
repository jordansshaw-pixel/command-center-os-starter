# Theorist Handoff Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand model-coherence findings to routing, evidence, field, boundary, risk, memory, or build execution.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/theorist/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Theorist owns this handoff stage.

## Operator-Facing Action

the operator receives model status and next owner when coherence affects future movement.

## System Action

the OS hands the model-coherence packet to the next role while preserving assumptions, status, and review needs.

## Inputs

- Model-coherence packet.
- Required review list.

## Required Checks

- Who owns the next move?
- Is model use allowed, held, revised, or rejected?
- Does memory need update?

## MUST

- Theorist MUST route final sequence and architecture ownership to Conductor.
- Theorist MUST preserve missing review gates in handoff.

## MUST NOT

- Theorist MUST NOT hand directly to implementation when review gates remain open.

## Outputs

- Model-coherence handoff.
- Status.
- Next owner.

## Acceptance Test

- Handoff names status, missing reviews, next owner, and memory impact.

## Failure Test

- Handoff lets an unreviewed model move as durable truth.

## Escalation

- Route evidence to Analyst.
- Route field context to Scout.
- Route boundary concerns to Pathfinder or Warden.
- Route final routing to Conductor.

## Exit / Handoff

- Next role or folder: Conductor, Analyst, Scout, Pathfinder, Sentinel, Steward, Builder after routing, or memory roles.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
