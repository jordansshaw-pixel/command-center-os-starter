# Builder Handoff Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Hand build output to routing, review, memory, project owner, or the next implementation pass.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/builder/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Builder owns this handoff stage.

## Operator-Facing Action

the operator receives completion state, verification result, open loops, and next owner when build work matters later.

## System Action

the OS hands build output to routing, review, memory, project owner, or the next approved build pass with verification and residual risk preserved.

## Inputs

- Build output.
- Verification result.
- Residual risk.
- Memory impact decision.

## Required Checks

- Is the build complete, partial, held, stopped, or superseded?
- What review or verification remains?
- Does memory need a durable record?
- Who owns the next action?

## MUST

- Builder MUST hand off incomplete work with exact open loops.
- Builder MUST route residual risk to Sentinel or Conductor.
- Builder MUST route live-system concerns to Warden.
- Builder MUST route durable build decisions through memory.

## MUST NOT

- Builder MUST NOT mark work complete when required tests or review remain open.

## Outputs

- Build handoff.
- Verification summary.
- Open loops.
- Next owner.

## Acceptance Test

- Handoff identifies active agent, active stage, source role, receiving role, result, files changed, verification, residual risk, memory impact, and next action.

## Failure Test

- Handoff says complete while unresolved verification, review, or risk remains.

## Escalation

- Route incomplete scope to Conductor.
- Route residual risk to Sentinel.
- Route live-system or credential concerns to Warden.
- Route durable decisions through memory.

## Exit / Handoff

- Next role or folder: Conductor, Sentinel, Warden, Steward, memory roles, project owner, or next approved build pass.
- Signal required: handoff
- Memory impact: none, check, write, or update-source
