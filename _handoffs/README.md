# Handoffs


Status: Root handoff lane
Date: 2026-06-05

## Purpose

This folder holds handoff packets between the OS roles, sessions, projects, and stages.

Short rule:

```text
Work should not vanish into chat. It should land in a handoff, a context file, a decision log, or an output folder.
```

## When To Use

Use this folder when:

- Work moves from one root role to another.
- A session ends with unfinished root work.
- A project or stage needs a clean next-action packet.
- A correction changes routing, memory, governance, connectivity, or agent behavior.
- Context loss would make the next session reconstruct too much from chat.

## Files

- `HANDOFF-TEMPLATE.md`: standard handoff packet.
- `HANDOFF-LOG.md`: chronological index of important handoffs.
- `PROJECT-HANDOFF-STATE.md`: current project and project-like lane handoff state.

## Project Handoff Architecture

Project handoff behavior is governed by:

- `_routing/project-handoff-architecture-standard.md`

Before substantial project work moves, the OS should check `PROJECT-HANDOFF-STATE.md` and the relevant project-local `CLAUDE.md`, `CONTEXT.md`, `ROUTING.md`, memory, governance, connectivity, and stage contracts.

The project handoff state is a routing aid, not a replacement for project-local truth.

## Default Receiving Role

When the receiving role is unclear, route first to Conductor.

Conductor should then decide whether the next owner is Steward, Keeper, Recorder, Librarian, Sentinel, Signal, Warden, Voice, a project router, or the operator.
