---
description: "Predictions of binary sequences lean toward the latest stimulus (attractive) and, at the third-to-last position, sometimes away from it (repulsive), beyond the base rate."
aliases: ["sequential effects", "attractive effect", "repulsive effect", "recency effect in prediction"]
sources: ["doi-10-7554-elife-81256"]
---
# Attractive and repulsive sequential effects

In a sequence of independent stimuli, the previous stimulus carries no information about the next, so a rational predictor should ignore it. Human predictions do not. In a binary prediction task with Bernoulli stimuli, subjects predicted A more often after an A than after a B, for every generative probability tested: "these two conditional proportions are markedly different for all stimulus generative probabilities."[^s1] The paper calls this the attractive effect, in which predictions are "biased toward the recent stimulus history" even though "the environment is static and the Bayesian belief converges."[^s2][^s3] The effect is strongest when the generative probability is near 0.5 and weaker at the extremes.[^s4]

The attractive effect is not the whole pattern. Going further back, the paper finds a repulsive effect, "in which predictions are biased away from" stimuli "presented in more distant trials."[^s5][^s6] The clearest case is the third-to-last stimulus: "the third-to-last stimulus is A followed by the sequence BA."[^s7] An older A, in that position, lowers the chance of predicting A, so the sign flips relative to the recent-trial effect. This is what makes the pattern counter-intuitive: the same stimulus pushes toward its own prediction when recent and away from it when older.

The two model families the paper fits do not account for this equally. The attractive effect is captured by both: "Both classes of models capture this" pattern.[^s8] The repulsive effect is produced by one only. The paper states that "we do not obtain any repulsive effect with any of the unpredictability" cost models, while it appears with the precision-cost models of Markov observers.[^s9] The mechanism for the precision family is exponential discounting of old evidence, which "amounts to an exponential discount of remote observations."[^s10] Under that process a third-to-last stimulus is still in the belief, and its weight in the prediction is what the fit reproduces.

The repulsive pattern also shows up in the data of subjects best fitted by the family that does not predict it. The authors write that they "also find, perhaps surprisingly, a significant repulsive effect of the third-to-last" stimulus among those subjects.[^s11] So the observation of repulsion does not, by itself, favour the precision family. It is a feature of the data that the best-supported model is not the only one to match.

## Limits

- One task: binary lightning-strike predictions, blocks of 200 trials, generative probabilities from 0.05 to 0.95, with a stationarity check on the second half of each block. No other task or stimulus structure is tested.
- The effects are measured on predictions, which are responses. The response rule (a generalised probability matching with a fitted exponent) can shape the pattern. The paper reports that a propensity to repeat or alternate "these analyses do not change our conclusions."[^s12] That is a robustness check within the paper's model class.
- Model selection is not decisive. The authors report that Bayesian model selection gives no "decisive evidence in favor of either model."[^s13] The sign of the repulsive effect is thus a result about the data, not a verdict on the mechanism.
- The repulsive effect is reported at a specific pattern (third-to-last A, then BA). The paper does not establish a general repulsion at every lag, and I have not checked the other patterns in the figures.
- Whether these effects survive feedback changes, non-binary stimuli, or non-stationary environments is not tested here.

## Related

- [[forgetting-factor-beta-bernoulli]] — exponential forgetting of old evidence, the mechanism behind the precision-cost family's attractive and repulsive predictions.
- [[unpredictability-cost-belief-bias]] — the other family, which produces the attractive effect through a biased belief rather than through forgetting.

[^s1]: doi-10-7554-elife-81256 — "these two conditional proportions are markedly different for all stimulus generative probabilities"
[^s2]: doi-10-7554-elife-81256 — "biased toward the recent stimulus history"
[^s3]: doi-10-7554-elife-81256 — "the environment is static and the Bayesian belief converges"
[^s4]: doi-10-7554-elife-81256 — "this attractive sequential effect seems stronger for values"
[^s5]: doi-10-7554-elife-81256 — "in which predictions are biased away from"
[^s6]: doi-10-7554-elife-81256 — "stimuli presented in more distant trials"
[^s7]: doi-10-7554-elife-81256 — "the third-to-last stimulus is A followed by the sequence BA"
[^s8]: doi-10-7554-elife-81256 — "Both classes of models capture this"
[^s9]: doi-10-7554-elife-81256 — "do not obtain any repulsive effect with any of the unpredictability"
[^s10]: doi-10-7554-elife-81256 — "amounts to an exponential discount of remote observations"
[^s11]: doi-10-7554-elife-81256 — "we also find, perhaps surprisingly, a significant repulsive effect of the third-to-last"
[^s12]: doi-10-7554-elife-81256 — "these analyses do not change our conclusions"
[^s13]: doi-10-7554-elife-81256 — "not provide decisive evidence in favor of either model"
