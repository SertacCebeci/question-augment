---
description: "A fact changed in an external triple store, with entity images attached, can reach every hop of a multihop answer without editing model weights; the work does not isolate the store's contribution."
aliases: ["non-parametric knowledge editing", "retrieval-based knowledge update", "parameter-free fact update", "dynamic knowledge graph update"]
sources: ["arxiv-2512-00881"]
---
# External graph fact update

A parametric edit writes a new fact into the weights of a language model. A question whose answer needs that fact in the middle of a chain then has to read the change from inside the network, and a single-layer edit fits one hop depth at best (see [[redundant-multilayer-knowledge-editing]]). The alternative in this work keeps the facts outside the model. Its dynamic multimodal knowledge graph "represents knowledge as structured triples (head, relation, tail), where entities are linked with corresponding images, and supports dynamic updates to accommodate evolving knowledge."[^c1] The authors set this against parametric methods: their framework enables "dynamic knowledge updates and retrieval without requiring modification of model parameters".[^c1]

The mechanism for a multihop question is a sequence of reads from the store. The question is decomposed into sub-questions. A visual sub-question is answered by a multimodal retrieval model that encodes the sub-question together with candidate entities and their images from the graph. A reasoning sub-question runs two paths in parallel: a traversal of the graph's relations, and a vision-language model that reads context pulled from the graph. A decision module then picks between the two candidates when they disagree.[^c2] Because each hop is answered from the store, a changed triple is seen at the hop where it is used. That reading is my inference from the design; the work does not test it directly.

The reason to check each hop is that a final answer can hide a stale link. The authors note that "models may occasionally produce the correct final answer while relying on outdated or" incorrect facts.[^c3] An update that changes only the final answer is not enough evidence that the chain was updated. The paper reports an intermediate measure for this reason, and a stricter one than final-answer accuracy.[^c4]

The comparison with the retrieval-augmented in-context method IKE is the closest thing to a measurement of the store route. IKE "maintains relatively stable baseline performance", but "leading to a significant decline in H-Acc as the number of editing rounds increases."[^c5] The proposed framework is reported to outperform the baselines on the all-hop measure, with the largest gains at four and five hops.[^c4]

## Limits

- The store is never ablated. The ablation in the paper removes the linking, retrieval-augmented and decision modules, not the graph itself.[^c6] The gain over IKE and the parametric methods therefore cannot be credited to updatability alone; the backbone, the retrieval model and the decision step all change together.
- The updates are the benchmark's own edits to a fixed set of facts. The authors list the next step as "to support dynamic knowledge updates by incorporating temporal and event-based information", which is not yet done.[^c7]
- The route depends on an LLM decomposition of the question. A weak decomposer degrades the whole system, according to the appendix comparison of decomposition models.[^c8] A wrong sub-question sends the store lookup to the wrong entity regardless of how well the triple is updated.
- Editing an entity's image or name is not the same as editing a relation. Whether the store handles changes to relations as well as to entities is not reported.

## Related

- [[redundant-multilayer-knowledge-editing]] — the parametric counterpart: the same two-hop failure appears when the edit is written into weights
- [[personalization-as-model-editing]] — a weight edit for user preference that fails on paraphrased queries; the store route avoids the weight write altogether
- [[feedback-adaptation-metrics]] — measures how a correction propagates to later queries in a retrieval system, the same question asked of a store update
- [[alias-tolerant-answer-matching]] — the same benchmark's scorer, which decides whether an answer read from the store counts as correct

[^c1]: arxiv-2512-00881 — "dynamic knowledge updates and retrieval without requiring modification of model parameters"
[^c2]: arxiv-2512-00881
[^c3]: arxiv-2512-00881 — "models may occasionally produce the correct final answer while relying on outdated or"
[^c4]: arxiv-2512-00881
[^c5]: arxiv-2512-00881 — "leading to a significant decline in H-Acc as the number of editing rounds increases"
[^c6]: arxiv-2512-00881
[^c7]: arxiv-2512-00881 — "to support dynamic knowledge updates by incorporating temporal and event-based information"
[^c8]: arxiv-2512-00881
