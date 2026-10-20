---
description: "Query-time expansions that led to a correct answer can be folded into document keys, since query and key expansion rank alike; the index then improves with use at no inference cost."
aliases: ["Evolving Retrieval Memory", "ERM", "amortized query expansion", "query-to-key expansion transfer"]
sources: ["arxiv-2602-05152"]
---
# Correctness-gated key evolution

Query expansion in retrieval-augmented generation is stateless. Each expansion is computed for one query and then thrown away, so the system learns nothing across queries and pays the inference cost again every time.[^c1] Evolving Retrieval Memory (ERM) keeps those expansions instead. It writes the ones that proved useful into the document keys of the index, so the next query benefits without any expansion step.

## Mechanism

1. **Equivalence.** If the similarity is bilinear or monotone under additive embeddings, expanding the query with a unit ej ranks documents the same way as adding ej to the key. The paper states this as Proposition 4.1: "Thus expanding queries is equivalent to expanding keys with respect to retrieval ranking under standard similarity operators."[^c2] This is what lets a gain found on the query side be stored on the document side.
2. **Correctness gate.** An expanded query is accepted if either retrieval correctness or generation correctness holds: "The expanded query is accepted if either retrieval correctness or generation correctness holds, preventing ERM from overfitting to a single subsystem."[^c3] Only expansion units from accepted queries are cached.
3. **Selective attribution.** For each retrieved document and each expansion unit, the marginal gain is measured against the original query. A unit is kept for a key only if the gain is positive: "We retain an expansion unit for a given key only if it yields a positive retrieval gain over the original query".[^c4] Scores accumulate in a bounded per-document memory, and the top-x units are added to the key.
4. **Stability.** Expansion embeddings are norm-bounded, and key updates are batched and stop when the marginal benefit falls. The paper proves the key sequence converges (Theorem 4.3), and that accumulated scores converge to the expected gated gain, so the top-x selection settles (Proposition 4.2, under i.i.d. queries and fixed keys).[^c5] The authors' own remark is that the fixed-key assumption is only a snapshot approximation of the real process.[^c6]

## What was measured

On BEIR and BRIGHT, with sparse, open and proprietary retrievers, ERM gave about +46% average nDCG for BM25 and +13–15% for dense retrievers. The largest gains were on reasoning-intensive sets with little lexical overlap, such as Pony (+64–103%).[^c7] End-to-end answer quality also rose, by about +6% for BM25 and +2–4% for dense retrievers (reported in the paper's Table 2 caption). Gains grew as more past queries were available, and ERM stacked on top of several query-expansion methods.

## Limits

- The equivalence holds only for bilinear or monotone similarities under additive composition. It is not a general property of retrievers, and it is not shown for cross-encoders or learned late-interaction scoring.
- The convergence results rest on i.i.d. queries, fixed keys (Proposition 4.2), and norm-bounded expansions. Real query streams drift, and the paper flags the approximation itself.
- The gate needs a verifiable correctness signal (ground-truth retrieval or answer labels). Where none exists, the gate is not defined. The paper does not test noisy or absent correctness labels.
- Reported gains are largest from low baselines (BM25, AoPS up to +2200%), so relative figures overstate the absolute change.
- Evaluation is benchmark-based, so how the method behaves on a live corpus that changes over time was not tested. Whether queries that differ from past ones also benefit is only partly tested (long-tail gains are explained by a mechanism, not isolated).
- That keys saved from expansions amount to "learning to ask" is my inference. The paper shows retrieval gains, not better question formulation.

## Related

- [[cross-retriever-reformulation-gain]] — reformulation gains vary by retriever. ERM's gain is also largest for the weakest retriever, BM25.
- [[corpus-grounded-one-shot-query]] — grounding a query in the corpus is an alternative way to close the query-document gap, done per query rather than stored in the index.

[^c1]: arxiv-2602-05152 — "adaptations are recomputed for each query and discarded thereafter, precluding cumulative learning and repeatedly incurring inference-time cost."
[^c2]: arxiv-2602-05152 — "Thus expanding queries is equivalent to expanding keys with respect to retrieval ranking under standard similarity operators."
[^c3]: arxiv-2602-05152 — "The expanded query is accepted if either retrieval correctness or generation correctness holds, preventing ERM from overfitting to a single subsystem."
[^c4]: arxiv-2602-05152 — "We retain an expansion unit for a given key only if it yields a positive retrieval gain over the original query"
[^c5]: arxiv-2602-05152 — "Theorem 4.3 (Stability of Key Sequences)."
[^c6]: arxiv-2602-05152 — "Remark A.1 (Snapshot approximation)."
[^c7]: arxiv-2602-05152 — "+46% average nDCG improvement for BM25 and +13–15% for dense retrievers."
