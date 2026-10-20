---
description: "Answering a chain that mixes a fact stored in the weights with one given in the context needs both atomic skills; a failure in either fails the composite."
aliases: ["COMP task", "parametric-contextual composition", "complementary parametric and contextual reasoning"]
sources: ["arxiv-2512-01970"]
---
# Complementary reasoning

Some questions cannot be answered from memory alone or from the page alone. Each step of the chain draws on one of two sources: a fact the answerer holds in its weights (parametric knowledge), or a fact supplied in the context in front of it (contextual information). Complementary reasoning is the case where one chain mixes both. The paper's example asks for the occupation of the business partner of a magazine's chief editor. The editor is named only in the context, and the partner's job is a stored fact; the question "requires integrating external information" with what the model already knows.[^c1]

The authors make the composite a conjunction of two atomic skills. "Formally, the capability requirement is a logical conjunction": the composite holds only when the parametric skill and the contextual skill both hold, so "A failure in either atomic skill" fails the composite.[^c2] To keep the two parts separable, the facts are built from synthetic biographies. Real relation names such as spouse are kept, but they are attached to novel entities: "we retain standard real-world relations (e.g., spouse) but instantiate them with novel entities via synthetic biographies."[^c3] The stated aim is to remove contamination from the facts while keeping the real-world semantics.[^c7]

The conjunction predicts that each atomic step can be solved while the chain still fails. In the paper's test, a model trained on both atomic skills separately "exhibits poor transfer to the composite skill", and the authors conclude that "possessing atomic skills does not guarantee their successful integration without further guidance."[^c4] Integration is therefore a skill of its own, not a free consequence of the parts.

The composite is also where memorization and generalization separate. A model trained directly on composite chains "achieves a near-perfect 90% in IID" but "collapses to 18% in Zero-shot", which the authors read as "SFT incentivizes memorizing relational patterns seen during training".[^c5][^c6] A high score on paths the model has seen is therefore weak evidence that it can integrate a new path. The paper tests this with unseen relation paths; a score on familiar chains alone would not show it. This last step is my reading of the numbers, not a separate result of the paper.

## Limits

- The testbed is synthetic: invented entities, biographies, and multi-hop factual chains. The text read does not test the same conjunction on open documents, code or math, where the atomic skills may not split so cleanly.
- The conjunction is the authors' formal definition, used to structure the experiment. What was measured is the drop in scores on unseen paths and the failure of atomic-only training to transfer; that the two atoms are the whole of the composite is assumed, not measured.
- "Zero-shot" here means unseen relational primitives during training, a narrower notion than the general novelty the word suggests. Other kinds of novelty, such as new entities on known paths, are a different test and are not separated in the sections read.
- The numbers come from one model setup. The text read does not report a replication across model families, and it does not compare against prompting-only or retrieval-only answerers.

## Related

- [[context-use-evaluation-axis]] — the parametric versus contextual split as an evaluation axis; a context-conditioned benchmark separates the atoms, while complementary reasoning is the case where both must be used in one chain
- [[parametric-retrieval-internalization]] — moves the retrieval step into the weights; the composite above keeps both sources and asks whether a model can integrate them
- [[atomic-sufficiency-for-rl-synthesis]] — how RL, given the atomic parts, learns to integrate them on unseen paths

[^c1]: arxiv-2512-01970 — "requires integrating external information"
[^c2]: arxiv-2512-01970 — "Formally, the capability requirement is a logical conjunction"
[^c3]: arxiv-2512-01970 — "we retain standard real-world relations (e.g., spouse) but instantiate them with novel entities via synthetic biographies"
[^c4]: arxiv-2512-01970 — "possessing atomic skills does not guarantee their successful integration without further guidance"
[^c5]: arxiv-2512-01970 — "achieves a near-perfect 90% in IID, it collapses to 18% in Zero-shot"
[^c7]: arxiv-2512-01970 — "To remove contamination while preserving real-world generality"
[^c6]: arxiv-2512-01970 — "SFT incentivizes memorizing relational patterns seen during training"
