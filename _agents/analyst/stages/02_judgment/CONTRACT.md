# Analyst Judgment Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Judge evidence quality, confidence, and assumption boundaries.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/analyst/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Analyst owns this judgment stage.

## Operator-Facing Action

the operator does not need to classify evidence status before Analyst inspects the sources.

## System Action

the OS classifies evidence, assumptions, confidence, limitations, and downstream owner.

## Inputs

- Evidence intake packet.
- Source files or references.
- Prior decision/memory records.

## Required Checks

- Is each claim source-supported, inferred, provisional, contradicted, or unknown?
- Is the source local OS truth, project-local truth, imported reference, external/current-world evidence, or stale/legacy material?
- Does Brand Guardian, Sentinel, Warden, Keeper, Recorder, Librarian, or Conductor need review?

## MUST

- Analyst MUST separate evidence from interpretation.
- Analyst MUST identify source limitations.
- Analyst MUST assign a confidence level to material claims.

## MUST NOT

- Analyst MUST NOT collapse conflicting evidence into a clean answer.
- Analyst MUST NOT treat legacy or imported material as current truth without classification.

## Outputs

- Evidence judgment.
- Confidence map.
- Research gap list.
- Downstream review recommendation.

## Acceptance Test

- Judgment names each material claim, evidence status, confidence, limitation, and downstream owner.

## Failure Test

- Judgment produces a conclusion without evidence classification.

## Escalation

- Route truth/proof concerns to Brand Guardian / Steward.
- Route risk concerns to Sentinel.
- Route route/destination uncertainty to Conductor.

## Exit / Handoff

- Next role or folder: `03_output`
- Signal required: evidence/source-check
- Memory impact: check or write when durable
