# Env Vault Map

Status: private-vault routing map, no values (TEMPLATE)
Edition: Community / distributable starter

## Purpose

This file maps the OS env contracts and credential ledgers to a private encrypted vault.

The env vault is a separate **private** GitHub repo intended to hold encrypted env profiles and
encrypted credential ledgers only. It is never this public repo.

Target repo (set your own):

```text
https://github.com/your-org/env-vault
```

## Architecture

```text
command-center repo (this repo)
  tracks env contracts, examples, and restore rules

env-vault private repo
  tracks encrypted env profiles and encrypted credential ledgers only

local machine
  decrypts selected profile into ignored .env files
```

## Required Vault Shape

```text
env-vault/
  README.md
  .gitignore
  .sops.yaml
  root/
    desktop.env.enc
    laptop.env.enc
  projects/
    sample/
      desktop.env.enc
      laptop.env.enc
      credentials.template.yaml
  manifests/
    variable-index.md
```

## Storage Rules

- Plaintext `.env` files MUST NOT be committed to either repo.
- Encrypted env files MUST use `.env.enc`.
- Encrypted human login credential ledgers MUST use `.credentials.enc.yaml`.
- Credential ledger templates MAY be committed only when they contain no real usernames, passwords,
  recovery codes, client data, or tokens.
- A plaintext decrypted file may exist only on the local machine and only at its target ignored path.
- A plaintext credential intake file may exist only under an ignored `.local/` path and must be
  encrypted into the vault before backup or handoff.
- GitHub Actions or hosting-provider secrets remain in their native secret stores; the vault may
  document names but should not replace platform secrets.

## Restore Destinations

Map each encrypted vault file to its local destination. The example row shows the shape:

| Vault encrypted file | Local destination | Owning project | Notes |
|---|---|---|---|
| `projects/sample/{machine}.env.enc` | `_examples/sample-project/.env.local` | sample | Machine-specific values for the sample project. |
| `root/{machine}.env.enc` | Destination named inside the encrypted profile | Root | Use only for root-level tools that need local values. |

## Restore Command Notes

SOPS `3.7.x` does not reliably infer dotenv format from `.env.enc`.

Use explicit dotenv flags for dotenv profiles:

```text
sops --decrypt --input-type dotenv --output-type dotenv path/to/file.env.enc
```

Profiles encrypted in binary mode may require normal SOPS decrypt output:

```text
sops --decrypt path/to/file.env.enc
```

## Recommended Encryption Tool

Preferred:

```text
SOPS + age
```

Reason:

- Encrypted files can be versioned in GitHub.
- Each computer can have its own decryption key.
- Values remain outside the main repo.
- Per-machine profiles support different local values.

## Bootstrap Sequence

1. Create a private repo `your-org/env-vault`.
2. Add `.gitignore` that blocks plaintext env files and allows encrypted env files.
3. Add `.sops.yaml` after age recipients are known.
4. Add encrypted profile files only.
5. Restore profiles locally into ignored `.env` destinations.
6. Verify `git status` in the main repo does not show plaintext env files.

## Approval Boundary

Creating the vault repo is a GitHub live-system action.

Adding encrypted placeholder structure is allowed after operator approval.

Adding real encrypted values requires a separate secret-handling pass and must not print values in
chat or markdown.
