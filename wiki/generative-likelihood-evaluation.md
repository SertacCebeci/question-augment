---
description: "An LLM scores generated text by the probability it assigns the text given a source or reference, treating generative likelihood as quality; one NLG evaluation class in the survey."
aliases: ["probability-based evaluation", "generation-probability score", "likelihood-based NLG evaluation"]
sources: ["doi-10-48550-arxiv-2401-07103"]
---
# Generative-likelihood evaluation

A generated text can be scored without asking an evaluator for a judgement. Condition a language model on the source, or on a reference text, and read off the probability it assigns to the candidate; that probability is the quality score. The survey that sorts LLM-based NLG evaluation into protocols names this "probability-based evaluation" and states its premise: "the quality of the generated text is often correlated with the ease of generation by LLMs based on source or reference text."[^g1] The score is the likelihood itself, "the generative likelihood of the produced text is calculated, serving as the score indicative of text quality."[^g2]

The lineage the survey traces starts with a fixed model. Yuan et al. (2021) "first leveraged BART as an evaluator to compute the probability of the generated text based on source or reference text", across machine translation, summarization and data-to-text.[^g3] Fu et al. (2023) carried the idea to LLMs: prompts with a task description and aspect definitions "instruct an LLM-based evaluator to calculate the" generation probability of the candidate.[^g4] A later variant does not read the probability as the score at all. Jia et al. (2023) take changes in probability across conditionings (source present or absent, source and summary swapped, a prefix of the summary supplied) as a reference-free measure, used "to evaluate the faithfulness of the generated summary."[^g5]

A third branch trains the model rather than prompting it. Qin et al. (2022) tuned T5 "in the generative and discriminative fashion, and used the probability of generating a" text as its quality score.[^g6] So the same formal object, a conditional probability of the candidate, is produced either by a frozen model with a prompt or by a model trained for the purpose.

What transfers from the other protocols is the object being scored. In score-based and Likert-style evaluation the LLM emits a number; in pairwise evaluation it "compare[s] the quality" of two texts.[^g7] In generative-likelihood evaluation nothing is emitted: the score is a property of the model's distribution over the candidate, so no answer format can be gamed by the judge's wording. What does not transfer is any guarantee that the distribution tracks quality. The survey treats the correlation as the premise of the method, not as a result.

## Limits

- The premise is asserted, not measured, in the sections of the survey read here. The text gives "often correlated" as background and cites no correlation figure for this protocol in those sections. It is a taxonomy, not a benchmark of the method.
- The score depends on what it is conditioned on. The survey notes that the reference is optional: prompts take "sources, or reference texts (optional)".[^g8] Without a reference, the score measures fit to the source alone, and the text does not show how much that differs.
- Inference, mine and not tested in the text: a likelihood reflects the conditioning model's own frequency preferences, so short, common phrasings may score well whatever their quality. Nothing read here checks that.
- The survey places frozen prompted models and trained models under one protocol. Whether a score from a trained model carries over to a prompted one is not tested here.
- The text does not discuss models that expose no token probabilities. Whether the method applies to such models is open in this text.

## Related

- [[llm-judge-validation-gap]] — what a judge's score does and does not establish; the likelihood score raises the same validation question without a judge in the loop
- [[pairwise-judge-over-scalar-reward]] — the pairwise protocol the survey sets beside this one, where the judge's output is a choice rather than a probability
- [[token-regeneration-probability-confidence]] — a token-probability signal used as a model's confidence in its own answer, not as a score for another text
- [[cross-model-perplexity]] — perplexity as a fluency measure; the score here is closer to a perplexity conditioned on a source or reference
- [[llm-judge-biases]] — systematic preferences of LLM judges; a likelihood score has no judge prompt, but the conditioning model still carries its own preferences (my inference)

[^g1]: doi-10-48550-arxiv-2401-07103 — "the quality of the generated text is often correlated with the ease of generation by LLMs based"
[^g2]: doi-10-48550-arxiv-2401-07103 — "generative likelihood of the produced text is calculated, serving as the score indicative of text quality"
[^g3]: doi-10-48550-arxiv-2401-07103 — "as an evaluator to compute the probability of"
[^g4]: doi-10-48550-arxiv-2401-07103 — "instruct an LLM-based evaluator to calculate the"
[^g5]: doi-10-48550-arxiv-2401-07103 — "evaluate the faithfulness of the generated summary"
[^g6]: doi-10-48550-arxiv-2401-07103 — "used the probability of generating a"
[^g7]: doi-10-48550-arxiv-2401-07103 — "pairwise comparison methods involve using LLM evaluators to compare the quality"
[^g8]: doi-10-48550-arxiv-2401-07103 — "reference texts (optional) as"
