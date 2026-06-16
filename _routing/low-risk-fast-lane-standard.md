# Low-Risk Fast Lane Standard

Status: Root routing standard draft
Date: 2026-06-06

Contract language standard:

- `_routing/deterministic-contract-language-standard.md`

## Purpose

This standard defines when the OS may move reversible internal work without running the full build-time review sequence.

Short rule:

```text
Fast lane reduces ceremony, not authority.
```

## Owner

Conductor owns fast-lane routing.

Sentinel owns risk score.

Signal owns fast-lane signal.

Steward may stop fast-lane movement when proof, meaning, refusal, governance, or durable law is at stake.

## Operator-Facing Action

the operator asks for work to continue, proceed, clean up, draft, update, generate, summarize, index, or improve an internal the OS artifact.

the operator does not need to classify whether the work is fast-lane eligible.

## System Action

the OS MUST classify fast-lane eligibility before execution when a request appears low-risk, reversible, and internal.

the OS MUST use the normal routing path when any eligibility test fails.

Fast lane MUST be treated as a post-classification execution lane. It is not an intake lane, not a build methodology, and not permission to skip governance.

Fail-closed rule:

```text
If fast-lane eligibility is uncertain, fast lane is unavailable.
```

Governance rule:

```text
Fast lane may skip ceremony only after source, destination, reversibility, authority boundary, risk, stop condition, and verification are already clear.
```

Deterministic gate:

- `_routing/atx_fast_lane_gate.py`
- `_routing/atx_hook_runner.py --event fast-lane-check`

## Eligibility

Fast lane MAY be used only when all of these are true:

- The work is inside the current approved workspace.
- The destination is clear from root routing, nearby files, source maps, or existing indexes.
- The source is clear from root routing, nearby files, source maps, or existing indexes.
- The action is reversible by ordinary file edit or regeneration.
- The action is internal-facing.
- The action crosses no more than one authority boundary.
- Existing contracts, standards, indexes, or source maps define the exact action and acceptance test.
- The action does not change Operator Canon, Steward oath, approval standards, refusal authority, live-system permissions, client commitments, legal/compliance posture, financial commitments, or public claims.
- The action does not activate a dormant or undecided project.
- The action does not create or retire a named role.
- The action does not touch credentials, secrets, live systems, external accounts, third-party writes, or production deployments.
- The action preserves existing user edits.
- New claims are source-confirmed, user-confirmed, or explicitly labeled inferred/provisional.
- Sentinel risk score is `0` or `1`.

## Approved Fast-Lane Classes

Fast lane MAY be used for these classes when every eligibility condition also passes:

- Internal typo, formatting, or link-target cleanup.
- Internal index or pointer updates when the source file already exists and the destination is obvious.
- Regenerating a generated artifact from its named source map.
- Running validation, parse, build, lint, or smoke-test commands.
- Creating a small internal draft or summary that is clearly labeled draft and does not become source truth.
- Moving or classifying a non-sensitive file into an already-approved folder.
- Updating a routine log when the event has already happened and the source is clear.

## Blocked Fast-Lane Classes

Fast lane MUST NOT be used for:

- Root law, Operator Canon, Steward, approval, refusal, governance, doctrine, or role-authority changes.
- Project activation, project status decisions, dormant/placeholder movement, or role creation/retirement.
- Public-facing, client-facing, legal/compliance, financial, health, regulated, or reputation-sensitive claims.
- GitHub push, Cloudflare, DNS, CRM, GHL, forms, booking, analytics, deployment, external-account, credential, or live-system movement.
- New durable memory from inference.
- Any task where source, destination, scope, authority boundary, approval state, or reversibility is unclear.

## MUST

- the OS MUST name the source, destination, risk score, reversibility, and stop condition before fast-lane execution.
- the OS MUST produce or mentally satisfy the fast-lane signal before execution; substantial fast-lane passes SHOULD use `_routing/atx_fast_lane_gate.py`.
- the OS MUST keep edits scoped to the smallest file set that resolves the current request.
- the OS MUST regenerate output only from its named source file when a generated artifact is involved.
- the OS MUST verify syntax, source parseability, or generated-output presence when a practical verification command exists.
- the OS MUST preserve user edits and unrelated dirty work.
- the OS MUST report that fast lane was used in the final summary for substantial passes.

## MUST NOT

- the OS MUST NOT use fast lane for live-system, credential, legal/compliance, financial, public, client-facing, or irreversible action.
- the OS MUST NOT use fast lane to write durable root law from inference.
- the OS MUST NOT use fast lane to skip Steward when proof, meaning, oath, refusal, doctrine, brand, or governance authority is being changed.
- the OS MUST NOT use fast lane when project or client scope is unclear.
- the OS MUST NOT use fast lane to create, retire, or materially redefine a named role.
- the OS MUST NOT treat a regenerated output as source truth.
- the OS MUST NOT let deterministic scripts claim to judge truth, meaning, business risk, or approval. Scripts validate declared eligibility only.

## Inputs

This standard accepts:

- The user request.
- Current workspace and destination path.
- Relevant root routing, memory, approval, and source-map files.
- Existing dirty-worktree state.
- Sentinel risk score.
- Declared source, reversibility, stop condition, verification, and authority-boundary state.

## Outputs

Fast-lane signal:

```text
Fast lane:
- Eligible: [yes | no]
- Source:
- Destination:
- Risk: [0 | 1]
- Authority boundary count: [0 | 1]
- Reversible: [yes | no]
- Stop condition:
- Verification:
- Blockers:
- Next action:
```

If not eligible, route through the normal the OS sequence:

```text
Intake
-> memory check when relevant
-> build-time review when triggered
-> risk score
-> signal packet
-> route / output / handoff
```

## Acceptance Test

This standard passes when:

- Eligibility is checked before execution.
- Every eligibility condition is true.
- Risk is `0` or `1`.
- Source and destination are named.
- The edit is reversible and internal-facing.
- The action crosses no more than one authority boundary.
- The exact action and acceptance test already exist in a contract, source map, index, or nearby source file.
- Verification is run or the missing verification reason is named.
- The final summary identifies the files changed and whether fast lane was used.

## Failure Test

This standard fails when:

- A full-review action moves through fast lane.
- A live-system, credential, client-facing, public, legal/compliance, financial, or irreversible action moves through fast lane.
- A dormant or undecided project is activated through fast lane.
- A generated artifact is hand-edited instead of regenerated from its source.
- A provisional inference is written as durable root law.
- A deterministic script is treated as truth, meaning, risk, or approval judgment.
- the operator is asked to classify fast-lane eligibility before the OS inspects the request.

## Escalation

Escalate to Steward when proof, oath, meaning, refusal, governance, doctrine, or external-facing truth is affected.

Escalate to Warden when the work touches live systems, credentials, access, permissions, external accounts, or do-not-touch zones.

Escalate to the operator when the action requires business judgment, moral judgment, client commitment, project activation, role creation/retirement, public claims, legal/compliance risk, financial risk, or risk score `2` or higher.
