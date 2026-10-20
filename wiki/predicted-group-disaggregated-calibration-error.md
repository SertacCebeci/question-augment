---
description: "Splitting ECE by the model's predicted group, not by correctness, exposes disparities aggregate ECE hides; Gender-ECE showed one model well calibrated for male pronouns, badly for female."
aliases: ["Gender-ECE", "Gender-Aware Group-ECE", "group-wise ECE"]
sources: ["arxiv-2601-07806"]
---
# Predicted-group disaggregated calibration error

Aggregate Expected Calibration Error (ECE) bins predictions by confidence and averages the absolute gap between mean confidence and mean accuracy in each bin. It cannot show whether the model is calibrated equally for different kinds of answers. The paper's complaint is that "overall calibration, such as ECE, does not reveal how the model behaves differently with respect to male versus female pronouns."[^c1]

## Mechanism

Gender-ECE computes ECE separately for the instances the model predicts as male and for those it predicts as female. It then averages the two: (ECE_male + ECE_female)/2.[^c2] The grouping variable is the predicted label. This differs from MacroCE, which splits by whether the prediction was correct. In the paper's words, Gender-ECE "divides data into two groups (i.e. male and female) based on the predicted label, not relying on the true label for the division."[^c3] The grouping therefore needs no ground truth. "Accuracy" here means agreement with the human stereotype (the benchmark's label), so the score measures how well confidence tracks that bias. It does not measure factual correctness.

The confidence is the softmax probability the model assigns to a pronoun at the cloze position, given the preceding words. It is not a verbalized confidence.[^c4]

## What it showed

- Most of the six models were less calibrated on female pronouns. Gemma-2-9B on WinoBias had ECE of 7% for male and 93% for female pronouns; on GenderLex it was 6% and 94%.[^c5]
- Gender-neutral subjects ("someone", "person") produced the highest calibration error. The authors attribute this to semantic ambiguity and say an explicit occupational role reduces uncertainty and improves calibration.[^c6]
- Larger size helped calibration for male-associated predictions and hurt it for female ones.[^c7]
- A post-hoc Beta calibrator fit on 385 validation items cut ECE about threefold on WinoBias. Accuracy against human bias also rose, for example Gemma-2-9B from 51.6% to 54.7%. The authors note this is expected because the calibrator is fitted on extra data.[^c8]

## Limits

- Only binary male/female groups were scored. The paper's own gender-neutral and queer-identity datasets were evaluated with standard ECE, not with a multi-group version.
- The metric is bin-wise, so it depends on bin count and on how many items fall in each group. With about 771 WinoBias items, per-group bins are sparse. The paper does not test this sensitivity as far as I read.
- The Gemma-2 result (7% vs 93%) coexists with the same model being rated the best-calibrated on the queer-identity benchmark, so the ranking of models depends on the benchmark. A single "worst model" claim does not transfer.
- The causal explanations (distillation hurts calibration, unfiltered data helps) are the authors' interpretation from a few models, not controlled experiments. The paper notes the distillation effect shrinks at 70B.
- Whether the same disaggregation helps for other group splits (language, topic, question type) is my extrapolation, not tested here.

## Related

- [[group-level-accuracy-calibration-target]] — calibrates at group level as a training target; this note measures the same gaps at evaluation time.
- [[group-conditional-abstention-reward]] — another place where group-conditional confidence behavior matters.
- [[accuracy-calibration-gradient-conflict]] — accuracy and calibration can move apart, as they do here between aggregate and group-wise views.

[^c1]: arxiv-2601-07806 — "does not reveal how the model behaves differently with respect to male versus female pronouns"
[^c2]: arxiv-2601-07806 — "(ECEmale + ECEfemale )"
[^c3]: arxiv-2601-07806 — "based on the predicted label, not relying on the true label for the division"
[^c4]: arxiv-2601-07806 — "we extract the probability confidence of the model assigning to"
[^c5]: arxiv-2601-07806 — "Gemma-2-9B achieves low ECE for"
[^c6]: arxiv-2601-07806 — "gender-neutral i.e. someone and"
[^c7]: arxiv-2601-07806 — "Increasing model size improves confidence calibration for male-associated predictions but increases miscalibration for female pronouns"
[^c8]: arxiv-2601-07806 — "resulting in about"
