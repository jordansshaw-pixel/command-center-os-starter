# Liaison Judgment Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Judge the human/client signal and next routing need.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/liaison/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Liaison owns this judgment stage.

## Operator-Facing Action

the operator does not need to translate messy human context into routing fields.

## System Action

the OS identifies need, signal type, uncertainty, missing question, risk, and next role.

## Inputs

- Human intake packet.
- Project/client context.

## Required Checks

- Is this human intake, voice, library, evidence, field context, or routing work?
- What uncertainty matters?
- What next role is safest?

## MUST

- Liaison MUST route library work to Librarian and voice work to Voice.
- Liaison MUST name uncertainty.

## MUST NOT

- Liaison MUST NOT make external commitments or final claims.

## Outputs

- Human signal judgment.
- Next-role recommendation.

## Acceptance Test

- Judgment names signal, uncertainty, risk, and next role.

## Failure Test

- Judgment hides missing context.

## Escalation

- Route client/public risk to Sentinel and Brand Guardian / Steward.

## Exit / Handoff

- Next role or folder: `03_output`
- Signal required: intake or routing
- Memory impact: check or write
