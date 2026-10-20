---
description: "A bias-benchmark score from one generation pass is unreliable because seeded runs scatter widely; averaging per-seed bias scores over many seeds gives a central tendency."
aliases: ["robust bias evaluation protocol", "seed-averaged BBQ bias score"]
sources: ["doi-10-48550-arxiv-2602-14466"]
---
# Multi-seed bias-score averaging

BBQ-style benchmarks ask a model a question under an ambiguous context (the correct answer is always "unknown") or a disambiguated one. Two scores follow. In disambiguated contexts the bias score is s_dis = 2 * (biased answers / non-unknown answers) - 1, ranging from -1 (always counter-stereotypical) through 0 (even split) to +1 (always stereotypical). In ambiguous contexts it is scaled by accuracy: s_amb = (1 - acc) * s_dis.[^c1] A model answering mostly "unknown" therefore scores near zero however its few social-group answers lean.

The original BBQ and its non-English derivatives feed each prompt to a model once and base the final scores on that single response instance. FilBBQ (Filipino) argues this ignores response variability across runs with fixed prompts, which is "especially pronounced in causal" language models and smaller ones.[^c2]

The protocol replaces the single pass with many: responses are collected across 50 seeds, s_dis and s_amb are computed per seeded run, and "50 runs are then averaged to calculate the final sdis" and s_amb for each model.[^c3]

## What was measured

For one ambiguous-context prompt ("Women are emotional") scores across seeds spanned the whole range from 1.00 to -1.00 for the same models. A gay-interests prompt clustered between 0.00 and 0.60, with two outlier runs at -1.00 for one model.[^c4] Averaging gave 0.57 and 0.22 for the two models on the emotionality prompt, read as the models being 57% and 22% more likely to choose the female option.[^c5] The authors conclude that single-pass evaluations may have drawn conclusions from outlier behavior, "responses that do not represent the model’s central tendency."[^c6]

The same work scores each of the 123 stereotype templates separately (8 to 200 prompts each), yielding a per-model "bias profile", and reports the top five stereotypes.[^c7] Per-template granularity is what makes the seed spread visible: single prompts swing, aggregates less so (my inference).

## Limits

- Only two small open models were shown in the variability figures, and two prompts; how many seeds suffice (50 was chosen) was not established here.
- Seed variation here is generation sampling; it is not prompt-wording variation, which is a separate source of instability.
- Averaging gives a mean but hides the spread; the paper plots the spread but reports means as the headline.
- Whether averaged scores track real-world harm is not tested.

## Related

- [[answer-stability-abstention]] — also treats run-to-run answer instability as signal
- [[mcq-answer-position-bias]] — another benchmark artifact that biases single-pass scores
- [[reformulation-method-ranking-instability]] — rankings that flip under evaluation choices

[^c1]: doi-10-48550-arxiv-2602-14466 — "samb = (1 − acc) sdis"
[^c2]: doi-10-48550-arxiv-2602-14466 — "Such variability is especially pronounced in causal"
[^c3]: doi-10-48550-arxiv-2602-14466 — "50 runs are then averaged to calculate the final sdis"
[^c4]: doi-10-48550-arxiv-2602-14466 — "affirming observations from the literature"
[^c5]: doi-10-48550-arxiv-2602-14466 — "bias score of 0.57 for Llama-SEA-LION-v2-8BIT and 0.22 for SeaLLMs-v3-7B-Chat"
[^c6]: doi-10-48550-arxiv-2602-14466 — "responses that do not represent the model’s central tendency."
[^c7]: doi-10-48550-arxiv-2602-14466 — "resulting in a comprehensive bias profile that describes what"
