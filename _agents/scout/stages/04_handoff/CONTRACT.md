# Scout Handoff Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand field context to routing, evidence, boundary, human-intake, memory, or project owner.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/scout/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Scout owns this handoff stage.

## Operator-Facing Action

the operator receives the field context status and next owner.

## System Action

the OS hands the field packet to the next role while preserving observed/inferred boundaries.

## Inputs

- Field packet.
- Next-role recommendation.

## Required Checks

- Who needs the field context?
- Does memory or project context need update?
- What unknowns remain?

## MUST

- Scout MUST preserve observed/inferred boundaries in handoff.

## MUST NOT

- Scout MUST NOT hand off inferred terrain as proven.

## Outputs

- Field handoff.
- Unknowns.
- Next owner.

## Acceptance Test

- Handoff names receiver, constraints, unknowns, memory impact, and next action.

## Failure Test

- Handoff loses field constraints or uncertainty.

## Escalation

- Route source-confidence gaps to Analyst.
- Route human-context gaps to Liaison.

## Exit / Handoff

- Next role or folder: Conductor, Analyst, Liaison, Pathfinder, Warden, Sentinel, memory roles, or project owner.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
