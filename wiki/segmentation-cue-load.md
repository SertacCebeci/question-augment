---
description: "Adding color or texture to a counting prompt can pull a vision-language model's attention off the object's shape and lower its count. The load falls on the cue that segments the objects."
aliases: ["cognitive sink", "cue-induced attention suppression", "segmentation-cue overload", "cognitive load of a segmentation cue"]
sources: ["arxiv-2511-17722"]
---
# Segmentation-cue load

A counting question asks a vision-language model to do two things: find the objects, and keep count of them. Before any number is produced, the objects have to be separated from the background and from each other. The paper calls the cue that carries this separation the prompt's primary segmentation cue. Its benchmark is simple by design: black circles on a white field, with the prompt naming a color, a texture or a shape. Each attribute the prompt adds is one more thing the model must process while it is still doing the separating. The paper's account of its failures is that they come from "the cognitive load imposed by the prompt’s primary segmentation cue"[^s1], not from the step of combining attributes.

The evidence it offers is attention. In the fullest prompt, which names color, texture and shape together, the attention overlays show the model's attention to the object's shape is missing: "attention overlays confirm the model’s attention to the object’s shape is absent."[^s2] The authors attribute this to load, the shape being "suppressed by the cognitive load of processing texture"[^s3] and color. The general claim follows the same line: models "can perceptually attend to objects yet fail to" enumerate them "when competing semantic cues overwhelm the counting process."[^s4]

The same account covers texture in the scoring. Complex textures and patterns are said to "interfere with the models’ ability to reliably segment and enumerate objects,"[^s5] so the segmentation step itself degrades before counting begins. The paper names the effect a "cognitive sink." In the plainest prompt, P1, the model does best because "its very generality allows the model to deploy its most robust internal detector,"[^s6] which bypasses the sink that any specific cue creates. The paper borrows its frame from the visual attention sinks it cites as motivation, which it calls "visual attention sinks [12]."[^s7] The two are different objects. The sink in [[attention-sink]] is a set of visual tokens that absorb attention the query does not need. Here the attention lost is the object's own shape, taken by a text cue.

The load is not removed by more reasoning on the text side. The paper finds that "reasoning does not consistently improve counting performance"[^s8] in its reasoning variants, and it reads enumeration errors as stemming "primarily from visual grounding limitations"[^s9] rather than from insufficient linguistic reasoning.

For someone formulating a count question, this is my inference, not the paper's: the attributes that segment the objects belong to the question, and attributes that only describe them add load on the same process. The paper varies one feature at a time, so the drop in counting accuracy when a cue is added is measured. Which cue counts as primary, and the reading of the attention overlays, are the authors' interpretation.

## Limits

- The stimuli are synthetic by design. The paper says it "uses synthetic images by design"[^s10]. Its real-image check on a subset of FSC-147 is reported for the interventions, not for the count and cue grid. The paper itself lists real scenes as untested: the framework must be extended "to real-world scenarios with occlusion, varying scales, and complex spatial arrangements remains essential."[^s11]
- The attention evidence is a single figure: "Token-level attention heatmaps for the compositional prompt 5 of object texture task for Kimi."[^s12] That is one model and one prompt, shown as an overlay. The text does not quantify the suppression across models or prompts, and I read the overlay as qualitative.
- The load reading is an analogy. The benchmark is said to probe "a demand that mirrors cognitive challenges observed in human enumeration tasks."[^s13] No human was tested, so the cognitive-load term carries the authors' framing, not a measured human effect.
- The analysis "is limited to open-source VLMs,"[^s14] and the failure modes of proprietary models are not measured here.

## Related

- [[attention-sink]] — a different sink: visual tokens that absorb attention irrelevant to the query, in a medical LVLM; here the attention is taken from the object's shape
- [[prompt-specificity-effect]] — the same kind of added detail, whose effect changes sign with the feature it names
- [[enumeration-cue-dependence]] — whether a serial count runs at all depends on the cue; here the cue sets how much load a count already running carries
- [[count-magnitude-error]] — the other axis of the same benchmark: how many objects are counted, with the error rising past about thirty

[^s1]: arxiv-2511-17722 — "the cognitive load imposed by the prompt’s primary segmentation cue"
[^s2]: arxiv-2511-17722 — "attention overlays confirm the model’s attention to the object’s shape is absent"
[^s3]: arxiv-2511-17722 — "suppressed by the cognitive load of processing texture"
[^s4]: arxiv-2511-17722 — "models can perceptually attend to objects yet fail to"
[^s5]: arxiv-2511-17722 — "complex textures and patterns interfere with the models’ ability to reliably segment and enumerate objects"
[^s6]: arxiv-2511-17722 — "its very generality allows the model to deploy its most robust internal detector"
[^s7]: arxiv-2511-17722 — "visual attention sinks [12]"
[^s8]: arxiv-2511-17722 — "reasoning does not consistently improve counting performance"
[^s9]: arxiv-2511-17722 — "enumeration errors stem primarily from visual grounding limitations"
[^s10]: arxiv-2511-17722 — "uses synthetic images by design"
[^s11]: arxiv-2511-17722 — "framework to real-world scenarios with occlusion, varying scales, and complex spatial arrangements remains essential"
[^s12]: arxiv-2511-17722 — "Token-level attention heatmaps for the compositional prompt 5 of object texture task for Kimi"
[^s13]: arxiv-2511-17722 — "a demand that mirrors cognitive challenges observed in human enumeration tasks"
[^s14]: arxiv-2511-17722 — "analysis is limited to open-source VLMs"
