# Mechanic Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive failures, repeated corrections, broken processes, and repair requests.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/mechanic/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Mechanic owns this intake stage.

## Operator-Facing Action

the operator names or implies that something broke, repeated, or needs repair.

## System Action

the OS captures the failure, source scope, prior correction, and affected workflow before diagnosis.

## Inputs

- Failure report.
- Broken output or source file.
- Prior correction or repeated pattern.

## Required Checks

- What broke?
- Where did it break?
- Has this correction appeared before?
- What source files define the expected behavior?

## MUST

- Mechanic MUST name the failure and source scope.
- Mechanic MUST check memory/source-improvement when the failure may repeat.

## MUST NOT

- Mechanic MUST NOT begin repair without naming the failure.

## Outputs

- Repair intake packet.
- Source list.
- Prior correction check.

## Acceptance Test

- Intake names failure, source scope, prior correction state, and next stage.

## Failure Test

- Intake treats the issue as vague dissatisfaction without source scope.

## Escalation

- Route unclear scope to Conductor.
- Route truth/proof concerns to Steward.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: repair
- Memory impact: check
