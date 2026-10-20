---
description: "Multimodal models fail where an answer needs exact coordinates, stable object-location binding or counting under clutter, not where it needs recognition; prompt optimization leaves that gap open."
aliases: ["grounding-precision hardness", "structural CAPTCHA hardness", "fine-grained localization hardness", "compositional-consistency hardness"]
sources: ["arxiv-2512-02318"]
---
# Grounding-precision hardness

How hard a visual question is for a multimodal model is not the same as how hard the thing it names is to recognise. The CAPTCHA study this note draws on puts the split on the answer's structure: robustness "is governed less by semantic recognition difficulty and more by grounding precision and compositional consistency".[^c1] The hard tasks it names need "fine-grained spatial grounding in continuous image space" and "precise binding between objects and their locations",[^c2] together with "counting or aggregation under visual clutter".[^c3]

The mechanism is a gap between what a model can say and what it must output. The authors report that models "often exhibit correct high-level reasoning in natural language", yet "they frequently fail to translate this reasoning into exact coordinates, stable multi-object bindings, or accurate counts".[^c4] A correct description of the scene therefore does not yield a correct answer when the answer has to be a position, a set of bindings between several objects and several places, or a count across a cluttered view. An answer that is a label chosen from named options does not carry that requirement.

The benchmark shows the split at the level of task types. Across seven models and 18 CAPTCHA types, the types that stress grounding and counting "have cross-model averages well below 30%",[^c5] while recognition-style tasks "already exceed 60% on average, suggesting that they are easy targets" for automated solvers.[^c6] Prompt optimization is the natural remedy and it helps one side only: it lifts the recognition tasks further and, in the authors' words, fails "to significantly improve performance on tasks requiring complex spatial grounding or counting".[^c7]

The structure is also what the authors manipulate. Their proof of concept hardens a task that models already solve, Select_Animal, by "incorporating fine-grained localization and implicit counting",[^c8] and the success rate of the strongest models falls "decreasing from over 95% to 0%".[^c9] The design claim rests on that change of structure, not on a change of object category.

My reading, not the paper's: the same split should hold for questions put to a reader rather than a model. A question whose answer is a location, a binding or a count asks for a commitment that fluent prose does not supply, so the difficulty sits in the form of the answer and can be checked against it.

## Limits

- The grouping into recognition and grounding tasks is the authors' categorisation of 18 task types. The paper does not vary the structure of one task while holding its content fixed, so "structure, not content" is supported by the contrast between task types and by one manipulation, not by a controlled ablation.
- The account of why models fail (reasoning that does not become coordinates) is drawn from their analysis of reasoning traces. I did not read the trace section in full; the claim is the authors' interpretation of those traces, not a test of what the model perceived.
- The proof of concept is one task type (Select_Animal) against state-of-the-art models. Whether the same hardening transfers to the other task types, or to non-adversarial questions, is not shown.
- Hardness is scored as pass@1 under a retry cap and a 40% working threshold chosen by the authors. A different threshold or a different retry model moves the boundary between "easy" and "hard".
- The work concerns visual inputs to adversarial tests. That a text-only question with a count or a binding is hard for a model in the same way is my extension, not something this study measured.

## Related

- [[clutter-induced-recognition-error]] — one figure's misread polarity under excess content, repaired by a crop; this note is about whole task types whose answer form stresses the model
- [[perception-cognition-gap]] — values read correctly while the rules they encode are misinterpreted; a different split between reading and interpreting
- [[construction-parameter-difficulty-dial]] — difficulty set by generation parameters before items exist; here hardness is measured after the fact across task types and then changed by altering structure
- [[coarse-to-fine-evidence-zoom]] — a zoom raises the resolution of a span; it is one attempt at the fine-grained localization that this note finds hard

[^c1]: arxiv-2512-02318 — "governed less by semantic recognition difficulty and more by grounding precision and compositional consistency"
[^c2]: arxiv-2512-02318 — "they require finegrained spatial grounding in continuous image space, precise binding between objects and their locations"
[^c3]: arxiv-2512-02318 — "counting or aggregation under visual clutter"
[^c4]: arxiv-2512-02318 — "they frequently fail to translate this reasoning into exact coordinates, stable multi-object bindings, or accurate counts"
[^c5]: arxiv-2512-02318 — "have cross-model averages well below 30%"
[^c6]: arxiv-2512-02318 — "exceed 60% on average, suggesting that they are easy targets"
[^c7]: arxiv-2512-02318 — "to significantly improve performance on tasks requiring complex spatial grounding or counting"
[^c8]: arxiv-2512-02318 — "incorporating fine-grained localization and implicit counting"
[^c9]: arxiv-2512-02318 — "decreasing from over 95% to 0%"
