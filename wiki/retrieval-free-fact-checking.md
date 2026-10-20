---
description: "Verifying a natural-language claim from the model's own internal states alone, with no external evidence, so the verdict tracks parametric knowledge rather than retrieved text."
aliases: ["fact-checking without retrieval", "retrieval-free verification", "retrieval-free claim verification", "parametric fact verification"]
sources: ["doi-10-48550-arxiv-2603-05471"]
---
# Retrieval-free fact-checking

A claim can be checked for truth with no retrieval step at all. The paper names this a task of its own: the verification of arbitrary natural language claims, whatever their source, with no external evidence in the loop.[^c1][^c2] The verifier receives the claim alone, runs the model over it once, and reads a score from the model's internal states. The basis of the verdict is stated plainly: "the parametric knowledge encoded within the model M and the internal representations it generates"[^c3] when it processes the claim.

The setting exists because retrieval-based pipelines do something else. A claim is decomposed into atomic facts, evidence is fetched, and an LLM checks the claim's faithfulness to that evidence. The paper's objections are that such pipelines "prioritize retrieved context over the factual knowledge encoded in an LLM"[^c4] and that "Their effectiveness critically depends on retrieval quality, where noisy or irrelevant evidence"[^c5] can produce missed or false detections. The task is therefore set against faithfulness to evidence, not against factual truth in the world.

It also differs from uncertainty estimation. Against retrieval-based verifiers it "targets factual correctness rather than faithfulness to retrieved"[^c6] context; against uncertainty estimation it "evaluates the factuality of arbitrary claims, rather than confidence over a model"[^c7] own generations. A claim written by a person, a web page, or another model can be scored the same way, because the score does not depend on the claim having come from the model.

The signals a verifier may read are "hidden state activations, attention patterns, or output probabilities"[^c8] that arise while the claim is processed. Sampling is excluded: "Sampling-based approaches are unsuitable for claim" verification when the prompt and full generation are not available.[^c9] Among the signals compared, output-probability measures did worse than probes on internal states. The paper's summary is that "logit-based approaches often underperform compared to those that leverage internal model representations."[^c10]

The evaluation is about generalization rather than one benchmark: "we introduce an evaluation framework focused on out-of-domain generalization, spanning 9 datasets"[^c11], covering long-tail entities, human versus model-written claims, multilingual claims, long-form generations and claims from another model. Eighteen methods and three models are compared. On rare entities the paper reports that "supervised and internal signals enable robust hallucination detection" still works.[^c12] Its best detector, INTRA, "matches the Verb+RAG performance in ROC-AUC"[^c13] (a retrieval-augmented verbalized baseline) and is reported to need far less compute: "computational time than the Verb+RAG method, as detailed in Appendix D."[^c14]

A consequence the paper does not spell out: the verdict is one number about the claim, not a pointer to a source, so it cannot show the user what the claim rests on. That is my inference from the design, not a tested property.

## Limits

- The labels are dataset labels, and the paper distrusts part of its own benchmark: "widely used rule-generated datasets are largely"[^c15] saturated, and "we suspect contamination and overfitting at the method design stage."[^c16] Scores on those sets say less than scores on the rest.
- Generalization is a measured claim, not a guarantee. The supervised readouts that do best are exposed to a known failure: "the performance of supervised methods often degrades in out-of-distribution scenarios."[^c17] The paper tests across nine sets; it does not test every kind of claim.
- The multilingual result is thin. "Due to the limited number of observations for many individual languages"[^c18] the paper reports language-level rankings for only five languages, and says the rest are not reliable.
- The long-tail result shows the detectors still separate true from false claims about rare entities. It does not show that a claim the model never encoded gets a correct verdict. What the study measures is agreement with labels, not recovery of missing knowledge; that boundary is my inference.
- The uses the paper proposes, "reward signals during" training or as components "integrated into the generation process,"[^c19] are directions it names, not results it reports.
- Retrieval-free verification needs access to the model's internals for the strongest signals. A black-box model gives only output probabilities, which the paper finds weaker. That contrast is in the paper's table of baselines; I did not check every baseline's access requirement.

## Related

- [[cross-layer-probe-ensemble]] — how the strongest supervised readout combines hidden states across depths
- [[single-pass-internal-signal-detector]] — the same single forward pass over internal signals, applied to VQA and text QA
- [[internal-prober]] — a hidden-state readout for a different target: whether retrieval will help, not whether a claim holds
- [[uncertainty-guided-retrieval-triggering]] — closed-book likelihood used to decide whether to retrieve; the retrieval-free verdict uses an internal signal about the claim itself
- [[semantic-entropy]] — sampling-based uncertainty, which this setting excludes because a bare claim has no generation to resample

[^c1]: doi-10-48550-arxiv-2603-05471 — "We propose the task of fact-checking without retrieval, focusing on the verification of"
[^c2]: doi-10-48550-arxiv-2603-05471 — "arbitrary natural language claims, independent of their source."
[^c3]: doi-10-48550-arxiv-2603-05471 — "the parametric knowledge encoded within the model M and the internal representations it generates"
[^c4]: doi-10-48550-arxiv-2603-05471 — "They prioritize retrieved context over the factual knowledge encoded in an LLM"
[^c5]: doi-10-48550-arxiv-2603-05471 — "Their effectiveness critically depends on retrieval quality, where noisy or irrelevant evidence"
[^c6]: doi-10-48550-arxiv-2603-05471 — "Unlike retrieval-based verifiers, it targets factual correctness rather than faithfulness to retrieved"
[^c7]: doi-10-48550-arxiv-2603-05471 — "Unlike uncertainty estimation, it evaluates the factuality of arbitrary claims, rather than confidence over a model"
[^c8]: doi-10-48550-arxiv-2603-05471 — "such as hidden state activations, attention patterns, or output probabilities that arise when processing the text."
[^c9]: doi-10-48550-arxiv-2603-05471 — "Sampling-based approaches are unsuitable for claim"
[^c10]: doi-10-48550-arxiv-2603-05471 — "logit-based approaches often underperform compared to those that leverage internal model representations."
[^c11]: doi-10-48550-arxiv-2603-05471 — "we introduce an evaluation framework focused on out-of-domain generalization, spanning 9 datasets"
[^c12]: doi-10-48550-arxiv-2603-05471 — "supervised and internal signals enable robust hallucination detection"
[^c13]: doi-10-48550-arxiv-2603-05471 — "While INTRA matches the Verb+RAG performance in ROC-AUC"
[^c14]: doi-10-48550-arxiv-2603-05471 — "computational time than the Verb+RAG method, as detailed in Appendix D."
[^c15]: doi-10-48550-arxiv-2603-05471 — "widely used rule-generated datasets are largely"
[^c16]: doi-10-48550-arxiv-2603-05471 — "we suspect contamination and overfitting at the method design stage"
[^c17]: doi-10-48550-arxiv-2603-05471 — "the performance of supervised methods often degrades in out-of-distribution scenarios"
[^c18]: doi-10-48550-arxiv-2603-05471 — "Due to the limited number of observations for many individual languages"
[^c19]: doi-10-48550-arxiv-2603-05471 — "enable the use of such systems as reward signals during"
