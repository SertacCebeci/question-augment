---
description: "A reference structure fixes what counts as repetition and what may drift; a frequency reading of a probability is only as strong as the reference structure it is declared under."
aliases: ["declared repetition regime", "repetition regime", "repetition mechanism"]
sources: ["doi-10-48550-arxiv-2609-04115"]
---
# Reference structure

A probability reads as a long-run frequency only relative to some repetition. The reference structure is the regime-level statement of that repetition: what is treated as fixed when the process is replicated, what the forecaster or policy may adapt to, and what is allowed to drift. The paper defines it as "a regime-level specification comprising" two parts: what counts as repetition and what is held fixed, including any reference conditioning information; and the invariance, ergodicity, randomization or controlled-drift assumptions that justify the stated target.[^c1] It is not one object. "This encompasses exact symmetries (e.g., permutation invariance)" and also controlled deviations from symmetry, such as bounded or convergent drift.[^c2]

The paper's canonical examples are permutation invariance (exchangeability), "shift invariance (stationarity and ergodicity)", Markovian invariance under a fixed policy–environment pair, and design-based reference structures in adaptive experimentation.[^c3] Each one supports a different frequency reading. Under exchangeability the structure is the cleanest case. An exchangeable Bernoulli sequence is "a mixture of i.i.d. Bernoulli laws", so a latent parameter is what both the one-step forecasts and the empirical frequencies converge to. Exchangeability therefore gives the repetition a precise meaning: the symmetry says what is the same across replications, and the latent variable says what the frequency is a frequency of.[^c4]

The paper also suggests reading a reference structure as a protocol: "it is often helpful to read a reference structure as a protocol statement." Read this way, it declares which parts of the environment are treated as fixed across replications, whether the procedure is randomized, and which filtration is the information history.[^c5] The paper's audit asks that probabilistic claims report the assessment and evaluation laws when they differ, the filtration and target event, and the reference structure under which the frequency meaning is asserted.[^c6] A stopping rule placed in the information set does not by itself make a repeated-sampling guarantee: "it does not by itself establish a repeated-sampling guarantee."[^c7]

The paper's use of exchangeability is diagnostic as well as constructive. In adaptive regimes it is typically violated, and the paper uses the exchangeable case "as it isolates what additional content beyond coherence is needed" for a frequency meaning.[^c8] When the symmetry fails, the reference structure has to be a different object: a drift assumption, a fixed policy–environment pair, or a randomized design. The [[reference-drift-decomposition]] shows where that object enters the argument.

## Limits

- The paper does not claim that any particular structure holds in a deployment. "The point is not that any single structure is universally appropriate, but that frequency claims are regime-relative."[^c9] Whether a stated structure is true of a given system is a question the paper leaves open.
- The exchangeable alignment is the one case the paper proves outright, and it is marked as special: "This alignment is special because the exchangeability symmetry is typically absent in adaptive regimes."[^c10]
- The examples are illustrations, not measurements. The abstract describes the applications as clarifications: "Applied illustrations clarify calibration claims, synthetic-data validity, and structural mismatches relevant to some high-confidence unsupported AI outputs."[^c11]
- The list of four families is the paper's list, not a complete taxonomy. That a declaration can be stated does not show it is correct; the audit makes a claim checkable in principle, not verified. This last point is this note's own inference, not the paper's.

## Related

- [[coherence-frequency-role-separation]] — the principle this structure completes: coherence needs a reference structure before it yields a frequency claim
- [[reference-drift-decomposition]] — where the reference structure enters the stabilization of averages
- [[calibration]] — a frequency property of the joint forecast-outcome regime, so it depends on the structure declared
- [[conformal-prediction]] — its marginal guarantee rests on exchangeability, one reference structure among those listed here

[^c1]: doi-10-48550-arxiv-2609-04115 — "A reference structure is a regime-level specification comprising"
[^c2]: doi-10-48550-arxiv-2609-04115 — "This encompasses exact symmetries (e.g., permutation invariance)"
[^c3]: doi-10-48550-arxiv-2609-04115 — "shift invariance (stationarity and ergodicity)"
[^c4]: doi-10-48550-arxiv-2609-04115 — "an exchangeable Bernoulli sequence is a mixture of i.i.d. Bernoulli laws"
[^c5]: doi-10-48550-arxiv-2609-04115 — "In adaptive deployments, it is often helpful to read a reference structure as a protocol statement."
[^c6]: doi-10-48550-arxiv-2609-04115 — "Probabilistic claims should report"
[^c7]: doi-10-48550-arxiv-2609-04115 — "it does not by itself establish a repeated-sampling guarantee"
[^c8]: doi-10-48550-arxiv-2609-04115 — "as it isolates what additional content beyond coherence is needed"
[^c9]: doi-10-48550-arxiv-2609-04115 — "The point is not that any single structure is universally appropriate"
[^c10]: doi-10-48550-arxiv-2609-04115 — "This alignment is special because the exchangeability symmetry is typically absent in adaptive regimes"
[^c11]: doi-10-48550-arxiv-2609-04115 — "clarify calibration claims, synthetic-data validity, and structural mismatches relevant to some"
