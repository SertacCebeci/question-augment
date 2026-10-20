---
description: "An online method that decides whether a proactive assistant should interact now or stay silent, learning purely from sparse binary feedback without retraining an LLM."
aliases: ["EOPA", "evidence-driven online preference adaptation"]
sources: ["wang-2026-preference"]
---
# Evidence-driven online preference adaptation

> A proactive assistant's "ask now or wait" decision, made from two running
> tallies of past interaction/silence outcomes instead of a value function
> or a retrained model.

## Definition / Mechanism

Wang et al. (2026) address a proactive assistant
that polls a user's state (time, activity) and at each step must decide
interact-or-silence, when interaction-worthy moments are sparse (1.129% of
polling steps in their benchmark) and scattered across fine-grained states,
so per-state feedback is too thin for direct supervised learning.[^c1]

EOPA keeps two evidence carriers updated from binary feedback: **temporal
preference anchors**, indexed by time-of-day interval and by how many
polling steps have elapsed within the current activity (so a later stage of
the same activity carries its own tally), and **evidence-bearing activity
prototypes**, semantic clusters of open-ended activity descriptions that
each also carry interaction/silence counts. At each step both carriers
convert their matched counts into a probability of interaction-appropriateness
via a Beta-Binomial (Jeffreys-smoothed) estimate, then divide that estimate
by its own posterior standard deviation — "the resulting evidence score
tends to be larger when the temporal condition favors interaction and
receives stronger support from accumulated feedback" — so a confident,
well-observed anchor counts for more than an equally-high but thinly
observed one.[^c2]

The temporal and (relevance-weighted) activity evidence scores are summed
with a fusion weight $\lambda_t$ and compared to a threshold $\delta_t$:
interact if $s_t \ge \delta_t$, else stay silent. Both $\lambda_t$ and
$\delta_t$ are recalibrated online by replaying recent (evidence, feedback)
history under candidate parameter values and picking the pair with the best
historical F1 — no gradient step and no LLM call in the update itself.[^c3]

On a ProPerSim-based 32-persona, 14-day, 160,632-step benchmark, EOPA
improved interaction-timing F1 by 19.80–20.02 points over the strongest
tested baseline (Reflexion-style natural-language self-improvement) and cut
average daily adaptation time from 11.41 to 0.39 seconds.[^c4]

## Why it matters

This is a working answer to "when should the asker initiate?" that neither
computes a [[value-of-information|value of information]] nor retrains a model: it substitutes two
smoothed, uncertainty-scaled frequency counts, conditioned on a
context-progress index and a semantic activity match, for both. It is a
concrete alternative mechanism to weigh against [[intervention-advantage]]'s
POMDP value-gate on the same stall.

## Transfer

| | |
|---|---|
| **In its home field** | Beta-Binomial conjugate updating with a Jeffreys prior, and scaling a posterior mean by the inverse of its posterior standard deviation, are standard Bayesian-statistics moves for stabilizing sparse-count estimates |
| **Here** | Turned into a per-context "should I interact" evidence score: one Beta-Binomial estimate per (time-interval, activity-progress) anchor and one per activity-semantic prototype, fused and thresholded for a binary ask/silence decision |
| **What survives** | The shrink-toward-prior behavior under few observations, and variance shrinking as feedback accumulates so well-supported anchors dominate poorly-supported ones |
| **What does not** | No posterior distribution or credible interval is carried forward — the scaled mean is a point score fed into a threshold tuned by replay-and-search, not a Bayes-optimal decision rule, and the fusion weight/threshold pair is not proven to converge to any particular optimum |

## Limits

- Reported on one benchmark family (ProPerSim-based simulation with
  LLM-generated timing labels, human-evaluated only for plausibility, not
  ground truth); no deployment with real users is reported (same source as
  the F1 result above).
- The online recalibration of $\lambda_t,\delta_t$ is a local grid replay
  against recent history, not a convergence-guaranteed algorithm; its
  stability under non-stationary user preference is not analyzed.
- `wang-2026-preference` is an unreviewed 2026 arXiv preprint — `[?]`
  pending verifier confirmation.

## Related

[[intervention-advantage]] · [[value-of-information]] · [[bounded-rationality]] · [[sprt]]

[^c1]: wang-2026-preference — "This adaptation is difficult because interaction-worthy moments are sparse and scattered across fine-grained user states (i.e., user activity and current time)."
[^c2]: wang-2026-preference — "The resulting evidence score tends to be larger when the temporal condition favors interaction and receives stronger support from accumulated feedback, allowing better-supported anchors to contribute more strongly."
[^c3]: wang-2026-preference — "It maintains a recent history of temporal evidence, activity evidence, and feedback labels, periodically replays decisions under candidate parameter pairs, and adjusts the parameters to improve the F1 score on the historical data."
[^c4]: wang-2026-preference — "EOPA improves the interaction-timing F1 score by 19.80 points over the Reflexion baseline and substantially reduces inference latency and adaptation time."
