# Command Center OS

Command Center OS is a folder-based agentic operating system for keeping judgment, memory, routing,
governance, projects, and AI agents aligned before work moves into production.

This is the **Community Edition** — a clean, distributable starter with no operator data and no live
projects. **New here? Start with `GUIDE.md`** (plain-language walkthrough). See `DISTRIBUTION-README.md`
for the quickstart and `ROLE-GLOSSARY.md` for the agent crew.

## Start Here

1. Use this template (or clone the repo).
2. Open the repo with Claude Code, Codex, or another coding agent and load Runtime Tier 0 (below).
3. On a fresh install the system routes you to **operator onboarding**
   (`_routing/runtime/routes/operator-onboarding.md`) to capture who you are before substantial work.

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
