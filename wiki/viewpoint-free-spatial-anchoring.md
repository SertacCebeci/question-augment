---
description: "Spatial words such as left and right presuppose a camera pose; dropping them and anchoring each relation to an object or to a sight line between two objects removes that dependence."
aliases: ["anchor object and anchor sight", "camera-free spatial reference", "viewpoint-independent spatial description", "spatially anchored referral"]
sources: ["arxiv-2511-18817"]
---
# Viewpoint-free spatial anchoring

A spatial clause such as "the chair on the right of the table" names a direction only once a viewer has been placed. The paper's diagnosis is that spatial descriptions "often presuppose a specific 2D camera pose that is unknown during training and evaluation".[^c1] The dialogue then carries information the answerer cannot see: the relative positions "depend on viewpoint information not present" in the context.[^c2] The mechanism proposed is not to tell the model the camera, but to write spatial clauses whose direction comes from the scene itself.

It works in two moves. The first is pruning. The scene graph records only vertical adjacency and horizontal contact, and the authors "discard multi-object relations (involving more than two nodes) and all relative directions" when they build it.[^c3] A relation that needs a viewer is removed from the graph before any question is written.

The second is anchoring. The pipeline "introduce[s] two anchors: the anchor object and anchor sight".[^c4] An anchor object gives a distance-based clause: the nearest or farthest object relative to it, which needs no direction. An anchor sight is the line connecting two objects, and the clause picks "the leftmost (or rightmost) object relative to the anchor sight".[^c5] The left and right are then defined by the two objects, not by the camera that happened to record the scene. Anchors are drawn only from non-distractor objects that already have a discriminative referral, so the clause and the target both resolve.[^c6] The clause is first templated and then rewritten by an LLM "for fluency",[^c6] which changes the wording, not the anchor.

The paper also keeps a separate repair for camera pose. Non-canonical orientations are rotated "to approximate a canonical horizontal viewpoint" in 90-degree steps.[^c7] So the pipeline both corrects the camera where it can and avoids depending on it where it cannot. The overall claim is that "we eliminated viewpoint ambiguities introduced by either manual design or LLM-generated text".[^c8]

## Limits

- No experiment in the parts I read compares a model on left/right questions with and without anchoring. The claim of elimination is the authors' design claim, and their comparison table marks datasets with a check in a column "Viewpoint-ambiguity-free", which is a classification, not a measurement.
- The text does not say how "leftmost" is oriented relative to a sight line. A line between two objects has two sides, and the choice of which side counts as left is a convention the extracted text does not state. Whether that convention is consistent across scenes is my question, not something the paper reports.
- Distances and anchors come from 7-DOF bounding boxes built on point clouds. The source scans include noise and blur, and the authors list "Glass surfaces create virtual" images that MLLMs read as view-dependent objects, which the pipeline does not remove.[^c9]
- The method is a generation-side fix. It says nothing about how a person, asked a left/right question on a real scene, would describe a direction; whether people answer anchored clauses as quickly or as accurately is not tested.
- Pruning removes relative directions, so a question that truly needs one, such as "which chair faces the window", cannot be posed in this form. The paper states the removal as a choice to "suppress noise and ambiguity"; it does not measure what is lost.[^c10]

## Related

- [[egocentric-question-viewpoint]] — a question fixed to the wearer's viewpoint; here the viewpoint is removed rather than fixed, so the direction must come from objects.
- [[object-centric-view-centric-spatial-pattern]] — object-anchored versus observer-anchored organisation of views; a sight line between two objects is an object-level frame of the same kind (my reading).
- [[discriminative-referral-construction]] — the referrals that anchored clauses are attached to, and the step that decides which objects may serve as anchors.

[^c1]: arxiv-2511-18817 — "spatial descriptions often presuppose a specific 2D camera pose that is unknown during training and evaluation"
[^c2]: arxiv-2511-18817 — "implied in a dialogue depend on viewpoint information not present"
[^c3]: arxiv-2511-18817 — "discard multi-object relations (involving more than two nodes) and all relative directions"
[^c4]: arxiv-2511-18817 — "we introduce two anchors: the anchor object and anchor sight"
[^c5]: arxiv-2511-18817 — "the leftmost (or rightmost) object relative to the anchor sight"
[^c6]: arxiv-2511-18817 — "Spatial clauses are first templated"
[^c7]: arxiv-2511-18817 — "to approximate a canonical horizontal viewpoint"
[^c8]: arxiv-2511-18817 — "we eliminated viewpoint ambiguities introduced by either manual design or LLM-generated text"
[^c9]: arxiv-2511-18817 — "Glass surfaces create virtual"
[^c10]: arxiv-2511-18817 — "To suppress noise"
