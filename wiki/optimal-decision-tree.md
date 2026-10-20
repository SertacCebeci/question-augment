---
description: "Constructing the exactly optimal question order is NP-complete; greedy on the Given a finite hypothesis set and a finite, enumerated set of tests with known outcomes,"
aliases: ["optimal binary decision tree", "minimum expected cost decision tree", "optimal test sequencing"]
sources: ["hyafil-1976", "adler-2008"]
---
# Optimal decision tree

> Constructing the exactly optimal question order is NP-complete; greedy on the
> most informative test is a logarithmic-factor approximation.

## Problem

Given a finite hypothesis set and a finite, enumerated set of tests with known[^s1][^s2]
outcomes, build the decision tree minimising the expected number of tests until
one hypothesis remains.

## Result 1 — NP-complete (Hyafil & Rivest, 1976)

Constructing an optimal binary decision tree is NP-complete (Hyafil & Rivest, 1976): no algorithm finds the exact optimum in time polynomial in the number of
tests and hypotheses unless P = NP. The decision version is NP-complete; the
construction problem is correspondingly NP-hard.

This is a **tractability** result, not an undecidability one. The optimal tree
is computable — exhaustive search over trees finds it, and small instances are
solved exactly in practice. What the theorem denies is a polynomial-time exact
method, i.e. scaling.

## Result 2 — greedy is an $O(\log n)$ approximation

Choosing, at each step, the most informative test (maximising
[[expected-information-gain]]) is a $(\ln n + 1)$-approximation to the minimum
expected test count over $n$ hypotheses — Adler & Heeringa, *Approximating
Optimal Binary Decision Trees* (2008), which improved the constant on an
$O(\log n)$ ratio already known for greedy on this problem.

## Two large lessons

**1. Do not search for the perfect question order.** The exact optimum is
intractable at scale, not impossible in principle: enumerating the whole
question space and solving for the optimal order is a computation whose cost
grows super-polynomially, so for any question space of interesting size it is
not available.

**2. Greedy is good enough and guaranteed.** Asking "what narrows things most
right now" at every step is a logarithmic factor from optimal. For $n = 1000$
hypotheses $\ln 1000 + 1 \approx 8$ — greedy's expected test count is at worst
about $8\times$ the optimal tree's, on the *given finite test set* the bound is
defined over.

So proceeding one at a time, greedily, without backtracking is not a compromise
against a tractable ideal; it is the guaranteed option.

## The heuristic form

**This wiki's reading, not a result of the cited work.** *Ask the question whose
answer will most reshape the model* looks like greedy information gain stated
without mathematics, so a questioner who follows it may be running the greedy
step without ever computing an EIG. Neither hyafil-1976 nor adler-2008
identifies a natural-language heuristic with the greedy rule they analyse, and
no study cited here measures the correspondence; see
[[adaptive-submodularity]] for the same inference made against a different
guarantee.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Algorithms / complexity | optimal binary decision tree | exact — the object Hyafil & Rivest's theorem is about |
| Operations research | minimum expected cost decision tree | exact under unit test costs; with non-uniform costs the objective is the weighted one, which contains this as a special case |
| Testing / diagnosis | optimal test sequencing | close — the same minimisation, stated over diagnostic tests rather than an abstract test set |

Not an alias: *Hyafil–Rivest*. That is a source label (`hyafil-1976`), not a name
the object goes by. Nor are *decision tree NP-completeness* and *greedy decision
tree approximation* aliases: they name two different theorems, by different
authors, about this object — they are Result 1 and Result 2 above.

## Transfer

| | In its home field | Here |
|---|---|---|
| Objects | a finite hypothesis set and an enumerated finite test set with known outcome distributions | an unbounded, unenumerated set of possible questions with free-text answers and no prior |
| Cost | expected number of tests to isolate one hypothesis | number of turns in a conversation, where turns differ in effort and an answer may open new hypotheses |
| What survives | the hardness of exact ordering (so: do not plan the whole order), and the *shape* of the greedy guarantee — proceed one at a time, no backtracking, and expect the loss to be logarithmic rather than unbounded | |
| What does not | the $(\ln n + 1)$ factor itself: it is defined against an optimal tree over a **given** finite test set, which does not exist when questions are generated on the fly — and hence the "at worst $8\times$ for $n = 1000$" figure is not a statement about a conversation | |

## Limits

- [[np-completeness|NP-completeness]] is for the exact optimum over a finite, **given** test set
  with known outcomes; it says nothing about instances small enough to search,
  nor about approximate optima.
- The $\ln n + 1$ bound is on expected test count against the optimal tree, not
  against information; [[generalized-binary-search|greedy EIG]] and greedy tree cost coincide only under
  uniform test costs.
- Assumes the tests exist. Nothing here generates a question, and the moment new
  hypotheses appear mid-process the $n$ the bound is stated in has changed.
- `hyafil-1976` and `adler-2008` are verified against publication listings, not
  read in full here; the constant in the Adler & Heeringa bound is quoted from
  the paper's own statement of its result.

## Related

[[expected-information-gain]] · [[generalized-binary-search]] · [[adaptive-submodularity]] · [[huffman-coding]]

[^s1]: hyafil-1976
[^s2]: adler-2008
