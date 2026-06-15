# Local Env Manifest

Status: EMPTY SCAFFOLD — add your own env contracts (no values)
Edition: Community / distributable starter

## Purpose

This file records which local environment variables the OS knows about, where they are used, and where
local machines should restore them.

It MUST NOT contain raw secret values.

Short rule:

```text
Git tracks the contract. The env vault stores encrypted values. Local machines hold decrypted runtime files.
```

## Boundary

Tracked in this repo:

- Variable names.
- Purpose.
- Owning project.
- Local output path.
- Required/optional state.
- Safe template path.
- Vault profile pointer.

Not tracked in this repo:

- Raw `.env` files.
- API tokens, passwords, recovery codes, private keys.
- Any secret-bearing export.

## Known Env Contracts

Add one row per variable. The single example row below shows the shape — replace it with your own.

| Scope | Variable | Purpose | Required | Local output | Safe template | Vault profile |
|---|---|---|---|---|---|---|
| _example project_ | `EXAMPLE_API_TOKEN` | _Server-side token for the example integration_ | Required for live integration | `_examples/sample-project/.env.local` | `_examples/sample-project/.env.example` | `projects/sample/{machine}.env.enc` |

## Machine Profiles

Use a machine slug in vault file names:

- `desktop`
- `laptop`
- another explicit slug you approve

Do not assume env values are the same on every machine.

## Update Rule

When a project adds or changes an env variable:

1. Update the project `.env.example`.
2. Update this manifest.
3. Update `_connectivity/env-vault-map.md`.
4. Update the encrypted vault file in your private env-vault repo.
5. Restore locally on each machine that needs the value.

## Failure State

This manifest fails if:

- It contains raw secret values.
- It points to an untracked real `.env` file as source truth.
- It omits a required project env used by committed code or runbooks.
- It treats one machine's local value as universal truth.
