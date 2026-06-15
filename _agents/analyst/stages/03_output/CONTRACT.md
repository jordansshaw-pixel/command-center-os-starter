# Analyst Output Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce the evidence artifact that another role can build, route, approve, stop, or remember from.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/analyst/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Analyst owns this output stage.

## Operator-Facing Action

the operator receives a structured evidence packet when evidence output is needed.

## System Action

the OS produces an evidence packet with claims, source status, confidence, assumptions, unknowns, review needs, and next owner.

## Inputs

- Evidence judgment.
- Source confidence map.
- Research gap list.

## Required Checks

- Is the output clear enough for Conductor to route?
- Does Brand Guardian need truth/proof review?
- Does memory need a durable record?

## MUST

- Analyst MUST produce structured evidence output.
- Analyst MUST name unsupported assumptions explicitly.
- Analyst MUST name the next owner.

## MUST NOT

- Analyst MUST NOT bury uncertainty in prose.
- Analyst MUST NOT output implementation instructions as if evidence review is build authorization.

## Outputs

```text
Evidence packet:
- Question:
- Scope:
- Sources reviewed:
- Claims:
- Evidence status:
- Confidence:
- Assumptions:
- Unknowns:
- Conflicts:
- Required review:
- Next owner:
```

## Acceptance Test

- Output can be handed to Conductor, Brand Guardian, Sentinel, memory, or the current session runner without re-asking what is known.

## Failure Test

- Output leaves evidence status, confidence, or next owner implicit.

## Escalation

- Route unsupported high-risk claims to Brand Guardian / Steward or the operator.
- Route build authorization only through Conductor.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: evidence/source-check
- Memory impact: check or write when durable
