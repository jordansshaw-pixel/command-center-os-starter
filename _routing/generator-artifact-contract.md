# Generator Artifact Contract


Status: Root routing standard
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This contract governs the OS generators that produce reviewable artifacts, command surfaces, maps, interfaces, reports, or other outputs from source files.

Short rule:

```text
No the OS generator may produce an artifact unless a contract defines its source, owner, allowed output, truth constraints, validation checks, and failure conditions.
```

## Owner

Conductor owns generator routing and movement authority.

Librarian owns source linkage, findability, and schema visibility.

Steward owns truth, proof, visual-overclaim refusal, and correction authority.

Builder owns generator implementation only after routing permits build movement.

## Operator-Facing Action

the operator may ask to generate, regenerate, view, improve, or expand an the OS artifact.

the operator does not need to know whether the request changes source data, generator code, rendered output, or acceptance rules before the OS classifies it.

## System Action

the OS MUST classify generator work before artifact production.

the OS MUST identify:

- Contract governing the generator.
- Source file or source files.
- Role-status registry when role-like cards are rendered.
- Generator file.
- Output file or output folder.
- Truth owner.
- Validation checks.
- Failure conditions.
- Whether the generated artifact is review output, source law, or an approved control surface.

## Current Generator Registry

| Generator | Contract | Source | Output | Status |
|---|---|---|---|---|
| `_routing/generate-architecture-wireframe.js` | This file plus `_routing/command-surface-acceptance-standard.md` | `_routing/architecture-map.json` plus `_agents/ROLE-STATUS.json` | `_output/2026-06-06-atx-command-center-neural-interface.html` | Review artifact generator |
| `_routing/generate-agent-review-interface.js` | This file plus `_routing/command-surface-acceptance-standard.md` | `_routing/agent-review-interface-map.json` | `_output/atx-agent-review-neural-interface/index.html` | Public-safe static review artifact generator |

## MUST

- the OS MUST have a named generator contract before creating or regenerating an artifact that shapes operator understanding.
- the OS MUST use Builder for generator implementation after routing and required review gates permit build movement.
- the OS MUST keep generated artifacts subordinate to their source files and contracts.
- the OS MUST validate source parseability before writing output.
- the OS MUST load role-like card status from `_agents/ROLE-STATUS.json` or another approved role-status registry.
- the OS MUST validate required truth-state fields before rendering roles, projects, live systems, integrations, command surfaces, or current-state claims.
- the OS MUST fail generation when a visual element could imply activation, approval, live access, or operational readiness without source support.
- the OS MUST render status, source, contract, stage, runtime, and invocation state when displaying the OS roles or role-like lenses.
- the OS MUST write generated artifacts only to an approved output path for the current generator.
- the OS MUST regenerate output after source-map or generator changes.
- the OS MUST update `_output/OUTPUT-INDEX.md` when artifact meaning, contract, source, or status changes.
- the OS MUST record durable generator corrections in `_memory/decision-log.md` when the operator approves the correction as future behavior.

## MUST NOT

- the OS MUST NOT let a generator infer truth from a display label alone.
- the OS MUST NOT render queued, provisional, dormant, missing, or blocked items as visually equivalent to active built items.
- the OS MUST NOT treat a folder name, roadmap name, source-map item, or UI card as proof that an agent, integration, project, or live system exists.
- the OS MUST NOT generate an operator-facing architecture artifact from an unconstrained source map.
- the OS MUST NOT hand-edit generated output as source truth.
- the OS MUST NOT write generated output outside the approved workspace output lane unless a project or stage contract explicitly authorizes it.

## Inputs

This contract accepts:

- Generator requests.
- Regeneration requests.
- Source-map updates.
- Generator implementation changes.
- Generated output corrections.
- Human-facing interface or artifact requests.

## Outputs

Generator movement packet:

```text
Generator movement:
- Request:
- Contract:
- Source:
- Role status registry:
- Generator:
- Output:
- Truth owner:
- Validation:
- Risk:
- Status:
- Failure condition:
- Memory impact:
- Next owner:
```

## Acceptance Test

This contract passes when:

- The generator names this contract or a more specific approved contract.
- Source, generator, output, and truth owner are explicit.
- Required truth-state fields are validated before rendering.
- Generated output visibly distinguishes active, queued, provisional, missing, blocked, draft, and review-artifact states where relevant.
- The generator fails before writing output when required truth fields are missing or unsupported.
- The output index identifies the source, generator, contract, and review status.

## Failure Test

This contract fails when:

- A generator produces an artifact without a named contract.
- A generated artifact displays a role, project, integration, live system, or current-state claim without explicit source-backed status.
- A queued or provisional role appears equivalent to an active role.
- The generated artifact becomes the apparent source of truth.
- Output is written to an unapproved destination.
- A durable generator correction remains only in chat.

## Escalation

Escalate to Steward when visual output may create false truth, hide uncertainty, or imply authority that source files do not prove.

Escalate to Warden when generated output references live-system access, credentials, permissions, accounts, tools, or integrations in a way that could imply permission.

Escalate to the operator when:

- A generator would become an operational control surface.
- A generated artifact would display client-sensitive, public, legal, financial, credential, or live-system status.
- A source map cannot safely distinguish real, queued, provisional, missing, and blocked states.
