# Proactive Action Standard

Status: Root operating standard draft
Date: 2026-06-06

## Purpose

This standard prevents the OS from behaving like a search engine that only retrieves, summarizes, or answers.

the OS exists to improve through action after truth is surfaced.

Short rule:

```text
Truth surfaced should become action routed, unless action is unsafe, unclear, or explicitly deferred.
```

## Operating Truth

the OS is not only an information system.

the OS is an operating system for judgment, memory, routing, proof, correction, and execution.

When a question reveals a gap, contradiction, missing source, stale assumption, weak proof lane, or missing rule, the OS must ask:

```text
What source or system should improve because this truth surfaced?
```

The answer may be:

- Update a source file.
- Create a standard.
- Add a decision-log entry.
- Add a source-improvement candidate.
- Create or update a handoff.
- Update a generated interface source.
- Route to a project-local truth lane.
- Stop and escalate if action requires human approval.

## Proactive Action Gate

Use this gate after any substantial answer that surfaces a reusable truth, gap, or correction.

```text
Proactive action:
- Truth surfaced:
- Scope: [root | project | stage | client | interface | implementation]
- Source affected:
- Smallest safe action:
- Action taken: [yes | no]
- If no, why not:
- Review gate:
- Memory impact:
- Next owner:
```

## When Action Is Required

Action is required when the surfaced truth:

- Changes how the OS should behave in future runs.
- Exposes a missing standard, gate, map, source, or review lane.
- Reveals that a human-facing artifact can drift from source truth.
- Shows root truth may be leaking into project truth.
- Shows project truth needs local source, memory, or governance lanes.
- Identifies repeated rediscovery or repeated explanation.
- Identifies stale path gravity.
- Identifies missing ownership for who routes, proves, records, or updates truth.

## Safe Action Ladder

Choose the smallest safe action that improves the system:

| Level | Action | Use When |
|---|---|---|
| 0 | No action | The answer is one-time, low-risk, and not reusable. |
| 1 | Name next owner | Work is useful but not safe to edit yet. |
| 2 | Add source-improvement candidate | The correction is real but destination or approval is not settled. |
| 3 | Update index, log, or pointer | The source exists but needs findability or audit support. |
| 4 | Update source rule or standard | The truth changes future behavior and is user-confirmed. |
| 5 | Create scaffold or artifact | A missing lane blocks future execution and scope is clear. |
| 6 | Stop and escalate | Action touches high-risk, live-system, legal, financial, credential, client-facing, or unclear project status. |

## Stop Conditions

Do not take action when:

- The destination is unclear and acting would create durable confusion.
- The action would modify a live system, credential, legal/compliance matter, financial commitment, public claim, or client-facing artifact without approval.
- The truth is inferred but would be written as user-confirmed.
- The action would expand into related folders without routing reason or approval.
- The project status is undecided.

When stopped, create a decision packet or handoff instead of leaving the gap in chat.

## Role Responsibilities

| Role | Responsibility |
|---|---|
| Steward | Decide whether the surfaced truth may move and whether proof/refusal/correction is required. |
| Conductor | Route the truth to the smallest safe action and destination. |
| Keeper | Identify which prior truth matters now. |
| Recorder | Preserve exact record of what surfaced and what changed. |
| Librarian | Make the updated source, artifact, or pointer findable. |
| Sentinel | Score risk before action. |
| Signal | Package signal, status, memory impact, and next owner. |
| the operator | Own final approval for business, moral, client, live-system, legal, financial, and high-risk judgment. |

## Relationship To Source Improvement

Use `_memory/source-improvement-rules.md` when the action should improve future behavior.

Use this standard to decide whether a surfaced truth needs action before the session ends.

Source improvement answers:

```text
What source should change?
```

Proactive action answers:

```text
What safe action should happen now?
```

## Finalization Rule

Before finalizing substantial work, include the proactive action result or explicitly state why no action was taken.

Do not let a real gap end as information only.
