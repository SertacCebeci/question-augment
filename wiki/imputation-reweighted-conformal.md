---
description: "Reweighting one imputed calibration pool by each missingness pattern's likelihood ratio restores per-pattern conformal coverage, without splitting the data into starved subgroups."
aliases: ["ARC-CP", "acceptance-rejection-corrected conformal prediction", "mask-conditional weighted conformal prediction", "pre-impute-mask-then-correct"]
sources: ["arxiv-2512-14221"]
---
# Imputation-reweighted conformal prediction

> Impute the calibration set once, then correct the imputed scores so they
> look like the data a test point with the same missingness pattern would
> come from.

## Mechanism

Split [[conformal-prediction|conformal prediction]] assumes calibration and
test points come from one law. With missing covariates that assumption
breaks in a specific place: the paper states that conformal prediction
"fails to guarantee coverage when faced with missing covariates."[^c1]

The proposed fix has three steps. First, the calibration set is imputed,
then each imputed point is masked with the test point's missingness pattern
m, so calibration and test share the same observed form. Second, the
imputed points do not follow the true law of the observed coordinates given
the pattern; they follow an imputation law Q_m. The paper names this gap
"resulting in a mask-conditional distribution shift."[^c2] Plain split
conformal on the masked imputed set therefore does not deliver coverage
conditional on the pattern. Third, each imputed calibration point is
weighted by the likelihood ratio ω_m = dP_m/dQ_m, where P_m is the true law
of the observed coordinates and response given pattern m. The conformal
quantile is taken over these weighted scores, with the test point's own
mass placed at +∞ as in ordinary split CP.

The weights are functions of the response as well as the covariates. The
paper notes that its method "requires y-dependent weights for each
calibration point," so the prediction set is not read off a fixed threshold
on a y-free score; it is found by solving the weighted inequality for y.

Under the two stated assumptions (calibration and test data i.i.d., and P_m
absolutely continuous with respect to Q_m), the weighted interval has
conditional coverage at least 1 − α for the test pattern, and the paper
states this holds "for any missingness mechanism."[^c3] MCAR, MAR and MNAR
are therefore not treated as separate cases; the weight absorbs whatever
the pattern does to the law.

Why the weight is needed even when the imputer is good: under MAR or MNAR,
the pattern-conditional law differs from the marginal law, and the paper
says that valid coverage "may not be guaranteed even when the imputation is
perfect."[^c4] The bound it derives separates two terms, the error from
imperfect imputation and "the intrinsic distribution shift caused by
mask-dependent sampling."[^c5] Only the first term shrinks with a better
imputer; the second is what the likelihood ratio removes.

The ratio is estimated, not known. A probabilistic classifier is trained to
separate points that carry a random mask's imputation from points that do
not; "We train a binary classifier" on that labelled set, and Bayes' rule
turns its odds into an estimate of ω_m. The paper's estimator is a
histogram-based gradient-boosted classification tree.[^c6][^c22]

A second variant, the acceptance-rejection-corrected (ARC) method, avoids
weighting altogether. Each imputed point is kept with probability
ω_m/K, where K bounds the ratio. The retained points are then i.i.d. draws
from the true pattern law, and ordinary split conformal applies unchanged.[^c7]
The paper reports that ARC "reduces 90% of the computing time compared to
traditional weighted CP" in the presence of a distribution shift.[^c8]

## Contrast with splitting by group

The natural alternative for pattern-conditional coverage is to calibrate
inside each pattern, as in [[mondrian-conformal-prediction]]. For missing
data the earlier CP-MDA-Exact method (Zaffran et al.) does this by keeping only
calibration points with fewer missing values than the test point,
and the paper notes that this "is infeasible in small-sample regimes."[^c9]
The reweighting route instead "leverages all available calibration data
without modifying the test point."[^c10] The trade is that one pool serves
every pattern, at the price of estimating a density ratio for each.

The ablation in the paper is the clearest evidence of why the correction is
needed: without a weight or acceptance step, "the distribution shift results
in an under-coverage."[^c11] The experiments cover synthetic and
UCI data under all three mechanisms.[^c12] On my reading of the MAR and MNAR
table, worst-pattern coverage lies between about 88% and 91% against a 90%
target.

## Limits

- **Support.** The weights need P_m absolutely continuous with respect to
  Q_m and a bounded ratio. When imputation cannot generate some observable
  points, "the likelihood ratio may not be well-defined or bounded,
  compromising our methods" validity.[^c13] The paper does not test what
  happens to coverage under that violation.
- **Estimation.** "inaccurate estimators can lead to under- or over-coverage."[^c14]
  In a Gaussian study where the true ratio is known, the paper reports that
  coverage approaches target once the correlation between estimate and truth
  is above about 0.3.[^c15] That is one generative model with a known
  ratio. The paper itself says estimation may be hard "to estimate, for
  instance in high dimensions,"[^c16] and high-dimensional estimation is
  not measured here.
- **Cost.** For the weighted method the paper concedes that "it is still
  computationally expensive," which is the reason for ARC.[^c17]
- **Assumptions.** The proofs take calibration and test data to be i.i.d.
  and the imputer to be fitted on training data only. The intro frames the
  setting as exchangeability, but the proofs need i.i.d. draws; the imputed
  points stay exchangeable because the imputer is fitted on training data
  alone.[^c21] Any imputer that sees the calibration responses in a
  different way than the test point would break that symmetry; this is my
  reading, not something the paper tests.
- **Evidence.** The experiments are on "synthetic data and real UCI datasets"[^c18]
  with a score built from conformalized quantile regression.[^c20] Whether
  the gains hold for other scores, other imputers, or non-tabular inputs is
  not established.
- **Open.** The paper lists "deriving tighter robustness bounds" under
  ratio error and violated support as future work.[^c19]

## Transfer to asking and answering

My inference, not the paper's claim: when an answerer works from partial
inputs, the reliability of a stated set depends on which inputs were
present, so a single pooled coverage figure hides the pattern. The method
suggests a history of past answers can be reused for a new pattern by
reweighting rather than splitting, but whether that holds when missingness
is not random and the imputer is itself a model is untested here.

## Related

- [[conformal-prediction]] — the base guarantee; this note adds validity conditional on the missingness pattern, which marginal coverage does not give.
- [[mondrian-conformal-prediction]] — the other route to group-conditional coverage: split the calibration set by group. Reweighting keeps one pool at the cost of a density ratio.
- [[missing-input-clarification-gate]] — my inference: a gate that asks for a missing input removes the pattern shift at its source, where this method corrects for it afterwards.

[^c1]: arxiv-2512-14221 — "fails to guarantee coverage when faced with missing covariates"
[^c2]: arxiv-2512-14221 — "resulting in a mask-conditional distribution shift"
[^c3]: arxiv-2512-14221 — "for any missingness mechanism"
[^c4]: arxiv-2512-14221 — "not be guaranteed even when the imputation is perfect"
[^c5]: arxiv-2512-14221 — "the intrinsic distribution shift caused by mask-dependent sampling"
[^c6]: arxiv-2512-14221 — "We train a binary classifier"
[^c7]: arxiv-2512-14221 — "i.i.d. samples from"
[^c8]: arxiv-2512-14221 — "It reduces 90% of the computing time compared to traditional weighted CP"
[^c9]: arxiv-2512-14221 — "is infeasible in small-sample regimes"
[^c10]: arxiv-2512-14221 — "without modifying the test point"
[^c11]: arxiv-2512-14221 — "the distribution shift results in an under-coverage"
[^c12]: arxiv-2512-14221 — "We present results on synthetic data and real UCI datasets"
[^c13]: arxiv-2512-14221 — "the likelihood ratio may not be well-defined or bounded"
[^c14]: arxiv-2512-14221 — "inaccurate estimators can lead to under- or over-coverage"
[^c15]: arxiv-2512-14221 — "when the correlation exceeds 0.3"
[^c16]: arxiv-2512-14221 — "to estimate, for instance in high dimensions"
[^c17]: arxiv-2512-14221 — "it is still computationally expensive"
[^c18]: arxiv-2512-14221 — "We present results on synthetic data and real UCI datasets"
[^c19]: arxiv-2512-14221 — "Future work includes deriving tighter robustness bounds"
[^c20]: arxiv-2512-14221 — "Conformalized Quantile Regression method"
[^c21]: arxiv-2512-14221 — "as the imputation preserves exchangeability"
[^c22]: arxiv-2512-14221 — "estimated using a Histogram-based Gradient Boosting Classification Tree"
