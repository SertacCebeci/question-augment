---
description: "A four-check evidence gate (scope, source, time, contradiction) authorizing PROCEED, REOBSERVE, ABSTAIN or ESCALATE; cut unsafe proceeds from 20-40% to 0% on two robot benchmarks."
aliases: ["Conflict-Aware Belief Gate", "CoreSense belief gate", "conflict-aware belief gating"]
sources: ["li-2026-coresense"]
---
# Conflict-aware belief gate

> Before a robot acts on recalled or observed evidence, a deterministic gate
> checks the evidence itself — not just what it says — and returns one of
> four bounded moves rather than a single proceed/refuse split.

## Definition / Mechanism

Li (2026) defines each piece of evidence as a claim
$b_j=(c_j,v_j,s_j,t_j,\sigma_j,w_j,\pi_j)$ (predicate, value, source, time,
scope, support weight, provenance pointer) and the gate as a function
$d=G(q,a,B)$ over the active claim set $B$: "where P , R, A, and E denote
P ROCEED, R EOBSERVE, A BSTAIN, and E SCALATE."[^c1]

The gate does not score the whole set at once. "The Conflict-Aware Belief
Gate constructs an active claim set from current observations, retrieved
episodes, and derived candidate claims. It applies four checks in order:
(1) scope compatibility, (2) source precedence, (3) temporal validity, and
(4) contradiction/support."[^c2]

Each check can end the sequence early, and what each one licenses is fixed:
"Current authoritative observations can resolve older disagreement; a
derived claim cannot silently override conflicting direct or historical
evidence. Stale or incomplete evidence requests re-observation. Unresolved
high-impact conflict abstains or escalates. Only a supported, conflict-free
candidate proceeds."[^c3]

Measured against M0–M3 (stateless, recency/keyword, vector-similarity and
structured retrieval without gating, all sharing M4's retrieved set): "Table
I shows that M0–M3 all permit the ten CableTrace queries whose protocol
targets require withholding action, giving a 20% unsafe-proceed rate under
the evaluation definition. M4 gates all ten while preserving proceed
decisions for every nominal query."[^c4]

On the second benchmark: "On BotFails-200, M3 has 40% protocol-defined
unsafe proceeds and 20% nominal overblocking. M4 resolves the authoritative
nominal observations, exposes all fixed conflicts, and withholds every such
proceed, yielding 24 M4-only corrections and no M3-only corrections (p =
1.19 × 10−7 )."[^c5]

## Known as

| Name | Field | Relation |
|---|---|---|
| Conflict-Aware Belief Gate | the paper's own term (title case) | exact — same object |
| CoreSense belief gate | this wiki, tied to the system name | exact — the gate component of CoreSense |
| conflict-aware belief gating | the paper's title, gerund form | exact — same mechanism |

## Why it matters

This is a rule-based, deterministic instance of the bounded-decision pattern
[[pre-action-authorization-decision]] finds empirically in an LLM-prompted
setting: both replace a binary act/refuse split with several named moves.
The difference is where the moves come from — here the four-way decision is
produced by ordered checks over a typed evidence representation with
explicit provenance, not by prompting a model to classify a scenario. That
lets the paper show *why* a move was made (which check failed) rather than
only *what* was decided, and lets gating be evaluated against ungated
retrieval on the same input (M3 vs M4) rather than only against a
hand-authored reference decision.

## Transfer

| | |
|---|---|
| **Home field** | robot-system integration / auditable decision architectures |
| **Here** | an answerer that must decide, before committing an answer or action, whether the evidence behind it is current, from an authoritative source, and free of unresolved contradiction |
| **What survives** | the refusal to convert "evidence exists and is similar" into "evidence authorizes commitment" — a fixed check order (scope, source, time, contradiction) where any one failing point routes to a weaker commitment (reobserve/abstain/escalate) rather than to silent proceeding |
| **What does not** | the specific four checks and their robot-domain content (task/entity scope, sensor provenance, physical staleness) — a non-robotic answerer would need its own definition of "authoritative source" and "contradiction," which the paper does not supply outside robotics |

## Limits

- Single-author paper (an AWS hackathon project); the same author designed
  the gate rules and the benchmarks that evaluate them — the paper itself
  names this "experimenter bias" as a threat to validity.
- CableTrace-120 is a constructed, sanitized benchmark (60 queries, not
  independent physical trials) and BotFails-200 evaluation uses only labels
  and metadata, not raw sensor streams; the 20%→0% and 40%→0% reductions are
  validations of the implemented rules on frozen protocols, not general
  failure-detection accuracy.
- On the one raw-perception stress test (BotFails-Raw-40), the gate reaches
  0% unsafe proceed only by overblocking 100% of nominal episodes — the
  paper's own reading is that self-reported model confidence is not yet a
  useful authorization signal, so the headline reduction does not transfer
  unchanged to noisier evidence.
- No experiment measures executed [[recovery-postulate|recovery]] success or full cloud/offline
  equivalence; the claim is limited to an auditable integration pattern, not
  autonomous recovery or certified safety.

## Related

[[pre-action-authorization-decision]] · [[robot-response-mode-taxonomy]] · [[value-of-information]] · [[abstention]]

[^c1]: li-2026-coresense — "where P , R, A, and E denote P ROCEED, R EOBSERVE, A BSTAIN, and E SCALATE."
[^c2]: li-2026-coresense — "The Conflict-Aware Belief Gate constructs an active claim set from current observations, retrieved episodes, and derived candidate claims. It applies four checks in order: (1) scope compatibility, (2) source precedence, (3) temporal validity, and (4) contradiction/support."
[^c3]: li-2026-coresense — "Current authoritative observations can resolve older disagreement; a derived claim cannot silently override conflicting direct or historical evidence. Stale or incomplete evidence requests re-observation. Unresolved high-impact conflict abstains or escalates. Only a supported, conflict-free candidate proceeds."
[^c4]: li-2026-coresense — "Table I shows that M0–M3 all permit the ten CableTrace queries whose protocol targets require withholding action, giving a 20% unsafe-proceed rate under the evaluation definition. M4 gates all ten while preserving proceed decisions for every nominal query."
[^c5]: li-2026-coresense — "On BotFails-200, M3 has 40% protocol-defined unsafe proceeds and 20% nominal overblocking. M4 resolves the authoritative nominal observations, exposes all fixed conflicts, and withholds every such proceed, yielding 24 M4-only corrections and no M3-only corrections (p = 1.19 × 10−7 )."
