---
description: "Common support, or positivity, needs every treatment arm present within each confounder stratum; where it fails in the region the estimand needs, a causal answer may not be credible."
aliases: ["common support", "positivity assumption", "overlap condition"]
sources: ["arxiv-2511-19735"]
---
# Common support (positivity)

Common support, or positivity, is the requirement that within each stratum of the confounders every treatment strategy under study has a positive probability of occurring. The roadmap asks that it be checked explicitly: "Positivity, or common support, should likewise be assessed explicitly".[^p1] The paper extends the requirement beyond treatment comparisons: "analogous participation or selection positivity is required for target-trial emulation", and likewise for external-control borrowing, heterogeneous treatment effect estimation and transportability.[^p2]

The mechanism is simple. If a stratum contains only treated units, or only untreated ones, the data hold no comparison for it. A contrast reported for that stratum is then an extrapolation from other strata, however large the sample overall. The paper's diagnostic is that "Limited overlap can be diagnosed via extreme weights and"[^p3] and an effective sample size that is small relative to the nominal one. That extreme weights signal a near-empty stratum is my inference from the method, not a result the text shows.

The remedies named in the text are of two kinds. One is to adjust the analysis: "trimming, restricting to a common-support subpopulation, avoiding unsupported extrapolation". The other changes the question: "or redefining the target population or estimand".[^p4] The second is the point that matters for asking. A positivity failure is not only a fault of the method; it can show that the question asked is not one the data can answer, and the fix is to ask a narrower question.

The paper also states when the failure is serious: "If key confounders are systematically absent, if positivity fails in regions needed for" the estimand, "then the appropriate conclusion may be that causal identification is" not credible for the intended use.[^p5][^p6] The roadmap therefore treats overlap as one of several identification conditions, alongside the absence of unmeasured confounding, and not as something a larger sample removes.

A word on the name. The wiki's [[positivity-drift-in-answer-choices]] uses "positivity" for a tilt toward positive options in answers. That is unrelated. This note's term is the statistical condition.

What transfers, in my reading: a question can be asked where the answering evidence is absent for some of the cases it concerns. Checking for that absence before reporting a contrast is a discipline the paper's text supports for causal estimands. Its use for non-causal questions is my inference.

## Limits

- The paper names the diagnostics ("extreme weights and effective sample size") but gives no threshold for how much overlap is enough. The text does not calibrate them.
- The roadmap states that "Such discovery tools can scale hypothesis generation but do not replace scientific reasoning or identification theory".[^p7] Automated overlap checks are therefore not sufficient on their own, and the text does not show when they are.
- No measurement is reported of how often positivity failures change the conclusions of real studies.
- The conditions are stated for causal estimands. Their analogue for descriptive or predictive questions is not argued in the text.

## Related

- [[estimand]] — the question whose regions must have overlap; a failure can call for redefining it
- [[data-fitness-for-purpose]] — a broader check that asks whether the source holds the needed information at all
- [[rung-mismatch-in-interpretability-claims]] — identifiability as a separate check from the rung a claim reaches
- [[positivity-drift-in-answer-choices]] — the same word for an unrelated bias in answer options

[^p1]: arxiv-2511-19735 — "Positivity, or common support, should likewise be assessed explicitly"
[^p2]: arxiv-2511-19735 — "analogous participation or selection positivity is required for target-trial emulation"
[^p3]: arxiv-2511-19735 — "Limited overlap can be diagnosed via extreme weights and"
[^p4]: arxiv-2511-19735 — "subpopulation, avoiding unsupported extrapolation, or redefining the target population or estimand"
[^p5]: arxiv-2511-19735 — "If key confounders are systematically absent, if positivity fails in regions needed for"
[^p6]: arxiv-2511-19735 — "then the appropriate conclusion may be that causal identification is"
[^p7]: arxiv-2511-19735 — "replace scientific reasoning or identification theory"
