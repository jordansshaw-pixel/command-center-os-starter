# New Project Intake Standard


Status: Root routing standard draft
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`
- `_routing/project-folder-inheritance-template.md`
- `_routing/project-handoff-architecture-standard.md`

## Purpose

This standard defines how the OS receives a new project request, asks the first-step setup questions, creates the project folder, and deploys the OS project-local connectivity without making the operator design the folder architecture.

Short rule:

```text
Ask the project intake questions first; create the project scaffold only after status, scope, source, memory, and live-system boundaries are explicit.
```

## Owner

Conductor owns project routing, sequence, status, and scaffold authorization.

Liaison owns human-facing intake clarity.

Librarian owns findability, folder naming, source pointers, and index placement.

Keeper owns memory judgment and project-local memory destination.

Steward owns truth, proof, refusal, correction, and public/client-facing claim boundaries.

Warden owns live-system, credential, secret, regulated-data, legal/compliance, and external-system stops.

Sentinel owns risk scoring.

Signal owns the setup signal and handoff state.

Builder owns the local scaffold wizard after Conductor routes and the required review permits build movement.

the operator owns final approval for project activation, business judgment, client/public commitments, live-system movement, legal/compliance, finance, and risk score 3+ movement.

## Operator-Facing Action

the operator may ask for a new project in ordinary language.

the operator may run:

```text
python _routing/new_project_intake.py
```

the OS MUST ask the first-step intake questions before creating a project folder.

the OS MUST NOT ask the operator to choose internal folders, stage taxonomy, memory files, governance files, or connectivity files before the OS proposes the standard project scaffold.

## System Action

the OS MUST use this standard when creating a new root-level project workspace inside the OS.

the OS MUST gather the intake answers first.

the OS MUST create the project folder only when the project status is approved as `active project` or the operator explicitly approves a different status-specific scaffold.

the OS MUST deploy the project-local the OS connectivity pointer at:

```text
[PROJECT]/_connectivity/README.md
```

the OS MUST NOT store credentials, tokens, private keys, payment data, recovery codes, regulated data, legal/compliance material, or private client records in the project scaffold.

## First-Step Intake Questions

The setup MUST ask:

1. Project display name.
2. Root folder name.
3. Project status label.
4. Purpose.
5. Active scope.
6. Out-of-scope boundary.
7. Starting source material or references.
8. Known live systems, external tools, repos, domains, forms, automations, analytics, payment systems, or accounts.
9. Public/client-facing commitments, claims, compliance, legal, or financial sensitivity.
10. First next work item.

The setup MAY ask follow-up questions only when an answer triggers a stop condition.

## Status Labels

The setup MUST use the status labels from `_routing/project-folder-inheritance-template.md`:

- active project
- active resource workspace
- method engine
- dormant opportunity
- provisional workspace
- historical reference
- placeholder
- undecided

Default status for a requested new project is:

```text
active project
```

If status is not `active project`, the OS MUST produce an intake packet and stop before creating a full active-project scaffold unless the operator explicitly approves the status-specific scaffold.

## Default Project Scaffold

When creation is approved for an active project, the OS MUST create:

```text
[PROJECT]/
  CLAUDE.md
  CONTEXT.md
  ROUTING.md
  _governance/
    README.md
  _memory/
    project-memory.md
    decisions.md
  _connectivity/
    README.md
  references/
    README.md
  setup/
    README.md
    new-project-intake.md
  stages/
    README.md
```

the OS MUST point to root law instead of copying root law into the project.

the OS MUST save the intake answers in:

```text
[PROJECT]/setup/new-project-intake.md
```

the OS MUST update `_handoffs/PROJECT-HANDOFF-STATE.md` when a project scaffold is created.

## Inputs

This standard accepts:

- A new project request.
- Intake answers.
- Existing the OS root routing, memory, governance, connectivity, and project template files.
- Optional references or implementation pointers named during intake.

## Outputs

This standard produces:

- A new project intake packet.
- A project folder scaffold when approved.
- Project-local identity, context, routing, governance, memory, decision, connectivity, reference, setup, and stage placeholder files.
- A root project handoff state entry.
- A stop or decision packet when project activation is unclear.

## Required Checks

Before creating a project folder, the OS MUST check:

- The folder does not already exist.
- Project status is not undecided.
- Project name and folder name are present.
- Root inheritance files exist.
- Known live systems are listed as pointers only.
- Credential storage is blocked.
- Public/client/legal/compliance/financial commitments are labeled before movement.
- The first next work item is named.

## MUST

- The setup MUST ask intake questions before creating the folder.
- The setup MUST classify project status before active scaffolding.
- The setup MUST create project-local `_connectivity/README.md` as a pointer and boundary file.
- The setup MUST keep project-specific truth inside the new project workspace.
- The setup MUST record known systems as `reference-only` or `blocked` unless explicit approval exists.
- The setup MUST update project handoff state when a project is created.
- The setup MUST block live-system action, credential use, public/client commitments, legal/compliance, and financial movement until approval is explicit.

## MUST NOT

- The setup MUST NOT create an active project folder from an undecided, placeholder, dormant, provisional, historical, or reference-only request without approval.
- The setup MUST NOT imply live-system permission by listing a system.
- The setup MUST NOT store secrets or credentials in markdown.
- The setup MUST NOT import legacy `C:\ExampleLegacy`, `CLIENTS/...`, `ExampleOps/...`, `C:\Dev`, archive, or external implementation assumptions as active truth without source authority.
- The setup MUST NOT ask the operator to design routine folder architecture before the OS proposes the scaffold.

## Intake Packet

Use this packet before creation:

```text
New project intake:
- Timestamp:
- Project display name:
- Root folder:
- Requested status:
- Purpose:
- Active scope:
- Out of scope:
- Starting source material:
- Known systems:
- Public/client/legal/compliance/financial sensitivity:
- First next work:
- Recommended scaffold:
- Risk:
- Approval state:
- Action:
- Stop conditions:
```

## Acceptance Test

This standard passes when the operator can run one intake setup, answer the first-step questions, and receive either:

- A complete active-project scaffold with project-local the OS connectivity deployed and handoff state updated, or
- A decision/intake packet that names why scaffold creation is blocked.

## Failure Test

This standard fails when a project folder is created before intake questions are answered, when connectivity is omitted, when credentials are stored, when a live-system pointer is treated as permission, when project status is undecided but active structure is created, or when the operator is asked to choose internal folder architecture.

## Escalation

Escalate to Conductor for project status, folder naming, routing, and sequence conflicts.

Escalate to Keeper/Recorder/Librarian for memory, exact record, intake packet, handoff state, and findability gaps.

Escalate to Steward for truth, proof, claims, refusal, correction, public-facing meaning, or client-facing commitments.

Escalate to Warden before any live-system, credential, secret, regulated-data, legal/compliance, domain, repo, automation, analytics, payment, account, form, email, CRM, or deployment movement.

Escalate to the operator with a decision packet when activation, business judgment, risk ownership, public/client commitment, legal/compliance, finance, or risk score 3+ approval is required.
