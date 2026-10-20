---
description: "Confidence in multi-step reasoning is a trajectory, not a scalar; temporal-logic patterns of it separate right from wrong answers, failure patterns transferring across tasks better than success ones."
aliases: ["confidence over time", "STL confidence calibration", "temporal confidence patterns"]
sources: ["arxiv-2601-13387"]
---
# Stepwise confidence temporal signature

Scalar confidence scores (aggregated token probability, entropy, sample consistency) "collapse a sequential reasoning process into a scalar, discarding information about" how certainty evolved.[^c1] Raw sequence probability additionally "suffers from severe length bias, assigning smaller" values to longer responses whatever their correctness, so the score depends on verbosity.[^c2]

The alternative treated here: segment the response into reasoning steps, aggregate token probabilities inside each step into a step confidence, and read the resulting sequence s1..sn as a signal. Signal Temporal Logic (STL) formulas, for example "confidence stays above a threshold during the first t steps", are scored by a robustness value: it "indicates how well a confidence trajectory satisfies a given temporal specification".[^c3] A formula is a fixed structure plus continuous parameters (thresholds, time bounds).

What the authors report (Confidence over Time, arxiv-2601-13387):

- Discriminative mining finds formulas whose robustness separates correct from incorrect responses.
- Failure-mode patterns transfer across tasks better than success patterns: "failure-mode STL patterns generalize better across tasks than success".[^c4]
- Structure is task-bound, parameters are question-bound: "effective temporal structures remain largely task-dependent and require" in-domain mining, while the best parameters vary question by question, so a hypernetwork predicts parameters per question while the STL structure stays fixed for interpretability.[^c5]
- The resulting confidence is reported as better calibrated (ECE, Brier) than baselines on several reasoning tasks, at "an average inference time of 0.55±0.04 seconds per" example, cheaper than sampling-based self-consistency.[^c6]

Why it matters for asking and answering: an answer's trustworthiness is partly carried by the shape of its path (for instance an early dip and no recovery), which a final scalar erases. My inference, not the paper's claim: a questioner could ask about the stability of a step-wise path rather than only about the end value.

## Limits

- Needs step segmentation; the authors note "the choice of segmentation granularity may affect the resulting confidence" signals.[^c7]
- Signals are token-probability only (black-box applicable); evaluation is on structured reasoning benchmarks (math, science QA), not open-ended generation.
- Task-dependence means mined structures do not carry over without in-domain labeled data.
- I did not read the per-benchmark tables closely; effect sizes (ECE, Brier, AUROC gaps) are not restated here.
- Correlation of path shape with correctness is not shown to be causal.

## Related

- [[calibration]] — the property (ECE, Brier) the temporal score is evaluated against
- [[step-calibration-non-composition]] — step-level confidence does not simply compose into answer-level
- [[step-level-risk-calibrated-router]] — another use of step-level confidence signals
- [[inference-time-calibration-ceiling]] — limits on what inference-time confidence estimation can reach

[^c1]: arxiv-2601-13387 — "they collapse a sequential reasoning process into a scalar, discarding information about"
[^c2]: arxiv-2601-13387 — "suffers from severe length bias, assigning smaller"
[^c3]: arxiv-2601-13387 — "STL yields a quantitative robustness score that indicates how well a confidence trajectory satisfies a given temporal specification"
[^c4]: arxiv-2601-13387 — "failure-mode STL patterns generalize better across tasks than success"
[^c5]: arxiv-2601-13387 — "effective temporal structures remain largely task-dependent and require"
[^c6]: arxiv-2601-13387 — "an average inference time of 0.55±0.04 seconds per"
[^c7]: arxiv-2601-13387 — "the choice of segmentation granularity may affect the resulting confidence"
