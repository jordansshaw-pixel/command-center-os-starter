# Pathfinder Judgment Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Judge whether proposed work has safe boundary architecture and operating cover.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/pathfinder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Pathfinder owns this judgment stage.

## Operator-Facing Action

the operator does not need to classify allowed movement before Pathfinder inspects the boundary.

## System Action

the OS classifies allowed movement, forbidden movement, review gates, hard stops, and next owner.

## Inputs

- Boundary intake packet.
- Relevant root, project, stage, connectivity, governance, memory, or role sources.

## Required Checks

- What is allowed to move?
- What must remain in place?
- What must not be touched?
- What review gate protects the boundary?
- Does the boundary protect root truth, project truth, client context, live systems, credentials, public claims, or operator load?

## MUST

- Pathfinder MUST name allowed, forbidden, and review-required movement.
- Pathfinder MUST distinguish design guardrails from hard stops.
- Pathfinder MUST assign the next owner for unresolved boundary concerns.

## MUST NOT

- Pathfinder MUST NOT weaken a boundary because the implementation is convenient.
- Pathfinder MUST NOT invent local project inheritance when none is written.

## Outputs

- Boundary judgment.
- Safe movement envelope.
- Escalation list.

## Acceptance Test

- Judgment names protected boundary, allowed movement, forbidden movement, review gates, and next owner.

## Failure Test

- Judgment says work is safe without naming what is protected.

## Escalation

- Route hard-stop risk to Warden.
- Route risk scoring to Sentinel.
- Route truth/proof concerns to Steward.

## Exit / Handoff

- Next role or folder: `03_output`
- Signal required: boundary-review
- Memory impact: check or write when durable
