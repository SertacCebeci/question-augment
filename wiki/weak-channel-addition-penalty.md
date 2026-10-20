---
description: "When text alone already suffices, adding an image that the model reads poorly lowers accuracy below text-only, so the multimodal-minus-text gap goes negative."
aliases: ["text prevails", "vision-text degradation", "multimodal degradation below text-only", "modality addition penalty"]
sources: ["arxiv-2512-13747"]
---
# Weak-channel addition penalty

Give a model a question it can already answer from text, then add a second channel it reads poorly, and accuracy can fall. The study behind this note tests two medical decision tasks, three-stage Alzheimer's classification on OASIS-3 and 14-condition chest radiograph classification on MIMIC-CXR, under three input settings: text only, image only, and image plus text. Its headline finding is that "text-only reasoning consistently outperforms vision-only or vision–text settings, with multimodal inputs often performing worse than text" alone.[^c1]

The comparison is concrete. Across nearly all models and both datasets, "the text-only setting achieves" the highest accuracy.[^c2] For InstructBLIP2 on OASIS, accuracy "achieves 79.26% on OASIS (text-only), but drops sharply to" 4.98% when the image is added.[^c3][^c4] GPT-4o with debating "follows a similar pattern in MIMIC-CXR", where text-plus-image accuracy is far below text alone.[^c5] Image-only input is the weakest condition: "Vision-only performance is mostly the lowest across all models."[^c6] The general rule the authors draw is that "modality input often leads to performance degradation instead" of complementing the other input.[^c7]

So the quantity is the multimodal-minus-text gap, the same comparison used in [[perception-substitution-gap]], but here it is negative: the added channel costs accuracy rather than adding it. The penalty applies when text is sufficient and the image is poorly grounded for the model. It is a condition on the extra channel, not on the task alone.

The authors' account of the cause is a suggestion, not a measured effect. They attribute the drop to "a misalignment between the multimodal features," which they say appears "when models only have poor grounding capability."[^c8] My inference, not measured in the work: the reasoner is given an extra input whose content it cannot align with the text, and it reasons through that noise rather than discarding it. Whether the cost comes from attention, from fusion, or from the answer format is not tested.

The penalty is not fixed. The same paper reports that a few labeled exemplars in the prompt can raise poor visual performance: "even a small number of exemplars can substantially boost performance" on the OASIS benchmark, with the largest gains in the image-only setting.[^c9] This is evidence that the drop is partly a matter of how the model is cued to read the input, not only of what the image contains. The gains on MIMIC-CXR are slight.

## Limits

- The text and image conditions are not information-matched. For OASIS the text is built from "psychological and cognitive test results to text reports as input,"[^c10] and for MIMIC-CXR it uses "the refined findings from X-ray images designed" for another model's training.[^c11] Clinical labels are often defined by cognitive scores and radiology findings (my inference). If so, the text channel carries the label more directly than the image does, and the penalty measures how much more informative the text is as much as how much the image harms. The paper does not separate the two.
- The image input is reduced. The authors note that "are not designed to process 3D format," so the OASIS MRI is cut to three middle slices and resized to 224 by 224.[^c12] A stronger image pipeline may change the sign.
- The sample is small and single-run. The authors "randomly select 200 samples for inference" for each test.[^c13] No variance across seeds or prompts is reported in the sections read.
- The mechanism is untested. The misalignment account above is the authors' suggestion and was not probed.
- Two medical benchmarks, both zero-shot in the main table. The authors themselves say that "different MDM tasks demand varying levels of visual understanding."[^c14] The penalty may not hold where the image carries information the text lacks, which is the case the paper's framing argues against but does not test.
- The abstract also names vision captioning followed by text-only inference and few-shot fine-tuning of the vision tower as mitigations. The sections read do not report results for either, so this note does not cover them.

## Related

- [[text-modality-dominance]] — the converse probe: corrupting the text of omni-modal models costs more than corrupting vision, which is the same text reliance seen from the removal side
- [[perception-substitution-gap]] — replacing the image with its text rendering raises accuracy; this note's gap has the opposite sign
- [[in-image-question-rendering]] — moving the question into the image lowers accuracy on identical items, a format effect rather than an added channel
- [[label-free-caption-intermediate]] — turning the image into text before answering is one route to the text-only condition, which this work does not test as a method
- [[dissonance-graded-abstention-miscalibration]] — omni-modal models over- or under-abstain when modalities disagree, a calibration side of the same reliance

[^c1]: arxiv-2512-13747 — "with multimodal inputs often performing worse than text"
[^c2]: arxiv-2512-13747 — "the text-only setting achieves"
[^c3]: arxiv-2512-13747 — "achieves 79.26% on OASIS (text-only), but drops sharply to"
[^c4]: arxiv-2512-13747 — "4.98% when vision"
[^c5]: arxiv-2512-13747 — "follows a similar pattern in MIMIC-CXR"
[^c6]: arxiv-2512-13747 — "Vision-only performance is mostly the lowest across all models"
[^c7]: arxiv-2512-13747 — "modality input often leads to performance degradation instead"
[^c8]: arxiv-2512-13747 — "a misalignment between the multimodal features"
[^c9]: arxiv-2512-13747 — "even a small number of exemplars can substantially boost performance"
[^c10]: arxiv-2512-13747 — "psychological and cognitive test results to text reports as input"
[^c11]: arxiv-2512-13747 — "while using the refined findings from X-ray images designed"
[^c12]: arxiv-2512-13747 — "are not designed to process 3D format"
[^c13]: arxiv-2512-13747 — "we randomly select 200 samples for inference"
[^c14]: arxiv-2512-13747 — "Different MDM tasks demand varying levels of visual understanding"
