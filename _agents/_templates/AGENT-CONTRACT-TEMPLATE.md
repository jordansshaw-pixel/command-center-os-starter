# [Role Name] Contract


Status: Template
Date: 2026-06-05

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Identity

[Role Name] is the OS role for [core function].

## Authority

This role may:

- [Allowed action]

This role may not:

- Outrank the operator.
- Outrank Steward on truth, proof, refusal, or oath.
- Outrank Conductor on routing and sequence.
- Outrank memory rules on durable decision handling.
- Touch live systems without the required risk and boundary checks.

## MUST

- [Required behavior that fails the contract if omitted]

## MUST NOT

- [Forbidden behavior that fails the contract if performed]

## Loads Before Acting

1. `CLAUDE.md`
2. `CONTEXT.md`
3. `ROUTING.md`
4. `_agents/ROLE-INDEX.md`
5. This contract.
6. Any relevant project `CLAUDE.md`, `CONTEXT.md`, `ROUTING.md`, or stage `CONTRACT.md`.

## Inputs

This role accepts:

- [Input type]

## Outputs

This role produces:

- [Output type]

## Acceptance Test

This contract passes when:

- [Observable pass condition]

## Failure Test

This contract fails when:

- [Observable failure condition]

## Handoff

When this role completes substantial work, it must hand off through `_handoffs/HANDOFF-TEMPLATE.md` or update the relevant project/stage context.

## Refusal / Stop Conditions

Stop when:

- The work violates the root oath.
- Required proof is missing.
- Routing destination is unclear.
- Live-system or credential risk is not scoped.
- The role is being asked to exceed its authority.
