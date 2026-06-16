# Route Card: Live System


Status: active runtime card
Date: 2026-06-07

## Trigger

Any website, DNS, deployment, repo push, CRM, API, automation, analytics, form, email, calendar, payment, credential, or external account action.

## Load Next

- `_agents/warden/doctrine/live-system-hard-stops.md`
- `_connectivity/live-system-risk-rules.md`
- `_routing/atx_live_system_gate.py`
- Project `_connectivity/README.md` when scoped to a project.
- Warden contract only when live-system judgment must be produced.

## Packet Completeness Gate

Before live-system movement, validate the packet form with `_routing/atx_live_system_gate.py`.

A failed gate is a hard stop because the live-system packet is incomplete or internally inconsistent.

A passed gate only means the packet has the required fields and internal consistency needed for review. It advances work to the existing Warden and the operator approval step. It is not approval and does not authorize the action.

## Required Roles

Warden, Sentinel, Signal, Conductor, Steward.

## Stop Conditions

Risk is 4 until scoped down. Stop without explicit the operator approval, owner, source, permission class, rollback path, and credential handling.

## Output

Live-system packet with system, scope, action, owner, permission, risk, approval, blocked actions, safe actions, and next action.

## Provenance

Source archive: `_routing/source-archive/2026-06-07/ROOT-ROUTING.md`; root source: `_connectivity/live-system-risk-rules.md`.
