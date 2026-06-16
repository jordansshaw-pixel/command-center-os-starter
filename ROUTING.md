# Root Routing


Status: compact active routing pointer
Date: 2026-06-14

## Rule

Use compact runtime routing first. Load source evidence only after route selection.

## Boot

Runtime Tier 0:
1. `CLAUDE.md`
2. `CONTEXT.md`
3. `_memory/SESSION-BOOT-STATE.md`
4. `_routing/runtime/ROUTING-KERNEL.md`
5. `_routing/runtime/ROUTE-INDEX.md`
6. `_memory/runtime/MEMORY-KERNEL.md`
7. `_memory/runtime/LOAD-INDEX.md`

Do not default-load long standards, broad logs, archives, generated maps, role contracts, or project-local memory.

## If / Then

| If request involves | Then load |
|---|---|
| new/repaired workspace | `routes/project-scaffold.md` |
| website, CRM, API, DNS, deploy, repo push, email, calendar, automation, credential | `routes/live-system.md` |
| decision, durable finding, correction, source improvement | `routes/memory-write.md` |
| truth, proof, brand, public/client wording, unsupported claim | `routes/proof-claims.md` |
| build, prototype, script, generator, implementation | `routes/build-prototype.md` |
| resume, pause, transfer, next owner | `routes/handoff.md` |
| internal reversible low-risk edit | `routes/fast-lane.md` |
| multi-boundary or multi-role work | `routes/role-engagement.md` |
| context loss, startup recovery, boot pressure | `routes/context-recovery.md` |
| file placement, stale path, reference classification | `routes/reference-placement.md` |

If multiple rules match: choose highest risk. If unclear: start with `role-engagement.md`.

## Authority

Conductor owns route, destination, sequence, next owner.
Keeper owns memory relevance, write/no-write judgment, source-improvement need.
Steward owns truth, proof, refusal, correction, governance authority.
Sentinel scores non-trivial risk. Warden blocks live-system or credential movement without approval.

## Stops

Stop before live-system, credential, public/client, legal/compliance, financial, stale-path, destructive, or risk 3+ movement.

Use `_routing/decision-packet.md` when the operator must decide. Do not ask blind questions.

For substantial work, close with: what learned, where saved, what remains open, next role, files changed/reviewed.
