---
description: "With interval-valued predictions, pairs split into correct, incorrect and overlapping orderings; two interval AUCs equal those probabilities and, under coverage, bracket the optimal AUC."
aliases: ["iAUC", "interval-based AUC", "uncertainty-aware AUC", "uAUC", "AUC_L and AUC_U"]
sources: ["arxiv-2602-04775"]
---
# Interval-overlap three-region ranking decomposition

A classifier that reports an interval (L, U) for the event probability, instead of a point, can be scored on ranking by asking what the intervals settle. For a positive interval I1 and a negative interval I0, the pair is confidently correct if L1 > U0, confidently incorrect if U1 < L0, and uncertain if they overlap.[^c1] The paper builds two ROC-style curves from this: TPR_L against FPR_U (strict) and TPR_U against FPR_L (permissive). Their areas, AUC_L and AUC_U, are proved equal to P(I1 > I0) and 1 − P(I1 < I0).[^c2] The three probabilities sum to one, so the ROC plane splits into a correct region, an incorrect region and an overlap region.[^c3] When intervals shrink to points, overlap vanishes and both areas reduce to the classical AUC.[^c4]

## What it adds to a point AUC

A point AUC reports one number for pair ordering. On the Pima diabetes data with bootstrap 90% intervals around a logistic regression, the point AUC was 0.831, but the decomposition gave about 61% definitively correct pairs, 34% overlap and 5.6% confidently incorrect. The authors read this as showing that "a standard AUC-based evaluation would collapse these outcomes into a single estimate", hiding that few errors are made with confidence while many comparisons are ambiguous.[^c5] Widening the interval from 50% to 95% lowered AUC_L from 0.749 to 0.559 and raised overlap from 0.142 to 0.398.[^c6]

## Selective use: uncertainty-aware AUC

The uAUC is P(I1 > I0) / (P(I1 > I0) + P(I1 < I0)), the accuracy of the decisive pairs only. Proposition 1 shows it is non-decreasing in the confidence level, if the interval is symmetric around a score and correct-ranking probability does not fall as the score gap grows.[^c7] The model then abstains on more pairs and ranks the rest more reliably. This turns abstention into a property of pairs (does the evidence order these two?) rather than of single items.

## Bounds on the best achievable ranking

The optimal AUC* is the best AUC over any scoring function, attained by ranking on the true posterior η(x). If the intervals have class-conditional miscoverage α1 and α0, a pair is covered with probability at least 1 − p_pair, where p_pair = α1 + α0 − α1α0. On covered pairs a strict interval ordering implies the true ordering, which gives the sandwich AUC_L − p_pair ≤ AUC* ≤ AUC_U + p_pair (Theorem 3).[^c8] So observable intervals translate coverage guarantees, which cannot be checked per instance, into a range for how much discrimination remains possible.[^c9] This is my reading of the use: the gap between AUC_L and AUC_U is the part of ranking that this model's uncertainty cannot settle.

## Limits

- Theorem 3 assumes class-conditional coverage of the true posterior η(X) and independence of the two draws in a pair. The paper notes that individual-level coverage is unobservable, so the α values must come from assumptions or simulation, and the bounds are only as good as that input.[^c10]
- The bounds are loose when intervals are wide: p_pair is subtracted and added, so with 95% intervals AUC_L − p_pair may be uninformative. This is my inference from the formula.
- Proposition 1 needs a monotone score-gap assumption; the paper does not test it.
- Experiments use one dataset (Pima, 768 patients), one model (logistic regression) and one interval method (bootstrap percentile). Bootstrap intervals reflect parameter uncertainty, not necessarily coverage of η.
- Pair abstention is not item abstention: an item can be in many overlapping pairs, and the paper gives no policy that converts pairs into a deferral rule.
- Nothing here concerns questions or language-model answers; the transfer to those settings is untested.

## Related

- [[selective-abstraction]] — abstention on claims, where this note abstains on pairs
- [[confidence-interval-calibration]] — whether the interval itself is trustworthy, which the bounds require
- [[credible-interval-undercoverage]] — undercoverage would inflate p_pair
- [[credal-then-conformalize-interval-decomposition]] — another way of building intervals whose coverage matters here

[^c1]: arxiv-2602-04775 — "three comparison outcomes (Figure 1): (i) confidently correct if L1 > U0"
[^c2]: arxiv-2602-04775 — "We first prove that AUCL and AUCU equal the probabilities of strict interval orderings"
[^c3]: arxiv-2602-04775 — "P(I1 > I0 ) + P(I1 < I0 ) + P(overlap) = 1,"
[^c4]: arxiv-2602-04775 — "Thus, the proposed framework recovers standard ROC analysis as a special case."
[^c5]: arxiv-2602-04775 — "a standard AUC-based evaluation would collapse these outcomes into a single estimate"
[^c6]: arxiv-2602-04775 — "reaching 0.559 and 0.398 at 95% confidence, respectively"
[^c7]: arxiv-2602-04775 — "Then the uncertainty-aware AUC, uAU C(γ),"
[^c8]: arxiv-2602-04775 — "Given interval-valued predictions I(x) with classconditional miscoverage rates α1 and α0"
[^c9]: arxiv-2602-04775 — "This framework allows practitioners to quantify not just how well their current model"
[^c10]: arxiv-2602-04775 — "individual-level coverage of the true posterior η(x) remains unobservable in real-world settings"
