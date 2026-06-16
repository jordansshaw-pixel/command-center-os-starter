# Pathfinder Output Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce the boundary architecture artifact.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/pathfinder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Pathfinder owns this output stage.

## Operator-Facing Action

the operator receives a boundary packet when boundary output affects later movement.

## System Action

the OS produces a boundary packet with protected assets, proposed movement, allowed movement, forbidden movement, review gates, hard-stop concerns, operating cover, and next owner.

## Inputs

- Boundary judgment.
- Safe movement envelope.
- Escalation list.

## Required Checks

- Can Conductor route from this output?
- Can Sentinel score risk from this output?
- Does Warden need a hard-stop packet?

## MUST

- Pathfinder MUST produce a structured boundary packet.
- Pathfinder MUST state whether movement is allowed, held, or stopped pending review.
- Pathfinder MUST name the next owner.

## MUST NOT

- Pathfinder MUST NOT output only caution without a route.
- Pathfinder MUST NOT label an unreviewed live-system move as safe.

## Outputs

```text
Boundary packet:
- Boundary scope:
- Protected assets/layers:
- Proposed movement:
- Allowed movement:
- Forbidden movement:
- Review gates:
- Hard-stop concerns:
- Operating cover:
- Next owner:
```

## Acceptance Test

- Output can be handed to Conductor, Sentinel, Warden, Steward, or the current session runner without re-identifying the boundary.

## Failure Test

- Output leaves allowed movement, forbidden movement, or next owner implicit.

## Escalation

- Route hard-stop concerns to Warden.
- Escalate route/destination concerns to Conductor.
- Route risk concerns to Sentinel.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: boundary-review
- Memory impact: check or write when durable
