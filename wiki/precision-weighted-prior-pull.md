---
description: "A noisy magnitude estimate is pulled toward the prior mean by a weight set by measurement and prior precision; LLMs show this regression, and a biased range in the prompt moves their answers."
aliases: ["regression to the mean", "static Bayesian observer", "central tendency bias", "prior-weighted estimate"]
sources: ["arxiv-2512-02719"]
---
# Precision-weighted prior pull

When an estimate rests on a noisy measurement and on an expectation held before the measurement, the estimate is a weighted average of the two. The static Bayesian observer in the paper states it this way: the LLM's estimate "is a weighted average of the input stimulus" and a fixed prior belief, and the two weights are set by "the measurement and prior precisions respectively".[^p1] Precision is the inverse of variance. A precise measurement holds the estimate near itself; a precise prior holds it near the prior. The weight on the prior therefore rises when the measurement is made noisier or the prior is made more confident, and the estimate leans toward the centre of the range the estimator expects.[^p12] The paper's name for the visible signature is "regression to the mean".

The signature appears in the data. In the paper's Figure 1, "there is a regression to the mean effect, where responses are biased towards the centre of the stimulus range" holds for human psychophysics data and for Llama-4 Maverick's line-length ratio responses.[^p2] The authors read the human case as the same mechanism: people "automatically combine noisy measurements with prior expectations, producing characteristic behavioural patterns."[^p3] The human curve in that figure is adapted from another study (the paper cites "from Thurley, 2016"), so the match is a visual comparison, not a fitted one.

The prior can also be supplied in the prompt. The paper's stimuli come from a range-uniform prior per session, and "this choice enables a clean separation between prior and likelihood."[^p4] When a numerical range for prior observations is written into the prompt, "we find that LLMs behavior is strongly affected."[^p5] A deliberately biased range is the clearest case: "numerical range is given, as shown in the left panel of Figure 6, error increases".[^p6] The authors' reading is that the models "gravitate" toward the range: "consistent with the fact that LLMs gravitate" their "predictions towards prior information provided in-context."[^p7][^p8]

What this means for asking, as my inference and not a claim the paper makes about questions: the range an asker names becomes the centre an answerer is pulled toward. If that range is wrong, the answer is wrong in the direction of the range. The paper tests this with numeric prompts on four magnitude tasks, not with questions in general.

## Limits

- The pull is hard to see in the most accurate models. "When a model has very high accuracy, response will show little evidence of regression" in identity-mapping tasks, and "regression effect alone is insufficient".[^p9][^p10] The regression signature is therefore not a diagnostic for the strongest models; the paper turns to other probes for them.
- The static observer is a fit to black-box responses. The paper says it does "not rely on individual goodness-of-fit in static conditions" and uses the fitted weights as probes, "to demonstrate Bayesian consistent behavior" only through how they shift across conditions.[^p11] A good fit to the pull is a description, not evidence of a Bayesian computation.
- The steering result is one set of prompts on a set of models. The phrase "gravitate" is the authors' reading of the error pattern; no experiment isolates the mechanism inside the model.
- Prior precision is never measured directly. It is inferred from the fitted weight on the prior, so the pull is only as good as the model fitted to it.
- The result covers numeric magnitudes (length, location, distance, duration). Whether the same pull holds for categorical answers or for free-text answers is not tested here.

## Related

- [[bayesian-estimation]] — the posterior mean under squared loss; the static observer is the Gaussian, fixed-prior case of that estimate (my reading)
- [[anchoring-strength]] — when in-context cues override a pretrained prior; the same pull for scalar cues in place of a numeric estimate (my reading)
- [[reliability-weighted-cue-combination]] — the same precision weighting when the second term is another cue, not a prior
- [[bayes-consistency-under-ablation]] — the probe that tracks how the prior weight moves under perturbation

[^p1]: arxiv-2512-02719 — "is a weighted average of the input stimulus"
[^p2]: arxiv-2512-02719 — "where responses are biased towards the centre of the stimulus range"
[^p3]: arxiv-2512-02719 — "automatically combine noisy measurements with prior expectations"
[^p4]: arxiv-2512-02719 — "This choice enables a clean separation between prior and likelihood"
[^p5]: arxiv-2512-02719 — "we find that LLMs behavior is strongly affected"
[^p6]: arxiv-2512-02719 — "numerical range is given, as shown in the left panel of Figure 6, error increases"
[^p7]: arxiv-2512-02719 — "consistent with the fact that LLMs gravitate"
[^p8]: arxiv-2512-02719 — "their predictions towards prior information provided in-context"
[^p9]: arxiv-2512-02719 — "when a model has very high accuracy, response will show little evidence of regression"
[^p10]: arxiv-2512-02719 — "regression effect alone is insufficient"
[^p11]: arxiv-2512-02719 — "we do not rely on individual goodness-of-fit in static conditions"
[^p12]: arxiv-2512-02719 — "raises wprior"
