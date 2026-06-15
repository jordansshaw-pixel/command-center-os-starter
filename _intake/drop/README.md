# Intake Drop

Status: Operator-facing intake lane
Date: 2026-06-06

## Operator Action

Put unsorted incoming files here:

```text
_intake/drop/
```

## MUST

- the OS MUST treat this as the only operator-facing drop location for routine unsorted files.
- the OS MUST classify files after they are placed here.
- Librarian MUST inspect file evidence before recommending a destination.
- Conductor MUST route only after classification or a valid stop condition.
- Sentinel MUST score risk before movement when the file may affect durable truth, project/client truth, public claims, credentials, live systems, legal/compliance, finances, or operator load.

## MUST NOT

- the OS MUST NOT require the operator to decide whether the file is a reference, artifact, source, output, project, stage, governance, memory, or routing file before drop.
- the OS MUST NOT treat `_intake/drop/` as permanent storage.
- the OS MUST NOT move sensitive files broadly.

## Sensitive Boundary

Do not put secrets, credentials, private keys, payment data, regulated data, or live-system access material here.

If a file appears sensitive, the OS MUST stop and route through Warden and `_connectivity/` before opening, moving, indexing, or copying it broadly.

## Acceptance Test

This lane passes when the operator can put any non-sensitive unsorted file in `_intake/drop/` without choosing a category first.

This lane fails if the operator is asked to pick `references`, `artifacts`, `source`, `output`, project, or stage before the OS has inspected the file.
