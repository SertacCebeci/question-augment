---
description: "Subtracting a null-prompt score from a model's label score removes its prior bias toward some labels, so a measured shift reflects the input rather than the default preference."
aliases: ["calibrate before use", "null-prompt calibration"]
sources: ["arxiv-2512-08131"]
---
# Contextual calibration

A language model's answer to a classification prompt carries a prior. Some labels receive more probability than the input justifies, and the bias shows most in zero-shot use, where "models often fall back to label priors."[^k1] Contextual calibration removes that prior by scoring the model on a content-free input, a null prompt, and subtracting the null score from the score of the real input. What remains is the effect of the input itself. The work under study states the mechanism as "subtracting a nullprompt score, so results reflect only the input context" [^k2], and uses the same subtraction inside a reinforcement-learning reward rather than as a fixed correction at evaluation time.

The reward defines the calibrated cross-entropy as the context cross-entropy minus the null cross-entropy, with the null taken over the answer prefix alone. Written out, the difference of two negative log-probabilities is the negative log of the ratio of context to null probability, which is my inference from the definition and not a claim the paper makes. The point of the subtraction is stated directly: "By subtracting the null-prompt baseline, the reward focuses only on the effect of the actual input and any modification introduced by the adversarial suffix."[^k3] The metric the paper reports works the same way. Its lower values indicate "weaker confidence in the correct label after accounting for priors."[^k4]

The same reward pools label surface forms. Each label is expanded into lexical variants, since "task-specific label surfaces are expanded from a base set of lexical variants,"[^k5] and the variants' calibrated scores are combined with a log-sum-exp soft-min. That combination is a separate choice from the null subtraction. It makes a score count only when it moves error across the variants, not through a single surface form.[^k6]

The calibration is not a probability calibration in the sense of [[calibration]]. Both notes use the word, and it is easy to conflate them. Probability calibration asks whether a stated probability matches how often its events occur. Contextual calibration asks whether a score moved because of the input or because of the label's default weight. A model can pass one and fail the other. The paper uses "calibrated" in the second sense throughout.

## Limits

- The null is a choice. In the work it is the answer prefix with no input, and the prefix is fixed for all tasks: "for all tasks, the answer prefix is fixed."[^k8] No other null, and no other prefix, was tried in the sections read.
- The subtraction removes a label prior, not every bias. It does not claim to remove biases of content, position, or length in the input; the work's own wording is about "label-surface bias," and it says the calibrated reward makes suffixes "act beyond label-surface bias."[^k7]
- Its benefit is not isolated here. The sections read contain the calibrated reward and its transfer results, but no run of the same attack with the null subtraction removed, so the paper's transfer gain is not attributed to the calibration by a measured comparison in this text.
- The subtraction concerns a classifier's label scores. Whether the same correction improves open-ended answers, or answers evaluated by a judge, is not tested in this work.
- The method is named after a 2021 paper, Zhao et al., *Calibrate before use*, which the work cites for the idea. The work's version is a reward term inside an attack; the original was an evaluation-time correction for few-shot prompting. The two share the subtraction and differ in where it is applied.

## Related

- [[calibration]] — the other sense of the word: whether stated probabilities match outcome frequencies. Neither measure gives the other.
- adversarial-suffix — the attack whose reward uses this subtraction, so that a suffix must change the decision beyond the label prior.
- [[answer-option-surface-cue]] — another way a label's surface form, not the knowledge tested, can carry an answer.
- [[prompt-content-over-surface-form]] — evidence that prompt detail matters more than surface form in one classification setting.

[^k1]: arxiv-2512-08131 — "models often fall back to label priors"
[^k2]: arxiv-2512-08131 — "subtracting a nullprompt score, so results reflect only the input context"
[^k3]: arxiv-2512-08131 — "By subtracting the null-prompt baseline, the reward focuses"
[^k4]: arxiv-2512-08131 — "confidence in the correct label after accounting for priors"
[^k5]: arxiv-2512-08131 — "Task-specific label surfaces are expanded from a base set of lexical variants"
[^k6]: arxiv-2512-08131 — "favors suffixes that consistently increase error across different label tokens"
[^k7]: arxiv-2512-08131 — "making suffixes act beyond label-surface bias"
[^k8]: arxiv-2512-08131 — "the answer prefix is fixed"
