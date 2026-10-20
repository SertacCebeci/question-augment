---
description: "Binary search generalised to arbitrary question sets: the greedy Given a finite hypothesis set $\\mathcal{H}$ (Dasgupta's *effective hypothesis class* $\\widehat{H}$ — the distinct labelings a pool o…"
aliases: ["GBS", "greedy EIG", "Dasgupta's greedy"]
sources: ["dasgupta-2004", "arxiv-2512-03971"]
---
# Generalized binary search

> Binary search generalised to arbitrary question sets: the greedy
> [[version-space]] algorithm and its approximation guarantee. For noiseless
> binary tests the greedy step coincides with greedy EIG.

## Problem

Given a finite hypothesis set $\mathcal{H}$ (Dasgupta's *effective hypothesis[^s1]
class* $\widehat{H}$ — the distinct labelings a pool of points admits), a prior
$\pi$ over it, and a pool of tests each splitting $\mathcal{H}$ into two known
parts, minimise the **expected** number of tests until one hypothesis remains.

Unlike classical binary search, tests carve arbitrary subsets and may not split
evenly.

## Greedy strategy (Dasgupta, 2004)

**Mechanism.** With current version space $S \subseteq \widehat{H}$, let $S_i^+$
and $S_i^-$ be the hypotheses labelling test point $x_i$ positive and negative.
Pick the $i$ maximising $\min\{\pi(S_i^+), \pi(S_i^-)\}$ — the test whose two
outcomes are most nearly equal **in $\pi$-mass**.

**Guarantee (Dasgupta 2004, Theorem 3).** If the optimal query tree needs $Q^*$
tests in expectation for targets drawn from $\pi$, the greedy strategy needs at
most $4Q^*\ln\big(1/\min_h \pi(h)\big)$. For uniform $\pi$ the approximation
ratio is thus at most $4\ln|\widehat{H}|$ — the $O(\log|\mathcal{H}|)$ form. The
exact optimum is NP-complete to construct: see [[optimal-decision-tree]] for
Hyafil & Rivest (1976).

What this note holds that [[expected-information-gain]] does not: an
**algorithm** — a mass-balance rule over a version space — and a **bound on it**
against the optimal tree. EIG is a scoring functional; this is a procedure plus
its guarantee.

For noiseless **binary** tests the greedy step coincides with EIG maximisation
*as a ranking*: with $p = \pi(S_i^+)/\pi(S)$, both $\min\{p, 1-p\}$ and
$\mathrm{EIG}(q) = H_b(p)$ are strictly decreasing in $|p - \tfrac12|$, so they
order candidate tests identically. With more than two outcomes, or when the
answer is not a deterministic function of the hypothesis, the two criteria
differ — which is why the frontmatter files EIG as `close`, not `exact`.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Active learning | generalized binary search | exact |
| Active learning | greedy active learning strategy / Dasgupta's greedy | exact — the scheme Dasgupta (2004) analyses |
| Experimental design | greedy EIG / myopic BED | close — the same ranking for noiseless binary tests only; the criteria come apart for multi-outcome or noisy tests, and BED carries no approximation guarantee |
| Active learning | uncertainty sampling | close — same greedy step, different score, no bound attached |

Not an alias: *optimal decision tree*. That is the object greedy is measured
against, and it has its own note ([[optimal-decision-tree]]).

## Why "mass", not "count"

What gets split is not the **number** of hypotheses but the probability
**mass**: the rule is stated over $\pi(S_i^{\pm})$, and Theorem 3's factor is
$\ln(1/\min_h\pi(h))$, not $\ln|\widehat{H}|$, once $\pi$ is non-uniform. If 999
of 1000 hypotheses together hold 1% of the mass, the test separating them moves
almost nothing. Dasgupta's Claim 5 makes this sharp: there is a class and a
skewed $\pi$ on which the optimal tree has average depth below 3 while the
greedy tree has average depth at least $n/2$.

**On this wiki's reading**, this is where coverage-style evaluation of a
question set parts from information: a count of regions or topics touched is a
count, not a mass, so sweeping a large but low-mass region raises such a count
without lowering [[entropy]]. No specific metric is named here and no study cited
measures the correspondence — that corollary is this note's inference, not
Dasgupta's result. See [[typical-set]].

## Noisy version

Theorem 3 assumes each test's outcome is a known, deterministic function of the
hypothesis. If answers can be wrong, the object is a *different game*: see
[[renyi-ulam-problem]] for the bound and its noise model. Dasgupta (2004) covers
no noise, and this note makes no claim about how the question count grows under
lies.

## Transfer

| | |
|---|---|
| **Home field** | active learning: a finite effective hypothesis class $\widehat{H}$, an enumerated pool of tests whose outcome is a known deterministic function of $h$, and an explicit prior $\pi$ |
| **Here** | the [[possible-worlds|possible worlds]] $W$; a question whose free-text answer partitions $W$ only after interpretation; no written prior, and candidate questions are *generated*, not enumerated |
| **What survives** | the greedy step itself — take the question whose answer distribution is most balanced in **mass**, not in count — and the shape of the result: greedy is only a log factor from optimal *when the test set is given* |
| **What does not** | the bound $4Q^*\ln(1/\min_h\pi(h))$ itself. Free-text answers are neither binary nor deterministic; $\min_h \pi(h)$ is undefined without a written prior; and $Q^*$ is defined against an optimal tree over a given test set, which does not exist when questions are produced on the fly |

## Limits

- Theorem 3 assumes a finite hypothesis class, noiseless binary tests with known
  outcomes, and a prior $\pi$ — and it is **average-case** over targets drawn
  from $\pi$. Dasgupta's Claim 1 shows that in the worst case over target
  hypotheses (linear separators in $\mathbb{R}^2$) active learning gives no
  improvement at all.
- The ratio is relative to the optimal tree for that class and that test set,
  not an absolute test count.
- The factor is $4\ln(1/\min_h\pi(h))$; it is $O(\log|\mathcal{H}|)$ only for
  uniform $\pi$ and degrades as the prior skews (Claim 5).
- The coverage-metric reading in *Why "mass", not "count"* is this note's own
  inference, not a result of `dasgupta-2004`; no metric is named and no study is
  cited for it.
- `dasgupta-2004` is read here from the author's copy
  (`cseweb.ucsd.edu/~dasgupta/papers/greedy.pdf`, dated January 2005; a summary
  appeared in NIPS 2004), and `sources.json` records it without a url — the
  verifier should attach that one.
- **Counts over a syntactic class.** arxiv-2512-03971 runs the same min-balance step on counts of depth-$d$ decision trees, with each tree weighted equally, and estimates the counts with an approximate counter.[^s2] Equal weight per tree is a uniform prior over representations, not over the distinct labelings this note's $\widehat{H}$ counts; so the paper's rule is a mass rule only where trees and functions are in one-to-one correspondence. That the two come apart is this note's inference, not the paper's claim. See [[model-counting-query-selection]].

## Related

[[optimal-decision-tree]] · [[expected-information-gain]] · [[adaptive-submodularity]] · [[twenty-questions]] · [[version-space]] · [[renyi-ulam-problem]]
- [[mutual-information]]
- [[model-counting-query-selection]] — the same min-balance rule with tree counts from an approximate counter, where this note's $\widehat{H}$ is not enumerated

[^s1]: dasgupta-2004
[^s2]: arxiv-2512-03971 — "Then the number of distinct hypotheses in Hd,n is"
