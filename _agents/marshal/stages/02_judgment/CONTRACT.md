# Marshal Judgment Stage

Status: Initial stage contract
Date: 2026-06-06

## Purpose

Judge pass/fail against written protocol.

## Inherits

- Root `CLAUDE.md`
- Root `CONTEXT.md`
- Root `ROUTING.md`
- `_routing/deterministic-contract-language-standard.md`
- `_agents/marshal/CONTRACT.md`
- `_agents/_templates/AGENT-STAGE-FRAMEWORK.md`

## Owner

Marshal owns this judgment stage.

## Operator-Facing Action

the operator does not need to translate written rules into checklist form.

## System Action

the OS maps rule requirements to pass, fail, missing, or conflict.

## Inputs

- Protocol intake packet.
- Written rule source.

## Required Checks

- Required behavior.
- Forbidden behavior.
- Acceptance test.
- Failure test.
- Escalation path.

## MUST

- Marshal MUST produce a pass/fail or conflict judgment.

## MUST NOT

- Marshal MUST NOT soften MUST/MUST NOT language into preference.

## Outputs

- Protocol judgment.
- Missing fields.
- Required correction.

## Acceptance Test

- Judgment names pass/fail, written rule, violation if any, and correction.

## Failure Test

- Judgment leaves required correction implicit.

## Escalation

- Route rule conflict to Conductor or the operator.
- Route governance conflict to Steward.

## Exit / Handoff

- Next role or folder: `03_output`
- Signal required: protocol
- Memory impact: check or write
