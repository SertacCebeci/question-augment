---
description: "Given an empirical joint count table, the bottleneck becomes a greedy Input is an empirical joint count table $p(x,y)$ — nothing else. $X$ is the set of items to compress, $Y$ the relevance variable."
aliases: ["AIB", "agglomerative IB", "hard information bottleneck", "bottom-up information bottleneck"]
sources: ["dhillon-2003", "slonim-1999", "tishby-1999"]
---
# Agglomerative information bottleneck

> Given an empirical joint count table, the bottleneck becomes a greedy
> bottom-up merge whose cost per step is the exact information lost,
> producing not one distillate but every distillate from $N$ items down to 1,
> each with a price.[^c1]

## Mechanism (Slonim & Tishby, NIPS 1999)

Input is an empirical joint count table $p(x,y)$ — nothing else. $X$ is the
set of items to compress, $Y$ the relevance variable. AIB is the
$\beta \to \infty$ (hard-partition) limit of the IB self-consistent equations
([[information-bottleneck]]): each item belongs to exactly one cluster.[^c2]

Start with $N = |X|$ singleton clusters. For every pair,

$$d_{i,j} = \big(p(z_i)+p(z_j)\big)\cdot JS_{\Pi_2}\big[p(y\mid z_i),\,p(y\mid z_j)\big]$$

with $JS_\pi[p_1,p_2] = H[\sum_i \pi_i p_i] - \sum_i \pi_i H[p_i]$ and
$\pi_i = p(z_i)/p(\bar z)$. Slonim & Tishby's proposition 1 is that this
quantity **equals** the resulting drop $\delta I_y = I(Z_m;Y) - I(Z_{m-1};Y)$
— so the cost of a merge is read off the pair alone in $O(|Y|)$ operations
instead of recomputing the [[mutual-information|mutual information]] over the whole partition, a
factor-$m$ saving. Merge the argmin pair, update the affected costs, repeat
$N-1$ times.[^c3]

Two properties this buys, which the soft IB does not have:

1. **No $k$.** The output is the whole hierarchy $Z_m$ for every
   $m = N,\dots,1$; the number of clusters is chosen after seeing the cost
   curve, not before. (Dhillon, Mallela & Modha's co-clustering algorithm, the
   top-down alternative, takes the row and column cluster counts $k,\ell$ as
   *inputs*.)[^c4]
2. **A priced stopping signal.** The quality of $Z_m$ is the fraction
   $I(Z_m;Y)/I(X;Y)$ retained. On 20 Newsgroups, a two-group subset of 5765
   strings compressed to 50 clusters lost about 0.1% of the relevant
   information, and to 6 clusters kept about 90%.[^c5]

## Why it matters

Distillation names the missing algorithm: nothing in the wiki says
how to get from a transcript to a specification. AIB supplies one
**conditional on two inputs the method does not provide** — a declared
relevance variable $Y$ and a count table dense enough to estimate
$p(y\mid x)$.[^c6]

*Claim (this wiki's inference, not Slonim & Tishby's):* if each answer item
can be tagged with the decisions it bears on and those counts are formed,
AIB is the smallest procedure in the wiki that turns them into a priced
hierarchy of distillates. Nothing here supplies that tagging or that
density, so the algorithm sits on an unsolved upstream step (see Limits
below).[^c7]

Given those inputs the rest is mechanical and sourced: the procedure merges
items **because they predict the same thing about $Y$** — not because they
are worded alike or adjacent in the transcript — and each surviving cluster
carries a number, the information paid to fuse it. This does not resolve the
"point vs region" disagreement on stall 8: every $Z_m$ is still a point
commitment. What the hierarchy buys is that the choice of $m$ moves after
the evidence and carries a price, so committing to one $m$ becomes a
separate, auditable act.[^c8]

## Transfer

| | |
|---|---|
| **Home field** | distributional clustering of words/documents against a category variable, with a large corpus supplying the counts |
| **Here** | clustering answer items from one session against the decisions the specification must serve |
| **What survives** | the merge cost as the exact information loss, computable pairwise; the hierarchy over all $m$; the retained-information curve as the stopping instrument |
| **What does not** | the corpus — a single transcript gives a sparse count table with no sampling guarantee, and nothing in the method supplies $Y$; and the reading of $I(Z;Y)$ as a bound on Bayes classification error, which needs $Y$ to be a genuine class variable |

[^c9.1][^c9.2][^c9.3][^c9.4][^c9]

## Limits

- **Greedy, and known to be suboptimal.** Merging only *pairs* is justified
  because $\delta I_y$ can only grow with the number of components merged at
  once; the resulting $Z_m$ is not the optimal $m$-partition. The authors state
  the hard partition is "clearly inferior to the soft one" in the information
  plane, and propose it mainly as a starting point for reverse annealing.[^c10]
- **The stopping signal is a conjecture, not a theorem.** Slonim & Tishby
  report the retained-information curve was *empirically* concave and write "if
  this is always true" before concluding that a jump in the per-step loss marks
  a meaningful $m$. Nothing proves the curve is concave.[^c11]
- **One experiment stands behind the curve's usability.** The only
  quantitative evidence for the curve quoted above is a single 1999 experiment
  on a two-group subset of 20 Newsgroups (Slonim & Tishby); it has not been
  replicated here or shown to transfer to a non-corpus count table.[^c12]
- **Cost.** It begins with one cluster per item. Dhillon et al. (2003) quote
  the objection that agglomeration procedures do not scale linearly with sample
  size as top-down methods do; their alternating co-clustering runs in
  $O(nz\cdot\tau\cdot(k+\ell))$ but guarantees only a monotone decrease of the
  loss to a local minimum — co-clustering is NP-hard and, by their Corollary
  4.1, the algorithm terminates at a locally optimal assignment.[^c13]
- **Hard partition.** One item, one cluster. An answer that constrains two
  independent decisions must be split before the table is built, and that split
  is an unpriced human judgement upstream of the whole procedure.[^c14]
- It inherits [[information-bottleneck]]'s unsolved input: $Y$ is declared, not
  derived.[^c15]

## Related

[[information-bottleneck]] · [[mutual-information]] · [[kl-divergence]] · [[sufficient-statistic]] · [[semantic-entropy]] · [[rate-distortion-theory]]

[^c1]: slonim-1999 — "This algorithm can be considered as a bottom up hard version of the recently introduced "Information Bottleneck Method"."
[^c2]: slonim-1999 — "it can be considered as the hard (zero temperature) limit of deterministic annealing, for any prescribed number of clusters."
[^c3]: slonim-1999 — "information due to the merge of Zi and Zj can be evaluated directly (looking only at this pair) in O(IYI) operations, a reduction of a factor of m in time complexity (for every merge)."
[^c4]: slonim-1999 — "The output of the algorithm is the hierarchy of all m-partitions Zm of X for m = N, (N - 1), ... ,2,1."
[^c5]: slonim-1999 — "The quality measure of the obtained Zm partition is the fraction of the mutual information between X and Y that Zm captures."
[^c6]: dhillon-2003
[^c7]: dhillon-2003
[^c8]: slonim-1999 — "Our algorithm is a greedy procedure, where in each step we perform "the best possi- ble merge" , i.e. merge the components {Z1, ... , zd of the current m-partition which minimize cHy(Z1, ... , Zk)."
[^c9.1]: slonim-1999 — "We introduce a novel distributional clustering algorithm that max- imizes the mutual information per cluster between data and giv- en categories."
[^c9.2]: dhillon-2003
[^c9.3]: slonim-1999 — "information due to the merge of Zi and Zj can be evaluated directly (looking only at this pair) in O(IYI) operations, a reduction of a factor of m in time complexity (for every merge)."
[^c9.4]: slonim-1999 — "namely, the mutual information I(Zm; Y) which bounds the Bayes classification error."
[^c10]: slonim-1999 — "Since cHy(Zl, ... , Zk) can only increase with k (corollary 2), for a greedy procedure it is enough to check only the possible merging of pairs of components of the current m-partition."
[^c11]: slonim-1999 — "We found that empirically this curve was concave. If this is always true the decrease in the mutual information at every step, given by 8(m) == I(Z7n;Y)(-:~7n-l;Y) can only increase with decreasing m. Therefore, if at some point 8(m) becomes relatively high it is an indication that we have reached a value of m with "meaningful" partition or clusters."
[^c12]: dhillon-2003
[^c13]: dhillon-2003
[^c14]: dhillon-2003
[^c15]: dhillon-2003
[^c9]: dhillon-2003
