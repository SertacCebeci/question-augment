---
description: "A discriminative posterior reweighted by the deployment-to-training prior ratio, then renormalized, gives the deployment posterior once the training prior is known."
aliases: ["prior-ratio reweighting", "prior shift correction"]
sources: ["arxiv-2601-01522"]
---
# Prior correction of discriminative posteriors

A discriminative model returns a posterior $p_M(s\mid x)$ in which its training prior $p_{\text{train}}(s)$ is already multiplied in. In odds form Bayes' rule makes a change of prior a simple factor: posterior odds equal prior odds times the likelihood ratio ([[likelihood-ratio]]). Replacing the training prior with a deployment prior $p_{\text{deploy}}(s)$ therefore needs only the ratio $p_{\text{deploy}}(s)/p_{\text{train}}(s)$:

$$p_{\text{deploy}}(s\mid x) \propto p_M(s\mid x)\,\frac{p_{\text{deploy}}(s)}{p_{\text{train}}(s)},$$

normalized by summing over the states. The normalizing sum runs over the state space, which the posterior already supplies, so the constant is fixed by the requirement that the result sum to one; it is not chosen.

The work argues the opposite. It concedes that even with the training prior known "we can only extract likelihood ratios, not absolute likelihoods",[^c1] and concludes that "Ratios are insufficient for computing posteriors under a new prior"[^c2], because the step would require "arbitrarily choose a normalization constant".[^c3] The equation above applies the ratio to the posterior itself, so that step does not arise. The work's general conclusion, that "prior mismatch is not a calibration problem that can be solved with post-hoc adjustments",[^c4] is therefore too strong. My reading, not the work's: it holds for the case where $p_{\text{train}}(s)$ is unknown, and that is the case that matters for LLMs.

What is actually out of reach is $p_{\text{train}}(s)$ itself. The work notes that it would have to be reported by the model, "which standard LLMs do not do".[^c5] Without it the factor above cannot be formed, and the prior hidden inside a posterior stays hidden. The work's remedy avoids reweighting altogether: "Override LLM training priors with deployment-specific base rates".[^c6] It elicits likelihoods and attaches an explicit prior $\pi$ in its own Bayes step; its example prior is set "if institutional data shows that historically".[^c7]

So two routes separate. One reweights a posterior whose training prior is known. The other elicits likelihoods and attaches the prior explicitly, which needs the likelihoods to be usable as likelihoods ([[typicality-likelihood-elicitation]]).

## Limits

- The reweighting is exact only if $p_M(s\mid x)$ is a Bayes posterior under $p_{\text{train}}$ over the same states. Nothing guarantees that a model's stated probabilities are one; any [[calibration|miscalibration]] passes straight into the deployment posterior (my inference).
- $p_{\text{train}}$ is not observable from the outputs. Estimating it from behaviour is a separate problem that neither the work nor this note solves.
- In the slices read, the work does not run this reweighting on any LLM output. Its impossibility claim is a theorem about the discriminative form, and it is not tested against the reweighting.
- A correct formula does not make the corrected posterior correct. The deployment prior is itself an estimate: the work's own example prior is a set of illustrative base rates with no uncertainty attached (my reading).

## Related

- [[likelihood-ratio]] — the odds identity this correction is an instance of
- [[bayesian-estimation]] — the normalized Bayes update that the reweighted posterior is
- [[calibration]] — the reweighted posterior inherits whatever calibration the model's posterior had
- [[typicality-likelihood-elicitation]] — the work's alternative: elicit per-state likelihoods and apply the prior explicitly

[^c1]: arxiv-2601-01522 — "we can only extract likelihood ratios, not absolute likelihoods"
[^c2]: arxiv-2601-01522 — "Ratios are insufficient for computing posteriors under a new prior"
[^c3]: arxiv-2601-01522 — "arbitrarily choose a normalization constant"
[^c4]: arxiv-2601-01522 — "prior mismatch is not a calibration problem that can be solved with post-hoc adjustments"
[^c5]: arxiv-2601-01522 — "which standard LLMs do not do"
[^c6]: arxiv-2601-01522 — "Override LLM training priors with deployment-specific base rates"
[^c7]: arxiv-2601-01522 — "if institutional data shows that historically"
