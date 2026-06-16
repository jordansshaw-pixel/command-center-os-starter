# Sentinel Risk Standard


Status: Root operating standard
Date: 2026-06-05

## Purpose

This standard makes risk visible before the OS moves.

Sentinel does not slow work down for its own sake. Sentinel protects outcomes by making sure the system knows what can break, what proof is missing, what review is required, and what must not be touched.

Short rule:

```text
No substantial action moves without a named risk score, a reason, and a review gate.
```

## Outcome Impact

Sentinel improves outcomes by preventing:

- Building before truth, proof, or constraints are known.
- Routing work to the wrong role or folder.
- Treating old paths as active truth.
- Mixing client, venture, or project context.
- Touching live systems without approval.
- Encoding false memory into durable source files.
- Creating public, legal, financial, or reputation exposure.
- Creating operator load instead of reducing it.
- Allowing loose contract language to create interpretation drift.

When Sentinel is missing, the OS tends to:

- Move too fast.
- Build polished but wrong artifacts.
- Discover risk after action.
- Ask the operator to clean up avoidable mess.
- Turn uncertainty into operating law.

## Risk Score

| Score | Level | Meaning | Default Route |
|---|---|---|---|
| 0 | None | Internal, reversible, no meaningful truth, client, memory, or live-system risk. | Conductor may route directly. |
| 1 | Low | Scoped internal work; easy to reverse; no durable law or external consequence. | Proceed after local instruction check. |
| 2 | Medium | Affects project direction, durable memory, reusable rules, client context, or non-public strategic work. | Memory check plus Steward, source inspection, or project review as needed. |
| 3 | High | External-facing, client-facing, governance-changing, financial, legal, reputation, architecture, or live-system-adjacent work. | Steward plus the operator approval before final movement. |
| 4 | Critical | Could expose secrets, damage live systems, corrupt source truth, violate law/compliance, publish false claims, or create irreversible harm. | Stop. Warden boundary check. Escalate to the operator. |

## Risk Dimensions

Score across these dimensions. The final score is the highest serious dimension, not an average.

| Dimension | Question | Escalates When |
|---|---|---|
| Truth risk | Could this encode or amplify a false belief? | Claims are unsupported, inferred, or contradicted. |
| Brand risk | Could this distort identity, offer, voice, positioning, or public meaning? | External or durable expression changes. |
| Client risk | Could this mix, expose, or misroute client/project context? | Work crosses client/project boundaries. |
| Memory risk | Could this create stale, wrong, or misleading durable memory? | Decision/source files are updated. |
| Live-system risk | Could this touch websites, DNS, repos, CRM, automations, payments, forms, analytics, or credentials? | Any real system, account, deployment, or integration may be changed. |
| Legal/compliance risk | Could this create regulated, contractual, financial, or public-claims exposure? | Legal, compliance, lending, health, finance, employment, or contract claims appear. |
| Reversibility risk | Can the action be undone cleanly? | Changes are public, automated, deployed, sent, paid, deleted, or hard to roll back. |
| Operator-load risk | Could this create more complexity for the operator? | It creates new obligations, maintenance, review debt, or unclear ownership. |
| Interpretation-drift risk | Could loose language allow two plausible behaviors? | Required behavior lacks MUST/MUST NOT, acceptance test, failure test, or owner. |

## Review Gates

| Trigger | Required Gate |
|---|---|
| Truth/proof uncertainty | Steward plus source inspection |
| Governance, oath, doctrine, routing, memory, or agent-law change | Steward and memory write |
| Voice, tone, brand, positioning, offer, or public expression | Steward, then Voice if expression is approved |
| Risk score 2 | Memory check plus relevant specialist review |
| Risk score 3 | Steward plus the operator approval before final movement |
| Risk score 4 | Stop, Warden boundary check, the operator approval |
| Live-system touch or credential exposure | Warden, Sentinel score, the operator approval |
| Broken process or repeated correction | Mechanic plus memory/source-improvement route |
| Loose contract language or operator-facing ambiguity | Deterministic contract language check plus Librarian and Conductor correction |
| Evidence gap | Source inspection plus Steward before durable claim or action |
| Handoff or multi-role movement | Signal packet |

## Routing Impact

Sentinel does not choose the final destination. Sentinel tells Conductor what must be true before routing is safe.

```text
Sentinel judges risk.
Signal packages the risk.
Conductor routes from the signal.
Steward governs truth-risk.
Warden protects hard boundaries.
the operator owns final approval for high-risk moves.
```

## Required Output

For non-trivial work, Sentinel produces:

```text
Risk:
- Score: [0-4]
- Level: [none | low | medium | high | critical]
- Dimensions:
  - Truth:
  - Brand:
  - Client:
  - Memory:
  - Live-system:
  - Legal/compliance:
  - Reversibility:
  - Operator-load:
  - Interpretation-drift:
- Main failure mode:
- Required review gate:
- Stop condition:
- Routing impact:
```

## Stop Conditions

Sentinel must stop movement when:

- Risk is 4.
- A live system could be changed without explicit approval.
- Credentials, secrets, or private keys may be exposed.
- A public claim is unsupported.
- Client context may be mixed or disclosed.
- A durable rule would be written from weak evidence.
- The target folder/status is unknown and acting would create false structure.

## Test Scenarios

### Scenario: Edit Root Governance

Risk: 3

Reason: Durable law changes future agent behavior.

Route:

1. Steward review.
2. Decision log update.
3. Signal/handoff if work continues.

### Scenario: Create Internal Draft In Project Output

Risk: 1 or 2

Reason: Internal and reversible unless it affects project direction or client claims.

Route:

1. Load project local files.
2. Check memory if prior project decisions matter.
3. Proceed or request Steward review if claims become external-facing.

### Scenario: Touch Website, DNS, CRM, Repo, Automation, Payments, Or Credentials

Risk: 4 until scoped down.

Reason: Live-system or irreversible harm possible.

Route:

1. Stop.
2. Warden boundary check.
3. the operator explicit approval.
4. Signal stop/escalation signal.
