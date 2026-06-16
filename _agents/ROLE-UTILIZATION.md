# Role Utilization


Status: Root audit and routing evidence
Date: 2026-06-07
Timestamp: 2026-06-07 16:30:09 -05:00

## Purpose

This file tracks whether active OS roles are actually being invoked in practice.

Short rule:

```text
Role folders prove availability. Utilization evidence proves whether routing is using them.
```

## Current Evidence

Source checked:

- `_agents/ROLE-STATUS.json`
- `_agents/AGENT-RUN-LOG.md`
- `_routing/multi-agent-engagement-standard.md`
- `_routing/atx_multi_agent_gate.py`
- `_agents/BUILD-TIME-REVIEW-STANDARD.md`

Observed active-agent run-log counts as of 2026-06-07 16:30:09 -05:00:

| Active agent label | Count |
|---|---:|
| Conductor | 37 |
| Librarian | 12 |
| Builder | 4 |
| Marshal | 1 |
| session runner | 1 |
| `[role or session runner]` template line | 1 |

This is provisional evidence, not proof that other roles were never used. A role may have been used inline without being logged.

Latest role-invocation evidence:

- 2026-06-07 16:30:09 -05:00: ExampleWeb active path pointer cleanup invoked Conductor, Librarian, Keeper, Recorder, and Warden. No triggered roles were skipped.
- 2026-06-07 16:21:13 -05:00: ExampleWeb GHL media reference preservation invoked Conductor, Librarian, Recorder, Keeper, Warden, and Steward. No triggered roles were skipped.
- 2026-06-07 16:09:22 -05:00: ExampleAgency stale path cleanup rehearsal invoked Conductor, Librarian, Keeper, and Warden. No triggered roles were skipped.
- 2026-06-07 15:57:43 -05:00: Doctrine path registry pass invoked Conductor, Librarian, Marshal, Mechanic, and Recorder. No triggered roles were skipped.
- 2026-06-07 15:52:33 -05:00: the OS log pruning pass invoked Conductor, Keeper, Recorder, Librarian, Marshal, Mechanic, and Steward. No triggered roles were skipped.
- 2026-06-07 15:47:44 -05:00: Root boot compaction pass invoked Conductor, Keeper, Recorder, Librarian, Steward, Marshal, Mechanic, and Signal. No triggered roles were skipped.
- 2026-06-07 15:40:55 -05:00: Runtime Tier 0 cutover pass invoked Conductor, Keeper, Recorder, Librarian, Marshal, Mechanic, Steward, and Signal. No triggered roles were skipped.
- 2026-06-07 15:35:38 -05:00: Doctrine-aware runner compatibility pass invoked Conductor, Marshal, Mechanic, Librarian, Builder, Keeper, Recorder, and Signal. No triggered roles were skipped.
- 2026-06-07 15:22:53 -05:00: Runner compatibility was added to the lean runtime plan. Invoked Conductor, Mechanic, Marshal, and Librarian. No triggered roles were skipped.
- 2026-06-07 15:16:31 -05:00: Agent doctrine runtime pass invoked Conductor, Keeper, Recorder, Librarian, Marshal, Mechanic, Sentinel, Signal, Steward, Warden, Analyst, Pathfinder, Theorist, Builder, Voice, Liaison, and Scout. No triggered roles were skipped.
- 2026-06-07 14:55:05 -05:00: Lean routing runtime implementation invoked Conductor, Keeper, Recorder, Librarian, Marshal, Mechanic, Sentinel, Signal, Steward, and Builder. No triggered roles were skipped.
- 2026-06-07 13:58:14 -05:00: `Test-Routing-Rehearsal/` minimal routing rehearsal invoked Conductor, Keeper, Recorder, Librarian, Steward, Analyst, Pathfinder, Warden, Theorist, Sentinel, Signal, Marshal, Mechanic, Liaison, Scout, and Builder. Voice was triggered by public/landing-page wording but skipped because the wording was stopped as unusable test material rather than refined.

## Finding

the OS has 17 invokable roles in `_agents/ROLE-STATUS.json`.

The practical audit surface currently shows heavy concentration around a small runner set.

The likely failure mode is:

```text
Contracts and stages exist, but routing does not provide a cheap enough trigger path to invoke specialists consistently.
```

Related failure mode:

```text
The system may describe roles as optional or conditional, then skip them silently under context pressure.
```

## Correction Source

Compact role routing is now defined in:

- `_agents/ROLE-INVOCATION-MATRIX.md`

## Required Run-Log Fields

For substantial agent work, `_agents/AGENT-RUN-LOG.md` entries MUST include:

- Primary runner.
- Invoked roles.
- Triggered roles skipped.
- Skip reason.

These fields prevent apparent completion when the role architecture was not actually engaged.

## Acceptance Test

This utilization file passes when:

- Future substantial run-log entries distinguish primary runner from invoked roles.
- Triggered specialists are either invoked or skipped with a reason.
- Run-log evidence no longer requires guessing whether role routing happened.

## Failure Test

This utilization file fails when:

- Role invocation remains invisible in logs.
- Optional specialists are skipped without reason.
- Context-bloat concerns are solved by using fewer roles instead of cheaper role selection.

## Next Owner

Conductor owns enforcement.

Mechanic owns diagnosis if role-skipping recurs.

Librarian owns findability.
