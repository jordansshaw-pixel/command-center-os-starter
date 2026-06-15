# Git Hooks

Status: Local repo-managed hook lane
Edition: Community / distributable starter

## Purpose

This folder contains Git hook shims for the OS deterministic infrastructure.

`core.hooksPath` is per-clone, so the hook is opt-in. Activate it once per clone:

```text
git config core.hooksPath .githooks
```

## Installed Hooks

| Hook | Behavior |
|---|---|
| `pre-commit` | If staged files include OS files, run `_routing/atx_hook_runner.py` with `--event source-change`. On pass, allow the commit silently. On block, print the runner status, reason, and next action to stderr, then exit non-zero. If no OS files are staged, exit without action. |

## Emergency Bypass

Use Git's native bypass only for genuine emergencies:

```sh
git commit --no-verify
```

After bypassing, make a normal commit to confirm the hook passes again.

Do not add a separate bypass alongside Git's native bypass.

## Boundary

Hooks validate and route only.

They MUST NOT:

- Perform agent judgment.
- Mutate OS files.
- Install external automation.
- Touch live systems.
- Replace Conductor synthesis.

Source standard:

- `_routing/multi-agent-engagement-standard.md`
