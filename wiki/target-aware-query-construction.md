---
description: "A query selector that can see the true target has a per-round belief-alignment advantage of order sqrt(d) over any selector limited to its own belief, including information gain and volume removal."
aliases: ["target-awareness separation", "teacher-guided query construction"]
sources: ["mirenzi-2026"]
---
# Target-aware query construction

> Which criterion selects the next question usually assumes the asker
> cannot see the answer in advance. When one party can — a teacher who
> knows the target reward — that assumption itself has a measurable,
> dimension-dependent cost for everyone who lacks it.

## Definition / Mechanism

In a linear reward model $r(\xi)=x\cdot\psi(\xi)$ with unknown weight
$x^*\in S^{d-1}$ and a belief $B_t$ over it, both a belief-only selector
and a target-aware selector reduce to the same primitive: propose a
halfspace direction $a$ and score it by the belief mass it removes. They
differ only in what the scorer can see. Proposition 1 (Mirenzi & Admoni):
in the isotropic early-round regime, every rule selecting $a$ as a
function of the belief alone — including expected information gain and
volume removal, which the paper shows reduce to the same balanced-cut
family under a noiseless oracle — achieves expected per-round alignment
gain $E[\Delta\phi_t]=\Theta(1/d)$; a target-constructed query, such as a
counterfactual direction toward $x^*$ with $|a\cdot x^*|=\Theta(1)$,
achieves $E[\Delta\phi_t]=\Theta(1/\sqrt d)$. The target-aware advantage is
therefore a factor $\Theta(\sqrt d)$ per round, growing with feature
dimension; over $T$ rounds a belief-only learner needs $\Theta(\sqrt d)$
more queries to match the teacher's early-phase progress.[^c1]

## Why it matters

This gives a dimension-dependent answer to "does it matter who selects
the query" on the selection stall: for reward/preference dimensions large
enough that most of the teaching budget is spent in the early, low-information
regime, a selector with access to the target dominates any criterion —
including this wiki's own [[expected-information-gain]] and
[[volume-removal]] — restricted to the current belief, by a growing
margin, not a constant one. The gap is not about which belief-only
criterion is used; it is about whether the target is visible to the
selector at all.[^c2]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Rate analysis of active/query-based learning under a halfspace (linear separator) hypothesis class, with a Gaussian surrogate for the belief covariance | Compares two families of query-selection rules on the wiki's own stall-2 axis: belief-only (EIG, volume removal) versus target-aware |
| Survives | The asymptotic separation $\Theta(1/d)$ vs $\Theta(1/\sqrt d)$ as a function of the *information available to the selector*, and the reduction of information gain / volume removal to one balanced-cut family under a noiseless oracle | |
| Does not survive | The result is stated only for the early-round, isotropic-belief regime ($t\ll d$) and a linear reward on the unit hypersphere; it does not describe later rounds once the belief itself becomes informative, nor any non-linear or non-halfspace query space | |
[^c3]

## Limits

The separation is proven under a Gaussian surrogate for the particle
belief (Appendix A of the source, not reproduced here) and an isotropic,
early-round assumption ($t\ll d$, $C_t\approx \tfrac1d I_d$); the paper's
own two-point simulation ($d=20$ vs $d=40$) shows the gap widening but
does not trace the $\Theta$ rate itself, which the source leaves to an
extended version. The result also assumes a noiseless preference oracle;
Remark 1's reduction of information gain to a balanced-cut rule does not
hold once responses are noisy.[^c4]

## Related

[[understanding-statement]] · [[expected-information-gain]] · [[volume-removal]] · [[generalized-binary-search]]

[^c1]: mirenzi-2026
[^c2]: mirenzi-2026 — "Information gain and volume removal therefore select from the same balanced-cut family and fall under Proposition 1(i)."
[^c3]: mirenzi-2026 — "Proposition 1 (Target-awareness separation). Let x∗ be drawn uniformly on S d−1 (as in our trials) and consider the isotropic early-round regime (t ≪ d, so Ct ≈ d1 Id and x̄t ≈ 0) under the surrogate of Appendix A."
[^c4]: mirenzi-2026 — "Two dimensionalities do not trace the Θ rates; a gap-versus-d sweep is left to the extended version."
