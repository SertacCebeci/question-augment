---
description: "Structure-then-select compression parses a context into discourse units tied to source indices, keeps query-relevant subtrees within a budget, and restores source order before the model reads it."
aliases: ["structure-then-select", "EDU-based context compression", "LingoEDU context compressor", "discourse-tree context compression"]
sources: ["arxiv-2512-14244"]
---
# Structure-then-select compression

A long input is compressed in two phases. First, the text is parsed into a tree whose nodes are elementary discourse units (EDUs), the minimal spans that each carry one coherent piece of information, and whose edges record discourse links such as elaboration or contrast. The defining constraint is that each node keeps a pointer into the source. The paper describes the tree as one "where each node is strictly anchored to the source via coordinate" pointers.[^c1] The authors credit this anchoring with removing generative error from the tree: the units are "anchored strictly to source indices to eliminate hallucination".[^c2] The index is what is checked; the node's label is generated, but the content that is retained comes from the source span.

Second, the question is used to choose among the nodes. A small reranker scores each node against the query, using the node's generated title and "the representative text snippet from the span".[^c3] Nodes are then taken in score order until a token budget is reached, rather than cutting at a fixed K, because a fixed top-K "neglects token consumption".[^c4] Finally the chosen spans are sorted by their original start index: "The selected spans in C are sorted by their original start indices idstart before concatenation."[^c5] The output is a linear text whose pieces are in source order, so the answering model sees the query-relevant parts with the order of the original restored.

The motivation is a failure the authors attribute to standard retrieval: "A critical failure mode in standard RAG is the loss of discourse coherence when disjoint chunks are".[^c6] Re-ordering by source index is their answer to that. The design is explicit, where the rival family (implicit, latent compression) is not, and the paper says prompt-based compression by a frontier model alone "struggle[s] to effectively compress the context while preserving the original structural relations".[^c7]

What the work measures. In an ablation on node selection, the generator is held fixed (GPT-4.1) and the selection varies: no selection, random nodes at a matched budget, BM25, the generator choosing its own nodes, and the dedicated reranker. "Table 5 demonstrates that our dedicated ranking approach consistently outperforms other strategies."[^c8] The margin over self-selection is modest: "Ours surpasses Self-Sum across most datasets (e.g., +2.2% on HotpotQA, +1.83%".[^c9] On the budget, the paper reports that "increasing k naturally improves performance by incorporating more context;" but lowers the compression rate, and fixes k = 10 as the operating point where "identified nodes capture the vast majority of the task-relevant signal".[^c10]

What survives the move out of documents is the structure of the operation: units that carry their own source coordinates can be selected as units under a budget and then rebuilt in source order without generating new text. What does not survive is the particular tree. The tree here is produced by a trained parser, and the paper says it trained that parser "via a novel human-in-the-loop pipeline to obtain the" training data before supervised fine-tuning.[^c11] The quality of the selection is bounded by the quality of that parse.

## Limits

- The structural evaluation uses the authors' own benchmark, "a manually annotated benchmark comprising 248 documents",[^c12] built by the same group that trained the parser. The downstream gains are reported on several long-context and search tasks, but the parser's error rate on new domains is not reported in the part I read.
- The reranker is a 0.6B open model. The paper's case for it is cost and throughput ("By using a compact model (e.g., 0.6B parameters) rather than large-scale LLM APIs"[^c13]); I did not see a comparison with a stronger reranker at the same budget. That is my reading of the tables, not a finding of the paper.
- "Eliminate hallucination" in the abstract refers to the index format of the tree nodes. It does not show that the answer built on the compressed context is free of error. The downstream claims are separate measurements, and the ablations fix the generator, so the effect of the selection is not isolated across generators.
- The compressed context is relative to a query. A context selected for one question can be right for it and inadequate for another, so the method needs the question at compression time. This makes it unsuitable as a question-independent memory, which the authors do not claim it is.
- Budget choices are tuned on LongBench (k = 10). Whether the same operating point holds for other tasks, or for agent memory, is not tested here. The authors say so: "Future work will extend this paradigm to multi-modal contexts and dynamic agent memory."[^c14]

## Related

- [[dependency-closed-selection]] — both replace per-item relevance top-K with a selection that respects structure among the items; there the closure is over a join graph, here it is a token budget over a discourse tree.
- [[set-level-selection-over-relevance]] — the same complaint about scoring items one by one for relevance; there the missing property is coverage, here it is the coherence that source order restores.
- [[query-relative-token-overflow]] — a compressed context is adequate or overflowed relative to the question, which is why selection here needs the query.
- [[hallucination-onset-compression]] — how far a reference can be truncated before accuracy breaks; a measure of what compression costs, which this method tries to reduce by choosing units rather than cutting tokens.
- [[information-bottleneck]] — the general framing of compression as keeping what bears on a target; the selection here is a query-conditioned version of that idea.

[^c1]: arxiv-2512-14244 — "where each node is strictly anchored to the source via coordinate"
[^c2]: arxiv-2512-14244 — "anchored strictly to source indices to eliminate hallucination"
[^c3]: arxiv-2512-14244 — "representative text snippet from the span"
[^c4]: arxiv-2512-14244 — "To address the limitations of fixed Top-K retrieval (which neglects token consumption)"
[^c5]: arxiv-2512-14244 — "The selected spans in C are sorted by their original start indices idstart before concatenation."
[^c6]: arxiv-2512-14244 — "A critical failure mode in standard RAG is the loss of discourse coherence when disjoint chunks are"
[^c7]: arxiv-2512-14244 — "struggle to effectively compress the context while preserving the original structural relations."
[^c8]: arxiv-2512-14244 — "Table 5 demonstrates that our dedicated ranking approach consistently outperforms other strategies."
[^c9]: arxiv-2512-14244 — "Ours surpasses Self-Sum across most datasets (e.g., +2.2% on HotpotQA, +1.83%"
[^c10]: arxiv-2512-14244 — "identified nodes capture the vast majority of the task-relevant signal"
[^c11]: arxiv-2512-14244 — "we train the LingoEDU via a novel human-in-the-loop pipeline to obtain the"
[^c12]: arxiv-2512-14244 — "a manually annotated benchmark comprising 248 documents"
[^c13]: arxiv-2512-14244 — "By using a compact model (e.g., 0.6B parameters) rather than large-scale LLM APIs"
[^c14]: arxiv-2512-14244 — "Future work will extend this paradigm to multi-modal contexts and dynamic agent memory."
