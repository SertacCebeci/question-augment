---
description: "Scoring a search agent's decision to search as a binary classifier against parametric-only oracle labels, with F1 on the no-search class; always-search scores zero whatever its accuracy."
aliases: ["search-decision F1", "F1dec", "search-invocation F1", "search decision F1 score"]
sources: ["arxiv-2512-16883"]
---
# Search-decision F1

An agent that can answer from its own parameters or call a retriever makes two decisions, and exact-match accuracy blends them into one number: whether the answer is right, and whether the choice to search was right. The AdaSearch paper separates the second and scores it as a binary classification. The class of interest is "no search needed", taken as the positive class.[^c1] The oracle label for a question comes from the same model answering without search: if its parametric-only answer is correct, the question did not need a search.[^c2] Precision and recall of the model's search decisions against these labels give a harmonic mean, which the paper calls the search-decision F1, F1dec.[^c3]

## What the score shows that accuracy does not

An always-search agent never predicts "no search", so its score on the positive class is zero. The paper's Search-R1 baseline is the case: "its F1dec is 0 because the model invokes search for" every query.[^c4] Its exact-match score is nonetheless higher than the adaptive methods', which is the trap the metric is built to expose: "higher EM through its always-search behavior but obtains near-zero F1dec".[^c5] The reverse also holds. A model trained without search access gets "higher F1dec but lower EM due to limited internal knowledge".[^c6]

The paper's claim is that accuracy-only evaluation hides the decision: the F1 reveals "that prior methods often overlook readily available parametric knowledge".[^c7] The score is therefore read as a diagnostic of restraint, next to EM as a measure of result. Neither alone says whether a search agent is adaptive.

## Limits

- **Comparability.** The oracle depends on the evaluated model's own parametric knowledge, so the paper says F1dec "should only be compared" among methods from the same base model.[^c8] A number from one model is not a score for another.
- **The oracle is a sampled proxy.** "Parametric-knowledge" is operationalised as one parametric-only answer being correct, so a lucky guess counts as knowledge (my inference from the definition). The route to the label also differs by method: for a method that never searched the paper scores its final answer, and "If the model invokes search, we generate a separate" parametric answer.[^c9] The label thus depends on which path a method took, which is a comparability issue the paper does not discuss.
- **It scores the decision, not the answer.** An agent that answers without searching on a question the oracle marks as solvable counts as correct even when its own answer is wrong (my inference). Answer quality is a separate axis.
- **Binary verdict.** Each decision is yes or no. The authors name "quantification beyond binary outputs" as a key open direction.[^c10]
- **Cost is outside the metric.** False positives and false negatives weigh equally. Search cost and exposure to noisy content, which motivate the work, are not in F1dec; the paper reports search counts separately (my inference from the definition).
- **Scope.** The metric needs gold answers to define the oracle, so it applies to factoid QA with verifiable answers. The paper's experiments are on such sets, with models "up to 7B parameters" as the largest tested.[^c11]

## Related

- [[search-decision-boundary-misalignment]] — over-search and under-search are the two error types this F1 weighs at once; that note diagnoses them per step.
- [[counterfactual-search-routing-oracle]] — builds its own search-or-not labels from paired traces, a different oracle for the same decision.
- [[ra-f1]] — the same harmonic-mean device, applied to answer-or-abstain policies rather than search decisions.
- [[tokens-per-correctness]] — scores search cost against correctness, the part F1dec leaves out.
- [[dual-path-knowledge-boundary-probing]] — uses the same no-search correctness as a training label rather than as a score.

[^c1]: arxiv-2512-16883 — "we designate “search not needed” as the positive class."
[^c2]: arxiv-2512-16883 — "In both cases, a correct parametric-only answer corresponds to “search not needed”, and an incorrect"
[^c3]: arxiv-2512-16883 — "the resulting binary F1 score as the search-decision"
[^c4]: arxiv-2512-16883 — "its F1dec is 0 because the model invokes search for"
[^c5]: arxiv-2512-16883 — "higher EM through its always-search behavior but obtains near-zero F1dec"
[^c6]: arxiv-2512-16883 — "higher F1dec but lower EM due to limited internal knowledge"
[^c7]: arxiv-2512-16883 — "through an F1-based decision metric, revealing that prior methods often overlook readily"
[^c8]: arxiv-2512-16883 — "among methods post-trained from the same base model."
[^c9]: arxiv-2512-16883 — "If the model invokes search, we generate a separate"
[^c10]: arxiv-2512-16883 — "quantification beyond binary outputs is a key area"
[^c11]: arxiv-2512-16883 — "evaluated models up to 7B parameters."
