# Agent Test Standard


Status: Root operating standard draft
Date: 2026-06-05

## Purpose

This standard defines how the OS tests an agent pass before treating it as finished, handoff-ready, or safe to log.

Short rule:

```text
An agent pass is not tested until scope, sources, risk, output, and next movement have all been checked.
```

## What Counts As A Test

the OS tests are not limited to code execution.

For markdown, routing, governance, memory, and agent-structure work, a valid test can be:

- Source-load verification.
- Scope verification.
- Cross-reference verification.
- Risk and signal verification.
- Contract or stage compliance review.
- Deterministic contract language review.
- File placement and findability review.
- Handoff readiness review.
- Memory write review.
- Render, syntax, command, or tool execution when the artifact requires it.

The test must name what was checked and what passed, failed, or remains unverified.

## Minimum Test Packet

Use this packet before finalizing substantial agent work:

```text
Test:
- Scope checked:
- Required sources loaded:
- Destination checked:
- Risk checked:
- Signal checked:
- Output checked:
- Human interface source checked:
- Cross-references checked:
- Memory checked:
- Handoff checked:
- Deterministic contract checked:
- Result: [pass | pass-with-caveat | fail | not-run]
- Caveat:
```

## Required Checks

### 1. Scope Check

Confirm:

- The likely workspace or folder in scope.
- Whether work is root, project, stage, agent, memory, governance, connectivity, build, review, or cleanup.
- Whether related files were intentionally included or left for a later approval.

Fail when:

- The destination is ambiguous and the pass would create durable confusion.
- A related folder is silently included without routing reason or approval.

### 2. Source Load Check

For substantial root agent work, check the relevant root files:

- `CLAUDE.md`
- `AGENTS.md`
- `CONTEXT.md`
- `ROUTING.md`
- `_routing/router-contract.md`
- `_routing/destination-map.md`
- `_operator/` when operator truth, voice, judgment, load, approval, or cross-project truth scope matters.
- `_governance/steward.md` when durable law, proof, refusal, brand, governance, or agent behavior is involved.
- `_memory/MEMORY-ROUTER.md` and `_memory/decision-source-index.md` when prior decisions or durable memory may matter.
- `_agents/ROLE-INDEX.md` when role routing or agent files are involved.
- `_agents/ROLE-STATUS.json` when assigning, invoking, displaying, or validating a role or role-like lens.
- `_handoffs/README.md` when work may continue or move.

Fail when:

- Required local instructions are skipped.
- A decision is treated as open before checking likely decision sources.

### 3. Destination Check

Confirm the output belongs in the selected folder.

Default destinations:

| Work Type | Test Destination |
|---|---|
| Agent standards and audit behavior | `_agents/` |
| Role contracts and stages | `_agents/[role]/` |
| Routing rules | `ROUTING.md` or `_routing/` |
| Operator truth, voice, judgment, load, and approval standards | `_operator/` |
| Memory and decisions | `_memory/` |
| Handoffs | `_handoffs/` |
| Connectivity and live-system boundaries | `_connectivity/` |
| Project-local behavior | `[PROJECT]/` |

Fail when:

- The artifact duplicates source law instead of pointing to it.
- A root rule is buried in a project or working-output folder.

### 3A. Deterministic Contract Check

Use `_routing/deterministic-contract-language-standard.md` when a pass creates or changes contracts, standards, routing rules, folder lanes, operator-facing workflows, or agent-stage behavior.

Confirm:

- Required behavior uses `MUST` or `MUST NOT`.
- Operator-facing action is singular unless a real approval decision is required.
- Forbidden interpretations are named.
- Owner is named.
- Acceptance test is named.
- Failure test is named.
- Escalation path is named.
- Operator-load failure is checked.

Fail when:

- The user must classify work before the OS inspects it.
- A required behavior is written only as `should`, `may`, `when useful`, `as needed`, or `if obvious`.
- The test verifies that a file exists but not whether the operator-facing workflow reduced load.
- Two plausible interpretations remain without a deciding rule.

### 4. Risk Check

Use `_agents/sentinel/RISK-STANDARD.md`.

At minimum, name:

- Score.
- Level.
- Main failure mode.
- Required review gate.

Fail when:

- Risk is omitted for substantial work.
- Risk 3 or 4 work moves without the required Steward, Warden, or the operator review.
- Live-system, credential, legal, financial, public, or client exposure is treated as routine.

### 5. Signal Check

Use `_agents/signal/SIGNAL-STANDARD.md` when work is non-trivial, risky, corrective, or moving between roles/sessions.

Confirm:

- Active agent.
- Active stage.
- Source.
- Audience.
- Workspace.
- Risk.
- Status.
- Next action.
- Memory impact.
- Handoff needed.

Fail when:

- The next owner or status is implicit.
- Work moves without a clear audience.

### 6. Output Check

Confirm:

- The requested artifact exists.
- The file uses the repo's style and naming pattern.
- The file is readable markdown.
- The content is scoped to the request.
- No unrelated files were changed.

For code, spreadsheet, document, deck, browser, or visual work, use the relevant artifact-specific verification in addition to this standard.

Fail when:

- The artifact is missing, malformed, or unreviewed.
- The output creates a new rule that conflicts with root law.

### 7. Cross-Reference Check

Confirm references point to existing files or explicitly mark future files.

Fail when:

- A standard points to a missing file as if it exists.
- A role, stage, or folder is named differently from the actual path.

### 8. Human Interface Truth Check

Use this check for diagrams, dashboards, HTML schematics, maps, visual control surfaces, and any artifact intended to shape human understanding of the OS.

Confirm:

- The interface names its source of truth.
- The interface names its generator, update command, or manual update rule.
- The interface distinguishes source law from Layer 4 review output.
- The interface can be updated when wiring changes.
- The source of truth is stored in the correct Layer 3 location.

Fail when:

- A human-facing architecture artifact is only hand-maintained output.
- A diagram presents current state but has no update path.
- A visual interface can drift from root truth without detection.

### 9. Memory Check

Use `_memory/MEMORY-ROUTER.md`.

Confirm whether the pass creates:

- Decision.
- Correction.
- Finding.
- Rule.
- Handoff.
- Open loop.
- Source improvement.

Fail when:

- Durable findings remain only in chat.
- Inference is written as user-confirmed law.

### 10. Handoff Check

Use `_handoffs/README.md` when work continues, changes owners, or depends on future context.

Confirm:

- What remains open.
- Which role owns the next pass.
- Whether the handoff log or a packet should be updated.

Fail when:

- A substantial unfinished pass ends with no next owner.
- The next session would need to reconstruct the state from chat.

## Result Labels

| Result | Meaning |
|---|---|
| pass | Required checks completed and no blocking caveat remains. |
| pass-with-caveat | Checks completed but a named non-blocking gap remains. |
| fail | A blocking issue remains. |
| not-run | Check was not run; explain why. |

## Standard Completion Test

Before finalizing, answer:

```text
What did we learn?
Where was it saved?
What remains open?
Which role should pick it up next?
```

Then list:

- Files reviewed.
- Files changed.
- Tests run.

If the work is substantial and should be auditable later, add or update `_agents/AGENT-RUN-LOG.md`.
