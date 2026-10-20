---
description: "A chain-selection test whose distractors each break exactly one of two independent constraints, visual grounding or logical coherence, so a wrong pick can be assigned to the axis it failed."
aliases: ["single-constraint distractor attribution", "dual-axis distractor diagnosis", "one-violation distractors"]
sources: ["arxiv-2512-08228"]
---
# Orthogonal violation attribution

A selection test can locate a reasoning failure, not only count it, when each wrong option breaks exactly one of two independent requirements. MM-CoT is built this way. The model sees an image or a video and must "select the sole event chain" among candidates.[^c15] The paper describes the valid chain as one "that satisfies two orthogonal constraints": visual grounding, under which every event is "factually anchored to observable evidence", and logical coherence, under which the transitions must be "physically and commonsensically valid".[^c13][^c1][^c14] The construction rule is that each distractor breaks one constraint, in the paper's words "each distractor violating exactly one constraint".[^c2]

The gain is in the label. Since every distractor is marked as either visually inconsistent or logically incoherent, a wrong pick can be read on two axes. Rejecting visually inconsistent distractors is a measure of robustness against hallucination or perception error; rejecting "causally flawed distractors that remain visually compatible" with the scene is a measure of higher-order reasoning.[^c3][^c4] The mechanism is the known edit. Each distractor is the valid chain with one thing changed, and the changed thing belongs to a named constraint, so a failure on that distractor has a location. A model that accepts the visually inconsistent distractors but rejects the logically flawed ones is failing at perception, not at inference, and the score separates the two.[^c4]

Scoring is strict. An instance counts only when the unique valid chain is selected, and the paper says this "evaluates full-chain verification rather" than partial correctness at the level of single steps.[^c5] Verification, as opposed to generation, is the frame: the authors write that "existing benchmarks emphasize generation but neglect verification".[^c6]

The attribution has a control. Removing the input tests whether an axis can be solved from the text alone. In the paper's ablation, "Removing video or image signals leads to sharp accuracy decay", and for images "removing image information similarly causes a clear accuracy decline (30%–60%)".[^c7][^c8] Construction quality was checked by a human pass over a sample: annotators "strictly verify a random 10% subset", and after filtering the noise rate was "suppressed to below 1.5%".[^c9][^c10]

## Limits

- The axis is a label assigned at construction time. It says which constraint the distractor was written to break, not where the model looked or what it perceived. Whether a failure on a visual distractor is a perception failure in the model is an inference the paper draws from the label; I did not find a step-level trace that tests it.
- The paper reports the ablation as a clear drop, not as a per-axis decomposition of the drop. The text I read gives overall and split-level accuracies, but not whether accuracy on one axis predicts accuracy on the other.
- Chance level is my arithmetic from the stated distractor counts: K=3 for images and K=4 for videos, so pick-one chance is about 25% and 20%. The paper does not state these baselines in the parts I read, so an accuracy near chance is not labelled as such there.
- The construction audit covered a random 10% of generated data; the paper reports "Kappa of 0.86" and "The Distractor Validity score (0.82)".[^c11][^c16] The sample size behind those figures was not in the portion I read.
- The abstract claims "low correlation with existing benchmarks".[^c12] I did not read the analysis behind that claim, so what it measures against is not established here.
- The construction is one pipeline over one image source (Flickr30k) and one video source (ShareGPT4Video). Whether single-violation distractors built by another procedure keep the same attribution is not tested.

## Related

- [[counterfactual-hard-negative]] — the training-side form of the same edit: a rejected answer made fluent and then wrong in one named way. Here the same move is used to score a model, and the edits are split across two constraints.
- [[controlled-error-injection]] — edits a correct answer to label a test set; the new element here is that the edits are sorted by which constraint they break.
- [[grounding-answer-dual-axis-audit]] — crosses answer correctness with evidence overlap as two measured axes; this note builds the second axis into the distractors instead of measuring it on outputs.
- [[cot-hallucination-trap]] — the fluent but ungrounded chain that the visual-axis distractors are written to catch.
- [[text-prior-over-visual-evidence]] — why removing the visual input is the check that the visual axis really needs the picture.
- [[counterfactual-image-grounding-audit]] — a related control that blanks or swaps the image to test visual dependence.

[^c1]: arxiv-2512-08228 — "factually anchored to observable evidence"
[^c13]: arxiv-2512-08228 — "that satisfies two orthogonal constraints"
[^c14]: arxiv-2512-08228 — "physically and commonsensically valid"
[^c15]: arxiv-2512-08228 — "select the sole event chain"
[^c16]: arxiv-2512-08228 — "The Distractor Validity score (0.82)"
[^c2]: arxiv-2512-08228 — "each distractor violating exactly one constraint"
[^c3]: arxiv-2512-08228 — "Because each distractor is explicitly labeled as either visually inconsistent or logically incoherent"
[^c4]: arxiv-2512-08228 — "causally flawed distractors that remain visually compatible"
[^c5]: arxiv-2512-08228 — "This strict criterion evaluates full-chain verification rather"
[^c6]: arxiv-2512-08228 — "Existing benchmarks emphasize generation but neglect verification"
[^c7]: arxiv-2512-08228 — "Removing video or image signals leads to sharp accuracy decay"
[^c8]: arxiv-2512-08228 — "removing image information similarly causes a clear accuracy decline (30%–60%)"
[^c9]: arxiv-2512-08228 — "strictly verify a random 10% subset"
[^c10]: arxiv-2512-08228 — "suppressed to below 1.5%"
[^c11]: arxiv-2512-08228 — "Kappa of 0.86, confirming that the visual evidence in MMCoT is unambiguous"
[^c12]: arxiv-2512-08228 — "low correlation with existing benchmarks"
