---
description: "A cognitive task has two separable axes, the type of operation (Bloom) and its depth (Webb DOK); the EduEval authors argue a single axis is insufficient to classify educational tasks."
aliases: ["operation type and depth", "Bloom and DOK combined", "EduAbility two-axis taxonomy", "type-depth cognitive taxonomy"]
sources: ["arxiv-2512-00290"]
---
# Two-axis cognitive demand (operation type and depth)

A task's cognitive demand is described along two axes that the usual taxonomies keep apart. One is the *type of operation* performed (recall, interpretation, application, analysis, creation), which is what Bloom's taxonomy sorts. The other is the *depth* of the task, meaning how much rigour and how many steps it asks for, which is what Webb's Depth of Knowledge (DOK) levels sort. The EduEval authors state the split directly: "Bloom’s framework emphasizes the type of cognitive operation, while DOK emphasizes the depth and rigor of tasks."[^c1] Their claim is that "cognition is multidimensional and dynamic, so a single-axis view (type-only or depth-only) is insufficient."[^c2]

The authors do not leave the two axes free. They fix a mapping between them: "Memory and Understanding align with foundational processes and lower depth (roughly DOK 1–2, lower-order skills in Bloom)."[^c3] Application and Reasoning sit at roughly DOK 3, Creativity at DOK 4, and a sixth level, Ethics, is added because it is "not explicitly covered by traditional cognitive taxonomies."[^c4] The six levels are meant as "an interconnected scaffold rather than a strict ladder."[^c5] Assignment follows a rule: "identify the dominant cognitive operation, then determine the required depth."[^c6] Secondary processes are recorded but "do not override the primary label."[^c10]

The split is backed in the paper by one observed pattern, not by a test of the split against a one-axis rival. Across the evaluated models, few-shot prompting moved results differently by level: "Classroom dialogue classification and ethical reasoning tasks benefit from examples,"[^c7] while memory tasks stayed flat "since factual recall depends primarily on pre-training knowledge."[^c11] Read this way, a single difficulty label would hide that the same intervention helps one operation type and not another. That reading is mine, not the authors'.

For asking, the consequence I draw is that a question's level is two values, not one. The wiki's [[high-order-question-framework-comparison]] note treats Bloom's upper levels as the target of generated questions; the depth axis is what a "high-order" label does not carry. (My inference; the paper does not make this point about questions.)

## Limits

- The Bloom-to-DOK correspondence is the authors' construction, not an established equivalence. The paper says the "current mapping and definitions are optimized for Chinese K–12 contexts and LLM assessment,"[^c8] and that the framework "can be refined."[^c8]
- The paper points to its Appendix B for "empirical validation of this taxonomy."[^c9] The part of the text read here is the theoretical summary; the validation itself was not checked.
- The few-shot pattern is a difference in model scores across levels. It does not show that the two-axis labels predict those differences better than a single-axis label would. No such comparison is reported in the parts read.
- The Ethics level sits outside both source frameworks. It is an addition, and its status as a cognitive level, rather than a content area, is the authors' choice.
- Everything here concerns models being evaluated on educational tasks in Chinese K–12 settings. Whether the split helps someone judge or formulate a human question is untested in this work.

## Related

- [[high-order-question-framework-comparison]] — the same Bloom levels used as a grounding for generated questions; the depth axis is what that note's "high-order" label leaves out
- [[divergent-questioning]] — a second question-generation grounding, tested in the same study against Bloom's levels

[^c1]: arxiv-2512-00290 — "Bloom’s framework emphasizes the type of cognitive operation, while DOK emphasizes the depth and rigor of tasks."
[^c2]: arxiv-2512-00290 — "cognition is multidimensional and dynamic, so a single-axis view (type-only or depth-only) is insufficient"
[^c3]: arxiv-2512-00290 — "Memory and Understanding align with foundational processes and lower depth (roughly DOK 1–2, lower-order skills in Bloom)."
[^c4]: arxiv-2512-00290 — "which is not explicitly covered by traditional cognitive taxonomies."
[^c5]: arxiv-2512-00290 — "them as an interconnected scaffold rather than a strict ladder."
[^c6]: arxiv-2512-00290 — "identify the dominant cognitive operation, then determine the required depth."
[^c7]: arxiv-2512-00290 — "Classroom dialogue classification and ethical reasoning tasks benefit from examples because they clarify task specific conventions and evaluation criteria."
[^c8]: arxiv-2512-00290 — "The current mapping and definitions are optimized for Chinese K–12 contexts and LLM assessment; as data and use cases broaden, the framework can be refined"
[^c9]: arxiv-2512-00290 — "empirical validation of this taxonomy are extensively discussed in the Appendix B."
[^c10]: arxiv-2512-00290 — "do not override the primary label."
[^c11]: arxiv-2512-00290 — "since factual recall depends primarily on pre-training knowledge"
