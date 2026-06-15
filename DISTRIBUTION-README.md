# Command Center OS — Community Edition

A folder-based agentic operating system you run with a coding agent (Claude Code, Codex, or similar).
It keeps your judgment, memory, routing, governance, projects, and AI agents aligned **before** work
moves into production.

This is a clean, distributable starter: **no operator data, no live projects, no secrets.** You make
it yours during a guided first-run onboarding.

## What you get

- **A crew of functional agent roles** (`_agents/`) with contracts, doctrine, and a four-stage spine.
  See `ROLE-GLOSSARY.md`.
- **Runtime routing** (`_routing/runtime/`) — compact kernels + route cards that classify work before
  loading heavy context.
- **Memory discipline** (`_memory/`) — relevance, exact record, findability, log pruning.
- **Governance** (`_governance/`) — truth, proof, refusal, correction authority.
- **Connectivity gates** (`_connectivity/`) — live-system and credential boundaries; secrets stay in a
  separate private vault you create.
- **Deterministic gates** (`_routing/*.py`, `run_gates.py`) — gate self-tests and role-registry
  validation, enforced in CI (`.github/workflows/atx-gates.yml`).

## Quickstart

1. **Use this template** on GitHub (or clone the repo).
2. Open the repo with your coding agent and load **Runtime Tier 0**:
   `CLAUDE.md`, `CONTEXT.md`, `_memory/SESSION-BOOT-STATE.md`,
   `_routing/runtime/ROUTING-KERNEL.md`, `_routing/runtime/ROUTE-INDEX.md`,
   `_memory/runtime/MEMORY-KERNEL.md`, `_memory/runtime/LOAD-INDEX.md`.
3. On a fresh install the system routes you to **operator onboarding**
   (`_routing/runtime/routes/operator-onboarding.md`). Answer the interview; it fills `_operator/` and
   replaces the fresh-install boot state.
4. Prove one route end-to-end on the sample project in `_examples/`.
5. Add your own project folders at the repo root, keeping each project's operational truth local.

## Verify it works

```bash
python _routing/run_gates.py
```

All six checks should pass. (A separate maintainer-only scrub gate,
`_routing/distribution_scrub_gate.py`, guards the upstream template against reintroduced operator data;
it is intentionally not part of this suite, so it never false-positives on your own content.)

Optionally enable the commit-time gate (per clone):

```bash
git config core.hooksPath .githooks
```

## Make it yours

- **Rename the crew** to your own theme — see `ROLE-GLOSSARY.md`.
- **Set the product name** — the default is "Command Center OS"; find/replace to rebrand.
- **Set the license holder** — `LICENSE` is MIT with `Command Center OS contributors` as the holder;
  change it to your name or org.
- **Connect systems** only after reading `_connectivity/` and creating a private env vault
  (`_connectivity/env-vault-map.md`).

## How this was built

This edition was produced from a private workspace by an automated migration that excluded all
ventures and logs, renamed IP role personas to functional names, scrubbed operator data, blanked the
operator layer behind onboarding, and added the scrub gate. See `MIGRATION-MANIFEST.md`.
