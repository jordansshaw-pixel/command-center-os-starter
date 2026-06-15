# Route Card: Handoff

Status: active runtime card
Date: 2026-06-07

## Trigger

Pause, resume, transfer, next owner, project handoff, stage movement, or future-session state.

## Load Next

- `_agents/conductor/doctrine/routing-sequence-handoff.md`
- `_agents/signal/doctrine/signal-packets.md`
- `_agents/keeper/doctrine/memory-relevance.md`
- `_agents/recorder/doctrine/exact-record.md`
- `_agents/librarian/doctrine/findability-indexing.md`
- `_handoffs/PROJECT-HANDOFF-STATE.md` for project lanes.
- Specific handoff packet only when named.
- Project `ROUTING.md` and `CONTEXT.md` when scoped to a project.

## Required Roles

Conductor, Signal, Keeper, Recorder, Librarian. Add Warden for live-system boundary.

## Stop Conditions

Stop if receiving owner, folder/stage, memory destination, governance gate, connectivity gate, or blocker state is unknown.

## Output

Handoff signal or packet with current next action, blockers, stop conditions, memory impact, and receiving owner.

## Provenance

Source archive: `_routing/source-archive/2026-06-07/project-handoff-architecture-standard.md`.
