---
description: "Multi-turn information seeking formalized as a CSP in which k jointly-necessary variables, not one, must be assigned before the target variable becomes known."
aliases: ["k-MSS", "minimal k-sufficient set"]
sources: ["huang-2026"]
---
# K-underspecified CSP

> Selection is not "which one variable is missing" but "which variable to
> query next out of a set of k that are jointly required" — and k, not 1, is
> the ordinary case.

## Definition / Mechanism

A problem is a tuple $P = \langle X, D, C, A, Y \rangle$: $X$ a set of
variables with domains $D$, $C$ a set of logical constraints over them, $A$
an observed partial assignment, and $Y$ the target variable. The feasible
space $\Omega(P)$ is the set of full assignments consistent with both $C$
and $A$ — the states still possible given what is known. $Y$ is *known*
under $A$ when every assignment in $\Omega(P)$ agrees on $Y$; otherwise the
problem is *underspecified*.[^c1]

Writing $U(P)$ for the queryable variables (unassigned, not the target), a
subset $S \subseteq U(P)$ is *sufficient* if assigning it always fixes $Y$.
$S$ is a **minimal $k$-sufficient set (k-MSS)** if it is sufficient, has
size $k$, and no smaller subset of $U(P)$ is sufficient; $k$ is the
problem's degree of underspecification. Because $k$ is the worst case over
every possible target value, a single task instance — one fixed hidden
target $y$ — can require strictly fewer queries than the problem's $k$: e.g.
distinguishing four candidate animal classes needs a 3-MSS, but the
instance whose target is the one candidate with gills is separated by one
query alone.[^c2]

At each turn $t$ the asker selects $X_t \in U(P)$, an oracle returns $x_t$,
and the assignment updates to $A_{t+1} = A_t \cup \{X_t = x_t\}$; the
interaction ends when the asker commits to an answer. Prior single-variable
formulations of underspecified reasoning (cited by the source as prior
work) are the special case $k = 1$, where one query always suffices; this
formalization generalizes that case to $k$ jointly-[[backbone-of-a-formula|necessary variables]]
queried sequentially.[^c3]

## Why it matters

The CSP gives axis selection a ground truth independent of any model's own
report: whether a queried variable belongs to the k-MSS, and whether the
accumulated assignment already fixes $Y$, are both computable from $C$ and
$A$ alone, not from the asker's stated reasoning. This is what makes it
possible to separate "did the asker ask the right variables" from "did the
asker answer correctly" ([[final-sufficiency]]) instead of scoring only the
combined outcome.

## Limits

- The formalization assumes $X$, $D$ and $C$ are given and finite; it says
  nothing about how an asker without access to $C$ would discover which
  variables exist (stall 1, axis discovery) — the four structured domains
  built on it hand the model a predefined, finite $U(P)$.
- The worst-case degree $k$ is a property of the problem, not of any one
  task instance; a model that always queries the problem's full k-MSS is
  over-asking on task instances whose specific target needs fewer queries.
- Everything above rests on one source (huang-2026); the $k=1$ special case
  is attributed to prior work the source cites but this note has not read
  directly.

## Related

[[final-sufficiency]] · [[possible-worlds]] · [[clarification-benchmarks]] · [[sufficient-statistic]]

[^c1]: huang-2026 — "We define a problem as a tuple P = ⟨X , D, C, A, Y ⟩, where X is a set of variables with domains D, C is a set of logical constraints over these variables, A is an observed partial assignment, and Y is the target variable."
[^c2]: huang-2026 — "A set S ⊆ U(P ) is a k-MSS if it is sufficient, has a size of k, and no strictly smaller subset of U(P ) is sufficient. This value k defines the problem-level degree of underspecification."
[^c3]: huang-2026 — "Prior single-turn studies represent the special case of k = 1 [1]."
