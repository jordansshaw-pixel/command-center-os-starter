# Mechanic Judgment Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Diagnose root cause and decide the repair path.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/mechanic/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Mechanic owns this judgment stage.

## Operator-Facing Action

the operator does not need to diagnose the root cause before Mechanic inspects the failure.

## System Action

the OS separates symptom, cause, source gap, repair, prevention, and next owner.

## Inputs

- Repair intake packet.
- Source files.
- Prior decisions or run logs.

## Required Checks

- What is symptom versus root cause?
- What source failed?
- What repair prevents recurrence?
- Does Steward, Sentinel, Warden, or Conductor need review?

## MUST

- Mechanic MUST name root cause and prevention.
- Mechanic MUST identify whether a source-improvement update is required.

## MUST NOT

- Mechanic MUST NOT call a patch a repair when recurrence is likely.

## Outputs

- Repair judgment.
- Source-improvement recommendation.
- Required review gates.

## Acceptance Test

- Judgment names symptom, root cause, repair, prevention, affected source, and next owner.

## Failure Test

- Judgment lacks prevention or source ownership.

## Escalation

- Route risk changes to Sentinel.
- Route truth/proof issues to Steward.
- Route destination uncertainty to Conductor.

## Exit / Handoff

- Next role or folder: `03_output`
- Signal required: repair
- Memory impact: check or write
