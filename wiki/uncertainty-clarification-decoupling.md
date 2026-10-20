---
description: "In a three-grid reference game, VLMs told to ask when uncertain barely tie asking to their sampled-vote confidence; most requests are task-irrelevant and human answers do not raise accuracy."
aliases: ["clarification-uncertainty misalignment", "reference-game clarification test"]
sources: ["arxiv-2601-07820"]
---
# Uncertainty-clarification decoupling

A reference game gives a ground truth for when a listener should ask: a speaker describes one of three colour grids and the listener must pick it, so a description that fails to single out the target is detectable. Ali et al. use this to ask whether a vision-language model's clarification requests track its own uncertainty. The paper's framing is that in such a game "it is immediately clear when a description fails to single out the target and a clarification is needed."[^c1]

## Mechanism of the test

Each model is first run five times per round without any option to ask. The majority vote gives the baseline answer, and the share of samples agreeing with it gives a confidence in {0.4, 0.6, 0.8, 1.0}.[^c2] A second run instructs the model to ask a clarification question when uncertain. Three quantities follow: the clarification-request rate, accuracy over non-clarified answers, and relaxed accuracy, where a request counts as acceptable.[^c3] A well-aligned listener would answer when confident and ask when its baseline confidence was low or its baseline answer wrong. This is the paper's own criterion.

## What was measured

- Baseline confidence was high everywhere: GPT-5-mini 99% (accuracy 91%), Qwen2.5-VL-72B 91% (accuracy 77%), Qwen2.5-VL-7B 88% (accuracy 53%). The authors read this as overconfidence, especially for the Qwen models.[^c4]
- Request rates differed sharply: GPT-5-mini 13%, Qwen-72B 24%, Qwen-7B under 0.1%.[^c5]
- GPT-5-mini's rate rose with difficulty (6% far, 17% split and close), and its answered items were more accurate than baseline (94% vs 91%) while its asked items were less accurate (71% vs 91%). So it asks on hard items. Qwen-72B's rate did not follow difficulty.[^c6]
- Across models, confidence on asked items was only slightly lower than baseline; Qwen-72B went from 91% to 87%.[^c7]
- Qwen-72B's accuracy on the items it asked about was not stably lower than baseline: 78% vs 77% on the 500-item subset, 63% vs 71% on the full set.[^c8]

## Are the requests useful?

An expert annotator labelled all 116 Qwen-72B requests. Only 42% were task-relevant; a typical failure is the generic "Could you please clarify which grid you are referring to?", which names no specific ambiguity.[^c9] A human then answered each request (directly if relevant, otherwise by rephrasing the description) and the model was re-run. Confidence rose slightly but accuracy did not: on the 116 asked items, accuracy moved from 0.776 to 0.741, with gains only in the close condition.[^c10] The authors conclude that either the model does not use the added information or the requests seek information it does not need.[^c11]

The reading offered here, which is my inference rather than a tested result: asking and knowing are separate behaviours. A model can be told to ask, and sometimes asks more when items are hard, yet the request carries no content about what is unresolved. Raising the rate of asking therefore cannot be mistaken for raising its value, and a score that counts any request as acceptable (relaxed accuracy) rewards the generic request that did not help.

## Limits

Three models, one dataset (colour grids, 197 games), first-turn descriptions only, and GPT-5-mini ran on a 500-item subset because of cost. Relevance annotation and the human reply were done by a single author. The humans in the original data had 60 rounds to build common ground; the models did not.[^c12] Confidence from five samples is coarse and may itself be miscalibrated; an information-based estimate for Qwen-72B did not change the conclusion (per the authors' appendix, not read here). Some baseline errors may come from flawed speaker descriptions rather than the listener.[^c12] The prompt instruction is the only treatment varied; whether training would couple uncertainty to asking is not tested. The paper is a preprint.

## Related

- [[clarification-request]] — the act being measured here.
- [[natural-ask-timing-misalignment]] — the agentic-task analogue: models' unforced asking does not land where asking pays.
- [[underspecified-question-eager-answering]] — the opposite pole: answering when it should ask.
- [[calibration]] — the overconfidence of sampled-vote confidence is the calibration side of the same gap.
- [[grounding-entropy-clarification-gate]] — an explicit uncertainty gate, versus the prompt-only instruction tested here.

[^c1]: arxiv-2601-07820 — "it is immediately clear when a description fails to single out the target and a clarification is needed."
[^c2]: arxiv-2601-07820 — "This approach yields discrete confidence levels {0.4, 0.6, 0.8, 1.0}"
[^c3]: arxiv-2601-07820 — "Relaxed accuracy (the proportion of responses that are either correct"
[^c4]: arxiv-2601-07820 — "The high confidence across all models indicates a disposition"
[^c5]: arxiv-2601-07820 — "GPT-5-mini generates clarification questions in 13% of items, while Qwen72B does so in 24%"
[^c6]: arxiv-2601-07820 — "rising from 6% (far) to 17% (split and close)"
[^c7]: arxiv-2601-07820 — "Qwen-72B’s mean confidence only drops"
[^c8]: arxiv-2601-07820 — "indicating that it tends to generate clarification requests on more difficult"
[^c9]: arxiv-2601-07820 — "We find that only 42% of the clarification"
[^c10]: arxiv-2601-07820 — "end-to-end accuracy"
[^c11]: arxiv-2601-07820 — "suggesting either that the model does not effectively"
[^c12]: arxiv-2601-07820 — "the VLMs lack access"
