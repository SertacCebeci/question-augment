---
description: "A conformal-risk-control threshold, calibrated on exchangeable held-out data, bounds the marginal rate of committing to a wrong answer at a chosen level, for any confidence score."
aliases: ["conformal risk control", "CRC-calibrated threshold", "confident-error rate control"]
sources: ["gu-2026-pause"]
---
# CRC confident-error control

> A threshold set by conformal risk control does not certify that the
> answerer is right; it certifies a ceiling on how often it is confidently
> wrong — a different, and computable, promise.

## Definition / Mechanism

Gu, Yu, Partovi Nia & Asgharian (2026) calibrate the
abstention threshold $\lambda$ of a score-weighted answer-aggregation system
with conformal risk control (CRC), crediting the general method to
Angelopoulos et al. (2024b) and proving its guarantee for this setting
themselves. A **confident error** is the event that the system answers and
is wrong (as opposed to abstaining). Given a [[calibration]] set and a target
confident-error rate $\alpha$, the per-example loss $L_i(\lambda)$ is 1 when
threshold $\lambda$ still yields a confident error on example $i$; "because
raising λ only converts predictions into abstentions, Li (λ) is
non-increasing in λ."[^c1]

The threshold $\hat\lambda$ is set to the smallest $\lambda$ whose empirical
risk is below a finite-sample-corrected target. Their Theorem 2 proves that
this threshold controls the *next* example's confident-error probability:
"Theorem 2 guarantees that the fraction of inputs on which the system
answers incorrectly is controlled at α, regardless of task difficulty or
score choice."[^c2]

The guarantee needs only that calibration and deployment examples are
exchangeable, not i.i.d.: "Exchangeability is the minimal distributional
condition for conformal guarantees; it does not require the calibration
prompts to be i.i.d."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Conformal prediction (Angelopoulos et al. 2024b, per the source's own attribution) | conformal risk control (CRC) | exact — this note covers the source's application of the general procedure, not an independent reading of that paper |
| This source | CRC-calibrated threshold, confident-error rate control | exact |

[^c4.1][^c4]

## Why it matters

It gives stall 10 a certifiable number instead of a tuned one: the coverage
guarantee of [[abstention]]'s SGR algorithm needs an i.i.d. labelled
held-out sample and a fixed loss, while CRC needs only exchangeability and a
monotone loss in $\lambda$ — a weaker, more portable assumption for an
LLM pipeline where prompts arrive in a stream rather than as an i.i.d.
sample.

## Transfer

| | |
|---|---|
| In its home field | [[conformal-prediction|conformal prediction]]: a distribution-free calibration guarantee for a monotone loss over exchangeable calibration and test data, originally for coverage of prediction sets |
| Here | an abstention threshold over a chain-of-thought answer-aggregation confidence score, guaranteeing the marginal confident-error rate on the next question |
| What survives | the exchangeability-only assumption; the finite-sample marginal guarantee; the requirement that the loss be monotone in the threshold |
| What does not | any guarantee conditional on a subgroup or a single hard question — the bound is marginal over the calibration distribution, and a policy that always abstains trivially satisfies it too |

## Limits

- The claim traces to this paper's Theorem 2 and Assumption 3.6, which this
  note read directly; the general CRC method itself is attributed by the
  source to Angelopoulos et al. (2024b), a paper this pass did not read or
  verify — the general procedure is reported here only as the source
  describes it.
- "This is a validity guarantee, rather than utility: the degenerate policy
  that always abstains trivially satisfies the bound." A high yield (few
  abstentions) is not certified by Theorem 2 at all — only [[score-separability]]
  says whether the threshold is also useful.[^c5]
- The guarantee is marginal over the calibration/deployment distribution;
  Assumption 3.6 requires that path generation and the score depend only on
  the prompt, never on the true answer — violated by any pipeline that lets
  ground truth leak into scoring.

## Related

[[abstention]] · [[score-separability]] · [[semantic-entropy]] · [[calibration]]

[^c1]: gu-2026-pause — "because raising λ only converts predictions into abstentions, Li (λ) is non-increasing in λ."
[^c2]: gu-2026-pause — "Theorem 2 guarantees that the fraction of inputs on which the system answers incorrectly is controlled at α, regardless of task difficulty or score choice."
[^c3]: gu-2026-pause — "Exchangeability is the minimal distributional condition for conformal guarantees; it does not require the calibration prompts to be i.i.d."
[^c4.1]: gu-2026-pause — "We use conformal risk control (CRC) (Angelopoulos et al., 2024b): a principled calibration tool that bounds the confident-error rate at a user-specified level and fits naturally with exchangeable calibration data."
[^c5]: gu-2026-pause — "This is a validity guarantee, rather than utility: the degenerate policy that always abstains trivially satisfies the bound."
[^c4]: gu-2026-pause
