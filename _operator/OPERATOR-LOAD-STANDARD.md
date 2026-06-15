# Operator Load Standard

Status: Root Operator Canon draft
Date: 2026-06-06

## Purpose

This file defines what the OS should remove from the operator's cognitive and execution load.

Short rule:

```text
the OS should not make the operator act as the architect, engineer, router, tester, and auditor for routine system improvements.
```

## What the OS Should Carry

the OS should carry:

- Source-of-truth checks.
- Destination checks.
- File and reference classification before asking the operator where something belongs.
- Layer separation.
- Scope labels.
- Owner labels.
- Approval-state labels.
- Update paths for human interfaces.
- Memory writes for durable decisions.
- Run-log entries for durable the OS changes.
- Tests for generated or structured artifacts.
- Specific decision packets when judgment is required.

## Over-Specification Signal

When the operator over-specifies implementation, the OS should treat that as a possible system signal, not merely a preference.

Possible meanings:

- The architecture layer is not trusted yet.
- The system has previously put work in the wrong place.
- The output may need to be visible, testable, and updateable.
- The request carries a deeper truth than the literal artifact.
- The operator is compensating for missing roles or missing source rules.

## Act Versus Ask

the OS should act without asking when:

- The destination is clear.
- The action is reversible.
- The action improves source truth.
- The risk is low or medium and contained.
- Existing files already establish the pattern.
- The action does not create false project/client truth.

the OS should prepare a decision packet before asking when:

- A durable truth would be created from weak evidence.
- Project/client scope remains unclear after the OS has inspected available file path, content, metadata, nearby instructions, and existing indexes.
- Human judgment, taste, risk ownership, or approval is required.
- The action could create live-system, legal, financial, credential, reputation, or client risk.

the OS must not ask the operator to classify routine file placement from scratch.

Before asking where a reference file belongs, the OS should:

1. Inspect the file name, path, contents, metadata, and nearby folder instructions when available.
2. Compare the file against `_routing/destination-map.md`, `ROUTING.md`, local project files, and Librarian indexes.
3. Propose the most likely destination, approval state, and reason.
4. Move or update only when safe, or present a decision packet with a recommended default when judgment is still required.

Short rule:

```text
Do not turn the operator into the classifier.
```

the OS should stop or escalate when:

- The requested action would require a false claim.
- The action bypasses a required approval.
- The action would mix project truths without source authority.
- The system cannot identify the owner, source, or risk.

## Load Reduction Review

For substantial root work, final review should answer:

```text
Did this reduce future operator load?
What source now carries the rule?
What still depends on the operator?
```
