---
description: "Length and formatting enter a within-group comparison model as covariates, estimated jointly with quality, so their link to observed rankings is absorbed rather than rewarded."
aliases: ["objective-preserving attribute adjustment", "attribute-adjusted comparison model", "covariate-adjusted ranking reward", "auxiliary attribute covariates in preference fitting"]
sources: ["doi-10-48550-arxiv-2609-23457"]
---
# Covariate-adjusted comparison reward

A familiar fix for an unwanted property of a model's output is to add a reward term for the opposite. The work argues that this turns the auxiliary property into a training target and widens the surface a policy can exploit: "may unintentionally turn an auxiliary property into an optimization target."[^c1] The alternative it proposes keeps the rubric fixed and leaves the auxiliary property out of the reward altogether, but inside the fitting model, as a covariate.

Mechanically, each auxiliary attribute is turned into a pairwise contrast. For two rollouts with attribute values a_i and a_j, the paper builds a normalized difference, (a_i − a_j) / (a_i + a_j + ε), and standardizes it over the comparisons in the group.[^c2] These contrasts enter the same logit that already carries the criterion utilities of the [[within-group-ordinal-utility-aggregation|within-group comparison]]: the probability that one rollout beats another is a sigmoid of the utility difference plus a weighted sum of attribute contrasts. The attribute weights are fitted together with the utilities. "Both are estimated jointly, so the attributes influence the quality estimation without becoming additional reward dimensions."[^c3] The quality utility is thereby net of whatever part of the observed ranking the attributes explain, and the reward that comes out is built from the quality utility alone.

Two attributes are worked out. For reasoning length, the authors state the premise plainly: "a positive association between reasoning length and observed preference need not reflect a genuine quality benefit."[^c4] Their control does not remove the length term. It attenuates the fitted positive coefficient by a fraction λ and leaves non-positive coefficients alone, which "controls the strength of adjustment without imposing a target response length."[^c5] For formatting, the statistics are headings, lists and emphasis, normalized, standardized and included as covariates, so that formatting preference is controlled "without directly rewarding formatting."[^c6]

## What was measured

The length control was run on one training trajectory of Qwen3.5-9B, resumed from step 70, with λ set to 0, 0.25, 0.5 and 0.75.[^c7] The authors report that "the adjustment changes reasoning extent while keeping the capability-level averages within a narrow range."[^c8] So the knob moves how much the model reasons while the capability averages stay close.

The formatting control was run on the same trajectory. Formatting density rose before control and fell after attribute adjustment, while query-dependent markers stayed roughly stable. The formatting-controlled variant reached a capability average of 68.32, against 67.95 for the RLVR2+ row of the same table.[^c9] The text reads this as evidence that "formatting-related preference can be controlled without expanding the rubric or directly rewarding formatting."[^c10]

Against the usual route of a [[reward-model-bias-linear-tractability|null-space projection]], which removes a length direction from the reward, this one estimates the attribute's effect from the data. Against the judge-side [[llm-judge-biases|verbosity bias]], it is a training-side correction for the same tendency. The same logic of putting a known confound into the model and reading the residual appears in [[debiased-language-preference]], which regresses confounds out of a measured score; the difference is that here the confound is estimated inside the reward's own fitting step.

## Limits

- The premise is "need not reflect," which is weaker than "does not." Joint estimation cannot tell a length association that is pure padding from one that carries content, unless some assumption separates them. The paper's attenuation is a judgment that part of the positive coefficient is not quality; it does not measure how much (my inference).
- Because λ is applied to a fraction of the coefficient, the paper's own wording is "We randomly attenuate a fraction λ of the fitted positive coefficient." The reason for random rather than deterministic attenuation is not given in the parts read, so the strength of the control is a stochastic setting, not a fitted estimate (my inference).
- The only evidence for the length control is a single model and a single trajectory. The quality side is judged by capability averages, which "remain within a narrow range"; no measure of quality net of length is reported in the parts read.
- The attributes tested are length, headings, lists and emphasis. Other hackable attributes, such as repetition or template reuse, are not shown to be absorbed by the same mechanism.
- The method assumes the attributes are measurable per response and that their association with ranking is roughly linear in the logit. Neither is tested against the alternatives.
- I read the method and the two analysis subsections; I did not read the ablation on robustness and cost.

## Related

- [[within-group-ordinal-utility-aggregation]] — the comparison model these covariates enter; without it there is no logit to adjust
- [[reward-model-bias-linear-tractability]] — removes length, uncertainty and position by projecting a linear direction out of the reward; the covariate route instead estimates the association from rankings
- [[llm-judge-biases]] — the verbosity and position bias of judges that makes length a live confound for the reward
- [[debiased-language-preference]] — the same residual logic, applied to measured language preference rather than to a training reward

[^c1]: doi-10-48550-arxiv-2609-23457 — "may unintentionally turn an auxiliary property into an optimization target"
[^c2]: doi-10-48550-arxiv-2609-23457 — "We construct a normalized contrast for each attribute,"
[^c3]: doi-10-48550-arxiv-2609-23457 — "Both are estimated jointly, so the attributes influence"
[^c4]: doi-10-48550-arxiv-2609-23457 — "preference need not reflect a genuine quality benefit."
[^c5]: doi-10-48550-arxiv-2609-23457 — "This controls the strength of adjustment without imposing a target response length"
[^c6]: doi-10-48550-arxiv-2609-23457 — "preferences without directly rewarding formatting."
[^c7]: doi-10-48550-arxiv-2609-23457 — "We resume the Qwen3.5-9B run from step 70"
[^c8]: doi-10-48550-arxiv-2609-23457 — "the adjustment changes reasoning extent while keeping the"
[^c9]: doi-10-48550-arxiv-2609-23457 — "close to the 67.95 of RLVR2"
[^c10]: doi-10-48550-arxiv-2609-23457 — "formatting-related preference can be controlled without expanding the rubric or directly rewarding"
