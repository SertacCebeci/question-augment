---
description: "A keyword's hotness is the frequency of other keywords weighted by a Gaussian kernel on embedding distance, so a topic scores high when it sits in a dense semantic neighbourhood."
aliases: ["embedding-density hotness", "kernel-weighted keyword prominence", "keyword hotness rank"]
sources: ["arxiv-2602-03849"]
---
# Keyword hotness as kernel-weighted density

Before a question can be proposed, the topic has to be picked out of a literature, and a measure of "hotness" is one way to pick it. Zhao et al. build one from OpenAlex keywords. For each year they make a keyword co-occurrence graph, where an edge joins two keywords that appear on the same publication, and embed it with node2vec, so that each keyword gets a vector for that year.[^c1] The hotness of a keyword is then a density: "appearance frequencies of all other keywords, weighted by a Gaussian kernel function based on cosine distance."[^c2] The kernel makes the sum local: "This method assigns a higher weight to semantically closer keywords."[^c3] A keyword is hot when many frequent keywords sit near it in the year's semantic space, which the authors describe as "its density within the semantic space" as well as its frequency.[^c4]

The kernel's width is not a fixed constant. It is set each year from the cosine-distance distribution: the bandwidth "is set to the distance value found at a" pre-defined low percentile of a sample.[^c5] So the same keyword's hotness is comparable across years only through a rank that depends on that year's distance distribution.

The score is used in two ways. Clusters are grown greedily in descending hotness, and a cluster's seed is "the first, and hottest, keyword in that cluster."[^c6] Keywords are then picked by rank. A breakthrough candidate needs "having a 2024 hotness rank within the top kw_breakthrough_threshold" and a rise in rank in 2025, and question candidates come from the top clusters, split into those with high absolute rank and those with high change in rank.[^c7] The change term is what turns a density into a source of questions: a topic that is accelerating is one the question-writers are pointed toward (my reading). Transferred to another literature, the idea that carries over is the density-times-frequency measure and the use of its year-to-year rank change. What does not carry over is the set of thresholds, which the paper sets as absolute ranks (50 and 5 among them).

## Limits

- Hotness measures prominence and momentum in the keyword graph, not impact. The lists in the paper are called "high-impact", but the text does not test whether hot keywords lead to impactful work. (my reading)
- The text does not say how the per-year node2vec embeddings are aligned before the rank change is taken. Each year gets its own embedding, so a change in rank may partly reflect a change of space rather than of attention. (my reading)
- The bandwidth and the thresholds (percentiles, absolute ranks) are chosen by the authors and no sensitivity analysis is reported in the slices read.
- Validation is by illustration: a hotness figure for AI in 2025, a t-SNE map, and a table of top clusters. In the parts read, the coherence of the clusters is asserted, not scored against labels.
- The graph is built from keyword metadata, so the score inherits whatever the keywords were assigned to each paper, and a field that tags less would be measured less well. (my reading)

## Related

- [[retrospective-prospective-judgment-gap]] — the same paper's panel, which judges the candidates this density method proposes, and where agreement with humans drops for open questions.
- [[expert-weighted-stage-voting]] — the staged panel that narrows the candidate pool drawn from the hotness-selected keywords.

[^c1]: arxiv-2602-03849 — "learn a distinct vector embedding for every keyword for that specific year"
[^c2]: arxiv-2602-03849 — "appearance frequencies of all other keywords, weighted by a Gaussian kernel function based on"
[^c3]: arxiv-2602-03849 — "This method assigns a higher weight to semantically closer keywords"
[^c4]: arxiv-2602-03849 — "and its density within the semantic space"
[^c5]: arxiv-2602-03849 — "is set to the distance value found at a"
[^c6]: arxiv-2602-03849 — "the first, and hottest, keyword in that cluster"
[^c7]: arxiv-2602-03849 — "having a 2024 hotness rank within the top kw_breakthrough_threshold"
