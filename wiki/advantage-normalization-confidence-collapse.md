---
description: "Std-normalising GRPO advantages can push verbalized confidence to extremes: small reward variance within a group is amplified into a feedback loop that piles confidence above 0.9."
aliases: ["GRPO overconfidence from advantage normalization", "std-normalized advantage confidence collapse"]
sources: ["arxiv-2512-15528"]
---
# Advantage normalization confidence collapse

Group Relative Policy Optimization scores each sampled response against the other responses drawn for the same query. The standard variant centres the reward on the group mean and then divides by the group's standard deviation. Wu et al. report that this division, when the reward includes a confidence term, makes the stated confidence collapse toward one end. Their first attempt used the squared-error confidence reward of RLCR with the standard GRPO advantage, and the outcome was clear: "Empirically, this setting leads to severe overconfidence on VEC, with confidence estimates heavily concentrated above 0.9."[^c1]

The mechanism they adopt comes from Bereket and Leskovec, and they state it in these words: "when reward values within a group exhibit small variance, the normalization amplifies minor relative advantages, causing the model to repeatedly increase the probability of slightly preferred responses and drive toward extreme confidence estimations."[^c2] Read as a loop: when the group's rewards are nearly equal, a tiny difference in reward is rescaled to unit size. The update then favours whichever confidence value was slightly ahead, which makes the next group more uniform still, and the push runs toward the extremes. The loop does not need the reward to be wrong; it needs the spread within a group to be small.

The repair changes two things together. The advantage is kept centred but is not divided by the spread, "we compute the advantage" without the normalization, and the reward is switched to a log-likelihood form, which the authors chose "based on empirical exploration."[^c3] The paper's verdict on the pair: "two modifications effectively mitigate the overconfidence issue."[^c4] The same symptom has been reported before, in a Brier-plus-correctness reward with whole-rollout advantage, where about 95 percent of claim confidences exceed 0.9; see [[decoupled-claim-calibration-training]]. That note attributes the collapse to the advantage being computed over whole rollouts, so the two explanations point at different parts of the same pipeline.

## Limits

- The two modifications were applied together. The configuration that works removes the normalization and changes the reward at once, so the sections read do not isolate the effect of removing normalization alone. The attribution to normalization is the paper's reading of the cited analysis, not a separate ablation.
- The feedback-loop account depends on small within-group variance. When the model's accuracy is middling, groups are not uniform and the loop may not start. That condition is my inference from the paper's explanation; it is not measured.
- Only one task family was run in the sections read: emotion recognition with a fine-grained multi-class taxonomy. The paper itself notes the collapse is hard to avoid on that family, so the symptom's reach to other reward scales is not shown.
- The log-likelihood reward has its own edge behaviour, since it is unbounded as confidence approaches 0 or 1 when the answer is wrong or right. The paper chose it empirically and does not compare it with the other reward forms it tried in the sections read.
- Whether the collapse is a normalization effect or a reward-scale effect cannot be separated from these results. Another analysis in the literature treats reward-only advantages as provably AUC-inconsistent (see [[reward-only-advantage-miscalibration]]); the present work does not test that account against its own runs.

## Related

- [[decoupled-claim-calibration-training]] — the same symptom, confidence above 0.9, attributed there to whole-rollout advantage; this note attributes it to division by the group spread. The two are not tested against each other.
- [[reward-only-advantage-miscalibration]] — proves that a reward-only advantage is AUC-inconsistent; the mechanism here is about the scale of the advantage rather than the information it is a function of.
- [[log-score-verbalized-confidence-reward]] — a logarithmic scoring reward for confidence tokens, the same family as the reward that this repair switches to, applied there with the loss masked to confidence tokens.
- [[calibration-aware-policy-optimization]] — the general direction of changing what the advantage depends on so that calibration is not left to the reward alone.
- [[semantic-distance-graded-confidence-target]] — the same paper's graded training target for confidence, the other part of its calibration design.

[^c1]: arxiv-2512-15528 — "Empirically, this setting leads to severe overconfidence on VEC, with confidence estimates heavily concentrated above 0.9"
[^c2]: arxiv-2512-15528 — "the normalization amplifies minor relative advantages, causing the model to repeatedly increase the probability of slightly preferred responses"
[^c3]: arxiv-2512-15528 — "Based on empirical exploration, we adopt the log-likelihood reward for confidence calibration"
[^c4]: arxiv-2512-15528 — "two modifications effectively mitigate the overconfidence issue"
