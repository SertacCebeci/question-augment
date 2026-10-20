---
description: "Prompts that share a chain-of-thought interface may give stable answers: a sufficient-condition argument ties answer change to trace change and decision margin, untested here."
aliases: ["CoT reduces prompt sensitivity", "chain-of-thought stabilization", "reasoning-interface prompt invariance", "CoT prompt robustness"]
sources: ["arxiv-2511-20836"]
---
# Chain-of-thought prompt invariance

Prompt choice alone can move a leaderboard: a score taken under one fixed prompt is a measurement of that one invocation, and the same model can rank differently under another.[^c16] What keeps a family of prompts from moving the score is, on this evidence, whether the prompts ask for a reasoning trace before the answer. Across the structured prompts that all do, the reported accuracies bunch together and sit higher. The authors put it as "once the CoT interface is introduced, performance is both higher and more stable."[^c1] On the main leaderboard the mean moves from 61.4% under zero-shot prediction to 66.2% under zero-shot chain-of-thought, and then to 66.3% under the two few-shot optimizers.[^c2]

The mechanism, as the paper states it. Two prompts share a chain-of-thought (CoT) interface if both instruct the model to produce a reasoning trace τ before the answer y, with the same output structure. The working assumption, which the paper calls a Markov property of chain-of-thought, is that once the trace exists the answer no longer depends on the prompt: y is conditionally independent of the prompt given the input and the trace.[^c3] The authors motivate it by the causal structure of autoregressive generation, and add that the marginal effect of the prompt on the answer, given the trace, "may be relatively small."[^c4]

Given that assumption, the answer distribution is the trace distribution pushed through a fixed kernel. The appendix's Lemma 1 is a data-processing inequality: the total-variation distance between answer distributions under two prompts is at most the distance between their trace distributions. The paper describes this as "one sufficient-condition account of how prompt invariance could arise once a shared CoT" interface is in place.[^c5]

The stability condition runs through a decision margin: the probability of the predicted answer minus the probability of the runner-up. "A larger margin indicates more stable predictions."[^c6] Theorem 1 says that if the total-variation distance between the two answer distributions is below half that margin, the top answer does not change. Theorem 2 restates the condition in KL divergence between trace distributions: if that divergence is at most κ, the margin is at least 2ε, and κ < 2ε², the predicted answer is unchanged. "Theorem 2 provides one sufficient condition for prediction stability."[^c7]

What survives the transfer from information theory is the bound itself, which holds for any fixed kernel once its premises are granted. What does not transfer is the premise that the kernel ignores the prompt. For an autoregressive model the trace is generated under the prompt, so the prompt can still shape the answer through channels the assumption leaves out. That is my inference, not a result of the paper.

The paper offers two conjectured sources for the invariance: "chain-of-thought enlarges decision margins; and second, that structured prompts sharing a" CoT interface induce similar trace distributions.[^c8] Neither is measured. "We do not estimate decision margins or reasoningpath divergences directly in this paper."[^c9] The evidence it offers is the clustering: "tight clustering of performance across structurally different prompts," which it says is "consistent with" the condition, "though it does not directly verify it."[^c10][^c11]

## Limits

- The appendix is background, not evidence. The authors say it "is intended as background intuition rather than the primary evidentiary basis of the paper, which remains empirical."[^c12] They also write, "We include this appendix as conceptual background only."[^c13]
- The conditions are sufficient, not necessary. Failing them says nothing about a particular prompt pair, and the argument does not say which prompts will diverge.
- Clustering has another explanation. The paper itself attributes the flat result on HeadQA to "saturated baseline scores."[^c14] A set of scores pressed against a ceiling clusters for that reason alone, so tight clustering cannot by itself tell the invariance account from saturation. This is my inference from the paper's own HeadQA reading.
- The effect is averaged over six models and seven benchmarks. The per-instance decision margins that Theorem 1 needs are not reported, so the bound is not checked on any instance.
- The scope is short-answer tasks. The paper's own limitations note says that prior work "suggests that CoT gains are most reliable on math and symbolic reasoning, with more mixed effects in long-form" generation.[^c15] Open-ended answering is not tested here.
- Single deterministic runs at temperature zero. A cluster of three near-identical numbers under one run does not show the spread that stability would need.

## Related

- [[prompt-format-rank-instability]] — typesetting changes reorder leaderboards with no reasoning step involved; the trace argument is one conjectured reason a shared reasoning interface might blunt that kind of shift
- [[task-conditional-prompt-gain]] — the size of a prompting gain flips across tasks; the invariance argument concerns the spread across prompts, not the sign of a gain
- [[prompt-specificity-effect]] — how explicit a prompt is changes accuracy unevenly across tasks, a related prompt-level effect
- [[optimizer-gain-saturation-after-cot]] — the diminishing returns of few-shot optimizers once the reasoning interface is present, which this note's conjecture would predict

[^c1]: arxiv-2511-20836 — "once the CoT interface is introduced, performance is both higher and more stable"
[^c2]: arxiv-2511-20836 — "moving from Zero-Shot Predict to Zero-Shot CoT results in"
[^c3]: arxiv-2511-20836 — "the final answer y is conditionally"
[^c4]: arxiv-2511-20836 — "marginal effect of p on y given τ may be relatively small"
[^c5]: arxiv-2511-20836 — "one sufficient-condition account of how prompt invariance could arise once a shared CoT"
[^c6]: arxiv-2511-20836 — "A larger margin indicates more stable predictions"
[^c7]: arxiv-2511-20836 — "Theorem 2 provides one sufficient condition for prediction stability"
[^c8]: arxiv-2511-20836 — "chain-of-thought enlarges decision margins; and second, that structured prompts sharing a"
[^c9]: arxiv-2511-20836 — "We do not estimate decision margins or reasoningpath divergences directly in this paper"
[^c10]: arxiv-2511-20836 — "tight clustering of performance across structurally different prompts"
[^c11]: arxiv-2511-20836 — "though it does not directly verify it"
[^c12]: arxiv-2511-20836 — "intuition rather than the primary evidentiary basis of the paper, which remains empirical"
[^c13]: arxiv-2511-20836 — "We include this appendix as conceptual background only"
[^c14]: arxiv-2511-20836 — "saturated baseline scores, while Medec likely reflects knowledge base limitations"
[^c15]: arxiv-2511-20836 — "are most reliable on math and symbolic reasoning, with more mixed effects in long-form"
[^c16]: arxiv-2511-20836 — "prompt choice can materially impact leaderboard outcomes"
