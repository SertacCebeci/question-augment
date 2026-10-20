---
description: "Static weighted sums of rubric criteria let some criteria saturate while others stay unmet; reweighting each criterion by its estimated remaining headroom rebalances the reward during training."
aliases: ["reward polarization", "static scalarization", "headroom-weighted criterion reweighting", "criterion saturation"]
sources: ["doi-10-48550-arxiv-2605-26579", "doi-10-48550-arxiv-2510-15859"]
---
# Criterion saturation and headroom

When a model is trained against several rubric criteria at once, each criterion is a separate dimension of quality, and the criteria do not improve at the same speed. Easier ones, such as fluency or format, reach their ceiling early; harder ones, such as a nuanced trade-off or a decisive task requirement, stay below it for longer.[^c1] The concept is the gap between a criterion's current score and its ceiling. The paper calls this remaining room "frontier headroom," and it is the quantity a fixed weighting cannot see.

The mechanism is this. A judge scores each sampled answer on every criterion, and a static scalarizer folds those scores into one reward with fixed weights. Such a scalarizer "can fail to track this changing profile, continuing to emphasize saturated criteria while under-weighting" the rest.[^c2] The reward then ranks a polished answer above one that misses a decisive requirement, because the polished answer collects the reward from criteria that are already satisfied.[^c3] The failure is a property of the aggregation, not of any single judgment: each criterion may be scored correctly and the sum still pays for the wrong thing.

The paper's proposal estimates saturation from the reward itself. For a group of sampled answers, it converts their rewards into Gibbs weights at a temperature, uses those weights to average each criterion's scores over the group, and divides by the score ceiling. The result is a per-criterion saturation value P between 0 and 1.[^c4] The fixed weights are then multiplied by a headroom factor, (1 − P) raised to a power γ with a small smoothing constant, and renormalized so that the total weight mass is unchanged.[^c5] Criteria that the strong rollouts still fail receive more emphasis, and the rest receive less. The estimate is recomputed online as training proceeds, so the emphasis moves with the policy rather than being set once.

What the authors measured: on Qwen2.5-7B-Instruct, Qwen3-8B and Qwen3-30B-A3B, trained with rubric-based rewards and evaluated on six benchmarks, the reweighted reward beat the strongest static baseline in all 18 model–benchmark comparisons, with average gains of "+1.38 points on Qwen3-8B, and +2.50 points on Qwen3-30B-A3B."[^c6] The authors also report that the value of the temperature matters: "an overly large temperature may over-smooth the" rollout weights and weaken the saturation estimate.[^c7] The paper also gives a theorem that the static base weighting is locally misaligned whenever headroom differs across criteria, and that the misalignment vanishes when headroom is homogeneous.[^c8]

The concept is not new in kind. Static aggregators already exist in the paper's comparison: a bottleneck-style baseline "using bottleneck-style weights with minimum criterion score," and a uniform baseline.[^c9] What the headroom view adds is a diagnosis of when a fixed aggregator goes wrong, namely when criteria saturate at different rates. A reader who wants to know whether a given rubric needs this should ask whether its criteria are saturating unevenly, which the paper says is a property of the training trajectory and not of the rubric alone.

A second remedy for the same saturation works by removal rather than reweighting. InfiMed-ORBIT keeps a rubric for a query only while its pass rate stays below a threshold, a response passing a rubric when its judge score reaches a set level, because "Rubrics with excessively high pass rates contribute limited supervision value."[^c12] The motivation is the one this note describes, in the paper's words: "rewards often saturate quickly within rollout groups, producing identical scores and zero-variance advantages."[^c13] Removal is a hard gate on a criterion's contribution, where headroom weighting is a soft one. The sources read here do not compare the two, so which handles uneven saturation better is untested. (my reading)

## Limits

- The saturation estimate is only as good as the judge. The authors state that the method "benefits from well-calibrated rubric feedback, as is common in rubric-based RL," and that a judge which confuses criteria or miscalibrates absolute scores corrupts the estimate.[^c10]
- The theorem rests on "the symmetric and isotropic simplifications" and on a headroom-shaped edge model stated in an appendix.[^c11] I did not read that appendix. The bridge from the group estimate P to true frontier headroom is asserted in the main text, not measured in the parts I read. (my reading)
- The gains are averages over a few points on one family of tasks and one training recipe (GSPO on verl, 10K-example rubric subsets). No run compares the reweighting against a learned aggregator, and no run tests whether the gain survives when the criteria are weighted by a human rather than a preset prior. (my reading)
- The argument concerns the training reward. Whether the same headroom logic should govern which answer is chosen at inference, or how a rubric-based evaluation is reported, is my inference and was not tested here.
- The reweighting changes relative emphasis, not the criteria themselves. A criterion missing from the rubric is never saturated and never reweighted; the method cannot notice what the rubric omits. (my inference)

## Related

- [[compensatory-leakage]] — the flaw of scalar combination in which a strong criterion overturns an earlier one; headroom reweighting targets the same imbalance by changing the weights during training, not by testing each criterion as a gate
- [[pessimistic-min-judge-aggregation]] — the other common answer to a single aggregate score, taking the worst judge; the paper's bottleneck baseline is a per-criterion analogue, and it is one of the static aggregators the headroom method is compared against
- [[reliability-weighted-signal-fusion]] — weighting each signal by a softmax over a per-signal score; the headroom factor plays a similar role for criteria, but is estimated from the current rollout group rather than from a fixed reliability
- [[reward-overoptimization]] — a policy that drives a proxy reward up while true quality falls; uneven criterion saturation is one mechanism by which an aggregate reward can rise while a dimension is left behind

[^c1]: doi-10-48550-arxiv-2605-26579 — "as easier criteria saturate earlier while harder ones remain under-satisfied"
[^c2]: doi-10-48550-arxiv-2605-26579 — "fail to track this changing profile, continuing to emphasize saturated criteria while under-weighting"
[^c3]: doi-10-48550-arxiv-2605-26579 — "rubric criteria, with some criteria becoming saturated while others remain under-satisfied."
[^c4]: doi-10-48550-arxiv-2605-26579 — "to estimate the saturation degree of each criterion in the rubric, which forms"
[^c5]: doi-10-48550-arxiv-2605-26579 — "Since 1 − P estimates remaining frontier headroom"
[^c6]: doi-10-48550-arxiv-2605-26579 — "+1.38 points on Qwen3-8B, and +2.50 points on Qwen3-30B-A3B"
[^c7]: doi-10-48550-arxiv-2605-26579 — "an overly large temperature may over-smooth the"
[^c8]: doi-10-48550-arxiv-2605-26579 — "Theorem 2 shows that homogeneous base-weighted headroom makes the variance term vanish"
[^c9]: doi-10-48550-arxiv-2605-26579 — "using bottleneck-style weights with"
[^c10]: doi-10-48550-arxiv-2605-26579 — "well-calibrated rubric feedback, as is common in rubric-based RL."
[^c11]: doi-10-48550-arxiv-2605-26579 — "Under the symmetric and isotropic simplifications"
[^c12]: doi-10-48550-arxiv-2510-15859 — "Rubrics with excessively high pass rates contribute limited supervision value"
[^c13]: doi-10-48550-arxiv-2510-15859 — "rewards often saturate quickly within rollout groups, producing identical scores and zero-variance advantages."
