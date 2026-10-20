---
description: "Personalization benchmarks and retrievers reward semantic proximity; the Proximity Advantage score measures how often a relevant session beats a random distractor on query similarity."
aliases: ["Proximity Advantage", "PA score", "proximity bias", "semantic proximity bias"]
sources: ["doi-10-48550-arxiv-2604-26996"]
---
# Semantic proximity bias

Retrieval for lifelong personalization scores each stored session by its embedding similarity to the query. That works only when the relevant session is also the most similar one. The paper calls the case where it is not, and where similarity therefore stands in for relevance, "semantic proximity bias," and measures it with the Proximity Advantage (PA) score: "the fraction of queries for which the average cosine similarity between the query and its ground-truth relevant sessions" exceeds the similarity to a random session.[^c1] Concretely, for each query the score compares the mean similarity of its relevant sessions with the similarity of "a randomly sampled non-relevant session," and PA is the share of queries where the relevant side wins.[^c2] The paper embeds with all-MiniLM-L6-v2.[^c3]

The reading of the number is direct. "A PA of 50% implies that the relevant session is indistinguishable from a random distractor under similarity search."[^c4] A score near 100% means the benchmark can be solved by similarity alone.

The paper applies the score to existing benchmarks and reports that "existing benchmarks exhibit high semantic proximity bias," with PA between 91 and 99 percent for most of them.[^c5] ImplexConv, which was built to separate query and evidence semantically, still has PA of 61.1%, "indicating that relevant sessions still retain a semantic advantage over distractors."[^c6] The paper's own benchmark LUCid scores 51.2% and its hard subset 22.1%, which is close to or below chance.[^c7]

Where the bias bites is retrieval. The paper's Figure 3 bins queries by the semantic margin of the relevant session, and "recall decreases progressively" as that margin shrinks, reaching near zero once distractors are on average closer to the query.[^c8] The same pattern holds for rerankers: "Rerankers prioritize semantic similarity over situational relevance."[^c9] Instruction-guided LLM rerankers recover some hard cases, but the paper reads the remaining gap as evidence that "suggests proximity bias is deeply" built into how the models represent relevance.[^c10]

The paper gives a hypothesis for the cause, not a measured mechanism. Contrastive retrievers such as Contriever build positives from other spans of the same document, so "computing cosine similarity between these representations therefore operationalizes relevance as" closeness of topic.[^c11] Latent user context, sharing little surface overlap with the query, may then fall in the region the model reserves for negatives, "which we hypothesize prevents the model from surfacing situationally relevant signals."[^c12] Training negatives point the same way: the paper notes that "true hard negatives are relatively scarce," so many retrievers rely on in-batch negatives, which are "predominantly semantically unrelated to the query."[^c13]

A structural point follows from the pipeline, not from new data. Reranker recall "is upper bounded by retriever's Recall@k," so "no downstream reranker can surface it" if the latent context is not in the first-stage candidates.[^c14]

## Limits

- The score rests on one embedding model and one random distractor per query. The paper states the definition with a single sampled non-relevant session; a different sample could move a query across the zero line. Whether the reported percentages are stable under resampling is not shown in the text I read.[^c2]
- The authors report that stronger and supervised dense retrievers "exhibit similar degradation on LUCid," which is some evidence against a single-model artefact.[^c15] I found no sparse or lexical retriever compared on the same footing in the sections I read.
- The training-data explanation is explicitly a hypothesis. The paper does not ablate sampling strategies or retrain a retriever to test it.[^c12]
- LUCid-Hard is defined by three query dimensions (age group, geographic location, religion or culture), not by a PA cutoff. Its sessions are "topically distinct sessions relative to the query," as the paper describes them.[^c16] A low score on it partly reflects the construction, where irrelevant sessions are picked for high similarity. That is my inference.
- The result concerns recall of a latent attribute. It does not show that a system with higher PA produces worse answers in deployment, and generation has its own bottleneck: even with the relevant session supplied, models "struggle to condition on latent attributes even when" it is present.[^c17]

## Related

- [[situational-relevance]] — the notion of relevance this score is set against.
- [[reranker-as-relevance-judge]] — the reranking stage, where the paper finds the same bias when rerankers judge relevance.
- [[intent-aligned-cross-session-retrieval]] — a contrastive encoder trained on goal-level labels rather than topical ones; my inference is that it targets the same gap, though the paper does not test a fix like it.

[^c1]: doi-10-48550-arxiv-2604-26996 — "the fraction of queries for which the average cosine similarity between the"
[^c2]: doi-10-48550-arxiv-2604-26996 — "a randomly sampled non-relevant session"
[^c3]: doi-10-48550-arxiv-2604-26996 — "a standard sentence transformer trained for semantic similarity"
[^c4]: doi-10-48550-arxiv-2604-26996 — "a PA of 50% implies that the relevant session is indistinguishable from a random distractor"
[^c5]: doi-10-48550-arxiv-2604-26996 — "existing benchmarks exhibit high semantic proximity bias"
[^c6]: doi-10-48550-arxiv-2604-26996 — "indicating that relevant sessions still retain a semantic advantage over distractors"
[^c7]: doi-10-48550-arxiv-2604-26996
[^c8]: doi-10-48550-arxiv-2604-26996 — "recall decreases progressively"
[^c9]: doi-10-48550-arxiv-2604-26996 — "Rerankers prioritize semantic similarity over situational relevance"
[^c10]: doi-10-48550-arxiv-2604-26996 — "suggests proximity bias is deeply"
[^c11]: doi-10-48550-arxiv-2604-26996 — "computing cosine similarity between these representations therefore operationalizes relevance as"
[^c12]: doi-10-48550-arxiv-2604-26996 — "which we hypothesize prevents the model from surfacing situationally relevant signals"
[^c13]: doi-10-48550-arxiv-2604-26996 — "in-batch negatives, which are predominantly semantically unrelated to the query"
[^c14]: doi-10-48550-arxiv-2604-26996 — "reranker recall is upper bounded by retriever’s Recall@k"
[^c15]: doi-10-48550-arxiv-2604-26996 — "supervised dense retrievers exhibit similar degradation on LUCid"
[^c16]: doi-10-48550-arxiv-2604-26996 — "topically distinct sessions relative to the query"
[^c17]: doi-10-48550-arxiv-2604-26996 — "struggle to condition on latent attributes even when"
