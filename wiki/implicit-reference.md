---
description: "An implicit reference names its target through scenario knowledge, not visible cues; on UAV imagery, grounding models locate the explicit twin of an object more accurately."
aliases: ["implicit visual grounding", "implicit VG", "implicit referring expression", "knowledge-dependent referring expression"]
sources: ["arxiv-2601-00998"]
---
# Implicit reference

An implicit reference picks out an object by what its role in the scene implies, not by what is visibly distinctive about it. Its contrast class is the explicit reference, which uses perceptual cues: a color, a relative position, a relative size. The explicit form can be checked by looking; the implicit form cannot be resolved until the reader brings in domain knowledge about the scene.

DVGBench, a drone-imagery benchmark of 2,863 annotated samples, makes the contrast a paired design. "Each object provides both explicit and implicit queries."[^c1] The explicit query for a vehicle names its color and position. The implicit query names the same vehicle by what it is doing: a vehicle making an illegal left turn against traffic, or a person trapped by floodwater. Resolving the second requires knowing what counts as a violation or as rescue-relevant, which the image does not state.

The authors argue that the explicit form is of little use in the settings they target. In UAV work, "merely stating the position presupposes the answer."[^c2] Implicit references that require domain knowledge are the ones "operationally meaningful."[^c3] (The phrase "operationally meaningful" is the authors'. My reading is that it gives the asker a reason to prefer the implicit form, since the explicit form hands over the location the asker wanted to learn.)

## How the gap is measured

The paper defines the reasoning gap by the paired design: the difference in localization accuracy between the explicit and implicit query for the same object. "Quantification of the reasoning gap as" the explicit–implicit localization performance differential is one of three uses it names for the pairs.[^c4]

On the threshold sweep in the paper's Figure 8, the best model's explicit accuracy peaks at "For explicit queries, the accuracy peaks at 63.57% with" a threshold of 0.9, while its implicit accuracy reaches "of 54.75% is attained at the 0.9 threshold."[^c5][^c6] Those are the figure's values as read from the text; they put the implicit query roughly nine points behind the explicit one for the same model. The paper gives no confidence interval for this difference in the slices I read.

On the implicit-only benchmark (Table 2), the base Qwen2.5-VL 7B with reasoning scores 43.78%, and DroneVG-R1 7B scores 52.05%.[^c7] The implicit results are what the benchmark reports as its main number. The explicit results appear only in the paired analyses.

A second consistency measure asks whether the boxes for the two queries of one object agree. The paper's DVGBench-hard split scores both queries and reports a consistency figure; the best model reaches "consistency score of 47.60%, which is the highest among" the models compared.[^c8] Its accuracy on the strict split is lower than its implicit-only accuracy, which is the expected direction.

## Why the gap exists, according to the authors

The authors offer a training-data account. Models that generate referring data at scale still produce mostly explicit referents, because they were trained on human-annotated data that is mostly explicit. Their outputs "remain biased toward" explicit references, which the authors call a cycle of bias.[^c9] This is their argument. The paper does not test it, and nothing in the slices I read isolates it from the other differences between the two query types.

## Limits

- Scale and balance. The test split has 873 samples across six scenarios. The shares are uneven (traffic 33.0%, disaster 6.1%, security 4.8%), and the overall score averages per category.[^c10]
- The implicit queries are written by hand. The authors say that "humans instinctively combine referential expressions with contextual knowledge rather than" relying on visible attributes.[^c11] That is an observation from annotation, not a sample of how operators phrase requests. Nothing in the paper checks the implicit wording against real user language.
- The twins differ in wording as well as in knowledge. The explicit query was "constructed using only explicit, scene-agnostic attributes such" as color and position.[^c12] A gap between the two therefore cannot be assigned to knowledge alone. This is my inference from the construction, not a result the paper reports.
- The infant analogy in the introduction is motivation. The authors say "infants can easily understand" color and position references but not common-sense ones.[^c13] It is not evidence about models.
- The models compared are mostly from one family (Qwen2.5-VL), and the benchmark is aerial imagery from two drone datasets. Whether the gap holds for ground imagery or other reference types is untested here.

## Related

- [[implicit-to-explicit-restatement]] — the method the authors build on this gap: the model writes the explicit twin of the query before it boxes the object.
- [[implicit-predictive-intent]] — the tabular analogue: a question whose task type is unstated is answered worse until the task type is disclosed.
- [[pragmatic-plausibility]] — counts referring expressions the answerer cannot resolve as evidence that a reading is wrong.
- [[ambi-rvos]] — a referring benchmark where the expression is ambiguous and clarification is scored, a different remedy for the same unresolved referent.

[^c1]: arxiv-2601-00998 — "object provides both explicit and implicit queries"
[^c2]: arxiv-2601-00998 — "merely stating the position presupposes the answer"
[^c3]: arxiv-2601-00998 — "that require domain knowledge are operationally meaningful"
[^c4]: arxiv-2601-00998 — "quantification of the reasoning gap as"
[^c5]: arxiv-2601-00998 — "For explicit queries, the accuracy peaks at 63.57% with"
[^c6]: arxiv-2601-00998 — "of 54.75% is attained at the 0.9 threshold"
[^c7]: arxiv-2601-00998 — "Qwen2.5VL 7B (43.78%), when both are evaluated with reasoning"
[^c8]: arxiv-2601-00998 — "consistency score of 47.60%, which is the highest among"
[^c9]: arxiv-2601-00998 — "their outputs remain biased toward"
[^c10]: arxiv-2601-00998 — "a category-averaging method when calculating the overall"
[^c11]: arxiv-2601-00998 — "humans instinctively combine referential expressions with contextual knowledge rather than"
[^c12]: arxiv-2601-00998 — "explicit references for the same targets were constructed using only explicit, scene-agnostic attributes such"
[^c13]: arxiv-2601-00998 — "infants can easily understand"
