# VIBE-CODE-RULES.md — Coding Agent Rule Index

> This is the index. Do not load this file and all sub-files at once.
> Load only the files relevant to your current phase of work.
> Each file is self-contained and scoped to one concern.

---

## Entry Point — Read This First

**What are you doing right now?**

- Starting a brand new project → load `00-project-kickoff.md`
- Implementing a feature on an existing project → load `02-code-quality.md`
- Something is broken and you're debugging → load `04-debugging.md`
- Doing a code review or refactor pass → load `10-checkpoints.md`
- Reviewing the tech stack or setting up tooling → load `tech-stack.md`

Each file tells you where to go next based on what you find. Follow the routing at the bottom of each file — do not load files speculatively.

---

## Core Rule Files

| Phase / Concern | Load This File |
|----------------|----------------|
| Starting a new project | `00-project-kickoff.md` |
| Git, branches, commits, versioning | `01-git-and-versioning.md` |
| Code quality, structure, naming | `02-code-quality.md` |
| Security rules | `03-security.md` |
| Debugging a failure | `04-debugging.md` |
| Testing standards | `05-testing.md` |
| API design and response contracts | `06-api-standards.md` |
| UI, UX, and copy | `07-ui-ux.md` |
| Performance | `08-performance.md` |
| Documentation | `09-documentation.md` |
| Checkpoints and refactoring | `10-checkpoints.md` |
| Tech stack defaults | `tech-stack.md` |

## Language Extensions — load alongside `02-code-quality.md`

| Language | Load This File |
|----------|---------------|
| TypeScript | `stack-rules/lang-typescript.md` |
| Python | `stack-rules/python-standards.md` |

## Framework Extensions — load alongside language file

| Framework | Load This File |
|-----------|---------------|
| Next.js (App Router) | `stack-rules/fw-nextjs.md` |
| React Native / Expo | `stack-rules/fw-react-native.md` |

## Process Extensions — load when this type of work is happening

| Process | Load This File |
|---------|---------------|
| Implementing auth from scratch | `stack-rules/proc-auth-setup.md` |
| Deploying to production | `stack-rules/proc-deployment.md` |

## Stack Extensions — load when this tool is in the project

| Tool | Load This File |
|------|---------------|
| Supabase (DB, auth, storage) | `stack-rules/stack-supabase.md` |

---

## Load Order for Common Scenarios

**New project kickoff:**
`00-project-kickoff.md` → `tech-stack.md` → `01-git-and-versioning.md`

**TypeScript + Next.js feature implementation:**
`02-code-quality.md` + `stack-rules/lang-typescript.md` + `stack-rules/fw-nextjs.md` → `06-api-standards.md` (if touching APIs) → `05-testing.md` → `10-checkpoints.md`

**React Native feature:**
`02-code-quality.md` + `stack-rules/lang-typescript.md` + `stack-rules/fw-react-native.md` → `05-testing.md` → `10-checkpoints.md`

**Python + FastAPI backend feature:**
`02-code-quality.md` + `stack-rules/python-standards.md` → `06-api-standards.md` → `05-testing.md` → `10-checkpoints.md`

**Setting up auth:**
`stack-rules/proc-auth-setup.md` → `stack-rules/stack-supabase.md` (if using Supabase) → `03-security.md`

**Deploying for the first time:**
`03-security.md` → `stack-rules/proc-deployment.md`

**Debugging a broken build:**
`04-debugging.md` only. Do not mix with feature implementation files.

**Code review / refactor pass:**
`02-code-quality.md` → `10-checkpoints.md`

---

## Override Hierarchy

1. Project-specific `AGENTS.md` overrides everything in this folder
2. Files in this folder are global defaults
3. If a rule is not in `AGENTS.md`, fall back to this folder

---

> These rules are a baseline. If a project deviates from any of them, document the deviation in `AGENTS.md` with a reason.
