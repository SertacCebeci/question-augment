---
description: "How much of a belief's support structure survives compression is a regulated variable, set per cycle from stakes and learned history, not a fixed threshold — too little or too much both cost utility."
aliases: []
sources: ["arxiv-2604-16434"]
---
# Consequence-sensitive support resolution

> The right amount of support to keep is not a fixed threshold — it is a
> variable the system sets each cycle, and setting it too high costs as
> much as setting it too low.

## Definition / Mechanism

Walsh (2026) treats [[action-sufficient-compression|support
sufficiency]] not as a one-shot exact-or-ε compression but as a **regulated
variable across a recurrent loop**. At each cycle, active constraint fields
compose into a hypothesis geometry $H_t$; the system does not carry $H_t$
forward but compresses it, at a chosen resolution $\rho_t$, into a support
code $S_t^{\rho_t}$ alongside a selected content state $X_t$. The resolution
itself is set by a policy over three inputs — current hypothesis geometry,
arbitration memory $M_t$ (what prior cycles learned about which resolution
sufficed), and current consequence geometry $\mathcal Z_t$ (the stakes and
policy options in play): "We allow the system to regulate its current
support resolution, denoted ρ𝑡, as a function of current hypothesis
geometry, arbitration memory, and consequence geometry: ρ𝑡 = Γ(𝐻𝑡, 𝑀𝑡, 𝒵𝓉)."[^c1]

Resolution is set by a bounded objective trading policy utility against two
costs — the resource cost of finer support and a **fragmentation cost**:
"𝜌𝑡∗ = arg max [𝐸(𝑈(𝜋𝑡) ∣∣ 𝒵𝓉, 𝑀𝑡) − 𝜆res 𝐶res(𝜌) − 𝜆frag 𝐶frag(𝜌, 𝑀𝑡)]."[^c2]
This yields two named, opposite failure modes rather than one. Too coarse a
resolution collapses cases that call for different policies into one
arbitration state (**under-resolution**: verification under-allocated,
abstention fails to trigger). Too fine a resolution preserves distinctions
the current stakes do not need, splitting similar cases across narrow
support-conditioned contexts and slowing arbitration memory's learning
(**over-partitioning**) — a cost that a static sufficiency criterion, which
only asks whether a compression is fine enough, cannot see at all. The paper
states the resulting ordered prediction directly: "Adaptive controllers that
regulate support resolution outperform all fixed-resolution controllers in
cumulative utility. Agile adaptive control outperforms sluggish adaptive
control. Fixed high-resolution control achieves the best commitment accuracy
but still trails both adaptive controllers because resource cost and
learning fragmentation offset the gains from richer support retention."[^c3]

A minimal repeated-interaction simulation (binary latent state, two-to-three
Gaussian evidence channels, five controller types) confirms the ordering:
agile-adaptive > sluggish-adaptive > fixed-high > fixed-mid > fixed-low on
cumulative utility across ten seeds, even though fixed-high wins on raw
commitment accuracy. That dissociation is the paper's direct evidence for
over-partitioning as a real cost, not merely a theoretical one: "The
high-resolution controller achieved the best commitment accuracy overall, at
approximately 0.872 … Yet this gain in accuracy did not translate into the
highest cumulative utility. The high-resolution controller paid for its
richer support retention through persistent resource cost and more
fragmented support-conditioned learning."[^c5]

## Why it matters

A sufficiency criterion that only asks "is this compression fine enough"
(as in exact or ε-action-sufficient compression) has nothing to say once it
is fine enough — more resolution looks free. This framework adds the other
side: past the point the current stakes need, finer support is not neutral,
it actively degrades the learner that consumes it. A system deriving how to
compress gathered constraints needs both bounds, and needs to reset the
target as stakes and memory change, not fix it once.

## Limits

- Single-author preprint continuing the same author's own prior series
  (cited here as "Walsh 2026a", "Walsh 2026b" — not yet archived in this
  wiki; recorded as citation terms below); the framework is presented as an
  extension of that series' own Constraint Geometry proposal, not an
  independent replication.
- The simulation's adaptive controllers are "idealized and oracle-informed
  with respect to current stakes" — the paper is explicit that learning the
  resolution-control policy $\Gamma$ from experience is not shown, only that
  regulating resolution (when the regulator already knows the stakes) beats
  poorly matched fixed resolution.
- Five controller types, one minimal binary-latent-state task, ten seeds —
  no claim of generality across task structure is made or checked here.

## Related

[[action-sufficient-compression]] · [[bounded-rationality]] · [[information-bottleneck]] · [[rate-distortion-theory]] · [[sufficient-statistic]]

[^c1]: arxiv-2604-16434 — "We allow the system to regulate its current support resolution, denoted ρ𝑡 , as a function of current hypothesis geometry, arbitration memory, and consequence geometry: ρ𝑡 = Γ(𝐻𝑡 , 𝑀𝑡 , 𝒵𝓉 )."
[^c2]: arxiv-2604-16434 — "𝜌𝑡∗ = arg max [𝐸( 𝑈(𝜋𝑡 ) ∣∣ 𝒵𝓉 , 𝑀𝑡 ) − 𝜆res 𝐶res (𝜌) − 𝜆frag 𝐶frag (𝜌, 𝑀𝑡 )]."
[^c3]: arxiv-2604-16434 — "Adaptive controllers that regulate support resolution outperform all fixed-resolution controllers in cumulative utility. Agile adaptive control outperforms sluggish adaptive control. Fixed high-resolution control achieves the best commitment accuracy but still trails both adaptive controllers because resource cost and learning fragmentation offset the gains from richer support retention."
[^c5]: arxiv-2604-16434 — "The high-resolution controller achieved the best commitment accuracy overall, at approximately 0.872, compared with 0.852 for the fixed mid controller and 0.839 for the fixed low controller. Yet this gain in accuracy did not translate into the highest cumulative utility. The high-resolution controller paid for its richer support retention through persistent resource cost and more fragmented supportconditioned learning."
