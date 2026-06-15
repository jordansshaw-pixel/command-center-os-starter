# tech-stack.md — Canonical Stack Defaults

> This file defines the default technology choices across all projects.
> Individual projects may override these in their `AGENTS.md` with a documented reason.
> Keeping a stable default stack means: consistent patterns across projects, no re-learning
> integration details, and a human orchestrator who can read any project without context-switching.

---

## Backend

| Layer | Default Choice | Notes |
|-------|---------------|-------|
| Language + Framework | FastAPI (Python) | Type-safe, fast, first-class async support |
| Runtime | Python 3.11+ | Use `pyproject.toml` for dependency management |
| Package manager | uv | Faster than pip, lockfile-based |

---

## Frontend

| Layer | Default Choice | Notes |
|-------|---------------|-------|
| Framework | React + Vite | Fast build, ESM-native |
| Styling | Tailwind CSS | Utility-first, no CSS file sprawl |
| Component library | shadcn/ui | Copy-paste, you own the code |
| Type checking | TypeScript (strict mode) | No `any`, no implicit `any` |
| Icons | lucide-react | Clean, MIT licensed, tree-shakeable |
| Charts | Recharts | Composable, works natively with React |

---

## Infrastructure

| Layer | Default Choice | Notes |
|-------|---------------|-------|
| Database | Supabase (PostgreSQL) | RLS-first, auth built in, real-time capable |
| Authentication | Clerk | Drop-in, handles sessions, webhooks for user sync |
| Payments | Stripe | Standard, best-documented, webhook-reliable |
| File storage | Supabase Storage | Co-located with the DB, RLS-compatible |
| Deployment (frontend) | Vercel | Zero-config, preview branches, edge network |
| Deployment (backend) | Railway or Fly.io | Docker-based, straightforward env management |

---

## Tooling

| Tool | Purpose |
|------|---------|
| `pyright` | Python type checking (strict mode) |
| `black` | Python formatting (run before commit) |
| `isort` | Python import sorting (run before commit) |
| `eslint` | JS/TS linting |
| `prettier` | JS/TS/JSON formatting |
| `commitlint` | Enforces Conventional Commits format |

---

## Async Job Queue (when needed)

| Layer | Default Choice |
|-------|---------------|
| Queue | Supabase + pg_cron (simple) or Redis + Celery (complex) |
| Pattern | POST → 201 + job_id → GET /jobs/{id}/status (see `06-api-standards.md`) |

---

## Deviations

If a project uses a different choice than the defaults above, it must be documented in that project's `AGENTS.md`:

```markdown
## Stack Deviations from Defaults
- Auth: Using Supabase Auth instead of Clerk (reason: client already has Supabase org, no budget for Clerk)
- Backend: Using Node.js + Hono instead of FastAPI (reason: client team is JS-only)
```

---

## → Where to Go Next

Stack confirmed and documented in `AGENTS.md`?
→ Return to `00-project-kickoff.md` to complete the kickoff checklist

Using Python backend?
→ Load `python-standards.md` — pyright, black, and isort setup belongs in your tooling before the first commit

Stack deviation from defaults?
→ Document it in `AGENTS.md` under `## Stack Deviations` before writing any code
