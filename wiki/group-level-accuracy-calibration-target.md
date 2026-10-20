---
description: "Training a verbalized confidence toward the rollout group's mean correctness, not each sample's 0/1 outcome, gives an unbiased, lower-variance calibration target at no extra labelling cost."
aliases: ["group-level accuracy supervision", "hybrid instance-group calibration target"]
sources: ["arxiv-2603-09117"]
---
# Group-level accuracy as calibration target

A single rollout's correctness is a Bernoulli draw, a poor label for "how likely is this question to be answered correctly". Cheng et al. (2026, DCPO paper) note that "traditional instance-level binary supervision is insufficient for calibration optimization", being highly stochastic and pushing the model toward overly sharp distributions.[^c1]

## Mechanism

GRPO already samples G responses per question. Their mean correctness is the target. The paper proves "R̃G is an unbiased estimator of E[R(y)]" with variance O(1/G).[^c2] With absolute-error calibration loss |c - r|, the gradient variance under the instance label is 4p(p-1) in magnitude form, and zero under the group label for confidence not equal to the group mean; so group supervision never has higher variance, equality only when p is 0 or 1 (the paper's Proposition 4.4, my paraphrase of the derivation).

Pure group targets lose per-sample discrimination: every response to a question gets the same target. So a hybrid is used, R_IG = lambda * group + (1 - lambda) * instance, and the confidence reward is the negative absolute distance between stated confidence and R_IG. No external oracle or extra annotation is needed.

Ablation: removing group-level labels "causes a clear accuracy drop" (60.8% to 58.7%), and removing the instance part raises ECE (0.128 to 0.209).[^c3]

## Limits

The variance proof assumes i.i.d. Bernoulli outcomes within a group and a fixed question; with small G the estimate is still noisy, and G is tied to GRPO's compute budget. The group mean estimates question difficulty for the current policy, so the confidence learned is a difficulty estimate, not a per-answer correctness signal; the lambda mix is hand-chosen. Verified only on math and code with checkable answers.

## Related

- [[accuracy-calibration-gradient-conflict]] — the masked-gradient half of the same method.
- [[calibration]] — what the target is meant to approximate.
- [[log-score-verbalized-confidence-reward]] — a proper-scoring reward for verbalized confidence, instance-level.
- [[reward-only-advantage-miscalibration]] — why reward-only signals fail to calibrate.

[^c1]: arxiv-2603-09117 — "traditional instance-level binary supervision is insufficient for calibration optimization"
[^c2]: arxiv-2603-09117 — "Proposition 4.3. R̃G is an unbiased estimator of E[R(y)]"
[^c3]: arxiv-2603-09117 — "a notable increase in ECE from 0.128 to 0.209, while removing group-level labels causes a clear accuracy drop"
