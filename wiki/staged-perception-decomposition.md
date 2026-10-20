---
description: "Ordering a detection answer into presence, count, then boxes gave a 7B vision-language model +4.1 mAP over fine-tuning alone on COCO; the stages were not ablated one by one."
aliases: ["CoT4Det", "chain-of-thought for detection", "classification-counting-grounding decomposition", "perception chain-of-thought"]
sources: ["arxiv-2512-06663"]
---
# Staged perception decomposition

A vision-language model asked to detect objects in one pass fails in a patterned way. Its output repeats boxes: the model "frequently generate[s] duplicate bounding boxes at identical" locations until the output length is reached.[^c1] It boxes categories that are absent from the image, and it misses small and crowded objects. The staged format answers the same request in a fixed order inside one output. The paper calls the task a sequence of "steps: classification, counting, and grounding".[^c2]

The first stage lists which candidate categories are present. The second states how many instances each present category has. The third emits pixel-space boxes, grouped by category in the order of the category list. Each stage conditions the next. A category rejected at stage one never reaches grounding, and the count at stage two is a target the boxes must meet. The paper gives the two early stages these jobs. Classification "serves to distinguish between positive and negative categories",[^c3] and counting "plays a critical role in mitigating redundant predictions" by making the model predict a number first: "expected number of instances for each identified category, the model aligns its generation process" with that cardinality.[^c4] Negative categories are part of the input on purpose. Training samples "both positive and negative categories when constructing the" candidate list, so that the model learns to reject absent objects.[^c5]

The format is trained, not only prompted. The model "continues training from a strong" general vision-language model, on "a hybrid training corpus with a 50-50 ratio of detection-style and vision-language data".[^c6]

## What was measured

On COCO-Val, with Qwen2.5-VL-7B as the base, the ablation has three arms per input resolution: no extra training, supervised fine-tuning (SFT) on the mixed corpus, and SFT plus the staged format. Supervised training alone raises mAP "from 19.1 to 25.5 (+6.4)".[^c7] The staged format adds "yielding +4.1 mAP gain over SFT alone",[^c8] which is 29.6 at native resolution. In the harder full-category setting, "where all 80 COCO categories are used",[^c9] the paper reports "a mAP of 32.7" with precision 69.1 and recall 61.9.[^c10]

The resolution result is the part the paper stresses. Raising input resolution without the staged format gives little on small objects: "yields only marginal gains (APsmall : 6.0 → 8.1)".[^c11] With the staged format at the higher resolution, APsmall "jumps to 16.7".[^c12] The paper's reading is that "the bottleneck lies not in visual input quality" but in the language model's handling of fine spatial detail.[^c13] It calls the structured format "a critical reasoning scaffold that unlocks the latent" high-resolution information.[^c20]

My inference, not the paper's claim: the stages are a constraint on the form of an answer, fixed inside one output and produced by the model alone. This differs from the sub-questions of [[self-ask-decomposition]], which can be routed to a search and answered by something other than the model. The note says nothing about whether a human question should be staged this way.

## Limits

- One base model and one benchmark carry the ablation. The paper itself notes that it "has only been tested on medium-scale LVLMs".[^c14]
- The staged format was measured only as a trained output format on top of SFT. Table 5 has no arm with the staged format and no SFT, so the +4.1 is an effect over extra training, and what the format does without that training is not in the text read.
- The stages were not ablated one at a time. The paper credits "highlighting the effectiveness of the classification and counting"[^c15] for the full-category gains, but no arm drops one stage. Which stage carries the gain is the paper's reading, not a measurement.
- The resolution interaction is smaller than the text's wording suggests. The text compares 16.7 with the no-SFT, no-format row at 8.1. Matched on SFT, by my reading of Table 5, resolution raises APsmall by 2.8 without the format (7.1 to 9.9) and by 6.0 with it (10.7 to 16.7). The text reports no variance for these cells.
- The metric is contested. The paper argues that mAP mismatches how these models answer, since "LVLMs typically generate a limited number of" confident boxes, so it also reports precision and recall.[^c16] Its ground-truth-category setting names the present categories in the prompt, the way prior work evaluates detection,[^c17] so stage one is partly supplied there and that setting is the easier one.
- The vision encoder is frozen during training: "the vision encoder is kept frozen",[^c18] so the resolution finding holds under that condition only.
- The paper says the framework "is sensitive to prompt design and category set composition".[^c19] No sensitivity sweep is in the text read.

## Related

- [[self-ask-decomposition]] — sub-questions emitted mid-trajectory and routable to a search; here the stages are fixed within one output.
- [[reasoning-quality-over-structure]] — a fixed chain template whose benefit depends on what fills it; the same worry about structure without good content applies to these stages, and the paper does not test it.
- [[cot-capacity-responsiveness]] — how the benefit of a reasoning chain varies with model size; this paper tests one 7B model only.

[^c1]: arxiv-2512-06663 — "LVLMs frequently generate duplicate bounding boxes at identical"
[^c2]: arxiv-2512-06663 — "steps: classification, counting, and grounding"
[^c3]: arxiv-2512-06663 — "The classification stage serves to distinguish between positive and negative categories"
[^c4]: arxiv-2512-06663 — "expected number of instances for each identified category, the model aligns its generation process"
[^c5]: arxiv-2512-06663 — "we randomly sample both positive and negative categories when constructing the"
[^c6]: arxiv-2512-06663 — "a hybrid training corpus with a 50-50 ratio of detection-style and vision-language data"
[^c7]: arxiv-2512-06663 — "from 19.1 to 25.5 (+6.4)"
[^c8]: arxiv-2512-06663 — "yielding +4.1 mAP gain over SFT alone"
[^c9]: arxiv-2512-06663 — "where all 80 COCO categories are used"
[^c10]: arxiv-2512-06663 — "a mAP of 32.7"
[^c11]: arxiv-2512-06663 — "yields only marginal gains (APsmall : 6.0 → 8.1)"
[^c12]: arxiv-2512-06663 — "APsmall jumps to 16.7"
[^c13]: arxiv-2512-06663 — "the bottleneck lies not in visual input quality"
[^c14]: arxiv-2512-06663 — "it has only been tested on medium-scale LVLMs"
[^c15]: arxiv-2512-06663 — "highlighting the effectiveness of the classification and counting"
[^c16]: arxiv-2512-06663 — "LVLMs typically generate a limited number of"
[^c17]: arxiv-2512-06663 — "evaluate detection performance using prompts that include only the ground-truth categories"
[^c18]: arxiv-2512-06663 — "the vision encoder is kept frozen"
[^c19]: arxiv-2512-06663 — "is sensitive to prompt design and category set composition"
[^c20]: arxiv-2512-06663 — "a critical reasoning scaffold that unlocks the latent"
