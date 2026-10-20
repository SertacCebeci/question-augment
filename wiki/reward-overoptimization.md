---
description: "A learned reward keeps rising with KL from the reference while the true reward peaks and then falls; a fitted scaling law gives the curve, and DPO is reported to show the same pattern."
aliases: ["Goodhart in RLHF", "proxy reward overoptimization", "reward exploitation under KL", "overoptimization scaling law"]
sources: ["arxiv-2601-06108", "doi-10-48550-arxiv-2608-11669", "arxiv-2512-07407"]
---
# Reward overoptimization

A reward model is trained on finite preferences and is only a proxy for what people want. Optimize the proxy hard enough and the policy moves to where the proxy is high while the true objective is not. The work's figure shows the shape: "Proxy reward increases monotonically with KL from reference," while "true reward peaks then declines."[^c1]

The work takes the curve from a scaling study: "Gao et al. [11] establish scaling laws for reward model exploitation."[^c2] Under RL optimization, the true reward is modeled as a constant plus a coefficient times the square root of the KL from reference, minus a second coefficient times the KL. Under best-of-n sampling the same shape holds with the logarithm of n in place of the KL. The coefficients are said to scale predictably with reward model size: "where coefficients scale predictably with reward model".[^c3] The point of the form is that the peak is not a fixed property of the policy. It moves with the size of the proxy and with how far the policy is pushed from its reference.

The work then reports that the pattern is not specific to explicit reward models. "Critically, Rafailov et al. [19] show that DPO" "exhibits identical overoptimization patterns despite" "lacking an explicit reward model".[^c4] On this reading the implicit reward of [[dpo-implicit-reward]] is also exploitable, and the work reports the effect as occurring "fore completing one epoch of training."[^c5]

The same shape has been reported when the reward is a rubric, out of distribution. A 2026 preprint trains Qwen3-8B with GRPO on medical rubrics and grades an out-of-distribution benchmark with both the training judge and a stronger gold judge. The gold score peaks and then falls while the training judge's score keeps rising, and the authors read this as reward hacking because "so the divergence is reward hacking, not judge noise."[^c6] A judge with a fixed bias would move the gold curve by a constant instead of sending it down. They describe the result as "the Gao-style signature for rubric rewards, out of distribution."[^c7] In that setting, dropping a random subset of the rubric's criteria at each step "lowers the two hacking measures we track" (see [[rubric-criterion-dropout]]), and the two-judge measurement behind the reading is set out in [[proxy-gold-divergence-signal]].[^c8]

## Limits

- Theorem 7.1 is presented as a theorem, but its content is the fitted form of an empirical study. I treat it as a fit to the data of that study, not a derivation (my reading).
- The work does not give the values of the coefficients or the fitting procedure, and it does not re-estimate them. The claim that they scale predictably is the cited study's, not checked here.
- The DPO result is cited to a single other paper; the work does not re-run it, and the claim that DPO overoptimizes early in training is not separately measured here.
- The curve is shown for a proxy reward against KL from one reference. Whether the same peak appears for other reward types, tasks or domains is not tested in this work.
- Table 2 lists mitigations such as early stopping and stronger KL, and the work does not compare them against each other.
- The rubric-reward case rests on one run per configuration, so the reported gains are within-run and not across seeds. The preprint says "Every configuration is a single training run" and does not test the curve beyond two benchmark pairs.[^c9]

## Related

- [[dpo-implicit-reward]] — the implicit reward that the work reports as overoptimized in the same way
- [[process-reward-model-hackability]] — a separate case of a learned reward being exploited, measured on step-level reward models
- [[kl-divergence]] — the KL on the horizontal axis of the curve, measured from the reference policy
- [[coverage-separation-offline-online]] — the offline and online split for learning from preference data, which decides how much exploitation the data can support
- [[proxy-gold-divergence-signal]] — the two-judge reading of this divergence for rubric rewards, where a fixed judge bias is ruled out as the cause
- [[accuracy-auditability-trade-off]] — a different exploit of an answer-checking proxy: the reasoning moves into prose and the tool keeps only a minimal final program, which the authors call reward hacking.[^c10]

[^c1]: arxiv-2601-06108 — "Proxy reward increases monotonically with KL from reference,"
[^c2]: arxiv-2601-06108 — "Gao et al. [11] establish scaling laws for reward model"
[^c3]: arxiv-2601-06108 — "where coefficients scale predictably with reward model"
[^c4]: arxiv-2601-06108 — "exhibits identical overoptimization patterns despite"
[^c5]: arxiv-2601-06108 — "fore completing one epoch of training."
[^c6]: doi-10-48550-arxiv-2608-11669 — "so the divergence is reward hacking, not judge noise."
[^c7]: doi-10-48550-arxiv-2608-11669 — "We observe the Gao-style signature for rubric rewards, out of distribution."
[^c8]: doi-10-48550-arxiv-2608-11669 — "lowers the two hacking measures we track"
[^c9]: doi-10-48550-arxiv-2608-11669 — "Every configuration is a single training run"
[^c10]: arxiv-2512-07407 — "This pattern is a clear instance of reward hacking"
