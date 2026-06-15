# Decision Packet Standard

Status: Root routing standard
Date: 2026-06-05

## Purpose

the OS should not ask the operator vague or blind questions.

When a decision is needed, the system must do the thinking work first: load the relevant memory, identify what has already been settled, frame the remaining decision, show the options and tradeoffs, recommend a default, and then ask for approval or override.

Short rule:

```text
Do not ask the operator to decide from missing context.
Hand the operator a decision packet.
```

## When To Use

Use a decision packet when:

- The next move depends on operator judgment.
- The choice affects root law, routing, memory, governance, connectivity, or project structure.
- A project status is unclear.
- Multiple plausible paths exist and each has a different consequence.
- The agent is tempted to ask a broad question like "what next?" or "is there more?"
- A prior discussion likely answered the question, but context may have dropped.
- A file/reference placement decision remains unclear after the OS has inspected the file, nearby instructions, indexes, and destination map.

Do not use a decision packet for trivial confirmations or low-risk one-step tasks.

## Required Context Check

Before asking for a decision:

1. Load Tier 0 from `_memory/context-load-standard.md`.
2. Load `_routing/router-contract.md` and `_routing/destination-map.md` only if destination or routing authority is unresolved.
3. Load `_memory/MEMORY-ROUTER.md` when memory relevance may affect the decision.
4. Load `_memory/decision-source-index.md` if the decision may already have been answered elsewhere.
5. Load `_memory/decision-log.md` only when a targeted decision-log lookup is required.
6. Load local project or stage files if the decision is project-specific.

If saved files already answer the question, proceed from the saved answer. Do not ask the operator to repeat it.

## Packet Format

```text
Decision packet:
- Decision needed:
- Why this decision is needed now:
- What is already settled:
- Relevant source files:
- Options:
  1. [Option]
     - Tradeoff:
     - Risk:
  2. [Option]
     - Tradeoff:
     - Risk:
- Recommended default:
- Reason:
- What I will do if approved:
- What remains open after this:
```

## Question Standard

The final question should be specific and approval-oriented.

For file/reference placement, do not ask the operator to classify the file from scratch. Ask only for approval or override of the OS's recommended placement.

Good:

```text
Approve the recommended default, or choose option 2?
```

Good:

```text
Should I apply this only to ExampleWeb, or to both ExampleWeb and ExampleAgency in the cleanup pass?
```

Bad:

```text
What do you want to do?
```

Bad:

```text
Is there more?
```

Bad:

```text
Should I continue?
```

## Finalization Rule

At the end of a substantial pass, do not ask a vague continuation question.

Instead:

1. State exactly what was handled.
2. List changed and reviewed files.
3. State what remains open.
4. Name the recommended next owner and next action.
5. If the operator judgment is needed, present a decision packet.
6. If no judgment is needed, state the next queued build item from the roadmap.

The final question, when needed, must be contextual and specific.
