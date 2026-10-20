---
description: "Models plan for other agents better than for their own motion, and a task needing both self and other cues is hardest, so the reference frame a question fixes is part of its difficulty."
aliases: ["egocentric versus exocentric planning gap", "self-other reference asymmetry", "self-centred versus other-centred planning"]
sources: ["arxiv-2512-23219", "arxiv-2512-02340"]
---
# Self-other planning asymmetry

A planning question can ask about the motion of someone else or about the answerer's own motion. MM-UAVBench, a benchmark of multimodal models on low-altitude drone footage, splits its air-ground collaborative planning task into two parts: exocentric planning, "which focuses on predicting or planning for ground objects"[^c1], and egocentric planning, the drone's own goal-directed decision. The split is the authors' decomposition of one task, applied to the same items.

The measured result is an asymmetry. Across the models evaluated, performance is consistently higher on exocentric planning than on egocentric planning.[^c2] The authors read this as models being "adept at interpreting external scene dynamics than reasoning about their own actions"[^c2]. A third condition, where the answer must integrate self-centred and other-centred cues, is lower again for all models[^c3]. The authors' interpretation is that current models "struggle to ground predictions in their own embodiment and to generate coherent plans"[^c3].

The mechanism is stated only at the level of the authors' reading: the answerer must tie a predicted action to its own position in the scene, and the evidence for that is a motion relative to a viewpoint the answerer has to occupy. That account is mine, not a tested mechanism. What the paper shows is the gap itself, on this benchmark.

The asymmetry also bears on formulation. The same benchmark fixes the viewpoint of each question in advance: "the annotation protocol explicitly specifies whether the reference frame is the UAV itself or a ground" agent, because "MLLMs often produce inconsistent results across different viewpoints" of the same question[^c4]. So the asker does not only choose what to ask about; the frame in which the question is posed is a variable that changes the answer. Compare the referring-expression case, where a directional term is ambiguous until its frame is fixed, as in [[refguard-decision-policy]] and [[identity-switch]].

The same variable shows up in a multi-view benchmark, though there the frame is the organization of the views rather than the answerer's role. On ReMindView-Bench, VLMs "perform better in object-centric than view-centric conditions",[^c6] and questions that change the viewpoint "reveal large performance degradation";[^c8] the authors read this as "indicating weak cross-view constancy and reference-frame alignment".[^c7] Two papers, two different frames, one lesson: a question's frame is part of its difficulty. See [[object-centric-view-centric-spatial-pattern]] for the view-side measurement.

## Limits

- One benchmark, one task family, 16 models of mixed kinds[^c5]. The paper does not show that the two parts differ only in perspective; they may also differ in option format, scene content or answer length. An ablation holding those fixed is what would isolate the perspective effect, and it is not in the text.
- The "mixed" condition's lower score is measured on this data only. The interpretation that models "struggle to ground predictions in their own embodiment" is the authors' reading, not a tested cause.
- The paper's orientation-prediction finding (one model almost never predicting left or right turns) is a separate, model-specific bias on the same drone viewpoint. It is not shown to be the same mechanism as the self-other gap.
- The reference-frame protocol is stated as a remedy for annotation; the paper does not measure how much accuracy changes when the frame is fixed versus left open.

## Related

- [[refguard-decision-policy]] — a reference frame left open is an ambiguity to resolve before answering; the same variable at the level of referring expressions
- [[identity-switch]] — a directional term read in the wrong reference frame yields a confident answer to a different question
- [[object-centric-view-centric-spatial-pattern]] — the same frame question at the level of how multiple views are organized around an object or an observer

[^c1]: arxiv-2512-23219 — "which focuses on predicting or planning for ground objects"
[^c2]: arxiv-2512-23219 — "adept at interpreting external scene dynamics than reasoning about their own actions"
[^c3]: arxiv-2512-23219 — "their own embodiment and to generate coherent plans."
[^c4]: arxiv-2512-23219 — "the annotation protocol explicitly specifies whether the reference frame is the UAV itself or a ground"
[^c5]: arxiv-2512-23219 — "Extensive experiments on 16 open-source and proprietary MLLMs"
[^c6]: arxiv-2512-02340 — "perform better in object-centric than view-centric conditions"
[^c7]: arxiv-2512-02340 — "indicating weak cross-view constancy and reference-frame"
[^c8]: arxiv-2512-02340 — "reveal large performance degradation"
