---
description: "A clustered calibration set's effective sample size for a quantile threshold is set by the intra-cluster correlation of exceedance indicators, not of the raw scores."
aliases: ["exceedance design effect", "ancestry-effective calibration size", "effective sample size for thresholds under clustering"]
sources: ["noonan-2026"]
---
# Exceedance design effect

> A conformal threshold, an [[abstention]] gate's cutoff, a safety filter's
> percentile — all are order statistics of a [[calibration]] set. When the
> calibration examples share ancestry (a prompt, a document, a reasoning
> trace), the set is worth fewer independent points than it holds, and
> Noonan (2026) proves the discount is not the one survey
> statistics already had a name for.

## Definition / Mechanism

For calibration scores in $b$ clusters of size $m$ ($n=bm$), define the
exceedance indicator $\mathbb{1}\{S_{j,r}\le q_p\}$ — whether a calibration
point falls below the quantile $q_p$ at level $p$ — and $\rho_I(p)$, its
intra-cluster correlation. Noonan calls $1+(m-1)\rho_I(p)$ the **exceedance
design effect** and $n_{\text{eff}}=n/[1+(m-1)\rho_I(p)]$ the
**ancestry-effective calibration size**. Under exchangeable clusters and a
continuous, positive density at $q_p$, the calibration-conditional coverage
satisfies $\sqrt{n}(C-p_n)\to\mathcal N(0,\,p(1-p)[1+(m-1)\rho_I(p)])$
(Theorem 1) — the design effect enters exactly as a reduction in sample
size.[^c1]

The correlation that matters is between *exceedances*, not scores: two
same-cluster scores can be numerically close and land on opposite sides of
the cutoff, or far apart and agree. On a released SQuAD 2.0 set the score
correlation between two same-paragraph scores is −0.0026 (reads as no
clustering) while the exceedance correlation at the operating level is
+0.0640, giving a design effect of 1.60.[^c2]

Measured on a released process-reward calibration set (25,028 rows, 500
question-clusters), the plug-in and bootstrap estimates agree the set
carries about 1,300 independent points' worth of information once ties are
broken — roughly a 19-fold shrinkage against the exchangeability-implied
n = 25,028.[^c3]

The effect is not always a penalty: it is the variance in whichever
direction the dependence runs, so negatively correlated families
(antithetic or stratified sampling) give a design effect below one and
$n_{\text{eff}} > n$.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Survey statistics (Kish, 1965) | design effect | close — same name, different object: Kish's factor discounts an *average* by score correlation and is, per Noonan, the wrong quantity for a threshold |
| This paper | exceedance design effect / ancestry-effective calibration size | exact |

**Not this concept:** the classical Kish design effect (for a mean) is not
interchangeable with the exceedance design effect (for a quantile
threshold) — on the same data the two can disagree even in sign of what
they'd suggest (score correlation ≈ 0, exceedance correlation clearly
positive).[^c5]

## Why it matters

This is the statistical basis for how tightly a threshold on this stall —
an [[chain-entropy-abstention-gate|abstention gate]], a conformal cutoff, a "this axis is uncertain enough
to ask" trigger — can be calibrated once the calibration examples come from
a shared prompt, document or reasoning trace, the normal case in an LLM
pipeline. A pipeline reading score correlation as its clustering
diagnostic can conclude "no correction needed" on a set whose realized
coverage is over four times as dispersed as the exchangeable law promises.

## Transfer

| | |
|---|---|
| **In its home field** | survey statistics: Kish's (1965) design effect discounts a *mean* from clustered respondents, using the correlation of the measured values. |
| **Here** | a *quantile threshold* (conformal cutoff, abstention gate, safety filter) from clustered calibration scores in an ML pipeline. |
| **What survives** | effective sample size as a reduction factor on $n$, set by an intra-cluster correlation. |
| **What does not** | the input correlation — Kish's formula uses score correlation; a threshold needs the correlation of *exceedance indicators at that level*, which can differ in sign and magnitude and changes with where the threshold is set, so there is no single effective sample size for a dataset, only one per level. |

## Limits

- Theorem 1 is asymptotic ($b\to\infty$, $m$ fixed); a ragged-cluster-size
  correction (replacing $m$ with a size-biased mean) is needed when family
  sizes vary and can itself over-correct under informative sizes.
- Assumption (A3) — the test point drawn independently from the same
  distribution as the calibration clusters — is load-bearing: if it is
  drawn under a different realization of a shared factor, dispersion
  inflates further and no effective-sample-size correction repairs it;
  that is distribution shift, a separate problem.
- The measured 4.46× dispersion on the PRM set is for a tie-broken reading
  of an atomic (9-value) score; the raw atomic score itself shows only
  1.09×, because atomicity violates the theorem's continuity assumption.

## Related

[[calibration]] · [[abstention]] · [[sequence-level-conformal-prediction]] · [[stopping-rules]]

[^c1]: noonan-2026 — "We call 1 + (m̃ − 1)ρI (p) the exceedance design effect and neff the ancestry-effective calibration size."
[^c2]: noonan-2026
[^c3]: noonan-2026 — "Their 25,028-point calibration set delivers about 1,300 points’ worth of information, measured by resampling (Figure 5)."
[^c4]: noonan-2026 — "The sign is not restricted either, and the law covers the case where clustering helps. Nothing in Steps 1–2 requires ρI (p) > 0. Negatively correlated families, which antithetic or stratified calibration sampling produce, give a design effect below one and neff > n."
[^c5]: noonan-2026 — "Three consequences follow. The correction now used in the conformal literature is the wrong quantity, and can miss in either direction."
