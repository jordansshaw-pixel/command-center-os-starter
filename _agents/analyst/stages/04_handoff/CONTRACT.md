# Analyst Handoff Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand evidence work to routing, truth authority, risk, memory, or build execution.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/analyst/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Analyst owns this handoff stage.

## Operator-Facing Action

the operator receives the next owner and evidence state when evidence work affects later movement.

## System Action

the OS hands evidence output to routing, truth authority, risk, memory, or build execution with the evidence state preserved.

## Inputs

- Evidence packet.
- Required review list.
- Memory impact decision.

## Required Checks

- Who owns the next move?
- Does the evidence alter durable truth?
- Does a handoff packet or memory update need to be created?

## MUST

- Analyst MUST route truth/proof decisions to Brand Guardian / Steward.
- Analyst MUST route sequence/destination decisions to Conductor.
- Analyst MUST route durable records through memory.
- Analyst MUST route build authorization only through Conductor.

## MUST NOT

- Analyst MUST NOT hand directly to implementation when routing, risk, or truth review is unresolved.

## Outputs

- Handoff note.
- Memory write recommendation when needed.
- Next owner.

## Acceptance Test

- Handoff identifies active agent, active stage, source role, receiving role, work state, evidence status, risk concerns, memory impact, and next action.

## Failure Test

- Handoff leaves the next owner or evidence state unclear.

## Escalation

- Route unresolved truth/proof concerns to Brand Guardian / Steward.
- Route unresolved route/destination concerns to Conductor.
- Route unresolved risk concerns to Sentinel.

## Exit / Handoff

- Next role or folder: Conductor, Brand Guardian / Steward, Sentinel, Keeper, Recorder, Librarian, or Builder after routing.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
