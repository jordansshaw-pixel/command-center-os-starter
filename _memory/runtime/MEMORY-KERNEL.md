# Memory Kernel

Status: active Tier 0 runtime
Date: 2026-06-07

## Purpose

Classify memory need without loading long logs.

Canonical archive:

- `_memory/source-archive/2026-06-07/MEMORY-ROUTER.md`

## Memory Sequence

1. Decide whether memory is check, write, update-source, or no-write.
2. Prefer compact current-state files and indexes before chronological logs.
3. Load a specific evidence file only when the question names a decision, timestamp, run, handoff, project state, or proof path.
4. Preserve exact record through Recorder when archiving, pruning, or reconstructing.
5. Make durable outputs findable through Librarian.

## No-Load Defaults

Do not load `_memory/decision-log.md`, `_agents/AGENT-RUN-LOG.md`, `_handoffs/HANDOFF-LOG.md`, project-local logs, generated maps, or archives unless targeted evidence requires them.

## Output

Memory judgment: prior memory checked, durable write needed, destination, no-write reason, routing impact, truth impact.
