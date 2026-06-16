# Role Glossary

Command Center OS ships with a crew of functional agent roles. Each role has a folder under
`_agents/<role>/` with a `CONTRACT.md`, a `doctrine/` file, and a four-stage spine
(`01_intake → 02_judgment → 03_output → 04_handoff`).

## Authority Roles

| Role | Function |
|---|---|
| **Steward** | Truth, proof, refusal, correction, brand/governance authority. |
| **Conductor** | Routing, sequence, handoff, operating discipline (chief of staff). |
| **Keeper** | Memory relevance and continuity. |
| **Recorder** | Exact record and source trace. |
| **Librarian** | Index and findability. |
| **Sentinel** | Risk scoring — the mandatory gate; fires on all non-trivial work. |
| **Warden** | Hard boundaries, live-system and credential protection. |
| **Voice** | Tone, cadence, culture translation. |

## Specialist Roles

| Role | Function |
|---|---|
| **Analyst** | Evidence architecture, source confidence, research clarity. |
| **Pathfinder** | Boundary architecture, safe-movement envelopes. |
| **Theorist** | Model coherence, abstraction risk. |
| **Builder** | Build, prototype, tooling, automation, implementation. |
| **Mechanic** | Repair, diagnosis, failure analysis. |
| **Marshal** | Protocol, rules-as-written enforcement, checklist compliance. |
| **Liaison** | Human/client intake, close-to-ground context. |
| **Scout** | Field context, terrain, reconnaissance. |
| **Signal** | Signal packets and communication state (service role; no stop/truth authority). |

## Rename the Crew (optional)

These functional names are the default. To re-theme the crew as your own:

1. Rename the folders under `_agents/` (e.g. `_agents/steward/` → `_agents/<yourname>/`).
2. Find/replace the role name across `_agents/`, `_routing/runtime/`, `_memory/runtime/`,
   `_agents/ROLE-INDEX.md`, `_agents/ROLE-STATUS.json`, `_agents/ROLE-INVOCATION-MATRIX.md`, and
   `_routing/atx_multi_agent_gate.py` (its role roster must match `ROLE-STATUS.json`).
3. Run `python _routing/run_gates.py` — the registry-validation gate confirms names stay consistent.

## On the `atx` Namespace

The engine keeps a short internal namespace on its code and CI files (`_routing/atx_*.py`,
`.github/workflows/atx-gates.yml`, `ATX_*` shell vars). It is just a 3-letter prefix, not a brand or
personal data. Rename it only if you want to — it is not required, and the gates do not depend on the
product name.
