---
description: "The third way to get rid of $\\Lambda$: keep no model and no per-answer null, Li, Xie, Dai & Song (2019) monitor a stream with a kernel two-sample statistic."
aliases: ["scan B-statistic", "scan-B procedure"]
sources: ["li-2019", "wei-2022"]
---
# Scan B-statistic

> The third way to get rid of $\Lambda$: keep no model and no per-answer null,
> keep **the earlier answers themselves**. A kernel turns "has the stream
> changed?" into a two-sample test between the last $B$ answers and blocks of
> the retained reference material.

## Definition / Mechanism

Li, Xie, Dai & Song (2019) monitor a stream with a kernel two-sample[^s1][^s2]
statistic. As restated by Wei & Xie (2022):

- Inputs: a symmetric positive semi-definite **kernel** $k(\cdot,\cdot)$ on the
  observation space, a **reference sample** taken as pre-change, a block size
  $B$, and $N$ reference blocks of size $B$ drawn from it.
- The statistic: the unbiased **maximum mean discrepancy** between the
  post-change block — the most recent $B$ observations — and each of the $N$
  reference blocks, averaged and normalised by the null variance. Alarm when
  it crosses a threshold.
- Cost: $O(NB^2)$ per sample.
- The threshold is set analytically. Li et al. characterise the tail
  probability of the statistic by a change-of-measure argument, so the average
  [[run-length|run length]] can be targeted without simulating it. Wei & Xie extend the
  procedure by maximising over block sizes $B \in [2:w]$, give analytic
  approximations for both average run length and expected detection delay, and
  find an optimal window $w^\* \sim \log \gamma$ — the same order as classical
  parametric CUSUM — at $O(Nw^2)$ per sample via recursive Gram-matrix updates.

## Known as

| Name | Field | Relation |
|---|---|---|
| scan-B procedure | sequential analysis | exact — this note |
| maximum mean discrepancy (MMD) | kernel methods | **not** this concept — the divergence the statistic is built from, measured between two fixed samples with no run length or alarm |
| B-statistic | kernel two-sample testing | close — the block-averaged two-sample statistic the online version scans with; a test, not a detector |
| online kernel CUSUM | sequential analysis | close — Wei & Xie's maximisation over block sizes, a different statistic with its own delay analysis |

## Why it matters

For a questioning procedure this is the surrogate whose price is **storage**
rather than declaration. [[e-detector]] wants a declared class of pre-change
laws; [[conformal-test-martingale]] wants exchangeability; scan-B wants a kept
corpus of earlier answers plus a similarity function on answers, and a kernel
over sentence embeddings is available off the shelf.

That relocates the modelling decision rather than removing it. **The kernel
decides what counts as a change.** With an embedding kernel, a change of topic
in the questioning and a change in what the answerer asserts are the same
event; nothing in the statistic distinguishes them.

It also fixes a floor on how fast a coherence alarm can arrive: the statistic
is computed on a block of $B$ answers, so a change is invisible until enough
post-change answers exist to fill one.

## Transfer

| | In its home field | Here |
|---|---|---|
| Observation | a vector in a space carrying a kernel | one answer, embedded so that a kernel applies |
| The null | the reference blocks are pre-change draws | the earlier answers are assumed to be from the coherent phase — an assumption the session never checks |
| What survives | no densities and no per-observation null are needed; a kernel plus retained data gives a threshold that can be calibrated analytically to a target false-alarm rate |
| What does not | the i.i.d. reading of the reference blocks (answers respond to different questions), and the meaning of the alarm: a discrepancy in embedding distribution is not a contradiction, and the block delay means a single decisive clash is not what this detects |

## Limits

- **The reference sample is assumed clean.** If the incoherence was present
  from the start, the statistic compares a shifted stream with a shifted
  reference and stays silent. Nothing in the procedure audits its own baseline.
- **Block latency.** Detection requires a full post-change block; a
  contradiction that appears in one answer is not the object this method sees.
- **The definition above is taken from Wei & Xie's restatement of Li et al.,
  not from the Sequential Analysis paper itself**, which was not read this
  pass; the $O(NB^2)$ cost and the change-of-measure threshold argument are
  cited to Li et al. through that restatement.
- **The application to answers is this note's own mapping.** Neither cited work
  discusses questions, answers or coherence; the embedding step that makes a
  kernel available on text is assumed, not sourced.

## Related

[[e-detector]] · [[conformal-test-martingale]] · [[cusum]] · [[semantic-entropy]] · [[kl-divergence]]

[^s1]: li-2019
[^s2]: wei-2022
