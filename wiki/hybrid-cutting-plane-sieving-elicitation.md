---
description: "A two-phase pairwise-comparison algorithm for linear utilities that uses cutting-plane cuts to warm-start a provably-convergent sieving phase, using fewer queries in practice than either phase alone."
aliases: ["hybrid ACCPM and sieving preference elicitation", "Algorithm 1 (Zilberstein et al. 2026)", "hybrid cutting-plane sieving algorithm"]
sources: ["zilberstein-2026"]
---
# Hybrid cutting-plane–sieving elicitation

> Run the cheap, unbounded cutting-plane phase first to prune the weight
> space, then hand its cuts to a phase with a proven query-complexity bound
> — the speed of one, the guarantee of the other.

## Definition / Mechanism

Zilberstein et al. (2026) elicit a user's linear
utility weight vector $w^*$ from pairwise comparisons between outcome
profiles in two phases. Phase one runs the analytic-center cutting-plane
method (ACCPM) for a fixed budget of $T$ queries, cutting the feasible
weight space at each answer. Phase two runs an iterative sieving procedure
(adapted from Cohen-Addad et al. 2026) that eliminates candidate outcome
profiles rather than weights, warm-started by phase one: the ACCPM analytic
center picks the sieving phase's initial incumbent, and every cut
accumulated in phase one additionally prunes profiles that cannot beat the
incumbent under any weight still consistent with those cuts, on top of the
sieving algorithm's own elimination rule. The first phase learns cutting
planes through pairwise comparisons to rapidly shrink the space of possible
attribute weights and warm-starts the second phase by eliminating dominated
regions; the second phase then provably converges to the user's utility
function.[^c1]

The hybrid inherits the sieving phase's worst-case bound because its extra
pruning never removes fewer points than sieving alone would: the expected
number of queries is at most $O(d^2\log^2(1/\epsilon)\log(d\log(1/\epsilon)))
+ T$ (Corollary 2), and the returned weight satisfies a Euclidean-distance
approximation guarantee that translates into a per-outcome utility
approximation guarantee (Propositions 3 and Corollary 4).[^c2]

## Why it matters

In simulation ($d=6$, mirroring the paper's application) the hybrid reaches
each target approximation using fewer queries than ACCPM alone, sieving
alone, a random baseline, minimax-regret elicitation, and the
near-information-theoretic attribute-wise binary search of Ge et al.
(2024) — while matching the latter's query count and beating it under
noisy answers. Applied to elicit a community utility function for
heart-transplant allocation (about 40 pairwise queries per user) and fed
into downstream policy optimization, the resulting policy is near-optimal,
achieving a competitive ratio of 95% against the hindsight optimum — this
competitive ratio is substantially higher than both the status quo (54%)
and a greedy allocation policy (78%).[^c3]

This is a concrete answer to stall 2's "which axis first?" for one regime:
when the target is a bounded-dimensional linear utility and queries are
pairwise comparisons, an unbounded but cheap pruning criterion (cutting
planes) and a bounded-query elimination criterion (sieving) are not
substitutes but complements — one screens the candidate space cheaply, the
other is what actually terminates it with a guarantee.

## Transfer

| | |
|---|---|
| **In its home field** | preference elicitation for policy optimization: pairwise comparisons between outcome profiles under a linear utility over $d\le 6$ attributes, oracle assumed noiseless or margin-noisy |
| **Here** | any two-phase selection strategy where a cheap-but-unbounded criterion prunes the candidate space before a slower criterion with a proven stopping bound runs to completion |
| **What survives** | the warm-start structure — shrink the space first with an unbounded, empirically fast method, then run a method whose termination is provable on what remains, letting the first phase's discarded region count toward the second phase's bound |
| **What does not** | the elimination rule's correctness needs the two phases to share one convex feasible-weight representation (cuts stay feasible under the renormalisation between simplex- and Euclidean-normalized weights); a domain without a shared representation between the pruning and terminating criteria has no cuts to hand across |

## Limits

- The convergence guarantee (Proposition 3, Corollary 2) is stated for the
  noiseless ternary-comparison oracle; noise robustness is analysed
  separately (§D) and is not restated here as a guarantee.
- Query complexity is polynomial in $d$, but both the simulation and the
  heart-transplant application fix $d=6$; nothing here bounds behaviour at
  larger $d$.
- The competitive-ratio comparison (95% vs 54%) is against a hindsight
  optimum computed under the *elicited* utility, not an independently
  validated ground-truth utility — it measures fit to what was elicited,
  not to an external standard.
- Source verified provisionally against the archived arXiv text extract by
  the researcher; not yet independently re-verified. [?]

## Related

[[current-solution-strategy]] · [[optimistic-pessimistic-strategy]] · [[volume-removal]] · [[cross-type-eig]]

[^c1]: zilberstein-2026 — "Our algorithm has two phases. The first phase learns cutting planes through pairwise comparisons to rapidly shrink the space of possible attribute weights and warm-starts the second phase by eliminating dominated regions. The second phase then provably converges to the user’s utility function."
[^c2]: zilberstein-2026 — "Corollary 2 (Query complexity of Algorithm 1). The expected number of queries that Algorithm 1 asks is"
[^c3]: zilberstein-2026 — "Notably, our hybrid algorithm (Algorithm 1) uses fewer queries than ACCPM, iterative sieving,"
