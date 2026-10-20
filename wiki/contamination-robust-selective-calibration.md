---
description: "When a selected calibration set wrongly admits non-exchangeable items, split-conformal coverage falls by at most n-m over m+1; lowering the level by that slack restores 1-alpha."
aliases: ["delta-robust selective conformal coverage", "contaminated Mondrian calibration"]
sources: ["arxiv-2603-02204"]
---
# Contamination-robust selective calibration

Selective (Mondrian-like) [[mondrian-conformal-prediction]] calibrates a [[conformal-prediction]] interval only on calibration items believed exchangeable with the test item, which gives tighter sets than pooling. The stratum is often not known but estimated. This concept is the price of getting that estimate wrong.

## Mechanism

Setting: calibration items are interventions; for a target, a calibration intervention is "safe" if it does not affect the target, and only safe ones are exchangeable with a safe test intervention. A selector labels each one safe or affecting. Let n be the size of the selected set and m the number that are truly safe; the contamination fraction is δ = (n − m)/n, the share of the selected set that is not exchangeable.[^c1]

Theorem 1 gives a finite-sample lower bound that makes no assumption on the scores of the contaminants: coverage is at least 1 − α − (n − m)/(m + 1), equivalently 1 − α − g(δ, n) with g = δn/((1−δ)n+1), which tends to about δ/(1 − δ).[^c2] The bound is worst case over contaminating distributions, so observed coverage is often better; contaminants that truly affect the target tend to have larger residuals, which only widens the interval.[^c3]

Corollary 1: given an upper bound δ̂ on δ, running split conformal at level α′ = α − g(δ̂, n) restores coverage of at least 1 − α. If α′ ≤ 0 the interval is the whole line.[^c4]

## Errors are asymmetric

Of the two selector errors, only the false-negative rate (a truly affecting item labelled safe) contaminates. Discarding a truly safe item only shrinks the set. In terms of the safe fraction π0, δ = (1 − π0)FNR / (π0(1 − FPR) + (1 − π0)FNR).[^c5] So a conservative selector, which accepts more false positives to cut false negatives, is preferred. With sparse influence (π0 large), even labelling everything safe gives δ = 1 − π0, so π0 ≥ 0.95 gives δ ≤ 0.05 with no learning. When π0 is small, "δ grows rapidly with FNRi when π0 is small".[^c6]

The same reduction means the selector need not learn the full causal graph. It only learns the binary intervention-by-target labels it will query.[^c7]

## Limits

- The bound is worst case, and the correction needs a δ̂ that is known or estimated. The paper supplies it from recovery conditions or, in the synthetic experiments, the realized contamination. A wrong δ̂ voids the guarantee (my inference).
- The correction is conservative: when δ̂ is large, α′ can reach zero and the interval becomes uninformative.
- Only a safe test item is treated; the stratum of items that do affect the target is left to future work, as are combinatorial interventions.[^c8]
- Shown on linear structural-equation simulations and one CRISPRi screen, with finite-sample tradeoffs on the real data; I did not read the experiments in detail.
- Transfer to question asking and answering is my analogy only. A stratum of "comparable past cases" for calibrating a confidence statement is a possible reading, and the paper does not test it.

## Related

- [[mondrian-conformal-prediction]] — the stratified calibration this bound protects when strata are misestimated
- [[conformal-prediction]] — the exchangeability guarantee being weakened
- [[dp-stability-full-data-conformal-coverage]] — another coverage guarantee under a deliberate departure from the clean setup
- [[atom-stratified-federated-conformal-calibration]] — calibration stratified by group

[^c1]: arxiv-2603-02204 — "The contamination fraction is δ = (n − m)/n."
[^c2]: arxiv-2603-02204 — "We prove a finite-sample coverage lower bound that depends"
[^c3]: arxiv-2603-02204 — "Theorem 1 is worst-case over contaminating distributions; empirical coverage is often better than the bound."
[^c4]: arxiv-2603-02204 — "(when α′ ≤ 0, the interval is (−∞, ∞)"
[^c5]: arxiv-2603-02204 — "This expression shows that controlling the false-negative"
[^c6]: arxiv-2603-02204 — "However, δ grows rapidly with FNRi when π0 is small"
[^c7]: arxiv-2603-02204 — "Rather than learn the full causal graph,"
[^c8]: arxiv-2603-02204 — "descendant-target strata are"
