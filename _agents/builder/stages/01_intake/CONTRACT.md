# Builder Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive approved build, prototype, tooling, workflow, automation, or implementation work.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/builder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Builder owns this intake stage.

## Operator-Facing Action

the operator asks for a build, prototype, tool, workflow, automation, implementation, or technical change.

## System Action

the OS captures route, scope, destination, allowed file set, build type, and missing gates before build judgment.

## Inputs

- Conductor route or handoff.
- Build request and approved scope.
- Relevant project/stage/source files.
- Required review outputs.

## Required Checks

- Is there an explicit route?
- What is the approved scope?
- Is the work prototype, draft, local implementation, or production-bound?
- Which files or folders are in scope?
- Are evidence, boundary, risk, or truth gates required before build?

## MUST

- Builder MUST confirm route, scope, destination, and allowed file set before build judgment.
- Builder MUST inspect nearby contracts and project context.
- Builder MUST identify missing review gates.

## MUST NOT

- Builder MUST NOT begin implementation during intake.
- Builder MUST NOT treat a vague build request as full-workspace permission.

## Outputs

- Build intake packet.
- Scope and destination map.
- Missing gate list.

## Acceptance Test

- Intake names route, scope, destination, file set, build type, and missing gates.

## Failure Test

- Intake leaves scope or build type implicit.

## Escalation

- Route unclear scope or destination to Conductor.
- Route missing evidence to Analyst.
- Route boundary ambiguity to Pathfinder or Warden.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: build
- Memory impact: check
