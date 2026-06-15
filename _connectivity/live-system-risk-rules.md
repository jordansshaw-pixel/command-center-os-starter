# Live-System Risk Rules

Status: Root live-system risk standard
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This file defines when the OS must stop, review, or request approval before touching live systems.

Short rule:

```text
Live-system access is blocked until explicitly approved.
```

## Owner

Warden owns live-system hard stops.

Sentinel owns risk scoring.

Signal owns stop and escalation signals.

Conductor owns routing after approval or stop.

the operator owns approval for live-system actions.

## Live-System Definition

A live system is any system where action could affect real users, clients, data, money, access, public truth, operational records, deployments, or external state.

Live systems include:

- Websites and public pages.
- DNS and domains.
- Hosting and deployments.
- GitHub or other repositories when pushing, opening PRs, changing settings, or modifying protected branches.
- CRM, lead records, contact lists, pipelines, and client records.
- Automations, workflows, backend functions, and agents.
- Analytics, tags, pixels, consent tools, and tracking.
- Forms, booking links, calendars, email sending, and messaging systems.
- Payment, billing, invoices, subscriptions, and financial systems.
- Credential stores, API keys, tokens, secrets, and account access.

## System Action

the OS MUST classify live-system requests before action.

the OS MUST stop if approval, source, owner, risk, or rollback path is missing.

## MUST

- the OS MUST treat live-system action as risk score 4 until scoped down.
- the OS MUST require Warden review and the operator approval before live-system changes.
- the OS MUST identify the system, scope, owner, requested action, permission class, risk score, approval state, rollback path, and next action.
- the OS MUST keep secrets and credentials out of markdown.
- the OS MUST use a Signal stop, review, or escalation signal when live-system movement is blocked.
- the OS MUST keep project-specific live-system rules local to the project after root inheritance exists.
- the OS MUST treat legal/compliance review blocks as hard stops until the approval condition is met.

## MUST NOT

- the OS MUST NOT change DNS, production domains, deployments, repo state, CRM records, analytics, automations, forms, payment systems, emails, calendars, or public sites without explicit approval.
- the OS MUST NOT assume that a preview URL, app ID, repo path, or local implementation pointer authorizes action.
- the OS MUST NOT expose secrets, tokens, keys, private data, payment data, regulated data, or client records in chat or markdown.
- the OS MUST NOT claim an integration exists until the implementation source and approval state prove it.
- the OS MUST NOT bypass legal/compliance, Brand Guardian, Warden, or the operator approval because a technical path exists.

## Required Live-System Packet

Before any live-system movement, the OS MUST produce:

```text
Live-system packet:
- System:
- Scope:
- Requested action:
- Current source:
- Owner:
- Permission class:
- Risk score:
- Approval required:
- Approval status:
- Credential handling:
- Rollback path:
- Blocked actions:
- Allowed safe actions:
- Next action:
```

## Default Safe Actions

When live-system action is not yet approved, the OS MAY:

- Inspect non-sensitive local source files in the approved workspace.
- Draft a plan, checklist, packet, or proposed change.
- Identify missing approvals.
- Identify required credentials without asking for or exposing them.
- Create non-live local files that document the safe path.
- Prepare a handoff packet.

the OS MUST NOT apply the action to the live system.

## Acceptance Test

This standard passes when live-system movement is stopped or approved with a complete live-system packet and no secrets are exposed.

## Failure Test

This standard fails when a live system changes without explicit approval, or when the OS handles secrets in markdown or chat.

## Escalation

Escalate to the operator when:

- The action would change a live system.
- The action would use or create credentials.
- The action would affect legal/compliance, finances, public claims, client commitments, or irreversible state.
- Risk score remains 3 or 4 after scoping.

Escalate to Brand Guardian when:

- The action could change public truth, proof, claims, refusal, doctrine, brand, or reputation.

Escalate to Warden when:

- Secrets, credentials, access, permissions, live-system state, or do-not-touch zones are involved.

## Known Root Blocks

| Scope | Block | Source | Required Before Movement |
|---|---|---|---|
| Root | Do not store raw credentials or import old connectivity files wholesale. | `CLAUDE.md`, `ROUTING.md`, `_routing/destination-map.md` | Classification, Warden review, and approval for any non-secret import. |
| Project workspaces | Do not store project-specific live-system details in root the OS. | `_operator/OPERATOR-TRUTHS.md`, `_memory/MEMORY-ROUTER.md` | Save project live-system blocks in `[PROJECT]/_connectivity/` and route from there. |
