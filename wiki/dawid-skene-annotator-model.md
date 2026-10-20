---
description: "Dawid and Skene's annotator model gives each labeller a reliability, or a full confusion matrix, and infers hidden labels and reliabilities jointly by EM, with no ground truth."
aliases: ["Dawid-Skene model", "one-coin annotator model", "confusion-matrix annotator model", "one-coin EM", "annotator reliability model"]
sources: ["doi-10-48550-arxiv-2610-02005", "arxiv-2512-02405"]
---
# Dawid-Skene annotator model

Several labellers mark the same items, and their labels disagree. The question is what the true labels are, and how reliable each labeller is. The Dawid-Skene model answers both together. The truth is a latent variable, and each labeller's marks depend on that truth through its own parameters. Estimation alternates between the two, by expectation-maximization (EM), so no gold labels are needed.[^d1]

The simplest version is the one-coin model. Each annotator has one reliability: it marks the true class with that probability and any other class with the remaining mass spread evenly. The paper describes the one-coin model as the version that "fits one reliability per annotator by expectation" maximization, and it is the uniform-error special case of the general model.[^d1][^d2] The general version gives each annotator a full confusion matrix, one row per true class. Raykar and colleagues (2010) learn per-class matrices in this way.[^d3]

The paper under review does not use the model as a label-cleaning tool. It treats a council's typed moves as the observations. Each seat's endorsements are the annotator's marks, and each seat has its own reliability. The paper's own summary of the move is "deliberation as a reliability estimation problem," the framing the paper takes from this annotator model.[^d4] The transfer keeps the structure: a latent answer, a per-source reliability, and an evidence factor per source combined by Bayes' rule. What the paper changes is the carrier, not the model. Its moves are protocol-governed speech acts, not labels on items, and the reliabilities are fitted from a labelled calibration window.

Two things about the classical model show up again in the paper. First, the unsupervised estimator has a label-switching problem: with no labels, the fit can settle on the wrong name for each class. The paper says a supervised prior is what removes this: "ambiguity is exactly what a supervised prior resolves."[^d5] Second, the one-coin form over-counts when a source's marks are correlated, which the paper saw in the K>2 case and repaired with a fitted temperature rather than a richer matrix.[^d6]

The model has also been moved into multi-agent debate among LLMs. The WISE framework treats each agent's answer as one worker's label on the same problem. Its authors take the view that "agents can be viewed as workers prone to systematic errors," and fit a modified Dawid-Skene on the debate output, "assuming conditional independence of agents’ responses."[^d9][^d10] The reweighting is meant to "down-weight agents behaving randomly" while raising the influence of agents whose answers agree with the majority.[^d11] The reported result is a gain of "accuracy by 2–7% over the state-of-the-art MAD setups and aggregation methods."[^d12] That figure covers the debate structure and the aggregation together. The reweighting alone is not isolated in the parts read here (my reading). The debate roles that feed it are described in [[solver-reflector-role-split]].

## Limits

- The model's independence assumption carries the whole inference. Marks from different annotators are treated as conditionally independent given the truth. A seat's repeated moves on one task are the clearest case the paper gives, and models that share training data would plausibly break it too (my inference, not tested here). Where the marks are correlated, the posterior becomes over-confident. The paper's one-coin arm is overconfident for K>2 for exactly this reason.[^d6]
- Unsupervised, the estimator is weak where it matters most in the paper. Its unsupervised arm, DS-EM, sits off the scale of the calibration figure, "DS-EM off-scale (0.34)," and does not recover the calibration of the supervised variants.[^d7]
- The model was built for independent noise. The paper stresses that its test is different: it is "stress-tested against a live adversarial coalition rather than independent" noise.[^d8] A confusion matrix can invert a systematic adversary only if the labels are there to fit it. The classical model does not say what a coordinated error looks like.
- The paper's evidence is one council of three to four seats on three binary datasets and two multi-class sets. The transfer from annotators to deliberating models is the paper's argument, not a measured identity; no claim that the model is "correct" for LLM councils generally is established.

## Related

- [[signed-reliability-committee-vote]] — the weighted rule that the one-coin reliability feeds, including the negative weight for a seat below chance.
- [[rater-effects-latent-score-model]] — latent strictness and consistency for raters on score scales, a different parametrisation of the same question of trusting raters.
- [[agreement-based-annotator-clustering]] — groups annotators by pairwise agreement instead of fitting a confusion model per annotator.
- [[cross-rater-reliability]] — a chance-corrected agreement statistic for the same labellers, without a latent truth.
- [[annotator-disagreement-calibration]] — calibrating a detector to the spread of annotators' labels, with no ground truth.
- [[solver-reflector-role-split]] — the debate setting in which the same model is applied to LLM solvers and reflectors, with the reflectors' weights added to the aggregation.

[^d1]: doi-10-48550-arxiv-2610-02005 — "the one-coin model of Dawid and Skene (1979) fits one reliability per annotator by expectation"
[^d2]: doi-10-48550-arxiv-2610-02005 — "the onecoin of Dawid and Skene (1979) is the uniform-error submodel"
[^d3]: doi-10-48550-arxiv-2610-02005 — "Raykar et al. (2010) learn per-class confusion matrices"
[^d4]: doi-10-48550-arxiv-2610-02005 — "deliberation as a reliability estimation problem"
[^d5]: doi-10-48550-arxiv-2610-02005 — "ambiguity is exactly what a supervised prior resolves"
[^d6]: doi-10-48550-arxiv-2610-02005 — "over-counts the evidence"
[^d7]: doi-10-48550-arxiv-2610-02005 — "DS-EM off-scale (0.34)"
[^d8]: doi-10-48550-arxiv-2610-02005 — "stress-tested against a live adversarial coalition rather than independent"
[^d9]: arxiv-2512-02405 — "agents can be viewed as workers prone to systematic errors"
[^d10]: arxiv-2512-02405 — "assuming conditional independence of agents’ responses"
[^d11]: arxiv-2512-02405 — "This down-weights the agents behaving randomly"
[^d12]: arxiv-2512-02405 — "accuracy by 2–7% over the state-of-the-art MAD setups and aggregation methods"
