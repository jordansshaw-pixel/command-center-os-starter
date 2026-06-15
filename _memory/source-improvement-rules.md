# Source Improvement Rules

Status: Root source-improvement draft
Date: 2026-06-05

## Purpose

the OS must improve the source of future behavior, not only patch the current output.

Core rule:

```text
Editing the output fixes one run.
Editing the source fixes every future run.
```

## Trigger

Create a source-improvement candidate when:

- the operator gives the same correction more than once.
- A correction exposes a missing rule.
- An agent asks a question already answered in saved files.
- An agent asks the operator a vague or blind question instead of preparing a decision packet.
- Context loss causes rediscovery or repeated explanation.
- A routing mistake sends work to the wrong folder.
- A project-local file duplicates root law.
- A stale path becomes active by accident.
- A final answer omits required handoff, changed files, or open loops.
- A human-facing architecture interface is created without a source of truth and update path.
- A surfaced truth ends as information only when a safe source-improving action was available.
- the OS asks the operator to classify routine file/reference placement before inspecting evidence and recommending a destination.

## Candidate Format

```text
Source improvement:
- Problem:
- Correct behavior:
- Affected source file:
- Evidence:
- Approval status:
- Next owner:
```

## Default Destinations

| Problem | Destination |
|---|---|
| Root identity confusion | `CLAUDE.md` |
| Routing confusion | `ROUTING.md`, `_routing/router-contract.md`, `_routing/destination-map.md` |
| Blind or vague questions | `_routing/decision-packet.md`, `AGENTS.md`, `ROUTING.md` |
| Memory loss or rediscovery | `_memory/MEMORY-ROUTER.md`, `_memory/memory-rules.md` |
| Missing decision record | `_memory/decision-log.md` |
| Claude/Codex drift | `_memory/sync-rules.md` |
| Truth/proof/refusal issue | `_governance/brand-guardian.md` |
| Project-specific stale context | `[PROJECT]/CONTEXT.md` or `[PROJECT]/ROUTING.md` |
| Live-system or credential boundary | `_connectivity/` |
| Human-facing architecture interface drift | `_routing/architecture-map.json`, generator script, and affected `_output/` artifact |
| Missing proactivity after truth surfaced | `_routing/proactive-action-standard.md`, affected source file, and `_memory/decision-log.md` |
| Missing or thin Operator Canon | `_operator/`, `CLAUDE.md`, `ROUTING.md`, `_governance/brand-guardian.md`, affected agent contracts, and `_memory/decision-log.md` |
| Operator-load failure in file/reference placement | `_operator/OPERATOR-LOAD-STANDARD.md`, `_routing/destination-map.md`, `ROUTING.md`, `_agents/librarian/`, and `_memory/decision-log.md` |
| Missing drop zone for unsorted references and artifacts | `_intake/`, `_routing/destination-map.md`, `ROUTING.md`, `_agents/librarian/`, and `_memory/decision-log.md` |
| Loose contract language allows interpretation drift | `_routing/deterministic-contract-language-standard.md`, affected templates/contracts/tests, and `_memory/decision-log.md` |

## Current Source-Improvement Candidates

### 2026-06-05 - Context Drop Recovery

Status: User-confirmed and implemented in root draft files

Problem:

Closing VS Code or losing session context caused the agent to act as if answered the OS routing and memory decisions were still open.

Correct behavior:

Treat context loss as a memory-resume event. Load saved root files and continue from the roadmap and decision log before asking the operator to restate settled decisions.

Affected source files:

- `_routing/router-contract.md`
- `_memory/memory-rules.md`
- `_memory/decision-log.md`

Next owner:

- Conductor for resume routing.
- Keeper for relevant memory.
- Recorder for exact decision record.
- Librarian for findability.

### 2026-06-05 - Blind Question Correction

Status: User-confirmed and implemented in root draft files

Problem:

The agent kept asking vague continuation or scope questions after the OS had already invested in answering the underlying governance and routing questions.

Correct behavior:

When the operator judgment is needed, the OS must prepare a decision packet: what is known, what is settled, what remains unresolved, options, tradeoffs, recommended default, and the specific approval or override needed.

Affected source files:

- `_routing/decision-packet.md`
- `AGENTS.md`
- `CLAUDE.md`
- `ROUTING.md`
- `_routing/router-contract.md`
- `_memory/memory-rules.md`
- `_memory/decision-log.md`

Next owner:

- Conductor for routing discipline.
- Keeper for surfacing prior decisions.
- Brand Guardian for governance-level correction.

### 2026-06-06 - Human Interface Truth Source Rule

Status: User-confirmed and implemented

Problem:

The architecture wireframe was useful as a human interface, but as standalone HTML it could drift from the OS structure as wiring changed.

Correct behavior:

Human-facing architecture interfaces must be generated from a named source of truth or otherwise carry an explicit update rule at inception and during execution.

Affected source files:

- `_routing/architecture-map.json`
- `_routing/generate-architecture-wireframe.js`
- `_output/README.md`
- `_agents/AGENT-TEST-STANDARD.md`
- `_memory/decision-log.md`

Next owner:

- Librarian for findability.
- Conductor for routing discipline.
- Recorder for exact record.

### 2026-06-06 - Truth Must Route To Action

Status: User-confirmed and implemented

Problem:

the OS had baseline governance and routing infrastructure, but still relied on the operator to ask the question that surfaced the actionable truth. That made the system too reactive and too close to a search engine.

Correct behavior:

When the OS surfaces a reusable truth, gap, missing rule, weak evidence lane, stale source, or broken workflow, it must route the smallest safe action that improves the system.

Affected source files:

- `CLAUDE.md`
- `ROUTING.md`
- `_routing/proactive-action-standard.md`
- `_memory/decision-log.md`
- `_memory/source-improvement-rules.md`

Next owner:

- Conductor for routing truth to action.
- Steward / Brand Guardian for truth and correction authority.
- Keeper, Recorder, and Librarian for memory, exact record, and findability.

### 2026-06-06 - Operator Canon Source Layer

Status: User-confirmed and implemented

Problem:

Operator truth, voice, judgment, load, and approval were present across scattered root files and chat corrections, but not enshrined in a first-class source layer.

Correct behavior:

Create `_operator/` as the source layer for Operator Canon, keep it upstream of governance, and wire root files and role contracts to load it when relevant.

Affected source files:

- `_operator/`
- `CLAUDE.md`
- `AGENTS.md`
- `CONTEXT.md`
- `ROUTING.md`
- `_routing/destination-map.md`
- `_routing/architecture-map.json`
- `_governance/brand-guardian.md`
- `_agents/steward/CONTRACT.md`
- `_agents/voice/CONTRACT.md`
- `_memory/decision-log.md`

Next owner:

- Steward / Brand Guardian for truth inheritance.
- Voice for voice translation.
- Conductor for routing and approval sequencing.
- Librarian for findability.

### 2026-06-06 - Do Not Make Operator Classify Placement

Status: User-confirmed and implemented

Problem:

the OS answered a reference-placement question by asking the operator to identify whether the reference was the OS root, ExampleWeb, ExampleAgency, or stage-specific. That pushed classification work back onto the operator and increased load.

Correct behavior:

the OS should inspect available evidence, classify likely scope and destination, and present a recommended placement. the operator should only approve, override, or decide when risk or ambiguity remains after the system has done the classification work.

Affected source files:

- `_operator/OPERATOR-LOAD-STANDARD.md`
- `_operator/OPERATOR-JUDGMENT.md`
- `_operator/OPERATOR-APPROVAL-STANDARD.md`
- `ROUTING.md`
- `_routing/destination-map.md`
- `_routing/decision-packet.md`
- `_agents/librarian/CONTRACT.md`
- `_agents/librarian/stages/02_judgment/CONTRACT.md`
- `_memory/decision-log.md`
- `_memory/source-improvement-rules.md`

Next owner:

- Librarian for file/reference classification.
- Conductor for routing.
- Sentinel for risk.
- the operator for approval or override only when required.

### 2026-06-06 - Root Intake Lane For Unsorted Files

Status: Superseded by single-drop intake correction on 2026-06-06

Problem:

Even after the OS stopped asking the operator to classify files, there was no neutral place for the operator to put unsorted references and artifacts before classification.

Correct behavior:

Create `_intake/` with separate `references/` and `artifacts/` sublanes. the operator can drop files there; Librarian classifies, indexes, and recommends movement.

Affected source files:

- `_intake/`
- `CLAUDE.md`
- `AGENTS.md`
- `CONTEXT.md`
- `ROUTING.md`
- `_routing/destination-map.md`
- `_routing/architecture-map.json`
- `_routing/generate-architecture-wireframe.js`
- `_agents/librarian/CONTRACT.md`
- `_agents/librarian/stages/01_intake/CONTRACT.md`
- `_agents/librarian/stages/02_judgment/CONTRACT.md`
- `_memory/MEMORY-ROUTER.md`
- `_memory/decision-source-index.md`
- `_memory/decision-log.md`

Next owner:

- Librarian for intake classification.
- Conductor for route.
- Warden for sensitive-file boundaries.

Superseded because:

The original `_intake/references/` and `_intake/artifacts/` split still asked the operator to classify the file before the OS inspection.

### 2026-06-06 - Deterministic Contract Language

Status: User-confirmed and implemented

Problem:

the OS contract language was too loose. The system could satisfy the apparent folder or routing rule while violating the operator-load truth.

Correct behavior:

Durable contracts, standards, folder lanes, and operator-facing workflows must use deterministic language: MUST, MUST NOT, owner, acceptance test, failure test, and escalation path.

Affected source files:

- `_routing/deterministic-contract-language-standard.md`
- `_agents/_templates/AGENT-CONTRACT-TEMPLATE.md`
- `_agents/_templates/AGENT-STAGE-CONTRACT-TEMPLATE.md`
- `_agents/AGENT-TEST-STANDARD.md`
- `_agents/sentinel/RISK-STANDARD.md`
- `ROUTING.md`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTEXT.md`

Next owner:

- Conductor for routing determinism.
- Librarian for classification determinism.
- Sentinel for interpretation-drift risk.
- Brand Guardian / Steward for truth/correction halt.

### 2026-06-06 - Single Intake Drop Lane

Status: User-confirmed and implemented

Problem:

The first `_intake/` build gave the operator two cleaner classification buckets: `references/` and `artifacts/`. That still created operator load.

Correct behavior:

The operator-facing intake path must be singular: `_intake/drop/`. Classification outcomes are internal.

Affected source files:

- `_intake/`
- `_routing/destination-map.md`
- `ROUTING.md`
- `_agents/librarian/CONTRACT.md`
- `_agents/librarian/stages/03_output/CONTRACT.md`
- `_memory/decision-log.md`

Next owner:

- Librarian for intake classification.
- Conductor for routing.
- Warden for sensitive-file stop conditions.

## Approval Rule

Do not silently rewrite root law from a source-improvement candidate unless the correction is user-confirmed or clearly marked as provisional.

When in doubt, add the candidate and route it to Brand Guardian or the operator for approval.
