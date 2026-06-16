# AGENTS.md


Status: Codex-facing root instruction surface
Date: 2026-06-07

## Purpose

This file is the Codex-facing companion to root `CLAUDE.md`.

It must stay in sync with the OS root law without becoming a second independent rulebook.

Canonical source rule:

```text
CLAUDE.md is the canonical root identity.
AGENTS.md is the Codex-facing loader and sync pointer.
```

## Required Load Order

Before substantial work, Codex should use the runtime Tier 0 boot path and then the tiered load system when deeper source evidence is needed.

Runtime Tier 0 boot load:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

After Tier 0, load only the task-specific source named by the runtime route card or load index. `ROUTING.md`, `_memory/context-load-standard.md`, broad logs, decision history, role contracts, project memory, and generated maps are evidence/source files and should not load by default.

## Operating Rules

Follow root law:

- the OS exists to keep the operator's judgment, memory, ventures, clients, and agents aligned with what is true before anything moves.
- `_operator/` is the source layer for the operator's operator truths, voice, judgment, load, and approval standards.
- `_intake/` is the drop zone for unsorted references and artifacts; the OS classifies and routes them after inspection.
- `_routing/deterministic-contract-language-standard.md` prevents loose contract language from allowing interpretation drift.
- Steward owns oath, truth, proof, refusal, and correction authority.
- Conductor owns routing, sequence, handoff, and operating discipline.
- Keeper, Recorder, and Librarian own memory relevance, exact record, and findability.
- All meaningful work must resolve through the authority triad in `CLAUDE.md` and `ROUTING.md`: Conductor for routing, Keeper for memory judgment, and Steward for truth authority. Librarian makes work findable but does not replace those authorities.
- `_routing/multi-agent-engagement-standard.md` decides when the OS opens a structured multi-agent engagement instead of running roles inline.
- Standing operator instruction: when `_routing/multi-agent-engagement-standard.md` triggers and the work benefits from separate bounded workstreams, use available sub-agent, delegated-agent, or parallel-agent tooling where platform/tool policy permits it. Treat this as the operator's durable explicit delegation instruction for work in the OS; still obey live-system gates and scoped write boundaries.
- Do not treat legacy, external, or out-of-scope paths as active truth unless root files or the operator explicitly mark them active.
- Do not expand scope into related folders without a routing reason or user approval.
- Do not duplicate root law inside project files; point to canonical root files unless a local override is required.
- Do not ask the operator vague or blind questions. If a decision is needed, provide a decision packet with context, options, tradeoffs, recommended default, and a specific approval/override question.

## Sync Rule

When `CLAUDE.md` changes in a way that affects Codex behavior, check whether `AGENTS.md` needs a pointer or summary update.

When `AGENTS.md` changes in a way that affects root identity, routing, governance, memory, or connectivity, update the canonical source file first or record why this file is only a Codex-facing pointer.

Use `_memory/sync-rules.md` as the canonical sync policy.

## Context Loss Rule

If chat, editor, or tool context drops, do not ask the operator to reconstruct settled decisions from memory.

Resume through runtime Tier 0, then load targeted Tier 1 sources only after classifying the request.

Use `_memory/SESSION-BOOT-STATE.md` for compact current state. Use `ROUTING.md`, `_memory/context-load-standard.md`, `_memory/decision-log.md`, `_agents/AGENT-RUN-LOG.md`, role contracts, handoff logs, and project-local memory only as targeted evidence stores.

## Finalization Rule

Before finalizing substantial work, answer:

```text
What did we learn?
Where was it saved?
What remains open?
Which role should pick it up next?
```

Also list files changed or reviewed.

Do not end with a vague continuation question. If the operator needs to decide something, use `_routing/decision-packet.md`. If no decision is needed, state the next queued build item from the roadmap.
