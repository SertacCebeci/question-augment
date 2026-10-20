---
description: "An entropy cost on the outcomes a belief implies pulls an inferred Bernoulli rate toward extremes: inference converges, but to a biased value that reads as more predictable."
aliases: ["unpredictability cost", "entropy cost on implied outcomes", "predictability-biased inference"]
sources: ["doi-10-7554-elife-81256"]
---
# Unpredictability-cost belief bias

A learner who reports a belief about a binary process can be charged for the kind of environment that belief describes, rather than for how sharp the belief is. The charge here is the Shannon entropy of the outcome implied by the belief's parameter, averaged over the belief. The authors' premise is that subjects "favor, in their inference, parameter vectors" that imply more predictable outcomes.[^u1] For a Bernoulli rate, a belief concentrated near 0 or 1 is cheap, and a belief concentrated near 0.5 is dear, because the outcome it describes is the least predictable one.

When this cost is added to a divergence from the Bayesian posterior, the minimizer is the Bayesian posterior multiplied by a factor that favours low-entropy values, "and of a function that is larger for values of" the rate that imply a more predictable environment.[^u2] My reading of the paper's expression is that this factor is an exponential in the number of trials, so its pull on the posterior grows as data accumulate. The belief is therefore pushed toward predictable values while evidence keeps arriving.

What results is a stable bias, not a failure to converge. In the Bernoulli case the posterior does peak at a value, and that peak does settle, but it sits "closer to the extremes (0 and 1) than the stimulus generative probability": the learner ends up in "an environment more predictable than the actual one."[^u3] The paper's summary is that "except in the equiprobable case, the inference converges but it is biased."[^u4] Nothing is forgotten here. A consistent, wrong estimate is reached.

The same mechanism reaches sequences when the learner allows dependence between consecutive stimuli. The converged belief then "corresponds to an erroneous belief about the dependency of the stimulus on the recent stimulus history."[^u5] The stored belief does not depend on history, since the asymptotic posterior "does not itself depend on the history of the stimulus."[^u6] The history dependence enters at prediction time, through the assumed serial dependence. This is the route by which this family yields the sequential effects described in [[attractive-repulsive-sequential-effects]]. The step from a history-free belief to history-dependent predictions is my inference from the paper's Markov case.

The paper contrasts this with the precision cost, and says the two "do so by giving rise to qualitatively different inference processes."[^u7] The precision-cost family discounts old evidence instead of biasing the belief; see [[forgetting-factor-beta-bernoulli]]. Both are fitted to the same subjects, and the data do not separate them cleanly: the authors report that "not provide decisive evidence in favor of either model" under Bayesian model selection.[^u8]

## Limits

- The bias is a modelling result. The paper shows that a cost of this form fits some subjects' predictions, not that subjects represent entropy. A prior that favours extreme rates would give a posterior of the same shape, and nothing here separates a cost from such a prior. That distinction is my inference.
- The evidence is one binary task, a lightning-strike prediction with rates from 0.05 to 0.95, in blocks of 200 trials. No other environment or stimulus type is tested.
- The claim that the bias is absent at p = 0.5 is singular and stated in the paper as a special case, not generalised. The bias claim holds for p away from 0.5.
- Fitting identifies the cost weight and the response parameter jointly. The authors report that "corresponds to the true model in at least 70% of simulations" for model recovery, against a chance level of one in eight.[^u9] That is a check on the fitting procedure, not evidence that the cost is the right one.
- Not every subject is best fitted by this family. The paper reports a hybrid model, and the two families both capture part of the data.

## Related

- [[forgetting-factor-beta-bernoulli]] — the other cost family in the same framework: a precision cost discounts old evidence rather than biasing the belief.
- [[resource-rationality]] — the framing in which an inference cost is traded against accuracy.

[^u1]: doi-10-7554-elife-81256 — "the subjects favor, in their inference, parameter vectors"
[^u2]: doi-10-7554-elife-81256 — "and of a function that is larger for values of"
[^u3]: doi-10-7554-elife-81256 — "it implies an environment more predictable than the actual one"
[^u4]: doi-10-7554-elife-81256 — "except in the equiprobable case, the inference converges but it"
[^u5]: doi-10-7554-elife-81256 — "the asymptotic posterior corresponds to an erroneous belief about the dependency of the stimulus on the recent stimulus"
[^u6]: doi-10-7554-elife-81256 — "which does not itself depend on the history of the stimulus"
[^u7]: doi-10-7554-elife-81256 — "they do so by giving rise to qualitatively different inference processes"
[^u8]: doi-10-7554-elife-81256 — "not provide decisive evidence in favor of either model"
[^u9]: doi-10-7554-elife-81256 — "corresponds to the true model in at least 70% of simulations"
