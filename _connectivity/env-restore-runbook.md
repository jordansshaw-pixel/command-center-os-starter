# Env Restore Runbook

Status: setup runbook, no values (TEMPLATE)
Edition: Community / distributable starter

## Purpose

Restore machine-specific env values from your private encrypted env vault into local ignored `.env`
files.

This runbook documents the intended process only. It does not contain secrets.

## Preflight

Before restoring:

1. Confirm the main repo is clean.
2. Confirm the env vault repo is private.
3. Confirm the needed encrypted profile exists.
4. Confirm decryption tooling is installed.
5. Confirm the local destination is ignored by Git.

## Install Tooling

Preferred tooling:

```text
age
sops
```

The local machine must have its own age key. Do not commit private age keys.

## Restore Pattern

From the env vault repo:

```powershell
sops -d projects/sample/desktop.env.enc > "..\command-center-os\_examples\sample-project\.env.local"
```

Use the correct machine profile:

```text
desktop
laptop
```

## Restore Helper

Single profile:

```powershell
.\_connectivity\scripts\restore-env-profile.ps1 -Machine desktop -Profile sample -Plan
.\_connectivity\scripts\restore-env-profile.ps1 -Machine desktop -Profile sample -Force
```

All profiles for a machine:

```powershell
.\_connectivity\scripts\restore-env-machine.ps1 -Machine desktop -Plan
.\_connectivity\scripts\restore-env-machine.ps1 -Machine laptop -Profiles root,sample -Plan
```

Supported profiles (extend `restore-env-profile.ps1` as you add projects):

```text
root
sample
```

Helper behavior:

- `-Plan` reports vault and destination without restoring.
- Existing destination files are not overwritten unless `-Force` is passed.
- The destination must be ignored by Git before restore proceeds.
- Values are decrypted through SOPS directly into a temp file, then moved into place.
- Secret values are not printed.
- The bulk helper skips missing encrypted profiles by default and reports them as `MISSING`.

## Adding a Project Profile

1. Add the encrypted profile to your vault under `projects/<name>/{machine}.env.enc`.
2. Add a matching entry to the `$profiles` hashtable in `restore-env-profile.ps1`.
3. Add the variable contract to `_connectivity/local-env-manifest.md` and `env-vault-map.md`.

## Verification

After restore, from the main repo:

```powershell
git status --short
```

Expected: no plaintext `.env` files appear. Then confirm the destination file exists locally:

```powershell
Test-Path "_examples\sample-project\.env.local"
```

## Rotation

When a token rotates:

1. Update the local plaintext env file.
2. Re-encrypt into the matching vault profile.
3. Commit only the `.env.enc` change to the private vault repo.
4. Restore on the other computer.
5. Confirm the main repo remains clean.

## Failure States

Stop if:

- A plaintext `.env` file appears in Git status.
- A secret value is printed in terminal output that may be copied into chat or markdown.
- The vault repo is public.
- A decrypted profile is restored to the wrong project.
- A machine profile overwrites another machine's required values.
