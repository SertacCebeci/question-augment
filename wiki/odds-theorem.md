---
description: "A closed-form optimal rule for stopping on the **last** success in a fixed, Let $I_1,\\dots,I_n$ be indicators of independent events, $p_j = E[I_j]$, $q_j = 1-p_j$,"
aliases: ["Odds-theorem", "Odds-algorithm", "Bruss' odds algorithm", "Bruss algorithm"]
sources: ["bruss-2000"]
---
# Odds-theorem

> A closed-form optimal rule for stopping on the **last** success in a fixed,
> known sequence of independent yes/no trials — the exact answer to "which
> opportunity should I commit to, given I know how many remain and each
> one's own probability of being a hit."

## Definition / Mechanism

Let $I_1,\dots,I_n$ be indicators of independent events, $p_j = E[I_j]$,[^s1]
$q_j = 1-p_j$, and define the **odds** $r_j = p_j/q_j$. Bruss's Odds-theorem (2000, Theorem 1) states: an optimal rule for stopping on the *last* index
$k$ with $I_k=1$ exists, and it is to stop on the first success at or after

$$s = \sup\Big\{1,\ \sup\Big\{1\le k\le n : \sum_{j=k}^n r_j \ge 1\Big\}\Big\}.$$

The optimal win probability is $V(n) = \big(\prod_{j=s}^n q_j\big)\big(\sum_{j=s}^n r_j\big)$.

Operationally (the **Odds-algorithm**): list $q_j, r_j$ from the last trial
backward; accumulate $R_k = r_n + r_{n-1} + \dots + r_k$; stop accumulating
at the first $k$ where $R_k \ge 1$ — call it $s$ — and from then on commit
to the first success encountered. The value follows from the matching
running product of the $q_j$.

## Why it matters

The rule needs nothing about the $p_j$ beyond independence and their exact
values — no ranks, no records, no distributional family. Bruss re-derives
the classical secretary problem's threshold and $1/e$ asymptote as the
special case $r_k = 1/(k-1)$ (independent "new-record" indicators among $n$
ranked candidates), and the same closed form applies unchanged to unequal,
arbitrary per-step probabilities, to a random horizon via an inhomogeneous
Poisson-arrival intensity, and to a group-interview variant (stopping on the
last group containing the overall best across several batches, matching
Hsiau & Yang's dynamic-programming solution). It answers "when to commit"
for the sub-case of stall 2 where the sequence of opportunities is
exogenously ordered and only the *stopping point* is chosen against a known
horizon — distinct from the ranking/EIG comparisons already on the map,
which order an unordered set rather than time a fixed one.

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (Bruss 2000) | Odds-theorem, Odds-algorithm | exact |
| Later optimal-stopping literature | Bruss' odds algorithm, Bruss algorithm | exact — same threshold-index rule, same value formula |
| Optimal stopping (Bruss 1984) | 1/e-law | **not this concept** — a different theorem for an *unknown* number of trials; Bruss (2000) states explicitly that this law "does not follow from the Odds-theorem" |
| Classical secretary problem | (no separate name in this paper) | **not an alias** — the $l=1$, record-indicator special case of this rule, with its own separate literature not read in this pass |

## Transfer

| | |
|---|---|
| Home field | Optimal stopping over a sequence of **independent** indicator trials with a **known** horizon $n$ (or known intensity, for the continuous-time version) |
| Here | A sequence of remaining opportunities to accept an answer or candidate, each with a known, distinct probability of being "good enough," where only the *last* such success within a fixed budget may be captured |
| What survives | The threshold-and-summed-odds computation is exact and cheap: only the aggregate of remaining per-step probabilities matters, not the full joint history |
| What does not | Independence. An asking procedure whose later answer quality depends on earlier answers (the usual case once context accumulates) breaks the theorem outright — Bruss's own generalizations (Poisson arrivals, group interviews) all keep independence, they never relax it |

## Limits

Requires exact, known $p_j$ for every remaining trial and independence
across trials; the horizon $n$ (or $T$, in the continuous-time form) must be
known in advance. Bruss's own extension to stopping on the $l$-th-last
success (his §2.2) shows the closed form is special to $l=1$: for $l>1$,
summing odds to the target $l$ is only an approximate rule, not exact,
because the exact threshold needs the more complex identity
$s_2 = \sup\{1,\sup\{k : R_k - R_k^{(2)}/R_k \ge 2\}\}$ for $l=2$ and grows
in complexity with $l$.

## Related

[[reversibility]] · [[sprt]] · [[value-of-information]] · [[bounded-rationality]]

[^s1]: bruss-2000
