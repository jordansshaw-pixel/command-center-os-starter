# Deterministic Contract Language Standard


Status: Root routing standard draft
Date: 2026-06-06

## Purpose

This standard prevents the OS contracts from relying on loose language that creates interpretation drift.

Short rule:

```text
If a behavior must happen, write it as a testable MUST.
```

## Why This Exists

The first intake build used helpful-sounding language but still forced the operator to choose between `references/` and `artifacts/`.

That violated the Operator Load truth:

```text
Do not turn the operator into the classifier.
```

The failure was not only folder placement. The contract language allowed the system to satisfy the appearance of the rule while violating the operator experience.

## Contract Language Levels

Use these words deliberately:

| Word | Meaning |
|---|---|
| MUST | Required behavior. Failing this fails the contract. |
| MUST NOT | Forbidden behavior. Doing this fails the contract. |
| SHOULD | Strong default with allowed exceptions named in the contract. |
| MAY | Optional behavior. Not required for pass. |
| DEFAULT | The action the OS takes unless a stop condition or stronger rule applies. |
| STOP | Movement halts until the named condition is resolved. |

Do not use `should`, `can`, `when useful`, `as needed`, `if obvious`, or `appropriate` for required behavior unless the contract also defines the test that makes the phrase decidable.

## Required Contract Fields

Every durable the OS operating contract, standard, intake lane, routing rule, or stage contract MUST define:

- Owner: the role or source responsible.
- Operator-facing action: the exact action the operator takes, if any.
- System action: the exact action the OS takes.
- MUST rules: required behavior.
- MUST NOT rules: forbidden interpretations.
- Inputs: what the contract accepts.
- Outputs: what the contract produces.
- Acceptance test: how the contract passes.
- Failure test: how the contract fails.
- Escalation: who receives the stop, review, or decision packet.

If any required field is absent, the contract is provisional and MUST NOT be treated as complete.

## Operator-Facing Contract Rule

Any operator-facing workflow MUST expose one primary default action unless a real approval decision is required.

It MUST NOT ask the operator to:

- Classify routine file placement.
- Choose between internal taxonomy buckets.
- Infer which agent should receive the work.
- Decide whether something is source, output, reference, artifact, evidence, project, or stage before the OS inspects it.

If classification is required, the OS MUST classify first and ask only for approval or override when needed.

## Intake-Specific Rule

The operator-facing intake action is:

```text
Put the file in `_intake/drop/`.
```

`references`, `artifacts`, `source`, `output`, `project`, `stage`, and similar labels are internal classification outcomes. They MUST NOT be presented as required operator choices at intake.

## Determinism Test

Before finalizing a contract or folder lane, test:

```text
Determinism test:
- Operator action is singular:
- Required behavior uses MUST/MUST NOT:
- Forbidden interpretation named:
- Owner named:
- Acceptance test named:
- Failure test named:
- Escalation path named:
- Operator-load failure checked:
- Result: [pass | fail]
```

Fail when:

- A user must classify the work before the system has inspected it.
- A required behavior is written as a vague preference.
- Two plausible interpretations are allowed without a deciding test.
- The acceptance test verifies file existence but not operator experience.

## Review Owner

Librarian owns findability and classification language.

Conductor owns routing determinism.

Sentinel scores interpretation drift as operator-load risk.

Steward may halt durable rules that appear aligned but allow false movement.
