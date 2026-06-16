# Analyst Intake Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Receive work that needs evidence architecture, source confidence, research clarification, or assumption separation.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/analyst/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Analyst owns this intake stage.

## Operator-Facing Action

the operator provides or approves a question that needs evidence/source review.

## System Action

the OS captures the evidence question, source scope, and missing context before judgment.

## Inputs

- User request, build request, or handoff.
- Claims, assumptions, source files, references, or research questions.
- Relevant project/stage context when scoped to a project.

## Required Checks

- What claim or decision needs evidence?
- What source files are already available?
- What evidence may be current-world and unstable?
- What downstream role needs the evidence packet?

## MUST

- Analyst MUST identify the evidence question before judging evidence.
- Analyst MUST load local source files before treating a claim as unresolved.
- Analyst MUST mark missing source paths as open evidence gaps.

## MUST NOT

- Analyst MUST NOT start from unsupported assumptions when source files exist.
- Analyst MUST NOT route itself as builder or final approver.

## Outputs

- Evidence intake packet.
- Source list.
- Open evidence questions.

## Acceptance Test

- Intake output names the claim, source scope, missing evidence, and next stage.

## Failure Test

- Intake output jumps to conclusion without naming source scope.

## Escalation

- Route unclear source scope to Conductor.
- Route truth/proof concerns to Steward.

## Exit / Handoff

- Next role or folder: `02_judgment`
- Signal required: evidence/source-check
- Memory impact: check
