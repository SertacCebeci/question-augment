---
description: "Wearable-camera capture degrades the image a question is answered from: on WearVQA, unzoomed and occluded images cost the most accuracy, while low light costs little."
aliases: ["wearable image degradation", "egocentric image quality", "capture-side visual degradation", "unmagnified and occluded capture"]
sources: ["arxiv-2511-22154"]
---
# Egocentric capture degradation

A camera worn on the body produces images that a curated photograph does not. The wearer's movement blurs them, the body crops them, a hand or hair hides the subject, and a wide lens leaves distant things too small to read. The WearVQA benchmark names the defects it found in its images: it covers "six types of media quality issues common in such contexts", namely unzoomed, occluded, rotated, cut off, blurred and low light.[^c1] Each has a mechanism tied to the wearer. Blur is "prevalent in egocentric scenarios due to the" movement of walking, running or gesturing.[^c2] Unmagnified images "suffer from a lack of sufficient magnification or zoom", which matters when the subject is at a distance.[^c3] In occlusion "the primary object is partially obscured by intervening objects", here often hands or hair.[^c4] The benchmark reports that "54% of the images exhibit at least one of these issues".[^c5]

The mechanism for an answerer is simple. It must read the image before it can answer, so a defect that removes the evidence the question needs (small text, a partly hidden object) removes the answer with it. The benchmark measures this as a drop: accuracy falls "by 5-16%" on the images with quality issues, across the models it tested.[^c6] Split by defect, the paper reports that "small images when unzoomed stands as the biggest challenge (35% top-1)", and that "Occlusion presents another big challenge (42% top-1)".[^c7][^c8] The "top-1" figure is the paper's own; I read it as the best model's accuracy on that slice.

Low light is the exception. The paper reports minimal impact on answer quality and offers a hypothesis: "in low light, the primary subject is more prominent with focused illumination, whereas other distracting elements are obscured by darkness."[^c9] So the defect that looks worst to a human eye is not the one that hurts the answerer most. Raw pixel count does not explain the pattern either: when the same high-resolution images were downscaled, the paper found that "we do not find clear patterns", with some models gaining and others losing.[^c10] My inference from these numbers is that what matters is whether the defect removes the information the question asks for, not how many pixels the image has.

## Limits

- The defects were sampled, not applied. Annotators were told "to include images with quality issues", so the same scene is not captured once clean and once degraded.[^c11] Per-defect effects are therefore mixed with scene and question type; the paper's own question-type slices show large differences that are not separated from defect effects.
- The authors say slices were sized "ensuring statistically significant metric readings".[^c12] The text read reports no test. The per-defect figures are top-1 accuracies across models, not significance-tested differences.
- The low-light result is a hypothesis the paper states, not something it tests.
- The images are static frames. The paper says its design "fails to adequately capture the temporal dynamics inherent in real-world scenarios", so blur as a process over time is not measured.[^c13]
- One benchmark, English-only queries, and a fixed set of models. Whether the ranking of defects holds for other capture devices is not shown.

## Related

- [[weak-channel-addition-penalty]] — when the text alone suffices, an image the model reads poorly lowers accuracy below text-only; a degraded wearable frame is one way that happens
- [[visual-robustness-score]] — separates grounded answers from lucky ones under a misleading text cue; a different axis from how the capture was degraded
- [[occlusion-logprob-saliency]] — there a researcher places an occluder to see what an answer leans on; here the occlusion is already in the capture
- [[egocentric-question-viewpoint]] — the question side of the same wearable setting: what the asker refers to when the frame is the reference

[^c1]: arxiv-2511-22154 — "six types of media quality issues common in such contexts"
[^c2]: arxiv-2511-22154 — "Blurred images are prevalent in egocentric scenarios due to the"
[^c3]: arxiv-2511-22154 — "Images that suffer from a lack of sufficient magnification or zoom"
[^c4]: arxiv-2511-22154 — "Images where the primary object is partially obscured by intervening objects"
[^c5]: arxiv-2511-22154 — "Notably, 54% of the images exhibit at least one of these issues"
[^c6]: arxiv-2511-22154 — "drops by 5-16% on images affected"
[^c7]: arxiv-2511-22154 — "small images when unzoomed stands as the biggest challenge (35% top-1)"
[^c8]: arxiv-2511-22154 — "Occlusion presents another big challenge (42% top-1)"
[^c9]: arxiv-2511-22154 — "we hypothesis that this is because, in low light, the primary subject is more prominent with focused illumination"
[^c10]: arxiv-2511-22154 — "Interestingly, we do not find clear patterns"
[^c11]: arxiv-2511-22154 — "We also instructed annotators to include images with quality issues"
[^c12]: arxiv-2511-22154 — "ensuring statistically significant metric readings"
[^c13]: arxiv-2511-22154 — "fails to adequately capture the temporal dynamics inherent in real-world scenarios"
