---
description: "An LLM's proposed query terms become useful only after document-frequency checks against the target index; one such grounded BM25 query beat multi-round search agents without reading any results."
aliases: ["SIRA", "corpus-discriminative retrieval action", "DF-filtered query expansion", "expected-response sketch"]
sources: ["doi-10-48550-arxiv-2605-06647"]
---
# Corpus-grounded one-shot query

A question put to a search index can be made good before any answer is seen. Yang et al. (2026) define the idea as compressing multi-round exploratory search into "a single corpus-discriminative retrieval action".[^c1] Their system, SIRA, asks not which terms are relevant to the query but which terms separate the wanted evidence from corpus-level confusers.

## Mechanism

1. The LLM writes an expected-response sketch: concepts, entities and terms likely to appear in relevant evidence but absent from the query. It is a prior, not evidence.[^c2]
2. Each proposed term is checked against corpus statistics, used as a tool call. The filter enforces DF <= tau * |C| (too common, so little IDF weight) and, query-side, DF > 0 (the term exists in the index).[^c3] No answer passages are returned by these checks.
3. A single weighted BM25 call scores the original query plus a weighted filtered expansion.[^c4]
4. Offline, the same LLM also adds to each document search vocabulary the document lacks, filtered the same way.

The claimed reason multi-round agents are weaker: they "compensate for weak retrieval control by learning the corpus through interaction", absorbing snippets and near misses into context, which is costly and noisy.[^c5] SIRA removes that advantage by design and replaces it with index statistics.

## Measured

- Ten BEIR sets: average Recall@10 0.691 vs 0.648 (E5), 0.625 (SPLADE), 0.530 (BM25); NDCG@10 0.572 vs 0.543 (E5).[^c6]
- Largest gains where query and document vocabulary diverge (SciDocs +36% relative to E5).[^c7]
- Grep-style agents on the same LLM backbone reached only 0.280 and 0.253 Recall@10; the authors read this as isolating the retrieval interface, since grep patterns lack document-frequency weighting.[^c8]
- BrowseComp-Wikipedia (232 queries, 25.6M documents): one query reached 9.70% Recall@1 and 36.14% Recall@100, above multi-round Perplexity agents at every budget.[^c9]

## Limits

- An ablation separating the DF filter from enrichment and weighting was not found in the slices read; crediting the filter is the authors' interpretation, and unverified here.
- Strictly one query; the authors say multiple queries could improve results, so this does not show multi-round search is never better.
- The lexical gain depends on BM25 exposing document frequency; transfer to dense-only indexes was not shown.
- Benchmarks are English, public, and probably within LLM parametric knowledge; unfamiliar private corpora were not tested.
- Authors' own benchmark and system; no independent replication.

## Related

- [[cross-retriever-reformulation-gain]] — expansion gains depend on the retriever paradigm; here the lexical one is chosen deliberately
- [[searchwiki-hierarchical-corpus]] — another corpus-structure-aware search design
- [[verification-aware-stopping]] — contrasts with iterative search that decides when to stop

[^c1]: doi-10-48550-arxiv-2605-06647 — "the ability to compress multi-round exploratory search into a single corpus-discriminative retrieval action"
[^c2]: doi-10-48550-arxiv-2605-06647 — "This sketch acts as a retrieval prior, not as evidence."
[^c3]: doi-10-48550-arxiv-2605-06647 — "The filter enforces an upper bound DF ≤ τ · |C|"
[^c4]: doi-10-48550-arxiv-2605-06647 — "score(d) = BM25(qorig , d) + w · BM25(qexp , d),"
[^c5]: doi-10-48550-arxiv-2605-06647 — "the agent compensates for weak retrieval control by"
[^c6]: doi-10-48550-arxiv-2605-06647 — "SIRA achieves the highest average"
[^c7]: doi-10-48550-arxiv-2605-06647 — "+36% relative on SciDocs"
[^c8]: doi-10-48550-arxiv-2605-06647 — "Because the backbone is shared, the gap isolates the retrieval interface"
[^c9]: doi-10-48550-arxiv-2605-06647 — "reaching 9.70% Recall@1, 15.27%"
