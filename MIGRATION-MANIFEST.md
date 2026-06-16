# Migration Manifest

How this Community Edition was produced from a private workspace, and what is guaranteed about it.

## Guarantees

- **No operator identity:** no real names; the operator layer is empty scaffolds populated via onboarding.
- **No ventures or clients:** all project/venture folders and names were excluded or replaced with neutral placeholders.
- **No secrets or private infra:** no credentials, tokens, private repo URLs, vault contents, or machine paths.
- **No third-party IP role names:** the agent crew uses functional names (see `ROLE-GLOSSARY.md`).
- **Enforced upstream:** `_routing/distribution_scrub_gate.py` runs on the canonical repo only
  (`.github/workflows/distribution-scrub.yml`) and fails if any forbidden token, IP role name, or local
  machine path reappears. It is deliberately excluded from the end-user gate suite.

## Disposition by area

| Area | Disposition |
|---|---|
| `_routing/*.py`, `run_gates.py`, `ci/` | Kept (engine). Role rosters renamed; owner strings genericized. `distribution_scrub_gate.py` added. |
| `_routing/runtime/`, `_memory/runtime/` | Kept. Role names renamed; brand prose genericized. Onboarding route added + indexed. |
| `_agents/<role>/` | Kept. Folders + references renamed to functional roles; registry validated. |
| `_routing/` standards & templates | Kept; examples scrubbed. |
| `_governance/steward.md`, `README.md`, roadmap | Kept; scrubbed and de-ventured; archive/reference pointers cleaned. |
| `CLAUDE.md`, `CONTEXT.md`, `AGENTS.md`, `README.md`, `ROUTING.md` | Rewritten as generic identity with operator placeholders. |
| `_operator/*` | Behavioral standards kept (scrubbed); identity files (TRUTHS, VOICE) blanked to scaffolds; public-profile removed. |
| `_memory/SESSION-BOOT-STATE.md` | Rewritten to fresh-install state. |
| `_connectivity/*` | Rewritten to templates (no URLs/repos/profiles); restore scripts genericized to `root`/`sample`. |
| `_handoffs/` | Kept `HANDOFF-TEMPLATE.md` + README + empty log; dated handoffs excluded. |
| `_memory` logs, `_agents/AGENT-RUN-LOG.md` | Replaced with empty scaffolds. |
| `_intake`, `_output` indexes | Reset to empty scaffolds; binaries, classified, legacy imports, and artifacts excluded. |
| Project/venture folders, `.git`, archives | Excluded entirely. |
| `.github/`, `.githooks/`, `.vscode/`, start scripts | Genericized (branding, paths, role refs). |

## Added for distribution

- `_routing/runtime/routes/operator-onboarding.md` (+ ROUTE-INDEX entry)
- `_routing/distribution_scrub_gate.py` + `.github/workflows/distribution-scrub.yml` (maintainer-only; not in the end-user suite)
- `LICENSE` (MIT), `DISTRIBUTION-README.md`, `ROLE-GLOSSARY.md`, `CONTRIBUTING.md`, this manifest
- `_examples/sample-project/` (neutral worked example)

## Engine namespace

The `atx` prefix on engine code/CI files (`_routing/atx_*.py`, `.github/workflows/atx-gates.yml`,
`ATX_*` shell vars) is an internal namespace, not a brand or personal data, and is intentionally
retained. See `ROLE-GLOSSARY.md`.

## Verification

`python _routing/run_gates.py` runs six deterministic checks (gate self-tests + role-registry
validation). Maintainers additionally run `python _routing/distribution_scrub_gate.py`, which also runs
in CI on the canonical repo only. All must pass.
