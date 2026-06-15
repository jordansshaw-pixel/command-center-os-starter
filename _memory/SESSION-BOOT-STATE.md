# Session Boot State

Status: fresh-install recovery state
Edition: Community / distributable starter

## Current Root State

Command Center OS is a fresh install using runtime Tier 0 to reduce startup context load.

Runtime Tier 0:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

Do not load `ROUTING.md`, `_memory/context-load-standard.md`, broad logs, all role contracts, all
project files, or governance research by default.

## Standing Facts

- Runtime routing and memory kernels are the active Tier 0 boot path.
- `ROUTING.md` is compact active routing; `_routing/runtime/ROUTE-INDEX.md` is the active routing index.
- Route cards load only the sources and agent doctrine needed for the selected path.
- Sentinel is the mandatory root risk gate and fires on all non-trivial work.
- Large logs and archived source files are targeted evidence stores, not default boot files.

Source pointers:

- `_routing/runtime/`
- `_memory/runtime/`
- `_agents/ROLE-INVOCATION-MATRIX.md`
- `_agents/[role]/doctrine/`

## Open Loops

- **FIRST RUN — operator onboarding not yet complete. Run `_routing/runtime/routes/operator-onboarding.md`
  to populate `_operator/` and replace this boot state with your real operating state.**

## Default Recovery Move

1. Identify the likely workspace or folder.
2. Select the smallest matching route card from `_routing/runtime/ROUTE-INDEX.md`.
3. Load only the route card's Tier 1 sources.
4. Load Tier 2 evidence only when a specific prior decision, log entry, proof path, or audit record is needed.

## Next Owner

Conductor owns runtime route selection.

Keeper owns memory relevance.

Librarian owns pointer hygiene.
