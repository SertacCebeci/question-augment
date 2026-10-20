---
description: "Rankers differ in the unit a loss or score sees: one document (pointwise), a pair (pairwise), or the whole candidate list (listwise), which changes what the model can learn about order."
aliases: ["pointwise pairwise listwise", "listwise ranking loss", "pairwise ranking loss", "learning-to-rank supervision unit"]
sources: ["arxiv-2512-16236"]
---
# Pointwise, pairwise and listwise ranking

Ranking methods are categorized by "supervision strategies and how they process documents during training and scoring," which gives three units: pointwise, pairwise and listwise.[^p1]

A pointwise approach "consider[s] a single document at a time within the loss function"[^p2] in the sense that matters here: a classifier or regressor is trained to predict a relevance score, and the ranking is the sort of those scores. "They train a classifier or regressor to predict the relevance score of an" individual document.[^p3] A pairwise approach "focus[es] on pairs of documents"[^p4] and learns the relative order of two items. A listwise approach "directly consider[s] and optimize[s] the ranking of an entire" candidate list.[^p5]

The survey traces a movement from pairwise to listwise. A pairwise model with a metric-aware gradient was the pivotal step: it enabled direct optimization of non-smooth IR metrics, defining gradients "based on metric changes" from swaps.[^p6] Then came the explicit listwise loss: "[14] pioneered a listwise loss based on top-one probabilities."[^p7]

The survey's comparative claim is that "Listwise losses often yield better performance."[^p8] The sentence is made in the context of T5 rerankers and is the survey's own summary of the cited work. My reading of why the unit matters, not stated in the text: a pointwise loss cannot express that a document is relevant only in comparison with the others on the list, and a pairwise loss sees order but not the position-weighted metric the list is judged by. The listwise unit can encode both.

The unit also brings its own bias. For LLM-based listwise methods the survey notes "positional biases seen in other LLM-based listwise methods," which a tournament-based T5 method is said to mitigate.[^p9] LLMs are "effective in listwise reranking settings where the goal is to produce an ordered document list without explicit relevance scores for individual documents."[^p10] Pairwise prompting is also used: "LLMs have also been proven to be effective text rankers when used in pairwise ranking settings."[^p11]

## Limits

The survey's preference for listwise is a report, and it is hedged ("often"). The text read gives no controlled comparison of the three units on the same data, and the numbers behind the claims sit in cited works.

The word "proven" in the survey's pairwise-LLM sentence is its own; no experiment is reproduced in the text read.

The taxonomy is the survey's. It sorts methods by unit, but a method can combine units (a pairwise loss inside a listwise objective), and the text does not map those hybrids.

The cost of each unit, in comparisons or in tokens per list, is not given in the text read. Any statement about how cost scales with list length would be my inference.

## Related

- [[two-stage-reranking]] — where the choice of unit sits in a retrieve-then-rerank pipeline
- [[pairwise-judge-over-scalar-reward]] — the pairwise-over-pointwise argument, carried over to a judge
- [[listwise-rank-correlation-rubric-reward]] — a listwise objective used to train a rubric generator
- [[groupwise-query-performance-prediction]] — cross-candidate scoring in query performance prediction, where batch size 1 reduces to pointwise learning

[^p1]: arxiv-2512-16236 — "broadly be categorized based on their supervision strategies and how they process"
[^p2]: arxiv-2512-16236 — "Pointwise approaches consider a single document at a time within the loss"
[^p3]: arxiv-2512-16236 — "They train a classifier or regressor to predict the relevance score of an"
[^p4]: arxiv-2512-16236 — "Pairwise approaches focus on pairs of documents."
[^p5]: arxiv-2512-16236 — "Listwise approaches directly consider and optimize the ranking of an entire"
[^p6]: arxiv-2512-16236 — "metrics (like NDCG) by defining gradients (λ-values) based on metric changes"
[^p7]: arxiv-2512-16236 — "[14] pioneered a listwise loss based on top-one probabilities."
[^p8]: arxiv-2512-16236 — "Listwise losses often yield better performance."
[^p9]: arxiv-2512-16236 — "positional biases seen in other LLM-based listwise methods"
[^p10]: arxiv-2512-16236 — "LLM-based rerankers are effective in listwise reranking settings where the goal"
[^p11]: arxiv-2512-16236 — "LLMs have also been proven to be effective text rankers when used in pairwise"
