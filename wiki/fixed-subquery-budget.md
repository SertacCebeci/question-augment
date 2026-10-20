---
description: "A prompted LLM decomposer emits about five sub-queries nearly every time, and the count does not correlate with the gold evidence count: a fixed budget, not a hop estimate."
aliases: ["fixed sub-query budget", "over-complete decomposition", "decomposition count set by prompt"]
sources: ["doi-10-48550-arxiv-2507-00355"]
---
# Fixed sub-query budget

When a language model is asked to decompose a question for retrieval, the number of sub-queries it writes is set by the prompt, not by the question. In the pipeline measured by Ammann, Golde and Akbik, the prompt capped output at five: "We instruct the LLM to generate at most 5 subqueries per query in order to keep our experiments strictly zero-shot."[^b1] The cap is nearly always reached. The LLM "almost always generates" five sub-queries, in 93.3% of questions on MultiHop-RAG and 98.6% on HotpotQA, "matching the prompt limit."[^b2]

The count is unrelated to the evidence a question needs. Most questions have two or three gold supporting facts, "Most questions require only two or three supporting facts,"[^b3] yet the sub-query count does not track that number: "Both Pearson and Spearman coefficients are near zero."[^b4] The authors read this as the model following a budget rather than the question. The authors take the near-zero scores to mean that the model applies a fixed subquery budget, one "defined by the prompt, rather than adapting to question complexity."[^b5]

The budget is deliberate. The authors did not set out to match the gold count: "to mirror the gold evidence count, but to ensure broad coverage through over-complete decomposition."[^b6] The reasoning is that more sub-queries raise the chance that every relevant piece of evidence lands in the candidate pool. The reranker then prunes the pool, as in [[question-decomposition-retrieval]].

The mechanism, as the paper states it: the decomposer over-generates, and a downstream filter cuts. The sub-query count is therefore a coverage setting, not a model of how many reasoning steps the question has. My inference, not in the text: under a fixed budget a one-fact question and a three-fact question receive the same number of sub-queries, so the extra queries for the simple question can only add candidates for the filter to remove.

## Limits

- Measured on two benchmarks, with one prompt, one cap of five and zero-shot use. The decomposing model is not named in the sections read, so the result is not shown to hold for other models or prompts.
- The gold supporting-fact count is a proxy for "hops." The paper uses the two as one quantity, and "hop" has other senses; see [[temporal-hop-count]] for one of them.
- The near-zero correlation shows that the count does not track evidence. It does not show that five is the right size. The sections read do not vary the cap, so no budget is compared against another.
- The authors themselves suggest that "allowing variable-size decomposition could better align with actual evidence," a suggestion the sections read do not test.
- The sections read do not report how answer accuracy changes with the number of sub-queries, so the cost of over-completeness is not measured here.

## Related

- [[question-decomposition-retrieval]] — the pipeline whose candidate pool this budget fills
- [[preemptive-complexity-estimation]] — a learned predictor that sets whether to decompose and how much reasoning each step gets, the adaptive alternative to a fixed count
- [[temporal-hop-count]] — another sense of "hop," not the one the paper counts
- [[two-stage-reranking]] — the second stage that prunes an over-complete pool

[^b1]: doi-10-48550-arxiv-2507-00355 — "We instruct the LLM to generate at most 5 subqueries per query in order to keep our experiments"
[^b2]: doi-10-48550-arxiv-2507-00355 — "matching the prompt limit"
[^b3]: doi-10-48550-arxiv-2507-00355 — "Most questions require only two or three supporting facts"
[^b4]: doi-10-48550-arxiv-2507-00355 — "Both Pearson and Spearman coefficients are near zero"
[^b5]: doi-10-48550-arxiv-2507-00355 — "defined by the prompt, rather than adapting to question complexity"
[^b6]: doi-10-48550-arxiv-2507-00355 — "to mirror the gold evidence count, but to ensure"
