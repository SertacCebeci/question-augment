---
description: "A generated question that contains its own answer lets a model match rather than predict; the paper finds over 40 percent of generated questions do, and training on them worsens forecasting."
aliases: ["answer leakage in generated questions", "answer-in-question shortcut", "leaked answers in synthetic questions"]
sources: ["arxiv-2512-25070"]
---
# Answer-string leakage

When a language model writes a question from a source document, it tends to name the thing it is asking about. If the answer is a short string taken from that document, the question can contain the answer itself. A model trained on such a question can then reach the label by matching text, without the forecasting the question was meant to test.

The paper observes the failure directly. "Despite explicit prompts to avoid it, over 40% of selected questions directly contain the answer string."[^c1] Even after a selection step, "even the filtered samples sometimes leak information about the answer. This can create shortcuts during training."[^c2]

## Mechanism

Leakage is a property of the question text, not of the model. The paper's answers are short (usually one to three words), so the leak is detectable by exact string matching. The editing stage asks a selector model to scan "the title, background, and resolution criteria" for spans that reveal the answer, and to rewrite only those spans "replacing specifics with generic placeholders".[^c3] A final string match on the answer then discards any sample that still contains it.[^c4]

The effect on training is measured. Qwen3-8B trained with RL on 30,000 unfiltered generated questions gets worse: "Training without leakage removal (red) worsens the model, perhaps due to shortcut learning."[^c5] After leakage removal, training improves the model again. The paper's own reading is that the shortcut is the cause, and it is offered with the word "perhaps".

The shortcut is a learning hazard in the reward, not only a quality defect in the data. An outcome-based reward pays for the right answer, so a question whose text already names the answer pays for a reading that does not forecast. The paper does not run that control separately; it is my reading of why a leaked question harms rather than merely wastes compute.

## Limits

- The residual leakage is not measured. An exact string match misses paraphrase and implication: a question that says "the capital of the country whose parliament voted on ..." passes the filter even if it points at the answer. The paper does not estimate how much of this remains.
- The ablation is confounded. The best condition uses a second source as well: the paper's "green" line is "10,000 samples sourced from Forbes", set against 30,000 unfiltered and 30,000 leak-edited samples.[^c6] The gain is attributed to filtering, but source and filtering are not separated.
- The rewriting step is itself a model edit. Replacing a specific with a generic placeholder can make a question vaguer or less answerable; the paper does not measure this cost.
- One model family, one run per condition, and the test set is held out from the training news sources. The effect size on other generators or answer types is not shown.
- The paper's claim that leakage is what drives the drop is supported by the training curves, not by a direct test that the shortcut is being used.

## Related

- [[news-synthesized-forecasting-questions]] — the pipeline in which the leak arises and the editing stage that removes it
- [[free-form-brier-score]] — the reward whose confidence term a leaked question would inflate
- [[post-cutoff-corpus-benchmark-isolation]] — a different leak: pretraining memory of a benchmark's answers, rather than an answer written into the question

[^c1]: arxiv-2512-25070 — "over 40% of selected questions directly contain the answer string"
[^c2]: arxiv-2512-25070 — "even the filtered samples sometimes leak information about the answer. This can create shortcuts during training."
[^c3]: arxiv-2512-25070 — "scan the title, background, and resolution criteria"
[^c4]: arxiv-2512-25070 — "We apply a string matching filter to remove the remaining questions"
[^c5]: arxiv-2512-25070 — "Training without leakage removal (red) worsens the model, perhaps due to shortcut learning."
[^c6]: arxiv-2512-25070 — "10,000 samples sourced from Forbes"
