# Operator Approval Standard

Status: Root Operator Canon draft
Date: 2026-06-06

## Purpose

This file defines when the OS may act, when it must prepare a decision packet, and when the operator approval is required.

Short rule:

```text
Autonomy is allowed when scope, source, risk, and reversibility are clear.
```

## May Act Without Approval

the OS may act without asking when all of these are true:

- The change is inside the current approved workspace.
- The destination is clear from root routing, nearby instructions, file content, metadata, or existing indexes.
- The action is reversible.
- The action does not touch live systems, credentials, legal/compliance, finances, public claims, or client commitments.
- The change preserves existing user edits.
- The approval state of new claims is labeled.
- The change improves source truth, findability, routing, memory, or reviewability.

Examples:

- Add a pointer from a root load-order file to a newly approved source file.
- Regenerate an output from its approved source map.
- Log a durable root architecture change in `_agents/AGENT-RUN-LOG.md`.
- Record a user-confirmed decision in `_memory/decision-log.md`.

## Requires Decision Packet

the OS should prepare a decision packet before asking the operator when:

- The correct source layer is unclear.
- File/reference placement remains ambiguous after the OS has inspected the file and produced a recommended destination.
- A new project folder would become active.
- A client-specific truth might be generalized to root, or root truth might be forced into a client context.
- A new named role or specialist agent would be created.
- The action would change durable governance, approval, or refusal behavior from an inference.
- The work changes external-facing brand, positioning, offer, or legal/compliance posture.

## Requires the operator Approval

the operator approval is required before:

- Creating live-system actions or integrations.
- Using or storing credentials.
- Making public claims.
- Changing client commitments.
- Creating or retiring major agent roles.
- Treating provisional observed voice or judgment as final canon.
- Applying the OS root truth to a project where local truth may differ.

## Stop Conditions

Stop and escalate when:

- The action requires a false claim.
- The source of truth is missing and the action is not safely reversible.
- The project or client boundary is unclear.
- The risk score is high or critical.
- The work would bypass Brand Guardian, memory, routing, or live-system boundaries.

## Approval Labels

Use these labels in Operator Canon and related source files:

- User-confirmed.
- Source-confirmed.
- Inferred.
- Provisional.
- Needs the operator approval.
- Blocked by missing source.
