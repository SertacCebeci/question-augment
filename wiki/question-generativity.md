---
description: "A question's generativity counts the new knowledge gaps its resolution opens relative to what the asker already knows, a second axis of value distinct from how much uncertainty it removes."
aliases: ["generativity", "knowledge-gap generativity", "frontier question"]
sources: ["monosov-2026"]
---
# Question generativity

> A question can be cheap to resolve and remove a lot of uncertainty right
> now, or it can open more questions than it closes. These are different
> axes, and a selection rule that only tracks uncertainty removed is blind to
> the second one.

## Definition / Mechanism

Generativity $g_i(q,t)$ is the number of new knowledge gaps that resolving
question $q$ opens, relative to what agent $i$ already knows — a gross count:
the one gap $q$ itself closes is not subtracted, so any question that opens
even a single new gap has $g_i > 0$. A trivia question typically closes its
own gap and opens little else, so $g_i \approx 0$; a question in a sparse
region of the knowledge landscape can answer itself and open an entire
research program.[^c1]

Generativity is explicitly not the same quantity as immediate uncertainty
reduction: a cheap question can score high on immediate value and near zero
on generativity, while a costly "frontier" question can be low on immediate
satisfaction and high on generativity, and therefore on delayed return.
Which one an agent picks depends on the relative weight it places on
immediate resolution versus long-horizon return — generativity feeds the
long-horizon term of the [[curiosity-value-function]] as $L_i^{own}(q,t) = \ell_0 + \rho_i\, g_i(q,t)$.[^c2]

At the population level the same idea, evaluated against a shared knowledge
stock rather than one agent's knowledge, defines a frontier set: questions
whose population generativity $g_s$ exceeds a threshold $\bar g$ make up
$F_t = \{q : g_s(q,t) \ge \bar g\}$.[^c3]

## Why it matters

Every criterion already on this stall ([[mutual-information|mutual information]], EIG, adaptive
submodularity) scores a question by the uncertainty it is expected to remove.
Generativity names a distinct, independently-varying axis — what asking (and
answering) this question makes newly visible — that none of those criteria
compute, and ties it to why a selection policy might deliberately choose the
harder, less immediately satisfying question.

## Limits

Generativity is defined relative to "what the agent already knows," which
the paper does not operationalize — no procedure for counting gaps is given,
so the quantity cannot yet be computed from a real knowledge state. The
frontier-set threshold $\bar g$ is likewise left free. Both claims here are
from a single conceptual model, not measured on any dataset or system.

## Related

[[curiosity-value-function]] · [[expected-information-gain]] · [[mutual-information]] · [[adaptive-submodularity]]

[^c1]: monosov-2026 — "A second important property of a question is its generativity gi (q, t): the number of new knowledge gaps that resolving q opens, relative to what the agent already knows."
[^c2]: monosov-2026 — "Also note that a cheap question high in Ii can be near zero in gi ."
[^c3]: monosov-2026 — "Questions whose generativity gs exceeds a threshold ḡ make up the frontier set Ft : Ft = {q : gs (q, t) ≥ ḡ}."
