# Log Pruning Rule

Status: active runtime rule
Date: 2026-06-07

## Purpose

Keep OS-owned logs useful without making them default context loads.

## Scope

Applies to OS-owned decision, run, handoff, audit, validation, source, asset, intake, progress, design, and inherited project-local logs.

Does not apply to third-party, package-owned, reference, or imported changelogs unless the OS explicitly owns them.

## Trigger

When an active OS-owned log exceeds 300 lines, prune by archive-plus-index.

## Method

1. Move oldest complete entries into dated archive files until the active log is under 200 lines.
2. Never split an entry across active and archive files.
3. Preserve exact archived text.
4. Add or update an active `Archive Index` with date span, entry count, archive path, and SHA-256 hash.
5. Leave unresolved open loops, current blockers, and current next-owner notes active or explicitly pointed to.

## Archive Pattern

- `_memory/log-archive/[log-name]/YYYY-MM.md`
- `_agents/log-archive/AGENT-RUN-LOG/YYYY-MM.md`
- `_handoffs/log-archive/HANDOFF-LOG/YYYY-MM.md`

## Stop Conditions

Stop if hashes are missing, entries are partial, archive destination is unclear, or pruning would hide an unresolved decision or blocker.

## Enforcement

`_routing/atx_log_pruning_gate.py` is the deterministic detector for this rule. It measures enrolled logs in `_memory/runtime/log-registry.json` against per-log thresholds and routes over-threshold logs to Recorder. It detects only; it MUST NOT prune, edit, archive, hash, or split a log.

- Trigger (default 300): `warn`, non-blocking, flag to Recorder.
- Ceiling (default 500): `block`, exit 2.
- The gate self-test runs in `_routing/run_gates.py` (local hook + CI).
- The local `.githooks/pre-commit` scans only logs staged in the commit.
- A passed scan means only that no enrolled log is over its ceiling. It is not a prune and does not authorize one.

Owner: Recorder executes the prune; Keeper confirms active open loops stay; Librarian updates the Archive Index; Conductor routes; Sentinel gates risk.

## Provenance

Extends `_memory/log-rules.md` and preserves Recorder exact-record authority.

Execution evidence:

- `_memory/log-archive/decision-log/2026-06.md`
- `_agents/log-archive/AGENT-RUN-LOG/2026-06.md`
