---
description: "Similarity search across a shared multimodal embedding space can misplace cross-modal items, so retrieval for an audio or video query is first restricted to items of the query's own modality."
aliases: ["modality gap", "same-modality retrieval", "modality-wise search", "modality-wise distance retrieval"]
sources: ["arxiv-2512-20136"]
---
# Modality-wise retrieval

A shared embedding space is meant to let a query in one modality find material in another. Park et al. report that such spaces do not calibrate their cross-modal distances well: "cross-modal distances are not comparably calibrated" (they cite prior work for this).[^c1] The practical consequence they draw is that querying a knowledge base indexed in a different modality, "for instance, a video query against text embeddings", "often yields off-topic neighbors".[^c2]

This is the modality gap, and the paper's remedy is to stop searching across it. The step is to find the items of the same modality as the query and only then lift them to triplets.[^c3] Concretely, query embeddings come from multimodal foundation models for each stream, and the paper's examples are a video model for video and an audio–text model for audio.[^c8] That embedding is searched against an index built over the audio and visual items of the graph, using L2 distance;[^c9] the top-k nearest items are kept, and only those within a distance threshold of the query survive. The construction guarantees that each triplet is linked to at least one audio or visual item,[^c10] so each surviving item can be lifted to the triplets it supports. Where both streams are present, the two query vectors are concatenated and searched once.[^c11]

The contrast the paper draws is with a text-only graph in a shared space. The control removes the cross-modal links that tie triplets to items, converts each triplet to a sentence, and indexes those sentences with a text encoder.[^c4] Its own description of the effect is that modality-wise retrieval alone "reduces mismatched evidence".[^c5] The authors add that the combination with grounded pruning gives the largest gain, and they call the two "complementary and jointly necessary" in the ablation.[^c6]

What transfers, as I read it: the choice of which index a query is compared against is a separate decision from the choice of similarity measure. A question in one modality can be routed to material in that modality, and the routing is a design step that comes before any ranking.

## What was measured

The ablation is on VALOR, with Qwen2.5-Omni as the answering model, and it compares the same pipeline with and without cross-modal linkage. The threshold on distance is set separately for each benchmark, "separately per benchmark as follows", so the cut-off is not a single number carried across tasks.[^c7]

## Limits

- The modality gap itself is cited to prior work and is not measured in this paper. What the paper measures is the effect of restricting the search, in one ablation.
- One benchmark and one answering model for the ablation. The main table does not isolate this step from multi-hop expansion or from pruning.
- The distance threshold is tuned per benchmark, and the appendix's sensitivity sweeps are not part of what I read. Whether a threshold tuned on one benchmark carries to another is not tested.
- Restricting to the query's own modality can exclude evidence that exists only as text and is not linked to any audio or visual item. Whether such evidence matters for these benchmarks is not measured here; this limit is my reading of the mechanism.
- The paper uses modality-specific encoders (a video encoder and an audio–text encoder) that are chosen per stream. Whether the gain depends on those encoders being well aligned to the knowledge items is not tested.
- The evidence is a single ablation score, reported as Model-as-Judge. It does not show how often the same-modality search returns relevant items compared with the cross-modal search.

## Related

- [[grounded-selective-pruning]] — the filter that follows this step and removes what the query does not mention or the answer does not need
- [[text-modality-dominance]] — omni-modal models lean on text when the modalities conflict; a related observation about which modality an answer is built from, though the two are not linked by any measurement here
- [[multi-hop-retrieval-path-difficulty]] — retrieval over linked evidence, where the path through the graph matters as much as the first hop

[^c1]: arxiv-2512-20136 — "cross-modal distances are not comparably calibrated"
[^c2]: arxiv-2512-20136 — "often yields off-topic neighbors"
[^c3]: arxiv-2512-20136 — "we find the items of the same modality as the"
[^c4]: arxiv-2512-20136 — "we remove the cross-modal links L that connect multimodal"
[^c5]: arxiv-2512-20136 — "reduces mismatched evidence"
[^c6]: arxiv-2512-20136 — "Combining both offers the largest gain"
[^c7]: arxiv-2512-20136 — "separately per benchmark as follows"
[^c8]: arxiv-2512-20136 — "we obtain query embeddings with multimodal foundation models"
[^c9]: arxiv-2512-20136 — "using L2 distance in the embedding space"
[^c10]: arxiv-2512-20136 — "guarantees that each triplet in G is linked"
[^c11]: arxiv-2512-20136 — "we form a simple vector concatenation and apply the same search"
