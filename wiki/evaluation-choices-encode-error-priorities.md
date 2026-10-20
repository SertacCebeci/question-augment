---
description: "Deciding whether a model is accurate enough rests on four normative choices (metric, metric balance, test measurement, acceptance threshold), each fixing which errors count and how much."
aliases: ["techno-normative choices in performance evaluation", "accuracy is not purely technical", "appropriate level of accuracy"]
sources: ["arxiv-2604-03254", "arxiv-2512-15907"]
---
# Evaluation choices encode error priorities

A claim of the form "the model is X% accurate" answers a question only after four prior decisions have been made, and each decision carries a value judgement about which errors are tolerable. The paper calls these techno-normative choices: the choice and its technical implementation together determine how normative assumptions materialise.[^c1] The four are selecting metrics, balancing multiple metrics, measuring them against representative data, and determining acceptance thresholds.[^c2] The analysis is conceptual and legal-technical, illustrated with melanoma detection under the EU AI Act; it reports no experiment.

## Choice 1: which metric

Every metric weights errors differently. Accuracy gives false negatives and false positives equal importance, while Precision ignores false negatives altogether.[^c3] Two features of a task make plain accuracy misleading: class imbalance, where scores are driven by the majority class and can mask poor performance on the rare, critical one, and asymmetric error costs.[^c4] The opening example is a melanoma app claiming 99.8% accuracy, which an always-"no melanoma" predictor could roughly match on a rare-disease population.[^c5] Per-class reporting or Balanced Accuracy exposes the imbalance but does not remove the need to judge the unequal cost of the two error types.[^c6] Encoding that cost as a weight factor is itself a normative assumption, since it presumes a patient's death can be weighed against healthcare efficiency.[^c7] A reference-less table metric makes the same choice explicit as two weights, one on missing facts and one on extra facts, so that the trade-off between coverage and hallucination control can be set by the user rather than fixed inside the metric.[^c17] The weights are a visible normative setting, not a neutral default.

## Choice 2: how to balance metrics

Aggregating (F-score, weighted sums) fixes how much each metric contributes. Not aggregating does not escape the choice: it reappears when thresholds are set, because a stricter threshold on one metric prioritises it.[^c8] F-score's harmonic mean makes the effect of beta non-linear, so the encoded priority is hard to read back after the fact.[^c9] Reporting metrics disaggregated keeps the priorities visible to auditors and deployers.[^c10]

## Choice 3: how to measure

Test data must represent the deployment distribution, and the uncertainty estimate must cover plausible deployment variation. Stratifying on several properties at once (gender, ethnicity, age, outcome) needs a very large dataset or an imperfect stratification that can distort performance estimates for intersectional subgroups.[^c11] Splitting by patient rather than image improves validity for new patients but makes image-level stratification harder.[^c12] Uncertainty comes from the learned model (conformal prediction) and from the test sample (bootstrapping).[^c13]

## Choice 4: where the threshold sits

The paper calls the threshold the most evidently techno-normative aspect: once metric and measurement are fixed, it sets the acceptable gap from an ideal model, that is, what degree of harm is tolerable.[^c14] Comparing with humans does not settle it (average or best human? one metric or all? how is measurement uncertainty handled?), and a replacement role may demand more than a triage role.[^c15] The threshold can only be understood given the three earlier choices.[^c16]

## Limits

- Argued by analysis and one worked domain (melanoma, supervised classification with gold labels); the authors say similar choices arise elsewhere, often more complex, but this is not tested.
- No data show that explicit documentation of these choices improves outcomes or compliance.
- The paper does not analyse upstream data and splitting choices in depth, nor sector rules such as medical-device law.
- It offers no procedure for resolving the normative judgements, only that they be made deliberately and documented. Its guidance for open-ended generation or question answering is absent; transfer to those settings is my inference.

## Related

- [[calibrated-accuracy]] — accuracy as a single score hides what a calibrated reading would expose
- [[confidence-interval-calibration]] — measurement uncertainty, the paper's Choice 3
- [[cost-controlled-abstention]] — an explicit cost on error types, as in Choice 1
- [[confidence-discounted-composite-score]] — an aggregated metric whose weights set priorities, as in Choice 2
- [[reference-less-source-alignment]] — a table metric whose missing-fact and extra-fact weights are the explicit priority setting of Choice 1

[^c1]: arxiv-2604-03254 — "We refer to such choices as techno-normative choices, as both the choice and its technical implementation"
[^c2]: arxiv-2604-03254 — "(1) selecting metrics, (2) balancing multiple metrics, (3) measuring metrics against representative data, and (4) determining acceptance thresholds."
[^c3]: arxiv-2604-03254 — "the commonly used Accuracy metric assigns equal importance to false negative and false positive errors, whereas"
[^c4]: arxiv-2604-03254 — "potentially masking poor performance on the rare, yet often more critical,"
[^c5]: arxiv-2604-03254 — "High accuracy, thus, on its own, does not necessarily imply meaningful or safe performance."
[^c6]: arxiv-2604-03254 — "they do not"
[^c7]: arxiv-2604-03254 — "a view that can be ethically controversial"
[^c8]: arxiv-2604-03254 — "In setting thresholds, we may be more restrictive for certain metrics than for others, ultimately"
[^c9]: arxiv-2604-03254 — "As the effect of 𝛽 on the relative importance is non-linear."
[^c10]: arxiv-2604-03254 — "Disaggregating metrics helps with both of these objectives,"
[^c11]: arxiv-2604-03254 — "this would require either a very large dataset or an imperfect stratification"
[^c12]: arxiv-2604-03254 — "it could be better to split the dataset at the patient rather than image level"
[^c13]: arxiv-2604-03254 — "The most common approach in machine"
[^c14]: arxiv-2604-03254 — "The choice of an acceptance threshold is the most evidently techno-normative aspect of performance evaluation."
[^c15]: arxiv-2604-03254 — "others, its performance will need to be significantly higher."
[^c16]: arxiv-2604-03254 — "can only be properly understood and evaluated by taking into account the three techno-normative"
[^c17]: arxiv-2512-15907 — "favors sensitivity (rewarding comprehensive coverage)"
