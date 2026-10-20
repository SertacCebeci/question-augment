---
description: "Zigzag persistence tracks how loops in a sequence of layer-wise attention graphs are born and die when edges are both added and deleted between layers, giving a lifetime summary of attention dynamics."
aliases: ["zigzag persistence", "zigzag filtration", "zigzag persistent homology", "layer-wise attention topology"]
sources: ["arxiv-2601-01552"]
---
# Zigzag persistence of attention graphs

Zigzag persistence is a tool from topological data analysis for a sequence of graphs in which each step may add edges and may also delete them. Samaga, Gonzalez Arroyo and Dey (2026) apply it to a transformer by treating the attention matrix of each layer as a weighted graph, with tokens as vertices and attention weights as edge weights. The sequence of layer-wise attention graphs is then "the sequence of attention matrices as a zigzag" graph filtration.[^c1]

The reason for a zigzag rather than an ordinary filtration is that attention between layers is not monotone. "Unlike a standard filtration, which only allows the addition of new vertices/edges, a zigzag filtration also allows their removals."[^c2] Two tokens strongly attending to each other in one layer may stop doing so in the next, and an ordinary filtration cannot represent that loss.

## Mechanism

Each layer's attention matrix is averaged over heads, and the top k percentile of its weights become the edges of that layer's graph.[^c3] Consecutive layers are joined through an intermediate graph. Its edge set is the union of the two layers' edges, so the filtration has the shape G_l ⊆ G_l ∪ G_{l+1} ⊇ G_{l+1}. Where an edge is present in both layers, its union weight is "the maximum of the weights of the edge in Gl and Gl+1 if it exists in both graphs."[^c4]

Because the token set is the same at every layer, the vertex set does not change, and the quantity tracked is the loops. The rank of the first homology group, H1, of each graph counts its independent cycles, which the authors read as cyclic attention among tokens.[^c5]

The homology groups at each stage are linked by maps that follow the direction of the inclusions. Such a zigzag module splits into interval modules: "a direct sum of indecomposable interval modules." Each interval is the range of stages over which one class exists, which is its lifetime.[^c6] The collection of intervals can be drawn as a barcode or as a persistence diagram of (birth, death) points. Diagrams are then turned into fixed-length vectors, and the authors use three vectorization schemes "to vectorize the zigzag persistence diagrams" before a classifier is trained on them.[^c7]

## What the authors claim

The core hypothesis is "that factual and hallucinated generations exhibit distinct topological signatures." The reasoning is that stable attention structures persist across layers while the hallucinated case may look different: the authors "posit that hallucinations may manifest as numerous, short-lived, and structurally unstable cycles."[^c8] That is a stated conjecture about what the diagram would show, not a derived result.

Reported results, as the authors give them: the method is said to outperform baselines on several hallucination benchmarks, and to keep much of its accuracy when only the early layers are used. The paper states that hallucinations can be detected "with minimal degradation in accuracy compared to a full-model analysis" from the first 70 percent of layers.[^c9] It also reports "remarkable zero-shot generalization when transferred between different LLM architectures."[^c10] I did not read the result tables in the slices I took, so the sizes of these gains are not stated here.

## Limits

- The authors admit a methodological choice that may hide the signal: "mean-pooling of attention heads to create a single graph per layer," and "it is an important limitation." A single head whose aberrant behaviour causes a hallucination could be diluted in the average.[^c11]
- Cost is named as the main limitation: "the computational cost of computing persistent homology, particularly for long sequences (sentences)."[^c12]
- The scope is attention only. The paper says its approach "is currently blind to procedural failures that may" originate in other components, such as the MLP layers.[^c13]
- The threshold choices (the top-k percentile, and the persistence thresholds in the appendix) are free parameters. I did not read their sensitivity analysis, so I do not claim robustness to them.
- The hypothesis about short-lived cycles is the authors' posited mechanism. The slices I read give no direct test of it, such as inspecting the cycles behind a single example.
- My inference, not the paper's: the construction needs a shared vertex set across the stages. Any sequence of graphs on a common vertex set could in principle use the same zigzag, but the paper does not test that transfer.

## Related

- [[persistent-homology-ill-posedness-detection]] — the same topological toolkit applied to one point cloud of hidden states per layer, using H0 only; here the object is a sequence of attention graphs and the tracked feature is the H1 loop across layers.

[^c1]: arxiv-2601-01552 — "the sequence of attention matrices as a zigzag"
[^c2]: arxiv-2601-01552 — "Unlike a standard filtration, which only allows the addition of new vertices/edges, a zigzag filtration also allows their removals."
[^c3]: arxiv-2601-01552 — "We choose the top k percentile of attention weights to form the edges of the"
[^c4]: arxiv-2601-01552 — "the maximum of the weights of the edge in Gl and Gl+1 if it exists in both graphs"
[^c5]: arxiv-2601-01552 — "rank of the 1-dimensional homology group H1"
[^c6]: arxiv-2601-01552 — "a direct sum of indecomposable interval modules"
[^c7]: arxiv-2601-01552 — "to vectorize the zigzag persistence diagrams"
[^c8]: arxiv-2601-01552 — "posit that hallucinations may manifest as numerous, short-lived, and structurally unstable cycles"
[^c9]: arxiv-2601-01552 — "with minimal degradation in accuracy compared to a full-model analysis"
[^c10]: arxiv-2601-01552 — "remarkable zero-shot generalization when transferred between different LLM architectures"
[^c11]: arxiv-2601-01552 — "mean-pooling of attention heads to create a single graph per layer"
[^c12]: arxiv-2601-01552 — "the computational cost of computing persistent homology, particularly for long sequences (sentences)"
[^c13]: arxiv-2601-01552 — "is currently blind to procedural failures that may"
