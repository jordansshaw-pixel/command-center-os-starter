# Operator Truths

Status: EMPTY SCAFFOLD — populate during operator onboarding
Edition: Community / distributable starter

## Purpose

This file is the first-class source for the operator's durable truths inside Command Center OS.

Operator truth is upstream of governance. Brand Guardian / Steward inherits from this canon, then
applies proof, refusal, and correction standards through `_governance/brand-guardian.md`.

Short rule:

```text
Agents should not infer the operator's worldview from scattered corrections when a canon exists.
```

> **First run:** the Core Operator Truths table below is intentionally empty except for the universal
> system invariants. Run `_routing/runtime/routes/operator-onboarding.md` to add your own truths
> (who you are, what you build, your standards, your boundaries). Until then, treat operator-specific
> judgment as unknown and ask before assuming.

## Authority

The operator is the final human authority.

This file may record:

- User-confirmed operator truths.
- Source-confirmed operator truths already written into root files.
- Inferred or provisional truths, only when clearly labeled.

This file does not own:

- Project-specific facts.
- Client-specific truth.
- Live-system state.
- Temporary working drafts.
- External claims that require evidence.

## Status Labels

Use these labels for every truth claim that may affect downstream action:

| Status | Meaning |
|---|---|
| User-confirmed | The operator directly stated or approved it. |
| Source-confirmed | Existing root files already establish it. |
| Inferred | Reasoned from available material, but not directly confirmed. |
| Provisional | Useful draft pending later review or refinement. |

## Core Operator Truths

These universal system invariants ship with the OS. **Add operator-specific truths during onboarding.**

| Truth | Status | Source |
|---|---|---|
| The operator is the final human authority. | Source-confirmed | `CLAUDE.md` |
| Command Center OS exists to keep the operator's judgment, memory, ventures, clients, and agents aligned with what is true before anything moves. | Source-confirmed | `CLAUDE.md` |
| Truth before action. | Source-confirmed | `CLAUDE.md` |
| Judgment before automation. | Source-confirmed | `CLAUDE.md` |
| Memory before rediscovery. | Source-confirmed | `CLAUDE.md` |
| Routing before production. | Source-confirmed | `CLAUDE.md`, `ROUTING.md` |
| Proof before claims. | Source-confirmed | `CLAUDE.md`, `_governance/brand-guardian.md` |
| Correction before scale. | Source-confirmed | `CLAUDE.md`, `_governance/brand-guardian.md` |
| Boundaries before live-system access. | Source-confirmed | `CLAUDE.md`, `_connectivity/` |
| The OS improves through action, not only information. | Source-confirmed | `_routing/proactive-action-standard.md` |
| Human-facing architecture interfaces are truth surfaces and must be updateable from a named source of truth. | Source-confirmed | `_routing/architecture-map.json` |
| If something is queued to be built, it must be built before it is used. | Source-confirmed | this file |
| All meaningful work must resolve into routing, memory judgment, and truth authority before it moves or is treated as complete. Conductor owns routing, Keeper owns memory judgment, and Steward / Brand Guardian owns truth authority. Librarian makes work findable but does not replace those authorities. | Source-confirmed | this file |
| Specificity in truth matters. Truth needs scope, source, owner, and approval state. | Source-confirmed | this file |
| What is true at root may not be true for a given project unless inheritance or local truth is explicit. | Source-confirmed | this file |
| A project dropped into a command center must carry its own findings, planning, memory, governance, connectivity, and stage truth so it can run accordingly. Root stores the operating rule, not the project's operational information. | Source-confirmed | this file |
| AI must not turn the operator's judgment, client reality, or project identity into generic output. | Source-confirmed | `_governance/brand-guardian.md` |

## Operator-Specific Truths

_Not yet captured. Run `python install.py` (or follow the operator-onboarding route) to record who you
are, what you build, your standards, and your boundaries. Each becomes a labeled truth here._

## Truth Scope Rule

Every durable truth should carry:

- Scope: root, operator, governance, project, client, stage, interface, or implementation.
- Source: file, decision log entry, operator statement, observed artifact, or external evidence.
- Owner: the operator, Operator Canon, Brand Guardian, Conductor, project owner, or named role.
- Approval state: user-confirmed, source-confirmed, inferred, or provisional.

Short rule:

```text
Truth without scope can drift into false universality.
```

## Pushdown Rule

Operator truth moves through the OS in this order:

```text
Operator
-> Operator Canon
-> Steward / Brand Guardian worldview
-> Conductor routing discipline
-> Sentinel risk logic
-> Signal signal structure
-> Voice voice and resonance
-> Build-time architecture review through Conductor, Analyst, Pathfinder, Theorist, active roles, and source inspection
-> Implementation through Builder only after Conductor routes and required review gates permit movement
-> Project execution
-> Memory, source improvement, and generated interfaces
```

Downstream agents may inherit Operator Canon, but they must not overwrite it.

## Project Locality Rule

Project workspaces are portable operating units.

Project-specific findings, planning outputs, implementation state, connectivity pointers, live-system
boundaries, decisions, open loops, and stage truth MUST be saved inside the project workspace when the
project needs them to operate.

Root MUST NOT become required runtime memory, workflow state, data storage, or operational authority
for a project. If a project is moved or its root connection is broken, the project MUST still operate
from its own local memory, routing, connectivity, governance, stages, and implementation pointers.

Short rule:

```text
Root may carry reference analysis. The project must carry what it needs to run.
```

## Review Gate

If a new operator truth is inferred from behavior rather than directly confirmed, label it `Inferred`
or `Provisional` and route it to Brand Guardian or the operator before using it as durable law.
