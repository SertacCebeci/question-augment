---
description: "Two sources agreeing while both are uncertain is weaker evidence than agreement under confidence: high entropy plus overlapping top candidates marks a shared, unstable choice to re-examine."
aliases: ["uncertain agreement", "entropy-gated agreement", "suspicious agreement"]
sources: ["arxiv-2512-23765"]
---
# Uncertain agreement

Two models can agree on a next token for different reasons. When both are confident, agreement is ordinary. When both are unsure and still settle on the same plausible candidate, the agreement says less. The paper's motivation is that "errors often arise when both the draft and target models are uncertain but still agree on a plausible token," and that such cases "may reflect not confident correctness, but uncertain agreement."[^c1]

The measured form is a gate on the agreement itself. The paper uses a fast draft model and a stronger target model, with the target verifying the draft's tokens. It computes the [[entropy]] of both distributions and the overlap of their top-5 candidate sets. Its rule is that "When both models have high entropy and strong top-N overlap, EASD rejects the aligned token and resamples from the target distribution."[^c2] The trigger is set so that a step counts as overlapping when "at least four out of the top-5 tokens coincide between the two models."[^c3] The gate uses only the two distributions a verifier already has. It does not add a scorer or a reward model.

The two signals do different work. The ablation on the 32B target isolates draft entropy as the larger one: "With the 32B target, average accuracy drops from 52.89 to 50.85" when the draft-entropy term is removed, which is the largest drop among the single-signal variants.[^c4] Overlap plays a narrower role. The paper calls it a stabilizer: "The overlap term therefore acts as a stabilizer that makes entropy-based rejection more selective."[^c5] Removing overlap alone lowers the 32B average from 52.89 to 51.77. Removing both signals gives 49.36.

The gain also depends on how often the gate fires. The paper reports that "the best results arise when intervention is rare but well-targeted," and that "overly frequent rejection can dilute the effectiveness of resampling."[^c6] So the concept is not "distrust every agreement". It is a narrow class of agreements, under joint uncertainty, that are worth a second look.

For a question-asker or answerer, the transfer is this. Agreement among sources is not automatically confirmation. Before counting it, read it against each source's own uncertainty. Where both are unsure and the candidates coincide, the agreement is where a shared error is most likely to sit. This is a per-step, uncertainty-conditioned version of the worry in [[coincident-failure]], which measures correlated failure across independently produced sources. The two notes share a mechanism, a shared cause that makes agreement uninformative, but they operate at different grains: a whole answer in one case, a single decision in the other.

## Limits

- The paper measures accuracy, not whether the rejected agreed tokens were wrong. The mechanism is argued from the accuracy gains. The paper's own reading is that the flagged set is "a signature that can coincide with systematic mistakes shared across related models,"[^c7] which is a reading and not a measured error rate.
- The reading is tied to same-family pairs. The paper says that "For same-family draft/target pairs, high entropy with strong top-k overlap can indicate" uncertain agreement.[^c8] Whether two unrelated sources, or a human and a model, produce the same signature is not tested here.
- The thresholds carry the method. The paper states that the choice "is critical for the performance of EASD, as they directly determine when the dynamic penalty is applied."[^c9] The entropy threshold is set from a validation set (LIMO) and the overlap threshold is fixed at 0.8. The sweep finds a broad region that works, with "we do not observe sharp performance cliffs,"[^c10] but the region was found on these models and benchmarks.
- The evaluation covers Qwen2.5 draft and target pairs at 7B, 32B and 72B, and reasoning benchmarks (OlympiadBench, MATH500, AIME24, AMC23, GPQA-Diamond, Minerva Math). The paper's limitations say the evaluation "has not yet been extended to broader real-world reasoning scenarios."[^c11]
- The transfer to answering a question in prose, with human or model sources, is this note's inference. The paper contains no such experiment.

## Related

- [[coincident-failure]] — the population-level finding that independently produced sources fail together more than independence predicts; uncertain agreement is the per-decision gate on the same kind of agreement.
- [[entropy]] — the Shannon measure the gate reads on both models' distributions.
- [[cross-model-answer-disagreement-entropy]] — the opposite reading: uncertainty induced by disagreement between answers, where this note reads uncertainty together with agreement.

[^c1]: arxiv-2512-23765 — "errors often arise when both the draft and target models are uncertain but still agree on a plausible token"
[^c2]: arxiv-2512-23765 — "When both models have high entropy and strong top-N overlap, EASD rejects the aligned token and resamples from the target distribution."
[^c3]: arxiv-2512-23765 — "at least four out of the top-5 tokens coincide between the two models"
[^c4]: arxiv-2512-23765 — "With the 32B target, average accuracy drops from 52.89 to 50.85"
[^c5]: arxiv-2512-23765 — "The overlap term therefore acts as a stabilizer that makes entropy-based rejection more selective."
[^c6]: arxiv-2512-23765 — "overly frequent rejection can dilute the effectiveness of resampling"
[^c7]: arxiv-2512-23765 — "a signature that can coincide with systematic mistakes shared across related models"
[^c8]: arxiv-2512-23765 — "For same-family draft/target pairs, high entropy with strong top-k overlap can indicate"
[^c9]: arxiv-2512-23765 — "is critical for the performance of EASD, as they directly determine when the dynamic penalty is applied"
[^c10]: arxiv-2512-23765 — "we do not observe sharp performance cliffs"
[^c11]: arxiv-2512-23765 — "the evaluation has not yet been extended to broader real-world reasoning scenarios"
