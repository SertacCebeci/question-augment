---
description: "A predicted specificity score sets each unit's radius in a hyperbolic ball, putting general concepts near the center and specific facts near the edge; reported QA gains are small."
aliases: ["hyperbolic depth", "hierarchical depth embedding", "Poincaré radial depth", "hyperbolic hierarchy embedding", "radius as specificity"]
sources: ["arxiv-2511-18808"]
---
# Radial depth as specificity

In a hyperbolic embedding, distance from the origin can carry a hierarchy. General concepts sit near the center and specific facts near the boundary, so one space holds both a broad topic and the narrow mechanisms under it. Flat Euclidean embeddings have no such axis: similarity is the only geometric relation, and a broad node can sit as close to many queries as a specific one. The HyperbolicRAG paper states the failure in retrieval terms: "This behavior arises from the hubness inherent in high-dimensional Euclidean embedding spaces,"[^c1] and the result is that "causing retrieval to disproportionately favor high-frequency, generic nodes."[^c2] The concept under study is the use of a radial coordinate as an explicit measure of specificity, so that retrieval can tell a general node from a fine-grained one by where it sits.

## Mechanism

The depth is produced per text unit, by a learned module. The paper's depth predictor assigns each element "a scalar specificity score that determines its" place.[^c3] The unit's Euclidean embedding is first enriched with hierarchical cues. The predicted depth then rescales its norm, "assigning smaller norms to more generic concepts and larger norms to more fine-grained evidence."[^c4] The rescaled vector is mapped into the Poincaré ball by the exponential map. The stated reason for the geometry is that hyperbolic space expands with radius, so "the exponential expansion of hyperbolic space accommodates large and deep hierarchies."[^c5]

Retrieval then runs on these positions. The paper's claim is that a specific query activates specific nodes near the boundary, and that propagation from them stays focused, where a flat space would "spread over general subgraphs" under graph propagation.[^c6] The radial score is also not used alone. Retrieval is run in a Euclidean and a hyperbolic space, and the two rankings are combined by mutual-ranking fusion, under which "A mutual-ranking fusion then favors passages consistently ranked high" in both.[^c7] The fusion is a separate design choice from the depth itself; the ablation below separates them only partly.

## What was measured

On the multi-hop benchmarks the margin over the strongest structured baseline is small. Against HippoRAG2 the retrieval results read "(92.1% vs. 90.4%) and MuSiQue (76.2% vs. 74.7%)" for 2Wiki and MuSiQue.[^c8] End-to-end, the average is 51.4% EM against HippoRAG2's "HippoRAG2 (51.0% / 62.7%)".[^c9] Removing the hyperbolic ranking drops MuSiQue to 74.7%, and removing the Euclidean ranking drops it to 73.9%, against the complete system's "overall performance (76.2%, 91.1%, and 96.3%)".[^c10] The paper also reports that the same hierarchical layer "yields higher Passage Recall@5 compared with their Euclidean counterparts" across four dense encoders.[^c11]

## Limits

- The depth is predicted, not measured. The slices I read do not show that the learned radius tracks a human judgement of specificity; calling it specificity is the authors' naming. Whether it does is not tested here (my inference from the design).
- The hubness that the geometry is meant to correct is asserted from the geometry and illustrated with one query in the introduction. The slices I read give no count of hub nodes in any corpus, so the evidence for the mechanism is downstream QA only.
- The gains are one to two points, and the sweep over curvature finds that "c has minimal influence on retrieval performance."[^c12] The 2Wiki figure is 92.1 in the retrieval discussion and 91.1 in the ablation; the slices I read do not say which metric each table uses, and I did not resolve the difference.
- Graph construction bounds everything: "Inaccurate or incomplete extraction of entities and relations may introduce noise and fragmentation."[^c13]
- Only the Poincaré ball was used, though the paper says "it is also compatible with other hyperbolic models."[^c14] Those alternatives were not run.
- The work measures an LLM answerer reading retrieved passages. It does not test whether matching the grain of a question to the grain of its evidence helps when a person formulates the question. Carrying the mechanism over to asking is my inference, not the paper's claim.

## Related

- [[hubness-in-neural-metrics]] — the same hub geometry, found in evaluation metrics; here it is the retrieval side of that phenomenon.
- [[hierarchical-retrieval-interfaces]] — also lets the retriever choose a grain, coarse to fine, but by exposing separate tools rather than by the geometry of one index.

[^c1]: arxiv-2511-18808 — "This behavior arises from the hubness inherent in high-dimensional Euclidean embedding spaces"
[^c2]: arxiv-2511-18808 — "causing retrieval to disproportionately favor high-frequency, generic nodes"
[^c3]: arxiv-2511-18808 — "a scalar specificity score that determines its"
[^c4]: arxiv-2511-18808 — "assigning smaller norms to more generic concepts and larger norms to more fine-grained evidence"
[^c5]: arxiv-2511-18808 — "the exponential expansion of hyperbolic space accommodates large and deep hierarchies"
[^c6]: arxiv-2511-18808 — "leading graph propagation (PPR) to spread over general subgraphs"
[^c7]: arxiv-2511-18808 — "A mutual-ranking fusion then favors passages consistently ranked high"
[^c8]: arxiv-2511-18808 — "(92.1% vs. 90.4%) and MuSiQue (76.2% vs. 74.7%)"
[^c9]: arxiv-2511-18808 — "HippoRAG2 (51.0% / 62.7%)"
[^c10]: arxiv-2511-18808 — "overall performance (76.2%, 91.1%, and 96.3%)"
[^c11]: arxiv-2511-18808 — "yields higher Passage Recall@5 compared with their Euclidean counterparts"
[^c12]: arxiv-2511-18808 — "c has minimal influence on retrieval performance"
[^c13]: arxiv-2511-18808 — "Inaccurate or incomplete extraction of entities and relations may introduce noise and fragmentation"
[^c14]: arxiv-2511-18808 — "it is also compatible with other hyperbolic models"
