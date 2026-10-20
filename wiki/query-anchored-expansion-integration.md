---
description: "How an LLM expansion enters a frozen dense retriever decides whether it helps: encoding query and expansion separately and interpolating keeps the query as an anchor and bounds the expansion's pull."
aliases: ["AnchorQE", "SC-AnchorQE", "integration method for query expansion", "vector-level query expansion integration"]
sources: ["doi-10-48550-arxiv-2608-25521", "arxiv-2511-19349"]
---
# Query-anchored expansion integration

Query expansion has two separable decisions: what text is generated, and how that text enters the query-side representation. Sun and Surdeanu write the generated text as z = G(q) and the retrieval representation as v = I(q, z), so that "integration method I maps the query and saved expansion to the representation used for retrieval."[^c1] Most work varies G. This work holds the saved expansion fixed and varies only I, on a frozen retriever and index.

## Mechanism

Two common routes both lose control of the query. Expansion-only retrieval discards the original query. Text concatenation keeps its tokens but "entangles query and expansion through tokenization, attention, pooling, and truncation," and neither route controls how far generated evidence can move the query vector.[^c2]

AnchorQE encodes the query and the expansion separately, normalizes each, and submits the normalized interpolation (1 − α)q + αz as one vector.[^c3] With α = 0 it returns the query unchanged. Because α does not depend on expansion length, expansion trust becomes an explicit number. When several expansions are mixed, disagreement among them shrinks the mixture's norm and so weakens their joint correction.[^c4]

Two properties are proved. First, under raw dot-product scoring in a shared document space, the single vector ranks documents exactly as weighted CombSUM with weights (1−α, απ₁, …, απ_N). It needs one index request where fusion needs N+1.[^c5] This is a ranking equivalence, not equality of calibrated scores. Second, the angle between the original and expanded vector is at most arcsin(α/(1−α)) for α < 1/2. At α = .10 no expansion, whatever its content, can turn the retrieval direction by more than 6.38 degrees.[^c6] The bound limits influence, not relevance: a wrong expansion can still hurt within it.[^c7]

## What was measured

With the same Qwen3-8B expansions and a frozen BGE retriever, conventional published procedures and development-tuned text re-encoding each fell below the no-expansion baseline in 16 of 20 strategy-benchmark comparisons. AnchorQE at α = .15 beat both baseline and conventional procedure in all 20, with relative gains of .46% to 12.89%.[^c8] So the sign of the expansion's effect changed with integration alone, with no better generator. A sparse-retriever study points the same way at the term level: with BM25 and HyDE expansions, feedback-style selection and weighting of the expansion terms gained "by up to 1.4 points (4.2%)" over the strongest string-concatenation baseline, with the same generator on both sides.[^c14] See [[feedback-term-selection-and-weighting]].

## Calibrating trust without labels

SC-AnchorQE sets α from the first eight unlabeled queries of a stream and then freezes it. It is the product of two ratios. One is the expansion's top-1 retrieval strength relative to the query's. The other is how well the expansion's retrieved top-10 supports the query's retrieved top-10 documents.[^c9] Trust is high only when the expansion retrieves strongly and agrees with the original query's evidence. The rule has no fitted parameters, thresholds or labels.[^c10] The abstract reports that it beat a fixed weight tuned on a development partition by up to 3.81%.[^c11] Calibration costs two probe retrievals per prefix query. After that, each query needs one request.

## Limits

- The evidence is for frozen dense retrievers (BGE and eight other generator-retriever pairings) on TREC-DL, LoTTE and BEIR. Sparse, late-interaction and trained-retriever settings are not tested here.
- The equivalence does not hold for mixed sparse-dense streams, stream-specific score normalization, non-linear fusion, or independently truncated ANN candidate lists.[^c12] A nonlinear max-fusion variant was slightly stronger but cannot be compiled into one vector.
- The prefix rule assumes eight early queries represent the stream. A single stream-level factor can underweight an unusually useful expansion.[^c13] Drift in the stream is not covered by anything I read.
- Whether the anchor helps because the query stays dominant or because the expansion is damped was not separated by anything I read; that reading is mine.
- I read the abstract, method and the main diagnostic; the ablations and the nine-configuration tables were not read in detail.

## Related

- [[cross-retriever-reformulation-gain]] — shows that expansion gains depend on the retriever paradigm; this note shows that for a dense retriever the gain also depends on the integration step.
- [[corpus-grounded-one-shot-query]] — another way to shape what the generated query contains before retrieval.
- [[contrastive-hypothesis-retrieval]] — a hypothesis-driven retrieval design whose expansion text is likewise a candidate for this integration.
- [[feedback-term-selection-and-weighting]] — the sparse BM25 case of the same question: the integration step there is term selection and Rocchio-style weighting over the expansion's terms.

[^c1]: doi-10-48550-arxiv-2608-25521 — "integration method 𝐼 maps the query and saved expansion to the representation used"
[^c2]: doi-10-48550-arxiv-2608-25521 — "entangles query and expansion through tokenization, attention, pooling, and truncation."
[^c3]: doi-10-48550-arxiv-2608-25521 — "We therefore propose AnchorQE, a framework to separately encode the original query and expansion, then interpolate"
[^c4]: doi-10-48550-arxiv-2608-25521 — "disagreement"
[^c5]: doi-10-48550-arxiv-2608-25521 — "However, AnchorQE has one important advantage: it issues only"
[^c6]: doi-10-48550-arxiv-2608-25521 — "no expansion can alter the retrieval"
[^c7]: doi-10-48550-arxiv-2608-25521 — "The bound"
[^c8]: doi-10-48550-arxiv-2608-25521 — "In contrast, AnchorQE at 𝛼 = .15 exceeds the DR baseline and"
[^c9]: doi-10-48550-arxiv-2608-25521 — "the second measures its agreement with evidence retrieved by the"
[^c10]: doi-10-48550-arxiv-2608-25521 — "It has no fitted parameters, thresholds,"
[^c11]: doi-10-48550-arxiv-2608-25521 — "outperforms a fixed weight tuned on a development partition"
[^c12]: doi-10-48550-arxiv-2608-25521 — "It does not apply to mixed sparse–dense streams, streamspecific score normalization, non-linear fusion, or independently"
[^c13]: doi-10-48550-arxiv-2608-25521 — "stream-level factor may give too little weight to an unusually useful"
[^c14]: arxiv-2511-19349 — "by up to 1.4 points (4.2%)"
