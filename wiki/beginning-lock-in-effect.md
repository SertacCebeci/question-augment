---
description: "Early reasoning steps constrain the rest of an LLM's reasoning: a 15% prefix from a wrong answer cut accuracy by up to 27.5%, and 'wait' or 'however' recovered at most 9.2%."
aliases: ["BLE", "beginning lock-in", "prefix lock-in", "path dependence in LLM reasoning"]
sources: ["arxiv-2512-15274"]
---
# Beginning lock-in effect

The term is borrowed from the human-thinking notion of path dependence, in which "where early-stage thoughts constrain subsequent thoughts."[^c1] Applied to a language model, the question is whether the first part of a generated reasoning trace fixes where the rest of it goes. The paper names the answer the beginning lock-in effect: "where the initial reasoning process significantly constrains the subsequent reasoning steps and influences final results."[^c2]

The measurement holds the opening fixed and lets the rest vary. For two benchmarks, AIME'24 and GPQA Diamond, the authors sampled correct and incorrect outputs from DeepSeek-R1-Distill models, and "We then extract the first 15% of the tokens from each output as a fixed prefix token sequence."[^c3] For each fixed prefix, "we prompt the original LLM to generate eight continuations and calculate the average accuracy."[^c4] A prefix taken from an incorrect output lowers the accuracy of the continuations: "all the evaluated LLMs exhibit a significant performance decline" (up to 27.5% on AIME'24 with the 14B distilled model).[^c5] A prefix taken from a correct output raises it, "demonstrating substantial improvement (up to 20.2%) when initialized" from correct beginnings.[^c6]

The effect is also tested as a lock. The authors inserted "wait" or "however" after the malignant prefix tokens, which invite the model to reflect on what came before. Even so, "the maximum recovery of accuracy reaches only 9.2%."[^c7] The reading they draw is that "LLMs struggle to escape from the flawed initial reasoning."[^c8]

The effect is also located in the trace. Plotted against the retained proportion of the output, performance shows a transition at 15% and stabilises by 35%. In the authors' words, "BLE manifests within the first 15% of tokens, and essentially establishes by 35%."[^c9]

The mechanism the paper offers is the autoregressive one: "each token is generated based on previous tokens."[^c10] Its example is an early unit conversion or truncation that "misleads the reasoning process into an incorrect (precision loss) or inefficient (increased complexity) trajectory."[^c11] My inference, not the paper's claim: an error made early becomes part of the context that every later token is conditioned on, so the rest of the trace is pulled toward being consistent with it. The text does not test this account directly; it shows the outcome, not the internal route.

The paper then turns the observation into a training target. Its method, PPPO, applies "policy updates exclusively to prefix tokens," and estimates the value of a prefix by sampling continuations, a mechanism that "mitigates randomness and provides reliable evaluations for prefix tokens."[^c12][^c13] It reports gains of "up to 14.64%" in average accuracy over representative RLVR baselines, on Qwen3 backbones trained on DAPOMath.[^c14][^c15]

## Limits

- The evidence is a small controlled experiment on two reasoning benchmarks, with DeepSeek-R1-Distill models for the lock-in measurement and Qwen3 models for the training results. The text as read states the sample as 4 correct and 4 incorrect outputs per model and benchmark; it does not give the number of problems.
- The prefixes are chosen by the outcome of their source output. A prefix from a wrong answer is correlated with a wrong answer. The continuation experiment is an intervention on the prefix, but the part read does not say whether problem difficulty was controlled across the correct and incorrect groups. My inference: the decline is a real drop under fixed prefixes, but its size is not a clean causal estimate.
- The "wait" and "however" recovery test covers two insertions. The 9.2% ceiling is the best of those; it does not show that no corrective strategy can recover from a bad opening.
- The analogy to human path dependence is cited from David (1975) and not tested in this work. Whether the effect holds for human questions, or for answers outside verifiable-reward math and science, is not shown.
- The PPPO gains (up to 18.02% on AIME'25, and the average figure above) measure a training method built on BLE. They do not isolate the lock-in effect; the ablation sections were not read in this pass.

## Related

- [[prefix-correctness-readout]] — reads whether a partial generation is already going wrong; BLE is the reason an early part can carry the outcome, but the readout measures correctness from the trace, not the lock-in.
- [[prefix-localized-rubric-credit]] — also places credit on the early part of a response, by evidence sentence rather than by a fixed token fraction.
- [[first-token-entropy]] — measures how concentrated the distribution is when the first output token is about to be chosen. My inference: a candidate measure of the commitment BLE describes, not tested against it here.

[^c1]: arxiv-2512-15274 — "where early-stage thoughts constrain subsequent thoughts"
[^c2]: arxiv-2512-15274 — "where the initial reasoning process significantly constrains the subsequent reasoning steps and influences final results"
[^c3]: arxiv-2512-15274 — "We then extract the first 15% of the tokens from each output as a fixed prefix token sequence"
[^c4]: arxiv-2512-15274 — "we prompt the original LLM to generate eight continuations and calculate the average accuracy"
[^c5]: arxiv-2512-15274 — "all the evaluated LLMs exhibit a significant performance decline"
[^c6]: arxiv-2512-15274 — "demonstrating substantial improvement (up to 20.2%) when initialized"
[^c7]: arxiv-2512-15274 — "the maximum recovery of accuracy reaches only 9.2%"
[^c8]: arxiv-2512-15274 — "LLMs struggle to escape from the flawed initial reasoning"
[^c9]: arxiv-2512-15274 — "BLE manifests within the first 15% of tokens, and essentially establishes by 35%"
[^c10]: arxiv-2512-15274 — "Due to the autoregressive nature of LLMs, where each token is generated based on previous tokens"
[^c11]: arxiv-2512-15274 — "misleads the reasoning process into an incorrect (precision loss) or inefficient (increased complexity) trajectory"
[^c12]: arxiv-2512-15274 — "applying policy updates exclusively to prefix tokens"
[^c13]: arxiv-2512-15274 — "mitigates randomness and provides reliable evaluations for prefix tokens"
[^c14]: arxiv-2512-15274 — "and increases the average accuracy across all the benchmarks by up to 14.64%"
[^c15]: arxiv-2512-15274 — "We adopt the Qwen3 series"
