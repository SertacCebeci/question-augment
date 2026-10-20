---
description: "Retrieval pipelines lose about 20% nDCG@10 when a query is reworded without changing its meaning, neural re-rankers included, so one wording is a fragile measure of an information need."
aliases: ["query variation robustness", "robustness to query variations", "query variability sensitivity", "wording sensitivity of rankers"]
sources: ["doi-10-48550-arxiv-2111-13057"]
---
# Query-variation robustness

Retrieval benchmarks rest on a convention: each information need is written down as one query. The work states the premise directly: "IR benchmarks evaluate the effectiveness of (neural) ranking models based on the premise that a single query is used"[^c1] to stand for the need. Penha, Câmara and Hauff test what happens when that one wording is replaced. They keep the need fixed, generate variants that preserve the query's meaning, and run each variant through the pipeline in place of the original. The pipeline is a BM25 first stage, with neural models re-ranking its top results: "we apply BM25 as a first stage retriever and re-rank the top 100"[^c2] candidates.

The measured effect is a loss. Averaged over the valid variants, the models "become 20.62% and 19.21% less" effective, in nDCG@10, on TREC-DL-2019 and ANTIQUE respectively.[^c3] The loss is broad rather than occasional: for most combinations of variant and ranker the drop is statistically significant, and "no set of query variations improves statistically over using the original query."[^c4] The size of the loss depends on the kind of variant. Misspellings "have the largest effect (with an average drop of 0.25 nDCG@10"[^c5] while "the word ordering has the least effect (with an average drop of"[^c6] nDCG@10 below 0.01 on TREC-DL-2019.

## Where the loss sits

The authors ask whether the first stage is the culprit, since a first stage that retrieves too little would starve the re-ranker. The answer is no, though it is not only the first stage. Re-ranking alone, with variants and the original first stage, still loses: "query variations only for re-ranking they are of 9%. This indicates"[^c7] a smaller drop than the 20% for the full pipeline, and "that not only the first stage retrieval module is not robust to"[^c8] query variations. So the wording sensitivity appears at both stages. My reading is that the first stage changes which candidates reach the re-ranker, and the re-ranker then scores the same candidates differently; the work does not separate these two effects.

A second alternative is that variants pull up unjudged documents, which the benchmark scores as non-relevant. The authors check the top ten and find the share of judged documents rising, so "drops of the retrieval pipelines can not be attributed to unjudged documents being brought up in the ranking by the"[^c9] variants.

## Mitigation by fusion

Combining the rankings from several variants by reciprocal rank fusion narrows the loss: "rank fusion mitigates the decreases in effectiveness of different query variations"[^c10]. It does not reach the original: fusion "does not improve the effectiveness over using the original query."[^c11] The headroom is real but unreachable by a fixed rule. An oracle that picks the best variant for each query would gain "0.08 and 0.06 nDCG@10 points on TREC-DL-2019 and ANTIQUE respectively."[^c12]

The opening evidence was anecdotal: the work notes that the difference between variants "ranking qualities is anecdotally shown in Table 1 for a vanilla BERT model for ranking."[^c13] The systematic result is the contribution, and the authors draw the consequence that collections "should include query variations"[^c14] for a single information need.

## Limits

- Only valid variants enter the averages. The authors judged validity themselves, and "we resort to using only the valid queries as defined by the manual" annotations.[^c15] Generation quality varies a great deal: "largest percentage of invalid query variations: fewer than 38% of"[^c16] the WordNet synonym variants are valid. The averages describe the surviving variants, not all that a user might type.
- One variant per method per query: "single query variation per method which already yields enough"[^c17] data. The drop is measured for one realisation of each category, not over the spread of wordings a given asker could produce.
- Only the four syntax-preserving categories were generated. The semantic ones were left out: "We leave the exploration of query variation generators for"[^c18] gen./specialization and aspect change is future work. A variant that changes the need would test a different question.
- Two collections and seven rankers. Nothing here shows the loss transfers to other collections, to dense first stages, or to newer rankers.
- Effectiveness is measured against the relevance judgments of the original topics. The unjudged check addresses one way those judgments could mislead; whether a reworded query draws relevant but unjudged material in general is my inference, not tested beyond the top ten.
- The study measures ranking loss. It does not measure whether a person who phrases the need differently is served worse, nor whether the generated variants match what people type; the authors frame them as "query modifications that could be generated by humans"[^c19] but check only validity by annotation.

## Related

- [[query-variation-taxonomy]] — the human rewording categories these generators imitate; only the four syntax-preserving ones are tested here.
- [[minimal-edit-prompt-attack]] — the same wording sensitivity in a medical VLM, searched adversarially for answer flips; the variants here are natural and not optimised against the model.
- [[paraphrase-group-hallucination-dispersion]] — spread of answers across paraphrase groups as a consistency measure; the answer-side analogue of this note.
- [[original-query-rescoring-penalty]] — judging a fused set of query variants by the original query, a scoring issue this setup also meets.
- [[prompt-variant-augmentation]] — the training-side response to wording sensitivity; the work proposes evaluation collections with variants rather than training on them.
- [[levels-of-information-need]] — the need the variants are meant to share; the robustness result takes that need as fixed.

[^c1]: doi-10-48550-arxiv-2111-13057 — "IR benchmarks evaluate the effectiveness of (neural) ranking models based on the premise that a single query is used"
[^c2]: doi-10-48550-arxiv-2111-13057 — "we apply BM25 as a first stage retriever and re-rank the top 100"
[^c3]: doi-10-48550-arxiv-2111-13057 — "we see on average that the models become 20.62% and 19.21% less"
[^c4]: doi-10-48550-arxiv-2111-13057 — "no set of query variations improves statistically over using the original query"
[^c5]: doi-10-48550-arxiv-2111-13057 — "have the largest effect (with an average drop of 0.25 nDCG@10"
[^c6]: doi-10-48550-arxiv-2111-13057 — "the word ordering has the least effect (with an average drop of"
[^c7]: doi-10-48550-arxiv-2111-13057 — "query variations only for re-ranking they are of 9%. This indicates"
[^c8]: doi-10-48550-arxiv-2111-13057 — "that not only the first stage retrieval module is not robust to"
[^c9]: doi-10-48550-arxiv-2111-13057 — "drops of the retrieval pipelines can not be attributed to unjudged documents being brought up in the ranking by the"
[^c10]: doi-10-48550-arxiv-2111-13057 — "rank fusion mitigates the decreases in effectiveness of different query variations"
[^c11]: doi-10-48550-arxiv-2111-13057 — "improve the effectiveness over using the original query"
[^c12]: doi-10-48550-arxiv-2111-13057 — "0.08 and 0.06 nDCG@10 points on TREC-DL-2019 and ANTIQUE respectively."
[^c13]: doi-10-48550-arxiv-2111-13057 — "ranking qualities is anecdotally shown in Table 1 for a vanilla BERT"
[^c14]: doi-10-48550-arxiv-2111-13057 — "that IR collections should include query variations"
[^c15]: doi-10-48550-arxiv-2111-13057 — "we resort to using only the valid queries as defined by the manual"
[^c16]: doi-10-48550-arxiv-2111-13057 — "largest percentage of invalid query variations: fewer than 38% of"
[^c17]: doi-10-48550-arxiv-2111-13057 — "single query variation per method which already yields enough"
[^c18]: doi-10-48550-arxiv-2111-13057 — "We leave the exploration of query variation generators for"
[^c19]: doi-10-48550-arxiv-2111-13057 — "query modifications that could be generated by humans"
