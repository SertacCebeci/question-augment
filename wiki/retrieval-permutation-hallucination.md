---
description: "With identical retrieved documents and gold included, reordering alone flips a RAG generator's answer; the divergence grows in higher layers and can be estimated by clustering final hidden states."
aliases: ["permutation-induced hallucination", "permutation sensitivity in RAG", "Stable-RAG"]
sources: ["openalex-org-w7119233394"]
---
# Retrieval-permutation hallucination

When a retrieval-augmented generator is given the same Top-5 documents, gold document included, merely reordering them can send the model down a different reasoning path and produce an inconsistent answer. The authors call this a permutation-induced hallucination.[^c1] It differs from [[retrieval-order-sensitivity]], where reordering the components of a retrieval query changes which documents come back. Here the retrieved set is fixed and only the reader's input order changes.

## What was measured

The Perturbation Success Rate (PSR) is the share of document-order perturbations that produce a hallucinated result, over 1,000 sampled NQ instances, with the gold document pinned to each position in turn.[^c2] Answers varied substantially across permutations even with the gold document fixed first. The models sometimes ignored it and answered against the evidence, and this happened in short contexts under 1,000 tokens.[^c3]

The authors argue this is neither weak-document noise (the input documents are identical) nor long-context positional bias (Top-5 fits in about a thousand tokens). It is not the position-skew effects catalogued in [[reader-slot-zero-primacy]] or [[mcq-answer-position-bias]] either, since pinning the gold document does not remove it. They attribute it to structural instability in the model's internal reasoning dynamics.[^c4]

## Layer-wise divergence

Across all 5! = 120 orderings, the last-token hidden state before generation was clustered by spectral clustering. The number of clusters of final reasoning states was counted per layer. Trajectories are concentrated in shallow layers, diverge in the middle layers, and diverge more in higher layers. Samples with 10 or more clusters ("sensitive") diverge far more than samples with 1-2 clusters, mainly in the higher layers.[^c5] PCA of per-layer states shows shallow layers with mixed clusters where different answers interleave, and deeper layers with well-separated clusters where points sharing an answer group together.[^c6]

## Use as an uncertainty estimate

The cluster count and membership act as an estimate of generation uncertainty over orderings. The number of clusters K is chosen adaptively by the eigengap of the graph Laplacian.[^c7] Stable-RAG decodes the hidden state nearest each cluster centre to get a candidate answer per reasoning mode. It then aligns the model by DPO-style preference signals toward the consistent, correct candidates. The paper reports gains in accuracy, reasoning consistency, and generalization across datasets, retrievers and input lengths on three QA datasets.[^c8] It also reports the highest SubEM in both original and shuffled document orders on all datasets.[^c9]

## Limits

- The diagnosis (instability in internal reasoning dynamics) rests on hidden-state clustering. Whether the clusters cause the divergent answers or only correlate with them was not tested by intervention; this is my reading.
- The experiments use Top-5 retrieval and open-weight Llama and Qwen models. Larger candidate sets, where 5! enumeration is infeasible, are not what the PSR figure covers.
- The authors state that the method still incurs "non-trivial computational and labeling overhead", although it cuts annotation cost about threefold compared with exhaustive full-permutation decoding.[^c10]
- Layer-wise constraints on intermediate reasoning are left to future work.
- I did not verify the benchmark tables in detail, so the size of the accuracy gains is not restated here.

## Related

- [[retrieval-order-sensitivity]] — order sensitivity on the query side, where the retrieved set itself changes
- [[reader-slot-zero-primacy]] — a position effect of the reader, distinct from permutation instability with the gold fixed
- [[permutation-consistency-training]] — the same invariance objective for option order, trained by RL rather than hidden-state clustering
- [[mcq-answer-position-bias]] — position skew in answer options
- [[pseudo-ensemble]] — aggregating over perturbed views of one input

[^c1]: openalex-org-w7119233394 — "merely reordering them can lead the model to follow entirely different reasoning paths and produce"
[^c2]: openalex-org-w7119233394 — "PSR is computed as the proportion of successful document-order"
[^c3]: openalex-org-w7119233394 — "This reveals a previously underexplored sensitivity to retrieval permutations, even"
[^c4]: openalex-org-w7119233394 — "permutation sensitivity stems from structural instability in the internal reasoning dynamics"
[^c5]: openalex-org-w7119233394 — "while divergence emerges in"
[^c6]: openalex-org-w7119233394 — "in deeper layers the clusters become increasingly"
[^c7]: openalex-org-w7119233394 — "The number of clusters K is determined adaptively via the eigengap of L."
[^c8]: openalex-org-w7119233394 — "Stable-RAG improves answer accuracy, reasoning consistency, and generalization"
[^c9]: openalex-org-w7119233394 — "Our method achieves the highest SubEM scores"
[^c10]: openalex-org-w7119233394 — "and labeling overhead."
