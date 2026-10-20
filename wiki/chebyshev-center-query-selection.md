---
description: "The next pairwise question is the one whose hyperplane lies closest to the Chebyshev center of the feasible set, the center of its largest inscribed ball, so each answer cuts deeply."
aliases: ["Chebyshev-center query selection", "Chebyshev-center cut", "largest-inscribed-ball query selection", "most aggressive cut"]
sources: ["doi-10-48550-arxiv-2402-15073"]
---
# Chebyshev-center query selection

> Ask the comparison whose dividing hyperplane passes nearest the point that
> is safest to believe: the center of the largest ball that still fits inside
> what the answers have left open.

## Definition / Mechanism

Suppose an unknown parameter $A$ (here a symmetric matrix, the metric of a
subject's cost) is known only to lie in a bounded polytope $U_P$ built from
the answers so far. Each answered comparison $(i,j)$ contributes one
half-space $\langle A, M_{ij}\rangle \le \varepsilon$, where the margin
$\varepsilon$ is there "to model possible error in the judgment of the subject
and to accommodate the" indifference answer.[^c1] The Chebyshev center of
$U_P$ is the point from which the largest ball still fits: "the Chebyshev center
is the center of a ball with the largest radius inside" the set.[^c2] Its
radius is found by a semidefinite program in which every answered constraint is
tightened by $r\,\|M_{ij}\|_F$ (Theorem 3.1 of the source). The tightening is
exact because "the Frobenius norm is a self-dual norm, we have" a worst-case
perturbation of size $r$ in that direction equal to $r\|M_{ij}\|_F$.[^c3]

The question rule follows directly. Among all candidate pairs of options, ask
about the pair whose hyperplane $\langle A^\star_c, M_{ij}\rangle = 0$ is nearest
the incumbent center under the Frobenius projection distance
$|\langle A^\star_c, M_{ij}\rangle| / \|M_{ij}\|_F$. In the source's words, "we
find the question prescribing a hyperplane closest to this center;" and "this
hyperplane can be considered the most aggressive cut."[^c4] The introduction
frames the goal the same way: the rule picks "a cut that slices the incumbent
confidence set" as aggressively as possible, so the set shrinks with each
answer whichever way the answerer goes.[^c5] The sections read do not prove
that this geometric choice minimises the number of questions; "most
aggressive" is the paper's characterisation, and it is the reason the rule is
used.

Two practical points follow. First, the exhaustive search over pairs is
quadratic in the number of candidates: "This search may become too expensive
for large datasets because we" must scan all of them each round.[^c6] Second,
the source replaces the scan with a similar-cost heuristic. Sort the candidates
by their cost under the current center, $s_i = (x_i - x_0)^\top A^\star_c (x_i -
x_0)$, and score only neighbours in that order. The reason is that a pair whose
costs differ greatly is almost always answered the same way across $U_P$: "then
it is highly likely that the subject will prefer $x_i$ to $x_j$."[^c7] Only $N$
projections are computed, "by looking at pairs of adjacent costs, contrary to
the total" of $O(N^2)$ pairs, so the scan costs $O(N\log N)$ with the sort.[^c8]
The same idea extends to asking the subject to pick the best of $k$ options:
"we can slightly modify the similar cost heuristics to accommodate the k-option
questions," by averaging the projections over windows of $k$ adjacent costs.[^c9]

## Why it matters

The center does two jobs. It chooses the question, and it is a point estimate:
"its Chebyshev center represents a safe point estimate of the true cost
matrix."[^c10] In the recourse setting the same center is the reference metric
for the cost of each candidate action, so the questions and the recommendation
are computed from one object. In the source's experiment the center moves toward
the ground truth as questions accumulate: "A⋆ comes closer to the ground truth
A0 with the more questions we ask."[^c11] The mean rank of the center's
recourse among candidates "decreases as the number of questions increases."[^c12]

## Transfer

| | |
|---|---|
| **In its home field** | pairwise preference learning for a Mahalanobis cost metric: a subject states which of two recourses needs less effort, with a margin for error |
| **Here** | any elicitation in which the unknown is a parameter set and each answer is a linear inequality on it; the center and the nearest-hyperplane rule are defined only then |
| **What survives** | the largest-ball point as a defensible single estimate, and a deterministic question rule with a geometric reason to prefer it |
| **What does not** | the set and its center exist only if the answers are mutually consistent: a cycle of preferences empties $U_P$, and the paper says then "finding a Chebyshev center A⋆c is impossible" |

## Limits

- The experiments answer simulated subjects. The ground-truth matrices are
  generated, "We generate 10 ground-truth matrices A0 with this procedure:"
  and the answers come from them under the margin model. No human was asked.
- Inconsistency is not solved by the rule. The fix tolerates a fraction of
  violated answers and yields a binary SDP. The paper states that "and GUROBI
  do not support this class of problem", so the tolerant version needs ad hoc
  solvers.[^c13]
- The similar-cost heuristic can miss the pair that the full scan would pick;
  its quality is judged against that scan in the paper's appendix. "We provide
  an experiment comparing similar cost heuristics and exhaustive search in
  Section 6."[^c14] The run-time and quality numbers are not restated here.
- The rule needs a cost that is linear in the unknown. A non-linear or
  non-convex parametrisation has no Chebyshev center in this sense, and nothing
  in the sections read covers that case.

## Related

- [[separation-oracle-preference-elicitation]] — the same cut-and-shrink query
  for a linear reward, but with the analytic or volumetric center; the
  Chebyshev center is a third choice, defined by the largest inscribed ball
  rather than by distance or volume
- [[volume-removal]] — the other common rule: choose the question whose answer
  removes the most posterior mass. It needs an answer model; this rule uses
  only the geometry of the set of consistent parameters
- [[hybrid-cutting-plane-sieving-elicitation]] — cutting planes used first to
  prune the weight space, then a provable phase; a different linear-utility
  elicitation with the same geometric cut
- [[cost-robust-recourse]] — the recourse that is chosen against the set this
  rule shrinks

[^c1]: doi-10-48550-arxiv-2402-15073 — "to model possible error in the judgment of the subject and to accommodate the"
[^c2]: doi-10-48550-arxiv-2402-15073 — "the Chebyshev center is the center of a ball with the largest radius inside"
[^c3]: doi-10-48550-arxiv-2402-15073 — "Because the Frobenius norm is a self-dual norm, we have"
[^c4]: doi-10-48550-arxiv-2402-15073 — "we find the question prescribing a hyperplane closest to this center;"
[^c5]: doi-10-48550-arxiv-2402-15073 — "a cut that slices the incumbent confidence set"
[^c6]: doi-10-48550-arxiv-2402-15073 — "This search may become too expensive for large datasets because we"
[^c7]: doi-10-48550-arxiv-2402-15073 — "then it is highly likely that the subject will prefer xi to xj"
[^c8]: doi-10-48550-arxiv-2402-15073 — "by looking at pairs of adjacent costs, contrary to the total"
[^c9]: doi-10-48550-arxiv-2402-15073 — "Fortunately, we can slightly modify the similar cost heuristics"
[^c10]: doi-10-48550-arxiv-2402-15073 — "Thus, given a confidence set UP , its Chebyshev center represents a safe point estimate"
[^c11]: doi-10-48550-arxiv-2402-15073 — "A⋆ comes closer to the ground truth A0 with the more questions we ask."
[^c12]: doi-10-48550-arxiv-2402-15073 — "rank decreases as the number of questions increases."
[^c13]: doi-10-48550-arxiv-2402-15073 — "and GUROBI do not support this class of problem."
[^c14]: doi-10-48550-arxiv-2402-15073 — "We provide an experiment comparing similar cost heuristics and"
