---
description: "Locating one voter's approval-interval boundary in an ordered sample by binary search on approve/disapprove answers, cutting per-voter queries from linear to logarithmic."
aliases: ["querying voters intelligently", "per-voter bisection search"]
sources: ["arxiv-2604-21811"]
---
# Approval-boundary bisection query

> Find a voter's whole approved interval by asking about the *fewest*
> points, not the most: probe for one approved point, then bisect
> toward each edge.

## Definition / Mechanism

The setting: a set of sampled points on a line (an ordering, no
distances needed), and a voter whose approval region is a single
contiguous interval. Instead of asking every voter about every sampled
point — the point-first sweep the same paper uses to build its
training sample — this procedure asks one voter about a *subset* of
points chosen to locate both endpoints of that voter's interval:

1. **Find one approved point.** Query points at successive median
   splits of the ordered sample — the midpoint, then the surviving
   quartile, then the surviving eighth, and so on — until one lands
   inside the voter's approved region. Rather than asking a subset of
   voters about each sampled point, we can instead ask each voter about
   a subset of sampled points. We can perform a binary search-like
   procedure to find both endpoints of each voter's approved region.[^c1]
2. **Bisect to the left edge.** With an approved point $p$ found, hold a
   right boundary $R_{bound}$ (initially $p$) and a left boundary
   $L_{bound}$ (initially the sample's first point). Given an approved
   sample point p, determine the leftmost extent of v's continuous
   approval that includes p. Let Rbound be the current right boundary of
   the search (initially p) and Lbound be the current left boundary
   (initially the first sample point in the dataset). Repeatedly query v
   on the sample point q midway between Lbound and Rbound. If q is
   approved, update Rbound to q (as the approval extends at least this
   far left). If q is disapproved, update Lbound to be the sample point
   immediately to the right of q. Continue until Lbound and Rbound
   converge, identifying the left edge of approval and thereby labeling
   all queried points.[^c2]
3. **Bisect to the right edge** the same way, searching the points to
   the right of $p$.

Every query the procedure spends also labels the points it passes over
(approved or not), so nothing asked is wasted — unlike a plain
uninformed binary search over an unknown-shape region, this one is safe
*because* the region is known to be a single interval: each query's
answer is monotone in distance from the found point, so "approved"
always means "keep searching further" and "disapproved" always means
"stop, the edge was passed."

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Active learning / search | binary search for a monotone predicate's crossing point | exact — the mechanism is ordinary bisection; what is new here is only the setting (finding an *interval's two* edges instead of one threshold) |
| Computational social choice (Blair et al. (2026)) | "querying voters intelligently" | title |

## Why it matters

The paper's baseline needs one query per voter per sampled point — cost
linear in the sample size. This procedure instead needs a query only
where the sequence of answers might flip, so the cost is logarithmic in
the sample size per edge, run once per voter. On the paper's own
experiment: For example, when we sample 105 points, we typically
identify the optimal region using only slightly more than 30 queries
per voter. This active approach to querying voters dramatically reduces
the number of queries required to identify the optimal region.[^c3]
A hundred-thousand-point sample answered with roughly thirty questions
is the difference between a method that only works on synthetic data
and one a deliberation platform could run on real participants — the
paper calls this "vital for any application of this method to human
settings."

## Limits

- No formal guarantee is proven for this procedure — no sample or query
  bound, no approximation ratio. It is described and then measured
  empirically (Figure 4); the paper's PAC guarantees (Theorem 4.2) are
  for the *passive* estimator, not for this active query scheme.
- It assumes each voter's approval region is a single contiguous
  interval and that answers are noiseless and consistent — a query
  answered inconsistently breaks the monotonicity the bisection relies
  on to interpret "approved" as "keep going."
- It optimizes *within* one voter's search, not *across* voters: it
  gives no rule for which voter to query next or when enough voters
  have been queried, unlike [[generalized-binary-search]], which scores
  candidate tests against a full hypothesis posterior.
- Reported at one operating point (voters approving regions of width
  0.4–0.6 out of a normalized range, $n\approx10^5$ sampled points,
  synthetic voters); no result here bounds the query count as a
  function of sample size or interval width.

## Related

[[generalized-binary-search]] · [[expected-information-gain]] · [[twenty-questions]] · [[version-space]]

[^c1]: arxiv-2604-21811 — "Rather than asking a subset of voters about each sampled point, we can instead ask each voter about a subset of sampled points. We can perform a binary search-like procedure to find both endpoints of each voter’s approved region."
[^c2]: arxiv-2604-21811 — "Given an approved sample point p, determine the leftmost extent of v’s continuous approval that includes p. Let Rbound be the current right boundary of the search (initially p) and Lbound be the current left boundary (initially the first sample point in the dataset). Repeatedly query v on the sample point q midway between Lbound and Rbound . If q is approved, update Rbound to q (as the approval extends at least this far left). If q is disapproved, update Lbound to be the sample point immediately to the right of q. Continue until Lbound and Rbound converge, identifying the left edge of approval and thereby labeling all queried points."
[^c3]: arxiv-2604-21811 — "For example, when we sample 105 points, we typically identify the optimal region using only slightly more than 30 queries per voter. This active approach to querying voters dramatically reduces the number of queries required to identify the optimal region."
