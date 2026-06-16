# Marshal Output Stage


Status: Initial stage contract
Date: 2026-06-06

## Purpose

Produce protocol compliance output.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/marshal/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Marshal owns this output stage.

## Operator-Facing Action

the operator receives a clear pass/fail protocol packet.

## System Action

the OS produces protocol output with rule, status, violation, correction, escalation, and next owner.

## Inputs

- Protocol judgment.

## Required Checks

- Is a correction required?
- Is a stop required?
- Who owns the next action?

## MUST

- Marshal MUST name required correction and next owner.

## MUST NOT

- Marshal MUST NOT output only criticism.

## Outputs

```text
Protocol packet:
- Rule source:
- Action checked:
- Status:
- Violation:
- Required correction:
- Escalation:
- Next owner:
```

## Acceptance Test

- Output is actionable without re-reading the whole rule source.

## Failure Test

- Output lacks status or correction.

## Escalation

- Route stop/conflict to Conductor, Steward, or the operator as needed.

## Exit / Handoff

- Next role or folder: `04_handoff`
- Signal required: protocol or handoff
- Memory impact: none, check, write, or update-source
