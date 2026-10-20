---
description: "Appending many mask tokens for generation lowers accuracy in masked diffusion LMs trained from scratch; the paper reads the masks as distractors that draw attention away from the relevant context."
aliases: ["mask distraction", "extra mask tokens", "inverse scaling with masks", "generation placeholder tokens"]
sources: ["arxiv-2511-21338"]
---
# Mask-token distraction

A masked diffusion language model generates by filling in masked positions, so the number of mask tokens placed after a prompt is a generation-time choice. The paper treats that choice as something that can change what the model uses from the context. Its setup puts the answer's mask first and appends more masks after it: "the first mask token always corresponds to the answer for the test question," and only that first prediction is scored.[^m1] With more appended masks, LLaDA loses accuracy. The paper calls it "a consistent performance degradation as the number of masks increases,"[^m2] and describes the decline as "monotonic degradation in accuracy even under greedy decoding."[^m3]

The paper's reading is that the masks are not neutral. "These masks act as distractors, reducing the model's ability to process relevant information."[^m4] The argument is that degradation grows with the amount of irrelevant material the model must filter: "performance degradation due to extra masks generally increases with" the number of distractor examples, and so with the effective context length.[^m5] Read this way, the extra masks compete for attention with the evidence, and the more distractors there are, the more the competition costs.

The gradient view points the same way. Attribution to the mask tokens is high relative to other tokens, and the table caption reads: "MDLMs are particularly sensitive to mask tokens."[^m6] The authors also suggest a training-side explanation for the base model: "during training, random noising rarely produces long unmasked prefixes followed by large contiguous mask spans."[^m7] That explanation covers the base model only, since the instruct model shows a similar decline without it.

The effect differs by model. Dream, which was initialised from an autoregressive model, is more robust, but it shows "a noticeable drop (6 and 8 percentage points for the base and instruct model, respectively)" when about twenty masks are added.[^m8] The authors' guess for the difference is that Dream's mask tokens are "less integral to their architecture and training dynamics,"[^m9] which they offer as a hypothesis.

For the asker and the answerer the point is practical. The number and placement of generation slots is part of the setup, so two runs of the same model with different slot counts measure different things. The paper argues this should enter evaluation: it establishes mask configuration "as a critical factor in MDLM evaluations."[^m10] (My inference from that claim: a benchmark result for a diffusion LM is incomplete without the slot count.) Irrelevant text is also a known degrader of long-context use, as [[effective-context-length]] records; whether mask tokens act like that padding is a conjecture here, not something either source tests.

## Limits

- The effect is established for masked diffusion models, with LLaDA and Dream and an LLaDA-MoE appendix. The autoregressive comparison is not part of the mask experiment, so the claim that masks are worse than ordinary padding is not shown.
- The paper's "distractor" account is its hypothesis. It tests a control in which the masks are replaced by repeated neutral tokens, to rule out "appending many identical tokens," but the result of that control is in a part of the paper I did not read. The reading here rests on the setup and on the Figure 4 trend for LLaDA.
- The decline is an accuracy measure on a few-shot rule-learning task with a single scored mask, decoded in one step. Multi-step decoding of the extra masks is studied separately and is not covered here.
- The paper also proposes a training objective meant to make predictions invariant to mask count. That is a method, so it is not carried into this note; only the measured effect and its stated mechanism are.
- Scope of the claim is the models tested, with a range of mask counts up to about 200. No larger slot counts or other diffusion architectures are reported in the parts read.

## Related

- [[locality-bias-in-context-use]] — the same paper's finding that the model uses context by distance to the answer slot; the mask tokens sit at that slot and so compete with the evidence nearest to it.
- [[effective-context-length]] — how much context a model uses at a given size, with padding as one of the degraders.
- [[context-cost-accuracy-decoupling]] — the padding-with-irrelevant-text result in the wiki, where accuracy held for several models; whether that result and the mask effect agree is left open here.

[^m1]: arxiv-2511-21338 — "the first mask token always corresponds to the answer for the test question"
[^m2]: arxiv-2511-21338 — "we observe a consistent performance degradation as the number of masks"
[^m3]: arxiv-2511-21338 — "monotonic degradation in accuracy even under greedy"
[^m4]: arxiv-2511-21338 — "find that these masks act as distractors, reducing"
[^m5]: arxiv-2511-21338 — "degradation due to extra masks generally increases with"
[^m6]: arxiv-2511-21338 — "MDLMs are particularly sensitive to mask tokens"
[^m7]: arxiv-2511-21338 — "produces long unmasked prefixes followed by large contiguous mask spans"
[^m8]: arxiv-2511-21338 — "a noticeable drop (6 and 8 percentage points for the base and instruct model, respectively)"
[^m9]: arxiv-2511-21338 — "making mask tokens less integral to their architecture and"
[^m10]: arxiv-2511-21338 — "as a critical factor in MDLM evaluations"
