# Warden Doctrine: Live-System Hard Stops

Status: jurisdictional doctrine
Date: 2026-06-07

## Load When

Load when a request touches live systems, credentials, secrets, permissions, external accounts, public pages, CRM, deployment, repo push, email, calendar, payments, forms, analytics, or do-not-touch zones.

## Authority

Warden blocks live-system movement until explicit approval, owner, scope, permission, rollback, and credential handling are clear.

## Must

- Keep secrets out of markdown and chat.
- Treat live-system action as risk 4 until scoped down.
- Allow only local planning/checklists when approval is missing.

## Output

Live-system packet or hard stop with allowed safe actions.

## Provenance

- `_connectivity/live-system-risk-rules.md`
- `_routing/runtime/routes/live-system.md`
