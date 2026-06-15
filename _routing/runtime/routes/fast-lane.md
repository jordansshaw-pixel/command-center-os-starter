# Route Card: Fast Lane

Status: active runtime card
Date: 2026-06-07

## Trigger

Internal, reversible, source-clear work that appears risk 0 or 1.

## Load Next

- `_agents/conductor/doctrine/routing-sequence-handoff.md`
- `_agents/sentinel/doctrine/risk-gates.md`
- `_routing/source-archive/2026-06-07/low-risk-fast-lane-standard.md` only if eligibility is uncertain.
- Target file or nearest local instruction file.

## Required Roles

Conductor and Sentinel. Add Signal for substantial movement.

## Stop Conditions

Fast lane fails closed if risk is 2+, source/destination is unclear, more than one authority boundary appears, or live/client/public/credential/legal/financial movement appears.

## Output

Fast-lane signal with source, destination, risk, reversibility, stop condition, verification, blockers, and next action.

## Provenance

Source archive: `_routing/source-archive/2026-06-07/low-risk-fast-lane-standard.md`.
