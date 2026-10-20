---
description: "Serializing each tracked entity's depth-lifted 3D positions and motion vectors into text templates beside the question gives a video VLM cues its encoder struggles to use; 3D beats 2D motion."
aliases: ["motion-trajectory serialization", "depth-lifted motion as text", "spatio-temporal cue templates for VLMs"]
sources: ["arxiv-2511-18373"]
---
# Structured motion serialization

A video vision-language model reads motion only through its visual encoder, and the MASS paper locates the shortfall there: standard encoders struggle to "utilize or correlate spatial and temporal cues effectively."[^m1] The remedy it proposes is a serialization step placed in front of the question, not a change to the backbone. The paper calls MASS "a model-agnostic approach" that injects spatial-temporal signals into the language space.[^m2]

The pipeline has three parts. First, the question is parsed for its key components, which narrow the target for visual grounding: "We begin by semantically extracting the key components" of each probing question.[^m3] Second, the queried entity is tracked across frames and its tracked motion vectors are projected into 3D with the frame's depth map: "frames with their corresponding depth maps, we project the" tracked motion over the entity's points.[^m4] Third, the result is written out as "motion-trajectory sequences for each entity, including 3D" start and end positions, motion vectors, bounding boxes within each sub-segment, and temporal indices.[^m5] These are rendered through predefined natural-language templates and fused with the tokenized question.[^m6]

The reason given for choosing text over raw features is an inherited claim. Earlier work is cited as showing that LLM backbones handle physics-related concepts better "in the language space rather than as raw visual features."[^m7] The paper's own account of the effect is one of filtering: "Providing structured representations of key video dynamics enables stronger physics comprehension and reasoning while" removing distracting visual content.[^m8] This is the paper's reading, not a separated test of the filtering step.

The one ablation that isolates the depth lift is reported in direction only in the slices read. "Replacing the full 3D motion representation with 2D motion lowers accuracy for both models."[^m9] The paper reads this as depth-aware motion carrying information that a 2D track does not: "depth-aware motion provides information that" 2D motion misses.[^m10] It also argues the drop is not just a token count effect, since "Because this ablation only removes the depth-aware projection" the 2D variant differs in that one respect.[^m11]

For someone building questions about physical processes, the transferable point is that the cues a language model needs can be measured outside the model and stated as text, and that the choice of which geometry to keep (depth-lifted or flat) changes the answer. Whether the serialization is what a question-writer would produce, or only what this pipeline produces, is not something the paper addresses.

## Limits

- The benchmark is the authors' own, "consisting of 4, 350 real-world and AIGC videos," and its annotations include the same kinds of motion grounding the serialization writes out.[^m12] The slices read do not establish whether test-time cues come from the paper's tracker, described as "a motion tracker for object dynamics,"[^m13] or from the benchmark's annotations. (My inference.)
- The templates and the depth details are "detailed in the supplementary material," which was not read.[^m14] The exact wording of the serialization is therefore not checked here.
- Accuracy is scored by an automated judge: "we use GPT-4.1-Mini as an automated judge to assess".[^m15] The judge's own errors enter every reported number, and this was not measured.
- The 2D-versus-3D and SFT-versus-GRPO comparisons are in tables whose cells were not parsed; only the direction the paper states is recorded here.
- Grounding alone is not the claimed mechanism: "Motion-aware spatiotemporal grounding is necessary but not sufficient for physics comprehension."[^m16] The paper finds that SFT on the same inputs learns "purely from input" correlations and does not help physics reasoning, while reinforcement fine-tuning does, so the serialization is not a sufficient route to better answers.[^m17]
- Generalization beyond physics questions is claimed in the supplementary material (real-world video QA), which was not read.

## Related

- [[text-bottleneck-in-visual-reasoning]] — the opposite direction for text: there, verbal reasoning degrades perception; here, verbal serialization of measured cues is the input to the model. My inference: the difference may be whether the text carries measured signal or the model's own chain of thought.
- [[symbolic-temporal-representation]] — the same move applied to time: facts are rewritten as structured predicates before a language model reasons over them.

[^m1]: arxiv-2511-18373 — "utilize or correlate spatial and temporal cues effectively."
[^m2]: arxiv-2511-18373 — "We present MASS, a model-agnostic approach"
[^m3]: arxiv-2511-18373 — "We begin by semantically extracting the key components"
[^m4]: arxiv-2511-18373 — "frames with their corresponding depth maps, we project the"
[^m5]: arxiv-2511-18373 — "motion-trajectory sequences for each entity, including 3D"
[^m6]: arxiv-2511-18373 — "representations aligned with the tokenized questions."
[^m7]: arxiv-2511-18373 — "in the language space rather than as raw visual features."
[^m8]: arxiv-2511-18373 — "Providing structured representations of key video dynamics enables stronger physics comprehension and reasoning while"
[^m9]: arxiv-2511-18373 — "Replacing the full 3D motion representation with 2D motion lowers accuracy for both models."
[^m10]: arxiv-2511-18373 — "depth-aware motion provides information that"
[^m11]: arxiv-2511-18373 — "Because this ablation only removes the depth-aware projection"
[^m12]: arxiv-2511-18373 — "consisting of 4, 350 real-world and AIGC videos"
[^m13]: arxiv-2511-18373 — "a motion tracker for object dynamics"
[^m14]: arxiv-2511-18373 — "detailed in the supplementary material"
[^m15]: arxiv-2511-18373 — "we use GPT-4.1-Mini as an automated judge to assess"
[^m16]: arxiv-2511-18373 — "not sufficient for physics comprehension."
[^m17]: arxiv-2511-18373 — "learning purely from input"
