# Hello Command Standard

Status: Root routing standard draft
Date: 2026-06-07

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This file defines the the OS `hello` command.

Short rule:

```text
Hello is an entrance command, not a time-based automation.
```

## Owner

Conductor owns entrance routing.

Keeper owns memory judgment when prior state matters.

Librarian owns findability of the command and response path.

Signal owns the visible signal shape when work moves beyond greeting.

## Operator-Facing Action

the operator says or runs:

```text
hello
```

Accepted natural-language variants include:

- `hello`
- `good morning`
- `gm`
- `start the OS`
- `enter the OS`

## System Action

the OS MUST treat the command as an entrance request for the current workspace.

the OS MUST respond with the defined entrance response and then wait for the first scoped work item.

the OS MUST NOT create a time-based login item, scheduled task, service, background process, or live automation from the hello command.

## Defined Response

The response MUST include:

- Acknowledgement that the OS entrance is loaded.
- The current workspace path.
- The default scope assumption: root unless the operator names a project, folder, or file.
- The root entry sources to rely on: `CLAUDE.md`, `CONTEXT.md`, `ROUTING.md`, `_memory/MEMORY-ROUTER.md`, `_handoffs/README.md`.
- The current root build focus from `CONTEXT.md` when available.
- One concise scope prompt for the first work item.

Default operator-facing response:

```text
Command Center OS loaded.
Workspace: <your local path to command-center-os>
Default scope: root unless you name a project, folder, or file.
Entry sources: CLAUDE.md, CONTEXT.md, ROUTING.md, _memory/MEMORY-ROUTER.md, _handoffs/README.md.
Current focus: complete operator onboarding, then prove a route on the sample project.
What should enter the OS now: root work, a project lane, or an intake item?
```

## MUST

- the OS MUST keep the command local to the current workspace.
- the OS MUST keep the first response short and deterministic.
- the OS MUST load or rely on saved root files before treating follow-up work as settled context.
- the OS MUST ask no more than one scope question after the response unless the operator's next request requires a decision packet.
- the OS MUST route follow-up work through `ROUTING.md` and the authority triad when the work is meaningful.

## MUST NOT

- the OS MUST NOT treat `hello` as permission to resume an unfinished pass automatically.
- the OS MUST NOT infer a project lane unless the operator names it or the prompt clearly identifies it.
- the OS MUST NOT inspect unrelated projects, old ExampleLegacy paths, live systems, credentials, or external accounts from the hello command.
- the OS MUST NOT create durable memory from the greeting alone.

## Inputs

- Natural-language `hello` style command.
- Optional command-line invocation through `_routing/atx_hello.py` or root `hello.ps1`.
- Root `CONTEXT.md` for current focus.

## Outputs

Hello response:

```text
the OS entrance loaded.
Workspace: [path]
Default scope: [scope]
Entry sources: [files]
Current focus: [focus]
[one concise scope prompt]
```

## Acceptance Test

This standard passes when:

- `hello` produces the defined entrance response.
- The response names the workspace and entry sources.
- The response does not start hidden automation.
- The response asks one scoped next-action question.

## Failure Test

This standard fails when:

- `hello` launches a time-based startup process.
- `hello` expands into unrelated folders before the operator names a scope.
- `hello` asks vague questions or requires the operator to reconstruct the OS state.
- `hello` writes memory or handoff state without a real work item.

## Escalation

Escalate to the operator with a decision packet when the hello command is being changed into:

- A live dashboard control.
- A login item, scheduled task, service, or background automation.
- A project-activation trigger.
- A command that touches live systems, credentials, external accounts, public claims, client commitments, legal/compliance, or financial state.
