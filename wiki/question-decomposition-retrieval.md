---
description: "Retrieving for each LLM sub-query and merging the pool widens evidence coverage on multi-hop questions; a reranker scored against the original question then restores precision."
aliases: ["QD-RAG", "decompose-retrieve-rerank", "sub-query retrieval pooling"]
sources: ["doi-10-48550-arxiv-2507-00355"]
---
# Question decomposition for retrieval

A multi-hop question has its evidence spread across several documents, and a single query embedding tends to pull the one passage that is most like the whole question. This pipeline changes the query side of the search. An instruction-tuned LLM splits the question into sub-queries, the retriever runs once for each, the results are merged and deduplicated, and a reranker chooses the passages that reach the generator. The query set is written as Q = {q} ∪ DECOMPOSE(q, p), and the original query is kept on purpose: "where the original query q is always retained to preserve baseline retrieval performance."[^d1]

The sub-queries are fact-seeking. For "Which planet has more moons, Mars or Venus?" the decomposer asks how many moons each planet has, because each such question "is more likely to retrieve a precise, relevant answer" from a self-contained source.[^d2] The bet is on the pool: several focused queries can reach evidence that one broad query misses. The paper's summary is that the candidates from all sub-queries are merged so that they cover distinct aspects of the question, and that this is what "increases the likelihood of retrieving documents that address distinct aspects of the information need."[^d3]

The second stage scores against the original question, not against the sub-queries. The reranker "scores each retrieved document based on its relevance to the original complex query q," so the merged pool is cut by the question as asked, and the sub-queries only widen what can be cut from.[^d4] The authors split the two effects this way: decomposition supplies coverage, and "and reranking restores precision."[^d5]

What was measured. On MultiHop-RAG, retrieval only, decomposition alone gave "+4.4 percentage points on Hits@4 and +2.9 on Hits@10," and reranking alone added "a +7.6 point gain on Hits@4."[^d6] The full pipeline reached "reaching 87.2% Hits@10" and 0.635 MRR@10.[^d7] Those baselines come from the benchmark's own paper, which used other embedders, so the external comparison is between pipelines and not a controlled ablation; the within-paper ablation carries the causal weight.

On HotpotQA the picture is weaker. Decomposition alone "yields only marginal improvements over the naive RAG baseline" in answer F1, from 31.3 to 32.3. Reranking alone reached 32.9, and the combination 35.0.[^d8] On that benchmark the pairing carries the gain, and decomposition by itself does not.

## Limits

- One pair of benchmarks, one dense retriever (bge-large-en-v1.5), one off-the-shelf cross-encoder (bge-reranker-large) and one generator (Qwen2.5-32B-Instruct). The claim that the gains are attributable to decomposition and reranking rests on this single stack.
- Retrieval is the main result. In the sections read, answer-level results appear only for HotpotQA, and the gains there are a few F1 points.
- The paper states its own shortfall: "our approach falls short on MAP@10," against the strongest configuration of the MultiHop-RAG paper.[^d9] The external baseline used "a smaller embedding model" by the authors' own account, so the Hits gain is not a clean embedder-matched result.[^d10]
- Precision is not free. On HotpotQA supporting facts, the combined system has the highest supporting-fact precision, yet its "EM (17.9) and F1 (11.2) compared to RR" are below reranking alone.[^d11] So the pipeline trades one kind of precision for another.
- The decomposer emits about five sub-queries whatever the question needs; see [[fixed-subquery-budget]]. The sections read do not vary that budget, so whether the gain depends on it is untested.
- Sub-query generation samples at temperature 0.8 with top-p 0.8. The sections read report no run-to-run variance.
- The sub-queries feed retrieval only, and no intermediate answers are generated. My reading, not the paper's claim: this is a candidate-pool method, not a sub-question answering loop of the kind in [[self-ask-decomposition]].

## Related

- [[self-ask-decomposition]] — the sub-question loop that interleaves answers; here sub-queries only fill a candidate pool
- [[two-stage-reranking]] — the second stage this pipeline places after the merge, and the cap it inherits from first-stage recall
- [[multi-query-expansion-precision-penalty]] — a multi-query expansion that lost precision where no reranker followed
- [[query-planning-topology]] — parallel sub-queries issued in one pass, the shape this pipeline takes
- [[fixed-subquery-budget]] — how many sub-queries the decomposer is asked to emit

[^d1]: doi-10-48550-arxiv-2507-00355 — "where the original query q is always retained to preserve baseline retrieval performance"
[^d2]: doi-10-48550-arxiv-2507-00355 — "more likely to retrieve a precise, relevant answer"
[^d3]: doi-10-48550-arxiv-2507-00355 — "retrieving documents that address distinct aspects of the information need"
[^d4]: doi-10-48550-arxiv-2507-00355 — "on its relevance to the original complex query q"
[^d5]: doi-10-48550-arxiv-2507-00355 — "and reranking restores precision"
[^d6]: doi-10-48550-arxiv-2507-00355 — "+4.4 percentage points on Hits@4 and +2.9 on Hits@10"
[^d7]: doi-10-48550-arxiv-2507-00355 — "reaching 87.2% Hits@10"
[^d8]: doi-10-48550-arxiv-2507-00355 — "Applying question decomposition (QD) alone yields only marginal improvements over the naive RAG baseline"
[^d9]: doi-10-48550-arxiv-2507-00355 — "our approach falls short on MAP@10"
[^d10]: doi-10-48550-arxiv-2507-00355 — "Despite using a smaller embedding model"
[^d11]: doi-10-48550-arxiv-2507-00355 — "EM (17.9) and F1 (11.2) compared to RR"
