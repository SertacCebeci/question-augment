---
description: "Plugging an estimated variance into a known-variance GLR stopping rule targets the smaller known-variance complexity, so with asymptotically tight thresholds it cannot be delta-correct."
aliases: ["EV-GLR", "empirical variance GLR", "plug-in variance GLR stopping rule", "EV-TaS"]
sources: ["doi-10-48550-arxiv-2210-00974"]
---
# Empirical-variance GLR stopping rule

A generalized likelihood ratio (GLR) stopping rule in best-arm identification compares, for each competitor a of the current leader â, a statistic Z_a(t) against a threshold c(N_t, δ), and stops once every competitor is beaten. For known variances the statistic has a closed form that depends on the variance vector σ². The plug-in version replaces σ² by the empirical variance σ_t² computed from the samples so far. The resulting statistic is called EV-GLR, and the rule stops at the first t where Z_a^EV(t) exceeds the threshold for every a ≠ â.[^c1]

The mechanism is simple, and its consequence is a limit. Paired with a sampling rule that tracks the known-variance optimal allocation (EV-TaS and its Top Two analogue), the plug-in algorithm has an asymptotic sample complexity governed by the known-variance quantity T*_σ²(µ).[^c2] That quantity is smaller than the unknown-variance characteristic time T*(µ, σ²) in general, and a δ-correct algorithm must spend at least the larger one. So the plug-in algorithms cannot be δ-correct when the thresholds are asymptotically tight: "neither of these algorithms can be δ-correct".[^c3]

The paper goes further. There is a sampling rule for which every asymptotically tight threshold family, multiplied by any constant α0 > 0, yields "an algorithm which is not δ-correct".[^c4] Scaling the threshold up by a problem-independent constant does not repair the failure. The fix the authors use is to give up asymptotic tightness: they propose δ-correct EV thresholds (EV-Student, EV-Box, EV-BoB), derived from time-uniform concentration for the empirical variance. These thresholds are not asymptotically tight, so the plug-in rule does not reach the lower bound.[^c5]

The contrast is with the transportation-cost wrapper. It uses the ordinary GLR rule, and with an asymptotically tight threshold family the Track-and-Stop version satisfies a limsup of expected stopping time over log(1/δ) at most T*, the unknown-variance characteristic time.[^c6] The authors conclude that "algorithms obtained by adapting the transportation costs enjoy" stronger theoretical guarantees than the plug-in versions.[^c7]

In experiments on random instances with ten arms and δ = 0.01, the two families perform alike. The paper reports that "algorithms obtained by plugging in the empirical variance yield" similar results to the adapted-cost ones, with slightly better performance on an easy instance.[^c8] The stylized threshold used there is not δ-correct, yet the empirical error stays below δ: "the empirical proportion of error is lower than δ even when".[^c9]

## Limits

- The impossibility is an existence result over sampling rules. It shows that some sampling rule defeats the plug-in with asymptotically tight thresholds; it does not show that every plug-in algorithm with a natural sampling rule fails in practice.
- The asymptotic sample-complexity result for EV-TaS is stated in an appendix and is "a similar result involving" the known-variance quantity;[^c10] its exact conditions were not read here.
- The optimality guarantee for the transportation-cost wrapper is for a unique best arm. The experiments use a stylized threshold, so they do not test δ-correctness at all; they test only the stopping time.
- The practical gap between the two families is small in the paper's experiments, and the authors' explanation is that not knowing the variance has a small impact on sample complexity.[^c11] The theoretical gap is about worst-case guarantees, not about typical cost.
- The threshold calibration rests on time-uniform concentration for the empirical variance, which the authors say is "of independent interest",[^c12] and the detailed constructions were not checked here.

## Related

- [[unknown-variance-characteristic-time]] — the lower bound that the plug-in cannot reach, because it targets the smaller known-variance time.
- [[plug-in-glr-stopping-rule]] — another route to a GLR-type rule under unknown variance, which uses a self-normalized time-uniform boundary instead of an estimated variance inside the known-variance statistic.
- [[tie-aware-glr-stopping-rule]] — a Track-and-Stop GLR statistic for tied optima; the same family of statistics with a different alternative set.
- [[local-evidence-stopping-rule]] — a local GLR rule that also restricts the alternatives it must rule out.

[^c1]: doi-10-48550-arxiv-2210-00974 — "yields the Empirical Variance GLR (EV-GLR) statistic"
[^c2]: doi-10-48550-arxiv-2210-00974 — "In Appendix H, we derive a similar result involving"
[^c3]: doi-10-48550-arxiv-2210-00974 — "neither of these algorithms can be δ-correct"
[^c4]: doi-10-48550-arxiv-2210-00974 — "yields an algorithm which is not δ-correct"
[^c5]: doi-10-48550-arxiv-2210-00974 — "are δ-correct for the EV-GLR stopping rule"
[^c6]: doi-10-48550-arxiv-2210-00974 — "Using the GLR stopping rule with an asymptotically tight family of thresholds"
[^c7]: doi-10-48550-arxiv-2210-00974 — "algorithms obtained by adapting the transportation costs enjoy"
[^c8]: doi-10-48550-arxiv-2210-00974 — "algorithms obtained by plugging in the empirical variance yield"
[^c9]: doi-10-48550-arxiv-2210-00974 — "the empirical proportion of error is lower than δ even when"
[^c10]: doi-10-48550-arxiv-2210-00974 — "In Appendix H, we derive a similar result involving"
[^c11]: doi-10-48550-arxiv-2210-00974 — "reveals that this impact is rather small"
[^c12]: doi-10-48550-arxiv-2210-00974 — "These thresholds are based on new time-uniform concentration inequalities for Gaussian with unknown variances"
