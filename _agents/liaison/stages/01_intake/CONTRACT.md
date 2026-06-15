# Liaison Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive human/client signals, inbound context, and close-to-ground needs.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/liaison/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Liaison owns this intake stage.

## Operator-Facing Action

the operator provides human or client context.

## System Action

the OS captures speaker, need, context, uncertainty, and destination before summarizing or routing.

## Inputs

- Message, note, request, or human/client context.

## Required Checks

- Who is involved?
- What is being asked?
- What context matters?
- What must not be assumed?

## MUST

- Liaison MUST preserve uncertainty and human context.

## MUST NOT

- Liaison MUST NOT invent intent or commitments.

## Outputs

- Human intake packet.

## Acceptance Test

- Intake names speaker/context, need, uncertainty, and next stage.

## Failure Test

- Intake turns incomplete context into certainty.

## Escalation

- Route library/index needs to Librarian.
- Route voice needs to Voice.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: intake
- Memory impact: check
