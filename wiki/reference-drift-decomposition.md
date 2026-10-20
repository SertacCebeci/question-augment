---
description: "A running average of bounded outcomes splits into a predictable reference-drift term and a martingale innovation term, so stabilization reduces to convergence of the drift."
aliases: ["drift-innovation decomposition", "reference drift"]
sources: ["doi-10-48550-arxiv-2609-04115"]
---
# Reference-drift decomposition

For a bounded outcome sequence, the running average splits into two averages. The first is the reference drift: each term is the conditional mean of the outcome given the history joined with the reference conditioning information, and the average of these means is the predictable part. The second is the innovation: the outcome minus its drift, which is a martingale difference. The paper frames the split as "empirical averages are decomposed into a predictable" drift component plus a martingale innovation component, and notes that the predictable component "is the reference drift" of the [[reference-structure]].[^c1]

The mechanism is a division of labour. The innovation term averages to zero under the governing law with no further regime assumption. The paper proves this by applying "a martingale strong law to the bounded martingale differences".[^c2] This is the same innovation cancellation that gives validity in the large (see [[coherence-frequency-role-separation]]). Everything that depends on the regime therefore sits in the drift term: "The regime content is therefore carried by the first term, which depends on the chosen reference structure."[^c3] The paper's unified stabilization result follows. If the average of the drifts converges almost surely to some random limit, then the empirical average converges almost surely to the same limit. Stabilization is reduced to convergence of the drift.

Two conditions must hold for the argument to apply. The innovations must be martingale differences under the evaluation law P, which needs conditional correctness under P and not merely coherence under an assessment law Q. The paper is explicit that "Internal coherence under an assessment law Q implies it only when the relevant one-step conditional means under Q and P" agree.[^c4] And the drift must converge, which the regime has to supply. The paper lists the sources: "the reference drift, such as exchangeability, stationarity or ergodicity" and the other families in the reference structure.[^c5]

The decomposition also explains a failure. In the paper's reinforcement-learning example the innovations are martingale differences, so the average of forecast errors goes to zero, yet the predictable mean keeps oscillating and the average does not converge. "Both show that conditional-mean correctness does not control convergence of the predictable drift."[^c6] The drift, not the innovation, is where a frequency claim can fail.

## Limits

- The paper says it introduces no new limit theorem: "We do not introduce new limit theorems."[^c7] The decomposition is bookkeeping around standard martingale and stabilization results. Its content lies in the drift assumptions it makes visible.
- The drift is defined relative to the conditioning σ-algebra. Choosing a different reference conditioning changes the drift, and so changes what is claimed to stabilize. The paper notes that stationarity, ergodicity and drift convergence are "properties of the governing law or protocol rather than of" the conditioning alone.[^c8] The choice of conditioning is therefore part of the claim, not a technicality.
- Proposition 5 is a sufficiency result: drift convergence gives stabilization. The note does not claim the converse, and the paper does not state one. That the drift must converge for the average to converge is this note's own reading, not a result quoted from the paper.
- Non-convergence is not presented as typical: "Neither result suggests that nonconvergence is typical."[^c9] The decomposition shows where a frequency claim can break; it does not measure how often it does.

## Related

- [[reference-structure]] — the regime that supplies the drift assumptions: exchangeability, stationarity, a fixed policy–environment pair, or design-based randomization
- [[coherence-frequency-role-separation]] — the separation this decomposition makes operational, with the evaluation-law premise made explicit
- [[calibration]] — a separate frequency claim: the average of innovations gives validity in the large, not calibration over rich checking classes

[^c1]: doi-10-48550-arxiv-2609-04115 — "empirical averages are decomposed into a predictable"
[^c2]: doi-10-48550-arxiv-2609-04115 — "Apply a martingale strong law to the bounded martingale differences"
[^c3]: doi-10-48550-arxiv-2609-04115 — "The regime content is therefore carried by the first term, which depends on the"
[^c4]: doi-10-48550-arxiv-2609-04115 — "Internal coherence under an assessment law Q implies it only when the relevant one-step conditional means under Q and P"
[^c5]: doi-10-48550-arxiv-2609-04115 — "the reference drift, such as exchangeability, stationarity or ergodicity"
[^c6]: doi-10-48550-arxiv-2609-04115 — "Both show that conditional-mean correctness does not control convergence of the predictable drift."
[^c7]: doi-10-48550-arxiv-2609-04115 — "We do not introduce new limit theorems"
[^c8]: doi-10-48550-arxiv-2609-04115 — "properties of the governing law or protocol rather than of"
[^c9]: doi-10-48550-arxiv-2609-04115 — "Neither result suggests that nonconvergence is typical."
