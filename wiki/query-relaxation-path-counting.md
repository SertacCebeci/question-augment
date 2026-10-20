---
description: "Answering a query over an incomplete graph by relaxing its constants and ranking entities by the paths that reach them, with coarser relaxations breaking ties; no training."
aliases: ["RELAX", "training-free query relaxation", "relaxation-based query answering", "path-count query relaxation"]
sources: ["arxiv-2511-22565"]
---
# Query relaxation by path counting

A complex query over a knowledge graph (KG) is a small pattern of constraints with one fixed entity and one target variable. The paper's example asks for the location of the baseball team a player plays for: a fixed player, one intermediate team, and a target location. When the graph is incomplete, the exact pattern can match nothing, because the edge that would complete it is missing. Query relaxation answers in that case by loosening the pattern and ranking the entities the loosened pattern still reaches. The core idea, in the authors' words, is "to iteratively relax parts of the query, such as replacing a constant entity with a variable, and then to score each entity with the counts of paths arriving to it according to the relaxed query."[^c1]

The procedure is concrete. The first step "Replace the constants at the leaves with variables, count how many paths in the KG match the relaxed query that reach each entity, and assign that count as the score."[^c2] Entities that receive the same count form a tie group. Only the tied portion is then relaxed further, by dropping the constraints fixed so far and counting matches under the simpler pattern. "Residual ties are resolved by ranking entities based on their in-degree in the KG."[^c3]

The ordering is the mechanism. "Relaxation proceeds hierarchically: more specific matches are preferred," and "further relaxation is only applied when ties occur among candidate entities."[^c4][^c4b] The most constrained match wins whenever it discriminates; a coarser pattern decides only what the finer one could not separate. The count is the score, and the strategy uses only edges already in the graph. The authors contrast it with the neural methods: relaxation strategies "do not depend on iterative optimization and are dataset-agnostic."[^c5][^c5b]

What was measured: on three benchmarks built so that queries need one to three missing edges (FB15k237+H, NELL995+H, ICEWS18+H), with filtered MRR, the relaxation baseline "performs better or comparably" with several neural complex-query answerers in a number of cases.[^c6] The neural methods do not win consistently: "While some neural models do outperform RELAX in certain cases, this advantage is neither consistent nor" predictable across datasets.[^c7] The authors also report a length pattern. The gap between neural methods and relaxation "increases with query length, as neural methods compute predictions" whose errors "can propagate with length."[^c8][^c9] On that reading, a path counter does not lose ground as fast as the learned models when the chain gets longer.

What this changes for asking and answering: any system that answers questions over an incomplete graph has a training-free reference that is cheap to run and that uses only the observed structure. The paper's claim is that "simple, nonparametric query relaxation recovers a complementary set of answers that neural models often miss."[^c10] The authors also state the reason the baseline is useful for analysis: it is "computationally efficient in practice, allowing a systematic comparison across large datasets and query types."[^c11] Read this way, relaxation is a yardstick: a learned answerer that does not beat it has not shown that it reaches beyond the graph's explicit structure. That reading is my inference from the comparison; the paper frames it as a call to strengthen non-neural baselines.

## Limits

- The benchmarks are the three above, with queries of the 1p, 2p, 3p, 2i, 3i, pi and ip shapes. The text does not test other shapes, larger graphs, or other domains. The authors write: "Extending this analysis to large scale KGs might" require pruning or approximation.[^c12]
- Relaxation is capped for memory: "to two predicates to preserve memory, which we observe to work well in practice."[^c13] The cap is an engineering choice the authors observed to work, not a result about the method's ceiling.
- The analysis uses one relaxation scheme. "Finally, our analysis focuses on one instantiation of a broader class of query relaxation strategies."[^c14] Other relaxation orders, path statistics or type constraints are not tested.
- The parity is on MRR for these benchmarks. It does not show that relaxation is generally as good as the neural methods, and it does not separate the two explanations the authors offer: "(i) neural models may in practice be reducing to simple statistical patterns akin to those exploited by query relaxation; or (ii) they may be retrieving fundamentally different answers."[^c15] The overlap of the two answer sets bears on the second, and it is a separate note's concern.

## Related

- [[answer-set-complementarity]] — equal MRR for relaxation and neural answerers hides different top-k answer sets; this is the overlap side of the same comparison.
- [[text-free-triplet-answering]] — another way of answering over a triple store with no source text, hop by hop; relaxation is a training-free route over the same kind of graph.

[^c1]: arxiv-2511-22565 — "to iteratively relax parts of the query, such as replacing a constant entity with a variable, and then to score each entity with the counts of paths arriving to it according to the relaxed query."
[^c2]: arxiv-2511-22565 — "Replace the constants at the leaves with variables, count how many paths in the KG match the relaxed query that reach each entity, and assign that count as the score."
[^c3]: arxiv-2511-22565 — "Residual ties are resolved by ranking entities based on their in-degree in the KG."
[^c4]: arxiv-2511-22565 — "Relaxation proceeds hierarchically: more specific matches are preferred,"
[^c4b]: arxiv-2511-22565 — "further relaxation is only applied when ties occur among candidate entities."
[^c5]: arxiv-2511-22565 — "is computationally efficient in practice, allowing a systematic comparison across large datasets and query"
[^c5b]: arxiv-2511-22565 — "depend on iterative optimization and are dataset-agnostic."
[^c6]: arxiv-2511-22565 — "We identify several cases where RELAX performs better or comparably with neural methods."
[^c7]: arxiv-2511-22565 — "While some neural models do outperform RELAX in certain cases, this advantage is neither consistent nor"
[^c8]: arxiv-2511-22565 — "between neural methods and RELAX increases with query length, as neural methods compute predictions"
[^c9]: arxiv-2511-22565 — "whose errors can propagate with length."
[^c10]: arxiv-2511-22565 — "simple, nonparametric query relaxation recovers a complementary set of answers that neural models often miss."
[^c11]: arxiv-2511-22565 — "is computationally efficient in practice, allowing a systematic comparison across large datasets and query"
[^c12]: arxiv-2511-22565 — "Extending this analysis to large scale KGs might"
[^c13]: arxiv-2511-22565 — "to two predicates to preserve memory, which we observe to work well in practice."
[^c14]: arxiv-2511-22565 — "Finally, our analysis focuses on one instantiation of a broader class of query relaxation strategies."
[^c15]: arxiv-2511-22565 — "exploited by query relaxation; or (ii) they may be retrieving fundamentally different answers."
