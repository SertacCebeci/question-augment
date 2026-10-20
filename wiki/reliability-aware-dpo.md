---
description: "RA-DPO fuses model confidence, annotator agreement, and token-level uncertainty into one reliability score that ranks DPO preference pairs at training and gates abstention at inference."
aliases: ["RA-DPO", "Reliability-Aware Direct Preference Optimization", "reliability score R(x)"]
sources: ["mohammadi-2026"]
---
# Reliability-aware DPO (RA-DPO)

> One score, built from a human disagreement signal and two model-internal
> signals, used twice: to pick which preference pairs are worth training on,
> and to decide when the trained model should answer at all.

## Definition / Mechanism

Mohammadi et al. (2026) define a [[calibration|reliability]] score for a
subjective classification example $x$: "RA-DPO (Reliability-Aware Direct
Preference Optimization), which integrates annotator agreement, model
confidence, and a token-level uncertainty signal into a single reliability
score. RA-DPO uses this score to select high-value preference pairs during
training and to support inference-time abstention, which allows the model
to trade coverage for accuracy."[^c1]

The score is $R(x) = \alpha \cdot \mathrm{conf}(x) + \beta \cdot
\mathrm{agree}(x) + \gamma \cdot (1-\mathrm{sig}(x))$, where "conf(x) ∈
[0, 1] is the model's prediction confidence, the softmax probability of the
predicted token[;] agree(x) ∈ {0.5, 0.667, 0.833, 1.0} is the annotator
agreement calculated as the ratio of annotators' agreement[;] sig(x) = mean
σ(k · (T − pi)) ∈ [0, 1] is a token-level uncertainty score, where pi is
each token's probability, T is the mean token probability, k = 10 is a
steepness parameter, and σ is the sigmoid."[^c2]

The three weights are not hand-set: "We learn α, β, γ by 5-fold stratified
cross-validation. On each fold, a logistic regression takes (conf, agree, 1
− sig) as features and predicts whether the model's answer is correct; the
normalised absolute coefficients give the per-fold weights... Every test
example's R(x) uses weights fit on the other folds, so the coverage-accuracy
numbers below are leakage-free."[^c3]

$R(x)$ is used identically at both ends of the pipeline: at training, pairs
are ranked by $R(x)$ and DPO runs on the top-$k$%; at inference, "the model
predicts only when R(x) exceeds a learned threshold, trading coverage for
accuracy" — "answer if R(x) ≥ τ; else abstain."[^c4]

On 6,920 EXIST 2023 multilingual sexism-detection posts (a task with
persistent six-annotator disagreement), fine-tuning gpt-4o base with RA-DPO
and applying $R(x)$ at inference "reaches 96.2% accuracy at 50% coverage in
the true-agreement setting and 88.7% in the deployable predicted-agreement
setting, both exceeding the 85.3% no-agreement baseline."[^c5]

## Why it matters

On stall 10, this is a concrete instance of the [[abstention]] decision
rule $(f,g)$ in which the selection function $g$ is not one score but a
declared *sum of a disagreement-derived signal and two confidence signals*,
and the same composite is reused to filter training data — the score that
tells the model when to answer is also the score that told the trainer
which examples were worth learning from. It gives the abstention literature
a concrete way to fold *annotator* uncertainty (not just model uncertainty)
into the accept/abstain gate.

## Limits

- The claim rests on one subjective-classification task (EXIST 2023 sexism
  detection) with six annotators per item; agree(x) is defined by a
  four-value ratio specific to that label scheme and does not obviously
  transfer to tasks without repeated per-item annotation.
- At the reported operating point the advantage is thin: "SFT performs well
  because it has a larger α weight (0.280 vs RA-DPO's 0.146): its confidence
  signal is well calibrated and serves as a strong abstention cue by
  itself" — plain supervised fine-tuning ties or slightly beats RA-DPO at
  50% coverage, so the annotator-agreement term's contribution is not shown
  to dominate model confidence alone in this setting.[^c6]
- The deployable predicted-agreement setting substitutes a separately
  trained regressor for the true annotator ratio; its 88.7% (vs 96.2% for
  the unavailable true-agreement upper bound) is the number that matters for
  deployment, and the gap between the two is the price of not having gold
  annotator agreement at inference time.
- Weights are fit by 5-fold cross-validated logistic regression on this
  dataset alone; no cross-task or cross-domain generalisation of the fitted
  $\alpha,\beta,\gamma$ is reported.

## Related

[[abstention]] · [[multilingual-threshold-calibration]] · [[calibration]] · [[preference-optimization-for-questions]]

[^c1]: mohammadi-2026 — "RA-DPO (Reliability-Aware Direct Preference Optimization), which integrates annotator agreement, model confidence, and a tokenlevel uncertainty signal into a single reliability score. RA-DPO uses this score to select highvalue preference pairs during training and to support inference-time abstention, which allows the model to trade coverage for accuracy."
[^c2]: mohammadi-2026
[^c3]: mohammadi-2026
[^c4]: mohammadi-2026 — "the model predicts only when R(x) exceeds a learned threshold, trading coverage for accuracy"
[^c5]: mohammadi-2026 — "reaches 96.2% accuracy at 50% coverage in the true-agreement setting and 88.7% in the deployable predicted-agreement setting, both exceeding the 85.3% no-agreement baseline"
[^c6]: mohammadi-2026 — "SFT performs well because it has a larger α weight (0.280 vs RA-DPO’s 0.146): its confidence signal is well calibrated and serves as a strong abstention cue by itself"
