---
description: "Under a Beta-Bernoulli model of success rate, expected uncertainty reduction splits into a difficulty term and an evidence term that decays with n, so difficulty-only selection stalls."
aliases: ["weighted mutual information data selection", "INSIGHT", "difficulty-only selection limitation", "epistemic exploration in RLVR data selection"]
sources: ["arxiv-2603-01907", "doi-10-48550-arxiv-2606-09052"]
---
# Difficulty-evidence decomposition of data selection

Which prompt to train on next is a question about where an answer would teach the most. Common RLVR heuristics pick prompts whose sampled success rate is nearest 0.5, treating difficulty as informativeness. This work argues that this tracks only one of two uncertainties and shows the other analytically.

## Mechanism

Each prompt is an arm with a latent success rate. Its rewards are Bernoulli, so a Beta prior updates in closed form: "ϕtτ |Ht ∼ Beta(ατt + Sτt , βτt + K − Sτt )".[^c1] The target is the expected variance reduction after one binary reward, which simplifies to ϕ̄(1−ϕ̄)/(n+1)², where ϕ̄ is the prior mean and n = α+β is the accumulated evidence count (equation 8 in the text; my reading of the garbled extraction). The numerator is the difficulty factor, peaking at ϕ̄ = 0.5. The denominator is the evidence factor, shrinking quadratically as rollouts accumulate. The same quantity is stated as the objective: "∆V (τ ) = Varprior (ϕτ ) − Er [Varposterior (ϕτ |r)]".[^c2]

The paper's reading is that difficulty heuristics address aleatoric uncertainty (the intrinsic randomness of a prompt's outcomes) and ignore epistemic uncertainty about the success rate itself: "difficulty-only heuristics primarily target aleatoric uncertainty (i.e., the intrinsic stochasticity of reward outcomes for a given datapoint)".[^c3] A prompt can stay hard and mid-difficulty yet teach little once its success rate is well estimated. The mutual information I(R; Φ) between reward and latent rate captures the epistemic part, and a proposition shows it falls as O(1/n) with evidence.[^c4]

The proposed score multiplies two parts. The mutual information term is epistemic exploration. A weight w(ϕ̄) = ϕ̄(1−ϕ̄)·exp(−η(ϕ̄−µ)²), computed on the posterior mean rather than a sampled rate, is aleatoric exploitation. It contains a variance filter and a smooth bias toward a target difficulty µ. The top-M prompts by this score are trained on, and observed rewards update the posterior, so selection moves as evidence accumulates. Temporal discounting toward the prior keeps counts from freezing as the policy changes.[^c5]

Reported outcomes (Qwen3 and R1-Distill-Qwen models): gains over random selection on planning and mathematics benchmarks, and speedups of roughly 2.2x, 1.5x and 1.6x in training steps on three model sizes.[^c6]

A second line of argument, from the INFUSER paper on co-evolving generator and solver, names the same weakness from the side of the generator's reward. The authors fault a difficulty reward as "a coarse surrogate for utility": a question can score as hard because "a question may register as difficult because it is ambiguously phrased, misaligned with" its source, or because it carries a wrong reference answer, and training on it then carries no guarantee of helping the solver.[^c7] Their replacement is a score for whether training on the question would raise the solver's expected reward on a development set, computed from gradients rather than from success rate; see optimizer-aware-influence-score.[^c8] The paper's point is about utility, not about epistemic versus aleatoric uncertainty, so it does not test the decomposition above.

## Limits

The evidence is on RLVR training with binary rewards and K rollouts per prompt; the analysis fixes K = 1 for illustration. The Beta-Bernoulli model assumes the success rate is stationary apart from the discount heuristic, which is approximate under a moving policy. The gains are benchmark averages (about +1.4 on planning and math), so the effect size is modest. Whether the decomposition applies to choosing questions for a human or retrieval source is my inference, not tested. The equation details come from a garbled text extraction.

## Related

- [[value-of-information]] — expected uncertainty reduction as the selection criterion
- [[gradient-norm-epistemic-uncertainty]] — another separation of epistemic from irreducible uncertainty
- [[locality-weighted-information-gain-acquisition]] — an information gain score reweighted by a second factor
- [[reinforcement-prompt-selection]] — RL choice among prompt options, with a different reward
- optimizer-aware-influence-score — replaces the difficulty reward with a dev-set gradient-alignment score

[^c1]: arxiv-2603-01907 — "ϕtτ |Ht ∼ Beta(ατt + Sτt , βτt + K − Sτt )"
[^c2]: arxiv-2603-01907 — "∆V (τ ) = Varprior (ϕτ ) − Er [Varposterior (ϕτ |r)]"
[^c3]: arxiv-2603-01907 — "difficulty-only heuristics primarily target aleatoric uncertainty (i.e., the intrinsic stochasticity of reward outcomes for a given datapoint)"
[^c4]: arxiv-2603-01907 — "I(R; Φτ ) ≈ O("
[^c5]: arxiv-2603-01907 — "The temporal discounting techniques"
[^c6]: arxiv-2603-01907 — "with fewer training steps, yielding up to ∼2.2x, ∼1.5x,"
[^c7]: doi-10-48550-arxiv-2606-09052 — "a question may register as difficult because it is ambiguously phrased, misaligned with"
[^c8]: doi-10-48550-arxiv-2606-09052 — "optimizer-aware influence score, a per-question scalar that quantifies whether training the solver on the"
