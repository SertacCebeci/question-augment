---
description: "[[entropy|Entropy]] and mutual information computed from counts are wrong in a Setting: $N$ i.i.d. samples binned into $m$ cells;"
aliases: ["plug-in entropy estimator bias", "naive entropy estimator bias", "limited-sampling bias"]
sources: ["paninski-2003"]
---
# Information estimation bias

> [[entropy|Entropy]] and mutual information computed from counts are wrong in a
> direction, by an amount set by the ratio of table cells to samples — and the
> error bars are small exactly when the error is large.

## Results (Paninski, *Neural Computation* 2003)

Setting: $N$ i.i.d. samples binned into $m$ cells; $\hat H_{MLE}$ is the[^s1]
plug-in ("naive") estimator $-\sum \hat p_i \log \hat p_i$.

1. **The bias is one-sided and bounded by the cell-to-sample ratio.**
   Proposition 1: $-\log\!\big(1 + \tfrac{m-1}{N}\big) \le B(\hat H_{MLE})
   \le 0$, with equality above only for degenerate $p$; the lower bound is
   tight as $N/m \to 0$. For fixed $m$ and $N \to \infty$,
   $B(\hat H_{MLE}) = -\tfrac{m-1}{2N} + o(N^{-1})$ — Miller and Madow's 1955
   rate, proved here without their non-convergent expansion. Entropy is
   **underestimated**; a record therefore looks more determined than it is.
2. **Variance is small whatever $m$ is.** $\mathrm{Var}(\hat H_{MLE}) \le
   (\log N)^2 / N$ for all $N$, independent of $m$ and $p$ (Antos &
   Kontoyiannis 2001, restated in §3.2). Bias and variance move in opposite
   directions with $m$: the paper's own summary is that information estimates
   in this regime "are likely contaminated by bias, even if 'bias-corrected'
   estimators are used", and that standard confidence intervals "drastically
   underestimate the error".
3. **Mutual information inherits it with the opposite sign, but not
   always.** $\hat I = \hat H(x) + \hat H(y) - \hat H(x,y)$; when $p(x,y)$ has
   full support on $m_x m_y$ points,
   $$B(\hat I) = \frac{m_x m_y - m_x - m_y + 1}{2N} + o(N^{-1})
   = \frac{(m_x-1)(m_y-1)}{2N},$$
   positive, so $I$ is **overestimated**. Paninski notes explicitly that this
   is not universal: with support as small as $\max(m_x,m_y)$ the rate can be
   negative.
4. **The condition under which any of it converges.** Theorem 1: the sieve
   estimator is consistent if the discretisations satisfy
   $m_{S,N}\, m_{T,N} = o(N)$ — the number of **joint cells must be
   asymptotically negligible against the number of samples**. Theorem 3 gives
   the converse: if $N/m \to c \in (0,\infty)$, the sorted empirical histogram
   converges to the wrong density, $\hat H$ stays biased as $N \to \infty$,
   and the asymptotic error has a strictly positive lower bound over a large
   region of parameter space. Corrections barely help there: in the $c \to 0$
   limit the Miller correction removes half a nat and the jackknife one nat.
5. **No estimator escapes by cleverness alone.** Antos & Kontoyiannis (2001),
   restated in §3.2: for any sequence of estimators and any rate $a_N \searrow
   0$ there is a distribution whose true convergence is infinitely slower.
   Paninski's own polynomial-approximation estimator is offered with a bound
   on maximum error, not with a rate; its performance claims are not read
   here.

## Why it matters

[[agglomerative-information-bottleneck]] prices every merge as a drop in
$I(Z;Y)$, and [[information-bottleneck]] trades $I(\tilde X;X)$ against
$I(\tilde X;Y)$. Both are differences of estimated informations, and stall 8's
open question names the missing input as "a count table dense enough to
estimate $p(y\mid x)$". Theorem 1 makes "dense enough" a number: **cells
$= o(N)$**, where $N$ is the count of answers, not of words.

A session with 40 answers coded into 40 items $\times$ 5 decisions has
$N/m = 0.2$ — Theorem 3's regime, not Theorem 1's. There, the merge prices are
biased, the bias does not vanish with patience, and a bootstrap over the same
answers will report tight intervals around the wrong number. The lever this
note can price is a coarser table: fewer items, fewer decision categories,
until cells fall well below $N$. That coarsening is itself a compression
choice made *before* the priced one, and nothing prices it.

## Known as

| Field | Name there | Same object? |
|---|---|---|
| Statistics / information theory | bias of the plug-in (maximum-likelihood) entropy estimator | exact |
| Neurophysiology data analysis | the limited-sampling bias / sampling bias problem | exact — same estimator, same $m/N$ dependence; the phrase names the practical problem |
| Machine learning (decision trees) | information gain's preference for high-arity splits | close — the same upward bias in $\hat I$, met as a split criterion; [[mutual-information]] records Quinlan's gain ratio as the response |
| — | Miller–Madow correction, jackknife, NSB | **not aliases** — these are corrections and rival estimators; item 4 above says how little the first two recover when $N \sim m$, and NSB is not read here |

## Transfer

| | |
|---|---|
| **Home field** | $N$ i.i.d. draws from a fixed joint law, binned by a discretisation chosen **before** the data are seen (Paninski is explicit that $S_N, T_N$ "are chosen in advance, before we see a single sample") |
| **Here** | one session's answers, coded into an item $\times$ relevance-variable table built *after* reading the transcript, with each question chosen in light of the previous answer |
| **What survives** | the cell-count condition $m = o(N)$ as a yardstick; the signs (entropy down, mutual information up under full support); and the warning that small variance is not evidence of a small error |
| **What does not** | the premises the bounds are proved under. Answers in a session are neither independent nor identically distributed, and the binning is chosen after the fact — both push the estimate further from the truth in ways no result here covers, so these bounds are a **best case** for a transcript, not a [[calibration]] of it |

## Limits

- Whether a dedicated undersampled-regime estimator — NSB,
  Kraskov–Stögbauer–Grassberger nearest-neighbour estimation, or Paninski's
  own polynomial-approximation estimator — rescues a table with $N \sim m$ was
  not read here. Item 5 rules out a *uniform rate guarantee*, not a practical
  improvement. Coarsening is the lever this note can price, not the only lever
  that exists.
- The theorems are about discrete binned data, i.i.d. sampling, and
  fixed-in-advance discretisation. This note's use of them on an answer
  record satisfies none of the last two; what it earns is a necessary
  condition and a direction, not a corrected number — that reading is this
  wiki's, not Paninski's.
- The mutual-information sign result is conditional on the support pattern of
  $p(x,y)$; the paper corrects the belief that plug-in $\hat I$ is biased
  upward everywhere. Quoting "$I$ is overestimated" without the full-support
  condition would be wrong.
- Proposition 1 bounds the bias of $\hat H$, not of a *difference* of three
  such estimates; how the three biases compose in $\hat I$ for a specific
  table is given asymptotically (item 3), not as a finite-$N$ bound.
- Nothing here tells you how to build the table, which is the input stall 8
  actually lacks; it only says when a table you already have is too fine.

## Related

[[agglomerative-information-bottleneck]] · [[information-bottleneck]] · [[mutual-information]] · [[entropy]] · [[expected-information-gain]] · [[distillation-input-debt]]

[^s1]: paninski-2003
