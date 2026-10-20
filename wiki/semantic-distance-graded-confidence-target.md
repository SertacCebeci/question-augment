---
description: "Confidence targets can be graded by label geometry: a wrong emotion label near the true one earns more confidence than a distant one, so near-misses are not scored like gross errors."
aliases: ["graded confidence target", "semantic-distance confidence target", "near-miss confidence grading"]
sources: ["arxiv-2512-15528"]
---
# Semantic-distance graded confidence target

A verbalized confidence is usually trained against a binary target: 1 when the answer is right, 0 when it is wrong. Wu et al. replace that target, for a visual emotion task, with one that depends on how wrong a wrong answer is. Their reason is that emotion labels are not interchangeable. The authors put the categories on a loop built from the NRC VAD lexicon, so that the gap between two labels is measured along that loop: "a perimeter-based normalized semantic distance between any two emotion categories".[^c1] For a hierarchical taxonomy the loop is constrained so that subcategories sharing a parent stay adjacent.

The target is then assembled from two parts, as I read the paper's formula. For a correct answer it rises with the model's own token probability, averaged over the response. For a wrong answer it starts from one half and is reduced by the product of the semantic distance and that same average probability. A near-miss therefore keeps more confidence than a distant error, and a wrong answer the model was very sure of gets a lower target than one it hedged on. The authors state the intent directly: "for an image labeled as amusement, the model should assign higher confidence estimation to an erroneous prediction of contentment than to one of anger."[^c2]

Where the target enters the pipeline matters. In the second stage, a reasoning path is given a confidence value "quantified by the deviation between the predicted emotion and the ground-truth label," and the model is fine-tuned to emit it.[^c3] In the third stage, the reinforcement reward is different: the log-likelihood term "encourages high confidence for correct predictions and low confidence for incorrect ones," with no distance in it.[^c4] So, as far as the sections read show, the graded signal reaches the model through supervised tuning, and the reinforcement stage sees only correctness.

The reported effect is for the whole pipeline. "EmoCaliber achieves an ECE of 13.63, which is nearly half that of the second-best baseline, Qwen3-VL (Ans) at 26.31" on in-domain emotion recognition.[^c5] That number does not isolate the graded target from the structured reasoning, the verbalization stage, or the reinforcement stage.

## Limits

- No comparison of the graded target against a binary one appears in the sections read. The calibration gain is attributed to the system as a whole, so the claim that distance grading helps is not established here.
- The distance is a proxy. It is the arc between category positions on a loop built from one affect lexicon. Whether the ordering of "near" and "far" errors is stable under another affect model, or matches what viewers confuse, is not tested. The paper gives no measure of perceptual confusability.
- The paper's motivation is that verbalized confidence conveys "the plausibility of alternative interpretations," not only the model's competence.[^c6] Calibration is scored against one majority label per image. Whether the confidence tracks other readings that viewers would accept is not measured.
- The trade-off is named by the authors. "it is inherently challenging to simultaneously prevent overconfidence in fine-grained multi-class tasks and ensure sufficient confidence in coarse-grained binary tasks."[^c7] A ring of two labels carries little distance information, so the graded target probably does less on binary tasks (my inference, not measured).
- The probability term makes the target depend on how sure the model was of the wrong answer. That couples the target to the model's own token probabilities, which the paper does not compare against other sources of confidence.

## Related

- [[calibration]] — the property a confidence target is trying to make true; the paper's ECE, Brier and AUC are the calibration measures in use here.
- [[log-score-verbalized-confidence-reward]] — also grades confidence over an ordinal scale, but through the reward rather than the training target, and the distance there is numeric, not semantic.
- [[annotator-disagreement-calibration]] — also treats label ambiguity as the thing to calibrate to, but through annotator shares instead of a distance between labels.
- [[exact-match-versus-weighted-agreement]] — weighted agreement that credits adjacent-category errors; the same intuition applied on the scoring side.
- [[advantage-normalization-confidence-collapse]] — the reinforcement-stage failure this paper met when confidence was rewarded on correctness alone.

[^c1]: arxiv-2512-15528 — "a perimeter-based normalized semantic distance between any two emotion categories"
[^c2]: arxiv-2512-15528 — "the model should assign higher confidence estimation to an erroneous prediction of contentment than to one of anger"
[^c3]: arxiv-2512-15528 — "quantified by the deviation between the predicted emotion and the ground-truth label"
[^c4]: arxiv-2512-15528 — "It encourages high confidence for correct predictions and low confidence for incorrect ones"
[^c5]: arxiv-2512-15528 — "EmoCaliber achieves an ECE of 13.63, which is nearly half that of the second-best baseline, Qwen3-VL (Ans) at 26.31"
[^c6]: arxiv-2512-15528 — "provides users with an estimate of both the plausibility of alternative interpretations"
[^c7]: arxiv-2512-15528 — "it is inherently challenging to simultaneously prevent overconfidence in fine-grained multi-class tasks and ensure sufficient confidence in coarse-grained binary tasks"
