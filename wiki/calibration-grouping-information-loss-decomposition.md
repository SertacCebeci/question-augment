---
description: "For any proper loss, expected score loss splits into miscalibration, grouping (information lost compressing features to a score) and irreducible uncertainty; recalibration fixes only the first."
aliases: ["grouping term", "reliability-grouping-uncertainty decomposition", "information-level chain decomposition"]
sources: ["arxiv-2603-15232"]
---
# Calibration, grouping and irreducible uncertainty decomposition

A probabilistic score S = s(X) is judged by expected proper loss E[ℓ(S,Y)]. The work shows this loss is a sum of regrets between nested information levels plus a residual entropy: the chain identity for A ⊆ B is E[ℓ(T,Y)] = E d(T,Q_A) + E d(Q_A,Q_B) + E E_ℓ(Q_B).[^c1] Here Q_A is the best predictor given the information in A and d is the proper-loss regret.

Taking T = S, A = σ(S), B = σ(X) gives the three-term identity: E[d(S,C)] (calibration or reliability) + E[d(C,Q)] (grouping, the information loss from X to S) + E[E_ℓ(Q)] (irreducible at the X level).[^c2] C = P(Y|S) is the recalibrated score, Q = P(Y|X) the true conditional law.

## Three failure modes, three remedies

The operational reading is a separation: reliability is proper regret at the score level, grouping is loss induced by compressing X to S, and the last term is irreducible uncertainty at the feature level.[^c3] The remedies differ. Post-hoc recalibration acts inside σ(S), so it can only reduce reliability; reducing grouping requires changing the score or representation to retain more information; the irreducible term needs richer features or better data.[^c3]

For a strictly proper loss the grouping term is zero exactly when C = Q almost surely, i.e. when S is sufficient for predicting Y from X.[^c4]

## Perfect calibration with total information loss

Take X uniform on {1,2}, P(Y=1|X=1)=0.9, P(Y=1|X=2)=0.1, and the constant score S ≡ 1/2. Then C = S, so S is perfectly calibrated and reliability vanishes, yet under Brier loss the grouping term is 0.16.[^c5] Calibration alone is compatible with severe information loss, i.e. no discrimination.[^c6]

## Brier special case

In the binary Brier case, E[(S−Y)²] = E[(S−C)²] + E[(C−Q)²] + E[Q(1−Q)], and the grouping term equals the expected conditional variance of the Bayes score Q after compressing X to S.[^c7] The framework also recovers the classical uncertainty–resolution–reliability form, with E d(Q̄,C) playing the role of resolution.[^c8] A four-level version (S ⊆ X ⊆ Z) separates chance heterogeneity remaining at X from intrinsic noise at Z, so "irreducible" is relative to an observability level.[^c9]

## Relevance to asking and answering

A stated confidence can be honest (calibrated) and still useless if it collapses distinctions the question's evidence supports. Measuring only calibration therefore cannot tell a well-informed answerer from one who always says the base rate. This application is my inference, not a claim of the work.

## Limits

The identities are standard conditional-expectation arguments; the work itself says its contribution is the operational separation, not new proofs.[^c3] Grouping and noise are defined relative to chosen sigma-algebras and are not observable without Q, so estimating them from data needs additional assumptions that this summary does not cover. No empirical test on language-model confidences was read here. Only the identity sections were read; the recalibration, ensembling and boosting results were not examined closely.

## Related

- [[calibration]] — the reliability term is calibration error; this note shows it is only one component.
- [[step-calibration-non-composition]] — another account of calibration failing to compose.
- [[log-score-verbalized-confidence-reward]] — log loss is one proper loss to which the identity applies.

[^c1]: arxiv-2603-15232 — "E[ℓ(T, Y )] = E dℓ (T, QA ) +E dℓ (QA , QB ) +E Eℓ (QB ) ."
[^c2]: arxiv-2603-15232 — "grouping (information loss from X to S)"
[^c3]: arxiv-2603-15232 — "post-hoc recalibration can only reduce (i);"
[^c4]: arxiv-2603-15232 — "Lemma 2.3 (When does the grouping term vanish?). Assume ℓ is strictly proper. Then E[dℓ (C, Q)] = 0 if and only"
[^c5]: arxiv-2603-15232 — "so S is perfectly calibrated and the reliability"
[^c6]: arxiv-2603-15232 — "Thus, calibration alone is compatible with severe information loss (no discrimination)."
[^c7]: arxiv-2603-15232 — "E[(S − Y )2 ] = E[(S − C)2 ] + E[(C − Q)2 ] + E[Q(1 − Q)]."
[^c8]: arxiv-2603-15232 — "plays the role of resolution (information gain relative to climatology)"
[^c9]: arxiv-2603-15232 — "E[dℓ (Q, Π)]: chance heterogeneity remaining at the"
