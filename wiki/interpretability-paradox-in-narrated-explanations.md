---
description: "A model's inherent interpretability does not carry into LLM-narrated explanations: SARIMAX, with coefficients and higher R², got lower explanation quality than black-box ML models."
aliases: ["interpretability paradox", "inherently interpretable model yields worse narrated explanations", "SARIMAX paradox"]
sources: ["arxiv-2601-02224"]
---
# Interpretability paradox in narrated explanations

A model that is interpretable on its own terms does not necessarily produce the better explanation once an LLM narrates it. In a factorial study of household-electricity forecasts, the classical SARIMAX model, which is "inherently interpretable through its statistical coefficients," yielded lower LLM-generated explanation quality than the black-box ML models it was compared with.[^c1] The comparison runs against the paper's own MLP and RF models, whose R² was ".21–.37," while SARIMAX reached R² = .55.[^c2]

The paper calls this a paradox because the usual argument for interpretable models is that their structure is what makes them explainable. Here the explanations were produced from the same kind of context for every model: the predicted value, instance features, model metrics and, for the ML models, SHAP or LIME attributions.[^c3] SARIMAX enters only with its coefficients in the prompt, since in the study it "provides inherent interpretability through coefficients" and so was given only the no-XAI condition.[^c4] The LLM was then asked to explain an AR, MA or seasonal coefficient to a lay reader, and it did that worse than it explained a feature-importance list. The authors write that "LLMs produce better explanations for the opaque" models than for the transparent one.[^c5]

The study offers two hypotheses, neither tested. One is training data: feature-importance phrasing (a variable "contributed" a signed amount) may be more common in text than statistical coefficient notation, so the LLM has more practice with the former.[^c6] The other is translation: attributions may be "easier to translate … into natural language" than AR, MA and seasonal terms, which are harder to make accessible.[^c6] Both fit the broader reading in [[attribution-narration-bottleneck]]: the LLM's translation, not the form of the underlying model, sets the quality of the narrative. The authors say that if the cause is an LLM limitation rather than a property of model types, "fine-tuning on statistical content or improved prompting may close this gap."[^c7]

## Limits

The authors say directly that "We can only hypothesize about the cause, and it would need to be tested."[^c6] No experiment isolates the training-data or translation account, so the paradox is an observation in one setting.

The comparison is also narrower than the headline suggests. Table 1 lists XGBoost with R² = 0.69, above SARIMAX's 0.55; the paradox is against MLP and RF, not against the most accurate ML model (my reading of Table 1). SARIMAX was run only in the no-XAI condition, so it has about a third of the explanations the ML models have (66 against 198 per model in Table 2); the explanations differ in what context they carry, not only in the model. Other classical models were not tested, though the authors note that "other classical models (e.g., VAR, exponential smoothing)" may behave differently.[^c8]

The result concerns NLE quality as scored by LLM judges, not whether people understand the forecast better when it is explained by an LLM. The authors state that "paradox concerns NLE quality, not whether users" actually understand SARIMAX better when a human explains it.[^c9] A reader should not take the paradox as evidence that interpretable models are worse for people.

## Related

- [[attribution-narration-bottleneck]] — the same study's finding that the LLM outweighs the attribution method, which the paradox's hypotheses extend to the model type.
- [[rung-mismatch-in-interpretability-claims]] — both separate what the model's structure supports from what the claim about it needs; here the claim tested is about narrated quality, not about the model's structure (my reading).
- [[omega-squared-factor-share]] — the effect-size measure used for the model-type comparison.

[^c1]: arxiv-2601-02224 — "SARIMAX yields lower NLE quality than ML"
[^c2]: arxiv-2601-02224 — "vs. .21–.37 for MLP/RF"
[^c3]: arxiv-2601-02224 — "the predicted value, instance features, and XAI attributions when applicable"
[^c4]: arxiv-2601-02224 — "since it provides inherent interpretability through coefficients"
[^c5]: arxiv-2601-02224 — "LLMs produce better explanations for the opaque"
[^c6]: arxiv-2601-02224 — "easier to translate XAI outputs into natural language"
[^c7]: arxiv-2601-02224 — "fine-tuning on statistical content or improved prompting may close"
[^c8]: arxiv-2601-02224 — "other classical models (e.g., VAR, exponential smoothing)"
[^c9]: arxiv-2601-02224 — "paradox concerns NLE quality, not whether users"
