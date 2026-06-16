# Agent Stage Framework


Status: Root agent-stage framework
Date: 2026-06-05

## Purpose

This framework gives every active OS agent a staged ICM workflow.

Short rule:

```text
An agent folder is not complete with only a role contract. A live agent needs stages that show how work enters, is judged, becomes output, and hands off.
```

## Standard Agent Stages

Each active root operating agent should use this stage spine:

```text
_agents/[role]/
  CONTRACT.md
  stages/
    01_intake/
      CONTRACT.md
    02_judgment/
      CONTRACT.md
    03_output/
      CONTRACT.md
    04_handoff/
      CONTRACT.md
```

## Stage Meanings

| Stage | Meaning | Primary Question |
|---|---|---|
| `01_intake` | Receive work and load required context. | What has entered this role, from whom, and why? |
| `02_judgment` | Apply the role's authority and constraints. | What does this role decide, review, stop, or route? |
| `03_output` | Produce the role's specific artifact. | What packet, finding, decision, or draft leaves this role? |
| `04_handoff` | Move state to the next role, folder, or memory destination. | Who owns the next move and what must they know? |

## Stage Rules

- Stages inherit from the role `CONTRACT.md`.
- Stages do not override root `CLAUDE.md`, `ROUTING.md`, Steward, or memory law.
- If a stage discovers risk, it routes through Sentinel.
- If a stage moves work, it routes through Signal/handoff.
- If a stage creates durable truth, it routes through Steward and memory.

