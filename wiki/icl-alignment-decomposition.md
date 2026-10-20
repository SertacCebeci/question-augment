---
description: "A prediction can be scored against three references (truth, zero-shot prior, demonstrated mapping); under natural demonstrations the last equals accuracy, under inverted ones they split."
aliases: ["alignment decomposition", "truth prior and prompt alignment", "prior alignment", "prompt alignment"]
sources: ["arxiv-2511-21038"]
---
# ICL alignment decomposition

Accuracy alone cannot say what a few-shot prompt did to a model. A prediction that is correct might be the zero-shot answer that the prompt merely kept, or a new answer the demonstrations installed. The paper's decomposition scores each in-context prediction against three references at once. The first is the truth, which gives ordinary accuracy. The second is the zero-shot prior: the label the same model gives with task instructions and no demonstrations. The third is the prompt-favoured label, which is the true label under natural demonstrations and the inverted label under inverted ones.[^c1]

Each reference gets an agreement rate over the examples where the model returns a label. The paper defines prior alignment, the share of predictions equal to the zero-shot label, and prompt alignment, the share equal to the demonstrated mapping. It glosses the two in one line each: "Prior alignment reveals whether ICL refines or overrides zero-shot behavior." and "Prompt alignment measures agreement with demonstrated mappings."[^c2] Outputs that match no label are set aside as unknown and excluded from the metrics.[^c3]

The decomposition has a built-in identity. "Under natural demonstrations, prompt alignment equals accuracy."[^c4] The demonstrated mapping is the true one, so agreeing with the prompt and being right are the same event. Under inverted demonstrations the identity breaks, and the three references pull apart. This is what makes the decomposition informative: it separates a prompt that moves predictions toward the demonstrated label from a prompt that makes them correct.

Measured on one model, the natural case looks like refinement. "Natural ICL sharpens correct predictions while suppressing errors: refinement rather than replacement."[^c5] Accuracy rises with the number of demonstrations while prior alignment stays comparatively stable, and "Under natural demonstrations, k-shot predictions remain strongly coupled to zero-shot behavior."[^c6] Gains are largest where the zero-shot prior is weakest.[^c7]

The inverted case splits the references. "ICL degrades accuracy and prior alignment as prompt-following increases, but joint alignment remains zero."[^c8] Prompt-following rises, accuracy and prior agreement fall, and the joint event of being correct and following the inverted mapping never occurs. That joint event is the semantic override rate, which the decomposition isolates as its own term. See [[label-semantic-anchor]].

The paper treats the decomposition as a diagnostic. In its words, "Our alignment decomposition provides a diagnostic tool: high prior alignment indicates that ICL will succeed, and attempts to override semantics".[^c9] The idea is that one can read from prior alignment whether a few-shot prompt is likely to help, before the accuracy is known. The paper gives that as a reading of its results, not as a tested predictor.

A reading for asking, which is mine: the three references are three different sources a question can be answered from: what the answerer already believes, what the context says, and what is true. A question's demonstrations can align the answer with any one of them. The decomposition is a way of asking which of the three an answer followed, and it is available only when the answerer's unprompted answer is known.

## Limits

- The main text shows one model in detail: "We analyze in-context learning behavior for LLaMA-3.1-8B-Instruct across eight classification tasks", and "Results for all eight models are provided in Appendix A."[^c10] The breadth of the pattern rests on the appendix, which this reading did not check.
- Prior alignment is only as meaningful as the zero-shot reference. If the zero-shot label is itself wrong, a high prior alignment means the prompt kept an error. The decomposition does not separate a prior that is well-calibrated from one that is merely confident.
- The prompt-favoured reference depends on the mapping being a permutation of labels. For NLI the paper uses a three-label cycle, and the construction does not cover mappings that merge or split labels.
- The metrics are defined on classification with a fixed label set and greedy decoding. Generation, multi-label output, and free-form answers have no single label to align to, so the decomposition does not transfer to them as stated.
- The diagnostic claim (that high prior alignment predicts success) is the paper's stated reading. The text does not report a held-out test of it in the passage read.

## Related

- [[label-semantic-anchor]] — the joint term of this decomposition, and the claim that it stays at zero under inversion.
- [[demonstration-label-consistency]] — the share of demonstrations carrying the query's label, a property of the prompt rather than of the answer; the decomposition measures the answer's agreement with that share.
- [[anchoring-strength]] — a scalar score comparing cues with a prior; the decomposition counts agreements instead and does not produce a threshold.

[^c1]: arxiv-2511-21038
[^c2]: arxiv-2511-21038 — "Prior alignment reveals whether ICL refines or overrides zero-shot behavior."
[^c3]: arxiv-2511-21038 — "are marked as UNK and excluded from metrics."
[^c4]: arxiv-2511-21038 — "Under natural demonstrations, prompt alignment equals accuracy."
[^c5]: arxiv-2511-21038 — "Natural ICL sharpens correct predictions while suppressing errors: refinement rather than replacement."
[^c6]: arxiv-2511-21038 — "Under natural demonstrations, k-shot predictions remain strongly coupled to zero-shot behavior."
[^c7]: arxiv-2511-21038 — "Gains are largest where zero-shot priors are weakest"
[^c8]: arxiv-2511-21038 — "ICL degrades accuracy and prior alignment as prompt-following increases, but joint alignment remains zero."
[^c9]: arxiv-2511-21038 — "Our alignment decomposition provides a diagnostic tool: high prior alignment indicates that ICL will succeed, and attempts to override semantics"
[^c10]: arxiv-2511-21038 — "We analyze in-context learning behavior for LLaMA-3.1-8B-Instruct across eight classification tasks"
