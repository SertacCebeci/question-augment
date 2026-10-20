---
description: "A constraint set can be fully satisfied by a mapping that swaps concept values yet violates nothing; discrimination (no valid transposition) is necessary but not sufficient to rule this out."
aliases: ["reasoning shortcuts"]
sources: ["arxiv-2604-23377"]
---
# Reasoning shortcut

> A constraint set that every check passes can still have eight solutions
> instead of one — satisfying every constraint is not the same claim as
> pinning down the mapping the constraints were meant to fix.

## Definition / Mechanism

Fix a set of neural outputs $N$, concept labels $S$, constraints $C$ over
mappings $\phi: N \to S$, and the intended mapping $\phi^*$. The set of
valid mappings is $\Phi_C = \{\phi : N \to S \mid \phi \text{ satisfies all
constraints in } C\}$. A valid mapping $\phi \in \Phi_C$ is a **reasoning
shortcut** if $\phi \neq \phi^*$; the problem is **shortcut-free** iff
$|\Phi_C| = 1$. The **shortcut multiplicity** is $SM(C) = |\Phi_C| - 1$.
In the motivating example — four neural outputs mapped to digits 0–3 under
two sum constraints — 8 distinct bijections satisfy both constraints, and a
network may converge on any of them; the constraint graph's two
disconnected components let each side's swap combine independently.[^c1]

**Discrimination is necessary but not sufficient.** $C$ is *discriminative*
if no valid $\phi$ can be transposed at two labels ($\phi_{s_i \leftrightarrow
s_j}$) and remain valid. If $P$ is shortcut-free then $C$ is discriminative
— shortcut-freeness leaves only $\phi^*$, and every transposition of
$\phi^*$ differs from it, so no transposed mapping can also be in $\Phi_C$.
 But discrimination does not imply shortcut-freeness: a constraint graph
can be connected and reject every 2-cycle (pairwise swap) while still
admitting shortcuts through longer permutation cycles — modulo-arithmetic
constraints exhibit exactly this rotational symmetry. Constraint-graph
connectivity is likewise not sufficient on its own; whether connectivity
and constraint strength jointly suffice for uniqueness is stated as open.
[^c3]

**Complexity.** Given a constraint-based problem and $\phi^*$: deciding
shortcut-freeness is coNP-complete, counting shortcuts ($SM(C)$) is
#P-complete, and finding a minimal repair (fewest added pinning constraints
that eliminate all shortcuts) is NP-hard.[^c4]

**Disambiguation by labels.** When constraints alone leave $k = SM(C) \geq
1$ shortcuts, let $\Delta_C$ be the set of positions where some pair of
valid mappings disagree and $r = |S|$. Any adaptive learner needs at least
$\lceil \log_r(k+1) \rceil$ label queries to identify $\phi^*$; querying
every position in $\Delta_C$ always suffices, using at most $|\Delta_C|
\leq r$ queries. The lower bound is achieved when the candidate set splits
evenly at each query; the upper bound when each query eliminates only one
candidate.[^c5]

## Why it matters

"The learned concepts satisfy every constraint" is not evidence the
concepts are the intended ones: the constraint set can be simultaneously
consistent and multiply-satisfiable, so a system can pass every
consistency check on the market and still have the wrong
concept-to-label wiring. Discrimination gives a cheap necessary test to
rule out the simplest failure (pairwise swaps) before the harder question
— full uniqueness — is asked at all.

## Limits

- The framework assumes constraints over concept mappings are explicit
  (Definition 1's tuple); systems whose constraints are implicit in
  learned representations fall outside it.[^c6]
- Results are stated for $|N| = |S|$ with $\phi^*$ restricted to
  bijections; non-bijective shortcuts are excluded by that restriction
  when $|\Phi_C| > 1$, so the count and complexity results are for the
  bijective case specifically.
- Sufficient conditions for shortcut-freeness beyond discrimination
  remain open — the note reports what discrimination rules out, not a
  complete characterization.
- One source read; the complexity proofs are cited here by result, not
  independently checked.

## Related

[[k-underspecified-csp]] · [[max-sat-backbone]] · [[conflict-driven-clause-learning]] · [[np-completeness]]

[^c1]: arxiv-2604-23377
[^c3]: arxiv-2604-23377 — "discrimination holds yet shortcuts persist via longer permutation cycles, even with a connected constraint graph"
[^c4]: arxiv-2604-23377 — "deciding shortcut-freeness is coNP-complete, counting shortcuts is #P-complete, and finding minimal repairs is NP-hard"
[^c5]: arxiv-2604-23377 — "Lower bound: Any learner requires at least ⌈logr (k + 1)⌉ queries to identify ϕ∗ . 2. Upper bound: Querying all positions in ∆C identifies ϕ∗ using at most |∆C | ≤ r queries."
[^c6]: arxiv-2604-23377 — "A constraint-based neurosymbolic learning (NSL) problem is a tuple P = (N, S, C, ϕ∗ , D)"
