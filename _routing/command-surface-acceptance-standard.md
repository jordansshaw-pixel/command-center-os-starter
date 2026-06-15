# Command Surface Acceptance Standard

Status: Root routing standard draft
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

Architecture source:

- `_routing/atx-command-architecture-blueprint.md`

Generator artifact contract:

- `_routing/generator-artifact-contract.md`

## Purpose

This standard defines when an the OS command surface, map, cockpit, generated interface, or operator-facing architecture view is acceptable to use.

Short rule:

```text
The command surface is accepted only when it shows source-backed architecture state without creating new truth.
```

## Owner

Conductor owns command-surface routing and acceptance.

Librarian owns findability and source linkage.

Brand Guardian owns truth, proof, meaning, refusal, and correction review.

Sentinel owns risk scoring.

Builder owns generator or implementation changes only after routing permits movement.

## Operator-Facing Action

the operator may ask to view, improve, build, rename, polish, compare, or expand the the OS command surface.

the operator does not need to distinguish the command surface from architecture before the OS classifies it.

## System Action

the OS MUST classify whether the request changes:

- The architecture itself.
- The source map that represents architecture state.
- The generator that renders the command surface.
- The generated review output.
- The naming, acceptance criteria, or operator-facing semantics of the command surface.

the OS MUST route architecture changes to `_routing/atx-command-architecture-blueprint.md` or the relevant source-of-truth file before changing the visual surface.

## Required Source Chain

Every accepted command surface MUST have this chain:

```text
Architecture truth
-> source map
-> generator
-> generated review output
-> output index / findability pointer
```

Current the OS chain:

| Layer | Current Source |
|---|---|
| Architecture truth | `_routing/atx-command-architecture-blueprint.md` |
| Interface source map | `_routing/architecture-map.json` |
| Role status registry | `_agents/ROLE-STATUS.json` |
| Generator contract | `_routing/generator-artifact-contract.md` |
| Generator | `_routing/generate-architecture-wireframe.js` |
| Generated review output | `_output/2026-06-06-atx-command-center-neural-interface.html` |
| Output index | `_output/OUTPUT-INDEX.md` |

## Acceptance Criteria

The command surface is accepted only when all criteria pass:

| Criterion | Requirement |
|---|---|
| Source-backed | Every architecture claim on the surface is traceable to a named source file or marked as draft/provisional. |
| Architecture subordinate | The surface points to the architecture blueprint and does not claim to be the architecture itself. |
| State-labeled | Built, partial, missing, blocked, dormant, provisional, and undecided states are visually or textually distinguishable. |
| Project-locality safe | Project runtime truth is not centralized into root unless the root file is only a pointer or status-level reference. |
| No visual overclaim | Visual prominence does not imply operational readiness, live access, client commitment, or approval. |
| Generated from source | Generated outputs are regenerated from source maps or generator files, not hand-edited as source truth. |
| Reviewable | Output location and regeneration command are findable in `_output/OUTPUT-INDEX.md`. |
| Boundary safe | Live systems, credentials, permissions, external accounts, and production access are not implied by tool or project labels. |
| Operator useful | The surface helps the operator see current state, owner, next action, or gap without forcing him to classify internal taxonomy. |
| Drift checked | The surface has a failure test for source drift, stale project state, and visual implication. |

## MUST

- the OS MUST treat the command surface as a Layer 4 review artifact unless a separate approved control-system contract exists.
- the OS MUST apply `_routing/generator-artifact-contract.md` before creating or regenerating a command-surface artifact.
- the OS MUST use Builder for generator or implementation changes after routing and required review gates permit build movement.
- the OS MUST render role-like cards from `_agents/ROLE-STATUS.json` or another approved role-status registry, not from loose display-only labels.
- the OS MUST keep the architecture blueprint separate from generated interface output.
- the OS MUST update the source map before regenerating the interface when visual content changes.
- the OS MUST update the generator before regenerating the interface when layout or rendering logic changes.
- the OS MUST regenerate the output after source map or generator changes.
- the OS MUST verify source parseability and generated-output content after regeneration when practical.
- the OS MUST update `_output/OUTPUT-INDEX.md` when the command surface purpose, source, status, or content meaning changes.
- the OS MUST label current-state claims as built, partial, missing, blocked, dormant, provisional, undecided, draft, or review artifact where needed.
- the OS MUST validate source, contract, stage, runtime, and invocation state before rendering the OS roles or role-like lenses.
- the OS MUST escalate when visual changes imply new authority, activation, approval, live-system access, public claim, client commitment, or durable root law.

## MUST NOT

- the OS MUST NOT hand-edit generated HTML as source truth.
- the OS MUST NOT use visual polish to hide uncertainty, missing architecture, or partial status.
- the OS MUST NOT activate a project, specialist, integration, or live-system lane by adding it to the surface.
- the OS MUST NOT render queued, provisional, missing, dormant, or blocked roles as visually equivalent to active built roles.
- the OS MUST NOT show project runtime facts as current unless the project-local source supports them.
- the OS MUST NOT treat the command surface as a dashboard with live operational controls unless a control-system contract is created and approved.
- the OS MUST NOT use the command surface to bypass Brand Guardian, memory, routing, connectivity, or project-locality rules.
- the OS MUST NOT rename the command surface in source files without checking whether `Neural Interface`, `Command Surface`, or another name has been approved.

## Inputs

This standard accepts:

- User request about the OS map, cockpit, command surface, generated interface, or visual architecture.
- `_routing/atx-command-architecture-blueprint.md`
- `_routing/architecture-map.json`
- `_agents/ROLE-STATUS.json`
- `_routing/generator-artifact-contract.md`
- `_routing/generate-architecture-wireframe.js`
- `_output/OUTPUT-INDEX.md`
- Relevant root, project, memory, routing, governance, connectivity, and role sources.

## Outputs

Command-surface acceptance packet:

```text
Command surface acceptance:
- Request type: [view | source update | generator update | generated output | rename | expansion | review]
- Architecture source:
- Interface source:
- Generator:
- Output:
- Source-backed: [yes | no]
- State-labeled: [yes | no]
- Project-locality safe: [yes | no]
- Boundary safe: [yes | no]
- Visual overclaim risk: [none | low | medium | high]
- Accepted: [yes | no]
- Required correction:
- Next owner:
```

## Acceptance Test

This standard passes when:

- The command surface points to the architecture blueprint.
- The source map, generator, output, and output index are identified.
- The role-status registry is identified when role-like cards are rendered.
- The generator contract is identified and enforced.
- Generated output is produced from source and not hand-edited.
- Project, role, tool, and lane statuses do not imply unapproved activation.
- Missing or partial architecture is visible rather than hidden.
- Verification confirms source parseability and generated output contains expected content.

## Failure Test

This standard fails when:

- The surface presents itself as the architecture.
- The surface adds architecture truth not found in source files.
- A visual label implies live access, approval, or operational readiness without supporting source.
- A role-like card lacks explicit source, contract, stage, runtime, or invocation state.
- A project-local fact is centralized into root as runtime truth.
- A generated HTML file is edited as if it were source.
- The output index does not identify the source and regeneration path.
- The surface is visually polished but operationally misleading.

## Escalation

Escalate to Brand Guardian when the surface changes meaning, proof, oath, doctrine, external-facing claims, brand, or identity.

Escalate to Warden when the surface references live systems, credentials, permissions, accounts, integrations, or access state in a way that could imply permission.

Escalate to the operator when:

- The command surface name is being finalized.
- The surface would become a live dashboard or control system.
- The surface would show client-sensitive, financial, legal, live-system, or public-facing status.
- A project, specialist, or integration would appear active without settled source truth.

## Current the OS Result

Current status:

```text
Accepted as review artifact.
Not accepted as final command surface.
Not accepted as live dashboard.
Not accepted as operational control system.
```

Current approved movement:

- Source-backed review interface may be regenerated from `_routing/architecture-map.json`.
- The interface may show draft architecture state when labels remain explicit.
- Final naming and operational control behavior remain open.

## Next Action

Recommended next build item:

```text
Finish project handoff architecture for active lanes before adding richer project execution lanes to the command surface.
```
