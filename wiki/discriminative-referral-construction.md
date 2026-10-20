---
description: "A referring description is built by searching attribute sets over a distractor group and keeping only those whose match set is exactly the target, then pruning redundant modifiers."
aliases: ["discriminative object referring", "discriminative object referrals", "comparative disambiguation", "exclusive referring description"]
sources: ["arxiv-2511-18817"]
---
# Discriminative referral construction

A referring phrase for an object can be chosen by search rather than by wording. The method takes a target and the objects it could be confused with, then asks which descriptors single it out. The motivation is that unconstrained object descriptions "lack discriminative features, making target objects indistinguishable from distractors".[^c1] The construction works from the group, not from the target alone. Objects are first clustered by categorical relatedness, with the label graph as a prior, so that a group holds the objects that can plausibly be confused with one another.[^c2]

Within a group, descriptors come from three comparisons: appearance, where an LLM is prompted with few-shot examples to cluster objects by attribute differences; size, where 7-DOF box volumes are compared under a tolerance; and object relations, where object-centric sub-scene graphs are contrasted.[^c3] The descriptors are then fused into a matrix of candidate sets. A candidate is kept only if the objects it matches are exactly the target, and only compact candidates survive, so each kept descriptor is distinguishing and free of "without any redundant descriptors".[^c4] This is the same test that [[referent-match-set-ambiguity]] types as a question's match set, here used on purpose: a phrase whose match set has one member is unambiguous by construction (my reading).

Objects with no distractor get no comparison. Their label or caption is used directly, and a spatially anchored clause is added when plain descriptors cannot separate an object from its group: the nearest or farthest object relative to an anchor object, or the leftmost or rightmost relative to an anchor sight.[^c5] That second mechanism is treated in [[viewpoint-free-spatial-anchoring]].

## What the construction changes

The usual alternative is to drop the problem. A trivial baseline would discard every object that has a distractor, which avoids confusion at the cost of most annotations. The authors report that their strategy lets the pipeline "retain a substantially larger subset of annotated objects from the source dataset" than that baseline, in their Figure 6b.[^c8] The count itself is in a figure whose numbers were not in the extracted text, so the size of the gain is the authors' description, not a value I could read.

The construction is also checked by people. Annotators compared the 2D and 3D views of target and distractor objects, and "In total, 12% of the descriptions (130/1092) were revised."[^c6] Most of those edits were not factual fixes: "the majority of edits introduced by human annotators do not rectify factual inaccuracies but instead refine imprecise wording".[^c7] Words such as "largest" fit regular objects badly, so floor lamps and blankets were re-described by hand.

The authors use this as a point of comparison for human-written benchmarks. They cite a re-evaluation that "reports only 62% and 80% accuracy on ScanQA and SQA3D", and argue their descriptions carry less label noise.[^c11] That comparison is between label sets, not between two ways of writing referring phrases on the same scenes.

## Limits

- Exclusivity holds only over the descriptors the pipeline has. An attribute that no comparison produces cannot separate two objects, so a phrase can be "exclusive" in the pipeline's sense and still be confusable for a human who sees a different feature. This is my inference from the algorithm; the text does not test it.
- The human check covered "object descriptions generated in the Comparative Disambiguation stage",[^c9] not the spatially anchored clauses, which the authors say exhibit "low manual annotation accuracy".[^c13] The exclusivity of the anchored part is therefore less checked than the rest.
- Retention is not the same as label quality. "Dense or poorly delineated objects are often skipped",[^c10] so the source annotations limit what can be kept at all.
- The ablations I read cover training schedule and task mixing (Figure 8). I did not find one that removes the referral step while holding the rest of the pipeline fixed, so the claim that discriminative referrals improve downstream training is not isolated here.
- The method is written for the 3D scans of five source datasets and an LLM-and-MLLM stack. Whether phrases built this way match what people say in conversation was not tested; the authors' own summary is that the framework "resolves ambiguities present in earlier datasets while raising task difficulty".[^c12]

## Related

- [[referent-match-set-ambiguity]] — types an ambiguous phrase by the size of its match set; this note constructs phrases whose match set is one.
- [[referring-cue-density]] — counts discriminating cues per word; the pruning of redundant descriptors here applies the same discipline during construction.
- [[viewpoint-free-spatial-anchoring]] — the anchored clause used when plain descriptors fail, and why it avoids the camera.
- [[distractor-strength-reward-signal]] — distractors there are chosen by how often a model picks them; here the distractor group is built from labels and geometry.

[^c1]: arxiv-2511-18817 — "lack discriminative features, making target objects indistinguishable from distractors"
[^c2]: arxiv-2511-18817 — "Objects are clustered by categorical relatedness"
[^c3]: arxiv-2511-18817 — "LLM is prompted with few-shot examples to"
[^c4]: arxiv-2511-18817 — "without any redundant descriptors"
[^c5]: arxiv-2511-18817
[^c6]: arxiv-2511-18817 — "In total, 12% of the descriptions (130/1092) were revised"
[^c7]: arxiv-2511-18817 — "the majority of edits introduced by human annotators do not rectify factual inaccuracies but instead refine imprecise wording"
[^c8]: arxiv-2511-18817 — "retain a substantially larger subset of annotated objects"
[^c9]: arxiv-2511-18817 — "object descriptions generated in the Comparative Disambiguation stage"
[^c10]: arxiv-2511-18817 — "Dense or poorly delineated objects are often skipped"
[^c11]: arxiv-2511-18817 — "reports only 62% and 80% accuracy on ScanQA and SQA3D"
[^c12]: arxiv-2511-18817 — "Our framework resolves ambiguities present in earlier datasets while raising task difficulty"
[^c13]: arxiv-2511-18817 — "low manual annotation accuracy"
