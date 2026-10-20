---
description: "Coherence predictors estimate a result list's effectiveness from how similar its top-ranked documents are to each other, and dense embeddings make them competitive for dense retrieval."
aliases: ["retrieval coherency", "spatial autocorrelation predictor", "embedding coherence predictors"]
sources: ["doi-10-48550-arxiv-2310-11405"]
---
# Coherence-based performance prediction

A [[query-performance-prediction]] made after retrieval can read the ranked list the retriever returned, not only the query. Coherence predictors read the similarities among the top-ranked documents and need no relevance judgments. Their premise is that a retriever which separates relevant from non-relevant material should put a cluster of mutually similar documents at the top: "the presence of coherence, as reflected by highly similar documents in" the top of the list is taken to show the retriever's ability to tell relevant from non-relevant.[^c1]

The mechanism starts from the k-by-k matrix W of pairwise similarities among the top-k documents. Three measures from the sparse literature read W.

- *Spatial autocorrelation (AC)* multiplies W by the retrieval scores to get "diffused" scores, then takes the Pearson correlation between the original and the diffused scores. The predictor assumes that "a low correlation between scores of topically-close" documents signals poor retrieval.[^c2] The name comes from spatial statistics; in retrieval the "space" is the similarity graph over the documents (my inference).
- *WAND and WD* treat W as a graph. Edges below the mean similarity are pruned, WAND averages neighbourhood degrees over the pruned graph, and WD is the share of possible edges that are present. Both are read as coherence: "a higher neighbourhood degree and a higher density of" the graph means a more coherent result set.[^c3]

The sparse versions compute similarity from TF-IDF vectors. The change that defines this family is to take the similarities from the retriever's own dense embeddings, so that W lives in the space the ranking was built in. The paper says that no earlier work had "addressed unsupervised predictors using dense embedded representations" for dense retrieval.[^c4] The embedding variants are AC-embs, WAND-embs and WD-embs.

pairRatio is the paper's own addition. Instead of one correlation, it compares the mean similarity of the top block of ranks with the mean similarity of the lower block, split at a threshold τ, and takes the ratio. The motivation is a pair of heatmaps for a best and a worst TREC DL 2019 query, where the worst shows dark, low-similarity cells at high ranks. The authors' words are that "contrast as indicative of query performance".[^c5] The adjusted variant, A-pairRatio, first scales each pairwise similarity by both documents' query scores, and this "better encodes similarity of the query among the pairwise document similarities".[^c6]

The reported gains are relative to the sparse variants of the same predictors. The abstract gives "improved accuracy upon dense retrieval (up to 92% compared to sparse variants" for TCT-ColBERT and 188% for ANCE.[^c7] For TCT-ColBERT on NDCG@10 and MRR@10, the pairRatio variants "outperform not only supervised predictors, but also NQC".[^c8] Across the dense runs the pattern is split by metric: "score-based predictors perform well for MAP@100, while coherence-based predictors" gain on NDCG@10 and MRR@10.[^c9] On BM25 the sparse coherence predictors are weak: "very low for TREC DL datasets".[^c10] The transfer depends on matching the representation to the retriever: "the type of representations from sparse to dense increases the performance of coherence-based predictors across the dense retrieval" settings, "as the updated representations match those of the retrieval" method.[^c11][^c12]

## Limits

- Small query sets. The data are MS MARCO passages with TREC DL 2019 and 2020, "containing respectively 43 and 54 queries".[^c13] Kendall's τ over about fifty queries is noisy, and the paper itself finds that the predictors "don’t differ significantly in all cases".[^c14]
- No predictor wins everywhere. "we see that none of the examined predictors can outperform all" the others across settings.[^c15] For dense retrieval the coherence predictors "is quite" unstable across metrics: they do well on NDCG@10 and MRR@10 and poorly on MAP@100.[^c16]
- Tuning. The cutoff k and the threshold τ are chosen by a coarse grid on the other dataset: "we tune the hyperparameters of each dataset on the other."[^c17] The reported accuracy depends on this cross-tuning, and the paper does not report a fixed setting.
- Score-based predictors remain strong. They "still remain very competitive and outperform supervised predictors", especially for MAP@100.[^c18] The conclusion that changing the representation is "enough to generalise performance" of unsupervised predictors overstates what two retrievers and one corpus show.[^c19]
- Two dense models only (ANCE, TCT-ColBERT) plus BM25. Other dense architectures, learned sparse retrieval and rerankers were not tested (my inference).
- The pairRatio motivation rests on one heatmap pair, two queries (my inference).
- The measure is correlation with effectiveness. The introduction motivates prediction by interventions, "such as asking the user to reformulate the query", but no intervention is tested here.[^c20]

## Related

- [[query-performance-prediction]] — the general task; the existing note covers predictors that read generated or retrieved images, not a ranked list of documents.
- [[query-type-variance-in-qpp]] — the same paper's analysis of how much the query's type, rather than the predictor, moves its accuracy.

[^c1]: doi-10-48550-arxiv-2310-11405 — "the presence of coherence, as reflected by highly similar documents in"
[^c2]: doi-10-48550-arxiv-2310-11405 — "a low correlation between scores of topically-close"
[^c3]: doi-10-48550-arxiv-2310-11405 — "a higher neighbourhood degree and a higher density of"
[^c4]: doi-10-48550-arxiv-2310-11405 — "addressed unsupervised predictors using dense embedded representations"
[^c5]: doi-10-48550-arxiv-2310-11405 — "contrast as indicative of query performance"
[^c6]: doi-10-48550-arxiv-2310-11405 — "better encodes similarity of the query among the pairwise document similarities"
[^c7]: doi-10-48550-arxiv-2310-11405 — "improved accuracy upon dense retrieval (up to 92% compared to sparse variants"
[^c8]: doi-10-48550-arxiv-2310-11405 — "predictors outperform not only supervised predictors, but also NQC"
[^c9]: doi-10-48550-arxiv-2310-11405 — "score-based predictors perform well for MAP@100, while coherence-based predictors"
[^c10]: doi-10-48550-arxiv-2310-11405 — "very low for TREC DL datasets"
[^c11]: doi-10-48550-arxiv-2310-11405 — "the type of representations from sparse to dense increases the performance of coherence-based predictors across the dense retrieval"
[^c12]: doi-10-48550-arxiv-2310-11405 — "as the updated representations match those of the retrieval"
[^c13]: doi-10-48550-arxiv-2310-11405 — "containing respectively 43 and 54 queries"
[^c14]: doi-10-48550-arxiv-2310-11405 — "they don’t differ significantly in all cases"
[^c15]: doi-10-48550-arxiv-2310-11405 — "we see that none of the examined predictors can outperform all"
[^c16]: doi-10-48550-arxiv-2310-11405 — "the performance of dense representation coherence-based predictors is quite"
[^c17]: doi-10-48550-arxiv-2310-11405 — "we tune the hyperparameters of each dataset on the other"
[^c18]: doi-10-48550-arxiv-2310-11405 — "still remain very competitive and outperform supervised predictors"
[^c19]: doi-10-48550-arxiv-2310-11405 — "some further modifications is enough to generalise performance"
[^c20]: doi-10-48550-arxiv-2310-11405 — "may facilitate interventions, such as asking the user to reformulate the query"
