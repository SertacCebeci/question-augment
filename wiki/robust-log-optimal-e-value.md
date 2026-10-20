---
description: "With only an anchor law known to be within delta of the target, the worst-case log-optimal e-value has a closed form, and its growth rate J* sets optimal stopping time at 1/J* per log(1/alpha)."
aliases: ["Anchored E-Watermarking", "robust log-optimality", "worst-case Kelly e-value", "anchored e-value"]
sources: ["arxiv-2602-17608"]
---
# Robust log-optimal e-value

A detector must score evidence against a null without knowing the law that actually generated the data. The setting here is watermark detection: the detector knows only an anchor distribution p0 (a stand-in for the true model) and that the target q lies in a neighbourhood Q(p0, δ). The detector gets one outcome-signal pair (v, s) and rejects when its e-value exceeds 1/α.[^c1]

## Mechanism

**Validity is uniform over the neighbourhood.** The e-value must have expectation at most 1 under independence for every q in the set, so the score cannot depend on the unknown q.[^c2]

**Power is the worst-case log growth.** Validity gives no power. The criterion is the Kelly-style expected log growth under the alternative. Because q is unknown to the detector, the objective is a sup-inf-sup: the detector picks e, nature picks the worst q, and the generator picks the best coupling w given q.[^c3] This generalises the GROW criterion of Grünwald et al. to an "active" case in which the generator reshapes the alternative, so it does not reduce to GROW even for a fixed generator.[^c4]

**Closed form.** The optimal e-value is e*(v, s) = (1 − δ/2)/p0(s) when s = v and δ/(2(n−1)p0(s)) otherwise, with n the alphabet size.[^c5] The optimal growth rate is J* = H(p0) − H(ν_δ), where ν_δ is a categorical distribution with mass 1 − δ/2 on one point. The first term says high-entropy anchors are easier to watermark. The second is a decreasing function of δ and so prices robustness against power.[^c6]

**Sample complexity.** With wealth W_n the sum of log e over steps and stopping time τ_α the first n where W_n ≥ log(1/α), expected stopping time scales as log(1/α) divided by a rate. The paper proves a converse bound of 1/J* for every valid e-value and shows e* attains it, even against an adversary who changes the target within the neighbourhood at every step.[^c7] The one-step greedy optimum is therefore also globally optimal for sequential testing (the paper's statement).[^c8]

**Empirical.** The abstract reports that the framework reduces the average token budget needed for detection by 13–15% relative to state-of-the-art baselines.[^c9]

## Limits

- The optimality is relative to the declared neighbourhood Q(p0, δ). If the true q lies outside it, the validity constraint of Eq. (1) is no longer guaranteed (my inference from the definition; the paper's results assume q in Q).
- The 13–15% figure is a benchmark result on watermarking, not a general property of questioning or answering. The transfer to question-asking is not tested here.
- Only the log-growth criterion is optimised; other criteria (for example minimising the worst-case type-II error at fixed n) are not addressed in what I read.
- I read the theorem statements and setup, not the proofs or the experiment section in full.

## Related

- [[e-detector]] — also builds on e-processes and Ville's inequality; here the null is a fixed test rather than a change point
- [[multi-armed-testing-by-betting]] — the same 1/rate expected-rejection-time form, with the oracle replaced by an anchor
- [[sprt]] — the likelihood-ratio special case when null and alternative are simple

[^c1]: arxiv-2602-17608 — "The detector rejects the null hypothesis if e(v, s) > 1/α."
[^c2]: arxiv-2602-17608 — "the e-value must satisfy the expectation bound uniformly across the entire uncertainty set Q"
[^c3]: arxiv-2602-17608 — "we must optimize the worst-case log-growth rate over arbitrary q ∈ Q(p0 , δ)."
[^c4]: arxiv-2602-17608 — "so our problem can not be reduced to GROW even if the watermark generator is"
[^c5]: arxiv-2602-17608 — "The optimal e-value that solves the objective in Eq. (2) is"
[^c6]: arxiv-2602-17608 — "which mathematically formalizes the intuition that watermarking is inherently easier for distributions with high entropy."
[^c7]: arxiv-2602-17608 — "Crucially, this optimality holds even against an adaptive adversary that"
[^c8]: arxiv-2602-17608 — "is not only locally optimal but also globally optimal for sequential testing."
[^c9]: arxiv-2602-17608 — "reducing the average token budget required for detection by 13-15% relative"
