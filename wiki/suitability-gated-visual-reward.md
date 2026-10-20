---
description: "Trajectory-level reward for drawing: a bonus for a correct answer that ran code, larger where an auxiliary label marks the question as suitable for diagrams, with no step-wise labels."
aliases: ["adaptive reward mechanism", "visual-invocation reward", "suitability-weighted invocation reward"]
sources: ["arxiv-2512-24297", "arxiv-2512-04563"]
---
# Suitability-gated visual reward

A policy trained by reinforcement learning on whole trajectories cannot tell, from the outcome alone, which drawing step helped. The paper's adaptive reward handles the question of when to draw by changing the size of a trajectory-level bonus, not by labelling steps. First, each question gets a binary suitability label s from an auxiliary classifier, the question being whether diagrammatic reasoning is likely to help.[^c1] The paper states that the label "does not provide step-wise supervision", and that it "modulates reward magnitude, encouraging selective use of visual construction and making the policy robust to moderate misclassification."[^c2]

The visual term Rvis is computed once, at the end of a rollout. The equation as extracted gives 1.0 when the answer is correct, the code executed, and s = 1; 0.2 when the answer is correct, the code executed, and s = 0; and 0 otherwise.[^c3] The total reward adds this term to the answer-correctness and format terms, so a correct text-only answer keeps its correctness credit and only loses the visual bonus. The text summarises the rule as "a positive reward is granted" when drawing "contributes to a correct solution, with higher weight assigned" when the label predicts drawing is appropriate.[^c4] The effect the authors want is that drawing is treated "as a meaningful intermediate state rather than a mandatory or habitual operation."[^c5]

The label is not hand-written. The paper annotates each training question with the suitability label using an auxiliary language model, DeepSeek-V3, and the prompt is in an appendix.[^c6] The method is trained on DeepMath103K from an instruction-tuned base, with no supervised visual cold-start, which the authors cite as a benefit: "without requiring supervised cold-start."[^c7]

The ablation that removes this reward is one of two component ablations, and both "lead to performance degradation compared to the full" method.[^c8] The paper does not report the rate of code use with and without the reward in the portion read here, beyond a note that removing the reward "leads to a brief increase in early code" use.[^c9]

## How it differs from a learned gate

[[sufficiency-gated-imagination]] also asks when to add visual evidence, but there the policy judges sufficiency at inference and a cost penalty makes skipping safe. Here the signal is a prior on the question, fixed before rollouts, and it acts only through the reward's size. My reading: this gives the policy a push toward drawing where the label expects it to pay, but nothing at inference forces a decision the policy did not learn to make.

A second paper keeps the same shape of reward and changes the source of the label. COOPER trains a unified model to generate depth and segmentation maps and reward their use with a visual-gain label, "we use offline visual-gain labels created during data" construction.[^c10] My reading of its equation is that the label's sign comes from comparing accuracy with and without the generated assistance, so it is measured on the model's own behaviour rather than assigned from a prior. The bonus is not given for every use: "generated visual assistance exceeds σ (in strength or proportion) do we assign a positive reward or penalty," and boundary cases get nothing, because a naive scheme "leads to overuse or over-suppression."[^c11][^c12] The paper reports that the term "consistently improves performance" over format and outcome rewards alone, and reads it as helping the model "decide when and how strongly to invoke visual assistance."[^c13][^c14]

## Limits

- The suitability label is another model's judgement of the question. The paper says the design is robust to "moderate misclassification", but the text read contains no measurement of the label's accuracy or of the outcome when labels are flipped.
- The weights 1.0 and 0.2 are set values. No sensitivity analysis appears in the parts read, so how much the learned drawing rate depends on them is not established.
- The reward is trained on competition mathematics with verifiable answers. Whether a suitability label can be produced as reliably for problems without a checkable answer is not tested.
- The ablation removes the whole term. It does not separate the label's contribution from the bonus for drawing when the label is 0, so the two parts of the design are not shown to be independently necessary.
- Trajectory-level credit is coarse. My reading: a rollout that draws and happens to be right earns the same bonus whether the drawing was decisive or incidental, which the reward cannot distinguish.

## Related

- [[executable-visual-state]] — the drawing behaviour this reward is meant to regulate.
- [[sufficiency-gated-imagination]] — the same when-to-add-visual-evidence question, answered by an inference-time sufficiency judgement instead of a training-time bonus.
- [[competence-aware-credit-assignment]] — also learns when to invoke a tool from one outcome reward, scoring segments by how much they moved success instead of a prior label.
- [[multi-turn-reward-clarification-training]] — a trajectory-level reward that trades a costly turn against task outcome, the same design pattern for asking rather than drawing.
- [[self-generated-auxiliary-modality]] — the generated depth and segmentation maps that COOPER's visual-gain reward regulates; its label is measured per sample, not a prior.

[^c1]: arxiv-2512-24297 — "classifier, which outputs a binary suitability label"
[^c2]: arxiv-2512-24297 — "reward magnitude, encouraging selective use of visual construction and making the policy robust to"
[^c3]: arxiv-2512-24297 — "Rvis = 0.2,"
[^c4]: arxiv-2512-24297 — "a positive reward is granted"
[^c5]: arxiv-2512-24297 — "meaningful intermediate state rather than a mandatory or habitual operation"
[^c6]: arxiv-2512-24297 — "we annotate each instance with a binary"
[^c7]: arxiv-2512-24297 — "without requiring supervised cold-start."
[^c8]: arxiv-2512-24297 — "Both ablations lead to performance degradation compared to the full"
[^c9]: arxiv-2512-24297 — "leads to a brief increase in early code"
[^c10]: arxiv-2512-04563 — "we use offline visual-gain labels created during data"
[^c11]: arxiv-2512-04563 — "generated visual assistance exceeds σ (in strength or proportion) do we assign a positive reward or penalty"
[^c12]: arxiv-2512-04563 — "leads to overuse or over-suppression"
[^c13]: arxiv-2512-04563 — "the visual-gain reward consistently improves performance"
[^c14]: arxiv-2512-04563 — "decide when and how strongly to invoke visual assistance"
