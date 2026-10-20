---
description: "A proof generator rewarded for scoring its own proof the way an external verifier would, with its self-analysis meta-checked, so finding its own flaws pays more than claiming correctness."
aliases: ["self-analysis reward", "self-verification reward for generator", "self-evaluation reward", "faithful self-evaluation"]
sources: ["arxiv-2511-22570"]
---
# Faithful self-assessment reward

A generator trained only on whether its proof is right has no reason to look for its own flaws. The paper reports the behaviour this produces. When the generator is asked to write a proof and analyse it in one pass, "the generator tends to claim correctness even when the external verifier" can find the flaws.[^f1] The model can refine a proof when an external verifier points at problems, but it does not grade its own work with the rigour of a dedicated verifier.

The fix is to put a reward on the self-assessment. The generator writes a proof, then a self-analysis in the verifier's format and rubric, and a self-predicted score. The external verifier scores the proof, and the same verifier scores the self-analysis: "To ensure faithful self-evaluation, we use the verifier" to assess both components.[^f2] The self-analysis earns reward when its predicted score matches the verifier's score for the proof, and that reward is multiplied by a meta-verification score for whether the self-analysis's issues are real ([[meta-verification]]). The total reward is gated by a format check and combines the proof term with the self-analysis term. The authors summarise what this rewards: "Faithful acknowledgment of errors is rewarded over false claims of correctness."[^f3]

The incentive has a second consequence the authors name directly: "A good strategy to obtain high rewards for the proof generator is to identify and resolve" issues before finalising.[^f4] The self-analysis is worth reward only if it agrees with the verifier and survives meta-checking, so the cheapest way to earn it is to find the flaws the verifier would find. The generator is trained, in effect, to run the verifier's check on its own output before it commits.

The self-assessment then drives the test-time loop. In sequential refinement, the generator re-prompts itself with its own output and stops "until the generator assigns itself a perfect score or" the attempt cap is reached.[^f5] The paper reads the results as evidence that the self-score is informative: "The self-selected best proofs achieve significantly higher" verification scores than the average thread, and "Pass@1 improves substantially as maximum sequential" attempts increase.[^f6]

The mechanism is specific to proofs graded by a rubric. A same-model self-check used only at test time, without training against an external grader, is a different object; see [[same-model-self-verification-conditional-confidence]].

## Limits

- The self-analysis reward is only as good as the verifier and meta-verifier it is scored by. Expert grading is used for the benchmark figure: DeepSeekMath-V2 "was evaluated by our experts following the grading guidelines," but the training reward is the model's own verifier.[^f7]
- The text read reports no ablation that removes the self-analysis term and measures the generator's self-assessment afterwards. The claim that the term restores faithful self-assessment rests on the one-shot observation and on the refinement results.
- The stopping rule trusts a self-assigned perfect score. The text does not measure how often a self-assigned 1 is wrong, and that is the case where a faithful self-assessment matters most.
- Results are on olympiad and undergraduate mathematics. "The hardest IMO-level problems remain challenging for our model," so the reward does not solve the hardest cases.[^f8]
- The approach needs a verifier that can score a proof against a rubric. Open-ended tasks without such a rubric are not covered in the parts read; whether a self-assessment reward can be built there is my inference, not a result of the paper.

## Related

- [[same-model-self-verification-conditional-confidence]] — a same-model self-check used after the fact as a confidence signal, without training; here the self-check is trained against an external verifier
- [[shallow-self-monitoring]] — post-answer self-checks in reasoning models that mostly repeat earlier work; the reward here targets whether the check finds real flaws
- [[self-bias-in-self-refinement]] — a model's systematic over-rating of its own output, the failure a self-score reward has to counter
- [[critique-consistency-reward]] — a step critique rewarded when its verdict matches final correctness; the self-analysis here is rewarded against the verifier's proof score
- [[answer-reasoning-consistency-reward]] — scores a trace by how much it supports the answer; here the trace is scored by how well it assesses itself
- [[meta-verification]] — the check applied to the self-analysis term before it earns reward
- [[scaled-verification-labeling]] — the same verifier, used to label proofs for training rather than to reward a generator's self-assessment

[^f1]: arxiv-2511-22570 — "the generator tends to claim correctness even when the external verifier"
[^f2]: arxiv-2511-22570 — "To ensure faithful self-evaluation, we use the verifier"
[^f3]: arxiv-2511-22570 — "Faithful acknowledgment of errors is rewarded over false claims of correctness."
[^f4]: arxiv-2511-22570 — "A good strategy to obtain high rewards for the proof generator is to identify and resolve"
[^f5]: arxiv-2511-22570 — "until the generator assigns itself a perfect score or"
[^f6]: arxiv-2511-22570 — "The self-selected best proofs achieve significantly higher"
[^f7]: arxiv-2511-22570 — "was evaluated by our experts following the grading guidelines"
[^f8]: arxiv-2511-22570 — "We observe that the hardest IMO-level problems remain challenging for our model."
