# Route Card: Project Scaffold

Status: active runtime card
Date: 2026-06-07

## Trigger

Create, repair, classify, or scaffold a project/venture/workspace.

## Load Next

- `_routing/project-folder-inheritance-template.md` for the venture harness structure and inheritance files.
- `_routing/new-project-intake-standard.md` for new active project/venture intake.
- `_routing/project-stage-spine-template.md` and `_routing/project-stage-contract-template.md` for the stage spine.
- Existing project `CLAUDE.md`, `CONTEXT.md`, `ROUTING.md` when the folder already exists.

## Required Roles

Conductor, Keeper, Librarian, Steward. Add Warden for live-system or credential pointers.

## Venture Harness

On venture creation, the agent installs the **venture harness** into the new venture's folder — the
inherited project structure defined by `_routing/project-folder-inheritance-template.md`:

```text
[VENTURE]/
  CLAUDE.md          # project identity + root inheritance pointers
  CONTEXT.md         # current project state
  ROUTING.md         # project-local routing + stage map
  _governance/       # local governance inheritance
  _memory/           # project-memory.md + decisions.md
  _connectivity/     # local live-system pointers (no secrets)
  references/
  stages/            # 01_intake -> 02_judgment -> 03_output -> 04_handoff
```

Root law is inherited as pointers; the venture's working truth stays local so the venture can operate
even if separated from this root. See `_examples/sample-project/` for a worked instance.

## Stop Conditions

Stop on undecided status, dormant activation, public/client commitment, live-system movement, credential storage, legal/compliance, financial, or stale legacy path as active truth.

## Output

Project status label, destination, the installed venture harness file set, memory destination, governance gate, connectivity gate, and handoff path.
