---
description: "A fully non-adaptive one-bit query protocol matches the best adaptive protocol's sample complexity for mean estimation, closing a COLT 2026 open problem on whether interaction helps."
aliases: ["one-bit mean estimation", "interaction is not necessary theorem", "non-adaptive one-bit protocol"]
sources: ["hu-2026-interaction"]
---
# One-bit mean estimation

> Given only a single binary message per sample about a real-valued
> distribution, fixing every query in advance — never letting an earlier
> answer steer a later question — reaches the same order-optimal accuracy as
> the best protocol that adapts.

## Definition / Mechanism

One-bit mean estimation: for $P$ on $\mathbb{R}$ with mean $\mu_P \in
[-\lambda,\lambda]$ and $k$-th central moment $\le \sigma^k$ ($k>1$), each
sample is compressed to one bit by a query (a measurable binary-valued set).
A protocol is **fully non-adaptive** if all queries — for every sample — are
fixed by public randomness before any bit is observed; adaptive protocols
may choose a query using bits already seen. Hu & Zhong (2026)
prove that a non-adaptive protocol (fixed localization queries, then
fixed-scale, center-independent refinement queries decoded only after
collection) achieves $(\epsilon,\delta)$-accuracy with sample complexity
matching, up to constants in $k$, the known adaptive lower bound — for
$k>2$: $O((\sigma/\epsilon)^2\log(1/\delta))$, and correspondingly at $k=2$
and $1<k<2$.[^c1]

This gives a negative answer to Lau and Scarlett's (2026a) COLT open
problem asking whether interaction is necessary for order-optimal one-bit
mean estimation with general (arbitrary measurable) queries: it is not.[^c2]

## Why it matters

The wiki's stall-2 question is whether an asker gains anything, in the
limit, by choosing each question from the answers already received rather
than committing to a fixed question set up front. This theorem answers that
question exactly for one well-specified estimation task: no, not in sample
complexity order. Prior work on this same problem ([[hu-2026-interaction|Hu
& Zhong (2026)]], §1, citing Lau & Scarlett 2026b) had already shown
non-adaptive protocols are *suboptimal* when queries are restricted to
thresholds or intervals — so the answer depends on how rich the question
format is allowed to be, not on adaptivity being useless in general.

## Transfer

| | In its home field | Here |
|---|---|---|
| The object | a fixed statistical estimation task: recover $\mu_P$ from $n$ one-bit-compressed i.i.d. samples | an asker choosing a sequence of binary (or general) questions about an unknown quantity |
| The claim | a specific non-adaptive query construction (fixed-scale refinement, multiscale aggregation) matches the adaptive minimax rate | whether committing to a question battery in advance can match interactive questioning, for a well-defined target |
| What survives | the qualitative result: richness of the query *class* (not adaptivity) can be what buys sample efficiency | the caution that "batch loses to adaptive" is a per-task finding, not a law — here it is false when queries are general enough |
| What does not | the rate formulas, the moment-class assumptions $\mathcal{D}_k(\lambda,\sigma)$, and the two-stage localize-then-refine construction | none of these have an analogue for an open-ended asker; there is no fixed target distribution or known moment bound on a human or model answerer |

## Limits

- The result is about **order** of sample complexity (up to constants
  depending on $k$), not exact optimality, and is proved only for the class
  $\mathcal{D}_k(\lambda,\sigma)$ of distributions with a bounded $k$-th
  central moment and known $(\lambda,\sigma)$ — a target with a single
  numeric mean, not an open-ended world model.
- It holds for **general measurable queries**; the same authors note that
  when queries are restricted to thresholds or single intervals, non-adaptive
  protocols are *not* optimal (Lau & Scarlett 2026b, cited in the source) —
  so the "interaction is not necessary" claim is conditional on query
  richness, not universal.
- Independent concurrent work (Miao 2026, cited in the source) reaches the
  same order-optimal rate by a different construction; this note follows
  Hu & Zhong's account of it, not the concurrent paper directly. [?]

## Related

[[mutual-information]] · [[channel-capacity]] · [[generalized-binary-search]] · [[value-of-information]]

[^c1]: hu-2026-interaction — "We show that this interaction can be avoided by constructing a randomized fully non-adaptive protocol that fixes all queries before observing the data and matches the optimal adaptive sample complexity."
[^c2]: hu-2026-interaction — "This gives a negative answer to the COLT 2026 open problem asking whether interaction is necessary for order-optimal one-bit mean estimation with general queries (Lau and Scarlett, 2026a, Open Problem 1)."
