---
description: "Training on positive-advantage samples only at first, then adding negative ones after a switch point, trades early gradient variance for later unbiasedness in policy-gradient RL."
aliases: ["CAPO", "curriculum advantage policy optimization", "imitation-then-discrimination curriculum", "advantage-sign curriculum", "positive-first advantage schedule"]
sources: ["arxiv-2512-02580"]
---
# Positive-only advantage curriculum

In policy-gradient training of language models, each sampled trajectory is weighted by its advantage, and the sign of that advantage says whether the sample did better or worse than expected. This mechanism uses the sign as a schedule. The work describes it as "a two-phase curriculum learning strategy based on advantage signals."[^c1] In the first phase, the update keeps only the samples whose advantage is non-negative, so training is a filtered imitation of successful trajectories. The filter is a hard indicator on the advantage's sign, not a reweighting: the phase-one objective "filters out negative-advantage" samples and adds a KL penalty toward a reference policy.[^c2] After a switch point, negative-advantage samples are admitted as well and the update uses the full signed advantage. The authors call the two stages imitation and discrimination.

The stated reason is a variance–bias account of the policy-gradient estimate. The model is an advantage estimate that equals the true advantage plus "zero-mean noise with variance" σ²,[^c3] and in that model dropping the negative samples lowers the variance at the cost of bias. The authors argue the overall error still falls: "the overall MSE is lowered, ensuring stable improvement."[^c4] Once the advantage variance has shrunk as the policy improves, the second phase restores an unbiased estimator: "Phase 1 bounds variance, Phase 2 restores unbiasedness."[^c5] The appendix calls the first-phase bias "tolerable early on," since it steers the policy toward high-reward actions.[^c6] Negative samples are the ones dropped, and the text gives as their reason that they are "often high-magnitude in early training."[^c7]

The schedule is a single hard switch, not a ramp. The authors "experimented with gradually introducing negative signals," but report that no progressive scheme "matched the effectiveness of a simple switch point."[^c8] The switch sits at "a predefined switch point (e.g., at 10% or 20% of total" training steps in the method section,[^c9] and the sensitivity study finds that performance peaks when it "occurs around 20%–30% of training."[^c10]

In the reported experiments, the mechanism is added to GRPO, PPO, RLOO and Reinforce++ on mathematical reasoning. The authors report gains "ranging from +2.4 to +4.0 on 1.5B models and from +1.7 to +3.9 on 7B models," and "+3.81" on a GUI reasoning task.[^c11] On 7B, against a static difficulty ordering built from pass@16, the authors write that "predefined difficulty heuristics are insufficient."[^c12] Trained only on math, the 7B model reportedly "achieves an average accuracy of 52.8, outperforming GRPO" on ARC-C and GPQA-Diamond.[^c13]

The mechanism, stated plainly: the first phase lowers the variance of the update by removing its large negative terms, and the second phase removes the bias that the first one introduced. What the reader should keep is that the curriculum is a change in which samples enter the gradient, not in the order of the data.

## Limits

- The variance argument is a sketch. It assumes Gaussian-like advantages to get its factor: "symmetry implies filtering halves the variance contribution."[^c14] Whether real GRPO or RLOO advantages behave this way was not tested in the text I read (my inference).
- The convergence proposition gives a local optimum under Robbins–Monro step sizes. It does not say how long the first phase should be; the switch point is picked by sweep, and the sweep is reported for AIME24 and AMC23 only.[^c15]
- The text is inconsistent about the boundary. The method section writes the phase-one indicator as A ≥ 0, while the appendix writes "CAPO filters updates to only positive advantages."[^c16] Samples with zero advantage, which are common in group-relative methods when all rollouts agree, fall on different sides. The effect of this difference is not analysed (my reading).
- The first phase learns only from successes. Where a model rarely succeeds on a prompt, phase one gives it little signal, and the text does not examine such prompts (my inference).
- The gains are on one math training set, two model sizes and one GUI setting. The comparison in the reward and entropy figure is GRPO against CAPO on the 7B model.[^c17] A run that isolates the positive-only phase from the switch alone was not among the parts I read.

## Related

- [[suppressed-criteria]] — the opposite worry: a negative advantage can push down a behaviour the rollout did satisfy. This mechanism deliberately removes negatives for a while, which is a different remedy for the same signed advantage.
- [[signed-process-reward-stabilization]] — a continuous alternative to dropping negatives: scale them by a factor below one, so the policy does not learn to stop acting.
- [[scenario-curriculum-rl]] — a phased curriculum gated on measured mastery, but it changes the environment the policy meets, not the sign of the advantage it learns from.
- [[zero-variance-group-waste]] — when all rollouts in a group agree, the advantage is zero and the sample carries no signal, which is the boundary case the sign filter has to settle.

[^c1]: arxiv-2512-02580 — "It adopts a two-phase curriculum learning strategy based on advantage signals"
[^c2]: arxiv-2512-02580 — "filters out negative-advantage"
[^c3]: arxiv-2512-02580 — "zero-mean noise with variance"
[^c4]: arxiv-2512-02580 — "the overall MSE is lowered, ensuring stable improvement"
[^c5]: arxiv-2512-02580 — "Phase 1 bounds variance, Phase 2 restores unbiasedness"
[^c6]: arxiv-2512-02580 — "Although bias is introduced, it is tolerable early on"
[^c7]: arxiv-2512-02580 — "often high-magnitude in early training"
[^c8]: arxiv-2512-02580 — "We also experimented with gradually introducing negative signals, but found that no such progressive"
[^c9]: arxiv-2512-02580 — "a predefined switch point (e.g., at 10% or 20% of total"
[^c10]: arxiv-2512-02580 — "occurs around 20%–30% of training"
[^c11]: arxiv-2512-02580 — "achieving improvements ranging from +2.4 to +4.0 on 1.5B"
[^c12]: arxiv-2512-02580 — "predefined difficulty heuristics are insufficient"
[^c13]: arxiv-2512-02580 — "achieves an average accuracy of 52.8, outperforming GRPO"
[^c14]: arxiv-2512-02580 — "symmetry implies filtering halves the variance contribution"
[^c15]: arxiv-2512-02580 — "Switch Point Sensitivity: Results on AIME24 and"
[^c16]: arxiv-2512-02580 — "CAPO filters updates to only positive advantages"
[^c17]: arxiv-2512-02580 — "The gray vertical line marks the transition from the imitation phase to the discrimination phase"
