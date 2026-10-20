---
description: "A task-irrelevant cue placed in the same image as the target pulls a vision-language model's wrong answers toward the cue's own answer, and the drift grows as accuracy falls."
aliases: ["visual distractor capture", "adversarial cue drift", "distraction likelihood", "co-present cue capture"]
sources: ["arxiv-2511-17004"]
---
# Distractor-cue capture

When a target object and a conflicting cue share one image, a vision-language model (VLM) can answer about the cue instead of the target. The signature shows up in the errors more than in the hits. Among the wrong answers, the share that lands on the cue's answer rises as accuracy falls: "the greater the tendency for its inaccurate predictions to drift directly toward" the perturbation cues.[^c1] The paper reports this across models and subregions as a strong negative relation, with the correlation "scoring at −0.76".[^c2]

The cue is a flag or a landmark of another country, stacked onto a photo of a cultural item (cuisine, attire, or a musical instrument), or generated into the image. Accuracy drops under both methods, and the generated version is worse: "accuracy drops heavily under simple image-stacking perturbations and even worsens with its image-generation-based" variant.[^c3] The average worsening is 17.34% for generative perturbation,[^c4] against 8.43% for stacking.[^c5] The cue is not uniform in strength. The flag does most of the damage: "a decline of up to 18.4%, whereas applying the landmark perturbation resulted in a minor drop of only up" to 6.9%.[^c6]

The paper's account of the mechanism is attention. It states the model is prone to "rely on easily interpretable visual cues", so that it can be "overridden by familiar visual shortcuts".[^c7] On one open model (a 30B variant), the attention focus on image tokens "was disproportionately driven by specific text components" such as system tokens, geographic tokens and some stopwords.[^c8] Removing those tokens from the prompt raised grounding accuracy and moved attention "back to the intended image region".[^c9] The paper's summary is that the failures "stem from systematic attention shifts toward distracting cues".[^c10] So two channels feed the capture: the image cue draws attention, and the wording of the question adds to that draw.

The identity of the cue matters too. Cues built from the nearest item in description-embedding space, the "hard" pairs, are expected to be the most confusing, because "a higher similarity value indicates that the items share" strong semantic overlap.[^c11] The paper finds that "distinguishing morphologically similar items and items" from nearby cultures stays hard.[^c12]

What this changes for asking and answering, as my reading and not a result of the paper: when a scene holds a second object with a strong prior, the errors have a predictable direction, toward that object's answer. An answerer who gets a wrong answer can check whether it matches the cue before attributing it to the target. A question can be worded to keep the cue from being the reference point, though the paper's prompt ablation shows this does not always help.

## Limits

- The −0.76 relation is a correlation across subregions for each model. It does not intervene on the cue, so it shows co-variation of drift and accuracy, not that the cue causes the error.
- The attention analysis covers one open model, chosen because its errors were "less random", not all fourteen benchmarked models.[^c13] The attention result is a visualisation plus an ablation, not a causal account of each error.
- The prompt ablation is mixed. In one attire case "a prompt correction even turned a previously correct answer into a" wrong one.[^c14]
- A second error source is not separated from capture. Models over-predict some countries even without a cue, and the paper "hypothesize[s] that this over-representation may arise" from training-data prevalence.[^c15]
- The suite covers three categories, two cue types (flag, landmark) and two perturbation methods, all cultural. Whether non-cultural cues, or human answerers, drift the same way was not tested here.

## Related

- [[salience-relevance-decoupling]] — the text-side analogue: slot binding follows salience instead of relevance. Here the cue is visual and co-present, and the measured signature is the direction of the errors.
- [[segmentation-cue-load]] — a colour or texture cue pulls attention off the object in a counting prompt; the same attention channel, a different task.
- [[instruction-steered-cue-reliance]] — the wording of a question moves which cue a multimodal answerer relies on, which is the prompt-token channel above.
- [[max-distractor-similarity-difficulty]] — similarity to a rival orders difficulty for closed items; the hard-pair construction applies the same idea to cultural cues.

[^c1]: arxiv-2511-17004 — "the greater the tendency for its inaccurate predictions to drift directly toward"
[^c2]: arxiv-2511-17004 — "the correlation of this relationship is also scoring at −0.76"
[^c3]: arxiv-2511-17004 — "accuracy drops heavily under simple image-stacking perturbations and even worsens with its image-generation-based"
[^c4]: arxiv-2511-17004 — "leading to an average performance worsening of 17.34%"
[^c5]: arxiv-2511-17004 — "compared to only 8.43% drop using image-stacking"
[^c6]: arxiv-2511-17004 — "a decline of up to 18.4%, whereas applying the landmark perturbation resulted in a minor drop of only up"
[^c7]: arxiv-2511-17004 — "VLMs tend to rely on easily interpretable visual cues"
[^c8]: arxiv-2511-17004 — "attention focus on the image tokens was disproportionately driven by specific text components"
[^c9]: arxiv-2511-17004 — "in attention back to the intended image region"
[^c10]: arxiv-2511-17004 — "failures stem from systematic attention shifts toward distracting cues"
[^c11]: arxiv-2511-17004 — "A higher similarity value indicates that the items share"
[^c12]: arxiv-2511-17004 — "distinguishing morphologically similar items and items"
[^c13]: arxiv-2511-17004 — "to select its 30B variant for deeper"
[^c14]: arxiv-2511-17004 — "where a prompt correction even turned a previously correct answer into a"
[^c15]: arxiv-2511-17004 — "We hypothesize that this over-representation may arise"
