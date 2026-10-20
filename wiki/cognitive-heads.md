---
description: "Linear probes on attention-head activations at step boundaries find a small set of heads that predict non-linear reasoning, such as backtracking; steering them changes the step count."
aliases: ["cognitive attention heads", "non-linear reasoning heads", "reasoning-behavior heads"]
sources: ["arxiv-2512-24574"]
---
# Cognitive heads

A reasoning model's chain of thought can be cut into steps at the "\n\n" delimiter, and each step labelled by its wording: non-linear if it contains a cue word such as "Wait" or "Alternatively", linear otherwise. The labelled behaviours are the moves a straight step-by-step trace does not make: "backtracking, verification, subgoal setting and backward chaining".[^c1] The labelling is lexical, by design: each step is categorized "using keyword matching".[^c2] The open question is whether any component of the network carries that label in its activations, and whether changing that component changes the trace.

The test runs in three stages. First, each step is embedded as the post-attention activation of every attention head at the step's final delimiter token. Second, a linear probe is fit per head to predict the step's label, and the heads are ranked by accuracy. A control makes the result meaningful: the same probes trained on randomly sampled tokens stay at chance, "the classification accuracy remains near chance level", while certain heads "achieve significantly higher accuracy".[^c3] The paper names the top of that ranking: "We refer to these as Cognitive Heads, while the remaining are treated as standard heads."[^c4] The abstract states the finding in one line: the paper "uncover[s] specialized attention heads that correlate with distinct cognitive behaviors such as verification and backtracking."[^c5]

The heads are not spread evenly. "cognitive heads are more prevalent in deeper layers", with some in middle layers.[^c6] The paper reads this against the view that deeper layers carry higher-level features, an expectation it cites rather than tests here.

Second-stage evidence is causal, not only predictive. During generation the paper pauses after each step and edits the selected heads: the post-attention state x is replaced by x − α v, where v is the mean activation over the non-linear steps of the calibration set. The sign of α sets the direction: "α > 0 attenuates nonlinear behavior".[^c7] On one MATH500 problem with DeepSeek-R1-Distill-Qwen-1.5B, suppressing at step 9 shortened the trace to 12 steps, while enhancing at step 10 produced a path where "the enhanced non-linear path extends to 45 steps", against 17 in the original run. All three runs reached the correct answer.[^c8][^c16]

The control matters more than the example. Over 100 MATH500 samples, editing the top heads moved the number of reasoning steps with α, while editing the bottom 7% of heads by probe accuracy left it "largely unchanged across different intervention strengths".[^c9] The authors take this as evidence that "the existence of cognitive attention heads" and "the feasibility of manipulating cognitive behaviors during reasoning" both hold.[^c10]

What this establishes is a dose-response on the count of non-linear steps, with a matched set of heads that does not respond. It is a claim about the length and shape of a trace, not about what the heads compute. The paper does not show that a head "does" verification; it shows that a head's read-out, when pushed, changes how often the trace reverts.

## Limits

- The step labels are a lexical proxy. A verification phrased without a cue word is labelled linear, and a cue word used for another purpose is labelled non-linear. The paper concedes the consequence for the head vectors: "it inevitably carries noise within the activation space."[^c11] (My inference, not the paper's claim: the labels could be partly tracking the cue vocabulary rather than the behaviour.)
- The head fraction is not fixed across the paper as I read it. Calibration keeps "the top 10% of heads",[^c12] online intervention selects "the top 7% of attention heads",[^c13] and the head-count ablation finds that "steering approximately the top 38% of attention heads delivers the strongest" result.[^c14] A reader should not assume one fraction.
- The probing evidence I read is one model, DeepSeek-R1-Distill-Qwen-1.5B, in Figure 1; other models and datasets are in an appendix I did not read. The step-count statistic uses "100 samples from the MATH500 test set".[^c15]
- The mechanism is correlational at the probe stage. Probe accuracy shows that the head's output separates the two labels, not that the head is where the behaviour is generated; the intervention narrows this but does not identify the circuit.

## Related

- [[norm-preserving-rotation-steering]] — the intervention rule the same paper applies to these heads at test time
- [[gated-activation-steering-for-abstention]] — a probe-direction steering that is gated per token rather than applied to fixed heads
- [[detection-correction-gap]] — a probe signal that is readable but did not correct the output when steered along; the contrast is what each intervention is aimed at

[^c1]: arxiv-2512-24574 — "These non-linear trajectories (e.g., backtracking, verification, subgoal setting and backward chaining)"
[^c2]: arxiv-2512-24574 — "categorize each reasoning step into one of two types using keyword matching"
[^c3]: arxiv-2512-24574 — "the classification accuracy remains near chance level"
[^c4]: arxiv-2512-24574 — "We refer to these as Cognitive Heads, while the remaining are treated as standard heads."
[^c5]: arxiv-2512-24574 — "uncover specialized attention heads that correlate with distinct cognitive behaviors such as verification and backtracking"
[^c6]: arxiv-2512-24574 — "cognitive heads are more prevalent in deeper layers"
[^c7]: arxiv-2512-24574 — "α > 0 attenuates nonlinear behavior"
[^c8]: arxiv-2512-24574 — "the enhanced non-linear path extends to 45 steps"
[^c9]: arxiv-2512-24574 — "the number of reasoning steps remains largely unchanged across different intervention strengths"
[^c10]: arxiv-2512-24574 — "support the existence of cognitive attention heads and demonstrate the feasibility of manipulating"
[^c11]: arxiv-2512-24574 — "it inevitably carries noise within the activation space"
[^c12]: arxiv-2512-24574 — "Keep the top 10% of heads."
[^c13]: arxiv-2512-24574 — "select the top 7% of attention heads"
[^c14]: arxiv-2512-24574 — "steering approximately the top 38% of attention heads delivers the strongest"
[^c15]: arxiv-2512-24574 — "Using 100 samples from the MATH500 test set"
[^c16]: arxiv-2512-24574 — "all versions of the reasoning process ultimately produce the correct final answer"
