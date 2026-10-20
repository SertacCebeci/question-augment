---
description: "Scene reasoning split into objects, then the physical properties a goal depends on (material, affordance, function); VLMs recognise objects well but fall 10 to 20% on property-level questions."
aliases: ["PercepTax", "perceptual taxonomy reasoning", "property-level scene reasoning", "scene-object-property hierarchy"]
sources: ["arxiv-2511-19526"]
---
# Perceptual taxonomy

A scene can be read at three levels: its layout, the objects in it, and the physical properties of those objects that a goal depends on. The Perceptual Taxonomy paper calls this structure a taxonomy and treats it as the way human perception works: "a hierarchical process of extracting structured information from visual input."[^c1] Its example is a person who needs protection, surveys a room, and must "infer which properties are required" before choosing an object to serve as a shield.[^c2] The property level has four families, material, physical attributes, affordance and function. The authors annotate them for 3,173 objects across 84 fine-grained attributes.[^c3]

The benchmark built on these annotations, PercepTax, is multiple-choice. It has 5,802 images from synthetic and real domains[^c4] and 28,033 template-based questions in four types, plus 50 expert-written questions. The measured claim is the gap between levels. Models do well on recognition, but they "degrade significantly by 10 20% on property-driven questions, especially those requiring multi-step reasoning over structured attributes."[^c5] The hardest category is taxonomy reasoning, with "accuracies ranging from 28% to 63%."[^c6] For GPT-5 the fall is larger: its real-image taxonomy score is "representing a drop of more than 29 points" below its object-level score.[^c7] The authors read this as a failure to combine cues: current VLMs "struggle to integrate material, affordance, and functionality cues into" a coherent physical picture.[^c8] On the expert set the top model reaches "the best-performing model answers only achieves 24% accuracy."[^c9]

The same hierarchy was also used as a prompt. An in-context exemplar, built from simulation data, guides the model "from scene layout to object-level physical properties before answering."[^c10] In the sections read, this raised real-image taxonomy scores for the strongest models: "Gemini improves from 63.67% to 65.90% in" taxonomy reasoning,[^c11] and "GPT-5 improves from 59.18% to 64.78%."[^c12] For an 8B open model the change was small, "Qwen3-VL-8B shows only marginal improvements," which the authors attribute to "likely due to weaker" instruction-following.[^c13]

What the split changes for a question is which step fails. A question that asks what is present can be answered by recognition, which the models do well. A question that asks which property makes an object usable needs an intermediate step, the property inference, and that is where the paper locates the failures. Its interpretation is that models "primarily rely on" associative pattern matching rather than "explicit reasoning over object and property relationships."[^c14] Treating the property level as a separate place to test is my inference from these numbers, not a result the paper states.

## Limits

- The three-level hierarchy is the authors' design, motivated by the human perception literature they cite. The sections read do not compare it with another decomposition of the same scenes.
- The in-context result covers four models and "one simulation exemplar."[^c15] The sections read compare the exemplar against no exemplar. They do not compare it with a flat exemplar that carries the same properties without the hierarchy, so the gain cannot be credited to the hierarchy alone.
- The questions are multiple-choice and scored by exact match on templates, with a small expert set of 50. A choice-format shortcut is not ruled out by the sections read. The pattern-matching reading of the failures is an interpretation of accuracy gaps; the paper does not test it directly.
- The property dictionary is the authors'. The sections read report no inter-annotator check on the 84 attributes, so the property labels, and everything built on them, are only as firm as that dictionary.
- The sim-to-real claim rests on the real-image subset of this one benchmark. Transfer to other visual tasks is not tested here.

## Related

- [[spatial-cognition-hierarchy]] — another level-wise decomposition of visual ability. That one orders spatial skills; this one orders the object properties a goal depends on.
- [[program-computed-ground-truth]] — PercepTax builds its template questions from per-object property labels. My inference is that this is the same dependency on stored metadata: questions can only test what the annotations encode.

[^c1]: arxiv-2511-19526 — "a hierarchical process of extracting structured information from visual input"
[^c2]: arxiv-2511-19526 — "infer which properties are required"
[^c3]: arxiv-2511-19526 — "We annotate 3,173 objects with four property families: material, physical attributes, affordance, and function covering 84 fine-grained attributes"
[^c4]: arxiv-2511-19526 — "benchmark with 5,802 images spanning both synthetic and"
[^c5]: arxiv-2511-19526 — "well on recognition tasks but degrade significantly by 10 20% on property-driven questions"
[^c6]: arxiv-2511-19526 — "with accuracies ranging from 28% to 63%"
[^c7]: arxiv-2511-19526 — "representing a drop of more than 29 points"
[^c8]: arxiv-2511-19526 — "integrate material, affordance, and functionality cues into"
[^c9]: arxiv-2511-19526 — "the best-performing model answers only achieves 24% accuracy"
[^c10]: arxiv-2511-19526 — "model from scene layout to object-level physical properties before answering"
[^c11]: arxiv-2511-19526 — "Gemini improves from 63.67% to 65.90% in"
[^c12]: arxiv-2511-19526 — "GPT-5 improves from 59.18% to 64.78%"
[^c13]: arxiv-2511-19526 — "Qwen3-VL-8B shows only marginal improvements"
[^c14]: arxiv-2511-19526 — "current VLMs primarily rely on"
[^c15]: arxiv-2511-19526 — "We provide one simulation exemplar"
