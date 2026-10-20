---
description: "Eliminate a detected shortcut by pinning one disagreeing position to its intended value and re-verifying, repeating; provably converges in at most k iterations but not to a minimal fix."
aliases: ["greedy shortcut repair"]
sources: ["arxiv-2604-23377"]
---
# Greedy pinning repair

> Each repair step buys exactly one bit of resolution — pin one position
> where the current shortcut disagrees with the intended mapping — and the
> multiplicity strictly drops each time, so the loop cannot run longer than
> the number of shortcuts it started with.

## Definition / Mechanism

Given a [[reasoning-shortcut|constraint set with shortcuts]] $C$ and the
intended mapping $\phi^*$ (required to already satisfy $C$), the repair
loop runs a verification pass, and on each iteration where it finds a
shortcut $\phi_{sc}$: computes the disagreement set $D_{sc} = \{n \in N :
\phi^*(n) \neq \phi_{sc}(n)\}$, picks one position $n^* \in D_{sc}$, and
adds the unary **pinning constraint** $\phi(n^*) = \phi^*(n^*)$ to $C$.
Verification re-runs against the augmented set until it returns
shortcut-free or a timeout budget $T$ is exhausted.[^c1]

**Correctness.** Let $C_0 = C$ and $C_i$ the constraint set after
iteration $i$, with $\phi^* \in \Phi_{C_0}$, $|\Phi_{C_0}|$ finite, and
$T \geq k$ where $k = SM(C_0)$. Then: (1) the shortcut multiplicity
strictly decreases each iteration that adds a constraint — the detected
shortcut $\phi_{sc}$ violates the new pinning constraint by construction,
so it is removed from $\Phi_{C_{i+1}}$ while $\phi^*$ still satisfies it;
(2) $\phi^*$ remains valid at every step, since the pinning constraint is
built from $\phi^*$'s own value at $n^*$; (3) the loop terminates in at
most $k$ iterations at a shortcut-free set; (4) the algorithm does **not**
minimize the number of constraints added — it is greedy, not optimal.
[^c2]

**Optimal repair is intractable.** Finding a minimal set of pinning
constraints (drawn from a fixed library, each pinning one or more
positions) that eliminates every shortcut is NP-hard — which is exactly
why the method settles for a greedy, provably-terminating but
suboptimal fix rather than searching for the smallest one.[^c3]

The verification sub-routine that the loop calls at every iteration
compiles the constraint set to Answer Set Programming: neural outputs and
concepts become domain atoms, bijectivity is enforced by cardinality
constraints, each task constraint becomes an integrity constraint, and
$\phi^*$ is excluded so that a full-enumeration ASP solve (e.g. `clingo
--models=0`) returns either an empty answer set (shortcut-free) or every
remaining valid mapping (each one a shortcut) — with proven soundness and
completeness.[^c4]

## Why it matters

A repair loop that is merely "add constraints until the checker stops
complaining" gives no guarantee it terminates or that it never contradicts
the answer it is trying to protect. Building the new constraint directly
from $\phi^*$'s own value at the chosen position guarantees both:
termination is bounded by the shortcut count going in, and the intended
mapping can never be pinned out by its own repair.

## Limits

- Convergence to zero multiplicity is guaranteed; convergence to a
  *minimal* or *small* repair is not — the method is explicitly
  suboptimal (part 4 of the correctness result), and minimal repair is
  NP-hard, so no efficient method can promise both.[^c3]
- The precondition $\phi^* \in \Phi_{C_0}$ is required going in; if it
  fails, the underlying verification step reports the mapping itself is
  invalid rather than repairing anything.
- Reported experiments show full elimination in 6 of 8 benchmark domains
  within the iteration bound, consistent with repair difficulty varying
  sharply by domain even though termination itself is guaranteed.
- One source read; not independently benchmarked here.

## Related

[[reasoning-shortcut]] · [[conflict-driven-clause-learning]] · [[max-sat-backbone]]

[^c1]: arxiv-2604-23377
[^c2]: arxiv-2604-23377
[^c3]: arxiv-2604-23377 — "finding minimal repair is NP-hard"
[^c4]: arxiv-2604-23377
