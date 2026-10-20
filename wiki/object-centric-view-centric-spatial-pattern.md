---
description: "Vision-language models answer object-centric multi-view spatial questions better than view-centric ones, so the organizing frame of a spatial scene changes how hard the same question is."
aliases: ["object-centric versus view-centric", "object-centric and view-centric spatial patterns", "object-centric vs view-centric representation"]
sources: ["arxiv-2512-02340"]
---
# Object-centric versus view-centric spatial pattern

Visual cognition separates two ways a set of views can be held together. In an object-centric representation the object is the anchor: it integrates several views of one thing, and what it preserves is "maintaining geometric identity across views".[^c1] A view-centric representation instead "reflects spatial organization tied to the observer",[^c2] so the layout follows where the observer stands. The same photographs can show one object from several sides or a room from several positions, and the two organizations call for different comparisons across views.

ReMindView-Bench, a multi-view benchmark for vision-language models (VLMs), builds this contrast into its design. It "systematically organizes scenes according to object-centric and view-centric spatial patterns".[^c3] For each scene the authors render views so that "we render 4 canonically orthogonal views for each target object",[^c4] under both patterns. The scene content is held fixed while the way the views relate to the object or to the observer is varied.

The direction of the measured gap is consistent. Across 15 VLMs,[^c5] models "perform better in object-centric than view-centric conditions".[^c6] The authors read the gap as models that "rely on within-view visual cues but fail to maintain relational consistency across view".[^c7] The loss is concentrated in questions that change the viewpoint: "tasks involving perspective-changing or relative direction queries reveal large performance degradation".[^c8]

My inference, not the paper's claim: if the pattern is a property of how the views are organized, then two questions with the same wording can differ in difficulty depending on the set of views they are asked over. The paper does not test this directly. It compares the two patterns as benchmark conditions, and the reading that they are the same kind of difficulty as a question's frame is mine.

The same logic of a fixed reference frame appears in [[self-other-planning-asymmetry]], where the frame is the answerer's own role. Here the frame is how the views are organized around an object or an observer.

## Limits

- The scenes are synthetic indoor layouts: "Each 3D scene is imported into" Blender for rendering.[^c9] The text read does not show the contrast on photographs or on real multi-view capture.
- The two patterns are the authors' operationalization, drawn from earlier work on spatial memory. The paper measures a gap in model accuracy; it does not test the cognitive mechanism the patterns are named after.
- The benchmark also varies layout and clutter: "We incorporate scene variability in layout diversity and"[^c10] object densities. The reported pattern comparison is not shown to hold those fixed.
- The per-model and per-query numbers sit in tables that were not extracted in full here. What this note records is the direction of the gap, not its size.

## Related

- [[self-other-planning-asymmetry]] — the reference frame a question fixes as a source of difficulty; there the frame is the answerer's role, here it is how the views are organized.

[^c1]: arxiv-2512-02340 — "maintaining geometric identity across views"
[^c2]: arxiv-2512-02340 — "reflects spatial organization tied to the observer"
[^c3]: arxiv-2512-02340 — "according to object-centric and view-centric spatial patterns"
[^c4]: arxiv-2512-02340 — "we render 4 canonically orthogonal views for each target object"
[^c5]: arxiv-2512-02340 — "Evaluations of 15 current VLMs"
[^c6]: arxiv-2512-02340 — "perform better in object-centric than view-centric conditions"
[^c7]: arxiv-2512-02340 — "rely on within-view visual cues but fail to maintain relational consistency across view"
[^c8]: arxiv-2512-02340 — "reveal large performance degradation"
[^c9]: arxiv-2512-02340 — "Each 3D scene is imported into"
[^c10]: arxiv-2512-02340 — "We incorporate scene variability in layout diversity and"
