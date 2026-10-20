---
description: "A subject supplied as an image forces a hidden first hop: the entity must be resolved early enough for the stored recall layers to read it, and late resolution fails even when recognition succeeds."
aliases: ["two-hop problem in multimodal recall", "late entity resolution", "visual two-hop factual recall", "first-hop timing"]
sources: ["arxiv-2512-03276"]
---
# Late entity resolution in two-hop recall

A question about a thing that is not named in the question is two steps. The answerer must first form a representation of the entity (the first hop) and then read the facts stored about it (the second hop). The LLM literature already describes the text case this way: the layer localization of factual recall "has been linked to their struggles with multi-hop reasoning, which requires resolving intermediate entities before answering the full query".[^c1] Venhoff et al. apply the same frame to a subject that arrives as an image: factual recall from visual input "requires VLMs to solve a two-hop problem: (1) forming entity representations from visual inputs, and (2) recalling associated factual knowledge based on these entity representations."[^c2]

The mechanism they propose is one of timing, not of missing knowledge. In a text-only LLM, early-layer MLPs read subject tokens and produce subject-related facts. A vision-language model whose visual representations are not aligned with the LLM's token space may resolve the entity only in middle layers, after those MLPs have already run. In their words, the degraded models "resolve the first hop too late in the computation", so they cannot reuse the factual-recall circuit of their backbone.[^c3] The effect is broad in their benchmark: "11 out of 14 VLMs exhibit lower factual-recall accuracy than" their language-only backbones.[^c4]

Linear probes on the residual stream locate the difference. For the LLaVA-style models, "probe accuracy remains poor, indicating that early layers do not encode robust entity representations."[^c5] For Gemma-3-12B and Qwen2.5-VL-7B, the probes stay high across layers, and those models do not show the degradation.[^c6] A causal test follows the same line: "heuristic patching recovers 35% of the factual" recall gap when early-layer MLP outputs from the backbone are copied into the degraded VLM.[^c7] The comparison arms recover less, "only recovers 13%, and random patching recovers 16%", so the early MLPs are a specific missing piece and not any intervention at any position.[^c8]

The useful part for asking and answering is the structure, which the paper states as a question of timing. A hop whose output is needed early is resolved late, so the later hop has nothing to read. Recognition can be perfect and recall still fails. The benchmark is built to keep the two apart: "the sample is discarded to avoid conflating recognition errors with factual retrieval."[^c9] A measurement that does not separate the hops cannot say which one failed.

A reasoning step was tried as a route around the late hop. The VLM may "describe the visual entities relevant for factual recall in text space, and then answer the question."[^c10] Here the paper's result is mixed: "the effect of chain of thought prompting seems to be very model dependent"[^c11], and it closed the full gap for Pixtral while LLaVA-1.5-7B lost accuracy. My reading, not stated in the paper: the gain is consistent with the entity becoming a text representation that the recall layers can read, but the paper does not separate that from more tokens in general.

## Limits

- The claim is shown for factual recall only. The paper says "While our study focuses on factual recall, future work should examine" other tasks.[^c12]
- The degradation is measured on LLaVA-style adapters trained with limited data and compute; the authors' "fundamental limitations" claim is scoped to "LLaVA-style VLMs that are trained with limited data and compute resources."[^c13] Native and heavily fine-tuned adapter models are the contrast, not a demonstration of a general law.
- The probes use 50 ImageNet classes, and the timing is read off layer indices, so "early" and "late" are relative to each model's depth. The probe result is correlational; only the patching is causal, and it recovers about a third of the gap on average.
- Whether a subject delivered through any non-question channel (a table, a document, a retrieved passage) is resolved late in the same way is not tested. That extension is my inference.
- The chain-of-thought result does not isolate entity grounding from other effects of longer output.

## Related

- [[redundant-multilayer-knowledge-editing]] — the same depth ordering, a hop resolved after the layer that stores the next hop, used there to explain why single-layer edits fail on 2-hop questions.
- [[reasoning-for-parametric-recall-underoptimization]] — reasoning as a route to recall; here the route is a text description of the entity before the answer.
- [[cross-modal-aggregation-gap]] — another vision-language case where the image and text channels are not combined into one judgment.

[^c1]: arxiv-2512-03276 — "which requires resolving intermediate entities before answering the full query"
[^c2]: arxiv-2512-03276 — "a two-hop problem: (1) forming entity representations from visual inputs, and"
[^c3]: arxiv-2512-03276 — "because they resolve the first hop too late in the"
[^c4]: arxiv-2512-03276 — "11 out of 14 VLMs exhibit lower factual-recall accuracy than"
[^c5]: arxiv-2512-03276 — "probe accuracy remains poor, indicating that early layers do not encode robust entity representations."
[^c6]: arxiv-2512-03276 — "Gemma-3-12B and Qwen2.5-VL-7B on the other hand show consistently high probe accuracies"
[^c7]: arxiv-2512-03276 — "heuristic patching recovers 35% of the factual"
[^c8]: arxiv-2512-03276 — "only recovers 13%, and random patching recovers 16%"
[^c9]: arxiv-2512-03276 — "the sample is discarded to avoid conflating recognition errors with factual retrieval."
[^c10]: arxiv-2512-03276 — "relevant for factual recall in text space, and then answer the question."
[^c11]: arxiv-2512-03276 — "the effect of chain of thought prompting seems to be very model dependent"
[^c12]: arxiv-2512-03276 — "While our study focuses on factual recall, future work should examine"
[^c13]: arxiv-2512-03276 — "These findings expose fundamental limitations in current LLaVA-style VLMs that are trained with"
