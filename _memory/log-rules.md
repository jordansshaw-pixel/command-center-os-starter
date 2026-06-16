# Log Rules


Status: Root memory standard
Date: 2026-06-06

## Purpose

This file defines the shared rule for OS-owned logs.

the OS logs exist to preserve what happened, when it happened, what source moved, and what owner should pick it up next.

Short rule:

```text
Every new OS-owned log entry needs a date, time, and timezone offset.
```

## Scope

This rule applies to OS-owned logs, including:

- Decision logs.
- Agent run logs.
- Handoff logs and handoff packets.
- Audit logs.
- Validation logs.
- Source, asset, intake, progress, and design logs.
- Project-local logs when the project inherits the OS root rules.

Third-party, reference, imported, or package-owned changelogs and troubleshooting logs should not be rewritten as the OS logs unless the OS explicitly owns that file.

## Timestamp Rule

New OS-owned log entries MUST include a timestamp next to the date.

Use this format:

```text
YYYY-MM-DD HH:mm:ss +/-HH:MM
```

Preferred heading format:

```text
### YYYY-MM-DD HH:mm:ss +/-HH:MM - [Short entry name]
```

If a log uses a table, form, or packet instead of headings, it MUST include a `Timestamp` field or column using the same format.

## Legacy Entries

Historical date-only entries before this rule remain valid legacy records.

the OS MUST NOT fabricate timestamps for historical entries when the exact time is unknown.

If a historical exact timestamp is later recovered from a reliable source, the OS MAY update that entry and cite the source of recovery.

## Pruning Rule

OS-owned logs MUST stay findable without becoming default context loads.

When an active OS-owned log exceeds 300 lines, the OS SHOULD prune by archive-plus-index:

1. Move oldest complete entries into dated archive files until the active log is under 200 lines.
2. Preserve exact archived text and compute a SHA-256 hash for each archive file.
3. Add or update an `Archive Index` in the active log with date span, entry count, archive path, and hash.
4. Leave unresolved open loops, blockers, current decisions, and next-owner notes active or explicitly pointed to.

Do not split an individual entry across active and archive files.

Do not prune third-party, package-owned, reference, or imported changelogs unless the OS explicitly owns them.

Runtime pruning source:

- `_memory/runtime/LOG-PRUNING-RULE.md`

## Ownership

- Recorder owns exact record and provenance.
- Librarian owns findability and indexing.
- Keeper owns relevance and continuity.
- Conductor owns routing and handoff compliance.
- Steward may stop or correct log behavior when a log creates a false truth surface.

## Failure Condition

A new OS-owned log entry fails the log standard if it records durable work with only a date and no time or timezone offset.
