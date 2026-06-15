# Librarian Output Stage

Status: Initial stage contract
Date: 2026-06-05

## Purpose

Produce the findability artifact.

## Inherits

- `_routing/deterministic-contract-language-standard.md`
- `_agents/librarian/CONTRACT.md`

## MUST

- Librarian MUST produce a packet with destination, owner, approval state, risk, and next action when classifying intake.
- Librarian MUST update `_intake/INTAKE-INDEX.md` when processing files from `_intake/drop/`.
- Librarian MUST name whether the action is move, index, hold, or decision packet.
- Librarian MUST name the authority-triad state for routing, memory judgment, and truth authority when the output affects durable source, routing, memory, governance, agent behavior, project direction, or operator-facing workflow.

## MUST NOT

- Librarian MUST NOT output only a vague placement recommendation when the file came through `_intake/drop/`.
- Librarian MUST NOT ask the operator to choose reference, artifact, source, output, project, or stage before classification.
- Librarian MUST NOT close findability work as complete while routing, memory judgment, or truth authority remains unresolved.

## Outputs

- Index update.
- Placement recommendation.
- Intake classification packet.
- Pointer update.
- Findability correction.
- Authority-triad state.

## Acceptance Test

- Output names exact recommended destination, owner, approval state, risk, and next action.
- Operator-facing action remains `_intake/drop/`.
- Output names routing authority, memory judgment, and truth authority or gives a clear no-action reason for each.

## Failure Test

- Output asks the operator to classify the file before the OS inspection.
- Output leaves destination or next action implicit.
- Output treats indexing as complete while unresolved authority-triad questions remain.

## Exit

Move to `04_handoff`.
