# Pathfinder Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive work that needs boundary architecture, operating cover, scope separation, or safe movement design.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/pathfinder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Pathfinder owns this intake stage.

## Operator-Facing Action

the operator asks for movement, build, workspace, project, stage, or boundary review.

## System Action

the OS captures the proposed movement, protected boundary, source scope, and hard-stop screening result.

## Inputs

- Build request or handoff.
- Project/root/stage/source/output boundary question.
- Connectivity or live-system-adjacent boundary question.

## Required Checks

- What boundary is being protected?
- What movement is proposed?
- What source files define the boundary?
- Does Warden need to be loaded immediately?

## MUST

- Pathfinder MUST identify the boundary scope before judging movement.
- Pathfinder MUST load relevant local contracts and routing files.
- Pathfinder MUST flag hard-stop risk for Warden.

## MUST NOT

- Pathfinder MUST NOT approve movement during intake.
- Pathfinder MUST NOT treat all boundary questions as live-system hard stops.

## Outputs

- Boundary intake packet.
- Source list.
- Hard-stop screening result.

## Acceptance Test

- Intake names boundary scope, proposed movement, source files, and whether Warden is required.

## Failure Test

- Intake leaves the protected boundary unnamed.

## Escalation

- Route hard-stop risk to Warden.
- Escalate route/destination uncertainty to Conductor.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: boundary-review
- Memory impact: check
