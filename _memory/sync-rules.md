# Claude / Codex Sync Rules

Status: Root sync draft
Date: 2026-06-05

## Purpose

the OS must work across Claude-facing and Codex-facing instruction surfaces without creating two competing operating systems.

Root rule:

```text
One rule should have one canonical source. Other surfaces may point to it or summarize it.
```

## Canonical Sources

| Rule Type | Canonical Source |
|---|---|
| Root identity | `CLAUDE.md` |
| Root current context | `CONTEXT.md` |
| Codex-facing root loader | `AGENTS.md` pointing to `CLAUDE.md` and root source files |
| Root routing | `ROUTING.md`, `_routing/router-contract.md` |
| Destination routing | `_routing/destination-map.md` |
| Brand Guardian, proof, refusal, correction | `_governance/brand-guardian.md` |
| Memory behavior | `_memory/MEMORY-ROUTER.md` |
| Memory law | `_memory/memory-rules.md` |
| OS-owned log timestamp and ownership rules | `_memory/log-rules.md` |
| Decisions | `_memory/decision-log.md` |
| Decision-source lookup | `_memory/decision-source-index.md` |
| Source improvement | `_memory/source-improvement-rules.md` |
| Sync/parity behavior | `_memory/sync-rules.md` |
| Connectivity and live-system boundaries | `_connectivity/` |
| Root role index, role-status registry, compact agent doctrine, role contracts, and agent stages | `_agents/ROLE-INDEX.md`, `_agents/ROLE-STATUS.json`, `_agents/[role]/doctrine/*.md`, `_agents/[role]/CONTRACT.md`, `_agents/[role]/stages/[stage]/CONTRACT.md` |
| Handoff behavior and handoff packets | `_handoffs/README.md`, `_handoffs/HANDOFF-TEMPLATE.md`, `_handoffs/HANDOFF-LOG.md` |
| Project-local context | `[PROJECT]/CLAUDE.md`, `[PROJECT]/CONTEXT.md`, `[PROJECT]/ROUTING.md` |
| Stage behavior | `[PROJECT]/stages/[NN_stage]/CONTRACT.md` |

## Duplication Rule

Do not maintain two full independent versions of the same operating rule.

Allowed:

- Short pointers.
- Summaries with canonical file links.
- Project-local overrides that explicitly identify the root rule they override.

Not allowed:

- Copying root governance law into each project folder.
- Maintaining separate Claude and Codex versions of the same rule without a canonical source.
- Letting old ExampleLegacy or client files silently outrank the OS root law.

## Root CLAUDE / AGENTS Sync

`CLAUDE.md` is the canonical Layer 0 identity.

`AGENTS.md` is the Codex-facing root loader and sync pointer.

When root identity, routing, governance, memory, or connectivity behavior changes:

1. Edit the canonical source first.
2. Check whether `AGENTS.md` still points to the right source files.
3. Update `AGENTS.md` only when Codex-facing load order or summary behavior changed.
4. Record durable sync decisions in `_memory/decision-log.md`.

## Project Inheritance

Project-local files should say:

```text
This project inherits root governance, routing, memory, connectivity, and agent rules unless a local override is stated here.
```

Local overrides must include:

- What root rule is being narrowed or extended.
- Why the local condition exists.
- Whether it is temporary or durable.
- Who approved it, if approval matters.

## Resume Rule

When a tool, editor, or session context drops, the next agent should use runtime Tier 0 rather than relying on chat memory or loading all root evidence.

Minimum resume load is runtime Tier 0:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

After Tier 0, load only task-specific Tier 1 sources named by the route card or load index. Load triggered role doctrine before full role contracts. Load `ROUTING.md`, `_memory/context-load-standard.md`, decision logs, run logs, handoff logs, role contracts, generated maps, and project-local memory only as targeted evidence when the task requires them.

## Change Rule

When editing an operating rule:

1. Identify the canonical source.
2. Edit the canonical source first.
3. Update pointer files only if the pointer became stale.
4. Add or update a decision-log entry if the change records a durable decision.
5. Add a source-improvement note if the change came from a correction.

## Drift Check

Run a drift check when:

- Root law and project-local files disagree.
- Claude-facing and Codex-facing instructions disagree.
- A stale path appears active.
- A project folder duplicates root governance or memory.
- An agent asks a question already answered in root files.

Drift check output:

```text
Sync check:
- Conflicting surfaces:
- Canonical source:
- Drift:
- Proposed correction:
- Approval needed:
```
