---
description: "A question that needs the picture draws on dialogue and language priors; for some proprietary models, removing the frames raised factuality on a video benchmark."
aliases: ["language prior dominance", "modality prior over vision", "visual input displacing textual priors"]
sources: ["doi-10-48550-arxiv-2601-02536", "arxiv-2511-23112"]
---
# Text prior over visual evidence

A question about a video can be answered from the audio or subtitles, from what a plausible scene would contain, or from the frames themselves. MovieRecapsQA measures which of these multimodal models rely on by giving them the same recap segment under different inputs: full multimodal, frames only, and dialogue only.[^t1] The result that stands out is the one the authors headline: "Removing visual input improves proprietary model performance."[^t2] Proprietary models "score higher under dialogue-only than full-modality input," and the gains from dropping the frames are largest on vision-centric questions, the ones that rely on visual cues alone.[^t3]

The authors' reading is that the frames do not supply usable signal: "indicating that these models do not extract useful signal from video frames. Rather than helping, visual input actively disrupts their predictions, pulling them away from the textual priors they would otherwise rely on."[^t4] A second observation points the same way. Under full input, proprietary models lead the open-source ones on every question type, "but this advantage collapses under frames-only."[^t5] The authors conclude that "proprietary superiority is driven by stronger language priors, not better visual understanding."[^t6]

The paper also separates two failures that are easy to run together. Relevance stays stable across modalities: "models discuss the right content but cannot extract the precise visual facts needed to answer correctly."[^t7] So the answer is on topic and its scene is found, but the detail that needs the picture is wrong. Humans are not immune. Vision-centric questions score lowest on factuality for humans too, and the authors say that "getting the facts right is hard not because models are weak, but because visual information is difficult to extract even for humans watching the same video."[^t8]

What I take from this, as my inference rather than the paper's claim: a text prior gives an answer that is fluent, on topic and plausible, and a frame that is hard to read does not correct it. The same pull appears in chain-of-thought under weak grounding (see [[cot-hallucination-trap]]). Whether the frames are ignored or actively overridden cannot be told apart from the scores alone.

The same pull appears in university-level mathematics. MathSight shows each problem with its original figure, a hand-drawn figure, or a photo-captured figure, and adds "a text-only condition for controlled comparison."[^t11] The visual forms do not separate the models: the three variants "yield no statistically significant differences in model performance."[^t12] The text-only route does not lose either. Qwen3-VL "achieves 50.53% accuracy without any image input",[^t13] and its multimodal results sit lower, with the original figure at "only its own multimodal variants (original: 40.85,"[^t14] Scale does not move the answers: "altering the scale of the visual input scarcely impacts reasoning performance."[^t15] The authors read the stability across forms as reliance on text, since predictions are "largely insensitive to changes in visual form."[^t16] My inference: insensitivity to the figure's look shows that appearance does not drive the answer. It does not show the figure was ignored rather than read correctly, which is the same gap between being ignored and being overridden that the paragraph above leaves open. The difficulty axis on which this pull grows is in image-benefit-shrinks-with-difficulty.

## Limits

- The comparison of input conditions is confounded by frame count. The authors "use a different number of frames for each" model, up to each model's context limit.[^t9] A model given more frames is not given the same visual input.
- The facts that score an answer are themselves text, drawn from the recap's voiceover. A text-prior answer is therefore checked against text-derived facts, which may favour it. This is my inference; the paper does not test it.
- The drop on frames-only is not uniform. Open-source models "show smaller performance drops under frames-only in comparison to proprietary models."[^t10] The effect is a proprietary-model result in this benchmark, not a general one.
- The mechanism is the authors' reading from score patterns. No experiment isolates the priors directly, for instance by measuring answers to questions with the dialogue removed and no frames at all.
- Seven models, zero-shot, one standardized prompt. The reported figures are single-benchmark results for these models at one date.
- The mathematics result rests on a small multimodal portion, "the multimodal portion of the MathSight dataset contains 543 problems",[^t17] so differences between figure forms are estimated on few items. I did not find the significance test in the sections I read.

## Related

- [[cot-hallucination-trap]] — the same language-prior pull, here inside chain-of-thought when visual grounding is weak
- [[functional-perception-gap]] — a perception-side failure of vision-language models on a different visual task
- [[question-scoped-evidence-proxy]] — the text layer that scores the answers, and the reason a text-scored benchmark may flatter text answers
- [[counterfactual-hard-negative]] — training against fluent, plausible answers that the evidence contradicts, so that evidence outweighs the prior
- image-benefit-shrinks-with-difficulty — the same text pull in university mathematics, where the benefit of the figure falls as problems get harder

[^t1]: doi-10-48550-arxiv-2601-02536 — "frames-only, where the model receives only the visual input"
[^t2]: doi-10-48550-arxiv-2601-02536 — "Removing visual input improves proprietary model performance"
[^t3]: doi-10-48550-arxiv-2601-02536 — "higher under dialogue-only than full-modality input"
[^t4]: doi-10-48550-arxiv-2601-02536 — "indicating that these models do not extract useful signal from video frames"
[^t5]: doi-10-48550-arxiv-2601-02536 — "but this advantage collapses under frames-only"
[^t6]: doi-10-48550-arxiv-2601-02536 — "superiority is driven by stronger language priors, not better"
[^t7]: doi-10-48550-arxiv-2601-02536 — "discuss the right content but cannot extract the precise visual facts needed to answer correctly"
[^t8]: doi-10-48550-arxiv-2601-02536 — "getting the facts right is hard not because models"
[^t9]: doi-10-48550-arxiv-2601-02536 — "We use a different number of frames for each"
[^t10]: doi-10-48550-arxiv-2601-02536 — "open-source models show smaller performance drops under"
[^t11]: arxiv-2511-23112 — "a text-only condition for controlled comparison"
[^t12]: arxiv-2511-23112 — "yield no statistically significant differences in model performance"
[^t13]: arxiv-2511-23112 — "achieves 50.53% accuracy without any image input"
[^t14]: arxiv-2511-23112 — "only its own multimodal variants (original: 40.85,"
[^t15]: arxiv-2511-23112 — "altering the scale of the visual input scarcely impacts reasoning performance"
[^t16]: arxiv-2511-23112 — "predictions are largely insensitive to changes in visual form"
[^t17]: arxiv-2511-23112 — "the multimodal portion of the MathSight dataset contains 543 problems"
