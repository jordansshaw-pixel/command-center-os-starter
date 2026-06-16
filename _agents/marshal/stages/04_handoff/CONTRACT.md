# Marshal Handoff Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand protocol findings to routing, correction, memory, or the affected source owner.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/marshal/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Marshal owns this handoff stage.

## Operator-Facing Action

the operator receives next owner and whether protocol passes, fails, or is blocked.

## System Action

the OS hands the protocol packet to the role or source owner responsible for correction.

## Inputs

- Protocol packet.
- Correction requirement.

## Required Checks

- Is correction required?
- Is memory/source update required?
- Who owns the correction?

## MUST

- Marshal MUST name next owner and correction status.

## MUST NOT

- Marshal MUST NOT close a failed protocol check without correction owner.

## Outputs

- Protocol handoff.
- Next owner.

## Acceptance Test

- Handoff preserves status, correction, memory impact, and next action.

## Failure Test

- Handoff leaves failed protocol without owner.

## Escalation

- Route unresolved conflicts to Conductor or the operator.

## Exit / Handoff

- Next role or folder: Conductor, Mechanic, Builder, memory roles, Steward, or affected source owner.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
