---
description: "Each KG triple gets the other triples from its own source chunk attached as context; SFT on these context graphs beat bare-triple SFT on 3- to 5-hop questions in one study."
aliases: ["context graph (CG)", "context-augmented KG supervision", "CG-grounded supervision", "same-chunk context triples", "two-layer context graph"]
sources: ["doi-10-48550-arxiv-2609-12230"]
---
# Same-chunk context supervision

A knowledge graph stores each fact as an isolated triple (head, relation, tail). A model trained on one triple at a time learns the fact but not the neighbourhood it came from. The mechanism studied here supplies that neighbourhood: for each primary triple, the other triples that the extraction pipeline drew from the same source text chunk are attached to it. The authors call the result a context graph (CG), "supporting triples extracted from the same source text chunk to form a context graph (CG)".[^c1] The primary triple stays the target. KG-grounded supervision "uses only the target KG triple or path", while CG-grounded supervision uses the same target together with its supporting triples.[^c2]

The attachment rests on provenance, not on a new retrieval step. Each chunk carries an identifier that every triple extracted from it keeps, so the candidates for a primary triple are the rest of its chunk's triples, "using the shared source-chunk identifier, without introducing" another corpus.[^c3] The candidates are then filtered by similarity. Each triple is written as "head [SEP] relation [SEP] tail", embedded with a biomedical encoder, and compared with the primary triple by cosine similarity; only candidates at or above a threshold stay. "In this work, we set θ = 0.65, based on our preliminary experiments."[^c4] The result has two layers: "The lower layer contains the original primary KG triples, while the upper layer" holds the supporting triples.[^c5]

The measured effect is a gain in higher-hop accuracy after training on one-hop items only. Qwen3-14B is fine-tuned once on KG-grounded one-hop items (KGModel) and once on CG-grounded one-hop items (CGModel), then both are tested on 3-, 4- and 5-hop questions. For Gastroparesis, "For Gastroparesis, CGModel improves over KGModel by 1.98, 2.20, and 2.15 percentage points" on KG-grounded questions, and "On CG-grounded QA, the gains are even larger" at 2.96, 3.31 and 3.79 points.[^c6][^c7] For Diabetes the KG-grounded gains are "over KGModel by 1.59, 2.66, and 2.02 percentage points on KG-grounded QA", with smaller CG-grounded gains.[^c8] The paper reports that every disease, setting and hop length favours CGModel.

The gain is not only a matching of test format. "Importantly, the improvement is observed not only on" the CG-grounded test, where the context is present, but also on the KG-grounded test, where it is absent.[^c9] The authors read this as a change in how the model composes relations: "its ability to compose them across longer reasoning chains".[^c10] Their explanation for the gain is that it "comes from presenting each target fact with richer and more clinically meaningful local context".[^c11] That is their hypothesis. The sections read do not separate which context triples carry the gain.

## Limits

- Two diseases, one extractor, one model. "although we evaluate the framework on two disease settings, Gastroparesis and Diabetes, broader" validation is still needed.[^c14] The triples come from one extraction pipeline, so the same-chunk rule has been tested only where that pipeline chunks text this way.
- Context is restricted to the source chunk. "Finally, context augmentation in this work is limited to supporting triples extracted from the same" chunk.[^c13] The paper does not test context from other chunks or from retrieval. My inference: a chunk boundary can separate a fact from the evidence that bears on it, and the same-chunk rule would miss that evidence. The text does not measure this.
- Synthetic questions. "the datasets are synthetic, some residual ambiguity or generation noise may remain".[^c12]
- Confound. A CG item carries more triples and more text than a KG item. The sections read do not show a control that adds the same number of unrelated triples to a KG item. So "more evidence" and "better composition" are not separated here; this is my reading, not a finding of the paper.
- Threshold. θ = 0.65 was chosen from preliminary experiments. The sections read show no sweep over θ.
- Spread. The gains are between about 1.5 and 3.8 points, one number per cell. The sections read report no variation across training runs, so the size of a gain against run-to-run noise is not established.

## Related

- [[failure-triage-before-repair]] — the repair stage that follows this SFT in the same paper; it targets the one-hop failures that context training leaves behind.
- [[ontology-constrained-triplet-validation]] — checks triples extracted from text before use; this note takes such extracted triples as given and asks what should be attached to each of them.
- [[atomic-sufficiency-for-rl-synthesis]] — another route to multi-hop composition: that note conditions RL on the atomic parts being present, this one conditions SFT on the local neighbours of each fact.

[^c1]: doi-10-48550-arxiv-2609-12230 — "supporting triples extracted from the same source text chunk to form a context graph (CG)"
[^c2]: doi-10-48550-arxiv-2609-12230 — "KG-grounded supervision, which uses only the target KG triple or path"
[^c3]: doi-10-48550-arxiv-2609-12230 — "using the shared source-chunk identifier, without introducing"
[^c4]: doi-10-48550-arxiv-2609-12230 — "In this work, we set θ = 0.65, based on our preliminary experiments."
[^c5]: doi-10-48550-arxiv-2609-12230 — "The lower layer contains the original primary KG triples, while the upper layer"
[^c6]: doi-10-48550-arxiv-2609-12230 — "For Gastroparesis, CGModel improves over KGModel by 1.98, 2.20, and 2.15 percentage points"
[^c7]: doi-10-48550-arxiv-2609-12230 — "On CG-grounded QA, the gains are even larger"
[^c8]: doi-10-48550-arxiv-2609-12230 — "over KGModel by 1.59, 2.66, and 2.02 percentage points on KG-grounded QA"
[^c9]: doi-10-48550-arxiv-2609-12230 — "Importantly, the improvement is observed not only on"
[^c10]: doi-10-48550-arxiv-2609-12230 — "its ability to compose them across longer reasoning chains"
[^c11]: doi-10-48550-arxiv-2609-12230 — "comes from presenting each target fact with richer and more clinically meaningful local context"
[^c12]: doi-10-48550-arxiv-2609-12230 — "the datasets are synthetic, some residual ambiguity or generation noise may remain"
[^c13]: doi-10-48550-arxiv-2609-12230 — "Finally, context augmentation in this work is limited to supporting triples extracted from the same"
[^c14]: doi-10-48550-arxiv-2609-12230 — "although we evaluate the framework on two disease settings, Gastroparesis and Diabetes, broader"
