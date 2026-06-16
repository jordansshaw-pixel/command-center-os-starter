# Command Center OS — Guide

A plain-language handbook for getting started. If you read one file, read this one.

---

## 1. What this is

Command Center OS is a **folder of instructions that an AI coding agent reads** to work the way you
work. Instead of asking an AI the same setup questions every session, the OS holds your identity,
standards, memory, and guardrails as files — so the agent stays aligned with *you* before it does
anything.

It is not an app you install and click. It is a repository you open with an AI agent
(Claude Code, Codex, or similar). The agent reads the files and follows them.

Think of it as: **an operating manual your AI assistant boots from.**

---

## Features at a glance

- **Tiered runtime boot** — loads compact kernels first (low context cost); deep sources load only when a route needs them.
- **Request routing** — every request is classified to the smallest matching route card before work starts.
- **Agent crew (17 roles)** — functional roles (Conductor, Sentinel, Steward, Keeper, Builder, Warden, and more), each with a contract, doctrine, and a four-stage spine. Fully renameable.
- **Mandatory risk gate** — Sentinel scores risk and fires on all non-trivial work before anything moves.
- **Live-system & credential boundaries** — Warden stops before touching websites, deploys, money, or secrets and asks for approval.
- **Truth & proof governance** — Steward refuses unsupported claims (proof before claims).
- **Operator Canon** — your truths, voice, judgment, load, and approval standards drive the system.
- **Guided onboarding** — interactive `install.py` (no agent required) or the agent-driven route fills your profile.
- **Venture harness** — each venture gets a full, portable project structure installed at creation by the agent.
- **Memory discipline** — relevance checks, exact-record archiving, findability indexing, and log pruning.
- **Deterministic gates** — engine self-tests + role-registry validation, runnable locally and in GitHub CI.
- **Decision packets** — when human judgment is needed you get options, tradeoffs, and a recommended default — not a vague question.
- **Connectivity templates** — env vault map + SOPS/age restore scripts; the repo never stores secrets.
- **Handoff templates & logs** — clean resume/transfer between sessions or owners.
- **Architecture generators** — render an architecture/interface view from a source-of-truth map.
- **Optional commit gate** — a Git pre-commit hook can run the gates before each commit.
- **MIT-licensed GitHub template** — “Use this template,” rename the crew, rebrand, make it yours.

---

## 2. What you need

- A GitHub account.
- An AI coding agent that can read a repo and run commands — e.g. **Claude Code** or **Codex**.
- Python 3.10+ installed (only used to run the built-in self-checks).

That's it. No servers, no database, no paid services to start.

---

## 3. Install (5 minutes)

1. On the GitHub page for this template, click **“Use this template” → “Create a new repository.”**
   Name it whatever you like and make it private if you prefer.
2. Clone your new repository to your computer.
3. Onboard — pick **one**:
   - **No agent needed:** run `python install.py` in the repo folder and answer the questions. It writes
     your profile directly.
   - **With your agent:** open the repo and tell it “Load Runtime Tier 0, then start.” Because your
     operator profile is empty, it routes you straight into the same onboarding interview.

That's the whole install. The onboarding step — next — is where it becomes *yours*.

---

## 4. First boot: the Truth interview

Onboarding (via `python install.py` or the agent's `operator-onboarding` route) is a short interview
that asks you, one group at a time:

1. **Identity** — who you are and what you build.
2. **Ventures / clients** — the lanes you work in. You give the **name** (and a one-line intent). You do
   *not* describe the whole venture here — when you actually create a venture, the agent installs a full
   **venture harness** into its folder (see §7). Root just remembers the lane.
3. **Standards** — your quality bars and non-negotiables.
4. **Boundaries** — what the system must never touch without asking (live systems, money, credentials).
5. **Voice** — how you write and speak, and how you like to be challenged.
6. **Approval posture** — when the system may act on its own vs. ask first.

Your answers are written into `_operator/OPERATOR-TRUTHS.md` and `OPERATOR-VOICE.md`, and the boot
state is refreshed. From then on, every session starts already knowing who you are. You can re-run the
interview or edit those files by hand anytime.

> **Tip:** be specific. “Truth needs a source and an owner” is the kind of standard the system uses to
> keep AI from making confident-but-unsupported claims.

---

## 5. The crew (your agents)

The OS organizes work through a set of named roles — a **Conductor** that routes work, a **Sentinel**
that checks risk before anything moves, a **Steward** that owns truth and proof, a **Keeper** for
memory, a **Builder** for implementation, and more. You don't memorize these; the system invokes them.
Full list in `ROLE-GLOSSARY.md`. If you'd rather they had your own names, the glossary explains how to
rename them.

---

## 6. Daily use

You just describe what you want in plain language. Under the hood the OS **classifies** the request and
picks the smallest matching “route card” before doing work:

- Small, reversible edit → fast lane.
- Touching a website, deploy, credential, or external account → live-system route, which **stops for
  your approval** first.
- A decision worth remembering → it gets written to memory.
- Starting or handing off a project → scaffold / handoff routes.

The guardrails are real: the system is designed to refuse unsupported claims, stop before live-system
actions, and ask before crossing a boundary you set during onboarding.

### Check it's healthy

From the repo folder:

```bash
python _routing/run_gates.py
```

You should see **“the OS gate checks passed.”** These are deterministic self-checks (six of them) that
confirm the engine and its role registry are intact. They run automatically on GitHub too.

---

## 7. Add a venture (the venture harness)

A **venture** is any project, client, or work lane. You don't hand-build its folders — you ask your
agent, e.g.:

> “Scaffold a venture called Acme.”

The agent installs the **venture harness** into a new top-level folder: a complete, self-contained
project structure that inherits root law but keeps its own working truth. It contains:

```text
Acme/
  CLAUDE.md          # the venture's identity + pointers back to root
  CONTEXT.md         # current state
  ROUTING.md         # how work routes inside this venture
  _governance/       # local truth/proof boundaries
  _memory/           # the venture's memory + decision log
  _connectivity/     # local live-system pointers (never secrets)
  references/
  stages/            # 01_intake -> 02_judgment -> 03_output -> 04_handoff
```

Why this matters:

- **Portable.** Each venture carries everything it needs to run. Move the folder out of the repo and it
  still works — root is not a dependency, just an inheritance source.
- **Isolated.** One venture's facts never leak into another. What's true for Acme isn't assumed true
  elsewhere unless you say so.
- **Consistent.** Every venture gets the same intake → judgment → output → handoff spine, so any agent
  can pick up work in any venture the same way.

There's a worked example in `_examples/sample-project/` showing the shape. Run a route on it first to
see the flow before creating a real venture.

---

## 8. Secrets and live systems

This repo never holds secrets. When you connect real services:

- Keep plaintext `.env` files local only (they're already ignored by Git).
- Store encrypted values in a **separate private vault repo** you create — see
  `_connectivity/env-vault-map.md`.
- The OS will stop and ask before any action that touches a live system, credential, or external
  account.

---

## 9. Make it yours

- **Name** — the product is called “Command Center OS” by default; find/replace to rebrand.
- **Crew** — rename the agent roles via `ROLE-GLOSSARY.md`.
- **License** — `LICENSE` is MIT with `Command Center OS contributors` as the holder; change it to your
  name or org.

---

## 10. FAQ

**Do I need to know how to code?**
No, but you need an AI coding agent and basic comfort opening a repo and running one command.

**Will it do things without asking?**
Only low-risk, reversible work inside your repo. Anything touching live systems, money, credentials, or
public claims stops for your approval — and you set those boundaries during onboarding.

**The gate checks failed — what now?**
Re-read the failure message; it names the gate. Most failures mean a file was edited into an
inconsistent state. Ask your agent to “run the gates and fix what they report.”

**Can I change the roles, names, or rules?**
Yes — all of it is plain text. Edit the files. Run `python _routing/run_gates.py` afterward to confirm
nothing broke.

**Where do I start reading?**
This guide, then `DISTRIBUTION-README.md` for the quickstart and `ROLE-GLOSSARY.md` for the crew.
