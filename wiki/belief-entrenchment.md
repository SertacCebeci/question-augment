---
description: "Belief entrenchment: a reasoner's belief updates are predictable from its prior belief. The Martingale Score, the OLS slope of update on prior, measures it without ground truth."
aliases: ["Martingale Score", "martingale violation of belief updates", "belief-update predictability", "prior-driven belief drift"]
sources: ["arxiv-2512-02914"]
---
# Belief entrenchment

Belief entrenchment is a systematic tendency to update a belief toward the side it already leans, "a systematic tendency to update beliefs in favor of prior opinions rather than in response to new evidence".[^c1] The source's move is to treat it as a statistical property of the update rather than as a psychological trait. Under Bayesian updating the martingale property holds: the expected posterior, given the prior, "should always equal the expectation of prior".[^c2] Equivalently, the direction of an update should not be predictable from the starting point alone: "belief updates cannot be predicted from solely the current belief".[^c3] A reasoner whose updates can be predicted from where it began is, on this definition, entrenched, and no ground truth is needed to see it.

## Mechanism of the measurement

A chain of thought is treated as a belief-updating process. The opening stance is the prior, and "the very end of model output, after extensive reasoning or engagement with external evidence" is the posterior.[^c4] The stance itself is not read from a token probability or a self-report, because "LLMs are often [[calibration|poorly calibrated]]".[^c5] A separate judge model reads each trace and assigns a belief score in [0, 1].

With the prior and posterior in hand, the paper regresses the update on the prior, "where bprior are the prior probabilities" and the update is posterior minus prior, by ordinary least squares.[^c6] The Martingale Score M is the fitted slope on the prior, and "positive value of the linear coefficient is our practical choice of the Martingale Score".[^c7] A positive M means that the higher the starting belief, the further the reasoning moves it upward; M near zero means the update is not linearly predictable from the prior. The authors describe the score as "the unsupervised, regression-based Martingale Score".[^c27] They chose the slope over an R-squared from a logistic regression on the direction of the update, since the logistic version "neglects the magnitude of belief updates and produces random-seeming results".[^c8]

Why zero is the right null: "the prior bprior is statistically exogenous to the belief update" under the martingale property, so the expected coefficient is zero and the estimate converges to zero as samples grow.[^c9] A nonzero slope, with a significant t-test, is what the paper calls a violation. Its operational definition follows: "We thus operationalize belief entrenchment as the degree to which a model violates the Martingale property."[^c10]

## What was measured

Across forecasting questions (Metaculus, Polymarket), value-laden questions from r/ChangeMyView, and ICLR submissions from OpenReview, the paper finds positive scores in most setups, "including almost all of those with CoT (51 out of 54)".[^c11] The domains are ordered by propensity: "in increasing order of propensity for belief entrenchment" runs Forecasting, then r/ChangeMyView, then OpenReview.[^c12] Under chain of thought the r/ChangeMyView score is roughly three times the forecasting score (M CMV-CoT = 0.103 against 0.037 in forecasting).[^c13]

In forecasting, where outcomes resolve, the score tracks accuracy. Each point in the paper's scatter is one setup, one model, one prompt and one reasoning mode, over more than 100 questions.[^c14] The absolute score is "positively correlated across all setups, suggesting belief entrenchment harms accuracy on binary problems".[^c15] The scale is small: at a score of 0.0 the Brier score is below 0.25, the random-guess level, while at a mild score of 0.04 the paper reports that "the forecasting performance is worse than random guess".[^c16]

The effect is not only an artefact of the prompt that deliberately pushes the prior. Under no system prompt and under a critical-thinking prompt, "belief entrenchment also happens, although to a lesser extent".[^c17] Debate lowers the score, "that the use of debate mitigates belief entrenchment", and DeepSeek R1 "shows exceptional resistance to belief entrenchment".[^c18][^c19]

## Limits

- **A zero slope is not rationality.** The paper says only that "the Martingale property is a prerequisite for Bayesian reasoning".[^c20] The converse is not shown. My inference: a score of zero shows that the update is not linearly predictable from the prior, not that it is correct. An update can be unrelated to the prior and still wrong.
- **The Bayesian property is transferred to self-generated evidence.** The martingale property is stated for evidence arriving from outside the reasoner. A chain of thought produces its own evidence, so the prior partly chooses which considerations are raised. My inference: a reasoner that retrieves confirming considerations would show a positive slope even if it updates correctly on what it retrieves. The score cannot separate selection from updating. The paper concedes its scope: "In this study we only focused on the former", meaning irrational engagement with the internal reasoning process rather than with external evidence.[^c21]
- **Ground truth exists only in forecasting.** For OpenReview the paper states that "this study does not demonstrate the correlation between Martingale Score (belief entrenchment) and Brier Score (accuracy)", attributing this to noisy community-voted decisions.[^c22] The word "causality" in the discussion is stronger than the design: the accuracy evidence is a correlation across setups, not an intervention on the score.[^c23] My reading of the paper's regression figure is that the share of Brier variance explained by the absolute score is small, a few percent in its labels, so the score is one factor among several.[^c24]
- **The belief is a judge's reading.** The default judge is GPT-4o, "we set up GPT-4o as the default judge for all comparisons", because other judges were run on far fewer problems.[^c25] Judge error enters the slope directly, so the score is only as steady as the judge that reads the stances.
- **Reinforced reasoning is untested.** "we have not systematically studied belief entrenchment in reinforced reasoning", so the score's behaviour on trained reasoners is open.[^c26]

## Related

- [[sycophantic-capitulation]] — the same kind of defect, a commitment that moves for a non-evidential reason; there the pull comes from the asker's pushback, here from the model's own starting stance, and no pushback is applied.
- [[calibration]] — why the paper reads expressed rather than internal confidence. The score does not require the belief to be calibrated, only its updates to be unpredictable from the prior.
- [[confidence-weighted-debate-submartingale]] — another martingale in LLM reasoning: there the expected belief of a debate is flat under homogeneous agents. Here the object is the regression of update on prior, a different test.
- [[conformal-test-martingale]] — martingale vocabulary in a different field; only the term is shared.

[^c1]: arxiv-2512-02914 — "a systematic tendency to update beliefs in favor of prior opinions rather than in response to new evidence"
[^c2]: arxiv-2512-02914 — "should always equal the expectation of prior"
[^c3]: arxiv-2512-02914 — "belief updates cannot be predicted from solely the current belief"
[^c4]: arxiv-2512-02914 — "the very end of model output, after extensive reasoning or engagement with external evidence"
[^c5]: arxiv-2512-02914 — "LLMs are often poorly calibrated"
[^c6]: arxiv-2512-02914 — "where bprior are the prior probabilities"
[^c7]: arxiv-2512-02914 — "positive value of the linear coefficient is our practical choice of the Martingale Score"
[^c8]: arxiv-2512-02914 — "which neglects the magnitude of belief updates and produces random-seeming results"
[^c9]: arxiv-2512-02914 — "The Martingale property (2) implies that the prior bprior is statistically exogenous to the belief update"
[^c10]: arxiv-2512-02914 — "We thus operationalize belief entrenchment as the degree to which a model violates the Martingale property."
[^c11]: arxiv-2512-02914 — "including almost all of those with CoT (51 out of 54)"
[^c12]: arxiv-2512-02914 — "in increasing order of propensity for belief entrenchment"
[^c13]: arxiv-2512-02914 — "M CMV-CoT = 0.103"
[^c14]: arxiv-2512-02914 — "Each data point represents the Brier Score and Martingale Score of one setup"
[^c15]: arxiv-2512-02914 — "positively correlated across all setups, suggesting belief entrenchment harms accuracy on binary problems"
[^c16]: arxiv-2512-02914 — "the forecasting performance is worse than random guess"
[^c17]: arxiv-2512-02914 — "belief entrenchment also happens, although to a lesser extent"
[^c18]: arxiv-2512-02914 — "that the use of debate mitigates belief entrenchment"
[^c19]: arxiv-2512-02914 — "DeepSeek R1 shows exceptional resistance to belief entrenchment"
[^c20]: arxiv-2512-02914 — "As the Martingale property is a prerequisite for Bayesian reasoning"
[^c21]: arxiv-2512-02914 — "In this study we only focused on the former"
[^c22]: arxiv-2512-02914 — "this study does not demonstrate the correlation between Martingale Score (belief entrenchment) and Brier Score (accuracy)"
[^c23]: arxiv-2512-02914 — "we demonstrated the causality of belief entrenchment and accuracy"
[^c24]: arxiv-2512-02914 — "Increased absolute value of the Martingale Score is associated with worse prediction"
[^c25]: arxiv-2512-02914 — "we set up GPT-4o as the default judge for all comparisons"
[^c26]: arxiv-2512-02914 — "we have not systematically studied belief entrenchment"
[^c27]: arxiv-2512-02914 — "the unsupervised, regression-based Martingale Score"
