---
description: "Logic inertia: a model keeps deducing along a learned chain after its premises contradict, so accuracy on contradiction cases falls to 0.000 while base accuracy stays at 1.00."
aliases: ["persistence along a deductive trajectory under inconsistent premises", "deductive persistence under contradiction"]
sources: ["arxiv-2512-06393"]
---
# Logic inertia

Logic inertia is the tendency of a generative model to keep following a deductive path it has learned even when the premises it reasons from are inconsistent. The authors define it as "tendency to persist along a learned deductive trajectory under inconsistent premises."[^l1] The mechanism they isolate is a missing check, not a missing rule: the model applies its usual deductions without first asking whether the premise set still holds together.

The benchmark makes this measurable. All instances are derived from one canonical rule-based system, and a contradiction variant injects an explicit contradictory fact, "which forces the model to detect inconsistency and halt/reject deduction."[^l2] The paper adopts a conservative semantics: once the premises entail a contradiction, every query is labelled false. A model that keeps its original deductive answers therefore disagrees with the label on at least one query, and instance-level exact match drops to zero: "an untreated model that persists with its original deductive answers disagrees on at" least one query.[^l3]

The pattern is sharp in the untreated baselines. They "stay at 1.000 on the base task and Variant 1," drop "to 0.25–0.295 under essential-rule removal (Variant 2)," and fall to 0.000 under explicit contradiction, which the authors take as "direct evidence of Logic Inertia."[^l4] The collapse is not confined to small models. GPT-4o "resolves only 56.0% of contradiction cases."[^l5] The paper also reports the same shape in BERT, Qwen2/3, TinyLlama and Gemma-3-4B, and it says that a concurrent literature surfaces "closely related failure modes under different terminology."[^l6]

A remedy the paper proposes is a verify-then-deduce trace: "Deductive rules cannot be applied until the model has explicitly validated premise" consistency.[^l7] The point for asking and answering is that the same answer can be right on the base rules and wrong on the contradicted ones, so accuracy on the base split alone does not show whether a model checks its premises.

## Limits

- The benchmark is synthetic and propositional. The authors state that "The benchmark is propositional and synthetic; saturation evidences that the structural prior generalises."[^l8] Nothing here shows the same collapse on open-text premises with ambiguous or partly false statements.
- The contradiction semantics is a choice. The paper "commits to a single conservative contradiction semantics; paraconsistent or priority-based resolution strategies" are out of scope.[^l9] Under another convention a model that keeps deducing might be scored correct, so the 0.000 partly measures disagreement with the label. That reading is my inference from the labelling rule; the paper does not test it.
- The failure reappears under rewrites after a partial fix. A model trained only with SFT and DPO "can achieve perfect accuracy on the original rule formulations yet" drops "from 1.000 to 0.327 on De Morgan variants."[^l10] Consistency under rewording is therefore a separate property from consistency under contradiction.
- The paper's only control for the phenomenon is its own remedy. I have not seen an independent replication in the text read here.

## Related

- [[contextual-inertia]]: my inference, not the paper's claim. That note is about a model holding to its own earlier turns in a multi-turn context. Logic inertia is about a single premise set that contradicts itself, so the two may share a cause but are measured differently.
- [[minimal-edit-belief-revision-benchmark]]: my inference. Its "inertia rate" keeps a pre-edit answer when a new premise demands a change. The shape is similar, but there the premises are consistent and updated, not contradictory.
- [[false-premise-question]]: the answer-side counterpart. A question built on a false premise has the same problem of answering through a premise that does not hold.
- [[contradiction-gate]]: a method-side relative that abstains when a verifier finds a contradiction in the input, rather than trains the check into the model.
- [[invariance-sensitivity-trade-off]]: the cost the paper reports for the invariance penalty it adds against the same family of failures.

[^l1]: arxiv-2512-06393 — "tendency to persist along a learned deductive trajectory under inconsistent premises."
[^l2]: arxiv-2512-06393 — "contradictory fact, which forces the model to detect inconsistency and halt/reject deduction."
[^l3]: arxiv-2512-06393 — "an untreated model that persists with its original deductive answers disagrees on at"
[^l4]: arxiv-2512-06393 — "all models stay at 1.000 on the base task and Variant 1,"
[^l5]: arxiv-2512-06393 — "resolves only 56.0% of contradiction cases."
[^l6]: arxiv-2512-06393 — "surfaces closely related failure modes under different terminology"
[^l7]: arxiv-2512-06393 — "Deductive rules cannot be applied until the model has explicitly validated premise"
[^l8]: arxiv-2512-06393 — "The benchmark is propositional and synthetic; saturation evidences that the structural prior generalises"
[^l9]: arxiv-2512-06393 — "single conservative contradiction semantics; paraconsistent or priority-based resolution strategies"
[^l10]: arxiv-2512-06393 — "drop sharply (e.g., from 1.000 to 0.327 on De Morgan variants) when logically equivalent rules are"
