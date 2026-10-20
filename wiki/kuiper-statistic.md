---
description: "Kuiper statistic: the spread between the largest and smallest running sum of score-weighted miscalibration over sorted predictions, a calibration measure that needs no bins."
aliases: ["Kuiper metric", "Kuiper calibration statistic", "max cumulative miscalibration"]
sources: ["arxiv-2512-22245"]
---
# Kuiper statistic

Calibration can be measured in two ways that differ in what they throw away. Binned measures such as expected calibration error (ECE) sort predictions into bins and average the gap in each bin. The Kuiper statistic keeps the predictions in order and asks where the running deviation between outcomes and scores is largest. The paper describes it as a metric that "measures maximum cumulative miscalibration by computing the spread between over- and under-confidence across all thresholds".[^k1]

Concretely, sort the predictions by score, so that "Given sorted scores S1 < S2" and binary labels R1 to Rn are paired with them.[^k2] Accumulate the weighted differences between each label and its score, Ck over k from 0 to n, with C0 = 0 and weights Wj.[^k3] The statistic is the maximum of the running sum minus its minimum. A perfectly calibrated sequence keeps the running sum near zero, so a large spread means some stretch of thresholds is systematically over- or under-confident.

## Weights

The weights are a choice, and the paper's choice matters. It sets the weight to the score itself, "to prioritize calibration in high-confidence regions".[^k4] The stated reason is production use: high-confidence judgments are kept and low-confidence cases are sent elsewhere, so errors at the top of the score range are the ones that count. Lower values mean better calibration.[^k3]

## Why the paper uses it

The paper reports ECE beside the Kuiper value but calls the Kuiper value "the main indicator of calibration as it is the most stable of the two metrics".[^k5] For ECE it notes "a known weakness" in "that ECE is sensitive to bin size", and uses bins of width 0.1, which is the common choice.[^k6][^k7] Across three train-test splits, "Standard deviations were near zero for all results".[^k8]

My inference: because the Kuiper value is a maximum over thresholds, a single badly placed stretch of confidence sets it, where a bin average would dilute that stretch across its bin. That is why it can register miscalibration that ECE hides, and also why it can be dominated by one region. The paper does not test this directly.

## Relation to the other measures

In [[calibration]] the measures are the Brier score, the reliability diagram and ECE. The Kuiper statistic is a fourth measure of the same property, not a different property. The same limit applies to it as to ECE: a low value does not show that the confidences carry information. On the RewardBench set, higher accuracy lets verbalized confidence, which "tends to overestimate certainty", score "deceptively well", so a low value can come from easy data as much as from good confidence.[^k9]

## Limits

- **One work's evidence.** The stability claim is the authors' own, measured on three splits of the PPE data. Nothing here establishes that the Kuiper statistic is more stable than ECE in general.
- **Weights are a design choice.** Wj = Sj emphasizes high scores. Other weights answer a different question, and a Kuiper value is only comparable across methods that use the same weights.
- **Not a skill score.** Whether a low Kuiper value comes with any resolution, as opposed to a base-rate predictor, is not measured in this work. The calibration note's warning about ECE applies here too.
- **Transcription.** The text renders the running-sum formula only partly. The definition above follows the surrounding prose and the notation in the text; check it against the source before relying on exact constants.
- **Sample size.** No dependence on the number of items is reported, so the value at small n is not known from this work.

## Related

- [[calibration]] — the property this statistic measures; the other measures are the Brier score, reliability and ECE.
- [[brier-calibration-probe]] — the probe whose calibration the paper reports with this statistic as primary.
- [[verifier-discrimination-and-calibration]] — discrimination and calibration as separate properties, with ECE as the calibration measure.

[^k1]: arxiv-2512-22245 — "measures maximum cumulative miscalibration"
[^k2]: arxiv-2512-22245 — "Given sorted scores S1 < S2"
[^k3]: arxiv-2512-22245 — "where C0 = 0 and Wj are weights"
[^k4]: arxiv-2512-22245 — "to prioritize calibration in high-confidence regions"
[^k5]: arxiv-2512-22245 — "main indicator of calibration as it is the most stable"
[^k6]: arxiv-2512-22245 — "weakness that ECE is sensitive to bin size"
[^k7]: arxiv-2512-22245 — "we use a bin size of 0.1, as is common in"
[^k8]: arxiv-2512-22245 — "Standard deviations were near zero for all results"
[^k9]: arxiv-2512-22245 — "higher overall accuracy across models, leading verbalized confidence"
