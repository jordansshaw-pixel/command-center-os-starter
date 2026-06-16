# Pathfinder Handoff Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand boundary architecture to routing, risk, hard-stop enforcement, truth authority, memory, or implementation.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/pathfinder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Pathfinder owns this handoff stage.

## Operator-Facing Action

the operator receives movement status and next owner when boundary work affects later movement.

## System Action

the OS hands boundary output to routing, risk, hard-stop enforcement, truth authority, memory, or implementation with movement status preserved.

## Inputs

- Boundary packet.
- Review gate list.
- Movement status.

## Required Checks

- Is movement allowed, held, or stopped?
- Who owns the next review gate?
- Does memory need to record the boundary?

## MUST

- Pathfinder MUST route hard-stop concerns to Warden.
- Pathfinder MUST route risk concerns to Sentinel.
- Pathfinder MUST route sequence/destination concerns to Conductor.
- Pathfinder MUST route durable boundary rules through memory.

## MUST NOT

- Pathfinder MUST NOT hand directly to implementation when review gates remain unresolved.

## Outputs

- Handoff note.
- Movement status.
- Next owner.

## Acceptance Test

- Handoff identifies active agent, active stage, source role, receiving role, boundary status, risk concerns, memory impact, and next action.

## Failure Test

- Handoff leaves boundary status or next owner unclear.

## Escalation

- Route hard-stop concerns to Warden.
- Escalate route/destination concerns to Conductor.
- Route risk concerns to Sentinel.

## Exit / Handoff

- Next role or folder: Conductor, Sentinel, Warden, Steward, memory roles, or Builder after routing.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
