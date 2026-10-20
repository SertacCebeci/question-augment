---
description: "A calibration error in which each confident wrong answer is weighted by the clinical cost of its risk category, so overconfidence is measured where mistakes do the most harm."
aliases: ["Clinical Uncertainty Score", "CUS", "harmful overconfident error", "severity-weighted ECE"]
sources: ["arxiv-2511-16625"]
---
# Severity-weighted calibration

Expected calibration error weights every item equally: a confident mistake about a trivial fact counts the same as a confident mistake about a dosing decision. The severity-weighted variant changes the weighting. Each item is assigned to one or more risk categories, and each category carries "a severity weight encoding the clinical cost of a confident error."[^c2] The weights define a subset of errors: "harmful overconfident errors (those in high-severity categories, severity ≥ 2.5)," which are confident, wrong and high-severity.[^c1]

The paper's summary metric, the Clinical Uncertainty Score (CUS), is a calibration measure in which the clinical severity weights "scale with the potential harm associated with" each category.[^c3] The mechanism is the same as ECE, a gap between stated confidence and accuracy, with the gap counted more heavily where a confident error would cost more. This is why the same miscalibration can look small in ECE and large in CUS: ECE sees one average, CUS sees where the average is concentrated.

The measured claims are about the metric's relation to the failures it is meant to summarize, not about clinical outcomes. Across 739 model, method and category groups, CUS "correlates strongly with the harmful overconfident error rate (Pearson r = 0.88)."[^c4] Its incremental value over ECE is reported as variance: in a regression of harmful-error rate on ECE alone and on ECE plus CUS, the explained variance rises "from R2 = 0.60 to 0.79."[^c5] The paper's point is that CUS captures "the severity structure of miscalibration that ECE, which weights all errors equally, does not" capture.[^c9]

The metric is a calibration measure and is blind to ranking by design. Its correlation with AURC is weak, and the paper says that is expected "since CUS is a calibration metric, not a ranking metric."[^c6]

## Limits

- The categories are rule-based strata, not ground truth. The paper uses its 13 categories "as transparent, reproducible evaluation strata (not clinical ground-truth labels)."[^c7] A harm weight is therefore a judgement encoded as a rule, not a measured cost.
- The severity weights are set by the authors. In the sections I read there is no sensitivity analysis showing how the rankings of models change under other weights, so the choice of weights is an open dependency.
- The correlations are between metrics across groups. They show that CUS tracks harmful-error rates in this set of models; they do not show that a lower CUS means fewer patient-level harms.
- The paper itself treats CUS as secondary: "we therefore report CUS as a pre-specified, clinically motivated supplementary summary" while the primary conclusions rest on ECE, AURC and abstention measures.[^c8]
- The evaluation is multiple-choice clinical QA (MedMCQA, MedQA-USMLE) with encoder models. Open-ended clinical generation, where a confident answer is not a letter, is not covered.
- The incremental-variance result is a single regression; I did not check its robustness to other choices of baseline metric.

## Relation to the transfer

My own inference: the transferable idea is that a calibration summary can be made to carry the cost of an error, not only its frequency. Any domain that can name a cost class for its items could build the same kind of weighting. What the paper does not show is that the weights it chose match what a clinician would pay, so the number is useful for comparing models under one fixed weighting and is not an absolute measure of harm.

## Related

- [[calibration]] — the base property; ECE is its unweighted measure, which CUS extends by a severity weight.
- [[confidently-wrong-low-entropy-regime]] — the failure that raw high confidence on wrong answers exhibits, which this metric is designed to expose where it is costly.
- [[expected-severity-risk]] — also weights a clinical severity, but to rank which diagnostic question to ask next, not to score the calibration of an answer.
- [[severity-weighted-omission-risk]] — the same kind of asymmetric severity, applied to what a question leaves out rather than to confidence.
- [[monte-carlo-dropout]] — one of the uncertainty estimators whose output this metric is applied to in the paper.

[^c1]: arxiv-2511-16625 — "weights define harmful overconfident errors (those in high-severity categories, severity ≥ 2.5) and weight"
[^c2]: arxiv-2511-16625 — "Each category carries a severity weight encoding the clinical cost of a confident error"
[^c3]: arxiv-2511-16625 — "that scale with the potential harm associated with"
[^c4]: arxiv-2511-16625 — "CUS correlates strongly with the harmful overconfident error rate (Pearson r = 0.88)"
[^c5]: arxiv-2511-16625 — "variance in the harmful overconfident error rate from R2 = 0.60 to 0.79"
[^c6]: arxiv-2511-16625 — "is expected, since CUS is a calibration metric, not a ranking metric"
[^c7]: arxiv-2511-16625 — "used as transparent, reproducible evaluation strata (not clinical ground-truth labels)"
[^c8]: arxiv-2511-16625 — "we therefore report CUS as a pre-specified, clinically motivated supplementary summary"
[^c9]: arxiv-2511-16625 — "the severity structure of miscalibration that ECE, which weights all errors equally, does not"
