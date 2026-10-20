---
description: "Differential privacy only guarantees a coverage floor f(α) for full-data conformal sets, sharply short of 1−α; recovering nominal coverage needs mechanism-specific stability of the trained model."
aliases: ["full-data private conformal prediction", "DP-SCP", "black-box DP coverage floor"]
sources: ["arxiv-2603-07522"]
---
# DP stability and full-data conformal coverage

Conformal prediction needs exchangeable scores. A model trained on all n points and then used on a new point gives in-sample scores that run smaller than the test score, so the scores are not exchangeable and naive full-data sets undercover.[^c1] Data splitting repairs this at the cost of sample size, and leave-one-out retraining would cost a privacy budget per model. Cho and Awan (2026) propose using the stability that differential privacy (DP) already enforces, so one private model can be trained and calibrated on the same data (their method is DP-SCP).[^c2]

## What DP alone gives, and why it falls short

Theorem 2(a) says that for any f-DP mechanism, if the set has coverage at least 1−α when the model is trained with the test point included (the ideal exchangeable world), then coverage with the model trained without it is at least f(α).[^c3] Part (b) says this is sharp. Their construction releases a noisy histogram on a diagonal-support distribution; coverage is attained in the ideal world but is at most f(α)+γ in the real one.[^c4] The construction is fragile because its behaviour depends on whether the exact test pair appears in the sample.[^c5]

For (ε,δ)-DP the nominal miscoverage α is inflated by a factor e^ε, a coverage gap of at least (e^ε−1)α+δ. The authors state this is "an intrinsic limitation of black-box DP reasoning".[^c6]

## What recovers the nominal level

With mechanism-specific assumptions the gap closes. Four assumptions are needed: model stability, P(‖θ_{n+1}−θ_n‖>u_n) ≤ δ_n; scores Lipschitz in the parameter; no ties; and one-sided anti-concentration of scores near the target quantile.[^c7] Theorem 3 then gives coverage at least (1−β_n)(1−α−2fLu_n−3δ_n−1/(n+1)), with the private quantile run at a raised rank r′ = r + m_n + τ. The buffer m_n covers training scores that cross below the ideal threshold when the model shifts, and τ covers privacy noise.[^c8]

The bound contains no privacy parameter. Coverage is governed by stability, and privacy shows up as larger sets because noise inflates the scores and the threshold.[^c9] The finite-sample variant (DP-SCP-F) keeps the full correction; the asymptotic variant (DP-SCP-A) drops m_n and τ, trading the finite-sample guarantee for efficiency.[^c10] Projected DP-SGD is analysed via synchronized coupling, and the paper reports m_n = o(n) for it.[^c11]

Relevance to asking and answering (my inference, not tested in the paper): a confidence statement computed on the same data that trained the answerer is only trustworthy to the extent the answerer is insensitive to any single item. The generic assurance is weaker than the nominal one, and the missing piece is a measurable stability property rather than a general "robustness" label.

## Limits

- The refined guarantee depends on assumptions 1–4. The authors call score regularity "not automatic for arbitrary private mechanisms"; they argue it is mild for continuous regression pipelines.[^c12]
- Coverage is marginal and for exchangeable (i.i.d.) data; nothing is shown for conditional coverage, shift, or sequential interaction.
- The setting is private regression-style learning; the transfer to language-model answering or question selection is my analogy and is not measured here.
- The sharpness construction is adversarial and does not say typical mechanisms attain the floor.

## Related

- [[conformal-prediction]] — the base guarantee whose exchangeability requirement is at issue
- [[mondrian-conformal-prediction]] — another route to validity through structure on the calibration scores
- [[conformal-abstention-floor]] — a different guaranteed floor from conformal calibration
- [[conformal-set-size-calibration-tradeoff]] — coverage preserved while set size absorbs the cost, as here with privacy

[^c1]: arxiv-2603-07522 — "the in-sample scores tend to be systematically smaller than the out-of-sample score of the test point due to overfitting"
[^c2]: arxiv-2603-07522 — "While typically viewed as a cost, DP inherently enforces algorithmic stability, as it limits the influence of any single data point on the trained model."
[^c3]: arxiv-2603-07522 — "For any f -DP mechanism M , any distribution P , and any"
[^c4]: arxiv-2603-07522 — "P(Yn+1 ∈ C(M (Dn ), Xn+1 )) ≤ f (α) + γ."
[^c5]: arxiv-2603-07522 — "This construction is deliberately fragile from a stability viewpoint"
[^c6]: arxiv-2603-07522 — "an intrinsic limitation of black-box DP reasoning"
[^c7]: arxiv-2603-07522 — "Assumption 1 (Model stability)."
[^c8]: arxiv-2603-07522 — "The bound in (2) decomposes the loss relative to the nominal level 1 − α into three sources."
[^c9]: arxiv-2603-07522 — "A pivotal feature of Theorem 3 is that the coverage bound contains no privacy parameter"
[^c10]: arxiv-2603-07522 — "This variant sacrifices a finite-sample"
[^c11]: arxiv-2603-07522 — "our stability analysis establishes that mn = o(n) for projected DP-SGD"
[^c12]: arxiv-2603-07522 — "These score regularity conditions are not automatic"
