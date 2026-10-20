---
description: "A cheap first stage returns a wide candidate set, and a costlier model reorders its top items by scoring each query against each candidate; the expense falls on a short list."
aliases: ["reranking", "re-ranking", "second-stage reranking", "neural reranker", "cross-encoder reranking"]
sources: ["arxiv-2512-16236", "arxiv-2512-05430", "doi-10-48550-arxiv-2507-00355", "arxiv-2511-18177"]
---
# Two-stage reranking

Retrieval in search and in retrieval-augmented generation runs in two stages. The first is an "initial, often rapid, retrieval phase that produces an extensive collection of candidate documents."[^c1] The second stage, the reranker, reorders that collection "to show the user the most pertinent results."[^c2] The survey's claim is that this second pass "dramatically improves the overall quality and efficacy" of the system.[^c3] That is a report of the cited work; the text does not measure it.

The split exists for cost. The reranker sees only the short list the first stage kept, so it can afford a heavier model on a small input. The leading neural form is the cross-encoder. Cross-encoders "jointly encode query-document pairs, enabling rich token-level interactions" and "They output a relevance score."[^c4] Because the query and the document pass through the model together, the score cannot be computed once per document and stored. The survey names the price directly: "Efficiency is a key challenge."[^c5]

A late-interaction alternative changes what is computed jointly. It "encodes queries and documents independently," keeping token embeddings and scoring with a maximum-similarity sum over query and document tokens.[^c12] The survey reports that this "allows document precomputation, drastically reducing latency while" the cited method keeps accuracy.[^c6] My reading, not the text's: what is precomputed is exactly the query-document interaction the cross-encoder had, so the speed is bought by removing that interaction.

Generative rerankers take a different route. T5-style models frame the task as text-to-text: "They frame relevance prediction as a text-to-text task."[^c7] The relevance score is then read from the model's generated output rather than from a classification head. Large language models used as rerankers change the output itself: they are effective "where the goal is to produce an ordered document list without explicit relevance scores for individual documents."[^c8] The survey also names a limit of this route: the "issue of context length limitations."[^c9]

A measured case of the second stage comes from a different paper, ArtistMus, not from the survey. On Llama 3.1 8B, placing a BGE reranker after first-stage BM25 passages raised both kinds of question: "Adding a reranker further boosted both factual (+6.8 pp) and contextual (+5.6 pp) performance".[^c13] Retrieval alone moved the two kinds of question very differently, as [[retrieval-gain-by-question-type]] sets out. This is one model on one benchmark, and I have not checked whether the pattern holds for other rerankers.

A second measured case puts the second stage after a pool merged from several sub-queries, with the cross-encoder scoring each candidate against the original question. There the reranker's role is to cut back what [[question-decomposition-retrieval]] widened. On MultiHop-RAG, reranking alone gave "a +7.6 point gain on Hits@4" over naive dense retrieval.[^c15] The authors split the division of labour between the two stages: decomposition supplies coverage, and "and reranking restores precision."[^c14] The measurement is retrieval only, with one cross-encoder, bge-reranker-large, and it is the authors' own ablation, not a test across rerankers.

A third measured case is a cross-encoder placed after a first-stage vector search over SEC filings. Baseline vector retrieval reached "MRR@5 of 0.160 with Recall@5 of 0.50."[^c16] Reranking a short list of 10 down to 5 chunks raised MRR@5 to 0.750, and the paper reports that this "setting achieved MRR@5 of 0.750 (59% absolute improvement) with perfect Recall@5 of 1.00."[^c17] "All reranking settings achieved perfect recall (1.00) compared to baseline recall of 0.50."[^c18] The reranker was "Cohere rerank-english-v3.0 for reranking," and the comparison used "50 questions for cross-encoder reranking evaluation."[^c19][^c20] This is retrieval only, and the answer-level result for it is not reported in the sentences read.

## Limits

The source is a survey. It offers "a structured synthesis of the diverse reranking paradigms"[^c10], and its effectiveness and efficiency claims are reports of cited work. The parts read give no measured gap between first-stage and reranked quality, and no cost ratio between a cross-encoder and a late-interaction model.

My inference, not in the text: a two-stage pipeline caps quality at the first stage's recall. A relevant document the first stage drops is never promoted by the reranker. The survey does not discuss this bound.

The text treats cost as an engineering challenge and does not separate the cost of the first stage from that of the reranker in any measured way.

The SEC-filing measurement rests on one reranker, on 50 questions, and on one setting picked from a grid of parameter pairs. The text read does not say whether that setting was chosen on questions separate from the ones it is scored on. The perfect Recall@5 of the reranked settings says the first-stage cut was not the bottleneck on that set; it does not show that a relevant chunk the first stage dropped would have been promoted. That bound is my inference, not the paper's.[^c18]

## Related

- [[pointwise-pairwise-listwise-ranking]] — the unit of loss and scoring a reranker is built around
- [[knowledge-distillation]] — the survey's route to lighter rerankers
- [[reranker-as-relevance-judge]] — a reranker's score used as a judge rather than as an ordering step
- [[pairwise-judge-over-scalar-reward]] — the pairwise-over-pointwise argument, here for a judge

[^c1]: arxiv-2512-16236 — "initial, often rapid, retrieval phase that produces an extensive collection of candidate documents"
[^c2]: arxiv-2512-16236 — "reorders these candidates to show the user the most pertinent results after an"
[^c3]: arxiv-2512-16236 — "This dramatically improves the overall quality and efficacy of"
[^c4]: arxiv-2512-16236 — "jointly encode query-document pairs, enabling rich token-level interactions"
[^c5]: arxiv-2512-16236 — "Efficiency is a key challenge."
[^c6]: arxiv-2512-16236 — "This allows document precomputation, drastically reducing latency while"
[^c7]: arxiv-2512-16236 — "They frame relevance prediction as a"
[^c8]: arxiv-2512-16236 — "is to produce an ordered document list without explicit relevance scores for"
[^c9]: arxiv-2512-16236 — "issue of context length limitations"
[^c10]: arxiv-2512-16236 — "The survey provides a structured synthesis of the diverse reranking paradigms"
[^c12]: arxiv-2512-16236 — "It encodes queries and documents independently with"
[^c13]: arxiv-2512-05430 — "Adding a reranker further boosted both factual (+6.8 pp) and contextual (+5.6 pp) performance"
[^c14]: doi-10-48550-arxiv-2507-00355 — "and reranking restores precision"
[^c15]: doi-10-48550-arxiv-2507-00355 — "a +7.6 point gain on Hits@4"
[^c16]: arxiv-2511-18177 — "MRR@5 of 0.160 with Recall@5 of 0.50"
[^c17]: arxiv-2511-18177 — "setting achieved MRR@5 of 0.750 (59% absolute improvement) with perfect Recall@5 of 1.00"
[^c18]: arxiv-2511-18177 — "All reranking settings achieved perfect recall (1.00) compared to baseline recall of 0.50"
[^c19]: arxiv-2511-18177 — "Cohere rerank-english-v3.0 for reranking"
[^c20]: arxiv-2511-18177 — "50 questions for cross-encoder reranking evaluation"
