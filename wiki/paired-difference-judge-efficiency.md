---
description: "For comparing two versions on the same tasks, a judge's label-efficiency gain is the single-rate gain scaled by (1 − r)/(1 − r_ε), so shared task outcomes shrink what a judge can save."
aliases: ["paired judge-assisted efficiency", "judge-assisted paired audit efficiency", "prediction-powered inference for paired differences"]
sources: ["doi-10-48550-arxiv-2609-34198"]
---
# Paired-difference judge efficiency

Prediction-powered inference lets a small labelled sample stand in for a larger judged one. "Prediction-powered inference with an optimally weighted proxy multiplies the effective labeled sample" by τ = 1/(1 − ρ²), where ρ is the correlation between the proxy and the target on a labelled unit.[^c1] For a single success rate the proxy is the judge's verdict and the target is the reference outcome.

A version comparison changes the unit. The unit is a task, the target is the paired difference D = H_n − H_o of reference outcomes, and the proxy is the difference of verdicts Z_n − Z_o. The paper's Proposition 3 treats a judge that is marginally non-differential, with verdict FPR + J·H plus an error whose conditional mean is zero given both outcomes, and two versions with equal outcome and error variances. Under those assumptions the paired gain is the single-rate gain multiplied by (1 − r)/(1 − r_ε), "where r = corr(H_o, H_n) is the task-level correlation of the two versions' outcomes", and r_ε is the corresponding correlation of the judge's errors.[^c2] The paper states the general form for unequal variances without its details being in the part of the text read here.

The ratio is the mechanism. Versions of one agent share most of their tasks, so r is high, and the paired proxy carries less information than a level proxy. "Two versions of an agent succeed and fail on largely the same tasks, so r is typically well above zero," [^c3] and the paired signal shrinks accordingly. The judge recovers efficiency only through its errors: they must be correlated across the two versions on the same task, for instance "because a task's patches are hard to judge whoever wrote them."[^c4] With uncorrelated judge errors (r_ε = 0), "the paired gain is the level gain times (1 − r)."[^c5]

**Measured.** The paper reports the efficiency as a width saving in its audit simulations: a paired audit saves only 5% in interval width at 80 labelled tasks.[^c6] This is the only measured efficiency this note reports. The paper's estimated values of r and r_ε are not in the part of the text read for this note, so the size of the factor on the paper's own data is not stated here.

## Limits

- The exact ratio holds under a single linear proxy, marginal non-differentiality and equal variances. "Proposition 3 assumes a single linear proxy and marginally non-differential error" [^c7]; it describes what one binary verdict can offer, not every judge-based estimator.
- Richer proxies can do better. "judge's probabilities or several judges' verdicts, can do better" [^c8] than a single verdict, so the ratio is a bound for one kind of proxy.
- Differential error is outside the benchmark. Differential error adds bias, which a labelled audit removes, and "it changes the proxy's correlation" [^c9] with the target, so the ratio no longer describes the efficiency. The paper treats Proposition 3 as the non-differential benchmark against which observed efficiencies are compared.
- The gain is an ideal. "the ideal label-efficiency gain of judge-assisted inference for a paired difference" [^c10] is the gain with optimal weighting and known correlations; estimated correlations on a finite sample will do worse.
- Power is limited for close pairs. "of close versions have low power" [^c11], so a small saving on a close pair may be the difference between an interval that excludes zero and one that does not.

## Related

- [[calibrated-judge-estimator-efficiency-ordering]] — the single-rate case, where the efficiency ordering among estimators is set out; this note gives the paired factor that scales that gain
- [[version-dependent-judge-error]] — the differential term that adds bias and changes the proxy's correlation, outside the ratio's assumptions
- [[transported-judge-calibration]] — reusing old-version labels instead of labelling the current outputs; the paper prefers the latter

[^c1]: doi-10-48550-arxiv-2609-34198 — "Prediction-powered inference with an optimally weighted proxy multiplies the effective labeled sample"
[^c2]: doi-10-48550-arxiv-2609-34198 — "where r = corr(H_o, H_n) is the task-level correlation of the two versions' outcomes"
[^c3]: doi-10-48550-arxiv-2609-34198 — "Two versions of an agent succeed and fail on largely the same tasks, so r is typically well above zero,"
[^c4]: doi-10-48550-arxiv-2609-34198 — "task's patches are hard to judge whoever wrote them"
[^c5]: doi-10-48550-arxiv-2609-34198 — "the paired gain is the level gain times (1 − r)"
[^c6]: doi-10-48550-arxiv-2609-34198 — "A paired audit saves only 5% in interval width at 80 labeled tasks."
[^c7]: doi-10-48550-arxiv-2609-34198 — "Proposition 3 assumes a single linear proxy and marginally non-differential error"
[^c8]: doi-10-48550-arxiv-2609-34198 — "judge's probabilities or several judges' verdicts, can do better"
[^c9]: doi-10-48550-arxiv-2609-34198 — "it changes the proxy's correlation"
[^c10]: doi-10-48550-arxiv-2609-34198 — "the ideal label-efficiency gain of judge-assisted inference for a paired difference"
[^c11]: doi-10-48550-arxiv-2609-34198 — "of close versions have low power"
