# Connectivity Lane

Status: Root connectivity contract
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This folder owns the OS root connectivity, tool permission, credential-boundary, live-system risk, and implementation-pointer rules.

Short rule:

```text
No live system moves until source, owner, permission, risk, and approval are explicit.
```

## Owner

Warden owns hard stops for live systems, credentials, secrets, access, and do-not-touch zones.

Conductor owns routing into and out of `_connectivity/`.

Sentinel owns risk scoring.

Signal owns stop, review, and handoff signals.

Brand Guardian / Steward owns truth, proof, refusal, public-claim, and governance review.

the operator owns final approval for live-system actions, credentials, client commitments, legal/compliance, finance, public claims, and high-risk movement.

## Operator-Facing Action

the operator may ask for connectivity, tool, credential, integration, deployment, DNS, repo, CRM, analytics, automation, payment, form, email, or live-system work in ordinary language.

the operator does not need to classify the tool, permission, risk, or destination first.

## System Action

the OS MUST classify the request against this folder before any live-system action.

the OS MUST use:

- `connectivity-registry.md` for known systems and implementation pointers.
- `tool-permissions.md` for permission classes and allowed actions.
- `live-system-risk-rules.md` for stop rules, approval gates, and escalation.

## MUST

- the OS MUST treat live-system movement as blocked until permission, owner, risk, and approval are explicit.
- the OS MUST route credential, secret, private key, token, payment, regulated-data, and access-risk questions through Warden.
- the OS MUST score risk with `_agents/sentinel/RISK-STANDARD.md` before live-system movement.
- the OS MUST package review, stop, or approval state with `_agents/signal/SIGNAL-STANDARD.md`.
- the OS MUST record reusable connectivity decisions through `_memory/MEMORY-ROUTER.md`.
- the OS MUST keep project-specific connectivity pointers separate from root rules unless the pointer affects root routing or inheritance.

## MUST NOT

- the OS MUST NOT store raw secrets, credentials, private keys, tokens, recovery codes, payment data, or regulated data in the OS markdown.
- the OS MUST NOT change DNS, deployments, repos, CRM records, analytics, automations, payments, forms, email sending, calendars, or public sites without explicit approval.
- the OS MUST NOT treat legacy `C:\ExampleLegacy`, `CLIENTS/...`, `ExampleOps/...`, or `C:\Dev` paths as active connectivity truth unless current the OS files or the operator mark them active.
- the OS MUST NOT turn a local implementation pointer into a live-system action.
- the OS MUST NOT ask the operator to classify routine connectivity risk before the OS inspects available source context.

## Inputs

This lane accepts:

- Tool and connector references.
- Permission questions.
- Live-system action requests.
- Credential-boundary questions.
- External implementation pointers.
- Project-specific connectivity summaries.
- Stop, approval, or handoff packets involving live systems.

## Outputs

This lane produces:

- Connectivity registry entries.
- Permission class decisions.
- Live-system risk decisions.
- Credential-boundary rules.
- Approval requirements.
- Stop signals.
- Safe path recommendations.
- Project-local connectivity pointer requirements.

## Acceptance Test

This lane passes when:

- A connectivity request has a named system, scope, owner, permission class, risk score, approval state, and next action before movement.
- Sensitive material is blocked from markdown.
- Live-system actions require the operator approval.
- Project-local connectivity inherits root rules instead of duplicating them.

## Failure Test

This lane fails when:

- A live system changes without explicit approval.
- A secret or token is stored in markdown.
- A legacy or external path is treated as active truth without current source authority.
- A project-specific integration promise becomes root truth.
- the OS asks the operator to classify routine connectivity before inspecting available sources.

## Current Source Files

- `_connectivity/connectivity-registry.md`
- `_connectivity/tool-permissions.md`
- `_connectivity/live-system-risk-rules.md`
- `_connectivity/local-env-manifest.md`
- `_connectivity/env-vault-map.md`
- `_connectivity/env-restore-runbook.md`

## Escalation

Escalate to Warden when live systems, secrets, credentials, access, permissions, or do-not-touch zones appear.

Escalate to the operator when action would touch live systems, credentials, public claims, legal/compliance, financial commitments, client commitments, or risk score 3+.

Escalate to Brand Guardian when connectivity changes could affect public truth, proof, refusal, brand, doctrine, or governance.
