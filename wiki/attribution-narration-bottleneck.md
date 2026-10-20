---
description: "Turning SHAP or LIME attributions into an LLM narrative is bottlenecked by the LLM: LLM choice explains far more explanation-quality variance than the attribution method does."
aliases: ["XAI-to-NLE bottleneck", "LLM translation bottleneck for attributions", "attribution narration gap", "NLE quality dominated by the generator"]
sources: ["arxiv-2601-02224"]
---
# Attribution-to-narrative bottleneck

When numeric feature attributions are turned into a plain-language explanation by an LLM, the quality of the resulting explanation is set mostly by the LLM, and very little by the attribution method that produced the numbers. The pipeline in the study ran in three steps: a forecasting model made a prediction, an XAI method (SHAP, LIME, or none) produced attributions, and an LLM was prompted to write an explanation for a non-technical user from a context that included "the predicted value, instance features, and XAI attributions when applicable."[^c1]

The no-XAI condition was not an empty prompt. It kept "only prediction context without feature attributions," so the LLM still had the feature values and the model's performance metrics.[^c2] This is what makes the comparison informative: the XAI factor adds one kind of content to a context that already contains most of the facts.

The measured result is a strong asymmetry. Across the 660 explanations, LLM choice carried most of the score variance, and the XAI factor carried little. On Expert Relevancy, the paper reports that the LLM factor is "overwhelmingly determined by LLM capability (ω 2 = .50)," and that the XAI effect is a "small effect" (ω² = .02), in which feature attributions "provides marginally more technical content" — the LLM's ability to present information coherently "explains 25× more variance" (the ratio is the paper's, and it is the ratio of the two ω² values).[^c3][^c13][^c4] On the accuracy dimension, which scores faithfulness to the supplied attributions, the paper finds no XAI effect at all: "LLMs accurately report whatever information they receive."[^c5] SHAP and LIME "show no significant differences across any dimension."[^c6]

The paper's reading is that the bottleneck is the translation, not the producer of the numbers: "The bottleneck for NLE quality appears to be the LLM's translation of attributions into narrative, not the XAI method itself."[^c7] The interaction results fit this reading only loosely. For Expert Relevancy, GPT-4o gained about 0.3 points with XAI, DeepSeek-R1 about 0.2, and Llama-3 no significant gain; the authors suggest "that weaker models may not effectively leverage" the attribution information even when it is supplied.[^c8] So the value of attributions is conditional on the generator, and the average effect is small because the strongest generators gain only modestly from it.

The mechanism, stated as concretely as the data allow: a numeric attribution such as "lag_1: +0.23" is one more token sequence in the prompt.[^c14] Whether it becomes a usable explanation depends on whether the model can convert signed magnitudes into the claim a lay reader needs, such as last week's high usage pushing the forecast up. That conversion is what the LLM does, and the study varies the LLM far more than the attribution method.

## Limits

The study covers one household's energy use, aggregated to weekly totals, and one forecasting task. The authors call these patterns "intuitive," and they warn that "domains requiring specialized knowledge... may yield different patterns."[^c9] A domain where the LLM lacks common-sense priors could reverse the ordering, since the LLM would then have less to translate with and more to need from the attribution.

Only two XAI methods were tested; "We test only two XAI methods (SHAP and LIME)," and attention-based, counterfactual or concept-based attributions were not.[^c10] The main study uses three test instances, so the per-instance variance is thin. Scores come from G-Eval with LLM judges, "(G-Eval) rather than human annotators."[^c11] The paper also says it measures quality, not utility, and that "explanation quality and user performance are often weakly correlated."[^c12] Whether the bottleneck matters for what a user does with the explanation is untested.

The bottleneck claim is a marginal one. The XAI factor's small share is averaged over the LLMs; the significant XAI-by-LLM interaction means that for a strong generator the effect is larger than the headline ω² suggests. Nothing here shows that a better attribution method would never help a weak translator, only that in this design it did not show up in the averages.

## Related

- [[omega-squared-factor-share]] — the effect-size measure that produces the ratios above, and where its marginal shares stop adding up.
- [[interpretability-paradox-in-narrated-explanations]] — the same study's model-type result, which the translation reading is offered to explain.
- [[llm-judge-biases]] — the G-Eval scores are LLM judgments, so the judges' known biases bear on every number here; the paper averages two judges to limit self-preference.
- [[medium-context-sweet-spot-for-numeric-prediction]] — another case where an LLM's handling of numbers in context, not the amount of numeric input, decides the outcome.

[^c1]: arxiv-2601-02224 — "the predicted value, instance features, and XAI attributions when applicable"
[^c2]: arxiv-2601-02224 — "only prediction context without"
[^c3]: arxiv-2601-02224 — "It is overwhelmingly determined by LLM capability (ω 2 = .50)."
[^c4]: arxiv-2601-02224 — "explains 25× more variance"
[^c5]: arxiv-2601-02224 — "XAI condition has no effect: LLMs accurately report whatever information they receive,"
[^c6]: arxiv-2601-02224 — "SHAP and LIME show no significant differences"
[^c7]: arxiv-2601-02224 — "of attributions into narrative, not the XAI method"
[^c8]: arxiv-2601-02224 — "that weaker models may not effectively leverage"
[^c9]: arxiv-2601-02224 — "may yield different patterns"
[^c10]: arxiv-2601-02224 — "We test only two XAI methods (SHAP and LIME)"
[^c11]: arxiv-2601-02224 — "(G-Eval) rather than human annotators"
[^c12]: arxiv-2601-02224 — "and user performance are often weakly correlated"
[^c13]: arxiv-2601-02224 — "provides marginally more technical content"
[^c14]: arxiv-2601-02224 — "lag_1: +0.23"
