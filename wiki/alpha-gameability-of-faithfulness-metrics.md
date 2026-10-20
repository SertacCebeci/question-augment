---
description: "A faithfulness metric is alpha-gameable if a model scores alpha with no dependence between explanation mentions and intervention impact; CT is 1-gameable, CCT and phi-CCT are not."
aliases: ["trivial gameability", "alpha-gameability", "counterfactual test gameability"]
sources: ["doi-10-48550-arxiv-2503-13445"]
---
# Alpha-gameability of faithfulness metrics

A counterfactual faithfulness test inserts a word into an input, records whether the model's prediction changes (impact I), and records whether the model's explanation mentions the inserted word (E). Gameability asks whether a metric can be satisfied by an explanation that carries no information about what drove the decision. The work formalizes this: for a metric F built from E and I, if some model reaches score alpha on F with no statistical dependence between E and I, F is alpha-gameable.[^c1]

The Counterfactual Test (CT) deems an explanation unfaithful when an impactful word is not mentioned. A model can pass it by repeating the full input verbatim, which says nothing about which factors matter.[^c2] In the formalization, CT is 1-gameable on all datasets, while the Correlational Counterfactual Test (CCT) is no more than 0-gameable on any dataset.[^c3] The phi-CCT, which replaces the point-biserial correlation with a phi coefficient between binary mention and binary impact, is also no more than 0-gameable and needs no token probabilities.[^c4] Across settings the phi-CCT predicts most of the CCT's variance (R2 = .92), whereas CT predicts it weakly (R2 = .09).[^c5]

The mechanism is that CT equals the true positive rate alone, so it ignores false positives; a correlation needs mentions to be concentrated on impactful words, which forces dependence between E and I.[^c6]

## Limits

- Zero-gameability does not make correlation a clean measure: it remains sensitive to verbosity and to class imbalance in the intervention distribution (see [[verbosity-controlled-faithfulness-auroc]]).
- The tests are explanatory-faithfulness tests on three natural classification datasets with random word insertions; adversarial settings where a model hides its reasoning were not tested.
- The theorems are the work's own; the proofs live in its appendix and I did not read them.

## Related

- [[verbosity-controlled-faithfulness-auroc]] — the metric the same work builds after finding correlation's remaining biases
- [[hint-adherence-without-acknowledgement]] — another test of whether explanations mention what drove behavior
- [[stance-consistency-plus-causal-influence-faithfulness]] — a different composite faithfulness measure
- [[cot-reasoning-faithfulness-by-truncation]] — causal rather than explanatory faithfulness

[^c1]: doi-10-48550-arxiv-2503-13445 — "if there exists a model M achieving score α on F with no statistical dependence between E and I, then we say that F is α-gameable."
[^c2]: doi-10-48550-arxiv-2503-13445 — "a model can achieve 0% CT unfaithfulness via the trivial strategy"
[^c3]: doi-10-48550-arxiv-2503-13445 — "Theorem 1. CT is 1-gameable on all datasets."
[^c4]: doi-10-48550-arxiv-2503-13445 — "Theorem 3. phi-CCT is no more than 0-gameable on any dataset."
[^c5]: doi-10-48550-arxiv-2503-13445 — "CCT is largely predicted by our"
[^c6]: doi-10-48550-arxiv-2503-13445 — "Note that under this framing, CT faithfulness"
