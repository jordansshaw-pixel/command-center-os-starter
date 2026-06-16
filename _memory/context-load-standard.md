# Context Load Standard

Status: Root memory and routing standard
Date: 2026-06-07
Timestamp: 2026-06-07 15:40:55 -05:00

## Purpose

This standard prevents the OS recovery from consuming too much session context before work begins.

Short rule:

```text
Boot compactly, classify the work, then load only the evidence needed for that work.
```

## Problem

Long sessions are creating a system memory problem when new conversations spend a large share of context on root files, logs, and repeated load rules.

the OS must preserve memory without forcing every session to reload the whole operating system.

## Load Tiers

### Tier 0 - Boot Load

Load these first for workspace entry, recovery, or broad root orientation:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

Tier 0 should be enough to answer:

- What is the OS?
- What state is the OS in now?
- What is the next safe routing move?
- Which source should be loaded next, if any?

`ROUTING.md` and this full standard are canonical source/audit files, not default runtime load files after the 2026-06-07 cutover.

### Tier 1 - Task Routing Load

After Tier 0, load only the smallest relevant source set for the task type.

| Task Signal | Load Next |
|---|---|
| Operator truth, load, voice, approval, judgment | Relevant `_operator/` file only |
| Governance, proof, refusal, root law | `_governance/steward.md` and relevant governance source |
| Routing, destination, standards, handoff architecture | Relevant `_routing/` standard or contract |
| Memory behavior or context recovery | `_memory/MEMORY-ROUTER.md`, `_memory/memory-rules.md`, or relevant memory source |
| Decision already may exist | `_memory/decision-source-index.md`, then targeted source lookup |
| Role assignment, role availability, or role selection | `_agents/ROLE-STATUS.json`, `_agents/ROLE-INVOCATION-MATRIX.md`, triggered `_agents/[role]/doctrine/*.md`, then `_agents/ROLE-INDEX.md` if human-readable role context is needed |
| Specific role work | Triggered `_agents/[role]/doctrine/*.md`; load specific `_agents/[role]/CONTRACT.md` and stage `CONTRACT.md` only when doctrine is insufficient, the role is primary executor, or durable source truth changes |
| Project work | Project `CLAUDE.md`, `CONTEXT.md`, `ROUTING.md`, then project memory/governance/connectivity only as needed |
| Handoff or resumed unfinished work | `_handoffs/PROJECT-HANDOFF-STATE.md` or the specific handoff packet |
| Log or audit reconstruction | The specific log file and timestamp range needed |

### Tier 2 - Evidence Load

Load large logs, long research files, project archives, generated interface maps, and historical decision records only when the task requires evidence from them.

Tier 2 sources include:

- `_memory/decision-log.md`
- `_agents/AGENT-RUN-LOG.md`
- `_handoffs/HANDOFF-LOG.md`
- Long governance research files.
- Generated maps and output indexes.
- Project-local decision logs and audit logs.

These files are evidence stores, not default boot memory.

## Context Budget Rule

the OS should treat context as an operating resource.

Default behavior:

- Do not load broad logs just because they exist.
- Do not load every root standard before classifying the task.
- Do not load `ROUTING.md` or this full standard during ordinary startup unless source-law, audit, or rule-edit work requires them.
- Do not load role contracts merely to select roles; load triggered role doctrine first.
- Do not load role contracts unless doctrine is insufficient, the role is primary executor, or the role contract/stage/source truth is being edited or audited.
- Do not load project-local memory unless project work is in scope.
- Prefer indexes and current-state files before long chronological logs.

If a new session has already consumed a large share of context before work begins, the OS should stop expanding source load and switch to targeted lookup.

## Boot-State Rule

`_memory/SESSION-BOOT-STATE.md` is the compact current-state file for recovery.

It should stay short and point outward.

It may include:

- Current root state.
- Current active build focus.
- Current next queued work.
- Current load warnings.
- Pointers to the source files that hold full evidence.

It must not become:

- A duplicate decision log.
- A duplicate roadmap.
- A duplicate role index.
- A dump of project state.
- A substitute for source-of-truth files.

## Recovery Procedure

When chat, editor, tool, or session context drops:

1. Load runtime Tier 0.
2. Classify the incoming request.
3. Check `_memory/SESSION-BOOT-STATE.md` for current warnings and next routes.
4. Load Tier 1 sources only for the task.
5. Load Tier 2 evidence only when a specific decision, audit record, proof path, or timestamped history is needed.
6. Continue from saved source state instead of asking the operator to reconstruct the session.

## Acceptance Test

This standard passes when a future new conversation can enter the OS, identify scope, and start useful work without loading `_memory/decision-log.md`, `_agents/AGENT-RUN-LOG.md`, role contracts, or project-local memory unless the request requires them.

## Failure Test

This standard fails when the OS consumes major context by loading broad logs, all role files, all project state, or every root standard before routing the task.

## Ownership

- Conductor owns routing and load sequence.
- Keeper owns memory relevance and no-load judgment.
- Recorder owns exact records and logs as evidence stores.
- Librarian owns compact pointers and findability.
- Steward may require deeper source load when truth, proof, refusal, or correction is at stake.
