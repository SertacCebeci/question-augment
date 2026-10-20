---
description: "A small generative model trained on the whole optimization history predicts each prompt's current success rate, even for unseen prompts, without extra rollouts, and also guides test-time compute."
aliases: ["generalizable prompt predictive model", "GPS", "global difficulty context", "shared-experience difficulty estimation"]
sources: ["arxiv-2602-01970"]
---
# Shared-history prompt difficulty prediction

In RL post-training with verifiable rewards, the success rate of a prompt (the probability the current model solves it) is its difficulty, and it changes as the model trains. Exact evaluation needs extra rollouts. Earlier predictive methods keep a separate belief per prompt, so a prompt that is rarely sampled gets stale or no updates.[^c1] The work replaces this with one lightweight generative model whose global latent "difficulty context" is inferred from the full history and shared across prompts; a decoder maps (prompt, context) to difficulty.[^c2]

## Mechanism

The context has a history-conditioned prior, a variational posterior and a shared likelihood, trained by maximizing an evidence lower bound. The prior acts as a temporal summarizer, so predictions track the drifting policy.[^c3] Difficulty for any candidate prompt, visited or not, is a Monte Carlo average of the decoder over contexts drawn from the prior.[^c4] This addresses two named failures: independent estimators collapse toward uninformative priors in high-dimensional prompt spaces, and non-stationarity produces lagged adaptation.[^c5]

A theorem states that conditioning on the full history yields strictly lower predictive mean squared error than an optimal predictor using only prompt-specific history.[^c6] This is a statement about optimal predictors, not about the trained network.

## Use in batch selection

Prompts are scored by a utility peaked at success rate 0.5, plus a history-anchored diversity term (within-batch dispersion and distance from the previous step's batch). The authors argue 0.5 maximizes reward variance for binary rewards.[^c7] Removing the diversity term causes a substantial drop; removing only the inter-step term a smaller one.[^c8]

## Measured effects

Against uniform sampling: 1.4x-2.0x fewer training steps to the same level, with gains of 1.6-1.9 points on math and 4.1-5.7 on logic. Against exact-evaluation selection: comparable performance with up to 69% fewer rollouts.[^c9] At test time the same predictor correlates with empirical success on most unseen benchmarks; allocating samples by predicted difficulty gives up to 3.2% relative gain at fixed budget, or up to 36.4% less compute with no loss.[^c10]

## Limits

Binary correctness rewards are the main setting. The predictive correlation diminishes for semantically distant test prompts.[^c11] Test-time allocation was evaluated offline and the authors note more advanced designs may help. All evidence is math and logic RLVR; transfer to open-ended asking or answering is my inference, not tested. Baseline comparisons are by the authors, on their chosen backbones.

## Related

- [[zero-variance-group-waste]] — why prompts at the extremes of difficulty give no gradient.
- [[uncertainty-peaked-challenge-reward]] — another reward peaked at intermediate success.
- [[pre-generation-success-probe]] — a different route to predicting a model's own success before generation.
- [[prompt-composition-against-solve-all-saturation]] — controlling difficulty mix of training prompts.

[^c1]: arxiv-2602-01970 — "prompt-specific modeling isolates"
[^c2]: arxiv-2602-01970 — "we construct a lightweight generative PPM that exploits the entire optimization histories and shares"
[^c3]: arxiv-2602-01970 — "acts as a temporal summarizer of the optimization history"
[^c4]: arxiv-2602-01970 — "This mechanism enables the model to infer the difficulty"
[^c5]: arxiv-2602-01970 — "Accumulated Estimation Error from Delayed Reward Signals"
[^c6]: arxiv-2602-01970 — "conditioning on full optimization history yields a strictly lower predictive mean"
[^c7]: arxiv-2602-01970 — "targeting a 0.5 success rate theoretically maximizes reward variance for stronger learning signals"
[^c8]: arxiv-2602-01970 — "causes a substantial performance drop"
[^c9]: arxiv-2602-01970 — "requiring up to 69% fewer rollouts"
[^c10]: arxiv-2602-01970 — "reduces computation by up to 36.4% with no loss in performance"
[^c11]: arxiv-2602-01970 — "the predictive correlation naturally diminishes for semantically distant"
