---
description: "An LLM-agent architecture that uses idle time between user turns to predict likely future needs and pre-acquire evidence for them before being asked."
aliases: ["idle-time proactive agent architecture"]
sources: ["hu-2026-anticipate"]
---
# ProAct architecture

> Between user turns, a proactive agent predicts what the user will
> probably ask next from dialogue history and persistent memory, spends
> idle-time compute resolving the knowledge gaps those predicted needs
> imply, and only then decides whether to push, queue, or silently store
> what it found.

## Definition / Mechanism

Hu, Lyu, Kong et al. (2026) define ProAct as "a
proactive agent architecture that leverages idle-time compute to
anticipate and fulfill likely upcoming user needs. By analyzing evolving
dialogue history together with persistent memory, ProAct predicts
upcoming needs and iteratively acquires information, allowing the agent
to resolve knowledge gaps and prepare evidence before the user initiates
a query."[^c1]

The loop is $(H_t, M_t) \to Z_t \to S(z) \to A_z \to d_z \to M_{t+1}$:
after a foreground turn, Future-State Prediction generates a candidate
set of future needs $Z_t$ from the dialogue history $H_t$ and persistent
memory $M_t$; Idle-Time Acquisition scores and filters those candidates
(see [[idle-time-acquisition-value-score]]), retrieves or decomposes into
sub-questions for the ones it accepts, and produces a grounded artifact
$A_z$; a delivery policy assigns each artifact a mode $d_z \in
\{\text{push}, \text{queue}, \text{store}\}$. Accepted or rejected
candidates and their provenance are written back to memory, closing the
loop for the next idle interval.

On the authors' own 200-scenario, 40-domain ProActEval benchmark, "ProAct
accelerates task completion by reducing required turns by 14.8%,
decreases user effort by 11.7%, and cuts hallucination rates by 28.1% on
ProActEval compared with a reactive baseline."[^c2]

An ablation isolates what is doing the work. An "Undirected Idle"
variant that runs the same background acquisition without Future-State
Prediction "spends 69.8k active tokens per scenario on average" but "only
slightly improves over Reactive, reducing T100 by 0.9% and User Effort by
1.1%," whereas the full, prediction-guided system "reduces T100 by 14.1%
and User Effort by 10.7% relative to Undirected Idle, and achieves an
Anticipation Recall of 0.428 where both other settings remain at 0."[^c3]

Idle-time compute alone barely helps; direction — having a predicted
candidate to search for — is what the measured gain comes from.

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Hu et al. 2026) | ProAct | exact |
| This wiki | idle-time proactive agent architecture | exact — descriptive name for the mechanism |

Not the same object as `ProACT` (capital ACT) in
[[breakdown-aware-proactive-intervention]] (Yang et al. 2026), and the
name is deliberately not registered as an alias here to avoid a
case-insensitive collision with that note's alias: that architecture
diagnoses a labelled collaboration breakdown in a multi-user conversation
before speaking; ProAct here predicts an individual user's future need
and spends idle compute preparing an answer to it in advance.

## Why it matters

Every criterion on this stall's map ([[mutual-information|mutual information]], EIG, VoI,
[[adaptive-submodularity|adaptive submodularity]]) scores a candidate question the agent could ask
now. ProAct is a working system whose selection problem is one step
earlier: which future need — of several the agent has itself predicted,
unprompted — is worth investigating during idle time, before there is a
question to score at all. The ablation is the load-bearing result for
that framing: undirected background search is nearly useless without a
predicted candidate to search for.

## Limits

- Reported effects (14.8% / 11.7% / 28.1%) are all measured on the
  authors' own ProActEval benchmark, built and validated by the same team
  that built ProAct; no independent replication is cited.
- The benchmark's ground-truth "predictable" needs are annotated by
  construction (a `predictable_after` field authored during scenario
  synthesis), not discovered — so the measured Anticipation Recall (0.428)
  is bounded by how predictable the authors chose to make their own
  scenarios.
- The value score and thresholds ($\theta_{\mathrm{conf}}$,
  $\theta_{\mathrm{val}}$, the weights $w_r, w_g, w_v, w_\tau$) are not
  given fixed values in the excerpt read; how they were set or tuned is
  not established here.

## Related

[[idle-time-acquisition-value-score]] · [[breakdown-aware-proactive-intervention]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: hu-2026-anticipate — "a proactive agent architecture that leverages idle-time compute to anticipate and fulfill likely upcoming user needs. By analyzing evolving dialogue history together with persistent memory, ProAct predicts upcoming needs and iteratively acquires information, allowing the agent to resolve knowledge gaps and prepare evidence before the user initiates a query."
[^c2]: hu-2026-anticipate — "ProAct accelerates task completion by reducing required turns by 14.8%, decreases user effort by 11.7%, and cuts hallucination rates by 28.1% on ProActEval compared with a reactive baseline."
[^c3]: hu-2026-anticipate
