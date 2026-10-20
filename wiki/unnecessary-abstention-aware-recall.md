---
description: "Scoring abstention against the base model's own knowledge, counting correct answers turned into refusals, separates useful abstention from over-conservatism that accuracy and selective accuracy hide."
aliases: ["Hallucination F1", "known-relative precision and recall", "unnecessary abstentions R-", "false insufficiency"]
sources: ["arxiv-2602-02018", "openalex-org-w7203956628"]
---
# Unnecessary-abstention-aware recall

Accuracy ignores abstentions, and selective accuracy (correct among attempted) rewards a model that refuses nearly everything. Altinisik et al. (2026) treat answer-or-abstain as binary classification of whether a question is known to the model, so refusing a question the model could have answered becomes a measurable cost.

## Mechanism

With an oracle for known versus unknown: attempting means predicting "known". A correct attempt is a true positive (C), an incorrect attempt a false positive (X), a correct abstention a true negative (R+), and an abstention on a truly known question a false negative (R-).[^c1] Precision is C over C+X, which is selective accuracy. Recall is C over C+R-, the share of known questions the model actually answers.[^c2]

The oracle is not available for a base model. The authors note the problem disappears when comparing mitigation methods built on the same model: R- is estimated by counting cases the base model answered correctly but the intervention refuses (C to R).[^c3] F1 of P and R is called Hallucination F1.[^c4]

What it exposed: knowledge probing, a refusal-training baseline, reached high precision but raised R- sharply. On Qwen2.5-3B it cut correct answers from 55.5 to 33.5 and recall fell to 60.0, against 85.7 for the self-verification model with similar precision to the base range. Self-consistency sampling was worse still for that model (14.8 correct, recall 26.8), since small models failed to check consistency reliably.[^c5] Knowledge probing also lost recall under distribution shift.[^c6]

## Refusal on answerable retrieval queries

The same event, a refusal on a question whose answer is in the knowledge base, appears in retrieval-augmented answering under the name false insufficiency. A 2026 master's thesis on RAG reliability states the two-sided requirement: "hallucination awareness should not only prevent unsupported answers; it should also avoid unnecessary refusal".[^c7] In the configuration it inspected, which "achieved the strongest overall retrieval coverage among the evaluated configurations",[^c8] the refusal was the same sentence each time, and "the system did not simply fail by hallucinating; instead, it failed by abstaining when an answer should have been produced."[^c9] The thesis gives a cause, that the sufficiency criterion was applied "too conservatively", and that this "may occur when the relevant information is not phrased in a directly extractable form".[^c10]

The count is the same R- as above, but the thesis does not compute it. It reads representative examples from one run by hand, so a rate of refusals on answerable queries is not reported and no oracle for "known" is built. The refusals were not removed by the strongest retrieval setting, so in that thesis retrieval coverage and the refusal rate are separate measurements (my reading).

## Limits

- Recall is relative to the base model's own knowledge, not to the truth. A method cannot be credited for teaching new facts.
- Defining "known" through base-model correct answers on a single greedy answer is a proxy; a question answered correctly by luck counts as known.
- Valid only for questions with gold answers, so for factoid QA here. Open-ended generation has no clean C or X.
- Treating the comparison as fair assumes all methods share the same base model and the same answer extraction.
- The metric weights precision and recall equally; a deployment that prices wrong answers higher than refusals would want a different weighting. That is my inference, not tested.

## Related

- [[selective-abstraction]] — the framing of answering only when confident, whose precision this metric reuses
- [[accuracy-masks-selective-reliability]] — why accuracy alone hides abstention behaviour
- [[abstention]] — the behaviour being scored
- [[stage-level-hallucination-loss-masking]] — the training method evaluated with this metric
- [[evaluation-choices-encode-error-priorities]] — metric choice as a choice of which error to tolerate

[^c1]: arxiv-2602-02018 — "questions predicted unknown by the model and are truly so, thus correctly abstained from"
[^c2]: arxiv-2602-02018 — "Recall, by contrast, measures the fraction of queries that are actually known to the model for which it chooses to answer rather than abstain."
[^c3]: arxiv-2602-02018 — "R− can be estimated by counting instances that were answered correctly by the base model but are refused after applying a mitigation intervention (C → R)."
[^c4]: arxiv-2602-02018 — "We refer to this metric as Hallucination F1."
[^c5]: arxiv-2602-02018 — "smaller Qwen and LLaMA models frequently fail to reliably check consistency"
[^c6]: arxiv-2602-02018 — "KP often attains high precision but suffers a sharp degradation in recall under distribution shift"
[^c7]: openalex-org-w7203956628 — "hallucination awareness should not only prevent unsupported answers; it should also avoid unnecessary refusal"
[^c8]: openalex-org-w7203956628 — "achieved the strongest overall retrieval coverage among the evaluated configurations"
[^c9]: openalex-org-w7203956628 — "the system did not simply fail by hallucinating; instead, it failed by abstaining when an answer should have been produced."
[^c10]: openalex-org-w7203956628 — "This may occur when the relevant information is not phrased in a directly extractable form"
