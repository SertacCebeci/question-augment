---
description: "A benchmark's redundancy can be read from its embedding clusters: compactness and the share of items near their centroids indicate how far the set can be compressed."
aliases: ["dataset X-ray", "Dataset X-ray", "cluster-geometry redundancy", "benchmark redundancy diagnostic"]
sources: ["arxiv-2601-03272"]
---
# Cluster-geometry redundancy diagnostic

Before a benchmark is compressed, its redundancy can be read from the shape of its embedding clusters. The paper's "Dataset X-ray" reduces this to a few numbers: the mean silhouette of a K-means partition, the share of items within a fixed Euclidean distance of their own centroid, and the share in sparse regions beyond a larger radius. On the 3GPP test set (109,043 items, K = 100, embeddings from the tuned model) the mean silhouette was 0.67, which the authors read as "compact clusters"[^c1]; 68.3% of items lay within 0.5 of their centroids[^c2]; and only 5.2% lay in low-density regions beyond 1.2.[^c3]

The authors read the compactness as "strong evidence of high semantic redundancy," and the mass near centroids as "a large portion of the test set consists of semantically similar or near-duplicate questions."[^c4][^c7] The example given is variants of one question, "What is the cause of RLF during handover?" That reading is the authors', from one benchmark.

The diagnostic then sets the cut. The rule has two branches: where clusters are "compact and well-separated," sampling is aggressive, 10% per distance band;[^c5] where clusters are "diffuse or overlapping," compression is reduced so that about 20 to 30% of items are kept.[^c8] For the 3GPP set the diagnosis "automatically recommends an aggressive compression ratio of" 10:1, and that ratio is the one the compression experiment then used.[^c6]

The mechanism, in my reading: redundancy is operationalized as how tightly items concentrate around cluster centres in one embedding space, and the compression intensity is a function of that concentration. The same benchmark can be cut harder or softer depending on its own geometry, rather than by a fixed ratio. What the geometry measures is the concentration of embeddings, which is a proxy for redundancy, not redundancy itself.

## Limits

- The thresholds (radius 0.5, radius 1.2, five distance bands, 20 to 30% retention for diffuse sets) are stated without derivation. Only the compact branch and its 10:1 output are reported; the diffuse branch is described but not exercised in the sections read.
- The numbers depend on the embedding. These come from one fine-tuned Qwen3-1.7B space; another model would give other silhouette and radius shares, and the text does not test that.
- Geometry is not validated against outcomes. Nothing in the sections read checks whether a high silhouette or a large near-centroid share predicts how much accuracy a compression loses. The only fidelity result is one benchmark at one ratio.
- K is fixed at 100 for the silhouette; no sweep over K is reported.
- "Near-duplicate" is an interpretation drawn from one example, not a measured duplicate rate.

## Related

- [[history-free-test-set-compression]] — the compression whose sampling intensity this diagnostic sets
- [[questioning-diversity]] — the per-item cousin: average pairwise embedding distance among one item's generated questions, where this note is about a whole benchmark's clusters
- [[difficulty-enriched-item-sampling]] — a different selection effect on what a benchmark's items look like; redundancy and difficulty are separate axes of a set

[^c1]: arxiv-2601-03272 — "mean silhouette score of 0.67, indicating well-separated and compact clusters"
[^c2]: arxiv-2601-03272 — "within a Euclidean distance of 0.5 from their respective"
[^c3]: arxiv-2601-03272 — "only 5.2% of samples reside in"
[^c4]: arxiv-2601-03272 — "strong evidence of high semantic redundancy"
[^c5]: arxiv-2601-03272 — "If clusters are compact and well-separated (high redundancy), we perform aggressive sampling"
[^c6]: arxiv-2601-03272 — "automatically recommends an aggressive compression ratio of"
[^c7]: arxiv-2601-03272 — "set consists of semantically similar or near-duplicate questions"
[^c8]: arxiv-2601-03272 — "If clusters are diffuse or overlapping (low redundancy)"
