# Changelog

All notable changes to Command Center OS are documented here.

## [0.1.0] - 2026-06-26

### Added

- **Log freshness gate** (`--freshness` flag on the pruning gate): warn-only check that logs
  enrolled in the memory registry must have been updated within a configurable window. Inverse
  of size-pruning -- logs cannot silently go stale. Includes registry enrollment for built-in
  log files and a non-blocking pre-commit reminder hook.

- **Session-time enforcement hooks** wired via `.claude/settings.json`:
  - *PreToolUse* -- conservative-allowlist adapter that hard-blocks live-system actions
    (deploy, push, curl, ssh), credential-touching, irreversible commands, and edits to
    durable root-law files; everything else passes or escalates non-blockingly.
  - *Stop* -- finalization reminder printed at the end of every agent turn.
  - *SessionStart* -- context-recovery packet surfaced at session boot.

- **`install.py` ensures `.claude/settings.json` exists**: the installer now calls
  `ensure_hooks(root)` after writing the operator profile. If the hooks file is missing it is
  created (UTF-8, no BOM); an existing file is never overwritten. A single summary line
  confirms enforcement hooks are active. A fresh `python install.py` is now the complete
  setup step with no manual file placement required.