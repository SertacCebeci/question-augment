---
description: "Reweights conformal calibration by the likelihood ratio an adaptive clarification induces, restoring finite-sample coverage at every committed round, not just the first."
aliases: ["turn-valid coverage guarantee", "Proposition 1 (Turn-valid coverage)", "selection-reweighted conformal prediction"]
sources: ["tran-2026"]
---
# Turn-valid coverage

> A single conformal threshold fit at the first turn stops being valid the
> moment the system asks an adaptively chosen clarifying question and
> updates on the answer; this result reweights the [[calibration]] by the
> selection's own [[likelihood-ratio|likelihood ratio]] to keep the guarantee at every round a
> session might commit.

## Definition / Mechanism

Split [[conformal-prediction|conformal prediction]] needs calibration and test points to be
exchangeable. In an interactive retrieval session the system picks which
clarification panel to show based on its current belief, then conditions on
the user's pick — the round-$m$ query distribution now depends on the
system's own earlier choices: "Split conformal coverage is valid only when
calibration and test data are exchangeable. A calibrated threshold is fit
once, on first-turn beliefs. But the moment the system asks an adaptively
selected question and folds the answer back into the belief, the test
distribution is no longer exchangeable with the calibration set: the act of
choosing the most informative question, and of conditioning on its answer,
is a form of selection."[^c1]

The fix computes, for each round $m$, the likelihood ratio $w_m(q)$ between
the post-selection query distribution and the calibration distribution —
computable because the panels shown and the picks made are both known to
the system — and replaces the ordinary empirical quantile with the
$w_m$-weighted one: "We correct for the shift explicitly. Let wm (q) denote
the likelihood ratio between the round-m (post-selection) query
distribution and the calibration distribution."[^c2]

The guarantee: for every round at which the system commits, the coverage
set built with that round's reweighted, per-axis threshold contains the
target with probability at least $1-\alpha$, unconditional on which round
the commit happens at. "Proposition 1 (Turn-valid coverage). Suppose the
calibration pairs and the round-m test query are weightedexchangeable with
weight function wm as in Eq. (6), and the selection model π is correctly
specified."[^c3]

## Known as

| Field | Name there | Match |
|---|---|---|
| Tran, Le, Pham et al. (2026), §3.4 | turn-valid coverage guarantee | exact |
| Tran, Le, Pham et al. (2026), Prop. 1 | Proposition 1 (Turn-valid coverage) | exact — the formal statement |
| This note | selection-reweighted conformal prediction | close — the wiki's short name for the mechanism, not the paper's own phrase |

## Why it matters

Without this reweighting, an interactive system that adapts its own next
question and re-applies its original threshold silently loses its coverage
guarantee. "Naive interactive conformal—re-applying the first-turn
threshold—meets coverage at T 0 but drifts below nominal as rounds
accumulate, losing about ten points by T 3 and far more in the worst axis;
this is precisely the feedback-covariate-shift failure of Sec. 3.4."[^c4]

It bears on whether the set a system is willing to commit to at round $m$
is still a valid constraint, which the calibration done at round 0 alone
cannot certify.

## Transfer

| | |
|---|---|
| **In its home field** | Weighted split conformal prediction extends distribution-free finite-sample coverage to known covariate shift between calibration and test; feedback covariate shift is the case where the shift is induced by the model's own past decisions |
| **Here** | Applied to an interactive retrieval session where the "covariate shift" at round $m$ is exactly the panel the system chose to show and the user's resulting pick |
| **What survives** | The finite-sample, distribution-free guarantee, now valid at every committed round rather than only $m=0$, and a continuous (not catastrophic) degradation bound when the selection model is misspecified |
| **What does not** | Simultaneous validity across all rounds of one trajectory — each round's guarantee is separate; the guarantee also requires the user's choice model $\pi$ to be correctly specified |

The misspecification case is bounded, not open-ended: "twice the
total-variation gap between the true and assumed choice models—so coverage
degrades continuously rather than catastrophically."[^c5]

## Limits

The guarantee is conditional on the selection (panel-choice) model $\pi$
being correctly specified or close to it in total variation; it is proven
for the paper's own visual-panel selection mechanism
([[clara-visual-disambiguation]]) and is not shown here to hold for an
arbitrary adaptive clarification policy such as a text-question chooser,
whose selection likelihood ratio may not be computable the same way.

## Related

[[clara-visual-disambiguation]] · [[sequence-level-conformal-prediction]] · [[round-wise-regret-conformal-acceptance]] · [[value-of-information]]

[^c1]: tran-2026
[^c2]: tran-2026 — "We correct for the shift explicitly. Let wm (q) denote the likelihood ratio between the round-m (post-selection) query distribution and the calibration distribution."
[^c3]: tran-2026 — "Proposition 1 (Turn-valid coverage). Suppose the calibration pairs and the round-m test query are weightedexchangeable with weight function wm as in Eq. (6), and the selection model π is correctly specified."
[^c4]: tran-2026 — "Naive interactive conformal—re-applying the first-turn threshold—meets coverage at T 0 but drifts below nominal as rounds accumulate, losing about ten points by T 3 and far more in the worst axis; this is precisely the feedback-covariate-shift failure of Sec. 3.4."
[^c5]: tran-2026 — "twice the total-variation gap between the true and assumed choice models—so coverage degrades continuously rather than catastrophically."
