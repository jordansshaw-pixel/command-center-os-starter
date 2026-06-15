# Tool Permissions

Status: Root tool-permission standard
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This file defines what the OS may do with tools, connectors, local paths, repos, deployments, automations, accounts, and live systems.

Short rule:

```text
Permission class determines movement.
```

## Owner

Warden owns permission stops and credential boundaries.

Conductor owns routing from permission class to next action.

Sentinel owns risk scoring.

the operator owns approval for live-system actions and credentials.

## Operator-Facing Action

the operator may ask for a tool or integration action directly.

the OS MUST classify permission before acting.

## Permission Classes

| Class | Meaning | Default Action | Approval Required |
|---|---|---|---|
| `reference-only` | the OS may read or cite non-secret saved facts and pointers. | Reference and route. | No, unless facts are stale or sensitive. |
| `read-only` | the OS may inspect without modifying state. | Inspect and report. | Approval may be required for sensitive systems. |
| `draft-only` | the OS may draft proposed changes without applying them. | Draft packet or plan. | No live approval until applying. |
| `local-edit` | the OS may edit files in the approved workspace. | Edit scoped files and verify. | No, if reversible and not live-system-adjacent. |
| `staged-change` | the OS may prepare a change that needs explicit review before live movement. | Create branch, patch, draft, or handoff as approved. | Yes before live application. |
| `live-action` | the OS would change a live system, account, repo, deployment, automation, DNS, CRM, analytics, payment, form, email, calendar, or public site. | Stop and request approval. | Yes. |
| `credential-handling` | the OS would create, use, move, inspect, or store credentials, secrets, tokens, keys, or access material. | Stop and route to Warden. | Yes. |
| `blocked` | the OS may not act under current source/approval state. | Stop. | Yes, plus missing condition must resolve. |

## MUST

- the OS MUST assign one permission class before tool movement.
- the OS MUST treat unknown permission as `blocked` until classified.
- the OS MUST treat credentials, secrets, private keys, tokens, recovery codes, payment data, and regulated data as `credential-handling`.
- the OS MUST treat DNS, deployments, repo pushes, CRM writes, automations, analytics changes, payment changes, form submissions, email sends, calendar writes, and public-site changes as `live-action`.
- the OS MUST use `draft-only` when the user asks for a plan, packet, proposal, or copy that does not change a live system.
- the OS MUST use `local-edit` only inside the current approved workspace and only when the edit is reversible and scoped.
- the OS MUST package permission questions with Signal when work moves to the operator, Warden, a project, or a future session.

## MUST NOT

- the OS MUST NOT use tool access merely because a connector or CLI is available.
- the OS MUST NOT convert `reference-only` or `read-only` into `live-action` without explicit approval.
- the OS MUST NOT store credentials in markdown, output files, chat summaries, handoffs, or project context.
- the OS MUST NOT write to a project repo, deployment, DNS, CRM, analytics, automation, payment, email, calendar, or form system without live-action approval.
- the OS MUST NOT ask the operator to choose a permission class before the OS inspects available context.

## Inputs

This standard accepts:

- Tool requests.
- Connector requests.
- CLI, repo, deployment, DNS, CRM, analytics, automation, payment, email, calendar, form, API, and account requests.
- Local workspace edit requests.
- Credential-boundary questions.

## Outputs

This standard produces:

```text
Permission check:
- System:
- Scope:
- Requested action:
- Permission class:
- Risk:
- Required approval:
- Allowed action:
- Blocked action:
- Next action:
```

## Acceptance Test

This standard passes when the requested action has a named permission class, risk score, approval state, allowed action, blocked action, and next action.

## Failure Test

This standard fails when the OS acts before permission is classified, or when a live action occurs under a non-live permission class.

## Escalation

Escalate to Warden for `credential-handling`, `blocked`, or unclear live-system boundaries.

Escalate to the operator for `live-action`, `credential-handling`, risk score 3+, or any client/public/legal/financial commitment.
