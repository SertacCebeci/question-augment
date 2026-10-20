---
description: "Conciseness can be scored without a reference: how many words an LLM can still strip from a reply while keeping its meaning and named entities, averaged over three compressions."
aliases: ["ConCISE", "reference-free conciseness metric", "compression-based conciseness", "word-removal conciseness"]
sources: ["arxiv-2511-16846"]
---
# Removable-content conciseness

In this work an answer is concise when no word can be taken out of it without harming its meaning or its accuracy.[^c1] The definition is written so that it can be checked without a gold answer: the reply is judged by how much of it a language model can still remove. The metric built on it, ConCISE, has three steps. One LLM prompt asks for three rewrites of the reply: an abstractive summary, an extractive summary, and a pruned text in which non-essential words are removed while the core meaning is kept.[^c2] A second LLM prompt asks whether each rewrite keeps "the same meaning and all the important entities" of the original.[^c3] Each rewrite then yields a compression ratio, the word-length difference between reply and rewrite over the reply's length. Negative differences, and rewrites longer than the reply, count as zero.[^c4] The score is the average of the three ratios.[^c5]

The sign of the score needs care. The prose says the number of words removed "indicates the level of conciseness", which points one way; the definition points the other, since a reply that can lose many words is not concise. The printed formula has each term as one minus the removed fraction, which follows the definition, so I take the formula as operative: a reply a rewriter can cut heavily scores low. This reading comes from a garbled layout in the extracted text (my reading).

The mechanism is simple. A reply that carries only what the question needs leaves the rewriter little to strip, so the ratios stay small. A padded reply gives large ratios. The paper builds the verbose side of its test set this way: GPT-4o was asked to rewrite each answer so that it "retains the same facts but includes filler and repetition".[^c6]

## Evidence

The test set is WikiEval, question-context-answer triples sourced from 50 recently updated Wikipedia pages.[^c7] Human annotators gave Likert ratings, and the paper computes Spearman's correlation "between the ConCISE scores and the human Likert Scale".[^c8] The best version, with GPT-4o as the judge, reached a Spearman of 0.628 with the human ratings.[^c9] The other three judges, Claude-4 Sonnet, Gemini-2.0-Flash and Mistral-Large-2, reached 0.537, 0.518 and 0.473 (the rows of Table 1).[^c10]

In pairwise comparisons, ConCISE agreed with the human choice of the more concise of two answers in 94% of cases for three judges and 90% for GPT-4o.[^c11] The paper reads the pairwise result as "substantially outperforming the GPT Ranking method", which agreed with humans 39% of the time.[^c12]

The baselines are the other half of the claim. Asking an LLM for a 0 to 10 conciseness score gave "weak correlations with human ratings", negative in sign (Spearman −0.108).[^c13] The paper's reading is that "general-purpose LLM judgments and pointwise scoring showed limited effectiveness for conciseness evaluation".[^c14] So the measure's gain is not from using an LLM as judge as such; it is from the compression procedure the judge is asked to carry out.

## Limits

- **Context dependence.** "The definition of non-essential content varies across domains": regulatory disclosures in finance or explanations in education can look redundant and still be needed for accuracy.[^c15] The score has no domain term, so it cannot tell these apart.
- **Narrow validation.** One dataset, one prompt set and four judge models. The paper says "broader validation across diverse datasets, prompting strategies, and evaluation settings would be needed to establish its generalizability and robustness."[^c16] The verbose side of the data is model-made, so it may not match the verbosity people produce.
- **Shared prompt.** The three rewrites come from one prompt. The paper flags that this could let the model's performance on one technique "influences the others", and proposes separate prompts as a test it did not run.[^c17]
- **Correctness is not checked.** The definition mentions accuracy, but the verification step asks only about meaning and named entities relative to the original answer. A short, wrong reply has no removable words left and would score as concise (my inference from the prompt; not tested).
- **Judge dependence.** The score moves with the judge: from 0.473 to 0.628 in Spearman across four models. Which model compresses and which checks is a free parameter the paper does not fix.
- **Scale.** Length enters only as the normalizing denominator. How the ratios behave on very short replies, where a few words are a large fraction, is not reported.

## Related

- [[excess-length-over-minimal-sufficient-baseline]] — the other route to over-generation: score a reply against a curated minimal answer, where this note scores it against its own compressions
- [[llm-judge-biases]] — the verbosity bias of judges; the paper says earlier LLM evaluators are "susceptible to length bias", a claim it does not test here
- [[information-bottleneck]] — compression that keeps what bears on a target; here the target is the reply's own meaning and named entities, with no separate question (my inference about the frame)

[^c1]: arxiv-2511-16846 — "is concise if you cannot remove any words from a(q)"
[^c2]: arxiv-2511-16846 — "generate three versions of the answer using the following"
[^c3]: arxiv-2511-16846 — "the same meaning and all the important entities"
[^c4]: arxiv-2511-16846 — "we consider their values as zero"
[^c5]: arxiv-2511-16846 — "average of three calculations"
[^c6]: arxiv-2511-16846 — "includes filler and repetition"
[^c7]: arxiv-2511-16846 — "sourced from 50 recently updated Wikipedia pages"
[^c8]: arxiv-2511-16846 — "between the ConCISE scores and the human Likert Scale"
[^c9]: arxiv-2511-16846 — "of 0.628 and a Kendall"
[^c10]: arxiv-2511-16846
[^c11]: arxiv-2511-16846 — "aligning with human decisions 94% of the time"
[^c12]: arxiv-2511-16846 — "substantially outperforming the GPT Ranking method"
[^c13]: arxiv-2511-16846 — "the GPT Score baseline showed weak correlations with human ratings"
[^c14]: arxiv-2511-16846 — "general-purpose LLM judgments and pointwise scoring showed"
[^c15]: arxiv-2511-16846 — "The definition of non-essential content varies across domains"
[^c16]: arxiv-2511-16846 — "broader validation across diverse datasets, prompting strategies, and"
[^c17]: arxiv-2511-16846 — "using separate prompts for each compression technique could reduce potential bias"
