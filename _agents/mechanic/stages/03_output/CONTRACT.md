# Mechanic Output Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce repair diagnosis and prevention output.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/mechanic/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Mechanic owns this output stage.

## Operator-Facing Action

the operator receives a concise repair packet when repair output affects future movement.

## System Action

the OS produces a repair packet with failure, cause, repair, prevention, source update, verification, and next owner.

## Inputs

- Repair judgment.
- Source-improvement recommendation.

## Required Checks

- Does the repair change source?
- Does memory need a durable record?
- Can the repair be verified?

## MUST

- Mechanic MUST produce a structured repair packet.
- Mechanic MUST name verification or the reason verification is unavailable.

## MUST NOT

- Mechanic MUST NOT leave source update needs implicit.

## Outputs

```text
Repair packet:
- Failure:
- Root cause:
- Affected source:
- Repair:
- Prevention:
- Verification:
- Memory impact:
- Next owner:
```

## Acceptance Test

- Output can be handed to Conductor, Builder, memory, or the affected source owner without re-diagnosing the issue.

## Failure Test

- Output omits prevention, verification, or next owner.

## Escalation

- Route implementation to Builder after Conductor authorization.
- Route durable correction to memory.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: repair or handoff
- Memory impact: check, write, or update-source
