---
description: "Difficulty weighting alone misses prompt groups whose rollouts collapse to one solution; multiplying it by the dispersion of the group's solutions downweights exactly those groups."
aliases: ["exploration-aware curriculum", "solution-space dispersion weight", "rollout collapse weighting", "PuzzleCraft curriculum"]
sources: ["arxiv-2512-14944"]
---
# Rollout dispersion curriculum

In group-relative RL a prompt is informative when its rollouts disagree. A difficulty term captures part of this. With mean group reward d, the product d(1 − d) "peaks at medium difficulty and vanishes at the extremes" [^c1], which is the zero-variance logic described in [[zero-variance-group-waste]]. The PuzzleCraft work adds a second factor: how many distinct solutions the rollouts actually propose. Its example has a multiple-choice verifier with ground truth A. The groups {A, B, B, B, B, B, B, B} and {A, B, B, C, C, D, E, F} have the same mean success, "yet the first reflects strong collapse to a single incorrect option."[^c2] Reward statistics cannot tell them apart.

## Mechanism

The group weight is w(x) = λ · d(1 − d) · d_π(x)^γ, with λ = 4 and γ = 0.5 "in all experiments."[^c3] The factor d_π is a normalized dispersion of the group's solution keys, and it is puzzle-specific.

- For binary-choice puzzles (rotation angle, candidate index), d_π is the normalized entropy of the selected options. The paper reads "d_π ≈ 0" as "rollouts collapse to a single option."[^c4]
- For the Jigsaw puzzle, each rollout induces a permutation of tile positions. With M distinct permutations among G rollouts, d_π = (M − 1)/(G − 1). The authors use permutations because "multiple distinct permutations can yield the same reward," so partial-credit reward can hide a collapse onto one arrangement.[^c5]

The weight is applied inside a token-level GRPO objective with the KL coefficient set to zero (β = 0).[^c6] The curriculum thus changes which prompts contribute to the update, not the reward itself. The stated purpose is the one already named above: the authors say the curriculum "detects when rollouts within a prompt group collapse to the same solution, and it downweights such groups to mitigate vanishing-advantage updates."[^c7] Their account of the failure is that "homogeneous rollouts cause group-relative advantages to shrink."[^c8]

## Measured

On Jigsaw with Qwen2.5-VL-7B, the authors compare against two difficulty-only curricula (Observe-R1 and VCRL) and report that the exploration-aware version improves average accuracy "by more than 2.5 points over both methods."[^c9] Their reading is that "reward statistics alone are not sufficient for puzzle-based RLVR."[^c10] The main text puts the same claim as "our exploration-aware curriculum consistently outperforms difficulty-only curricula."[^c11]

## Limits

- The dispersion statistic is defined per puzzle. The principle is to extract "a discrete solution key" from each rollout, but the paper gives no key for free-form answers, so the method does not transfer to open-ended questions as written (my inference).
- Tested on synthetic visual puzzles built from COCO images, with Qwen2.5-VL and Qwen3-VL backbones. Nothing here tests a task without a checkable outcome.
- Dispersion measures diversity, not correctness. A group can be diverse and wrong, and the weight would still raise it (my inference).
- The gain is reported for the combined weight against difficulty-only baselines. I found no run that isolates the dispersion factor alone in the parts of the text I read, so its share of the gain is not separated.
- λ and γ are fixed, and I found no sweep over them in the parts I read. The fractional exponent is a choice the text does not justify beyond fixing it.
- d_π is computed from the same G rollouts that feed the update. With small G, M − 1 over G − 1 is a coarse estimate (my inference).

## Related

- [[zero-variance-group-waste]] — the difficulty-side argument this weight starts from; the dispersion factor is what it adds
- [[curriculum-collapse]] — a questioner-side collapse into a narrow problem slice; here the collapse sits in the solver's own rollouts
- [[permutation-consistency-training]] — also treats option order, but as a reward-invariance requirement, not as a weight on prompts
- [[process-outcome-consistency-verification]] — the same PuzzleCraft work tracks reasoning–answer consistency as a diagnostic, and the curriculum is reported to slow its late decline

[^c1]: arxiv-2512-14944 — "d(1 − d) peaks at medium difficulty and vanishes at the extremes"
[^c2]: arxiv-2512-14944 — "yet the first reflects strong collapse to a single incorrect option."
[^c3]: arxiv-2512-14944 — "where we use fixed values of λ = 4 and γ = 0.5 in all experiments."
[^c4]: arxiv-2512-14944 — "dπ ≈ 0 indicates that rollouts collapse to a single option"
[^c5]: arxiv-2512-14944 — "multiple distinct permutations can yield the same reward"
[^c6]: arxiv-2512-14944 — "We set the KL-to-reference coefficient to zero (β = 0)"
[^c7]: arxiv-2512-14944 — "it detects when rollouts within a prompt group collapse to the same solution, and it downweights such groups to mitigate vanishing-advantage updates"
[^c8]: arxiv-2512-14944 — "homogeneous rollouts cause group-relative advantages to shrink"
[^c9]: arxiv-2512-14944 — "improving Avg. by more than 2.5 points over both methods"
[^c10]: arxiv-2512-14944 — "This suggests that reward statistics alone are not sufficient for puzzle-based RLVR"
[^c11]: arxiv-2512-14944 — "our exploration-aware curriculum consistently outperforms difficulty-only curricula"
