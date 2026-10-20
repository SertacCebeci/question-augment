---
description: "A rubric's weight is its column's spread across rollouts times its non-redundancy with the other columns, then mixed with the author's prior by a least-squares rule fitted per group."
aliases: ["matrix-derived rubric weights", "dispersion-times-nonredundancy weights", "data-derived criterion weights"]
sources: ["doi-10-48550-arxiv-2610-00389"]
---
# Dispersion-redundancy criterion weights

A rubric whose column in the win matrix varies across rollouts is one that separates them. The paper states the intuition directly: "greater variation within a column means that the rollouts receive more different outcomes under that rubric."[^c1] To put columns on one scale, each nonconstant column is min–max normalized, and "We measure variation by the population standard deviation" of the normalized column, σ_k.[^c2] A constant column gets zero variation and zero weight.

Variation alone double-counts. If two rubrics rank the rollouts almost the same way, they carry one signal, so each should count less. The paper therefore multiplies σ_k by the sum over the other rubrics of (1 − ρ_kℓ), where ρ_kℓ is the Pearson correlation between the normalized columns, and normalizes across rubrics to get a weight a_k.[^c3] The reason given for the correlation term is that columns "exhibit similar win-rate patterns, so each contributes" less distinct information.[^c4] The construction cites the nonredundancy idea from Diakoulaki et al. (1995), which the paper does not restate.[^c5]

The matrix weight says how distinct the rollouts are under a rubric. It says nothing about how much the rubric matters for the query, and the paper says so: the matrix weights reflect distinctness "but not how important that rubric is for the query."[^c6] The author's prior p_k is therefore kept, and the two are mixed by a game-theoretic least-squares rule, fitted per group rather than set as a fixed coefficient.[^c7] In the degenerate case where the fit fails, the mixture falls back to a fixed split, "record the coefficients as (0.5, 0.5)."[^c8]

What was measured: on the same reward mapping, the full weight extractor is compared with an entropy extractor and an SVD extractor. The paper describes entropy as using "within-column win-rate dispersion without accounting for cross-rubric correlation."[^c9] The four-benchmark averages in that comparison are "63.02, 60.24, 61.46, and 62.16, respectively," and the full method's 63.02 is the highest of them.[^c10] The paper argues that entropy weights are "sensitive to judge noise and extreme responses," but this is the paper's argument, and the comparison does not isolate that effect.[^c11]

## Limits

- The weights come from one group of G rollouts. Correlations among K columns estimated from few rows are noisy when G is small (my inference; the paper's group sizes are not discussed in the part read).
- The weights are computed from judge verdicts. A column is only as reliable as the pairwise judgments behind it, and the paper's claim about judge noise is made for the entropy alternative.
- Pearson correlation measures only linear co-movement of the normalized columns. A redundancy that appears in a nonlinear way between rubrics is not seen by this term (my inference).
- Because the non-redundancy term sums over the other rubrics in the same group, adding or removing a rubric changes every weight, not only its own (my inference from the formula).
- The prior p_k must be supplied; the method calibrates only how much to trust the matrix against it.
- The benchmark differences in the paper's weight comparison are a few points on a four-benchmark average, from one policy model. They do not establish that the extractor is the cause of the gains over the baselines.

## Related

- [[rollout-rubric-win-matrix]] — the object whose columns these weights are computed from
- [[recursive-rubric-decomposition]] — also treats rubric redundancy, but by splitting and filtering the rubric criteria before rollouts are scored, not from the win statistics
- [[weight-stratified-criterion-pass-rate]] — shows how fixed priority weights can hide what a rubric actually separates; a data-derived weight addresses the same gap (my inference)

[^c1]: doi-10-48550-arxiv-2610-00389 — "greater variation within a column means that the rollouts receive more different outcomes under that rubric"
[^c2]: doi-10-48550-arxiv-2610-00389 — "We measure variation by the population standard deviation"
[^c3]: doi-10-48550-arxiv-2610-00389 — "dk = σk hk"
[^c4]: doi-10-48550-arxiv-2610-00389 — "they exhibit similar win-rate patterns, so each contributes"
[^c5]: doi-10-48550-arxiv-2610-00389 — "nonredundancy as (Diakoulaki et al., 1995)"
[^c6]: doi-10-48550-arxiv-2610-00389 — "but not how important that rubric is for the query."
[^c7]: doi-10-48550-arxiv-2610-00389 — "we use a game-theoretic least-squares combination (Huang et al., 2023)"
[^c8]: doi-10-48550-arxiv-2610-00389 — "record the coefficients as (0.5, 0.5)"
[^c9]: doi-10-48550-arxiv-2610-00389 — "uses within-column win-rate dispersion without accounting for cross-rubric correlation"
[^c10]: doi-10-48550-arxiv-2610-00389 — "The four-benchmark averages are 63.02, 60.24, 61.46, and 62.16, respectively."
[^c11]: doi-10-48550-arxiv-2610-00389 — "weights sensitive to judge noise and extreme responses"
