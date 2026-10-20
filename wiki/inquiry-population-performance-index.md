---
description: "A Cobb-Douglas index multiplies a population's inquiry volume, topic diversity and frontier share, so raising one factor alone cannot raise the score."
aliases: ["population-performance index", "inquiry ecosystem index", "curiosity ecology index"]
sources: ["monosov-2026"]
---
# Inquiry population-performance index

> When many agents share a question-asking budget, more questions is not the
> same as better questions: a group that floods one topic or avoids the
> frontier can ask a great deal and still fail to grow what is known.

## Definition / Mechanism

For a population of agents sharing a knowledge landscape, three quantities
are tracked at each time $t$: query volume $Q_t = \sum_q \sum_i P_i(q,t)$ (total
pursuit mass), topic diversity $D_t$ (the normalized [[entropy|Shannon entropy]] of that
mass across $K$ mutually exclusive topics, $0$ when concentrated on one topic
and $1$ when spread evenly), and frontier share $F_t$ (the fraction of
inquiry aimed at the [[question-generativity|generativity]]-defined frontier set).[^c1]

These combine into a population-performance index
$R_t^S = A_S\, Q_t^{a_Q}(\epsilon_D+D_t)^{a_D}(\epsilon_F+F_t)^{a_F}$, explicitly modelled on a
Cobb–Douglas production function, with small floors $\epsilon_D,\epsilon_F>0$
so the index does not collapse to zero when one factor is exactly zero. Because
the terms multiply rather than add, more volume raises the index only when it
is not offset by losses in diversity or frontier-directed effort: for small
proportional changes $\Delta\log R_t^S = a_Q\Delta\log Q_t + a_D\Delta\log D_t + a_F\Delta\log F_t$.[^c2]

## Why it matters

On this stall's question of which axis to pursue first, the notes already
present score a *single* candidate question. This index scores a *population's
whole distribution* of choices at once, and formalizes why maximizing any one
factor (asking more, or diversifying topics, or chasing only the frontier) at
the expense of the others can leave a shared knowledge stock no better off —
a multi-agent generalization the single-question criteria on this stall do
not address.

## Transfer

| | |
|---|---|
| Home field | growth macroeconomics — the Cobb–Douglas production function (Cobb & Douglas 1928), aggregating capital and labor multiplicatively into output |
| Here | aggregating a population's inquiry volume, topic diversity and frontier share into one health-of-the-ecosystem number |
| What survives | the multiplicative, complementarity structure — each factor must be present for the index to be high, one factor cannot fully substitute for another |
| What does not | no estimated exponents or scale constant; the production-function's economic interpretation (returns to scale, factor shares as economic quantities) does not carry over — the paper calls it an inspiration, not a fitted model |

## Limits

The index is defined but never computed on real or simulated inquiry data in
the source; $A_S$, $a_Q$, $a_D$, $a_F$, $\epsilon_D$, $\epsilon_F$ are free
parameters with no fitting procedure given. Topic diversity by Shannon entropy
"measures spread across topics but not semantic distance between them," so two
populations asking about near-identical topics under different labels would
score as diverse. The index rests entirely on [monosov-2026], a single-author
conceptual preprint not yet independently checked.

## Related

[[question-generativity]] · [[curiosity-value-function]] · [[mutual-information]] · [[value-incommensurability]]

[^c1]: monosov-2026 — "Second, topic diversity measures how evenly that mass is spread across K topics ω"
[^c2]: monosov-2026 — "The index is inspired by a Cobb–Douglas form (Cobb and Douglas, 1928):"
