---
description: "Fitting a linear reward's weights is recast as a convex feasibility problem on the unit sphere, narrowed by O(n log κ) preference queries chosen by a separation-oracle cutting-plane method."
aliases: ["separation-oracle preference elicitation", "geometric preference elicitation", "ACCPM query selection", "volumetric center query selection"]
sources: ["sadigh-2017", "shi-2026-framework"]
---
# Separation-oracle preference elicitation

> Each preference query is a hyperplane cut through the space of possible
> reward weight vectors; choose the cut analytically and the number of
> queries needed to pin the weights down to a given tolerance is known in
> advance.

## Definition / Mechanism

Shi & Knox (2026) fit a linear reward $R(x) = w^\top x$
by treating weight [[recovery-postulate|recovery]] as a convex feasibility problem: since the
reward is scale-invariant, $w$ is identified with a point on the unit
sphere $S^{n-1}$, and each preference query over a synthesized trajectory
pair $(\tau^+, \tau^-)$ yields a half-space constraint $\{w : s\, q^\top w
\ge 0\}$ through the origin, where $q$ is the normalized feature
difference and $s$ the elicited sign. This is exactly the separation-oracle
(SO) setting of Grötschel et al. (1981): a query point (the next trajectory
pair to propose) is chosen by a cutting-plane center — the analytic center
(ACCPM) or the volumetric center — and both reduce the feasible region to a
tolerance $\epsilon$ in $O(n \log \kappa)$ oracle calls, $\kappa = nR/\epsilon$
for $n$ reward terms and initial containing-box radius $R$. "This framework
is equivalent to the separation oracle (SO) setting of Grötschel et al.
(1981)... Both use O(n log κ) oracle calls and differ primarily in how they
select the query point: ACCPM uses a distance-based criterion (the analytic
center), while the volumetric center uses a volume-based criterion."[^c1]

Because each step places the accepted query inside the current feasible
region, the accumulated constraint set is guaranteed consistent — the
method "never asks the same (preference) question twice" — and the query
generation is deterministic rather than distributional: trajectory pairs
are synthesized from scratch to realize the exact half-space the center
computation calls for, rather than drawn from a fixed dataset and scored
for expected volume removed. "Because SO methods find a point within the
feasible region at each step, the resulting constraint set is guaranteed
to be consistent and conflict-free... We also employ analytic approaches to
calculate optimal cutting planes rather than sampling multiple cuts for
empirical estimates of [[volume-removal|volume removal]] over a distribution. This further
allows us to output definitive weights rather than probabilistic ones."[^c2]

## Why it matters

For stall 2 (which axis — here, which weight — to query next) this gives a
query count that is *derived*, not tuned: $O(n \log \kappa)$ is a property
of the cutting-plane method, not a stopping heuristic fit after the fact.
It answers "how many preference questions to ask" with a bound that only
needs the number of reward terms and the desired tolerance, in exchange for
committing to a linear reward and to trajectories that can be synthesized
on demand rather than drawn from a fixed pool.

## Transfer

| | |
|---|---|
| **In its home field** | convex optimization: recovering an unknown point in a convex body from a separation oracle that returns a violated half-space, via the ellipsoid method's polynomial-time successors (ACCPM, volumetric center) |
| **Here** | recovering an unknown reward-weight vector from a human answerer who returns a preference sign on a synthesized trajectory pair — the answerer stands in for the separation oracle |
| **What survives** | the $O(n \log \kappa)$ query bound and the guarantee that every accepted query strictly shrinks the feasible region — so the constraint set from past questions is never contradicted by a later one |
| **What does not** | the oracle's correctness — convex-optimization theory assumes the separation oracle answers exactly, but a human answerer can be inconsistent or indifferent, and the source neither models nor measures that case |

## Limits

- The claimed query complexity presupposes the reward is exactly linear in
  the chosen outcome variables ($R(x) = w^\top x$); the paper's own
  justification for linearity (computational feasibility, interpretability,
  compatibility with the convex-geometry machinery) is an assumption about
  the reward family, not a property proved of arbitrary rewards.
- $O(n \log \kappa)$ counts oracle calls to reach a feasible-region
  tolerance $\epsilon$; it does not bound how close the recovered $w$ is to
  a human's "true" preferences when the human's answers are themselves
  noisy or inconsistent, a case the source does not evaluate.
- No user study accompanies this method in the source — the complexity and
  consistency claims are analytic, not measured on human answerers, unlike
  the volume-removal line of work it is contrasted against.

## Related

[[volume-removal]] · [[value-of-information]] · [[expected-information-gain]] · [[optimal-decision-tree]] · [[chebyshev-center-query-selection]] — the same cut-and-shrink query with the largest-inscribed-ball center instead of the analytic or volumetric one

[^c1]: shi-2026-framework
[^c2]: shi-2026-framework
