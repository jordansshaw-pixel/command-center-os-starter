# Connectivity Registry

Status: Root connectivity registry
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This registry names known systems, implementation pointers, and ownership boundaries so the OS does not confuse a reference with approved live-system access.

Short rule:

```text
Registry entry does not equal permission to act.
```

## Owner

Conductor owns registry routing.

Librarian owns findability.

Warden owns sensitive-system and access boundaries.

## Operator-Facing Action

the operator may mention a system, tool, repo, domain, account, local implementation path, or integration request.

the OS classifies and registers the pointer when useful.

## System Action

the OS MUST classify each known connection by scope, status, permission class, credential state, and next action before movement.

## Registry Fields

Every registry entry MUST include:

- Scope.
- System.
- Type.
- Current status.
- Owner.
- Permission class.
- Credential rule.
- Source.
- Allowed action.
- Blocked action.
- Next action.

## Permission Classes

Use permission classes from `_connectivity/tool-permissions.md`:

- `reference-only`
- `read-only`
- `draft-only`
- `local-edit`
- `staged-change`
- `live-action`
- `credential-handling`
- `blocked`

## Known Root Systems

These rows describe the OS infrastructure that ships with this edition. Add your own systems below as
you connect them. The OS itself never carries secrets.

| Scope | System | Type | Current Status | Owner | Permission Class | Credential Rule | Source | Allowed Action | Blocked Action | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|
| Root | `.githooks/pre-commit` via `core.hooksPath=.githooks` | Local Git hook gate | Optional; activate per clone because `core.hooksPath` is per-clone | Warden / Conductor | staged-change | No secrets or credentials in hook output | `.githooks/README.md` | Run local staged-change validation and block commits when `_routing/atx_hook_runner.py` returns `block` | Do not add a bypass or assume fresh clones are gated before activation | Activate the hook once per clone if you want commit-time gating |
| Root | GitHub Actions gates workflow at `.github/workflows/atx-gates.yml` | Remote CI validation | Read-only workflow runs the gate suite on push and pull request | Warden / Conductor | read-only | No secrets, write credentials, or deploy keys | `_routing/ci/run-gates.sh`; `_routing/atx_multi_agent_gate.py` | Run deterministic gate checks and role-registry validation in CI | Do not add secrets, write permissions, or deploy steps in this workflow | Observe CI after push |
| Root | `_routing/atx_live_system_gate.py` | Local live-system packet completeness gate | Active read-only validator for JSON live-system packets; gate pass is not approval | Warden / Conductor | read-only | No secrets in packet output; validate references only | `_connectivity/live-system-risk-rules.md`; `_routing/runtime/routes/live-system.md` | Validate required packet fields and internal consistency before Warden and operator review | Do not perform live-system action, handle credentials, or treat gate pass as permission | Use before any live-system movement |
| Your infra | _e.g._ `your-org/env-vault` | Private encrypted env vault repo | _Set when you create it_ | Warden / Conductor | credential-handling | Encrypted env files only; no plaintext `.env` or raw secret values | `_connectivity/env-vault-map.md` | Store encrypted `.env.enc` profiles after a separate secret-handling pass | Commit plaintext env files or print values | Create the vault repo and add SOPS/age recipients before storing anything |

## Project Systems

Project-specific systems, implementation pointers, tool facts, analytics IDs, backend app identifiers, CRM/email details, DNS state, deployment state, and live-system blocks belong in the project-local connectivity layer:

```text
[PROJECT]/_connectivity/
```

Root MAY record that a project has a local connectivity layer or that a project is active. Root MUST NOT store the project's operational connectivity inventory.

## MUST

- the OS MUST mark every live-system pointer as `reference-only`, `blocked`, or another explicit permission class before action.
- the OS MUST use current project-local context before treating a project system as active.
- the OS MUST preserve credential boundaries in every registry entry.
- the OS MUST store project-specific connectivity facts in the project-local connectivity registry.

## MUST NOT

- the OS MUST NOT store raw secrets, tokens, passwords, recovery codes, or private keys.
- the OS MUST NOT infer permission to act from a known URL, app ID, repo path, or local path.
- the OS MUST NOT import old connectivity files wholesale without classification and approval.
- the OS MUST NOT store project operational connectivity details in the root registry.
- the OS MUST NOT mix project systems across projects or root the OS.

## Acceptance Test

This registry passes when each listed system has scope, status, permission class, credential rule, blocked action, and next action.

## Failure Test

This registry fails when a system is listed without an approval boundary, or when a pointer implies live access.

## Escalation

Escalate to Warden and the operator before changing any system with permission class `live-action`, `credential-handling`, or `blocked`.
