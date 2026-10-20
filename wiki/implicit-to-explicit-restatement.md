---
description: "Writing an implicit query out as explicit perceptual terms before the box raised UAV grounding accuracy; the paper reads the gain as attention moving onto the target during that span."
aliases: ["I2E-CoT", "implicit-to-explicit chain-of-thought", "explicit restatement before grounding", "explicit-reference reasoning reward"]
sources: ["arxiv-2601-00998"]
---
# Implicit-to-explicit restatement

A vision-language model asked to find "the person trapped by floodwaters" has to know which region the phrase denotes before it can box it. The restatement mechanism inserts one step between the query and the coordinates. The model first writes a short description of the referent in perceptual terms (color, size, relative position), inside a dedicated tag, and only then emits the box. The authors call this implicit-to-explicit chain-of-thought (I2E-CoT). The prompt asks for the span directly. The paper says the design "strategically forces the model to translate an implicit query" into a grounded description.[^c1] That description comes before the box, and that ordering is the step the paper trains.

The object this operates on is an [[implicit-reference]]: a query whose referent the image does not state.

## What the restatement is measured to do

The evidence is attention. The authors plot the share of attention that generated tokens pay to image tokens across generation steps. Under plain GRPO that share is dispersed. With I2E-CoT, the peak falls on the restated span: "visualizations before, during, and after the explicit region reveal that it successfully concentrates attention" on the object.[^c2] In the paper's worked example (Figure 2, a left-turning car), the explicit phase is where the model names the "green" cue, and attention to the matching image tokens rises: "substantially increasing attention to the corresponding image tokens."[^c3]

The authors read this as the restatement turning an implicit query into an explicit one, which makes the image tokens easier to attend to. My reading is that Figure 2 is one example and the attention curves are peaks over a few samples; the paper does not run a causal test that removes the restated span and holds the rest fixed.

## The reward that trains the restatement

The restatement is trained with a reasoning reward. The model's explicit span is compared with a human-written explicit reference from the benchmark, using Jaccard text similarity, and the reward is 1 "if similarity > 0.9; otherwise, the reward is 0."[^c4] The reward sits beside a format reward and a perception reward (IoU above 0.5 and L1 distance under 10 pixels) in a linear combination.

The ablation reports that the reasoning reward carries more weight than the perception reward: "combining Format and Reasoning rewards achieves an accuracy of 54.07%," above the configuration that keeps perception but drops reasoning.[^c5] The authors state the general claim as "the reasoning reward is even more critical" than the perception reward.[^c6]

The similarity threshold has an interior optimum. The best setting is 0.9 for both query types, and the authors explain the failure at 1.0 by "insisting on a perfect textual match between the generated" rationale and the reference.[^c7] Their sweep found the best threshold the same for explicit and implicit queries, which they treat as a practical simplification.

## Results

On the implicit-only benchmark, DroneVG-R1 7B reaches 52.05% average accuracy. The base model with reasoning enabled, Qwen2.5-VL 7B, scores 43.78%. A supervised Qwen2.5-VL 7B without rationale scores 50.28%, and DroneVG-R1 7B surpasses it "by nearly 2 percentage points."[^c8] The gain over the base model is about eight points, and the comparison that matters for the mechanism is with the same base model and reasoning turned on.

## Limits

- The method needs a model that can write valid intermediate reasoning. The authors say its "effectiveness is directly contingent upon the LVLM’s capacity for generating valid intermediate reasoning steps," and it does not apply to models that output only boxes.[^c9]
- The reward is lexical. A restatement that is semantically right but worded differently scores 0 unless its Jaccard similarity clears 0.9. The authors name this as the open problem: "overcome the limitations of current explicit text similarity."[^c10]
- The gains bundle several changes: the restated span, the reward, GRPO training, and the prompt. The paper's main comparisons do not isolate the restated span from the RL training it is trained under. I did not find a run in the slices I read that gives the prompt alone, without the reward.
- The mask stage (SAM2 on the predicted box) is decoupled and not part of the accuracy reported here, which is box-level. The results do not speak to pixel-level grounding.
- The evidence is for one benchmark of UAV imagery with 873 test samples. The authors' own threshold and weight sweeps show the reward is sensitive to its settings, and the method has not been tested on other domains.

## Related

- [[implicit-reference]] — the referring form this mechanism is built to handle, and the explicit–implicit gap that motivates it.
- [[implicit-subject-resolution-injection]] — another account in which an unnamed subject is made explicit inside the model, and answer probability rises when it is.
- [[procedural-hallucination-readout-routing]] — restating the relevant binding near the query turned failed long-context retrievals into correct ones, an account of the same kind: the failure is one of access at readout, not of storage.

[^c1]: arxiv-2601-00998 — "strategically forces the model to translate an implicit query"
[^c2]: arxiv-2601-00998 — "visualizations before, during, and after the explicit region reveal that it successfully concentrates attention"
[^c3]: arxiv-2601-00998 — "substantially increasing attention to the corresponding image tokens"
[^c4]: arxiv-2601-00998 — "assigned if similarity > 0.9; otherwise, the reward is 0"
[^c5]: arxiv-2601-00998 — "combining Format and Reasoning rewards achieves an accuracy of 54.07%"
[^c6]: arxiv-2601-00998 — "demonstrate that the reasoning reward is even more critical"
[^c7]: arxiv-2601-00998 — "insisting on a perfect textual match between the generated"
[^c8]: arxiv-2601-00998 — "by nearly 2 percentage points (50.28%"
[^c9]: arxiv-2601-00998 — "is directly contingent upon the LVLM’s capacity for generating valid intermediate reasoning steps"
[^c10]: arxiv-2601-00998 — "overcome the limitations of current explicit text similarity"
