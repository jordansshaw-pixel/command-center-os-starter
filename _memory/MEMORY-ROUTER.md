# Memory Router


Status: Root memory draft
Date: 2026-06-05

## Identity

the OS memory is carried by three related roles:

- Keeper: veteran memory and continuity judgment.
- Recorder: archivist, exact record, logs, provenance, and version history.
- Librarian: library, index, placement, and retrieval.

Short rule:

```text
Keeper remembers what matters.
Recorder preserves what happened.
Librarian makes it findable.
Conductor uses memory to route.
```

## Authority Triad Relationship

All meaningful work MUST resolve memory judgment as part of the authority triad:

- Conductor owns routing and next destination.
- Keeper owns memory judgment and what should shape future work.
- Steward owns truth authority, proof, refusal, and correction.
- Librarian owns findability and source pointers after the right authority is known.

Memory judgment is not optional when a correction, route, artifact, agent behavior, project state, generated interface, or durable source changes. If the finding does not need memory, Keeper or the session runner must state the no-write reason.

## Purpose

The Memory Router prevents the OS from losing serious work in chat, repeating old discovery, or turning corrections into one-time edits.

Context load is governed by:

- `_memory/context-load-standard.md`
- `_memory/SESSION-BOOT-STATE.md`

Memory relevance includes no-load judgment. Keeper should prevent unnecessary loading of broad logs, long decision history, role contracts, and project-local memory when the task can be routed from compact boot state and targeted sources.

Memory should answer:

- What findings should be saved?
- Where should they be saved?
- What should remain in chat only?
- What should update durable memory versus project-local context?
- What requires approval before becoming a rule?
- What should Conductor know before routing next time?
- What log, if any, needs an exact timestamped record?

## When Memory Must Be Checked

Run a memory check:

- At session start when the task touches an existing project, agent, governance area, or prior open loop.
- Before declaring a decision open when the user indicates it may already have been answered.
- Before substantial root routing, governance, project, or agent work.
- Before Steward review when prior correction or truth decisions may matter.
- Before project cleanup or stale path rewrites.
- Before finalizing a long analysis or build pass.
- During handoff, resume, or context reconstruction.

For resume or context reconstruction, use `_memory/context-load-standard.md` before loading broad memory evidence.

Memory check output:

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

Authority-triad memory output:

```text
Memory judgment:
- Prior memory checked:
- Durable write needed: [yes | no]
- Destination if yes:
- No-write reason if no:
- Routing impact:
- Truth-authority impact:
```

## What Must Be Saved

Save durable findings when a session produces:

- Reusable analysis.
- Architecture findings.
- Governance or doctrine decisions.
- Routing changes.
- Memory, source-improvement, or sync rules.
- Connectivity or tool-permission facts.
- Project status updates.
- Corrections that should affect future behavior.
- Decisions the operator made.
- Open loops that matter later.

Do not leave durable findings only in chat unless the operator explicitly says not to save them.

## Default Destinations

| Memory Type | Default Destination |
|---|---|
| Unsorted incoming references or artifacts | `_intake/drop/` |
| Operator truth, voice, judgment, load, approval, and truth-scope rules | `_operator/` |
| Governance, doctrine, proof, refusal, brand law | `_governance/` |
| Routing rules and destination behavior | `ROUTING.md`, `_routing/` |
| Memory rules, log rules, decisions, indexes, source improvement | `_memory/` |
| Connectivity, permissions, live-system boundaries | `_connectivity/` |
| Agent contract findings | `_agents/` |
| Project-specific state | `[PROJECT]/CONTEXT.md`, `[PROJECT]/_memory/` when created |
| Stage-specific output | `[PROJECT]/stages/[NN_stage]/output/` |
| Research/evidence | Nearest `references/` folder or `_governance/` if root architecture research |
| Handoff roadmaps | Nearest project/system planning folder |

If the correct destination is unclear, load prior decisions and use `_routing/decision-packet.md` before asking the operator for judgment.

If a decision appears missing, check `_memory/decision-source-index.md` before calling it open.

## Log Timestamp Rule

New OS-owned log entries MUST follow `_memory/log-rules.md`.

Minimum timestamp format:

```text
YYYY-MM-DD HH:mm:ss +/-HH:MM
```

Do not fabricate timestamps for historical date-only entries when the exact time is unknown.

## Project Locality Rule

Project-specific operational findings, planning outputs, implementation state, connectivity pointers, live-system boundaries, decisions, open loops, and stage truth MUST be saved in the project workspace when the project needs them to operate.

Root memory MAY save the general rule, coarse status, pointers to project-local source files, and command-center reference analysis that mentions or compares projects. Root memory MUST NOT become required runtime memory, workflow state, data storage, or operational authority for a project.

Short rule:

```text
If the project needs the fact to run, save it in the project.
```

## Layer 3 Versus Layer 4

Use the ICM distinction:

- Layer 3 source files improve the factory.
- Layer 4 working artifacts improve one run.

Editing the output fixes one run. Editing the source fixes every future run.

If the operator gives the same correction repeatedly, or a correction affects how the OS should behave later, flag it as a source-improvement candidate.

## Role Behavior

### Keeper

Keeper decides which memory matters now.

Keeper should surface:

- Relevant decisions.
- Constraints.
- Prior corrections.
- Known stale assumptions.
- Reusable lessons.
- Current state.
- Open loops.
- What source file owns the truth.

Keeper should not dump history. Memory must be concise and routing-useful.

### Recorder

Recorder preserves the exact record:

- What happened.
- When it happened.
- What was decided.
- What source proves it.
- What changed.
- What version is authoritative.

Use Recorder when dates, provenance, prior versions, audit trail, or exact source references matter.

### Librarian

Librarian protects findability:

- Where the record should live.
- What should be indexed.
- What duplicate or stale paths exist.
- What should be archived, linked, or surfaced.
- What root or project file should point to the source.

Use Librarian when memory exists but may not be findable later.

## Memory Write Packet

Use this packet when saving or updating durable memory:

```text
Memory write:
- Type: [decision | correction | finding | rule | handoff | open-loop | source-improvement]
- Scope: [root | project | stage | agent | connectivity]
- Source:
- Destination:
- Summary:
- Reason it matters later:
- Approval status: [user-confirmed | inferred | provisional]
- Next owner: [role]
```

## Approval Standard

Do not convert an inference into durable law without labeling it.

Memory status labels:

- User-confirmed: the operator directly stated or approved it.
- Source-confirmed: supported by an existing file or authoritative reference.
- Inferred: reasoned from available material, not directly confirmed.
- Provisional: useful draft pending later review.

Durable root law should be user-confirmed or clearly marked as draft/provisional.

## Handoff Rule

Before finalizing substantial work, answer:

```text
What did we learn?
Where was it saved?
What remains open?
Which role should pick it up next?
```

If a finding matters again, save it or name the destination that should receive it next.
