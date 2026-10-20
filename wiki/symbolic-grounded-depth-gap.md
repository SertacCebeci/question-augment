---
description: "Deeper multi-hop chains over a concept graph are realized in text less reliably: in SciNets, diversity-enforced paths dropped 40.5% against 4.5% for shortest paths."
aliases: ["Drop Rate", "Alignment Frontier", "grounding drop rate", "path fracture", "symbolic-to-grounded depth loss"]
sources: ["arxiv-2601-09727"]
---
# Symbolic-grounded depth gap

A multi-hop chain can be found in a graph and still fail to become a sentence. Dubey (2026) builds a query-local directed concept graph from a small literature corpus, enumerates paths between query concepts, and then asks a language model to write each selected path out as a causal explanation. Two lengths are kept for each query. Symbolic Depth is the length of the path found in the graph; Grounded Depth is "the realized causal chain length in natural language".[^c1] The Drop Rate is the loss between the two, defined as "the proportional loss between the symbolic and grounded reasoning depths".[^c2] A drop near 0 means the written explanation keeps the depth of the path; a drop of 1.0 means no grounded realization was produced.

The design separates the two stages on purpose. "Graph traversal and path selection are executed deterministically under fixed decoding settings," and natural language realization is applied only after path selection.[^c3] The gap therefore sits at realization: the path is fixed before the language model writes, and the model may fail to write it. Strategies that ask for longer or more varied paths meet this failure more often. Across fourteen queries, the diversity-enforced strategy dropped 40.5% of its depth with a 42.9% failure rate, while shortest-path reasoning dropped 4.5% with no failures. Random walks dropped 81.4% and a retrieval-only language model with no graph dropped 100%.[^c4] The paper calls the set-up an "Alignment Frontier": past a certain symbolic depth the realization stops keeping up.

Per query, the pattern is sharper. On the three queries with the most abstract bridges (Q3, Q4, Q5) the symbolic depths were 3.4 to 4.0 and the grounded depths were 0.0, with a drop rate of 1.0. The paper's reading is that "symbolic chains are identified, but grounded realizations fail" in these cases.[^c5] Failures concentrate where the path crosses wide structural holes between semantically distant clusters: "the language model lacks the linguistic connective tissue" needed to say the bridge out loud.[^c6] Two queries show the reverse, with grounded depth above symbolic depth, which the paper names grounding amplification.

When no grounded path exists, the system declines rather than writing one. The paper reads this as abstention, and as "signal of structural uncertainty rather than a system malfunction."[^c7] For asking and answering the lesson is a check on realized depth: the number of hops a question or an answer proposes is not the number the text can carry. What transfers from this setting to a single question answered in prose is my inference, not something the paper tests.

## Limits

- The evidence is one author, one system, and fourteen queries for the mechanism comparison (plus six traced queries). The paper's own framing is that it "does not validate scientific truth, establish causality, or claim epistemic certainty."[^c8]
- The graph is noisy by construction. The paper names "the model's inability to independently validate the physical correctness of the extracted relations" as a core limitation, so a path can be deep because an extracted relation is wrong.[^c9]
- The Drop Rate is a ratio of two lengths. The slices read do not state how chain length in prose is counted, so the comparison between strategies depends on a counting rule that is not shown.
- Novelty, feasibility and testability are self-assessed by the model and "not human-assessed", so the paper's quality scores do not bear on the drop measure, and they are not evidence that the realized chains are right.[^c10]
- The gap is domain dependent: the paper finds it "most fragile when the bridge is purely theoretical or analogical."[^c11] The abstract names machine learning, biology and climate science; the slices read report no run with a larger or different realizer.
- Whether the gap is a property of the realizer or of the graph is not separated. The paper does not run the same paths through a human writer.

## Related

- [[ungrounded-reasoning-gap-ratio]] — also a gap between what a trace establishes and what it keeps saying, but measured in tokens after an uncertainty marker rather than in chain length
- [[breadth-depth-hallucination-decomposition]] — splits errors by the stage that catches them; here the stage is path-to-sentence
- [[topology-driven-knowledge-gap-detection]] — structural holes are where this paper's bridges fail; that work treats the same holes as places to search
- [[grounding-answer-dual-axis-audit]] — pairs a localization measure with answer correctness, the same move of reading two measures against each other

[^c1]: arxiv-2601-09727 — "comparing Symbolic Depth (the graph-theoretic chain length identified) to Grounded Depth (the realized"
[^c2]: arxiv-2601-09727 — "The drop rate quantifies the proportional loss between the symbolic and"
[^c3]: arxiv-2601-09727 — "Graph traversal and path selection are executed deterministically under fixed decoding settings."
[^c4]: arxiv-2601-09727 — "leading to a 40.5% drop rate"
[^c5]: arxiv-2601-09727 — "symbolic chains are identified, but grounded realizations fail"
[^c6]: arxiv-2601-09727 — "the language model lacks the linguistic"
[^c7]: arxiv-2601-09727 — "signal of structural uncertainty rather than a system malfunction."
[^c8]: arxiv-2601-09727 — "SciNets does not validate scientific truth, establish"
[^c9]: arxiv-2601-09727 — "inability to independently validate the physical correctness of the extracted relations"
[^c10]: arxiv-2601-09727 — "These values are not human-assessed."
[^c11]: arxiv-2601-09727 — "the bridge is purely theoretical or analogical"
