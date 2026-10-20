---
description: "Sequential graphical testing certifies many correlated hypotheses by propagating and recycling a significance budget along a graph, controlling family-wise error at Bonferroni's cost."
aliases: ["SGT", "sequential graphical testing", "graphical multiple testing"]
sources: ["jia-2026"]
---
# Sequential graphical testing (SGT)

> A Bonferroni correction spends its error budget once, evenly, and never
> gets any of it back; graphical testing spends it along a graph and lets
> a certified node hand its unused budget to its neighbors — a cheaper way
> to certify many hypotheses that are known to be correlated.

## Definition / Mechanism

Jia, Ye, Jia et al. (2026) apply SGT (attributed to Bretz
et al. 2009) to certify which threshold pairs on a two-dimensional lattice
keep a cascade's error rate under a target level, choosing it over a
Bonferroni correction because "neighboring threshold pairs typically
induce highly correlated routing decisions, and safe operating points
often form contiguous regions."[^c1]

Each lattice node $(i,j)$ carries a local significance budget $\delta_{i,j}$
and is certified once its one-sided exact binomial p-value falls under
that budget: "SGT maintains a local testing budget δi,j at each active
node and certifies the node whenever pi,j ≤ δi,j." The nodes form a
directed acyclic graph from each threshold pair to its "immediate relaxed
neighbors" (more permissive threshold pairs); once a node is certified,
its remaining budget is transferred forward: "Once node (i, j) is
certified, its budget is transferred to uncertified successors." Two
diffusion rules are compared — Uniform Grid Diffusion splits budget evenly
among successors, Diamond-Wavefront Diffusion gives equal accumulated
budget to every node the same total relaxation away from the start — and
because the graph is acyclic the budget update can be applied once per
node in order.[^c2]

The procedure controls the family-wise error rate over the whole certified
set, which is what licenses picking any point from that set — including
the best-looking one — after the fact: "Since the final threshold pair
will be selected adaptively from all certified candidates, we require
family-wise error rate (FWER) control at level δ... any later choice from
[the certified set], including the acceptance-maximizing one, remains
valid."[^c3]

## Why it matters

Most of this wiki's stopping and escalation rules test one threshold. SGT
is a formalism for the case a cascade actually needs: many candidate
operating points that are not independent, where testing each alone at
Bonferroni's per-test budget would certify almost none of them, but
testing them as a graph and recycling unused budget certifies a usable
region without inflating the false-certification rate.

## Transfer

| | |
|---|---|
| **In its home field** | Multiple-testing / clinical-trial statistics (Bretz et al. 2009): propagate a fixed overall significance budget through a graph of hypotheses, transferring a rejected hypothesis's unused budget to its successors, to control family-wise error across a correlated hypothesis family |
| **Here** | Each hypothesis is "this threshold pair's selection-conditioned error exceeds α"; the graph is the partial order of threshold pairs by how permissive they are |
| **What survives** | The family-wise error guarantee over the whole certified set, so a downstream rule may pick any certified point (including the best one) without spending further budget |
| **What does not** | Bretz et al.'s original clinical-trial hypothesis structure and edge weights — the routing-lattice graph and its two diffusion rules (UGD, DWD) are `jia-2026`'s own construction, and this note has not read Bretz et al. (2009) directly to check what else does or does not transfer |

## Limits

The p-value computation assumes the per-node accepted-error count is
binomially distributed conditional on the accepted count,
$K_{i,j}\mid M_{i,j}\sim \mathrm{Bin}(M_{i,j}, R(\lambda_{i,j}))$, which
needs i.i.d. [[calibration]] examples; this note took the FWER guarantee
(the source's Theorem 1) from `jia-2026`'s statement and appendix pointer,
not from re-deriving it or from reading Bretz et al. (2009) itself, so the
general SGT procedure is reported only as `jia-2026` uses it.

## Related

[[balancerag]] · [[crc-confident-error-control]] · [[abstention]]

[^c1]: jia-2026 — "neighboring threshold pairs typically induce highly correlated routing decisions, and safe operating points often form contiguous regions."
[^c2]: jia-2026
[^c3]: jia-2026
