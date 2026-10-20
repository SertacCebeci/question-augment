---
description: "Asking an LLM how typical an observation is under each hypothesized state, not which state it is in, yields per-state scores usable as likelihoods, though uncalibrated."
aliases: ["contrastive likelihood prompt", "state-conditioned typicality elicitation", "generative likelihood elicitation"]
sources: ["arxiv-2601-01522"]
---
# Typicality elicitation of likelihoods

A language model asked for a posterior answers "given this observation, what is the state?", which targets $p(s\mid x)$. The elicitation described here inverts the direction: "Given this state, how typical is this observation?"[^c1] That targets $p(x\mid s)$, the quantity Bayes' rule needs ([[likelihood-ratio]]). The mechanism has three parts in the work.

First, state conditioning. The prompt opens by assuming a state and describing it, which the work calls "forcing forward simulation" rather than backward inference: given a quality level, what features of the input would one expect?

Second, typicality framing. The work prefers asking about typicality or representativeness to asking about probability, arguing that "typicality judgments are more natural for humans" and, by extension, for models trained on human text.[^c2] This is a justification the work offers, not a measured effect.

Third, per-state independent queries. Each state is asked separately, which "avoids the implicit normalization and competition between" states that a single classification prompt induces.[^c3] The model returns a raw score on a 0 to 10 rubric, which the work divides by ten to get a number in [0, 1]. Across five models the work takes "the sample median" for each state.[^c4]

The headline result comes from the synthetic resume experiment: the framework "reduces total costs by $294,000 (34% improvement) compared to the best single-LLM"[^c5] baseline. That figure belongs to the whole pipeline, which also includes median aggregation, Bayesian updating, cost-based action and value-of-information. The part due to elicitation alone is not separated in the sections read.

Only ratios among states matter, because Bayesian inference "requires likelihoods only up to a proportionality constant".[^c6] The per-state scores therefore need only be comparable across states on one rubric, not sum to one. That removes a normalization step, but it also means the trusted quantity is the ratio between two states' scores.

## Limits

- The scores are [[calibration|uncalibrated]]. The work says so itself: "Raw LLM scores are not proper probabilities."[^c7] Its normalization is a heuristic, not something derived from probability theory.
- The scale is coarse and the output is context-dependent: "Likelihood estimates may shift based on prompt framing, temperature".[^c8] Two inputs that differ slightly can receive the same score.
- Typicality is not probability. A judgment of how representative a text looks may track canonical appearance; [[prototypicality-bias-in-metrics]] reports an evaluator that rewards canonical-looking answers. Whether the same bias shapes resume likelihoods is my inference, not tested here.
- The test data are synthetic: "1,000 synthetic resumes with known ground truth".[^c9] Synthetic text may be more prototypical than real applications, which would flatter typicality judgments (my inference).
- The work's own verdict is modest: "our approximate likelihoods are sufficient for substantial gains".[^c10] That is an end-to-end cost result, not evidence that the scores are calibrated. Its proposed fixes (post-hoc calibration, comparative judgments) are not tested in the text read.

## Related

- [[prior-correction-of-discriminative-posteriors]] — the other route: reweight a posterior when its training prior is known
- [[balar]] — elicits an LLM likelihood table per dimension in dialogue, not a per-state typicality score
- [[prototypicality-bias-in-metrics]] — typicality judgments can reward canonical appearance
- [[calibration]] — the property the elicited scores lack

[^c1]: arxiv-2601-01522 — "Given this state, how typical is this observation?"
[^c2]: arxiv-2601-01522 — "typicality judgments are more natural for humans"
[^c3]: arxiv-2601-01522 — "This avoids the implicit normalization and competition between"
[^c4]: arxiv-2601-01522 — "aggregate using the sample median"
[^c5]: arxiv-2601-01522 — "reduces total costs by $294,000 (34% improvement) compared to the best single-LLM"
[^c6]: arxiv-2601-01522 — "Since Bayesian inference requires likelihoods only up to a proportionality constant"
[^c7]: arxiv-2601-01522 — "Raw LLM scores are not proper probabilities"
[^c8]: arxiv-2601-01522 — "Likelihood estimates may shift based on prompt framing, temperature"
[^c9]: arxiv-2601-01522 — "1,000 synthetic resumes with known ground truth"
[^c10]: arxiv-2601-01522 — "our approximate likelihoods are sufficient for substantial gains"
