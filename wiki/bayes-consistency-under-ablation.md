---
description: "Accuracy can saturate while behaviour still shifts; a score that signs how the fitted prior weight moves under perturbations detects Bayes-consistent change that accuracy misses."
aliases: ["Bayesian Consistency Score", "BCS", "Bayes-consistent behavioural shift"]
sources: ["arxiv-2512-02719"]
---
# Bayes-consistency under ablation

A model can be accurate and still behave in a way that does not respond to the conditions it should respond to. The paper keeps capability, measured by task accuracy and cue-combination efficiency, apart from behaviour, which it scores by behavioural consistency.[^b1] The consistency measure is the Bayesian Consistency Score, which "detects Bayes-consistent behavioural shifts even when accuracy saturates."[^b2]

The score is built on the fitted weight of the static prior-and-measurement observer described in [[precision-weighted-prior-pull]]. The paper chooses five ablations in three multimodal tasks: "These ablations are designed to increase" the prior precision, the measurement precision falling, or both.[^b3] Steering supplies a range or a prompt about noise, "effectively strengthening the prior."[^b17] Blur on the image is meant to "reduce measurement precision."[^b13] A longer context window raises the prior weight "without altering current measurements."[^b14] For each ablation, the paper "compare[s] fitted weights to the base experiment," and the sign of the change gives s_a:[^b15] plus one when the weight does not fall, minus one when it falls. The sign is set to zero when the base weight is above 0.9, "because this indicates a prior-dominant regime, where the model is" effectively ignoring the stimulus.[^b4] "The Bayesian consistency score sums over ablations."[^b5]

Because each of the three tasks has five ablations, the sum runs over a fixed range. The paper normalises with bounds of minus 15 and 15, which "are set equal to the range of scores for five ablations across three" experiments.[^b6] A score near the top means every ablation in every task moved the prior weight the way a Bayesian observer would. A score near the bottom means the opposite. This is my reading of the construction, not a result the paper states.

What the score adds to the paper's accuracy results: the authors note that "the relationship between accuracy and behaviour is empirical and is not by necessity."[^b7] A perfect predictor of the stimulus, they say, "is indistinguishable from a linear model" and so can show no probabilistic tendencies.[^b8] So a high accuracy score says nothing about how the model moves under perturbation. The reported trend is that generally more accurate models show more Bayes-consistent behaviour,[^b16] with exceptions: models of lower accuracy "achieved a decent BCS value" anyway.[^b9]

## Limits

- The score keeps only the sign. The paper focuses on the sign because magnitudes depend on model-specific factors, so a large move and a barely positive move count the same.[^b12] A model with a small but real response is scored like one with a large response.
- The sum hides which ablation moved. A total of plus five could be five small moves or one large move and four zeros. The summary number alone does not show where the behaviour changed.
- Each ablation is chosen to raise the prior weight under the static observer. A model that shifts for another reason, such as a change in prompt format or output length, would score the same way. The score tests direction, not mechanism. The authors say the fitted weights are used "to demonstrate Bayesian consistent behavior" only as probes across conditions, not as proof of a Bayesian computation.[^b10]
- Five ablations across three tasks is a small design. The normalising bounds are the range of this design, so the score is not on an absolute scale and should not be compared with a different ablation set.
- Reasoning was not fully controlled. The authors disabled extended thinking "where possible," and for GPT-5 Mini the residual reasoning "which we can attenuate but not fully disable" stayed on.[^b11] A consistency score from a model with hidden reasoning may reflect that reasoning as well as the observer.

## Related

- [[clean-accuracy-masks-adversarial-collapse]] — the same concern in another setting: a clean score can hide a failure under perturbation
- [[precision-weighted-prior-pull]] — the fitted prior weight that the score is computed from
- [[reliability-weighted-cue-combination]] — the cue-combination efficiency the paper reports alongside this score, a capability measure rather than a behaviour one

[^b1]: arxiv-2512-02719 — "behaviour strategy as measured by (iii) behavioural consistency"
[^b2]: arxiv-2512-02719 — "detects Bayes-consistent behavioural shifts even when accuracy saturates"
[^b3]: arxiv-2512-02719 — "These ablations are designed to increase"
[^b4]: arxiv-2512-02719 — "because this indicates a prior-dominant regime"
[^b5]: arxiv-2512-02719 — "The Bayesian consistency score sums over ablations"
[^b6]: arxiv-2512-02719 — "are set equal to the range of scores for five ablations across three"
[^b7]: arxiv-2512-02719 — "the relationship between accuracy and behaviour is empirical and is not by necessity"
[^b8]: arxiv-2512-02719 — "a perfect predictor that maps all stimulus to accurate estimates is indistinguishable from a linear model"
[^b9]: arxiv-2512-02719 — "they achieved a decent BCS value"
[^b10]: arxiv-2512-02719 — "to demonstrate Bayesian consistent behavior"
[^b11]: arxiv-2512-02719 — "due to the residual reasoning which we can attenuate but not fully disable"
[^b12]: arxiv-2512-02719 — "magnitudes depend on model"
[^b13]: arxiv-2512-02719 — "reduce measurement precision"
[^b14]: arxiv-2512-02719 — "without altering current measurements"
[^b15]: arxiv-2512-02719 — "we compare fitted weights to the base experiment"
[^b16]: arxiv-2512-02719 — "more accurate models also tend to exhibit"
[^b17]: arxiv-2512-02719 — "effectively strengthening the prior"
