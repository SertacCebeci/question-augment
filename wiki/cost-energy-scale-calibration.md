---
description: "Adding a statistical risk term to an operational cost term in one selection rule is not scale-invariant; a single learned multiplier restores a well-defined, finite policy family."
aliases: ["cost-energy multiplier", "one-dimensional cost calibration", "scale-mismatch proposition", "policy-family invariance under linear rescaling"]
sources: ["zhang-2026-bayesian"]
---
# Cost–energy scale calibration

> Netting an information/risk term against a cost term assumes the two are
> already in the same units; that assumption can silently flip which
> question gets asked.

## Definition / Mechanism

Zhang, Song, Wang, Bhatt & Huang (2026) prove that a
Bellman rule comparing a statistical terminal risk against an operational
evidence cost is not scale-invariant. "Proposition 1 (Raw Bellman policies
are not scale invariant). Consider the raw recursion" — for a one-query
comparison "query iff $\Delta > c_m$" ($\Delta$ the risk drop from
querying, $c_m$ the cost), multiplying every terminal risk by $a>0$ while
holding cost fixed changes the query condition to $a\Delta > c_m$: "For any
fixed ∆ > 0 and cm > 0, choosing a < cm /∆ makes stopping optimal, while
choosing" the opposite makes querying optimal — with no change in which
subset has the lower predictive risk.[^c1]

Proposition 2 gives the fix: fix dimensionless terminal risks and
cost-normalized modality costs — "Proposition 2 (Policy-family invariance
under linear terminal-risk rescaling). Fix dimensionless" — and if terminal
risks are linearly rescaled by $a$, the hard Bellman policy obtained with
multiplier $\lambda'=a\lambda$ is identical to the one obtained with
$\lambda$ before rescaling: "with multiplier λ = aλ is identical to Π(λ) up
to tie-breaking." A single scalar absorbs any linear unit change.[^c2]

Lemma 2 shows this scalar is findable: "Lemma 2 (Well-posed one-dimensional
[[calibration]]). On a finite development set, with a finite" modality set and
a compact search interval, the calibration objective attains a minimizer
and only finitely many distinct hard policies occur as the multiplier
varies — a one-dimensional search suffices.[^c3]

## Why it matters

Any stall-2 criterion that nets an information/risk term against a cost
(e.g. [[value-of-information]]'s $\mathrm{Net}=\mathrm{VoI}(q)-\mathrm{Cost}(q)$)
is implicitly assuming the two are already commensurable. Proposition 1
shows that assumption is not automatic: the optimal axis can reverse from a
unit change alone, with the underlying risk ordering untouched. Proposition
2 supplies the minimal remedy — one multiplier, fit once, not a hand-picked
constant.

## Transfer

| | |
|---|---|
| In its home field | Combining a Gibbs/free-energy posterior score with operational evidence costs in one Bayesian surveillance decision |
| Here | Any question-selection criterion adding an information-value term and a cost term (VoI − Cost, EIG − Cost) |
| What survives | The proof that naive addition is not scale-invariant, and that one positive multiplier, fit by one-dimensional search on held-out data, restores a well-defined finite policy family |
| What does not | The specific calibration recipe (robust log-risk scale, robust cost-vector scale, grid search under a budget penalty) presumes a labelled development split, which a one-off question-selection setting rarely has |

## Limits

- Proved for a scalar multiplier reconciling exactly two heterogeneous
  quantities (risk, cost); it does not address a criterion combining three
  or more incommensurable terms at once.
- The multiplier is selected on a labelled development split; the proof
  gives no method for choosing units when no such split exists.
- Read from the arXiv preprint's appendix proofs (Zhang et al. 2026); not
  yet peer-reviewed — [?].

## Related

[[value-of-information]] · [[bellman-evidence-acquisition-policy]] · [[expected-utility]] · [[sensitivity-as-value-of-information]]

[^c1]: zhang-2026-bayesian — "Proposition 1 (Raw Bellman policies are not scale invariant). Consider the raw recursion"
[^c2]: zhang-2026-bayesian — "Proposition 2 (Policy-family invariance under linear terminal-risk rescaling). Fix dimensionless"
[^c3]: zhang-2026-bayesian — "Lemma 2 (Well-posed one-dimensional calibration). On a finite development set, with a finite"
