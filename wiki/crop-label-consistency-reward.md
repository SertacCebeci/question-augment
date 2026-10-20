---
description: "A process reward for a zoom-in tool call scores the returned crop against the label the model itself gave, using a pretrained image-text similarity, so grounding needs no boxes."
aliases: ["process-based ROI grounding reward", "annotation-free grounding reward", "CLIP grounding reward", "crop-label cosine reward"]
sources: ["arxiv-2512-14044"]
---
# Crop-label consistency reward

When a reasoner can call a zoom-in tool, the training signal for each call can be read off the call itself. The OmniDrive-R1 paper defines a per-call term. The model emits a bounding box and a label for the region it wants, the tool returns that crop, and the reward is the cosine similarity between the crop and the label, computed by a pretrained image-text encoder: "We leverage a pre-trained CLIP model to" compute it.[^c1] The label is not an external annotation; it is the model's own output, "produced by the model in the reasoning" step.[^c2] The term is paid "upon a successful tool invocation at step t", so a call that returns nothing earns nothing.[^c3]

The stated purpose is to avoid dense labels. The authors write that the design "circumvents the need for labor-intensive manual annotation of key" regions, and that "Second, it ensures semantic relevance between the cropped visual content and the generated label."[^c4] The paper's name for this is an "annotation-free, process-based grounding reward."[^c5]

Because the term is summed over a trajectory, it can be inflated by calling the tool more often. The paper's answer is a decay: each term is weighted by λ^(t-1), so the reward for call t shrinks geometrically with the call's position, and the process reward is the sum over the E calls of a trajectory (Eq. 3 of the paper). The decay is introduced "to prevent the model from exploiting this reward by frequently invoking the tool."[^c6] An outcome reward is added on top. It has an accuracy term, a formatting term, and a tool bonus that is paid only when the answer is correct and at least one tool was used: "specifically awarded only when the model achieves a correct" final answer.[^c7]

The term answers a specific failure. The authors report that the policy, before training, "exhibits a strong bias towards text-based reasoning, leading" to rare tool calls, and that an outcome-only reward "can discourage the model from exploring necessary tool usage."[^c8][^c9] A per-call reward gives credit to a call before the answer is known, so the policy can learn that a look helps while the answer is still far away.

The paper's ablation keeps the two-stage pipeline fixed and drops only this term. The reasoning score falls from 80.35% to 70.18% and MCQ accuracy from 73.62% to 57.19% on DriveLMM-o1. The authors conclude that the result "provides compelling evidence that the grounding reward is indispensable for achieving high-quality multi-modal reasoning and guiding judicious tool invocation."[^c10]

What the term measures is a match between a crop and the words that name it. It does not measure whether the crop holds the evidence the answer needs. Both are produced by the same policy, so the term is a check on the reasoning step's internal coherence, and its value as a grounding signal depends on how well the label names the region.

## Limits

- The sections read report no accuracy of the crops against ground-truth boxes. "ensures semantic relevance" is the authors' design argument for the term, not a measured property of the crops in this paper.
- The check is circular in the way the paper's own design implies. My inference, not the paper's claim: a policy can satisfy the term by naming a wrong object that is visually present and cropping it. Whether the crop is the right one is left to the outcome reward.
- The decay coefficient λ is introduced, but the sections read do not isolate its value or show a sweep over it. The ablation removes the whole term, not the decay on its own.
- The evidence is one in-domain benchmark (DriveLMM-o1) on one backbone family (the baseline is Qwen2.5-VL-7B), with zero-shot SURDS reported separately. Nothing here shows the term transfers to other visual domains.
- The term presumes a label that names something a crop can contain. My inference: a relational label ("the car to the left of the bus") does not pick out one region, so the cosine has no single target. The paper does not test this case.
- CLIP-style embeddings are a fixed external judge. The term inherits whatever that encoder does with fine spatial distinctions, which the sections read do not examine.

## Related

- [[on-demand-resolution-zoom]] — the same ask-for-a-finer-look loop, on video under a frame budget; that work shapes the policy with an outcome-side tool bonus, this one adds a per-call process term.
- [[visual-evidence-scoring]] — grades the crops a zoom-reasoner cites against ground-truth boxes with a learned selector; this term needs no boxes and is a training reward, not a release score.
- [[rlvr-answering-bias]] — outcome-only verifiable rewards on a multimodal answerer; the process term is the step-level addition an outcome reward does not supply.
- [[cot-hallucination-trap]] — the failure this reward is built against: when grounding is weak, the rationale follows the language prior.

[^c1]: arxiv-2512-14044 — "We leverage a pre-trained CLIP model to"
[^c2]: arxiv-2512-14044 — "which are produced by the model in the reasoning"
[^c3]: arxiv-2512-14044 — "upon a successful tool invocation at step t"
[^c4]: arxiv-2512-14044 — "This design offers two key advantages: first, it circumvents the need for labor-intensive manual annotation of key"
[^c5]: arxiv-2512-14044 — "an annotation-free, process-based grounding reward"
[^c6]: arxiv-2512-14044 — "we introduce a decay coefficient"
[^c7]: arxiv-2512-14044 — "specifically awarded only when the model achieves a correct"
[^c8]: arxiv-2512-14044 — "exhibits a strong bias towards text-based reasoning, leading"
[^c9]: arxiv-2512-14044 — "based solely on the final outcome can discourage the model"
[^c10]: arxiv-2512-14044 — "provides compelling evidence that the grounding reward is indispensable"
