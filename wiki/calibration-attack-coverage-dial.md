---
description: "Split conformal coverage under test-time attack moves with the strength of the attack applied to the calibration set, reported as monotone, so that calibration attack sets where coverage lands."
aliases: ["calibration-time attack strength", "attacked calibration set", "adversarial calibration shift"]
sources: ["arxiv-2511-18562"]
---
# Calibration-time attack as a coverage dial

Split conformal prediction takes a threshold from calibration scores and gives coverage that holds when calibration and test points are exchangeable. The guarantee "critically relies on exchangeability, a condition often violated under distribution shift."[^c1] An adversarial test input is one such shift: "Adversarial attack is a prominent form of distribution shift in which inputs are deliberately perturbed in worst-case directions to degrade performance."[^c2]

The mechanism the paper adds is to make the calibration set itself adversarial. Each calibration input is attacked at strength ε_cal before the quantile Q is taken, so the calibration scores come from a perturbed sample, not from the clean one. The paper's first claim is that test-time accuracy is a monotone (non-decreasing) function of this calibration attack strength (Theorem 1).[^c3] In the discussion that follows, with the test attack range fixed, a larger calibration attack gives larger prediction sets and a smaller accuracy shortfall: "larger ϵcal induces larger prediction sets and hence smaller accuracy shortfall."[^c4] The derivation is first-order. The displayed bound has o(·) remainder terms, and the error sum e_train + d_cal + e_cal from Proposition 1 is taken over from an earlier result (my reading of the formulas, not restated in prose).

The second claim concerns a tolerance band rather than a point. Fix a tolerance β around the target 1 − α. Theorem 2 gives the test-attack strengths for which coverage stays inside [1 − α − β, 1 − α + β]: an interval whose length is set by β and the model's local sensitivity. Changing ε_cal shifts that interval. "Increasing ϵcal moves the interval toward larger attack levels; decreasing it moves the interval toward smaller ones," and "this shift does not change the interval" length.[^c5] So the calibration attack chooses where the band sits along the test-attack axis, and β and the sensitivity fix how wide it is.

In the experiments the paper uses image classifiers: "We conducted image classification experiments using two" architectures, ResNet-50d and ViT, on several image datasets.[^c6] The split is "We sampled 60% data for training, 20% for calibration, and the remaining 20% for testing."[^c7] With a 90% target and a 2% tolerance, the reported result is that for fixed ε_cal the band widens as ε_cal grows, "while prediction-set sizes remain nearly unchanged."[^c8] The baseline comparison is thin: a preliminary run of RSCP on CIFAR-100 "failed to maintain the desired coverage," and the paper did not compare further.[^c9] The motivation cites Gendler et al. (2022), who report that standard CP "fails to provide valid coverage under adversarial perturbations"; that work was not read here.[^c10]

Training enters through set size. Adversarial training is said to reduce set size "through increased output entropy."[^c11] The supporting argument for Theorem 3 rests on a uniform-residual assumption: "The assumption in Theorem 3 mirrors the standard" symmetric label-noise model of multi-class learning.[^c12] The result is therefore conditional on that model. The paper's empirical side is a comparison of clean and adversarially trained ViT and ResNet set sizes at matched coverage.

## Limits

- The theory is stated under ℓ2 perturbations, "We present the theory under ℓ2 bounded perturbations for algebraic clarity," while every experiment uses ℓ∞ attacks.[^c13] The paper argues the guarantees are attack-agnostic, but the tested regime is ℓ∞ only.
- The results are for image classification. Nothing here tests text, language-model answers, or any set that gates an answer, so the dial's behaviour in the note's usual setting is unmeasured.
- The coverage claims are approximations. The derivation drops remainder terms, and the band is an authors' choice (88% to 92% around 90%). Whether the band holds outside the tested grid of ε_train, ε_cal and ε_test is not shown.
- The sign of the effect is stated in two forms: a monotone coverage statement and a "smaller accuracy shortfall" statement. I read them as the same claim for fixed test range, but the wording does not make the direction explicit for every quantity.
- Exchangeability is still needed for the base guarantee. The paper handles the attacked test point through a stability assumption (Assumption 1), with constants that are not estimated from data. The width of the bound is the sum of those constants, so an unknown constant leaves the band uncertain.
- Adversarial calibration does not repair a shift that is not an attack. Missing inputs, for example, are a different failure, handled by reweighting rather than by perturbing the calibration set.

## Related

- [[conformal-prediction]] — the base guarantee; the exchangeability assumption it relies on is what the attack breaks at test time
- [[imputation-reweighted-conformal]] — another departure from exchangeability (missing inputs), corrected by reweighting instead of by shifting the calibration set
- [[abstention-option-uncertainty-inflation]] — in medical MCQA, perturbation also widens conformal sets, and an explicit abstain option widens them far more
- [[conformal-set-size-calibration-tradeoff]] — set size driven by output entropy, the channel through which the adversarial-training result operates here
- [[calibration]] — the wider question of whether stated probabilities match outcomes, of which set coverage is one form

[^c1]: arxiv-2511-18562 — "critically relies on exchangeability, a condition often violated under distribution shift"
[^c2]: arxiv-2511-18562 — "deliberately perturbed in worst-case directions to degrade performance"
[^c3]: arxiv-2511-18562 — "is a monotone (non-decreasing) function of the calibration attack strength"
[^c4]: arxiv-2511-18562 — "larger ϵcal induces larger prediction sets and hence"
[^c5]: arxiv-2511-18562 — "the interval toward larger attack levels"
[^c6]: arxiv-2511-18562 — "We conducted image classification experiments using two"
[^c7]: arxiv-2511-18562 — "We sampled 60% data for training, 20% for calibration, and the remaining 20% for testing."
[^c8]: arxiv-2511-18562 — "prediction-set sizes remain nearly unchanged"
[^c9]: arxiv-2511-18562 — "failed to maintain the desired coverage"
[^c10]: arxiv-2511-18562 — "standard CP fails to provide valid coverage under adversarial perturbations"
[^c11]: arxiv-2511-18562 — "set size through increased output entropy"
[^c12]: arxiv-2511-18562 — "The assumption in Theorem 3 mirrors the standard"
[^c13]: arxiv-2511-18562 — "We present the theory under ℓ2 bounded perturbations for algebraic clarity"
