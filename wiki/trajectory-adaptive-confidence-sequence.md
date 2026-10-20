---
description: "An upper confidence sequence built from the observed run, valid at every time at once, certifies when an iterative procedure has reached a target accuracy, without a worst-case horizon."
aliases: ["anytime-valid upper confidence sequence", "confidence sequence", "time-uniform upper confidence bound"]
sources: ["doi-10-48550-arxiv-2608-25551", "doi-10-48550-arxiv-2512-13123"]
---
# Trajectory-adaptive confidence sequence

An anytime-valid upper confidence sequence is an observable bound on a quantity the run cannot see, computed from the run and valid at every time at once. In the stochastic-gradient setting the bounded quantities are the squared distance of the current iterate to the optimizer and the suboptimality of a weighted average of iterates.[^c14] Neither is observable during the run, because the optimum and its value are unknown. The construction treats the run itself as evidence: the iterates and gradients "they also provide evidence about the unknown optimization error."[^c1] Because the bound holds simultaneously over time, a procedure can watch it and stop at the first time it falls below a tolerance. "the bounds may be monitored continuously and evaluated at a time selected from the observed trajectory without invalidating the coverage guarantee."[^c2]

The stopping time is what separates this from the usual alternative. A guarantee proved at a fixed horizon T "does not, in general, remain valid at a data-dependent" time chosen after the iterates, gradients or validation losses have been inspected.[^c3] One repair is to invert a worst-case fixed-time bound into a horizon and run that long. This is valid but conservative: "guarantees predict, sometimes by several orders of magnitude, so the resulting deterministic horizon" may far exceed what the realized run needs.[^c4] The sequence avoids this by being computed online "from the observed stochastic gradients and stepsizes."[^c5]

The paper also separates two properties that are easy to run together. A bound can be time-uniform (valid at all stopping times) without being trajectory-adaptive (shrinking when the realized run is benign). For an accuracy-based stop the authors state that "time uniformity alone therefore oﬀers no advantage over a ﬁnite-horizon guarantee," because thresholding either bound yields a worst-case iteration budget.[^c6] The savings come from the adaptation to the realized run, at the same worst-case decay order. On real data, the authors report that the certified stop comes "several orders of magnitude earlier than the trajectory-independent bounds against which they are compared."[^c7]

A second construction, for projected SGD with arbitrary predictable stepsizes, reaches a certificate of this kind through nonnegative supermartingales. The step that makes it valid at every time at once is the one "which converts supermartingale constructions into time-uniform" deviation control.[^c15] Its width grows with the stepsize-weighted distance and gradient terms: larger stepsizes or distances "lead to wider confidence sequences".[^c16] The convex result claims no smoothness or strong convexity: "without assuming smoothness or strong convexity".[^c17] The nonconvex version gives "time-uniform certificates for weighted first-order stationarity under smoothness assumptions".[^c18]

The 1/S_t factor is also a floor. On a one-dimensional quadratic with deterministic gradients, the paper argues that the normalisation is "unavoidable from a time-uniform (anytime-valid) perspective".[^c19] My reading, not the paper's wording, is that S_t is the accumulated stepsize weight of the average. Under the square-root schedule that makes the deterministic part scale like (1 + log t)/√t, so the speed of the certificate follows the stepsize schedule and is not fixed by the confidence construction.[^c20]

## Limits

- **Known inputs.** The constructions need the strong-convexity parameter and a sub-Gaussian variance bound. "we assume access to the problem constants that enter their" confidence sequences.[^c8] Unknown optimum values are not needed, but the constants are. The paper reports that conservative choices of the known constants matter little in the runs tested: "the eﬀect of conservative choices of these quantities is largely transient."[^c9]
- **Model assumptions.** Unbiased gradients and conditionally sub-Gaussian noise carry the analysis. "Assumption 1.3(i) is the standard conditional unbiasedness requirement in stochastic approximation."[^c10] A convex but non-strongly-convex objective is outside the stated results.[^c14]
- **Limited experiments.** The numerical evidence comes from one dataset family: "We run experiments on the covertype.binary dataset."[^c11] Nothing here tests other problem classes or noise models.
- **Time cost remains.** The rate is the canonical 1/t "up to the generally unavoidable log log t factors associated with time-uniform validity."[^c12]
- **Open gap.** The distance to the ground truth is not closed: "is an interesting question that we leave open."[^c13]
- **Nothing about asking.** The text concerns SGD. Questions, answers and human inquiry do not appear in it. The transfer below is mine.
- **Setting-specific assumptions (second construction).** The observable convex bound is stated in terms of a bound on the domain, "expressed only in terms of the known constraint radius", with sub-Gaussian noise.[^c21] The nonconvex case adds a smoothness condition, "require a standard smoothness condition on the objective",[^c22] and bounded gradients "which already appeared in the nonconvex setting to obtain an observable".[^c23] This does not conflict with the model-assumptions bullet above, which concerns the first paper's results.
- **No experiments.** My search of the archived text found no experimental section. The results are theorems, and whether the certified stop saves computation in practice is untested here.

## Transfer

*My reading, not the paper's.* An asker who stops after seeing the answers so far is choosing a stopping time from the data. A validity claim made for a fixed number of questions does not cover that stop. The non-adaptive fix is a budget set from a worst case; the paper's point is that the certificate should come from the trajectory actually observed.

What does not survive: an answer is not an unbiased gradient, there is no fixed optimum whose distance is bounded, and no sub-Gaussian noise model has an obvious counterpart in a judge's score. Whether an answer-based error admits a confidence sequence of this kind is a conjecture, not a result.

## Related

- [[time-uniform-conformal-prediction]] — the same validity at data-dependent stopping times, for prediction sets; this paper's point is that time-uniformity alone buys nothing for an accuracy stop, so trajectory adaptivity is the separate object.
- [[repeated-significance-testing]] — the error inflation from consulting one cut at every look; the sequence accepts that every-time consultation and pays only the iterated-logarithm factor.
- [[stopping-rules]] — the tolerance-based row is the one that needs a certificate of this kind.
- [[anytime-valid-majority-stopping]] — e-processes valid at any stopping time, used to stop sampling; the same validity property applied to a vote.
- [[plug-in-glr-stopping-rule]] — another time-uniform boundary used as a stopping rule, built differently (self-normalized).
- [[multi-armed-testing-by-betting]] — the same nonnegative-supermartingale device, with a wealth process in place of a stepsize-weighted variance proxy; both are valid at any stopping time.

[^c1]: doi-10-48550-arxiv-2608-25551 — "they also provide evidence about the unknown optimization error"
[^c2]: doi-10-48550-arxiv-2608-25551 — "the bounds may be monitored continuously and evaluated at a time selected from the observed trajectory without invalidating the coverage guarantee"
[^c3]: doi-10-48550-arxiv-2608-25551 — "a high-probability statement proved at a deterministic time T does not, in general, remain valid at a data-dependent"
[^c4]: doi-10-48550-arxiv-2608-25551 — "guarantees predict, sometimes by several orders of magnitude, so the resulting deterministic horizon"
[^c5]: doi-10-48550-arxiv-2608-25551 — "can be computed online from the observed stochastic gradients and stepsizes"
[^c6]: doi-10-48550-arxiv-2608-25551 — "time uniformity alone therefore oﬀers no advantage over a ﬁnite-horizon guarantee"
[^c7]: doi-10-48550-arxiv-2608-25551 — "several orders of magnitude earlier than the trajectory-independent bounds against which they are"
[^c8]: doi-10-48550-arxiv-2608-25551 — "we assume access to the problem constants that enter their"
[^c9]: doi-10-48550-arxiv-2608-25551 — "the eﬀect of conservative choices of these quantities is largely transient"
[^c10]: doi-10-48550-arxiv-2608-25551 — "Assumption 1.3(i) is the standard conditional unbiasedness requirement in stochastic approximation"
[^c11]: doi-10-48550-arxiv-2608-25551 — "We run experiments on the covertype.binary dataset"
[^c12]: doi-10-48550-arxiv-2608-25551 — "unavoidable log log t factors associated with time-uniform validity"
[^c13]: doi-10-48550-arxiv-2608-25551 — "is an interesting question that we leave open"
[^c14]: doi-10-48550-arxiv-2608-25551
[^c15]: doi-10-48550-arxiv-2512-13123 — "which converts supermartingale constructions into time-uniform"
[^c16]: doi-10-48550-arxiv-2512-13123 — "lead to wider confidence sequences"
[^c17]: doi-10-48550-arxiv-2512-13123 — "without assuming smoothness or strong convexity"
[^c18]: doi-10-48550-arxiv-2512-13123 — "time-uniform certificates for weighted first-order stationarity under smoothness assumptions"
[^c19]: doi-10-48550-arxiv-2512-13123 — "unavoidable from a time-uniform (anytime-valid) perspective"
[^c20]: doi-10-48550-arxiv-2512-13123 — "the deterministic components of"
[^c21]: doi-10-48550-arxiv-2512-13123 — "expressed only in terms of the known constraint radius"
[^c22]: doi-10-48550-arxiv-2512-13123 — "require a standard smoothness condition on the objective"
[^c23]: doi-10-48550-arxiv-2512-13123 — "which already appeared in the nonconvex setting to obtain an observable"
