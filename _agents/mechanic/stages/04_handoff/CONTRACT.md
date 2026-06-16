# Mechanic Handoff Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand repair output to routing, implementation, memory, or the affected source owner.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/mechanic/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Mechanic owns this handoff stage.

## Operator-Facing Action

the operator receives next owner and whether the failure is repaired, held, or still open.

## System Action

the OS hands the repair packet to the next role or source owner with prevention and memory impact preserved.

## Inputs

- Repair packet.
- Verification result.
- Memory impact decision.

## Required Checks

- Is repair complete, partial, held, or stopped?
- Who owns prevention?
- Does memory need update?

## MUST

- Mechanic MUST name next owner and open loops.
- Mechanic MUST route implementation through Conductor and Builder.

## MUST NOT

- Mechanic MUST NOT mark complete when prevention remains open.

## Outputs

- Repair handoff.
- Open loops.
- Next owner.

## Acceptance Test

- Handoff identifies status, source owner, prevention, memory impact, and next action.

## Failure Test

- Handoff hides unresolved repair or prevention.

## Escalation

- Route unresolved source truth to Steward.
- Route unresolved implementation to Conductor.

## Exit / Handoff

- Next role or folder: Conductor, Builder, memory roles, Steward, or affected source owner.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
