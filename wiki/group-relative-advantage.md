---
description: "Group-relative advantage scores each sampled response against the mean of its own sample group instead of a learned value network, trading a critic for the variance of a small group."
aliases: ["GRPO advantage", "group-normalized advantage", "group-relative baseline"]
sources: ["arxiv-2512-22631", "arxiv-2512-18571", "arxiv-2512-12858"]
---
# Group-relative advantage

In reinforcement-style fine-tuning of a language model, the advantage of a response is how much better it did than a baseline. Group-relative advantage takes that baseline from the sampling itself: several responses are drawn for the same prompt, and each response is judged against the others drawn for that prompt. The work under reading states the mechanism in one line: "GRPO computes advantages within each group of responses."[^c1] The update then moves the policy "model parameters relative to the group mean."[^c2] Because the baseline is the group's own average, no separate value model has to be trained, and the authors summarize the saving as "removing value networks and lowering memory."[^c3]

So the method is a choice about where the baseline lives. In a learned critic, as in PPO, the baseline is a function fitted to the data. In group-relative advantage it is the empirical mean of a handful of samples for the same input. The text does not spell out the scaling step (the usual one divides by the group's standard deviation), so that part is not claimed here.

The same update is used where the reward is a sum of costs rather than a correctness score. An embodied agent is scored by task reward minus a weighted sum of action costs, and the group-relative advantage is computed over trajectories scored that way. The authors say the effect is that it "encourages trajectories that achieve the task with lower costs" than their peers.[^c10] Within a group of successful trajectories, the advantage is then a ranking by cost, which is what lets a policy learn to check memory before it moves; see [[heterogeneous-action-cost-substitution]].

In the work, the group is small. "For each question, models generated 4 responses evaluated via four reward functions."[^c4] The four rewards cover format compliance, approximate format match, answer correctness, and numerical validation; the answer-correctness term is "tiered reward based on whether the predicted numerical result matched the ground truth."[^c5] Two consequences follow from the definition itself, and they are mine rather than the authors': if all four responses earn the same reward, every advantage is zero and the group teaches nothing, which is the situation [[zero-variance-group-waste]] analyses; and the size of each advantage depends on how many group members were right or wrong, which is the situation [[spurious-advantage-grpo]] analyses.

The contrast the work draws is with the preference objective. DPO "trains on pairs of preferred and rejected responses," with no group normalization and no reward model.[^c6] The DPO objective itself is a reparameterized log-ratio, treated in [[dpo-implicit-reward]]. The authors explain the faithfulness gap they measure by the reward structure: "This setup encourages systematic reasoning rather than memorisation of answer patterns."[^c7] That is a conjecture about mechanism, and the experiment does not isolate it.

## Limits

The comparison does not separate the baseline from the reward design. GRPO here is trained on four reward functions, while DPO is trained on a preference dataset, so a difference between them cannot be assigned to group-relative normalization alone. The data are also only roughly matched: GRPO used "a similar number of training instances" obtained by sampling "approximately 15% of the original GSM8K training set."[^c8]

The advantage was not shown to be general across scale. The authors report that "this advantage appears only at larger scales," and a 3B collapse that they attribute, without testing, to uniform hyperparameters: "while ensuring fairness, may not be optimal across scales."[^c9] A group of four samples may also be too few for the group mean to be a stable baseline at small model sizes; this is my inference, and the work does not vary group size, so it stays untested here.

The note describes a training mechanism, not a reasoning procedure. Whether group-relative training makes reasoning more faithful is a separate question, measured with proxies that have their own limits (see nli-judge-faithfulness-disagreement).

The critic-free claim is also untested in the embodied work. That paper motivates dropping the critic by "the difficulty of training a reliable value critic," but it never runs PPO on the same task; its only ablation of the update compares against the supervised starting policy.[^c11] Its training figure is labelled "The steady increase in Mean Critic Reward," although the method has no critic, and the text does not say what that quantity is.[^c12] So the cost-ranking reading above is the authors' account of a single run, not a comparison of critic and critic-free updates.

A second use of the group appears in the consistency work (arxiv-2512-12858). There the group is a set of semantically equivalent prompts, not several samples for one prompt. The authors say the grouped form "directly encodes variance minimization as part of the learning signal."[^c13] The reward they train on, though, is a separate term: a convex mix of an informativeness score and a stability score computed over a prompt pair.[^c14] My reading, not the authors' claim: the pressure toward low variance comes from that reward term, and the group-mean baseline is not shown to do the work. The work does not separate the two, so whether the grouping itself carries the consistency effect is untested.

## Related

- [[zero-variance-group-waste]] — groups whose rollouts all agree yield zero advantage; this is the failure mode of a small group
- [[spurious-advantage-grpo]] — the advantage magnitude depends only on in-group correct and wrong counts
- [[dpo-implicit-reward]] — DPO, the pairwise preference objective with no group baseline
- nli-judge-faithfulness-disagreement — the faithfulness proxies on which the two methods are compared
- [[heterogeneous-action-cost-substitution]] — the same update applied to a return that sums costs of different action kinds
- information-consistency-across-equivalent-prompts — the same update used with equivalent prompts as the group, scored by the dispersion of answer information

[^c1]: arxiv-2512-22631 — "GRPO computes advantages within each group of responses"
[^c2]: arxiv-2512-22631 — "model parameters relative to the group mean"
[^c3]: arxiv-2512-22631 — "removing value networks and lowering memory"
[^c4]: arxiv-2512-22631 — "For each question, models generated 4 responses evaluated via four reward functions"
[^c5]: arxiv-2512-22631 — "Answer correctness: tiered reward based on whether the predicted numerical result matched the ground truth"
[^c6]: arxiv-2512-22631 — "trains on pairs of preferred and rejected responses"
[^c7]: arxiv-2512-22631 — "This setup encourages systematic reasoning rather than memorisation of answer patterns"
[^c8]: arxiv-2512-22631 — "we sampled approximately 15% of the original GSM8K training set"
[^c9]: arxiv-2512-22631 — "while ensuring fairness, may not be optimal across scales"
[^c10]: arxiv-2512-18571 — "encourages trajectories that achieve the task with lower costs"
[^c11]: arxiv-2512-18571 — "the difficulty of training a reliable value critic"
[^c12]: arxiv-2512-18571 — "The steady increase in Mean Critic Reward"
[^c13]: arxiv-2512-12858 — "directly encodes variance minimization as part of the learning signal"
[^c14]: arxiv-2512-12858 — "A convex combination yields the scalar training signal"
