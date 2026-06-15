# Command Center OS

Command Center OS is a folder-based agentic operating system for keeping judgment, memory, routing,
governance, projects, and AI agents aligned before work moves into production.

This is the **Community Edition** — a clean, distributable starter with no operator data and no live
projects. **New here? Start with `GUIDE.md`** (plain-language walkthrough). See `DISTRIBUTION-README.md`
for the quickstart and `ROLE-GLOSSARY.md` for the agent crew.

## Features

- **Tiered runtime boot** — compact kernels first; deep sources load only when a route needs them.
- **Request routing** — every request classified to the smallest matching route card before work.
- **Agent crew (17 functional roles)** — contract + doctrine + four-stage spine each; renameable.
- **Mandatory risk gate (Sentinel)** — fires on all non-trivial work before movement.
- **Live-system & credential boundaries (Warden)** — stops and asks before deploys, money, or secrets.
- **Truth & proof governance (Steward)** — refuses unsupported claims; proof before claims.
- **Operator Canon** — your truths, voice, judgment, load, and approval standards drive behavior.
- **Guided onboarding** — interactive `install.py` (no agent) or the agent-driven route.
- **Venture harness** — full portable project structure installed per venture at creation by the agent.
- **Memory discipline** — relevance, exact record, findability, log pruning.
- **Deterministic gates** — self-tests + role-registry validation, local and in CI.
- **Decision packets** — options + tradeoffs + recommended default when human judgment is needed.
- **Connectivity templates** — env vault map + SOPS/age restore scripts; no secrets in the repo.
- **Handoff templates & logs**, **architecture generators**, optional **commit-time gate**.
- **MIT-licensed GitHub template** — rename, rebrand, make it yours.

Full walkthrough in `GUIDE.md`.

## Start Here

1. Use this template (or clone the repo).
2. Onboard: run `python install.py` (no agent needed), **or** open the repo with Claude Code / Codex,
   load Runtime Tier 0 (below), and the empty operator layer routes you to
   `_routing/runtime/routes/operator-onboarding.md`.
3. Create your first venture by asking the agent to scaffold it — it installs the full venture harness
   (`_routing/runtime/routes/project-scaffold.md`).

For an agent, begin with:

```text
Read CLAUDE.md, AGENTS.md, CONTEXT.md, _memory/SESSION-BOOT-STATE.md,
_routing/runtime/ROUTING-KERNEL.md, _routing/runtime/ROUTE-INDEX.md,
_memory/runtime/MEMORY-KERNEL.md, and _memory/runtime/LOAD-INDEX.md.
Then classify the request through the smallest matching route card before loading project files.
```

Runtime Tier 0 load order:

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

## Root Rules

- `CLAUDE.md` is the canonical root identity.
- `AGENTS.md` is the Codex-facing loader and sync pointer.
- `_operator/` owns the operator's durable truths (populated during onboarding).
- `_agents/` owns the agent crew (functional roles, stage spine, doctrine).
- `_routing/` owns routing, gates, and decision discipline.
- `_memory/` owns recovery, relevance, exact record, and findability.
- `_connectivity/` owns live-system, credential, tool, and repo movement gates.
- `_governance/` owns truth, proof, refusal, and correction authority.
- Project folders carry local truth and should not duplicate root law unless a local override is required.

## Environment & Secrets

This repo never stores secrets. Encrypted environment files live in a separate **private** vault repo
you create (`_connectivity/env-vault-map.md`). Plaintext `.env` files stay ignored and local only.

## Make It Yours

- Rename the crew: `ROLE-GLOSSARY.md` documents each functional role; rename folders + references if
  you want your own theme.
- Set your workspace name: the default product name is "Command Center OS"; find/replace to rebrand.
- Run onboarding to fill `_operator/` and replace the fresh-install boot state.
