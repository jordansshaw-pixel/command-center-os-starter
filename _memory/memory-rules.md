# Memory Rules

Status: Root memory rules draft
Date: 2026-06-05

## Purpose

This file defines what the OS must remember, what it must not over-store, and how memory affects future routing.

`MEMORY-ROUTER.md` defines role behavior. This file defines memory law.

## Core Rule

Serious work should not remain only in chat.

If a session produces reusable analysis, decisions, architecture findings, routing changes, governance rules, corrections, project-state updates, or open loops, the OS must identify a memory destination before finalizing.

## What Counts As Memory

Save memory when the item would prevent:

- Repeated discovery.
- Wrong routing.
- Stale path assumptions.
- Lost correction.
- Source drift.
- Client/project confusion.
- Rebuilding context after a session or editor reset.

## Memory Types

| Type | Meaning | Default File |
|---|---|---|
| Decision | the operator or the OS chose a direction. | `_memory/decision-log.md` or project decision log. |
| Finding | Reusable analysis or architecture truth. | Nearest governance, routing, memory, or references file. |
| Correction | Something was wrong and the correction matters later. | `_memory/source-improvement-rules.md` or affected source file. |
| Open loop | Known unresolved item. | Roadmap, decision log, or project context. |
| Handoff | Current state and next owner. | `_handoffs/` or nearest project/stage handoff file. |
| Source improvement | Output correction should become future system behavior. | `_memory/source-improvement-rules.md` and affected source file. |

## Memory Labels

Every durable memory should be one of:

- User-confirmed.
- Source-confirmed.
- Inferred.
- Provisional.

Do not silently promote inferred memory into law.

## What Not To Save

Do not save:

- Temporary phrasing that does not matter later.
- Exploratory guesses unless labeled provisional.
- Secrets, credentials, tokens, or private keys.
- Old folder assumptions as active truth.
- Duplicate copies of root law inside project folders.

## Context Loss Rule

If tool, editor, chat, or session context drops, the OS treats that as a memory-resume event.

The next agent should use `_memory/context-load-standard.md`:

1. Load Tier 0.
2. Use `_memory/SESSION-BOOT-STATE.md` for compact current state.
3. Classify the task.
4. Load Tier 1 sources only for the task.
5. Load Tier 2 evidence stores only when a specific prior decision, audit record, handoff, proof path, or project state is needed.

The agent should continue from saved source state rather than requiring the operator to reconstruct the session from memory.

## Memory Check Format

```text
Memory check:
- Relevant prior decisions:
- Known constraints:
- Current state:
- Open loops:
- Source of truth:
- What not to redo:
- Routing impact:
```

## Memory Write Format

```text
Memory write:
- Type:
- Scope:
- Source:
- Destination:
- Summary:
- Reason it matters later:
- Approval status:
- Next owner:
```

## Source Improvement Trigger

If the operator corrects an agent about a system rule, repeated decision, routing behavior, or memory failure, the OS must consider whether the source file needs updating.

Default route:

- Routing behavior problem -> `_routing/router-contract.md`
- Memory behavior problem -> `_memory/MEMORY-ROUTER.md` or `_memory/memory-rules.md`
- Governance/truth problem -> `_governance/brand-guardian.md`
- Role-world, contract, or stage problem -> `_agents/ROLE-INDEX.md`, `_agents/[role]/CONTRACT.md`, or `_agents/[role]/stages/[stage]/CONTRACT.md`
- Handoff problem -> `_handoffs/README.md` or `_handoffs/HANDOFF-TEMPLATE.md`
- Project-local problem -> project `CONTEXT.md`, `ROUTING.md`, or `_memory/`

## Decision Packet Rule

If memory shows that a decision has already been discussed or settled, do not ask the operator to decide blindly.

Instead:

1. Surface the relevant prior decision or open loop.
2. Name the source file.
3. Explain what remains genuinely unresolved.
4. Provide options, tradeoffs, and a recommended default.
5. Ask a specific approval or override question.

## Missing Decision Rule

Absence from `_memory/decision-log.md` does not prove a decision is unresolved.

Before labeling a decision open:

1. Check `_memory/decision-source-index.md`.
2. Search the listed root decision sources.
3. If the answer is found, import a compact entry into `_memory/decision-log.md`.
4. If the answer is not found, report the gap as "not found in searched sources," not as "never decided."

## Finalization Rule

Before finalizing substantial work, answer:

```text
What did we learn?
Where was it saved?
What remains open?
Which role should pick it up next?
```

If a decision remains, use `_routing/decision-packet.md` instead of a vague continuation question.
