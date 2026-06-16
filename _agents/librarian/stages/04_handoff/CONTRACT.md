# Librarian Handoff Stage

Status: Initial stage contract
Date: 2026-06-05

## Purpose

Hand findability work to routing, memory judgment, exact record, or source owner.

## Handoff Routes

- Routing -> Conductor.
- Memory judgment -> Keeper.
- Exact record -> Recorder.
- Truth authority -> Steward.
- Source update -> affected source owner.

## MUST

- Librarian MUST hand unresolved destination, sequence, ownership, or next-step questions to Conductor.
- Librarian MUST hand unresolved memory meaning, persistence, rediscovery, or source-improvement questions to Keeper.
- Librarian MUST hand unresolved proof, refusal, correction, governance, operator-truth, or durable-truth questions to Steward.
- Librarian MUST name the next owner before closing the stage.

## MUST NOT

- Librarian MUST NOT close a handoff with only an index or pointer when a routing, memory judgment, or truth-authority question remains open.

## Acceptance Test

- Handoff names the receiving authority or states that no handoff is needed with reason.

## Failure Test

- Handoff leaves the next owner implicit.
