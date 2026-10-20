---
description: "A label-free geometric proxy for budgeted querying is monotone submodular, so greedy selection keeps the classical (1−1/e) guarantee before any label is known."
aliases: ["ball-coverage acquisition proxy", "geometric coverage proxy", "greedy coverage subset selection"]
sources: ["khosravani-2026"]
---
# Ball-coverage acquisition proxy

> Which point to query next, decided without knowing any label: cover the
> pool with balls around the candidates and let a classical greedy
> guarantee stand in for a certification objective that only exists after
> the oracle answers.

## Definition / Mechanism

Khosravani (2026) needs to choose a budgeted query set
$S$, $|S|=k$, before any label is observed, so the ideal objective
(certified coverage, which depends on the labels revealed by $S$) cannot
be optimised directly. The proxy substitutes a purely geometric quantity:
"Fρacq (S) counts how many pool points lie within distance ρacq of at
least one selected point."[^c1]

Under a mild margin-floor assumption this radius has a certification
reading: "for any labeled center i ∈ S and any pool point u ∈ [N ] with
∥zu − zi ∥ < ρcert , we have LByi (u) > 0" — i.e. points inside the ball
are guaranteed some positive certified evidence once the center's label
is revealed, even though which class that evidence favours is not yet
known.[^c2]

Because the proxy is a set-coverage function, it is monotone submodular,
and a greedy algorithm (Algorithm 1: repeatedly add the point whose ball
covers the most still-uncovered pool points) inherits the classical
guarantee: "Fρacq is a monotone submodular function, so greedy
optimization achieves the standard (1 − 1/e) approximation guarantee."[^c3]

## Why it matters

On stall 2 this gives a rule for "which axis (pool point) to query next"
that needs no knowledge of what the answer will be and no learned scoring
model — only a fixed embedding and a radius. It sits between the informed,
label-dependent selection criteria this stall's map already carries
([[expected-information-gain]], [[generalized-binary-search]]) and pure
randomness: it optimises a stand-in objective chosen because it is
computable *before* querying, and inherits a worst-case guarantee on that
stand-in, not on the thing the asker actually wants.

## Transfer

| | Home field | Here |
|---|---|---|
| Objective | classical (non-adaptive) monotone submodular set coverage, Nemhauser–Wolsey–Fisher greedy | choosing which pool point to query so a downstream certificate can later force more labels |
| What survives | the $(1-1/e)$ guarantee, unconditionally, since it needs no assumption about labels at all — only that the proxy itself is a coverage function | |
| What does not | any claim that maximising the proxy maximises actual certified coverage; the paper states the two are not equal | |

## Limits

- The guarantee is on $F_{\rho_{acq}}(S)$, the geometric proxy, and not on
  certified coverage, which the source states are generally unequal:
  "Fρacq is generally not equal to certified coverage. Its purpose is
  instead to provide a simple pre-query surrogate that captures the
  locality structure of propagation and admits optimization guarantees."
  A budgeted-querying method that optimises this proxy is optimising a
  bound-carrying stand-in, and the gap between the two is not itself
  bounded here.[^c4]
- The radius $\rho_{acq}$ is a hyperparameter; the certification-linked
  reading only holds when $\rho_{acq}=\rho_{cert}=\gamma/L_{max}$ under
  the margin-floor assumption (Assumption 2 in the source), which is an
  additional condition beyond monotone submodularity.
- It ignores class identity and competition entirely (no upper-envelope
  elimination is modelled): two points covering the same ball may end up
  supporting different, conflicting classes once labels arrive.

## Related

[[adaptive-submodularity]] · [[generalized-binary-search]] · [[expected-information-gain]] · [[lipschitz-consistent-version-space]]

[^c1]: khosravani-2026 — "Fρacq (S) counts how many pool points lie within distance ρacq of at least one selected point."
[^c2]: khosravani-2026 — "for any labeled center i ∈ S and any pool point u ∈ [N ] with ∥zu − zi ∥ < ρcert , we have LByi (u) > 0"
[^c3]: khosravani-2026 — "Fρacq is a monotone submodular function, so greedy optimization achieves the standard (1 − 1/e) approximation guarantee."
[^c4]: khosravani-2026 — "Fρacq is generally not equal to certified coverage. Its purpose is instead to provide a simple pre-query surrogate that captures the locality structure of propagation and admits optimization guarantees."
