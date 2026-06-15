# 01 — Git & Version Control

> Load this file when committing, branching, or making versioning decisions.

---

## Branch Rules

- **Never work directly on `main`.** All work happens on a feature branch created from `main`.
- **Branch naming:** `feature/short-description`, `fix/short-description`, `experiment/short-description`. Lowercase, hyphens only.
- **Always start from a clean git state.** Before beginning any new branch: `git status`. If there are uncommitted changes, commit or stash them first.
- **Never force push to `main`.** Force push is acceptable on feature branches only.

---

## Commit Rules

### Commit Frequency

- **Commit after every working change.** Component renders → commit. API returns data → commit. Do not accumulate.
- **Push to remote after every commit.** Run `git push origin <current-branch>` immediately after committing. Do not batch pushes.
- **At the end of each work session,** commit all work and note what's next in the commit message body.

### Conventional Commits — Required Format

All commit messages must follow [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) with **mandatory scope**.

```
<type>(<scope>): <short description>

[optional body]

[optional footer(s)]
```

**Examples:**
```
feat(engine): support 4K rendering
fix(auth): resolve token refresh race condition
refactor(api): extract user service to separate module
docs(readme): add deployment instructions
chore(deps): update supabase client to v2.1
test(payments): add stripe webhook integration tests
perf(search): debounce query input to 300ms
```

### Required Types (use exactly one per commit)

| Type | When to Use | SemVer |
|------|------------|--------|
| `feat` | New feature added | MINOR |
| `fix` | Bug patched | PATCH |
| `refactor` | Code restructured, no behavior change | — |
| `perf` | Performance improvement | — |
| `test` | Tests added or corrected | — |
| `docs` | Documentation only | — |
| `style` | Formatting, whitespace, no logic change | — |
| `chore` | Dependency updates, build config, tooling | — |
| `ci` | CI/CD pipeline changes | — |
| `build` | Build system changes | — |
| `revert` | Reverts a previous commit | — |

Breaking changes: append `!` after type/scope and add `BREAKING CHANGE:` footer.
```
feat(api)!: remove v1 endpoints

BREAKING CHANGE: all /v1/* routes have been removed. Use /v2/*.
```

### Scope Rules

- **Scope is mandatory.** Every commit must include a scope.
- The scope must be a noun identifying the part of the codebase changed: `auth`, `api`, `ui`, `db`, `engine`, `payments`, `search`, `config`, etc.
- Scopes are defined in `AGENTS.md` for each project. If a scope doesn't exist yet, add it to `AGENTS.md` before committing.
- **One scope per commit.** If a commit needs two scopes, it should be two commits.

  _Why: The scope enforces single-responsibility at the commit level. It also signals to the human orchestrator exactly what part of the system changed._

---

## Merge Rules

- **When the feature is done and tested:** `git checkout main && git merge feature/branch-name`
- **Optional:** Open a pull request instead when you want automated code review (Greptile, CodeRabbit, etc.)

---

## Recovery

The 3-attempt reset protocol lives in `04-debugging.md`. Git commands for recovery are there.

---

## → Where to Go Next

Repo initialized and branch created?
→ Load `02-code-quality.md` — you're ready to start writing code

Just committed a completed feature and ready to merge?
→ Run the checklist in `10-checkpoints.md` before merging to `main`

Something broke and you're on attempt 2+?
→ Stop here. Load `04-debugging.md` instead
