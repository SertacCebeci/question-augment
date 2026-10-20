---
description: "The gated target-risk contrast D = A(ℓ − r⋆) turns a selective-risk test into a sign test on one bounded mean, valid only with an acceptance floor and a range of length one."
aliases: ["gated contrast", "target-risk contrast", "gated risk contrast"]
sources: ["doi-10-48550-arxiv-2608-07913"]
---
# Gated target-risk contrast

Selective risk asks for the loss among accepted items, which is a ratio: accepted loss over acceptance. The gated target-risk contrast removes the ratio. For a threshold j with acceptance indicator A_j = 1{score ≥ λ_j} and bounded loss ℓ, the paper defines "the gated target-risk contrast" D_j = A_j(ℓ − r⋆), where r⋆ is the declared target.[^c1] Rejected items contribute zero; accepted items contribute ℓ − r⋆, which lies in [−r⋆, 1 − r⋆].[^c2]

Taking expectations under a distribution Q, the mean of D is d = a(R − r⋆), where a is acceptance mass and R the conditional risk among accepted items. When a > 0, the sign of d is the sign of R − r⋆. So a bound showing d ≤ 0 is a bound showing accepted risk is at most the target. This is an algebraic identity from the definitions, my own derivation, not a result the paper proves separately. It means that a single mean of one bounded variable can be tested, rather than a ratio of two means.

## What the form buys

- **One object for concentration.** Any anytime or time-uniform bound on the mean of D, combined with a bound on acceptance a, gives a bound on accepted risk. The paper's martingales target d and a jointly, and the same contrast is reused for every registered threshold.
- **Cheap transfer across populations.** The contrast has range length one. In the paper's transfer argument this matters: total variation applied to D pays the mismatch once. "It therefore pays ηt , not (1 + r⋆ )ηt."[^c3] A ratio statistic with a range that depends on r⋆ would pay the larger factor.

## What the form does not do

The identity fails at zero acceptance. If no item is accepted, d = 0 and the sign test is satisfied trivially, which is the same triviality that lets an always-abstain policy pass a conformal risk bound (see [[crc-confident-error-control]]). A certificate therefore needs a second condition, an acceptance floor. "Operational certification additionally requires a predeclared floor" of a_min > 0, and "the contrast inequality alone" is not enough.[^c4]

The sign of d tells the operator only about the declared loss. A loss that is a weak proxy for harm gives a tight bound on the wrong quantity (see [[private-federated-selective-risk-certificate]] for the paper's limits).

## Limits

- The contrast is a marginal object: its mean is over the declared mixture, so it gives no per-input or per-subgroup statement.
- The paper uses it inside a private federated certificate, where the noise variance and the record count enter the martingale. Nothing here shows the contrast is the best statistic; the paper says the contribution is the combination "not the contrast statistic or acceptance floor individually."[^c5]
- Whether a betting or variance-adaptive construction for the same contrast gives tighter bounds is a separate question. The paper's variance-adaptive version "can improve sampling width when accepted mass is small," but "it can remain loose when its accepted-mass upper bound or the DP noise envelope dominates."[^c6]

## Related

- [[crc-confident-error-control]] — the conformal risk control threshold, where the accepted-risk ratio is bounded directly and the trivial always-abstain policy is noted
- [[conformal-abstention-floor]] — the lower bound on abstention that a risk target forces, the same floor question from the other side
- [[betting-based-conformal-risk-control]] — a nonprivate sequential bound on a conformal risk threshold
- [[private-federated-selective-risk-certificate]] — the certificate built on this contrast, with its private histogram release
- [[event-level-zcdp-histogram-release]] — how the histograms feeding the contrast are privatized

[^c1]: doi-10-48550-arxiv-2608-07913 — "the gated target-risk contrast"
[^c2]: doi-10-48550-arxiv-2608-07913 — "which lies in [−r⋆ , 1 − r⋆ ]"
[^c3]: doi-10-48550-arxiv-2608-07913 — "It therefore pays ηt , not (1 + r⋆ )ηt"
[^c4]: doi-10-48550-arxiv-2608-07913 — "Operational certification additionally requires a predeclared floor"
[^c5]: doi-10-48550-arxiv-2608-07913 — "not the contrast statistic or acceptance floor individually"
[^c6]: doi-10-48550-arxiv-2608-07913 — "can improve sampling width when accepted mass is small"
