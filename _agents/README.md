# Agents

Status: Root agent folder index
Date: 2026-06-06

## Purpose

This folder contains root role definitions, role status, stage contracts, standards, and audit logs.

Short rule:

```text
No role is usable because its name exists. Role status must be checked before use.
```

## Findability

Use:

- `ROLE-INDEX.md` for the human-readable role map, role folders, and role routing notes.
- `ROLE-STATUS.json` for machine-readable active, queued, provisional, runtime, and invocation status.
- `BUILD-TIME-REVIEW-STANDARD.md` for build-time review routing.
- `AGENT-TEST-STANDARD.md` for agent-pass verification.
- `AGENT-RUN-LOG.md` for audit history.

## Role Status Rule

Before assigning, invoking, displaying, or validating a role or role-like lens, load:

1. `ROLE-INDEX.md`
2. `ROLE-STATUS.json`

Queued roles MUST NOT be invoked, assigned ownership, routed execution, used as review gates, or treated as available before their folder, `CONTRACT.md`, stage contracts, handoff path, and active role-index status exist.

## Active Role Threshold

A role may be marked active only when:

- Folder exists.
- `CONTRACT.md` exists.
- Required stage contracts exist.
- Handoff path exists.
- `ROLE-INDEX.md` marks it active.
- `ROLE-STATUS.json` marks it `active-root-operating-role` or `active-specialist-role` with `invocationStatus` set to `invokable-as-role`.

## Handoff

Role routing questions go to Conductor.

Role-status findability and registry maintenance go to Librarian.

Truth, proof, refusal, and visual-overclaim concerns go to Brand Guardian / Steward.
