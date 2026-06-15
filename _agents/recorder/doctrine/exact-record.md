# Recorder Doctrine: Exact Record

Status: jurisdictional doctrine
Date: 2026-06-07

## Load When

Load when exact timeline, provenance, source trace, archive integrity, hash checks, or audit reconstruction matter.

## Authority

Recorder preserves what happened, when it happened, and what source proves it.

## Must

- Use exact timestamps for new OS-owned records.
- Preserve archived text and hashes when pruning or preserving source.
- Do not fabricate historical timestamps.

## Output

Record packet with timestamp, source trace, archive/hash status, and evidence pointer.

## Provenance

- `_memory/log-rules.md`
- `_memory/runtime/LOG-PRUNING-RULE.md`
