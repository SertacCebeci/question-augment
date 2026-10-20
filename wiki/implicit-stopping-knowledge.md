---
description: "Reasoning models often reach the correct answer well before they stop thinking, yet assign high confidence to short correct chains that pass@1 sampling skips; confidence-guided search finds them."
aliases: ["knowing when to stop thinking", "RFCS", "ratio of first correct step", "SAGE", "pass@1 obscures efficient reasoning"]
sources: ["arxiv-2602-08354", "arxiv-2512-05325"]
---
# Implicit stopping knowledge in reasoning models

Claim: a reasoning model can internally "know" when its reasoning is already sufficient, but ordinary sampling does not act on it, so extra reasoning is produced after the answer is already derived.

**Evidence that length is not the same as correctness.** The paper cites prior multi-sample findings: on AIME 2025 DeepSeek-R1 writes responses nearly 5x longer than Claude 3.7 Sonnet at comparable accuracy, and in 72% of problems with both correct and incorrect samples the longer response was more likely wrong.[^c1]

**A measure of overshoot.** The Ratio of the First Correct Step (RFCS) is the step index at which the correct answer first appears divided by the total number of reasoning steps (steps split on blank lines).[^c2] A value below 1 means the model kept going after being right. In the authors' MATH-500 runs, all three models tested showed significant ineffective steps in over half of samples, and more post-training (DeepScaleR) or a stronger model (Qwen3-8B) did not clearly improve this.[^c3]

**Where the knowledge shows.** Across many sampled chains, the model assigns high confidence to concise, effective paths, and this becomes more pronounced as the exploration space grows; the authors infer the model implicitly knows when to terminate, but pass@1 training and inference hide it.[^c4]

**SAGE.** The decoding strategy expands the top-m candidate sequences scored by average cumulative token log-probability, and accepts a candidate as a finished chain only when the end-of-thinking token is among the top-h most probable next tokens; low-probability termination is discarded as low confidence. Answers are then decoded greedily from each retained chain.[^c5] Folding SAGE in as mixed sampling in group-based RL (SAGE-RL) aims to move these short-chain patterns into standard pass@1 inference.[^c6]

**A probe at the cue.** The same knowledge can be read out directly at reflective tokens. LYNX trains a probe on hidden states at tokens such as "hmm" and "wait", labelled by whether a forced answer there would be correct, and wraps its scores in split conformal prediction.[^c7][^c8] The paper opens on the same phenomenon: models keep "reasoning long after they internally have enough information to answer".[^c9] A probe trained on forced-answer correctness shows a decodable signal in the hidden state at cue positions. It does not show that the model's own decision to stop follows that signal. See [[reflective-cue-decision-points]] and [[forced-exit-label]].

## Limits

All evidence is mathematical reasoning (MATH-500 for the diagnosis, six math benchmarks for results) on small to mid-size open models; nothing is shown for open-ended or non-verifiable questions. RFCS needs a checkable answer and step segmentation, so it is undefined where no correct answer exists. "The model knows" is an interpretation of confidence statistics (my reading: it shows a decodable signal, not a mechanism). The quantitative gains of SAGE-RL were not read in detail here and are not claimed.

## Related

- [[moderate-adaptive-reasoning-length]] — longer reasoning hurting accuracy, from the theory-of-mind side
- [[implicit-answer-conditioning]] — answers shaped before the reasoning finishes
- [[deep-thinking-ratio]] — measures of thinking quality beyond length

[^c1]: arxiv-2602-08354 — "in 72% of problems where both correct and incorrect answers were generated, the longer response was more likely to be incorrect than the shorter one."
[^c2]: arxiv-2602-08354 — "defined as the step index at which the correct answer first appears divided by the total number of reasoning steps."
[^c3]: arxiv-2602-08354 — "all models exhibit significant ineffective steps in over half of the samples."
[^c4]: arxiv-2602-08354 — "reasoning models implicitly know the appropriate moment to terminate their reasoning process, but this capability is obscured by current pass@1 training and inference paradigms."
[^c5]: arxiv-2602-08354 — "as the model’s confidence in terminating the thinking process is low at this point"
[^c6]: arxiv-2602-08354 — "we enable the reasoning model to learn concise yet effective thinking patterns without altering its original reasoning paradigm."
[^c7]: arxiv-2512-05325 — "trains a lightweight probe on hidden states at those cue tokens using supervision from forced exits"
[^c8]: arxiv-2512-05325 — "split conformal prediction to obtain distribution-free control over the rate of premature exits"
[^c9]: arxiv-2512-05325 — "continuing to reason long after they internally have enough information to answer"
