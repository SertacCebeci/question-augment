---
description: "The full Blackwell order calls almost every pair of experiments Blackwell (1953) defines, for every $k \\ge 1$,"
aliases: ["k-decision order", "comparison in k-decision problems", "k-decision comparison of experiments"]
sources: ["blackwell-1953"]
---
# K-decision order

> The full Blackwell order calls almost every pair of experiments
> incomparable. Bound how many actions the decision has and a weaker
> order results; when the *[[possible-worlds|state space]]* is binary (a dichotomy), every
> order — bounded or not — collapses to one Type-I/Type-II curve.

## Definition

Blackwell (1953) defines, for every $k \ge 1$, a comparison restricted to[^s1]
**decision problems with at most $k$ actions**: experiment $P$ is
*$k$-decision at least as informative as* $Q$ when, for every loss function
and every decision problem whose action set has size $\le k$, the expected
value obtainable from $P$ is at least the expected value obtainable from
$Q$. Blackwell's abstract calls this "a class of weaker comparisons" than
the unrestricted Blackwell order ([[blackwell-informativeness]]), which
demands the inequality for *every* decision problem regardless of how many
actions it has; that the restriction is *strictly* weaker (some pair is
$k$-decision comparable but not Blackwell comparable) is not confirmed
here — see Limits. Blackwell (1953) gives the $k$-decision order in three
equivalent forms.

Two restrictions must be kept apart:

- **Bounding the actions** ($k$). With $k=2$ and $m$ states of nature, a
  2-action decision problem is a test, and what an experiment contributes
  to it is the test's power function — a vector of $m$ correct-decision
  probabilities in $[0,1]^m$. Comparison in 2-decision problems is
  therefore a comparison of the *sets* of attainable power functions, not
  of a single curve, whenever $m > 2$.
- **Bounding the states** (a dichotomy, $m=2$). Blackwell (1953) shows
  that for dichotomies every one of these orders, the unrestricted one
  included, collapses to a single criterion expressible through errors of
  the first and second kind: one dichotomy dominates another exactly when
  its curve of attainable (false-positive, false-negative) trade-offs is
  nowhere worse than the other's.

The single-curve criterion belongs to the second restriction. The
$k$-action order reduces to it only when the state space is also binary.

## Why it matters when asking

*This section is this wiki's reading of the theorem, not the theorem
itself.* [[blackwell-informativeness]] draws a negative conclusion:
"better for every purpose" is almost never true, so ranking two question
sets needs a fixed utility. The $k$-decision order softens that: once the
downstream decision is known to have at most $k$ options — a binary
escalate/don't-escalate call, a fixed multiple-choice branch — the relevant
comparison is no longer over *every* conceivable utility, only the smaller
family of $k$-action ones. For a two-way decision over many possible states
of the world, the comparison is still set-valued: candidate question $P$
beats $Q$ for every two-way decision only if every power function $Q$ can
attain, $P$ can attain too. The comparison becomes a single curve only in
the narrower case where the *world* is binary — the question is a probe of
one hypothesis against one alternative — and there whichever candidate's
Type-I/Type-II trade-off is dominated is worse for every decision built on
it, with no utility beyond the two hypotheses.

## Transfer

| | |
|---|---|
| In its home field | Comparing two statistical experiments — Markov kernels on a shared, known state space — restricted to decision problems with $\le k$ actions; and, separately, restricted to a binary state space (a dichotomy), where every order becomes an ROC-type curve comparison. |
| Here | Comparing two candidate questions (or clarifying probes) that both feed a decision known in advance to have a bounded number of options. The asking case instantiates the *action* bound ($k$ fixed by the branch), not the state bound; it instantiates the dichotomy only when the question tests exactly one hypothesis against one alternative. |
| What survives | The structural relief: bounding the action count shrinks the family of utilities a candidate question must dominate on, so fewer pairs are incomparable; for a two-way branch the criterion is inclusion of attainable power-function sets, and for a binary world it is a curve comparison — either way a computable check rather than a full utility specification. |
| What does not | The kernel itself — no established mapping from a natural-language question to a Markov kernel over a shared state space, or from "the decision has two options" to a formal dichotomy experiment; the three equivalent forms Blackwell (1953) proves for general $k$ are not reproduced here, only the definition and the dichotomy corollary are used. |

## Limits

- Requires the downstream decision's action count to be fixed and known in
  advance, and a genuine Markov kernel on a shared state space — the same
  requirement [[blackwell-informativeness]] already flags as unmet for
  natural-language questions.
- The error-rate corollary needs a truly binary *state space* (two
  hypotheses), not merely a yes/no *question* or a two-action decision; a
  yes/no question about a non-binary world is a 2-decision problem, not a
  dichotomy, and its comparison is set inclusion in $[0,1]^m$.
- Strictness is not confirmed here. The abstract of `blackwell-1953` calls
  the $k$-decision comparisons "weaker"; whether they are strictly weaker
  (a counterexample separating $k$-decision comparability from Blackwell
  comparability) was not checked against the paper's text, and the note
  makes no claim beyond "weaker".
- What was read: the abstract page of `blackwell-1953` on Project Euclid
  (open access, DOI 10.1214/aoms/1177729032) and secondary
  characterisations; the full text (open, PDF) was not read for this
  note, so the three equivalent forms are cited for their existence only.

## Related

[[blackwell-informativeness]] · [[neyman-pearson-lemma]] · [[value-of-information]] · [[expected-utility]]

[^s1]: blackwell-1953
