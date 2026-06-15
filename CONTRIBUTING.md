# Contributing

Thanks for improving Command Center OS.

## Ground rules

1. **Never commit personal data or secrets.** No real names, client/venture names, credentials, API
   tokens, private repo URLs, or machine-specific paths. On the canonical template repo a maintainer-only
   scrub gate (`.github/workflows/distribution-scrub.yml`) enforces this; it does not run on forks.
2. **Keep the engine deterministic.** Changes to `_routing/*.py` must keep `python _routing/run_gates.py`
   green, including role-registry validation.
3. **Preserve the role contract shape.** Each `_agents/<role>/` keeps its `CONTRACT.md`, `doctrine/`,
   and four-stage spine. If you rename a role, update every reference and re-run the gates.
4. **Root stays portable.** Project-specific truth lives in the project folder, not in root.

## Before you open a PR

```bash
python _routing/run_gates.py
```

CI runs this suite on every push and pull request (`.github/workflows/atx-gates.yml`); PRs that break a
gate will fail. On the canonical repo, the maintainer scrub workflow additionally fails any PR that
reintroduces a forbidden token.

## Adding a project profile or env contract

See `_connectivity/env-restore-runbook.md` and `_connectivity/local-env-manifest.md`. Commit only
contracts and examples — never values.
