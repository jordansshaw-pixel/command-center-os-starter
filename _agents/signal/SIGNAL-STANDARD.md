# Signal Standard

Status: Specialist operating standard
Date: 2026-06-05

## Purpose

This standard makes the OS communication routable.

Signal does not decide truth, risk, or final routing. Signal makes sure the signal carries enough structure that Conductor, the next role, and the next session know what happened and what must happen next.

Short rule:

```text
If work moves, the signal must name active agent, active stage, source, audience, risk, status, reason, next action, and memory impact.
```

## Outcome Impact

Signal improves outcomes by preventing:

- Vague handoffs.
- Lost risk judgments.
- Hidden stop conditions.
- Repeated context reconstruction.
- Corrections disappearing into chat.
- Routing decisions that lack audience, status, or next action.
- Memory writes without a clear destination.

When Signal is missing, the OS tends to:

- Know something but fail to transmit it.
- Leave Conductor to infer state.
- Leave the next role without enough context.
- Ask the operator broad questions instead of presenting a precise packet.

## Base Signal Packet

Use this packet for substantial routing, risk, review, correction, stop, and handoff movement:

```text
Signal:
- Type: [intake | memory-check | routing | risk | review | build | handoff | correction | stop | escalation]
- Active agent: [role currently running]
- Active stage: [01_intake | 02_judgment | 03_output | 04_handoff | none]
- Source: [role]
- Audience: [role or the operator]
- Workspace: [root | project | stage | file/folder]
- Risk: [0-4]
- Status: [proceed | hold | review | stop | needs-evidence | needs-memory | needs-approval | ready | complete]
- Reason: [one concise reason]
- Next action: [specific next move]
- Memory impact: [none | check | write | update-source]
- Handoff needed: [yes | no]
```

## Signal Types

### Intake Signal

Use when a request first enters the workflow.

```text
Signal:
- Type: intake
- Active agent:
- Active stage:
- Source: the operator or session agent
- Audience: Conductor
- Workspace:
- Risk:
- Status:
- Reason:
- Next action:
- Memory impact:
- Handoff needed:
```

### Routing Signal

Use when Conductor assigns destination or role.

```text
Signal:
- Type: routing
- Active agent: Conductor
- Active stage: 03_output
- Source: Conductor
- Audience: [role or folder]
- Workspace:
- Risk:
- Status:
- Reason:
- Next action:
- Memory impact:
- Handoff needed:
```

### Risk Signal

Use when Sentinel has judged risk.

```text
Signal:
- Type: risk
- Active agent: Sentinel
- Active stage: 03_output
- Source: Sentinel
- Audience: Conductor
- Workspace:
- Risk:
- Status:
- Reason:
- Next action:
- Memory impact:
- Handoff needed:
```

Attach or summarize the Sentinel risk output when risk is 2+.

### Review Signal

Use when Steward, source inspection, Mechanic, Warden, Voice, or the operator must review.

```text
Signal:
- Type: review
- Active agent:
- Active stage:
- Source: Conductor or Sentinel
- Audience: [review role]
- Workspace:
- Risk:
- Status: review
- Reason:
- Next action:
- Memory impact:
- Handoff needed:
```

### Handoff Signal

Use when work moves to another role, stage, project, or future session.

```text
Signal:
- Type: handoff
- Active agent: [current role]
- Active stage: 04_handoff
- Source: [current role]
- Audience: [receiving role]
- Workspace:
- Risk:
- Status:
- Reason:
- Next action:
- Memory impact:
- Handoff needed: yes
```

For substantial work, create or update a handoff packet in `_handoffs/` or the nearest project/stage handoff folder.

### Correction Signal

Use when a correction changes future behavior or source files.

```text
Signal:
- Type: correction
- Active agent:
- Active stage:
- Source: [role or the operator]
- Audience: Keeper, Recorder, Librarian, and affected owner
- Workspace:
- Risk:
- Status: update-source
- Reason:
- Next action:
- Memory impact: write | update-source
- Handoff needed:
```

### Stop / Escalation Signal

Use when movement must stop.

```text
Signal:
- Type: stop | escalation
- Active agent:
- Active stage:
- Source: Sentinel, Warden, Steward, or Conductor
- Audience: the operator
- Workspace:
- Risk: 4
- Status: stop
- Reason:
- Next action:
- Memory impact:
- Handoff needed:
```

## Communication Rules

- One signal should carry one main movement.
- Always include the active agent and active stage so the runner state can be surfaced in logs, UI, handoffs, and final summaries.
- Do not hide uncertainty in polished prose.
- If risk is 2+, include Sentinel's score or reason.
- If truth/proof is involved, name whether Steward is required.
- If live-system risk exists, name Warden and the operator approval.
- If the work continues later, create a handoff packet or update the handoff log.
- If a decision was made, route memory to Keeper/Recorder/Librarian.

## Complete Loop

The default orchestrated workflow is:

```text
Intake signal
-> Conductor classifies scope
-> Keeper memory check when relevant
-> Sentinel risk score
-> Signal risk/routing signal
-> Conductor routes to role/folder
-> Execution or stop
-> Review gate
-> Signal handoff/correction signal
-> Memory write or source update
-> Next owner
```

## Test Scenarios

### Low-Risk Internal Edit

```text
Signal:
- Type: routing
- Active agent: Conductor
- Active stage: 03_output
- Source: Conductor
- Audience: nearest scoped file
- Workspace: root
- Risk: 1
- Status: proceed
- Reason: Internal reversible edit.
- Next action: Edit scoped file and verify.
- Memory impact: none
- Handoff needed: no
```

### Governance Change

```text
Signal:
- Type: review
- Active agent: Sentinel
- Active stage: 03_output
- Source: Sentinel
- Audience: Steward
- Workspace: _governance/
- Risk: 3
- Status: review
- Reason: Durable law changes future agent behavior.
- Next action: Steward review before finalizing.
- Memory impact: write
- Handoff needed: yes
```

### Live-System Risk

```text
Signal:
- Type: stop
- Active agent: Warden
- Active stage: 03_output
- Source: Warden
- Audience: the operator
- Workspace: live system
- Risk: 4
- Status: stop
- Reason: Action may affect production or credentials.
- Next action: Require explicit approval and scoped plan.
- Memory impact: check
- Handoff needed: yes
```
