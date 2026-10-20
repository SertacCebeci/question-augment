---
description: "Asking through a fixed-cost, symmetric-error channel strictly beats every no-query rule whenever the query's cost plus channel error falls below the no-query Bayes error."
aliases: ["bounded-cost clarification theorem"]
sources: ["hossain-2026"]
---
# Clarification channel theorem

Hossain, Shayoni & Morol (2026) prove a closed-form
condition for when a clarifying question is worth its cost, framed as a
three-action decision problem — accept, reject, or ask — over a binary
latent label $Z$ (genuine revision vs. adversarial claim). Asking costs a
fixed $\kappa$ and returns a noisy answer through a binary symmetric channel
of error $\varepsilon$. Writing $e$ for the pointwise Bayes error of the best
no-query rule given a sub-$\sigma$-algebra $G$ of observed evidence, the
optimal restricted policy asks exactly where the no-query error exceeds the
query's own cost:

> "Consider policies that ask on a G-measurable set and, having asked, act on
> Z̃. Within that class the optimal policy asks on Qκ = {e > κ + ε}... Its
> risk is R∗κ = Em[min{e, κ + ε}] ≤ R∗ = Em[e]... In particular, always
> asking beats every no-query rule when κ + ε < ½(1 − TV(Pg|G, Pα|G))."[^c1]

Restricting attention to policies that act on the noisy answer alone (rather
than jointly with the evidence $G$) only makes the *worthless-clarification*
characterization conservative, not the sufficient condition for asking:

> "Consequently R∗κ is an upper bound on the unrestricted optimum, the
> unrestricted ask region is a superset of Qκ, and the characterization of
> when clarification is worthless is a statement about the restricted class
> only. The sufficient condition Equation 23 is unaffected, since it is
> witnessed by a policy inside the class."[^c2]

The authors flag the theorem's own circularity: it assumes one fixed channel
error $\varepsilon$ for every history and every adversary, and grants the ask
channel an accuracy no function of the observed evidence need achieve —

> "We regard Theorem 4 as establishing that a bounded-cost query changes the
> achievable region, and not as evidence about how accurate real
> clarification is."[^c3]

## Transfer

| | |
|---|---|
| **In its home field** | Bayes-risk minimization over a ternary action set {accept, reject, ask} with a symmetric noisy side-channel — standard statistical decision theory |
| **Here** | Whether a personalized agent should silently write a contested memory update or ask the user to confirm it, when the true label (genuine vs. injected) is never observed |
| **What survives** | The qualitative threshold: ask whenever the marginal cost of asking ($\kappa+\varepsilon$) is below the risk of guessing without asking ($e$); conditioning on more evidence before deciding whether to ask can only shrink the no-query error and so shrink the region where asking is needed |
| **What does not** | The single global $\varepsilon$ for the clarification channel, held fixed across every history and adversary — the authors call this assumption "close to definitional" (§ Remark 5) rather than independently justified, since it defines genuineness partly through what the user confirms |

## Limits

- Holds only within the restricted policy class that decides whether to ask
  on $G$ and then acts on the noisy answer alone; the unrestricted optimum
  can do strictly better, so the stated ask set $Q_\kappa$ is a subset of
  the true ask region, not identical to it (claim[^c2]).
- $\varepsilon$ is a single fixed parameter assumed independent of the
  history and the adversary — not an estimate, and the authors themselves
  call the condition for it to help "close to definitional" rather than
  derived (claim[^c3]).
- The theorem bounds an *achievable* error region; it does not certify that
  CAPTURE's realized clarification (precision 0.79 / recall 0.70 in the same
  paper) attains that bound.
- `hossain-2026` [?] is a September 2026 arXiv preprint, unverified beyond
  this extract.

## Related

[[value-of-information]] · [[authenticity-gate]] · [[sprt]] · [[bayesian-experimental-design]]

[^c1]: hossain-2026
[^c2]: hossain-2026
[^c3]: hossain-2026 — "We regard Theorem 4 as establishing that a bounded-cost query changes the achievable region, and not as evidence about how accurate real clarification is."
