---
description: "Pointwise re-rankers can be turned into binary relevance judges by direct token generation or score thresholding, matching an LLM judge in 40-50% of cases, but they favor their own family."
aliases: ["re-ranker-as-relevance-judge", "re-rankers as relevance judges", "relevance judging as relevance prediction"]
sources: ["arxiv-2601-04455"]
---
# Re-ranker as relevance judge

Predicting whether a document is relevant to a query and ranking documents by predicted relevance are the same prediction at different output formats. The work cites the argument that there is "no fundamental difference between an LLM-based relevance assessment and an LLM-based re-ranking method."[^c1] It tests this by reusing existing pointwise re-rankers (monoT5, RankLLaMA, and the reasoning-based Rank1; 8 models, 220M to 32B) as judges on TREC-DL 2019-2023, scored by Cohen's kappa against TREC assessors and by system-ranking agreement.[^c2]

## The two adaptations

The obstacle is output format: judging assigns discrete labels, re-ranking outputs continuous scores.[^c3] Two bridges are used. Direct generation takes the final generated token ("true" or "false") of a re-ranker that scores through special-token logits as the label. Score thresholding converts any re-ranker's score to a binary label at a threshold, chosen per judge on a tuning dataset.[^c4]

## What was found

Re-ranker judges beat UMBRELA, a state-of-the-art LLM judge, in around 40%-50% of the cases under both strategies. Rank1 generally did best and was more robust across datasets; scaling up helped but not consistently.[^c5] Thresholding works best when scores sit near the extremes: Rank1's scores are often near 1 or 0, so it is less sensitive to the threshold, while RankLLaMA's best threshold shifted between TREC-DL 22 and 23.[^c6] The authors read the competitive results as evidence that judging is a special case of relevance prediction, so judges could be built on mature predictors instead of from scratch.[^c7]

## The circularity problem: family preference

When the judges then evaluated re-rankers, every judge rated its own re-ranker and same-family re-rankers highest. The RankLLaMA-7B judge ranked RankLLaMA-7B first and 13B second, and the 13B judge reversed them.[^c8] monoT5 and RankLLaMA judges put each other second and rated Rank1 much lower, sometimes near BM25 alone, a cross-family bias of non-reasoning judges against the reasoning family.[^c9] monoT5 and RankLLaMA judges also overestimated BM25, whereas UMBRELA and Rank1 predicted it accurately.[^c10] So a judge that is also a system under test inflates itself; agreement with assessors per document does not guard against this system-level effect (my inference from the two measurements being separate).

## Limits

- Binary labels and pointwise re-rankers only; graded labels and pairwise or listwise re-rankers are left to future work.[^c11]
- All re-rankers were trained on MS MARCO V1 and tested on TREC-DL; other collections and domains were not tested.
- Thresholds were tuned on one dataset and carried to others; the sensitivity result shows this transfers poorly for some models.
- The bias analysis is on a small set of nine systems per year (BM25 plus eight re-rankers), read from scatter plots and Kendall values; no mitigation was tested.
- "Around 40%-50% of cases" counts wins across datasets and metrics; it is not a uniform superiority claim.
- Whether the same-family effect arises from shared training data or shared architecture is not separated (my note).

## Related

- [[llm-judge-biases]] — self-enhancement bias in answer-quality judges; here the same preference appears in relevance judges and is clearer
- [[llm-judge-validation-gap]] — judge agreement with humans needs validation beyond per-item kappa
- [[rationale-level-relevance-judging]] — another approach to LLM relevance judging

[^c1]: arxiv-2601-04455 — "there is no fundamental difference between an LLM-based"
[^c2]: arxiv-2601-04455 — "We perform extensive experiments"
[^c3]: arxiv-2601-04455 — "The main challenge lies in the output"
[^c4]: arxiv-2601-04455 — "(2) Score thresholding applies to all re-rankers."
[^c5]: arxiv-2601-04455 — "Reasoning-based re-rankers (Rank1) generally outperform non-reasoning ones"
[^c6]: arxiv-2601-04455 — "RankLLaMA exhibits substantial sensitivity to threshold selection"
[^c7]: arxiv-2601-04455 — "Our study further suggests that relevance judging is not"
[^c8]: arxiv-2601-04455 — "First, all re-ranker-based judges exhibit clear self-preference:"
[^c9]: arxiv-2601-04455 — "This indicates a cross-family bias:"
[^c10]: arxiv-2601-04455 — "tend to overestimate it."
[^c11]: arxiv-2601-04455 — "adaptation strategies that support graded labels is a natural next"
