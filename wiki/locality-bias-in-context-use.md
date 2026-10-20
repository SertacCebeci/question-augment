---
description: "Masked diffusion LMs use context by proximity to the masked answer slot: accuracy falls as the relevant example moves away from it, whatever its absolute position in the prompt."
aliases: ["locality bias", "recency bias in masked diffusion models", "distance-to-target effect", "proximity bias"]
sources: ["arxiv-2511-21338"]
---
# Locality bias in context use

A model that answers from a long prompt has to find the part of the prompt that bears on the answer. For autoregressive models the familiar pattern is a U-shape: information at the start or at the end is used well, the middle less so. The masked diffusion paper finds a different shape in its models. In a few-shot setup where relevant examples were mixed with distractors, "highest when relevant information appears immediately before the test question, indicating a significant recency bias."[^l1] Unlike the autoregressive models, which "often display a U-shaped pattern", the masked diffusion models "show a monotonic decline in accuracy as relevant information moves farther away."[^l2][^l3]

The decisive test moves the question, not the evidence. The test question, with its answer masked, is placed at different positions while the examples stay fixed. Performance then tracks the question: the models "prioritise information close to the prediction target," "regardless of its absolute position in the prompt."[^l4] The paper's summary is that the earlier recency effect is "a broader locality bias", and that performance depends on "proximity of relevant information to the masked question, with local information processed more effectively."[^l5] What matters is the distance to the point where the answer is produced, not where the evidence sits in the prompt.

The gradient view gives a different picture for the same models. Attribution by the gradient of the predicted answer's logit with respect to each input embedding shows "the characteristic U-shape associated with both recency and primacy effects across all models."[^l6] The authors also report that masked diffusion models have "more evenly distributed gradient values than ARLMs," which they read as "greater potential for global context utilisation." So the accuracy curve and the attribution curve do not say the same thing about the same model, and the note should not collapse them into one.

The paper's account of the source is a hypothesis. The masked diffusion loss is weighted by 1/p, where p is the masking probability, so "training places greater weight on cases where only few tokens are masked".[^l7] Those are the cases in which nearby context is usually enough, and the authors write: "We hypothesise that this encourages MDLMs to rely on nearby context."[^l8] The weighting is a property of the objective; the claim that it produces the bias was not tested by an ablation in the parts read.

For someone building a question or a prompt, the transfer is this. If the answering model is of this kind, the evidence the answer depends on should sit next to the question, and a long prompt that puts it at the start is not equivalent to one that puts it at the end. (My inference: the paper does not test prompt design.) The same reading also says that moving relevant text closer can help without any change in its content, which is a different lever from the order effect in [[causal-prompt-order-dependence]].

## Limits

- The models are two pairs, LLaDA-8B against Llama3-8B and Dream-7B against Qwen2.5-7B, with LLaDA-MoE in an appendix.[^l13] The claim is about these masked diffusion models; it does not say the same locality holds for every diffusion LM.
- The task is a few-shot rule-learning setup, with "10 relevant examples and 40 distractors".[^l12] It is not open question answering. The paper's reason for leaving needle-in-a-haystack tests is that they are "relatively easy",[^l10] so the setup was chosen to force use of the whole context, and its results may not carry to retrieval-style lookup.
- The paper trains and tests within the context length it was trained on, and says it is "not interested in studying generalisation to larger context lengths".[^l11] Whether locality grows or shrinks at longer lengths is not shown.
- The decoding is greedy throughout: "use greedy decoding for all models we consider."[^l9] Sampled answers may show a different profile.
- The gradient U-shape is an uncomfortable counterpart to the monotonic accuracy decline, and the paper does not reconcile them. Read alone, the accuracy result is the stronger claim about use.
- The source of the bias is the authors' hypothesis from the loss weighting; no run in the parts read isolates it.

## Related

- [[causal-prompt-order-dependence]] — the autoregressive constraint on what each token sees; the contrast with the U-shaped autoregressive curve is the paper's own reference point.
- [[effective-context-length]] — how much of a long context a model uses at all; this note is about where within it the use falls.
- [[mask-token-distraction]] — the generation-time placeholder tokens that the same paper finds to reduce context use further.

[^l1]: arxiv-2511-21338 — "highest when relevant information appears immediately before the test question, indicating a significant recency bias"
[^l2]: arxiv-2511-21338 — "Unlike ARLMs, which often display a U-shaped pattern"
[^l3]: arxiv-2511-21338 — "MDLMs show a monotonic decline in accuracy as relevant"
[^l4]: arxiv-2511-21338 — "regardless of its absolute position in the prompt"
[^l5]: arxiv-2511-21338 — "proximity of relevant information to the masked question, with local information processed more effectively"
[^l6]: arxiv-2511-21338 — "exhibit the characteristic U-shape associated with both recency and primacy effects across all models"
[^l7]: arxiv-2511-21338 — "the masked diffusion loss is scaled by 1/p, where p"
[^l8]: arxiv-2511-21338 — "We hypothesise that this encourages MDLMs to rely on nearby context"
[^l9]: arxiv-2511-21338 — "use greedy decoding for all models we consider"
[^l10]: arxiv-2511-21338 — "relatively easy (An et al., 2024)"
[^l11]: arxiv-2511-21338 — "we are not interested in studying generalisation to larger context lengths"
[^l12]: arxiv-2511-21338 — "We use a dataset containing 10 relevant examples and 40 distractors"
[^l13]: arxiv-2511-21338 — "we compare the performance of LLaDA-8B with Llama3-8B"
