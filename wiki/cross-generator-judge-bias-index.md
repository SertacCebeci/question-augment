---
description: "A judge's fairness is scored across the models it grades: the spread between the most and least favoured model's judged-minus-human criterion rate. Overall score is Macro-F1 minus that spread."
aliases: ["bias index", "Bias-Index", "judge bias index", "max-min judge bias"]
sources: ["doi-10-48550-arxiv-2510-18941"]
---
# Cross-generator judge bias index

A judge can agree with human labels on average and still be more lenient toward one model's answers than another's. The bias index measures that unevenness, separately from how often the judge matches humans. For each generator the paper takes the bias as the judge's binary decision minus the human decision, averaged over all criteria: "by first calculating the bias for each model using".[^c1] The index is then the spread of those per-generator values: "the bias-index by taking the difference between max-bias minus the min-bias".[^c2] The overall judge score is Macro-F1 against human labels minus this index: "Overall performance is Macro-F1 minus Bias-Index."[^c3]

The index is a range, so it says how far apart the two most-treated generators are, not which one is favoured. A judge that is lenient toward all three generators by the same amount has an index near zero. Its leniency then reaches the score only through the Macro-F1 term, which compares its decisions with the human ones (my inference from the formula). Read the paper's way, a low value means "an LLM-Judge does not overly-reward/penalize any model's responses, relative to human annotated ground-truths and other models."[^c4]

The motivation is self-enhancement. The paper starts from the claim that "LLMs are known to have self-enhancement bias" and that judges score their own outputs or those of their family higher.[^c5] Qualitative versions of that claim are catalogued in [[llm-judge-biases]]. The bias index is one measured form of it, taken as a spread across three generators from different providers: o3, Grok4 and DeepSeek R1-0528. The vendor generated the responses, and each was scored by its annotator: "The annotator scores each of the three responses on each criteria with either Yes or No".[^c6] The reference for "bias" is therefore that yes/no call on the same responses.

The paper reports a result for its final judge: the benchmark "can be run with no more than 1% bias across 3 models from different providers".[^c7] For one judge, a GPT-4.1 run, the authors report that "both Macro-F1 and Bias-Index are highly consistent, differing no more than 0.2% across three independent runs".[^c8] The criteria were judged without the task prompt, following PaperBench, on the stated ground that "the criteria are designed to be used independently of the prompt".[^c9] The index is therefore a measure of unevenness on bare criteria.

## Limits

- Three generators is a small set. The range is set by two of the three values, and the index does not say which provider a judge favours.
- A spread across providers can come from style, length or content as well as from affinity for a family. The index has no control for these, so it cannot separate self-preference from general leniency toward one generator's output (see [[llm-judge-biases]], where a severity correction removed a raw self-preference figure).
- The reference is the annotators' own yes/no labels. Any annotator leaning toward one generator's wording would appear as neutral truth. The paper does not test this.
- The 0.2% stability figure is for one judge over three runs. The paper says other judges were run "once to save cost", so their index values carry no measured spread.[^c8]
- The 1% threshold is the paper's own figure. The text read gives no argument for why 1% is the right cutoff.
- The index is conditional on judging criteria without the prompt. Whether the prompt would change the spread is not tested here.

## Related

- [[llm-judge-biases]] — the qualitative biases (position, verbosity, self-enhancement); this note gives one of them a measured spread across generators
- [[cross-provider-judge-ensemble]] — averaging judges from several providers, another route around single-judge unevenness
- [[judge-reasoning-effort-tradeoff]] — the same paper reports that more judge thinking tends to raise bias toward particular generators

[^c1]: doi-10-48550-arxiv-2510-18941 — "by first calculating the bias for each model using"
[^c2]: doi-10-48550-arxiv-2510-18941 — "the bias-index by taking the difference between max-bias minus the min-bias"
[^c3]: doi-10-48550-arxiv-2510-18941 — "Overall performance is Macro-F1 minus Bias-Index."
[^c4]: doi-10-48550-arxiv-2510-18941 — "A low bias-index means that an LLM-Judge does not overly-reward/penalize any model’s responses, relative to human annotated ground-truths and other models."
[^c5]: doi-10-48550-arxiv-2510-18941 — "LLMs are known to have self-enhancement bias"
[^c6]: doi-10-48550-arxiv-2510-18941 — "The annotator scores each of the three responses on each criteria with either Yes or No"
[^c7]: doi-10-48550-arxiv-2510-18941 — "Our benchmark can be run with no more than 1% bias across 3 models from different providers"
[^c8]: doi-10-48550-arxiv-2510-18941 — "both Macro-F1 and Bias-Index are highly consistent, differing no more than 0.2% across three independent runs"
[^c9]: doi-10-48550-arxiv-2510-18941 — "we do not provide the original task prompt to the LLM-judge, as the criteria are designed to be used independently of the prompt"
