---
description: "Extends conformal prediction's coverage guarantee to multi-step decisions by calibrating on the minimum per-step confidence and rebuilding the prediction set causally, step by step."
aliases: ["sequence-level calibration", "causal conformal prediction", "multi-step conformal prediction"]
sources: ["ren-2023"]
---
# Sequence-level conformal prediction

> Standard [[conformal-prediction|conformal prediction]] needs i.i.d. examples; an agent's own
> actions change what it will see next. This extension keeps the same
> finite-sample guarantee across an entire multi-step plan by calibrating
> on the sequence's worst step and reconstructing the prediction set
> causally, one timestep at a time.

## Definition / Mechanism

Standard CP assumes each test point is drawn i.i.d. from the [[calibration]]
distribution. In a multi-step plan the context at step $t$ depends on the
actions taken (and help given) at steps before it, so this assumption
fails for any one step in isolation. [[ren-2023|Ren, Dixit, Bodrova et
al. (2023)]] instead lift the unit of calibration to a whole scenario: the
i.i.d. assumption is required only of the *scenario*, not of any one step
within it. the robot observes at future steps. Thus, the i.i.d. assumption
for the coverage guarantee is no longer valid.[^c3]

The nonconformity score for a sequence is the minimum of the LLM's
per-step confidence in the true label over all $T$ timesteps; a single
quantile is then calibrated on this sequence-level score exactly as in
single-step CP. Z ={zi =(xi,yi)}N i=1 . Next we use the lowest score over
the timesteps as the score for the sequence :[^c4]

Because the full-sequence prediction set cannot be observed at test time
(only a causal, one-step-at-a-time context stream is available), the
authors define, at each timestep, a causal set using the confidence
threshold from the same calibrated quantile, and prove that the Cartesian
product of these causal per-step sets equals the non-causally defined
sequence set — so building them one step at a time, online, loses nothing.
Claim 1 For any y ∈Y T , y ∈C(xtest) ⇐⇒ y ∈C(xtest).[^c5]

The coverage guarantee then carries over to the causal, sequential
construction: with probability $1-\delta$ over the sampling of the
calibration set, the task completion rate over new test scenarios — asking
for help at any step whose causal set is not a singleton — is at least
$1-\epsilon$. over new test scenarios drawn from D is at least 1−ϵ. If f̂
models true conditional probabilities, the average[^c6]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Ren et al. (2023), §3.3 | sequence-level calibration | exact |
| Ren et al. (2023), §3.3 | causal reconstruction of the prediction set | exact — names the specific step (Claim 1), not the whole calibration procedure |
| This note | multi-step conformal prediction | exact — this note's short name for the same object |

## Why it matters

This is the piece that makes a distribution-free, finite-sample "ask iff
uncertain" guarantee usable across a whole interactive session rather than
one isolated decision — the case that matters for any agent asking several
questions in sequence, where naively re-running single-step CP at each
step has no guarantee once earlier answers change the distribution of
later contexts.

## Transfer

| | |
|---|---|
| **In its home field** | Conformal prediction's coverage guarantee holds for one i.i.d. test point given an i.i.d. calibration set |
| **Here** | A sequence of $T$ dependent decisions inside one scenario, where later contexts are shaped by earlier actions and answers |
| **What survives** | The finite-sample, distribution-free coverage guarantee, now over the whole action sequence, and computability online — causal reconstruction needs no lookahead |
| **What does not** | Per-step marginal validity: the guarantee is over whole scenarios sampled i.i.d., not over individual timesteps, so nothing is said about the coverage rate conditional on having already reached a given step |

## Limits

- Requires i.i.d. sampling of whole *scenarios* (not steps) for
  calibration; a deployment distribution that differs scenario-by-scenario
  from the calibration distribution is not covered.
- The min-over-timesteps nonconformity score is one specific design
  choice; the source does not establish it is the tightest possible
  sequence-level score.
- Stated here only for the single-correct-label-per-step version; the
  source's own extension to multiple acceptable options per step is
  referenced but not read in the slices taken for this note, so it is not
  claimed here.

## Related

[[knowno]] · [[conformal-test-martingale]] · [[value-of-information]]

[^c3]: ren-2023 — "the robot observes at future steps. Thus, the i.i.d. assumption for the coverage guarantee is no longer valid."
[^c4]: ren-2023 — "Next we use the lowest score over the timesteps as the score for the sequence :"
[^c5]: ren-2023 — "Claim 1 For any y ∈Y T , y ∈C(xtest) ⇐⇒ y ∈C(xtest)."
[^c6]: ren-2023 — "over new test scenarios drawn from D is at least 1−ϵ. If f̂ models true conditional probabilities, the average"
