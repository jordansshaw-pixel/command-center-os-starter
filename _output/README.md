# Output Lane

Status: Root output lane
Edition: Community / distributable starter

## Purpose

This folder is the local output lane for root-level OS outputs that need to be evaluated without
opening another workspace.

Short rule:

```text
Reviewable OS output should live inside the workspace unless a project or stage contract says otherwise.
```

## What Belongs Here

Use this folder for:

- Root review packets.
- Evaluation snapshots.
- Working exports of root architecture.
- Operator-facing summaries that are outputs, not source law.
- Temporary review copies that should be visible beside the OS source files.

## What Does Not Belong Here

Do not use this folder for:

- Root law that belongs in `CLAUDE.md`, `ROUTING.md`, `_governance/`, `_routing/`, `_memory/`, `_agents/`, `_connectivity/`, or `_handoffs/`.
- Project-stage outputs that already belong in `[PROJECT]/stages/[NN_stage]/output/`.
- Client-facing deliverables unless routing explicitly places them here.
- Secrets, credentials, private keys, or live-system exports.

## Layer Rule

This is a Layer 4 output lane. Layer 4 output can be edited, reviewed, compared, or discarded.

If an output correction should change future OS behavior, route the correction back to the Layer 3
source file that owns the rule.

## Generated Interface Rule

Human-facing architecture interfaces are truth surfaces. They must be updateable from a named source
of truth at inception and during execution.

Generated review artifacts must name:

- Source of truth.
- Generator or update command.
- Output path.
- Whether the artifact is a snapshot or live source.

The OS ships generators for an architecture interface:

- Source: `_routing/architecture-map.json`
- Generator: `_routing/generate-architecture-wireframe.js`
- Output: `_output/` (generated locally; not committed in this edition)

## Naming Pattern

Prefer clear dated names:

```text
YYYY-MM-DD-short-output-name.md
```

Use subfolders only when a pass produces multiple files that should travel together.

## Index

Maintain `_output/OUTPUT-INDEX.md` for reviewable outputs that should be easy to find later.
