---
description: "The attention a decoder pays to the shortest-path triples of a linearized subgraph, minus what it pays to the rest; a high value marks shortcut reliance that co-occurs with hallucination."
aliases: ["Path Reliance Degree", "PRD", "shortest-path attention share", "path over-reliance"]
sources: ["arxiv-2512-09148"]
---
# Shortest-path attention concentration

In GraphRAG the knowledge reaches the model as a linearized subgraph: triples written into the prompt. Some of those triples lie on the shortest path between the question's entities and the answer's entities, and together they form a minimal reasoning backbone. The measure asks how much of the answer's attention goes to those tokens relative to everything else. The construct is defined as a difference of attention shares: it "measures the difference in attention allocated to shortest path tokens versus all other tokens during answer decoding".[^c1] For each answer token, at each layer and head, raw attention scores are softmaxed over all source positions; the mass landing on the path positions is compared with the mass on the non-path positions, and the difference is averaged over layers, heads and answer tokens.

The reading is directional. "A high PRD indicates that, on average, the decoder assigns a disproportionately large share of attention to shortest path tokens, evidencing path over-reliance".[^c2] A low or negative value means the opposite, a spread of attention over both path and non-path evidence. The motivating failure is what the authors call a deceptive semantic shortcut: "hallucinations occur despite the availability of the complete gold reasoning chain".[^c3] The model latches onto familiar or statistically salient parts of the input rather than traversing the chain. The paper's claim is correlational: "such rigid focus frequently co-occurs with hallucinations".[^c4]

The evidence is one controlled setting. The analysis uses "5,000 examples from the development set" of MetaQA-1hop, and "We use frozen decoder-only language models as base generators", with Llama-2-7b-chat for the empirical analysis.[^c5] On that set, PRD differs significantly between truthful and hallucinated responses, but the association is small.[^c6] The construct is also bounded by its own formula: "PRD is theoretically bounded" in [−1, 1], since each path-attention share lies in [0, 1].[^c7] That bound is a property of the ratio, not evidence about the model.

A structural point follows from the definition. Because the score is a difference of two softmax masses, a fixed share on path tokens means different things when the path has three triples and when it has thirty; the path set is also built from the gold answer entities during subgraph pruning, so the measure depends on how the subgraph was assembled, not only on what the model does. (This is my inference from the definition, not a result the paper reports.)

## Limits

The paper chose single-hop questions on purpose: "We focus on MetaQA-1hop because single-hop questions provide a controlled setting where we can establish clear causal relationships between internal mechanisms and hallucinations".[^c8] The same choice means nothing here is shown for multi-hop reasoning, where the shortest path is no longer a single triple; the authors state that extension is future work.[^c9]

The association is weak on its own. PRD's correlation with the hallucination label is small, and the paper's ablation finds "SAS-only significantly outperforms PRD-only in AUC on both models" (see [[semantic-alignment-score]]).[^c10] PRD is therefore a component of the paper's detector, not a detector by itself.

The analysis does not separate cause from accompaniment. Attention concentration is observed alongside errors; the paper does not report an intervention that redistributes attention and tests whether the output changes. (My observation about the design, not a claim the paper makes.) The truthfulness label is a surface rule, "either exact match or" sufficient token overlap with gold, and PRD inherits whatever that rule misses.[^c11]

## Related

- [[semantic-alignment-score]] — the paired measure: PRD says where attention goes, SAS says whether the answer's representation matches the knowledge it attended.
- [[salience-control]] — the same concern with which evidence a model foregrounds, measured through prompting rather than attention weights.
- [[initial-token-saliency]] — another attention bias that allocates weight by salience rather than relevance.
- [[single-pass-internal-signal-detector]] — the wider family of detectors that read internal signals in one forward pass.

[^c1]: arxiv-2512-09148 — "PRD measures the difference in attention allocated to shortest path tokens versus all other tokens during answer decoding"
[^c2]: arxiv-2512-09148 — "A high PRD indicates that, on average, the decoder assigns a disproportionately large share of attention to shortest path tokens, evidencing path over-reliance"
[^c3]: arxiv-2512-09148 — "Deceptive semantic shortcuts refer to instances where hallucinations occur despite the availability of the complete gold reasoning chain"
[^c4]: arxiv-2512-09148 — "Our empirical experiments show that such rigid focus frequently co-occurs with hallucinations"
[^c5]: arxiv-2512-09148 — "We use frozen decoder-only language models as base generators"
[^c6]: arxiv-2512-09148 — "Both PRD and SAS exhibit statistically significant differences between hallucinated and truthful responses"
[^c7]: arxiv-2512-09148 — "PRD is theoretically bounded"
[^c8]: arxiv-2512-09148 — "We focus on MetaQA-1hop because single-hop questions provide a controlled setting where we can establish clear causal relationships between internal mechanisms and hallucinations"
[^c9]: arxiv-2512-09148 — "provide generalizable insights that can be extended to more complex reasoning scenarios in future work"
[^c10]: arxiv-2512-09148 — "SAS-only significantly outperforms PRD-only in AUC on both models"
[^c11]: arxiv-2512-09148 — "A generation is labeled as truthful if it achieves either exact match or"
