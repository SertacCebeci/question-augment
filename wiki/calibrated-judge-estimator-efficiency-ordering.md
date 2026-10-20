---
description: "Estimating a mean from a noisy LLM judge plus a small human-labeled set: EIF = optimal PPI++ is asymptotically smallest in variance, then PPI, then Rogan-Gladen; naive judge means are invalid."
aliases: ["PPI versus Rogan-Gladen efficiency", "efficient influence function judge calibration", "prediction-powered inference for LLM-as-a-judge"]
sources: ["arxiv-2601-05420", "arxiv-2512-05456", "arxiv-2511-21140"]
---
# Calibrated judge estimator efficiency ordering

An LLM judge scores a large evaluation set, and humans label only a small calibration set. Using the judge's mean score alone is cheap but biased, because LLMs produce homogenized judgments. Using only the human labels is unbiased but high-variance.[^c1] The question is how to combine the two sets into an estimate of the true mean (an accuracy or win rate) with a valid confidence interval.

**Two families.** Measurement-error correction (Rogan-Gladen, confusion-matrix inversion) models how the judge errs, via sensitivity q1 and specificity q0, and inverts that model. Prediction-powered inference (PPI) treats the judge output as a surrogate for the truth and corrects its average bias using residuals on the calibration set. It never estimates the misclassification model.[^c2]

**Unification.** Efficient influence function (EIF) theory says the optimal estimator depends on the regression function E[Y | judge output].[^c3] The popular estimators are different approximations to that regression. PPI uses the identity map. PPI++ uses a one-parameter linear map with a tuned weight. RePPI uses a flexible learned model. For a binary outcome, PPI++ with the optimal weight coincides with the EIF estimator, and for general outcomes it need not.[^c4]

**The ordering.** Asymptotically, EIF = MLE = optimally tuned PPI++ is at least as precise as PPI, which is at least as precise as Rogan-Gladen. The PPI-versus-RG comparison is proved for binary outcomes with q0 + q1 > 1. The two variances are equal only if the judge is perfect, q0 = q1 = 1.[^c5]

**Why RG loses.** Its asymptotic variance carries a 1/(q0+q1-1)^2 factor, which blows up as the judge approaches chance.

**Measured.** In simulation, EIF and PPI++ gave near-identical, shortest intervals, typically 35-55% narrower than standard PPI.[^c6] At q0 = q1 = 0.6, RG intervals were roughly 10 times wider than those of EIF and PPI++.[^c7] The naive judge mean undercovers badly. It is close to nominal only where its bias happens to vanish, for example at theta = 0.5 with symmetric errors.

Efficiency is the whole difference among valid methods. Coverage is nominal for RG, PPI, PPI++ and EIF. That holds when the calibration and test sets share one label distribution. Under a shift between them, the paper reports that existing methods can become biased, while the Rogan–Gladen estimator stays unbiased.[^c9][^c10]

## Limits

- The theory concerns mean parameters (average scores, win rates) under a calibration sample that is independent of the evaluation sample and drawn from the same distribution as it. Both sets are assumed i.i.d.. This is my reading of the setup. Distribution shift between the calibration and evaluation sets is not treated here.
- The strict PPI-over-RG proof is for the binary case with a judge better than chance. The continuous-outcome case is explored empirically, not by a general ordering.
- The estimators fix inferential validity regardless of judge quality. They do not improve the judge itself, and a better-calibrated judge only shrinks variance.
- The results are asymptotic. With very few human labels (1%, m = 20), the paper reports that variance can be substantial.
- The real-data example uses a handful of judge and dataset pairs, so the empirical width numbers should not be read as general.
- The paper says nothing about how to choose which items to label, or about judge errors that depend on the item.
- A review of the wider field says that PPI++ "does not attain semiparametric efficiency" in general, and calls this an active area of research. The ordering above is therefore a binary-outcome result, and the efficiency of PPI++ for other outcomes is not settled by these sources.[^c8]
- The Rogan–Gladen unbiasedness under shift is conditional on the judge behaving the same on both sets. The paper's Table 2 groups the difference estimator used in PPI with the calibration-only and conditional-calibration estimators as ones that "rely on the assumption that PrP (Z) = PrQ (Z)".[^c11] Rogan–Gladen instead needs the judge's error rates to be invariant across the two sets, and the paper concedes this "may be violated" if nuisance factors such as response length or style shift the judge.[^c12]
- Whether calibrated judging beats human-only labels is a regime question, not a general one. The paper characterizes it by the judge's sensitivity, specificity and the true score, and reports that "none of the judges we evaluate" falls in the favourable region on its Chatbot Arena setting.[^c13][^c14]
- How to split the calibration labels between the two label types for the Rogan–Gladen interval is a separate question, treated in [[asymmetric-calibration-allocation]].

## Related

- [[llm-judge-validation-gap]] — the scarcity of human validation that makes the calibration set small
- [[llm-judge-biases]] — the systematic judge errors that make the naive mean biased
- [[llm-judge-score-instability]] — a separate noise source that this estimator does not model
- [[predicted-outcome-substitution]] — the naive plug-in whose bias and variance failures these estimators correct; the review that states it is arxiv-2512-05456
- [[asymmetric-calibration-allocation]] — how a fixed calibration budget is split between the two label types to shorten the Rogan–Gladen interval

[^c1]: arxiv-2601-05420 — "relying solely on the calibration set leads to high-variance evaluation, whereas relying on the evaluation set labels leads to biased evaluation, as LLMs are known to"
[^c2]: arxiv-2601-05420 — "This approach yields valid statistical inference without explicitly"
[^c3]: arxiv-2601-05420 — "the optimal estimator depends on the regression function E[Y | Yb ]"
[^c4]: arxiv-2601-05420 — "PPI++ with the optimal λ coincides with the EIF-based"
[^c5]: arxiv-2601-05420 — "with equality if and only if q0 = q1 = 1"
[^c6]: arxiv-2601-05420 — "typically 35–55% narrower than standard PPI"
[^c7]: arxiv-2601-05420 — "at q0 = q1 = 0.6, RG intervals are roughly 10× wider than those of EIF/PPI++."
[^c8]: arxiv-2512-05456 — "it does not attain semiparametric efficiency"
[^c9]: arxiv-2511-21140 — "existing methods can become biased under distribution shift between the test and calibration datasets"
[^c10]: arxiv-2511-21140 — "remains unbiased under such shifts"
[^c11]: arxiv-2511-21140 — "rely on the assumption that PrP (Z) = PrQ (Z)"
[^c12]: arxiv-2511-21140 — "nuisance factors such as response length, style, or prompt type affect the LLM judge differently across datasets"
[^c13]: arxiv-2511-21140 — "in which our LLM-based evaluation yields more reliable estimates than human-only evaluation"
[^c14]: arxiv-2511-21140 — "none of the judges we evaluate"
