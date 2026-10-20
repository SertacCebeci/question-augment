---
description: "Measured language preference is debiased by regressing exposure, gold-availability and cultural priors out of the raw score and keeping the residual; the English lead then largely disappears."
aliases: ["DeLP", "debiased language preference", "prior-calibrated language preference", "residual language preference"]
sources: ["arxiv-2601-02956"]
---
# Debiased language preference

A raw language-preference score compares how often a retriever surfaces evidence in each document language for a fixed query language. The score mixes two things: what the model would do with a neutral corpus, and what the corpus and benchmark make available. Debiased language preference (DeLP) separates them by a regression: the structural priors are fitted to the raw score, and the residual is kept as the model's own preference.[^d1]

## The mechanism

For each query language L_q and document language L_d, the raw score s_e comes from an existing metric (MLRS) for a given encoder e. A feature vector φ(L_q, L_d) stacks log-transformed covariates: the exposure prior, a corpus-size prior, a passage-length statistic, the gold-availability prior, the cultural prior, and an indicator for L_q = L_d.[^d2] A ridge regression fits β̂ to the raw score, and the residual r = s − φᵀβ̂ is what remains after the priors. The residual is re-centred by the global mean of the raw scores, so the output stays on the scale of the raw metric. Calibration is run separately for each encoder.[^d3]

Ridge regularization is there to keep the coefficients stable when the priors are correlated with one another.[^d4] The authors' stated test is that the residual, unlike the raw score, should not track the priors. Their check is a correlation between each preference measure and each prior. Here "After calibration, these correlations drop" sharply.[^d5] They conclude that DeLP "effectively decouples intrinsic model tendencies from the structural signals."[^d6]

## What the calibrated score shows

After calibration the landscape changes shape. "The previously dominant English preference largely disappears, and the strongest signal" moves to the same-language cells of the matrix.[^d7] The importance of this is that the raw English lead, read off the same matrix, was largely a prior. The next note covers what replaces it.[^d8]

## Transfer from another field

Residualizing a dependent variable on nuisance covariates is ordinary regression adjustment. What survives the transfer is the logic: a residual means "the part the covariates cannot explain," so it is only as clean as the covariate set. What does not transfer cleanly is the claim that the residual is "intrinsic." Here the priors are themselves computed from the same benchmark (the gold-availability prior from the corpus overlap, the cultural prior from an LLM classifier). If a prior absorbs part of the model's real preference, the residual under-states it; if a prior misses a confound, the residual over-states what is left. I did not find a text in the paper that checks either direction. This is my reading of the design.

## Limits

- The residual is a model of the priors, validated by correlation (Table 4 of the paper), not by any ground truth for intrinsic preference.
- The method debiases the retriever only. "generator-level preference can still remain" when the model reads the evidence.[^d9]
- The priors and the raw metric come from one Wikipedia-based setup and three multilingual encoders, two of them SentenceBERT variants.[^d10]
- The centring step keeps the scale comparable to the raw metric. The absolute values of DeLP therefore carry no meaning beyond the relative differences between language pairs.

## Related

- [[structural-priors-in-language-preference]] — the confounds this regression removes, and why the raw score is misleading
- [[monolingual-query-document-alignment]] — the residual preference that the calibration exposes
- [[embedding-retriever-position-bias]] — the same move (hold a nuisance variable fixed, then read the effect) applied to document length rather than language

[^d1]: arxiv-2601-02956 — "We define the debiased preference as the residual signal after removing the component explained by structural priors"
[^d2]: arxiv-2601-02956 — "we incorporate two auxiliary structural controls, namely a corpus-size prior"
[^d3]: arxiv-2601-02956 — "we apply our calibration procedure independently to each retriever and report"
[^d4]: arxiv-2601-02956 — "We use ridge regularization to stabilize coefficients under the various priors, preventing any"
[^d5]: arxiv-2601-02956 — "After calibration, these correlations drop"
[^d6]: arxiv-2601-02956 — "DeLP effectively decouples intrinsic model tendencies from the structural signals."
[^d7]: arxiv-2601-02956 — "The previously dominant English preference largely disappears, and the strongest signal"
[^d8]: arxiv-2601-02956 — "English preference is largely a byproduct of"
[^d9]: arxiv-2601-02956 — "our debiasing targets retriever-level preference, while generator-level preference can still remain."
[^d10]: arxiv-2601-02956 — "BGE-m3 (Chen et al., 2024) as the multilingual retriever and re-ranker."
