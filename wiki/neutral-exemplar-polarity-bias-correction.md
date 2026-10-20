---
description: "In LLM sentiment classification, a few examples of the neutral class counter the model's habit of forcing a polarity, raising neutral recall; the gain is larger for GPT-4o-mini than gemini-1.5-flash."
aliases: ["class-balanced few-shot exemplars", "neutral-class exemplar inclusion"]
sources: ["arxiv-2601-08302"]
---
# Neutral-exemplar polarity-bias correction

Zero-shot LLM classifiers asked for sentiment tend to commit to a polarity even when the text has none. The baseline evaluation in this work found both models struggled on the neutral class: "a certain polarity to generated responses, making neutral sentiment classification particularly challenging."[^c1]

Adding a single neutral example to a one-shot prompt shifted the answer distribution. In the authors' words, the "single neutral exemplar encouraged the models to classify instances as neutral more frequently, thereby mitigating the initial bias toward polarized sentiment predictions."[^c2] For gemini-1.5-flash on the three-class SB10k set, neutral recall rose from 0.37 to 0.51, a statistically significant change.[^c3]

The few-shot prompt gave two examples per class and extra examples for neutral. It was the best strategy on most subtasks. For GPT-4o-mini on SB10k the gain was not only on neutral: the examples improved F1 across all three classes (one-shot 0.68 to few-shot 0.72).[^c4] The authors summarise that exemplar-rich prompting "helps mitigate well-documented biases in LLMs toward polar sentiments."[^c5]

The same pattern of a prompt moving the model's class prior shows up for irony. Under gemini-1.5-flash, the baseline labelled almost every tweet ironic, with recall on the "no irony" class of 0.06. Chain-of-thought raised that recall to 0.38.[^c6] Here the correction came from reasoning rather than exemplars. My reading is that in both cases the prompt's effect is mostly a shift in the label prior, which a confusion matrix shows and an accuracy figure hides. That is my inference, not a measured result.

Model dependence: GPT-4o-mini gained far more from additional examples than gemini-1.5-flash, whose few-shot result was nearly indistinguishable from one-shot.[^c7]

## Limits

- Only two models (GPT-4o-mini, gemini-1.5-flash) and a handful of English and German datasets; no other model families.
- The neutral-recall figures come from one prompt wording and one choice of exemplars; the authors note that exemplar selection matters more in multi-class tasks, but exemplar choice was not varied systematically.
- Several few-shot gains were not significant (ABSA on gemini, irony on GPT-4o-mini).
- The prior-shift reading of the irony result is my inference.
- Chain-of-thought lowered some scores below baseline (GPT-4o-mini), so reasoning is not a general corrective.

## Related

- [[instruction-tuning-exemplar-dependence]] — exemplar content also drives outcomes in another setting.
- [[prompt-content-over-surface-form]] — what the prompt says matters more than how it is phrased.
- [[query-length-dependent-expansion-prompting]] — another prompting effect whose size depends on the case.

[^c1]: arxiv-2601-08302 — "a certain polarity to generated responses, making neutral sentiment classification particularly challenging."
[^c2]: arxiv-2601-08302 — "single neutral exemplar encouraged the models to classify instances as neutral more frequently, thereby mitigating the initial bias toward polarized sentiment predictions."
[^c3]: arxiv-2601-08302 — "the SB10k dataset increased from 0.37 to 0.51, demonstrating"
[^c4]: arxiv-2601-08302 — "dataset, GPTs F1-score increased from 0.68 to 0.72, whereas"
[^c5]: arxiv-2601-08302 — "helps mitigate well-documented biases in LLMs toward polar sentiments."
[^c6]: arxiv-2601-08302 — "the negative class of 0.06 in baseline, while the recall can be"
[^c7]: arxiv-2601-08302 — "While both models benefited from few-shot prompting compared to one-shot prompting, GPT-4o-mini exhibited a substantially stronger performance gain."
