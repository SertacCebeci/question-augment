---
description: "Split a predictor's total KL error into update divergence, its distance from its own best-fit discounted filter, and misspecification divergence, the best-fit filter's distance from the truth."
aliases: ["update divergence", "model misspecification divergence", "error split into updating and misspecification"]
sources: ["arxiv-2512-18489"]
---
# Update versus misspecification divergence

A forecaster that predicts a sequence of outcomes can be wrong for two different reasons. It may fold each new observation into its belief less faithfully than its own evidence warrants. Or its belief may be built from a family of updates that cannot track the true process, however carefully it updates inside that family. The decomposition separates the two by putting a reference filter between the predictor and the truth. The reference is the best-fit member of a discounted Bayesian filter family, with a discount factor γ* fitted to the predictor's own trajectory. The paper describes the total divergence as "decomposing the total divergence into two components" and reads it as a sum of two terms.[^c1]

The first term, the update divergence, is the KL divergence from the predictor's predictive distribution to the reference: D_Update = KL(p̂ ∥ p_Bayes(γ*)). It "Measures if the LLM is a principled discounted" updater.[^c2] The second term, the model misspecification divergence, is KL(p_Bayes(γ*) ∥ p_Truth). It "Measures the inherent error of the" best-fit filter.[^c3]

The split says where the error lives. On the paper's probes the update term is "consistently small (typically < 13% of total error)"[^c4], and "The majority of the total error" comes from the misspecification term.[^c5] The authors read this as predictors that are "proficient discounted updaters" rather than flawed Bayesians.[^c6] The conclusion places the error the same way: predictive errors come "from model misspecification rather than faulty updating."[^c7] The paper traces the misspecification term to "miscalibrated priors and intrinsic discounting,"[^c8] so on this reading the prior and the family, not the updating step, carry most of the error.

The reading depends on how the term is built. The reference γ* is chosen to minimise the predictor's total divergence to the discounted family, and the update term is that minimised value divided by T. My reading of the paper's Algorithm 1 is therefore that the update term is the fit residual. A small value says the family fits the predictor well at its best γ. It does not separately certify that the predictor updates well. Its size is evidence about the discounted family, and only indirectly about the predictor's updating.

**Transfer.** What survives the move to other forecasters is the question itself: is the error in the updating rule, or in the family the rule is drawn from? A different reference family, such as a sliding window, a hierarchical prior or a changepoint detector, would give a different misspecification term, and the decomposition would then describe that family. What does not carry over automatically is the additive reading. KL is not symmetric, and the two terms place the predictor and the reference in different slots. The text I read does not state an identity showing that the two terms add to the total. Whether they do is my inference to check, not a result I can report.

**Relevance to asking.** A predictor that drifts after a change can be repaired by changing how it updates, or by changing the prior it starts from. The decomposition does not say which, but it tells where to look first on these probes. The abstract says the authors "present prompting strategies that effectively recalibrate priors"[^c9], and that inherent priors are often miscalibrated. I did not read those strategies and do not describe them here. This note records only the diagnostic.

## Limits

- Two synthetic probes: a six-sided die whose dominant face "abruptly changes from one to another", and a Gaussian mean. Each has one changepoint, "with a parameter changepoint at t = 51"[^c10], in a sequence of 100 steps. The text does not test gradual drift or repeated shifts.
- Three model families, in base and instruction-tuned variants: "We evaluated the base and instruction-tuned variants of"[^c11] three families. The text reports differences between families, but the slices I read give no interval on the divergence terms.
- The predictive distribution is read from "applying softmax to the output logits for all possible next" outcomes.[^c12] A different readout of the same model would change every term, and the paper does not test this. That the readout matters is my inference.
- Both terms need the true predictive distribution, p_Truth. Synthetic probes supply it. For a task with no known generator the split as written cannot be computed, and a proxy would be a different quantity. This is my inference.
- The update term is the fit residual (see above), so a small value cannot serve as an independent test of updating.

## Related

- [[kl-divergence]] — the divergence both terms are built from
- [[forgetting-factor-beta-bernoulli]] — the discounted filter that serves as the reference, in its Beta-Bernoulli form
- [[uncertainty-sampling-regime-shift-lag]] — a query rule facing the same kind of abrupt shift, where a reference filter would be the question
- [[belief-trajectory-drift-evaluation]] — tracking a model's probability over time against an external reference, rather than a fitted filter

[^c1]: arxiv-2512-18489 — "decomposing the total divergence into two"
[^c2]: arxiv-2512-18489 — "Measures if the LLM is a principled discounted"
[^c3]: arxiv-2512-18489 — "Measures the inherent error of the"
[^c4]: arxiv-2512-18489 — "consistently small (typically < 13% of total error)"
[^c5]: arxiv-2512-18489 — "The majority of the total error"
[^c6]: arxiv-2512-18489 — "it suggests LLMs are not flawed Bayesian updaters but proficient discounted updaters"
[^c7]: arxiv-2512-18489 — "from model misspecification rather than faulty updating"
[^c8]: arxiv-2512-18489 — "miscalibrated priors and intrinsic discounting"
[^c9]: arxiv-2512-18489 — "present prompting strategies that effectively recalibrate priors"
[^c10]: arxiv-2512-18489 — "with a parameter changepoint at t = 51"
[^c11]: arxiv-2512-18489 — "We evaluated the base and instruction-tuned variants of"
[^c12]: arxiv-2512-18489 — "applying softmax to the output logits for all possible next"
