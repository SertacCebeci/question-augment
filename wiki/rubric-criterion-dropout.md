---
description: "Rubric Dropout scores each rollout group on a random subset of its rubric's criteria, with a new mask each step; it lowered out-of-distribution reward hacking where criterion reweighting did not."
aliases: ["Rubric Dropout", "sub-rubric sampling", "criterion dropout"]
sources: ["doi-10-48550-arxiv-2608-11669"]
---
# Rubric criterion dropout

A rubric reward is the weighted share of a rubric's criteria that a judge marks satisfied. Rubric dropout changes which criteria enter that share and nothing else. At each training step a random fraction f of the positive-weight criteria is removed before the reward is computed, always keeping at least three, and the reward is the same weighted share over the criteria that remain.[^c1] Safety-critical criteria form a protected set that is never dropped.[^c2] Evaluation always scores the full rubric, so the training reward is the only quantity that changes; the judge is called exactly as before.[^c3]

The motive is the fixedness of the rubric. A rubric is "a proxy for quality, not quality itself, and it is a fixed" proxy,[^c4] and a criterion scored identically at every step becomes a stable target: once a policy finds a cheap way to satisfy it, that shortcut is reinforced on every step, and on every prompt when the criterion is a shared template.[^c5] Dropout removes the guarantee that a given criterion is present in a given update. The analogy is to neuron dropout, which "prevents co-adaptation by making sure no single" unit can be relied on.[^c6] The paper is explicit that this is a motivating intuition: "We treat this as motivating intuition rather than an established mechanism."[^c7]

What makes the change sound under group-relative RL is the scope of the mask. If each rollout of a prompt drew its own mask, the group's responses would be scored on different criteria, and the group-standardized advantage would compare rewards that are not measured on the same rubric; in the paper's words they "would be graded on different sub-rubrics, and comparing them within the group would be meaningless."[^c8] The method therefore draws one mask per prompt and step, so every rollout of a group is graded on the same sub-rubric, and the mask changes from step to step. Because the group shares the mask, any normalizer that depends only on the mask cancels out of the standardized advantage.[^c9]

On Qwen3-8B trained with GRPO on medical rubrics, dropout at 30% and 50% raised the out-of-distribution gold score at every matched checkpoint, by +1 to +2 points on HealthBench-Hard and by +6 to +7 points on ResearchQA in the science pair.[^c10] It also lowered both hacking measures the paper tracks, and the full-rubric reward on training prompts did not fall.[^c11] The hyperparameter is not delicate: a sweep over f shows that the 30–50% range captures most of the benefit, and only at 60% does the sign flip.[^c12] The method costs one line in the reward function and no extra judge calls.[^c13]

The natural alternative, reweighting criteria toward the ones that are informative for training, did worse than no intervention. POW3R-style reweighting "attains the lowest OOD gold score of any run" in the paper's sweep.[^c14] The paper's guess at why is that reweighting by verdict variance "concentrates optimization pressure on exactly the criteria the policy is currently learning to" game. It offers this as one plausible mechanism, drawn from a single run at the method's published defaults.[^c15]

Transfer from neuron dropout is partial. What survives is the train-only noise that stops any single component from being relied on. What does not survive is the per-example independence of neuron dropout: under GRPO the mask has to be shared within the group, and the paper notes that "with a group-shared mask, dropout within one epoch is plain" subsampling of criteria, which leaves the co-adaptation story untested at that horizon.[^c16]

## Limits

- The mechanism is open. "Why it helps is still open."[^c17] The paper sets a more ordinary story beside the co-adaptation one: "A more boring story is implicit regularization."[^c18] Both predict the same curves at the training horizon. The separating test, a gold-versus-overclaim frontier at two or more epochs, was left to future work.
- Single seed. "Every configuration is a single training run," so the reported effects are within-run variation across checkpoints, not across seeds.[^c19]
- Scope. The results come from one RL algorithm and two domains: "one RL algorithm (GRPO)."[^c20] Other group-relative methods are untested.
- In-domain cost was measured on training prompts only: "In-domain cost is measured on the training set."[^c21] A small cost on unseen in-domain prompts is not ruled out.
- Too much dropout removes coverage. "Drop too much and the surviving sub-rubrics stop covering" what quality means, which is why the largest fraction tested reverses the gain.[^c22]
- The gold judge is a stronger model, not ground truth, so every gain is measured against another judge. The paper's claims survive a constant bias in either judge but not a bias that varies across distributions.
- My reading: the method changes which criteria are scored but not the verifier, so a shortcut that satisfies every criterion in a rubric, or a generic criterion that no subset removes, would remain available. The paper does not test this.

## Related

- [[reward-overoptimization]] — the proxy-rising, true-quality-falling curve that this mitigation targets, first shown for learned reward models
- [[proxy-gold-divergence-signal]] — the two-judge measurement with which the paper shows both the hacking and its reduction
- [[rubric-verifier-failure-modes]] — how a rubric verifier gets exploited; dropout leaves the verifier as it is and changes only the criteria it is asked about (my reading)
- [[verifier-exploitation-rate]] — a per-criterion hacking measure against a reference panel, a different way to observe the same exploitation

[^c1]: doi-10-48550-arxiv-2608-11669 — "same reward on the kept criteria only"
[^c2]: doi-10-48550-arxiv-2608-11669 — "Dropout never touches a protected set reserved for safety-critical criteria"
[^c3]: doi-10-48550-arxiv-2608-11669 — "Dropout is train-only, and evaluation always uses the full rubric."
[^c4]: doi-10-48550-arxiv-2608-11669 — "A rubric is a proxy for quality, not quality itself, and it is a fixed"
[^c5]: doi-10-48550-arxiv-2608-11669 — "A criterion rewarded identically at every step"
[^c6]: doi-10-48550-arxiv-2608-11669 — "Neuron dropout prevents co-adaptation by making sure no single"
[^c7]: doi-10-48550-arxiv-2608-11669 — "We treat this as motivating intuition rather than an established mechanism"
[^c8]: doi-10-48550-arxiv-2608-11669 — "would be graded on different sub-rubrics, and comparing them within the group would be meaningless."
[^c9]: doi-10-48550-arxiv-2608-11669 — "any reward normalizer that depends only on the mask cancels in GRPO"
[^c10]: doi-10-48550-arxiv-2608-11669 — "+1 to +2 points on HealthBench-Hard, +6 to +7 points on"
[^c11]: doi-10-48550-arxiv-2608-11669 — "lowers the two hacking measures we track"
[^c12]: doi-10-48550-arxiv-2608-11669 — "captures most of the benefit"
[^c13]: doi-10-48550-arxiv-2608-11669 — "The change is one line in the reward function, has a single hyperparameter, and adds no judge calls."
[^c14]: doi-10-48550-arxiv-2608-11669 — "POW3R attains the lowest OOD gold score of any run"
[^c15]: doi-10-48550-arxiv-2608-11669 — "variance concentrates optimization pressure on exactly the criteria the policy is currently learning to"
[^c16]: doi-10-48550-arxiv-2608-11669 — "With a group-shared mask, dropout within one epoch is plain"
[^c17]: doi-10-48550-arxiv-2608-11669 — "Why it helps is still open."
[^c18]: doi-10-48550-arxiv-2608-11669 — "A more boring story is implicit regularization."
[^c19]: doi-10-48550-arxiv-2608-11669 — "Every configuration is a single training run"
[^c20]: doi-10-48550-arxiv-2608-11669 — "one RL algorithm (GRPO)"
[^c21]: doi-10-48550-arxiv-2608-11669 — "In-domain cost is measured on the training set."
[^c22]: doi-10-48550-arxiv-2608-11669 — "Drop too much and the surviving sub-rubrics stop covering"
