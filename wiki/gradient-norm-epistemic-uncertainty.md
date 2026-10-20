---
description: "Under a first-order Taylor and isotropic-covariance assumption, epistemic uncertainty is the squared gradient norm of the prediction; it predicts errors on ambiguous questions, not on recall."
aliases: ["isotropic delta method", "squared gradient norm uncertainty", "gradient-based epistemic uncertainty"]
sources: ["arxiv-2603-29466"]
---
# Gradient-norm epistemic uncertainty

The delta method approximates the prediction near the trained parameters by a first-order Taylor expansion, so the posterior variance of a class probability becomes g^T Cov[θ] g, with g the gradient of the prediction with respect to the parameters.[^c1] Assuming isotropic covariance σ²I only rescales every estimate, so Cov[θ]=I is taken without loss of generality, leaving the squared gradient norm ||g||² as the epistemic estimate.[^c2] The aleatoric part is the Bernoulli variance p(1−p) of the point prediction, so both terms come from one forward-backward pass of an unmodified pretrained model.[^c3] It uses the label-wise variance decomposition (law of total variance), not the entropy and mutual-information one, which the authors cite as violating several axioms.[^c4]

## Why isotropy rather than a proxy covariance

For an LLM the training data is unavailable, so any Laplace or Fisher covariance must be built from a proxy corpus. The authors argue that such estimates carry structured, data-dependent error. The error is weighted by g_i², so it concentrates on the parameters the prediction relies on.[^c5] On a symmetric XOR problem, each half-data proxy inflates uncertainty where its data is absent and suppresses it where its data lies. The identity gives a symmetric estimate.[^c6] On DistilBERT fine-tuned on 20 Newsgroups, the identity kept the full-Hessian ranking (Spearman 0.979) better than single-domain proxies (0.920–0.962). Every single-domain proxy had its lowest value on its own domain.[^c7] A second argument is spectral: the Hessian has few large eigenvalues and a bulk near zero, so the damped inverse tends toward a multiple of the identity in large models.[^c8]

## What it predicts in question answering

Four LLMs were scored by AUROC for predicting answer correctness. On TriviaQA (factual recall) P(True) led at 0.69 and the epistemic estimate was 0.52, near chance. On TruthfulQA (misconceptions, ambiguous answer space) the aleatoric plus epistemic estimate reached 0.63, ahead of P(True) at 0.55.[^c9] The epistemic estimate correlates only weakly with P(True) (Spearman about −0.2), so the two carry largely different signal.[^c10] The authors read this as parameter-level uncertainty being most useful when the task involves conflict between plausible answers, and note that epistemic uncertainty may be less useful for hallucination detection than assumed.[^c11] The extra lift from the epistemic term over aleatoric alone on TruthfulQA was 0.60 to 0.63 (p = 0.018).[^c12] The cost is one backward pass after generation, a 46–107x speedup over the sampling baselines.[^c13]

For asking and answering: a model's own confidence signals and its parameter sensitivity answer different questions. Which one to trust depends on whether the question is a lookup or a contested one. This is this wiki's reading of the result, not a claim of the paper.

## Limits

- The scale is that of squared gradient norms. The unknown σ² cancels within one model's rankings but not in the ratio of aleatoric to epistemic estimates, or across models.[^c14]
- Validation against MCMC is on synthetic problems (Spearman 0.44–0.99), weakest at the interpolation threshold. The improvement with scale is a trend, not shown at LLM scale.[^c15]
- The isotropy argument is partly by analogy and prior literature. The comparison against proxy covariances is on small models and a diagonal-Laplace-style analysis, not on LLMs.
- The QA result is on two benchmarks and four models. Which uncertainty type helps varies by model (Llama favors aleatoric, OLMo and Phi-4 favor epistemic), and the training-data explanation is speculation.
- The decomposition assumes the MAP prediction equals the posterior predictive mean, which the authors say is incorrect in practice.[^c16]

## Related

- [[uncertainty-decomposition]] — the aleatoric/epistemic split here is made measurable by a variance formula, which the agent-level note says is missing at the prompt level
- [[calibration]] — the estimate is a ranking signal, not a calibrated probability
- [[pseudo-ensemble]] — another route to epistemic uncertainty without training multiple models
- [[heterogeneous-lora-ensemble-uncertainty]] — an ensemble alternative that needs extra models
- [[abstention]] — uncertainty scores of this kind are what an abstention rule would threshold

[^c1]: arxiv-2603-29466 — "Varθ [p(yc | x, θ)] ≈ g ⊤ Cov[θ] g"
[^c2]: arxiv-2603-29466 — "We are left with ∥g∥2 , the squared gradient norm, as our estimate of epistemic uncertainty."
[^c3]: arxiv-2603-29466 — "epistemic uncertainty as the squared gradient norm and aleatoric uncertainty as the Bernoulli variance of the point prediction, from a single forward-backward pass through an unmodified pretrained model"
[^c4]: arxiv-2603-29466 — "Wimmer et al. (2023) show that mutual information violates several"
[^c5]: arxiv-2603-29466 — "Since gi2 upweights the parameters the model"
[^c6]: arxiv-2603-29466 — "each proxy inflates uncertainty in the half of input space absent from its data and suppresses it where its data is concentrated"
[^c7]: arxiv-2603-29466 — "the identity preserves the uncertainty"
[^c8]: arxiv-2603-29466 — "a small number of large eigenvalues with a vast bulk near zero"
[^c9]: arxiv-2603-29466 — "the combined estimate achieves 0.63, the highest"
[^c10]: arxiv-2603-29466 — "The epistemic estimate and P(True) are only"
[^c11]: arxiv-2603-29466 — "epistemic uncertainty may not be as useful"
[^c12]: arxiv-2603-29466 — "the epistemic component provides a significant lift when combined (0.60 → 0.63, paired bootstrap"
[^c13]: arxiv-2603-29466 — "The gradient norm"
[^c14]: arxiv-2603-29466 — "so their ratio is not meaningful in absolute terms"
[^c15]: arxiv-2603-29466 — "The dip falling at the interpolation threshold suggests the"
[^c16]: arxiv-2603-29466 — "This assumption is incorrect in practice"
