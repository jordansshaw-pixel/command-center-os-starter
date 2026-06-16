# Forklift Readiness Standard

Status: Root routing standard draft
Date: 2026-06-14

## Purpose

This standard defines how the OS separates active operating files from original build material so the root command center can be copied into a clean install without dragging historical planning into daily runtime.

Short rule:

```text
Active files run the system. Archives prove where it came from. References explain why it was designed.
```

## Owner

Conductor owns folder cleanup sequence and active/install boundaries.

Librarian owns findability, indexes, manifests, and pointer hygiene.

Keeper owns memory relevance and whether material remains active, archive, or reference.

Steward owns governance truth and prevents source evidence from being treated as active law.

## Scope

This standard applies to the OS root system folders:

- `_agents/`
- `_connectivity/`
- `_governance/`
- `_handoffs/`
- `_intake/`
- `_memory/`
- `_operator/`
- `_output/`
- `_routing/`
- `.githooks/`
- `.github/`
- `.vscode/`
- root reference folders such as `agent-os-architect-brief-references/`

It does not apply to project or workspace folders unless a separate project-local cleanup is explicitly routed.

## Classification Labels

Use these labels during folder review:

| Label | Meaning |
|---|---|
| `active` | Required for daily boot, routing, governance, memory, handoff, connectivity, or role operation. |
| `source-archive` | Exact prior source, superseded operating law, compaction original, completed audit, or provenance file. |
| `reference` | Planning, research, comparative map, external source, inspiration, or design rationale. |
| `output` | Generated artifact, one-run review artifact, interface render, or evaluation output. |
| `local` | Machine, editor, Git, environment, or install-local support. |
| `project` | Project/workspace material excluded from this root pass. |

## Required Folder Shape

Each reviewed system folder should expose:

```text
[folder]/
  README.md
  active files
  references/       # only when reusable reference material belongs in this folder
  source-archive/   # only when exact prior source/provenance belongs in this folder
  log-archive/      # only for chronological operational logs
```

Do not create empty archive/reference folders unless the reviewed folder needs them now.

## Process

1. Inventory one root system folder.
2. Exclude project/workspace folders.
3. Classify every file as `active`, `source-archive`, `reference`, `output`, `local`, or `project`.
4. Keep active install files at the folder root or documented runtime location.
5. Move original planning and creation material to `references/` when it explains design but is not source law.
6. Move superseded source, completed audits, compaction originals, and provenance packets to `source-archive/`.
7. Add or update `README.md` with active files, no-load defaults, archive/reference locations, and forklift-install role.
8. Add `SOURCE-MANIFEST.md` when archiving exact source/provenance files.
9. Update pointer files that referenced old paths.
10. Stop before deleting material unless a separate cleanup decision approves deletion.

## Forklift Acceptance Test

A reviewed folder passes when:

- A clean the OS install can operate from active files only.
- Archives and references are clearly marked as non-runtime.
- Original build material remains findable.
- README names what loads by default and what does not.
- Existing pointers no longer send agents to stale paths.

## Failure Test

The pass fails when:

- Planning/research files remain beside active operating law without labels.
- A clean install needs historical planning files to boot.
- Archive/reference material is treated as current law.
- Old paths remain in indexes after files move.
- Project folders are changed during a root-only pass.

## Output Packet

Use this packet for each reviewed folder:

```text
Forklift readiness:
- Folder:
- Active files:
- Source archive:
- References:
- Outputs:
- Local/install-only files:
- Moves made:
- Pointers updated:
- Remaining open:
- Forklift status: [ready | partial | blocked]
```

## Stop Conditions

Stop and create a decision packet before:

- Deleting source, references, logs, or generated artifacts.
- Moving live-system, credential, legal/compliance, financial, or client-sensitive material.
- Changing root law instead of only moving/indexing it.
- Applying this root pass inside project/workspace folders.
