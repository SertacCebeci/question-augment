---
description: "A stated length constraint loses force when a helpfulness prior competes with it; removing helpfulness wording raised compliance at medium context, though the causal reading is inferred."
aliases: ["constraint salience hypothesis", "constraint salience", "task-frame ambiguity", "helpfulness-prior override of a constraint"]
sources: ["arxiv-2512-17920"]
---
# Constraint salience against a helpfulness prior

An instruction is followed only if it is salient enough, relative to everything else in the prompt. The paper proposes that compliance "depends on how perceptually salient the constraint is relative to other prompt features and learned" behavioral priors.[^s1] Applied to the U-shaped pattern in [[constraint-compliance-u-curve]], the proposal is that salience is high where the prompt is so short that the constraint is the whole task, and where the prompt is so full that the constraint is repeated and explicit. In between, the constraint is one line among much content.

The mechanism for the middle is competition between two behavioural modes. At medium context there is "sufficient context" to trigger a helpful explanation, but "constraint language is buried among semantic content."[^s2] The paper's account is that "RLHF-trained" helpfulness signals then "dominate, leading to verbose, constraint-violating responses."[^s3] The model faces what the paper calls task-frame ambiguity: "uncertainty about whether to prioritize helpfulness (elaborate) or constraint compliance (concise)." The word "ambiguity" here means uncertainty about which behavioural mode applies, not about what the concept means.

The test is an ablation at the medium level only. The system prompts were rewritten to remove wording that encourages a thorough answer, and the constraint itself was kept: the paper says it removed phrases encouraging comprehensive, detailed and helpful responses "while preserving the constraint specification."[^s4] Compliance rose. Across the 72 conditions the average improvement in constraint compliance was 598%, with a median of 525%.[^s5] Of the 72 trials, 71 improved, and 57 reached perfect compliance after the edit.[^s6] The paper takes this as confirmation: "that RLHF-trained helpfulness behaviors are the dominant cause of constraint violations at medium compression."[^s7]

## Limits

- The ablation changes the prompt text. It does not change any model's training, and nothing in the parts read shows the helpfulness wording was the only thing that moved. The step from "removing these words raised compliance" to "RLHF helpfulness is the dominant cause" is the paper's inference, and I read it as a hypothesis with good support, not as a demonstration.
- Confound. The removed phrases ("comprehensive", "detailed") also instruct the model to write more. Removing them may lower the length the model aims for, which is a length cue, not a salience effect. My inference: a control that replaced the wording with neutral text of similar length would be needed to separate the two. None is described in the parts read.
- Only the medium level was ablated. The same edit was not shown to leave the extreme levels unchanged, so the claim that the mechanism is specific to the middle is not tested here.
- The paper's other predictions are untested. Its own words: "The remaining predictions offer additional mechanistic validation targets for future work."[^s8] One of them predicts that capitalised "EXACTLY 35 WORDS" would improve compliance over plain "35 words," since emphasis raises salience; the paper's figure for that gain is a range it states in advance.[^s11] It says the emphasis should "reduce CC violations without changing" the semantic content, but no such run is reported.[^s9] Attention-entropy and concept-independence predictions are also left open.
- The account at the short end is a label, not a measurement. The paper says short prompts enter "pattern completion mode,"[^s10] which is a description of the behaviour, not a test of an internal state.
- The compliance measure is a word count scored by LLM judges (see [[constraint-compliance-u-curve]] for the scoring limits), so the size of the ablation effect carries the scoring error with it.
- Other accounts fit the same data and are not excluded in the parts read. A model may simply aim for a length set by the prompt's own length, so that a longer, richer prompt pulls the answer longer. That account needs no helpfulness prior, and it predicts the same middle-band failure if the prompt's length is treated as a target.

## Related

- [[constraint-compliance-u-curve]] — the pattern this mechanism is offered to explain
- [[compliance-bias]] — an RLHF-shaped drive to proceed under pressure, a reward-side account of a related failure in agents
- [[non-monotonic-prompt-pressure-hallucination]] — prompt pressure whose effect on output is non-monotone in the same way
- [[excess-length-over-minimal-sufficient-baseline]] — over-generation measured against a minimal sufficient answer, which is the output a helpfulness prior would produce

[^s1]: arxiv-2512-17920 — "relative to other prompt features and learned"
[^s2]: arxiv-2512-17920 — "but constraint language is buried among semantic content"
[^s3]: arxiv-2512-17920 — "signals dominate, leading to verbose,"
[^s4]: arxiv-2512-17920 — "while preserving the constraint specification"
[^s5]: arxiv-2512-17920 — "Average CC improvement: 598% (median: 525%)"
[^s6]: arxiv-2512-17920 — "Successful trials: 71/72 (98.6%) showed positive improvement"
[^s7]: arxiv-2512-17920 — "that RLHF-trained helpfulness behaviors are the dominant cause of constraint violations at"
[^s8]: arxiv-2512-17920 — "The remaining predictions offer additional mechanistic validation targets for future work."
[^s9]: arxiv-2512-17920 — "should reduce CC violations without changing"
[^s10]: arxiv-2512-17920 — "pattern completion mode"
[^s11]: arxiv-2512-17920 — "improves CC by 30"
