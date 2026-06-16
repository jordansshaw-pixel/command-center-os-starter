# Build Roadmap

Status: compact active roadmap
Edition: Community / distributable starter

## Purpose

Name the recommended build sequence for a fresh Command Center OS install without loading planning
history.

## Current Truth

Command Center OS is a fresh install being made the operator's own.

Operating rule:

```text
Truth before action. Routing before production. Proof before claims. Boundaries before live-system access.
```

Runtime Tier 0 is the default boot path:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

## Recommended First-Run Sequence

1. Complete operator onboarding (`_routing/runtime/routes/operator-onboarding.md`) to populate
   `_operator/` and replace the fresh-install boot state.
2. Run an end-to-end route on the sample project in `_examples/` to confirm the engine works
   (scaffold → fast-lane → handoff).
3. Optionally rename the agent crew to your own theme (`ROLE-GLOSSARY.md`).
4. Add your first real project folder at the repo root, keeping its operational truth local.
5. Connect live systems and secrets only after reading `_connectivity/` and setting up a private
   env vault.

## Do Not Expand Yet

Do not add live-system actions or new named roles until onboarding is complete and at least one route
has been proven on the sample project.

## Next Owner

Conductor owns sequence.

Librarian owns findability and indexes.

Keeper owns archive/reference memory judgment.

Steward owns governance truth.
