---
description: "Token confidence from sampling alone: diff a temperature-0 answer against five temperature-0.8 samples and score each token by the share of variants that keep it, then rescale."
aliases: ["multi-sample diff confidence", "variant-diff multisampling", "multisampling confidence"]
sources: ["arxiv-2512-24560"]
---
# Sample-diff retention confidence

A stochastic model gives a spread of outputs for one prompt, and the spread can be read as uncertainty. The work states the premise: the "possibility of variance between stochastic outputs, for a given prompt, can be viewed as a measure of uncertainty".[^d1] The variance can come from vagueness in the prompt or from noise in training, and the measure does not separate the two.

## Mechanism

Take one sample S at temperature 0, the model's most likely output. Draw a variant set V of five outputs at temperature 0.8: "samples, generated from the model at temperature 0.8."[^d2] Diff each variant against S with a standard sequence-diff library. For each token of S, count how many variants keep it. A token kept in three of five variants gets confidence 3/5. Lines are scored after the token step: "first doing token-level diffing, and taking an arithmetic mean of the confidence in the tokens in the" line.[^d3] The work found this better calibrated than diffing lines as units.

The lineage is consistency sampling. The work points to "later works" that "show how the degree of consistency between a given" sample and a multi-sampled set gives a calibrated measure of confidence in the sample.[^d4] The new step here is the unit: consistency is read off each token, not the whole answer.

## What was measured

The method needs no access to model internals. "Without any access to the model internals, multisampling is able to provide a" usable signal, "but requires Platt scaling."[^d5] For GPT-4o the work reports "For GPT-4o we see a line-level BSS of 0.13 and ECE of 0.03," and at token level a BSS of 0.13.[^d6] For Qwen2.5 7B, "For Qwen2.5 7B, we see a line-level scaled BSS of 0.13 and ECE of 0.04," with a token-level BSS of 0.17.[^d7] The authors single out the repository-level RepoCod data: "We note that multisampling offers a good (and potentially usable) performance" there.[^d8]

## Limits

- The sample count and temperature are hyperparameters, and the text reports one setting: "We note the sample count (5) and the higher temperature for sampling (0.8) are hyper-parameters."[^d9] The text does not report a sweep over them.
- Rescaling is required. Raw sample-diff scores are not calibrated, and the rescaling step needs labelled spans, the data the method otherwise avoids. The work's own summary: multisampling or reflection "is viable, but at least some data is needed for rescaling" to reach good calibration error.
- Variance is not error. A model that is consistently wrong gets high retention and high confidence. The work's definition of uncertainty explicitly mixes "vagueness in the prompt" with "noise/variation in the training data".[^d10] My inference: the measure cannot tell a consistent mistake from a consistent truth.
- With five variants, a token's raw score takes only six values (0, 1/5, … 1). Bucketed calibration then has few distinct levels to work with. This is arithmetic from the design, not a measured effect.
- The cost is six generations per problem (one greedy, five sampled), and token alignment depends on a diff heuristic. Both are design facts, not results.
- Results are on two generators (GPT-4o and Qwen2.5 Coder) and four code datasets. The work does not test other domains for this method.

## Related

- localized-calibration — the calibration these per-token scores are evaluated on.
- [[semantic-entropy]] — multi-sample uncertainty over whole answers; the per-token diff is an analogue, not the same measure.
- [[span-max-pooled-probe]] — the white-box alternative: the same token-level question answered from hidden states, which needs labels and model access.

[^d1]: arxiv-2512-24560 — "between stochastic outputs, for a given prompt, can be viewed as a measure of uncertainty"
[^d2]: arxiv-2512-24560 — "samples, generated from the model at temperature 0.8."
[^d3]: arxiv-2512-24560 — "first doing token-level diffing, and taking an arithmetic mean of the confidence in the tokens in the"
[^d4]: arxiv-2512-24560 — "Later works [8, 20, 31] show how the degree of consistency between a given"
[^d5]: arxiv-2512-24560 — "Without any access to the model internals, multisampling is able to provide a"
[^d6]: arxiv-2512-24560 — "For GPT-4o we see a line-level BSS of 0.13 and ECE of 0.03"
[^d7]: arxiv-2512-24560 — "For Qwen2.5 7B, we see a line-level scaled BSS of 0.13 and ECE of 0.04"
[^d8]: arxiv-2512-24560 — "We note that multisampling offers a good (and potentially usable) performance"
[^d9]: arxiv-2512-24560 — "We note the sample count (5) and the higher temperature for sampling (0.8) are hyper-parameters."
[^d10]: arxiv-2512-24560 — "due to vagueness in the prompt, or noise/variation in the training data"
