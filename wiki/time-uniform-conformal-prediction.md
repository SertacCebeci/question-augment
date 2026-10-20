---
description: "Prediction sets whose coverage holds at any data-dependent stopping time, not a fixed n; split conformal fails this, and a more conservative quantile (union bound over time) repairs it at a width cost"
aliases: ["TUC prediction", "TUPAC prediction", "anytime-valid conformal prediction", "time-uniform PAC prediction"]
sources: ["arxiv-2602-06297", "arxiv-2602-04364"]
---
# Time-uniform conformal prediction

Ordinary conformal prediction promises coverage for a sample size n fixed in advance. If an analyst may stop whenever they like, for instance when the set looks precise enough, that promise does not carry over. Time-uniform conformal (TUC) prediction asks for P(Z in C_T) >= 1 - alpha at a random, data-dependent stopping time T, with no assumption on how T is chosen. The sibling goal, time-uniform PAC (TUPAC), asks that the training-conditional coverage be at least 1 - alpha with probability at least 1 - delta, at every stopping time.[^c1]

## Mechanism

For IID data, the paper shows TUC at every random T is equivalent to an expected-minimum condition: the expected minimum probability content of the fixed-time sets over all t >= 1 must be at least 1 - alpha. The authors call it "much stronger" than the fixed-n goal.[^c2] The IID assumption is what lets everything be written in terms of the common distribution.[^c3]

Split conformal fails this test. In a standard-normal stream, the minimum probability content over 100,000 steps averaged 0.838 for a 0.9 target (0.768 for 0.85, 0.684 for 0.8). The split TUC intervals gave 0.890, 0.836 and 0.811.[^c4] The failure comes from taking the usual sample quantile at every t. The repair has the same split-conformal shape with a more conservative quantile at each step.[^c5]

Two ways to choose the quantile are given. Confidence sequences for a fixed quantile give TUPAC, but it is unclear how to get TUC from them.[^c6] A union bound over t, using the fact that the probability content of a sample-quantile set is a uniform order statistic, gives either TUC or TUPAC. A user-chosen function h spreads the alpha-budget over times, so it can be concentrated where the stop is expected, for example around t = 100.[^c7] A related earlier construction (SIPI) covers all miscoverage levels at once, so it is wider than needed when alpha is fixed.[^c8]

The paper also gives an online version in which the score transformation is updated as data arrive and old data can be discarded, and it argues the sets recover after a distribution change point. It states asymptotic width optimality against the oracle set. I read only the introduction and Sections 2 and 3's statements, not the proofs or Section 4.

## What it means for asking and answering

Answers given while a stream is being monitored carry a hidden commitment: the reported uncertainty is valid only if the stopping decision was not made by looking at it. TUC makes stopping on "the set is tight enough" legitimate, at a stated price. (This reading is mine, not a claim of the paper.)

## Calibration-conditional extension to risk control

A second paper moves the same time-uniform idea from coverage over a stopping time to risk conditional on the realized calibration set D_n. Standard split conformal controls error only on average over calibration sets; the authors note that at n = 500 there is a 48% chance of drawing a D_n whose miscoverage exceeds alpha.[^c11] Their anytime-valid risk control asks that, with probability at least 1 - delta, the conditional risk E[loss | D_n] is at most alpha for every n at once. The tool is an anytime-valid concentration bound (time-uniform, in the line of Darling and Robbins and Howard et al.) in place of a fixed-n one, which gives a correction term added to the empirical risk for bounded, monotone losses, including miscoverage as the case B = 1.[^c12] Risks also approach alpha from below (asymptotic tightness), and the authors report a matching lower bound.[^c13] Until the correction term drops below alpha, at small n, the construction returns the uninformative maximal set.[^c14] Test-time distribution shift is handled by importance-weighting the correction term (their Theorem 4.7). This is a different guarantee from the stopping-time one above, and the two are not shown equivalent here.

## Limits

- The price: convergence of the time-uniform intervals is slower than split conformal, which the authors call a necessary tradeoff.[^c9] The sets are wider at every t than fixed-n ones.
- It needs IID data. Long-run coverage for arbitrary, non-IID streams is a different and more ambitious goal handled by adaptive conformal methods.[^c10]
- Batch-level anytime-valid conformal sets (valid across batches, not observations) are a different target.
- The theorem proofs, the online guarantees, the width-optimality results and the real-data experiments were not read here.
- Experiments are mostly simulated normal streams; the practical choice of h affects widths and was not studied beyond a log-normal example.

## Related

- [[repeated-significance-testing]] — the same peeking problem in hypothesis testing, where fixed-n error rates break under optional stopping
- [[predictive-anytime-valid-test]] — another anytime-valid construction, for tests rather than prediction sets
- [[stopping-rules]] — the decision to stop is what the guarantee must survive
- [[betting-based-conformal-risk-control]] — an anytime-valid route to conformal risk control by betting
- [[sequence-level-conformal-prediction]] — conformal sets over sequences, with fixed rather than random sample size

[^c1]: arxiv-2602-06297 — "bT,α ) ≥ 1 − α for all random times T"
[^c2]: arxiv-2602-06297 — "it is much stronger than the usual conformal prediction goal"
[^c3]: arxiv-2602-06297 — "The IID assumption is crucial because it allows us to reformulate"
[^c4]: arxiv-2602-06297 — "content of split conformal prediction intervals is consistently below the desired 1 − α level,"
[^c5]: arxiv-2602-06297 — "the same as the split conformal prediction algorithm except that a more conservative sample"
[^c6]: arxiv-2602-06297 — "the TUC guarantee using such machinery"
[^c7]: arxiv-2602-06297 — "function h allocates the α-budget in order to achieve time-uniform coverage"
[^c8]: arxiv-2602-06297 — "Their procedure also provides uniform coverage"
[^c9]: arxiv-2602-06297 — "of convergence is slower for the time-uniform prediction intervals than the split conformal"
[^c10]: arxiv-2602-06297 — "Their goal is much more ambitious than ours"
[^c11]: arxiv-2602-04364 — "when n = 500 there is a 48% chance of drawing Dn such"
[^c12]: arxiv-2602-04364 — "Anytime-valid concentration bounds, which hold uniformly"
[^c13]: arxiv-2602-04364 — "We further establish a matching lower bound and show that our guarantees"
[^c14]: arxiv-2602-04364 — "hence in (7) we have the infimum of an empty set. By definition, this results in λn = λmax and yield an uninformative"
