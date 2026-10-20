---
description: "A calibration procedure that turns any uncertainty score into a threshold with a finite-sample, high-probability bound on the accepted-answer error rate."
aliases: ["CIC", "confidence-interval-based calibration", "confidence-interval calibration"]
sources: ["dong-2026-uncertainty"]
---
# Confidence-interval calibration (CIC)

> A selective-answering threshold is only as trustworthy as the number behind
> it; CIC replaces "pick a threshold that looked good on a held-out set" with
> a threshold whose accepted-answer error rate is bounded with a stated
> probability, before deployment.

## Definition / Mechanism

Dong & Shinnou (2026) define, for a frozen LLM
answering under a user-chosen uncertainty score $U$ and a binary alignment
label $E$ (1 = error) collected on a held-out [[calibration]] set, the
threshold-conditioned error rate $R(t) = P(E=1 \mid U \le t)$. Conditional on
the number of calibration points accepted at $t$, the error count is
Binomial$(n, R(t))$, so a Clopper–Pearson or Hoeffding upper confidence bound
$B(t;\gamma)$ satisfies $P(R(t) \le B(t;\gamma)) \ge 1-\gamma$ for any fixed
$t$ (Theorem 3.2).[^c1]

CIC then fixes a finite grid of candidate thresholds
$T=\{t_1,\dots,t_K\}$, applies the bound to each at level $\delta/K$
(Bonferroni), and returns the largest threshold whose bound stays under a
user-set risk level $\alpha$ — or `NULL` if none qualifies. Under
exchangeability between calibration and deployment data, this adaptive
selection controls the accepted-answer error rate at $\alpha$ with
probability $\ge 1-\delta$ simultaneously over the whole grid (Theorem 3.3).[^c2]

The score $U$ is treated as a black-box ranking signal, not required to be
itself calibrated; the method plugs into whatever uncertainty estimator (e.g.
predictive [[entropy]], [[semantic-entropy|semantic entropy]]) is already in use and adds the
statistical layer on top.[^c3]

## Why it matters

Every threshold-based [[abstention]] rule (Chow's rule, Geifman & El-Yaniv (2017)'s
SGR) needs *some* certified relationship between the threshold and the
resulting error rate; CIC names the exact finite-sample statement — binomial
counting plus a Bonferroni-corrected confidence bound — that licenses picking
one threshold out of a searched set and still trusting the number, rather
than only the single fixed threshold Theorem 3.2 covers on its own.[^c4]

## Transfer

| | |
|---|---|
| In its home field | risk-controlling prediction (split [[conformal-prediction|conformal prediction]] and multiple-testing-corrected risk control): a held-out calibration set, an exchangeable draw, a distribution-free confidence bound |
| Here | selecting a single acceptance threshold on an LLM's own uncertainty score for one-shot QA, choosing whether to answer or abstain |
| What survives | the calibration-set/deployment split; the binomial counting argument; the Bonferroni correction across a searched grid of thresholds; the finite-sample (not asymptotic) guarantee |
| What does not | the guarantee needs the calibration and deployment draws to be exchangeable and needs ground-truth alignment labels on the calibration set — for a genuinely one-off, unlabelled question neither holds, so only the calibration mechanics transfer, not the certified bound |

[^c5]

## Limits

- The guarantee is conditional on Assumption 3.1 (exchangeability of
  calibration and deployment data, decoding randomness fixed) — a shift in
  question distribution or model behaviour after calibration breaks it.[^c6]
- It needs a labelled calibration set scored by an application-specific
  alignment criterion $A$; building that criterion (what counts as "aligned")
  is left outside the method.[^c7]
- The exact Theorem 3.3 guarantee is stated for a pre-specified finite grid
  chosen before seeing calibration outcomes; scanning all observed scores for
  finer resolution, as the paper notes is done in practice, is not covered by
  the stated proof.[^c8]
- At small calibration-set sizes or tight risk levels the procedure can
  return no feasible threshold (`NULL`) — the paper reports this as a
  legitimate outcome of scarce data, not a defect of the bound, but it means
  the method can refuse to answer *at every score*, not just per-question.[^c9]

## Related

[[abstention]] · [[calibration]] · [[semantic-entropy]] · geifman-2017

[^c1]: dong-2026-uncertainty
[^c2]: dong-2026-uncertainty — "Theorem 3.3 (Adaptive threshold guarantee) Under Assumption 1, let T = {t1 , . . . , tK } be a fixed finite threshold grid, and let n o t̂ = max t ∈ T : B(t; δ/K) ≤ α ,"
[^c3]: dong-2026-uncertainty — "Our method does not require the uncertainty score itself to be calibrated. Instead, it treats the uncertainty estimator as a ranking signal, and calibrates a statistically"
[^c4]: dong-2026-uncertainty — "uncertainty scores alone are often heuristic, and thresholding them does not provide statistical guarantees on the error rate among accepted answers. We propose CIC, a confidence-interval-based calibration framework that converts arbitrary uncertainty scores into risk-controlled selective answering rules."
[^c5]: dong-2026-uncertainty — "Assumption 3.1 (Exchangeability) The calibration tuples {(Ui , Ei )}N i=1 and a future deployment pair (UN +1 , EN +1 ) are exchangeable."
[^c6]: dong-2026-uncertainty — "Equivalently, the calibration and deployment data are identically distributed, and the deployed model together with its decoding randomness is fixed across samples."
[^c7]: dong-2026-uncertainty — "we introduce an application-specific alignment criterion A : Y × Y → {0, 1},"
[^c8]: dong-2026-uncertainty — "the exact guarantee in Theorem 3.3 is most cleanly stated for a pre-specified finite grid,"
[^c9]: dong-2026-uncertainty — "If no threshold satisfies the constraint, CIC returns no feasible threshold; we report the number of such failed calibration trials as “Fail”."
