---
description: "Each gold entity in a static few-shot demonstration is paired with one perturbed wrong mention-type pair, so the prompt shows boundary and type confusions without retrieving examples."
aliases: ["entity-level contrastive demonstrations", "positive-negative entity pairs", "contrastive few-shot demonstrations", "static contrastive demonstrations"]
sources: ["arxiv-2511-19083"]
---
# Entity-level contrastive demonstrations

A few-shot demonstration for named entity recognition usually shows only the gold output: the sentence, then its entities with their types. This construction adds a wrong twin for each gold entity. For every gold mention-type pair, one negative pair is built by perturbing it. The perturbation is drawn at random from four common error types: a boundary change (missing modifiers or a partial name), an incorrect type label, a spurious mention that is absent from the sentence, or the omission of a valid mention.[^c1] The stated purpose is to "guide the model to better distinguish type semantics and boundaries", and the negatives "expose the model to boundary shifts, type confusions, hallucinated mentions, and omissions".[^c2]

The whole demonstration set is one static support set of k examples, shared across domains. Nothing is retrieved per input. The authors draw the consequence directly: "This eliminates the need for retrieval, reduces latency, and enhances robustness in low-resource scenarios".[^c3] The contrast is with retrieval-based few-shot methods, which pick demonstrations from a large labelled pool for each input. The construction still needs labour: the paper says the strategy works "with only a small amount of manually annotated examples".[^c4]

My reading of the mechanism, which the text does not state in these words: a demonstration teaches by contrast. A correct span sitting next to its wrong variant marks the boundary or the type the model must not cross, so the model sees the decision edge and not only the answer. The negatives are built from gold labels, not from the model's own mistakes. They therefore simulate annotation error, and they do not record what this model actually gets wrong. That is the difference from [[negative-rationale-augmentation]], which takes its negatives from the model's own correct answers.

What was measured. The paper's main comparison is between the whole pipeline and few-shot baselines: "KDR-Agent significantly outperforms all few-shot" baselines.[^c5] That comparison confounds the contrastive set with the agents. The one row that isolates the negatives is the ablation on GPT-4o, which removes the entity-level negatives and keeps the positives. The table caption defines the row: "NS represents the entity-level negative contrastive samples".[^c6] Removing them lowers F1 from 79.41 to 78.36 on NCBI, from 71.85 to 70.69 on OntoNotes 5.0, and from 60.87 to 58.99 on Twitter NER-7. The drops are about one point, one point and two points.[^c7]

## Limits

- The negatives are tested in one ablation row, on three of the ten datasets, with one backbone (GPT-4o). The text gives single F1 values with no run-to-run spread, so a one-point drop cannot be set against noise from the text alone.
- The control removes the negatives and nothing else in the set. Whether the same four error types would help if they were drawn from the model's observed errors, rather than from gold, was not tested.
- The perturbations are made to look like annotation errors. Whether they match the errors an LLM makes on unseen text is not measured.
- The construction removes retrieval, not labelling. It needs hand-written examples, and the paper does not compare how many are needed against retrieval over a larger pool at the same cost.
- The ablation shows the negatives help on top of the static positives. It does not show that a static contrastive set beats a well-selected retrieved set; the main table compares against baselines built differently.

## Related

- [[negative-rationale-augmentation]] — negatives there are explanations of why a model's correct item has a wrong option wrong, used in training; here the negatives are gold-derived perturbations placed in the prompt.
- [[demonstration-label-consistency]] — the other side of demonstration choice, which demonstrations carry the query's label; a static set drops the selection step that note studies, and whether a fixed set keeps that label share is not addressed in this text.
- [[typed-error-reflection]] — the same four error types reappear in the second pass, where they serve as the review checklist.

[^c1]: arxiv-2511-19083 — "randomly applying one of four common error types"
[^c2]: arxiv-2511-19083 — "guide the model to better distinguish type semantics and boundaries"
[^c3]: arxiv-2511-19083 — "This eliminates the need for retrieval, reduces latency, and enhances robustness in low-resource scenarios"
[^c4]: arxiv-2511-19083 — "enables in-context NER with only a small amount of"
[^c5]: arxiv-2511-19083 — "KDR-Agent significantly outperforms all few-shot"
[^c6]: arxiv-2511-19083 — "NS represents the entity-level negative contrastive samples"
[^c7]: arxiv-2511-19083 — "Ablation study results on the GPT-4o LLM backbone (F1 score)"
