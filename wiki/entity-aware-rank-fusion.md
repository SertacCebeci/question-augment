---
description: "Ranking chunks by shared knowledge-base entities, fused with dense similarity order, gave the best top-rank precision on a specialized lecture corpus and lost on a general one."
aliases: ["ELERAG", "entity-aware RRF", "entity-aware reciprocal rank fusion", "RRF-based entity re-ranking"]
sources: ["arxiv-2512-05967"]
---
# Entity-aware rank fusion

A dense retriever orders passages by how close their embedding lies to the query's embedding. Entity-aware rank fusion adds a second ordering, built from named entities, and merges the two orderings into one. It has three parts.

First, entities are linked, offline for the corpus. Each passage is run through named-entity recognition, and each mention is matched to a knowledge-base identifier, here Wikidata. Among the candidates for a mention, the choice is made by a hybrid score that mixes semantic similarity with popularity. The similarity is computed over the mention's context, "the similarity score considers the whole mention context"[^c1], so it can separate candidates that share a surface form. Popularity is "computed as the inverse of the candidate rank in the list returned by" the knowledge-base API.[^c2] The weight between the two terms "controls the balance between semantic and popularity signals."[^c3]

Second, the query's mentions are linked the same way, and each passage gets an entity score: the overlap between the query's linked entities and the passage's linked entities. The paper's version is recall-oriented, "the recall-oriented overlap between the set of query linked entities"[^c9] and the passage's set, normalised by the query's entity count.

Third, the two rankings, one by dense score and one by entity score, are merged. "The two distinct rankings are then fused using the RRF algorithm"[^c4], and each passage's joint score is the sum over the two lists of one over (K plus its rank in that list). The paper takes K = 60, "the value suggested by the authors of RRF and is a de facto standard."[^c7] The fusion rule is borrowed; what is new here is that one of the two lists is ranked by entity overlap rather than by a lexical score.

The mechanism has one property worth stating. The two lists are "independently ranked according to their dense score (semantic similarity) and their entity score (factual overlap)."[^c5] When a query contains no recognised entity, "the entity matching score evaluates to zero for all candidate chunks."[^c6] The entity list then keeps the dense order and the fused order is the dense order, so the method falls back to the plain dense baseline without a penalty. This follows from the construction; the paper states it as a design feature.

The cost argument is that the heavy work sits in indexing. "ELERAG shifts the heavy computational burden to the offline indexing phase"[^c8], and at query time there is a short NER pass, knowledge-base calls for the query's mentions, and a set intersection. The parts read make this argument in general terms and in complexity notation, and report no measured latency.

## What was measured

On a custom benchmark of 69 questions, built from the transcripts of two Italian university courses[^c17], the paper reports this fusion as the best of its variants on exact match and MRR. "Using the GPT-4o API, we prompted the model to generate three" types of question, with gold answers, and the set was then filtered.[^c15] My reading of the paper's Table 1: exact match 0.565 for the fusion against 0.522 for the dense baseline, 0.536 for a standalone cross-encoder. The text says the cross-encoder variants "scored lower than ELERAG in EM and MRR"[^c12] and sums the result as "achieving the highest scores in key precision metrics (EM, MRR, P@1)."[^c10] In the full pipeline, where an LLM filters the retrieved chunks, exact match was "0.551" against 0.522 for the baseline, the best of the set.[^c13]

The sensitivity to the entity-linking weight is flat. Across the range the exact match stays at the same value, "equals 0.565, while MRR ranges between 0.668 and 0.674)."[^c11]

On the general-domain control, SQuAD-it, the picture reverses. "the performance trend is sharply reversed."[^c18] The cross-encoder configurations reached exact match near 0.777, and "significantly outperforming both the baseline and the entity-based methods (ELERAG EM"[^c19] of 0.672, which is below the dense baseline's 0.693 in the same table. The authors read this as evidence that a generic reranker fits general web text and a domain-adapted signal fits specialised text: "provides strong experimental evidence for our Domain Mismatch hypothesis."[^c20]

## Limits

The custom benchmark is one corpus of 676 chunks, and its questions were produced by an LLM from that corpus. The paper validated them with a second LLM pass and then by the authors as experts, and it states that "standard inter-annotator agreement metrics were not applicable."[^c16] The exact-match gap of 0.043 is, by my arithmetic, about three questions out of 69. The parts read report no significance test, so that gap is not shown to exceed noise.

The method does not win everywhere. At deeper cutoffs the sparse-dense baseline and the standalone cross-encoder keep higher recall, and the paper attributes this to entity linking pulling in "passages discussing related entities or topics."[^c21] The fusion also fell below the dense baseline on the general benchmark, so the claim is about specialised text only.

The domain explanation is the authors' hypothesis, and the design cannot separate it from the dataset. The corpus is custom, its questions are generated, and the general benchmark is a different kind of material on other terms. My inference: the reversal shows that the entity signal and the cross-encoder disagree on these two sets, not which property of the domain causes it.

The sparse-dense hybrid baseline "was exclusively evaluated under" the custom dataset, so the comparison against lexical fusion does not exist on the general benchmark.[^c22] Only one cross-encoder was tested, "mmarco-mMiniLMv2-L12-H384-v1"[^c24], so the cross-encoder side is a single model. The paper says the architecture "could be applied to other languages"[^c23] and gives no test of that.

## Related

- [[two-stage-reranking]] — the cross-encoder this fusion is measured against; both reorder a dense candidate list, one by a learned query-passage score, the other by an entity-overlap score.
- [[unsupported-rationale-query-refinement]] — another reciprocal-rank-fusion retriever, fusing BM25 with a dense retriever rather than an entity signal.

[^c1]: arxiv-2512-05967 — "the similarity score considers the whole mention context"
[^c2]: arxiv-2512-05967 — "computed as the inverse of the candidate rank in the list returned by"
[^c3]: arxiv-2512-05967 — "controls the balance between semantic and popularity signals"
[^c4]: arxiv-2512-05967 — "The two distinct rankings are then fused using the RRF algorithm"
[^c5]: arxiv-2512-05967 — "according to their dense score (semantic similarity) and their entity score (factual overlap)."
[^c6]: arxiv-2512-05967 — "the entity matching score evaluates to zero for all candidate chunks."
[^c7]: arxiv-2512-05967 — "60 is the value suggested by the authors of RRF and is a de facto standard"
[^c8]: arxiv-2512-05967 — "ELERAG shifts the heavy computational burden to the offline indexing phase"
[^c9]: arxiv-2512-05967 — "the recall-oriented overlap between the set of query linked entities"
[^c10]: arxiv-2512-05967 — "achieving the highest scores in key precision metrics (EM, MRR, P@1)."
[^c11]: arxiv-2512-05967 — "equals 0.565, while MRR ranges between 0.668 and 0.674)"
[^c12]: arxiv-2512-05967 — "Cross-Encoder variants scored lower than ELERAG in EM and MRR (both MRR_gold"
[^c13]: arxiv-2512-05967 — "achieving the highest scores in Exact Match (0.551) and MRR (0.622)"
[^c14]: arxiv-2512-05967 — "The resulting benchmark contains 69"
[^c15]: arxiv-2512-05967 — "Using the GPT-4o API, we prompted the model to generate three"
[^c16]: arxiv-2512-05967 — "standard inter-annotator agreement metrics were not applicable"
[^c17]: arxiv-2512-05967 — "constructed from two Italian university courses"
[^c18]: arxiv-2512-05967 — "the performance trend is sharply reversed"
[^c19]: arxiv-2512-05967 — "significantly outperforming both the baseline and the entity-based methods (ELERAG EM"
[^c20]: arxiv-2512-05967 — "provides strong experimental evidence for our Domain Mismatch hypothesis"
[^c21]: arxiv-2512-05967 — "maintain higher Recall@5 and Recall@10 scores, respectively, compared to ELERAG."
[^c22]: arxiv-2512-05967 — "was exclusively evaluated under"
[^c23]: arxiv-2512-05967 — "could be applied to other languages"
[^c24]: arxiv-2512-05967 — "mmarco-mMiniLMv2-L12-H384-v1"
