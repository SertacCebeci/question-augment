---
description: "Self-bias is an LLM's systematic over-rating of its own outputs against a true or human score; in self-refine, which accepts refinements by that same score, the gap grows each iteration."
aliases: ["LLM self-bias", "self-preference in self-refinement", "self-narcissism of LLM evaluators", "false positive self-correction"]
sources: ["doi-10-48550-arxiv-2402-11436"]
---
# Self-bias in self-refinement

Self-bias is the tendency of a model to score its own output above what a reference standard would give it. The work defines it as a statistical bias: over n samples, the average gap between the model's expected quality prediction and the true quality of each sample.[^c1] When the gap is positive the model rates its own sample above the expected score; when it is negative the model underestimates it.[^c2]

An average gap can be zero while the errors are lopsided: one tail of the distribution long and thin, the other short and fat.[^c3] So the work adds a second statistic, distance skewness, which is 0 for a distribution symmetric about the reference and 1 when every deviation lies on one side.[^c4] Bias says whether the self-judgment is inflated; skewness says whether its error runs in one direction. The "true quality" is not always a human label. For translation the study used BLEURT, quantile-mapped to the MQM range, as a stand-in for human raters.[^c5] For constrained generation it used strict string matching of required concepts, and for math a 0/1 check against the ground-truth answer.[^c6]

**Why self-refinement amplifies it.** In self-refine, the same model writes an answer, writes feedback on that answer, and writes a refinement. The feedback is the model's own self-assessment, and a refinement is kept only if the feedback score improves.[^c7] The acceptance rule therefore runs through the very score that carries the bias. A refinement that only looks better to the model is accepted, and the bias compounds over iterations. The paper reports self-bias in all six models it tested (GPT-4, GPT-3.5, Gemini, LLaMA2, Mixtral and DeepSeek), across translation, constrained generation and math; it describes the bias as "universal in self-refine and selfrewarding pipelines."[^c8]

The central measurement is for GPT-4 and Gemini on translation. Their self-scores kept rising across iterations while the reference-based BLEURT score did not improve in step. The authors locate the cause here: the amplification happens because actual performance does not improve through iterations, while the model perceives improvements that are not there. The gap between the two measures "grows larger with each iteration."[^c9] The resulting pressure is toward "false positive corrections rather than improving the actual output quality."[^c10] The same paper finds that self-refine makes outputs more fluent and understandable, but that this "does not necessarily lead to" the improvements the prompt asks for.[^c11]

Stronger models showed less of it. The caption of the translation figure says open-source models exhibit higher levels than GPT-4 and Gemini, yet the amplification was still consistent across four language directions.[^c12][^c13] The bias is related to an older finding: LM-based metrics favor text produced by the same underlying model in summarization, which the authors call narcissism.[^c14]

The abstract names two levers that reduce the bias in the self-refine pipeline: larger model size, and external feedback with accurate assessment, which led to actual performance gains on downstream tasks.[^c15] Both act on the score that the loop trusts, not on the wording of the prompt.

## Limits

- The "true" quality is an approximation. The translation scores are BLEURT, not human ratings, which the authors used "as an approximation" because human raters were too costly.[^c5] A human check covered only 50 examples from Yoruba-English, one rater, at iterations 0 and 10.[^c16]
- Samples are small: 100 test examples per language pair and per task, and six models of 2023–2024 vintage. Newer judges were not measured (my reading).
- The math results are reported as "an increase in bias and skewness estimation" across iterations; the slices read here do not give effect sizes for that task.[^c17]
- The amplification is shown under one acceptance rule (accept if self-feedback improves). Other loops, such as fixed-iteration refinement with no acceptance gate, were not tested in the text read (my reading).
- The paper uses self-consistency as an alternative evaluator in an appendix; those results were not read here.
- The work does not separate a model's own outputs from those of a same-family model, so whether the bias is specific to "self" or to a shared style is not settled by this text (my reading).
- The mitigation claims rest on the abstract; the external-feedback experiments were not read in detail.

## Related

- [[llm-judge-biases]] — the qualitative self-enhancement finding; that note records it as not established, and this work supplies a formal definition and a measured loop effect
- [[judge-coverage-overestimation]] — judges over-rate completeness too, but without a generate-judge-accept loop that feeds the error back
- [[cross-provider-judge-ensemble]] — judging with a different provider is another route around one judge's own bias, the analogue of the external-feedback remedy
- [[cross-generator-judge-bias-index]] — a self-preference figure can carry general leniency; a self-bias statistic of this kind does not separate the two by itself (my reading)

[^c1]: doi-10-48550-arxiv-2402-11436 — "that an LLM favors its own generation."
[^c2]: doi-10-48550-arxiv-2402-11436 — "the LLM underestimates the sample quality compared"
[^c3]: doi-10-48550-arxiv-2402-11436 — "does not guarantee a symmetric distribution"
[^c4]: doi-10-48550-arxiv-2402-11436 — "Distance skewness ranges between 0 and 1."
[^c5]: doi-10-48550-arxiv-2402-11436 — "we utilized the reference-based learned metric"
[^c6]: doi-10-48550-arxiv-2402-11436 — "against the ground truth answer, outputting 1 if they"
[^c7]: doi-10-48550-arxiv-2402-11436 — "We will only accept refinement if the feedback score is"
[^c8]: doi-10-48550-arxiv-2402-11436 — "that self-bias is universal in self-refine and selfrewarding pipelines"
[^c9]: doi-10-48550-arxiv-2402-11436 — "performance measure grows larger with each iteration"
[^c10]: doi-10-48550-arxiv-2402-11436 — "false positive corrections rather than improving the"
[^c11]: doi-10-48550-arxiv-2402-11436 — "pipeline improves the fluency and understandability of model outputs, it does not necessarily lead to"
[^c12]: doi-10-48550-arxiv-2402-11436 — "all LLMs exhibit self-bias, where open-source"
[^c13]: doi-10-48550-arxiv-2402-11436 — "a consistent amplification of self-bias through the"
[^c14]: doi-10-48550-arxiv-2402-11436 — "favors text generated by the same underlying language model"
[^c15]: doi-10-48550-arxiv-2402-11436 — "size and external feedback with accurate assessment can significantly reduce bias in the"
[^c16]: doi-10-48550-arxiv-2402-11436 — "We employ one graduate student to annotate 50 examples"
[^c17]: doi-10-48550-arxiv-2402-11436 — "increase in bias and skewness estimation in the"
