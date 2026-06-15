# Runtime Load Index

Status: active Tier 0 runtime
Date: 2026-06-07

## Purpose

Name what may load at each runtime layer.

## Layers

| Layer | Load |
|---|---|
| Boot | `CLAUDE.md`, `CONTEXT.md`, `SESSION-BOOT-STATE.md`, `ROUTING-KERNEL.md`, `ROUTE-INDEX.md`, `MEMORY-KERNEL.md`, `LOAD-INDEX.md` |
| Route | One route card from `_routing/runtime/routes/` |
| Role | `ROLE-STATUS.json`, `ROLE-INVOCATION-MATRIX.md`, triggered agent doctrine, then specific role contract only when needed |
| Memory | `MEMORY-KERNEL.md`, then compact index or named evidence |
| Evidence | Specific log, archive, generated map, project memory, or source file named by the route |
| Archive | Source archive only for audit, validation, or provenance checks |

## Budget

Runtime files target 60 lines or fewer. Exceptions must state why the extra lines reduce total context load.

## Log Rule

Use `LOG-PRUNING-RULE.md` when OS-owned logs exceed the active-log threshold.

## Cutover State

This index is active for Tier 0 runtime load. Full source files remain available as targeted evidence.
