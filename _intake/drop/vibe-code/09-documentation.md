# 09 — Documentation

> Load this file when setting up a project or making architectural decisions.

---

## Project-Level Docs (Required)

Every project must have:

- **`README.md`** — what the project does, how to set it up, how to run it, how to deploy it
- **`AGENTS.md`** — project-specific rules, stack details, directory structure, scope definitions for commits
- **`.env.example`** — all required variable names, no values

---

## Decision Documentation

- **Document non-obvious decisions.** If you chose one approach over another, write down why. A one-liner is enough.
  - Example: `// Using server-side auth token validation instead of client-side because JWTs can be tampered with before expiry`
- **Update docs when decisions change.** If an architectural decision is reversed, update the relevant doc immediately — not later.

  _Why: Without context, the next person (or agent) to touch the code might reverse a deliberate decision, reintroducing a problem you already solved._

---

## API Documentation

- **Store a local copy of third-party API docs** your project depends on in `/docs/api/`.
- **Reference local docs in `AGENTS.md`** so the agent knows where to find them.

  _Why: Agents reference local docs reliably. Without them, agents hallucinate endpoints and parameter names._

---

## Keeping Docs Current

- **Update docs as part of the feature commit, not afterward.**
- If a code change makes an existing doc wrong, fix the doc in the same commit.
- Outdated docs are worse than no docs — they actively mislead.

---

## → Where to Go Next

Docs updated as part of a feature?
→ Commit the doc update in the same commit as the code change, not separately

Setting up a new project and docs structure isn't in place yet?
→ Return to `00-project-kickoff.md` — docs setup is part of the kickoff checklist

Everything documented and up to date?
→ Load `10-checkpoints.md` — you're ready for the done checklist
