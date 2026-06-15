# Intake

Status: Root intake lane draft
Date: 2026-06-06

## Purpose

`_intake/` is the root intake system for unsorted incoming files.

the operator should not have to determine whether a file is root, project, stage, reference, artifact, governance, memory, or output before placing it somewhere.

Short rule:

```text
Drop first. the OS classifies next.
```

## Where To Put Things

Operator-facing default:

```text
_intake/drop/
```

MUST:

- the operator MUST be able to drop a non-sensitive unsorted file in `_intake/drop/` without choosing a category first.
- the OS MUST classify the file after inspection.
- Librarian MUST update `_intake/INTAKE-INDEX.md` when processing intake files.

MUST NOT:

- the OS MUST NOT require the operator to choose `references`, `artifacts`, `source`, `output`, project, stage, governance, memory, or routing before drop.
- the OS MUST NOT present internal classification folders as operator choices.
- the OS MUST NOT treat intake as permanent storage.

## Classification Owner

Librarian owns intake findability and classification.

Conductor owns final routing destination.

Sentinel scores risk when movement could affect root law, project/client truth, public claims, credentials, live systems, legal/compliance, finances, or durable source behavior.

the operator approves or overrides only when the OS cannot safely decide after inspection.

## Intake Packet

When the OS processes a file from `_intake/`, use:

```text
Intake classification:
- File:
- Current location:
- Evidence inspected:
- Likely type: [reference | artifact | source | output | unknown]
- Likely scope: [root | operator | governance | routing | memory | connectivity | agent | project | stage | unknown]
- Recommended destination:
- Owner:
- Approval state:
- Risk:
- Action: [move | index | copy-pointer | hold | decision packet]
- Exact approval needed, if any:
```

## Boundary

Do not store secrets, credentials, private keys, payment data, regulated data, or live-system access material in `_intake/`.

If a file appears sensitive, stop and route through `_connectivity/` and Warden before moving or opening broadly.

## Acceptance Test

Pass:

```text
the operator can put a non-sensitive unsorted file in `_intake/drop/` without deciding what kind of file it is.
```

Fail:

```text
the operator must choose between references, artifacts, source, output, project, stage, or agent destinations before the OS inspects the file.
```
