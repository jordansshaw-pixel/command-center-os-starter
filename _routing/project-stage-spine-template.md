# Project Stage Spine Template

Status: Root routing template
Date: 2026-06-06

## Purpose

This template defines the default ICM Layer 2 stage spine for project workspaces.

It does not require every project to use the same stage names. It defines the minimum movement logic a project stage sequence must cover.

Short rule:

```text
Project stages must make movement legible from intake to handoff without hiding truth, memory, or live-system risk inside the run.
```

## Owner

Conductor owns stage sequence.

Marshal owns contract compliance.

Librarian owns findability and index pointers.

Keeper owns memory judgment.

Steward owns truth, proof, refusal, and correction authority.

Warden owns live-system and credential hard stops.

## Operator-Facing Action

the operator may ask for project work without naming a stage.

the OS MUST classify the likely project and stage from source evidence, then proceed or provide a decision packet if the route remains ambiguous.

## System Action

the OS MUST use this spine when creating or evaluating project stage architecture.

the OS MUST adapt stage names to the project domain while preserving the required movement functions.

## Default Stage Functions

| Function | Default Stage Pattern | Required Movement Question |
|---|---|---|
| Context / source state | `00_context` or project `CONTEXT.md` | What is true now, and what sources govern this run? |
| Intake / brief | `01_intake`, `01_brief`, or `01_discovery` | What entered, from where, and under what scope? |
| Requirements / gap map | `02_requirements`, `02_planning`, or `02_offer` | What must be true before output can be produced? |
| Assumptions / risk | `03_assumptions`, `03_review`, or project-specific judgment stage | What is proven, inferred, uncertain, risky, or blocked? |
| Design / plan / draft | `04_design`, `04_plan`, `04_draft`, or project-specific production stage | What is the proposed artifact, plan, or structure? |
| Build / output | `05_build`, `05_output`, or project-specific production stage | What artifact is produced and where does it live? |
| Review / test | `06_review`, `06_test`, or project-specific review stage | What proof, QA, compliance, or approval is required? |
| Handoff / close | `07_handoff`, `08_implementation-handoff`, or project-specific handoff stage | Who receives the work, what remains open, and what memory updates are required? |
| Improve / retro | `10_improve` when needed | What reusable lesson changes the system? |

## Required Project Stage Minimum

A project does not need every default stage.

Every active project MUST have enough project-local structure to answer:

- What is the current project truth?
- Where does intake or brief work enter?
- Where are requirements, assumptions, or risk judged?
- Where are outputs produced?
- Where are review/approval gates enforced?
- Where does handoff or closeout happen?
- Where do durable decisions and memory updates go?
- Where are live-system boundaries defined?

## Stage Folder Pattern

Default folder shape:

```text
[PROJECT]/
  stages/
    [NN_stage-name]/
      CONTRACT.md
      references/
      output/
```

`references/` MAY be omitted only when the project contract names a project-level reference destination and the stage contract points to it.

`output/` MAY be omitted only when the stage is explicitly non-output and the contract names the approved destination.

## MUST

- Stage spines MUST preserve project-local context, routing, memory, and connectivity boundaries.
- Stage spines MUST name the route from current work to next movement.
- Stage spines MUST make review gates explicit before public, client-facing, legal, compliance, financial, live-system, or implementation movement.
- Stage spines MUST define where durable decisions are saved.
- Stage spines MUST define how source gaps, blocked work, and unresolved decisions are handed off.

## MUST NOT

- Stage spines MUST NOT imply that a project is active because a folder exists.
- Stage spines MUST NOT import old or legacy stage sequences without source review.
- Stage spines MUST NOT route runtime artifacts into a method-engine folder unless that folder is the approved destination workspace.
- Stage spines MUST NOT skip memory and handoff just because output exists.
- Stage spines MUST NOT create project execution lanes before project truth and inheritance are defined.

## Inputs

This template accepts:

- A project folder.
- Existing project stages.
- A new project architecture plan.
- A project cleanup request.
- A method-engine or runtime-output routing question.

## Outputs

This template produces:

- A project stage-spine recommendation.
- A missing-stage-function list.
- A stage hardening queue.
- A decision packet when project status, activation, or stage ownership is unclear.

## Acceptance Test

This spine passes when a future agent can enter a project, identify the current stage, know what sources to load, know where output belongs, know which review gates apply, and know where to hand off or stop.

## Failure Test

This spine fails when project work can move from request to artifact without a named stage, source check, memory path, review gate, output destination, and handoff or stop condition.

## Escalation

Escalate to Conductor for stage sequence or project routing conflicts.

Escalate to Marshal for missing deterministic contract fields.

Escalate to Steward for truth, proof, claim, refusal, correction, or public/client-facing meaning.

Escalate to Keeper/Recorder/Librarian for memory, exact record, or findability gaps.

Escalate to Warden for credentials, live systems, regulated data, legal/compliance, production-domain, repo, automation, analytics, or external-system movement.

Escalate to the operator only with a decision packet when project activation, risk ownership, business judgment, public/client commitment, or risk score 3+ requires human authority.
