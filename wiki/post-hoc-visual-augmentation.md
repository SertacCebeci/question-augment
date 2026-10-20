---
description: "A reasoning model calls image transforms such as denoise, resize or rotate mid-answer, and feeds the re-encoded result back into its context, extending crop-only zoom tools."
aliases: ["VACoT", "visual augmentation chain-of-thought", "thinking with augmentation", "iterative image transform tool", "chain of manipulations"]
sources: ["arxiv-2512-02361", "arxiv-2511-23477"]
---
# Post-hoc visual augmentation

A vision-language model can be given a set of image operations as callable tools, and it can invoke them while it is already reasoning. The VACoT paper calls this "thinking with augmentation."[^c1] Cropping and other transforms are treated as "visual augmentations as post-hoc processing steps."[^c2] The contrast is the "thinking with bounding boxes" paradigm, which "employs local cropping" alone.[^c3] The authors argue that this is "merely a specific instance of visual information filtering."[^c4]

The mechanism is a loop over the generation. Generation "stops autoregressive generation at designated tokens" to either emit a visual call or end the answer.[^c5] The text inside the call is "parsed into a candidate operation," which an executor runs on the current image.[^c6] If the operation and its parameters match the allowed set, the new image "is re-encoded by the vision encoder" and its tokens are appended to the chat history; otherwise an error message is appended instead.[^c7][^c8] Decoding then resumes from that context. This is what allows several calls in one answer: the paper says its method can "leverage iterative augmentations on adversarial samples."[^c9] A crop followed by a denoise, as in the paper's first figure, is one such chain. The paper calls the whole arrangement a loop that "enables iterative token generation, visual augmentation, and feedback integration" into later steps.[^c10]

The operation set is kept small on purpose. The method starts from a list of common filters, which the paper says it "first implement[s] ... as API calls."[^c11] Manual evaluation then found that "these post-hoc operations have a negligible impact on the model" perceptual capability, and the set was narrowed to "stable operations for A: crop, resize," with rotate, flip, denoise and edge detection.[^c12] My reading: the narrowing keeps only transforms that change what the model can read. Each call is wrapped as a lightweight API, which the authors say reduces "the training difficulty" and avoids "uncontrollable actions."[^c13]

The reported effect is strongest where the input is hard to read. The abstract names gains "particularly on tasks requiring fine-grained recognition or robustness against adversarial text."[^c14] On the adversarial OCR set (AdvOCR), the authors say the augmentation "significantly" helps.[^c15] The ablation most relevant to the mechanism removes the tool: when the system prompt bars API calls, "performance drops significantly," and the authors take this to show "that the improvement stems from proper tool-based augmentation rather than other factors."[^c16][^c17] A baseline that forces a fixed set of pre-chosen transforms also helps, but "performance remains limited because they fail to select the" right transform.[^c18] On this account the gain depends on choosing the transform, not only on having transforms available.

A side result concerns cost. With input resolution cut to half, which removes about three quarters of the visual tokens, the paper reports that "performance drops by only" about one point when upscaling is allowed after the fact.[^c19] The authors attribute this to "the post-hoc resizing on" about 30 % of uncertain cases.[^c20] My reading: the model spends the extra tokens only where it is unsure.

## Limits

- The results are the paper's own. I read the method, the ablations and the AdvOCR construction, but not the main tables across the thirteen public benchmarks, so the size of the gain outside the adversarial and fine-grained sets is not verified here.
- The backbone is a single small model, "which is based on Qwen2.5VL-3B."[^c21] Nothing in the text tests a larger model or another family.
- The reward that teaches when to call a tool is scored by another model, a "teacher model to provide reward signals for verifying both" answer and format.[^c22] Whatever that judge gets wrong is inherited by the policy.
- AdvOCR is "comprising 100 adversarial samples for perception evaluation."[^c23] It was built by the authors from failure cases they collected and filtered, so it does not establish how often the method helps on adversarial inputs in general.
- The operations are non-semantic: a denoise or a resize does not know what the question asks. My inference: a transform that helps one text case can remove detail another question needs. The reward is the only check on that in the paper.
- The cold-start stage inserts calls "deliberately" and at random, "even if these calls are not semantically relevant."[^c24][^c25] My inference: that stage teaches the syntax of calls, not their use. The paper does not measure how much later behavior depends on it.

## Related

- [[crop-label-consistency-reward]] — a per-call reward for a zoom-in crop, scored against the model's own label. This note's operation set is wider than crop, and its reward is a correctness gate rather than a crop-label match.
- [[correctness-gated-redundancy-penalty]] — the same kind of gate on tool calls, applied to retrieval. The augmentation paper's call term is likewise gated on answer correctness.
- [[benefit-scaled-tool-reward]] — prices each call by a paired accuracy gain. The augmentation paper instead allows a fixed number of calls and penalises calls beyond it, when the answer is correct.
- [[interleaved-reasoning]] — the broader pattern of tool output and reasoning alternating within one generation. My inference: this note is a visual case of that pattern.
- [[visual-forgetting-during-reasoning]] — a related concern about visual information during long reasoning. The paper here does not measure forgetting.
- [[annotated-step-grounding-reward]] — the same call-and-feed-back loop applied to video, where the calls are query-conditioned temporal and spatial localizations ("find-segment to revisit short temporal windows"[^c26]). My reading: the loop carries over, the non-semantic transform set does not.

[^c1]: arxiv-2512-02361 — "we advocate for thinking with augmentation, reformulating cropping and other"
[^c2]: arxiv-2512-02361 — "visual augmentations as post-hoc processing steps"
[^c3]: arxiv-2512-02361 — "employs local cropping"
[^c4]: arxiv-2512-02361 — "strategy constitutes merely a specific instance of visual information filtering"
[^c5]: arxiv-2512-02361 — "stops autoregressive generation at designated tokens to either produce visual augmentations or terminate responses"
[^c6]: arxiv-2512-02361 — "is parsed into a candidate operation"
[^c7]: arxiv-2512-02361 — "is re-encoded by the vision encoder"
[^c8]: arxiv-2512-02361 — "API calls are only executed if the operation and its parameters match"
[^c9]: arxiv-2512-02361 — "leverage iterative augmentations on adversarial samples"
[^c10]: arxiv-2512-02361 — "enables iterative token generation, visual augmentation, and feedback integration"
[^c11]: arxiv-2512-02361 — "We first implement several augmentations as API calls"
[^c12]: arxiv-2512-02361 — "these post-hoc operations have a negligible impact on the model"
[^c13]: arxiv-2512-02361 — "all augmentations into lightweight API calls to reduce the"
[^c14]: arxiv-2512-02361 — "particularly on tasks requiring fine-grained recognition or robustness against adversarial text"
[^c15]: arxiv-2512-02361 — "demonstrate that our post-hoc visual augmentation significantly"
[^c16]: arxiv-2512-02361 — "performance drops significantly"
[^c17]: arxiv-2512-02361 — "confirming that the improvement stems from proper tool-based augmentation rather than other factors"
[^c18]: arxiv-2512-02361 — "performance remains limited because they fail to select the"
[^c19]: arxiv-2512-02361 — "performance drops by only"
[^c20]: arxiv-2512-02361 — "This resilience is attributed to the post-hoc resizing on"
[^c21]: arxiv-2512-02361 — "which is based on Qwen2.5VL-3B"
[^c22]: arxiv-2512-02361 — "teacher model to provide reward signals for verifying both"
[^c23]: arxiv-2512-02361 — "comprising 100 adversarial samples for perception evaluation"
[^c24]: arxiv-2512-02361 — "deliberately insert random API calls when rewriting"
[^c25]: arxiv-2512-02361 — "even if these calls are not semantically relevant"
[^c26]: arxiv-2511-23477 — "find-segment to revisit short temporal windows"
