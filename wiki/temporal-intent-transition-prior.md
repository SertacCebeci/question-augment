---
description: "A confidence-gated Bayesian-network prior over next-turn user intents, learned offline and injected into the system prompt to bias generation toward anticipated intents."
aliases: ["T-BN", "Temporal Bayesian Network intent prior", "BN-guided proactive generation", "TemporalBNReasoner"]
sources: ["arxiv-2604-27379"]
---
# Temporal intent-transition prior

> A next-intent forecast, learned once from transcripts and re-derived
> at inference from one utterance, tells the generator what to volunteer
> before the user asks for it.

## Definition / Mechanism

Luo (2026) builds the prior in two offline steps and
applies it at inference in two more. Offline: every USER turn's intent
label is normalized to an Action-Object form and packed into a binary
turn-intent matrix; consecutive turns are then lifted into lagged triples
$(x_t, x_{t+1}, \rho_t)$, where $\rho_t$ buckets the turn's position in
the dialogue into early/mid/late.
[^c1]

A Bayesian network is structure-learned
over these $2K+3$ variables with NOTEARS under a tabu-edge constraint that
forbids any edge running from $t+1$ back to $t$, so the graph is
forward-only by construction rather than by convention; a Bayesian
estimator with a BDeu prior then fits the conditional probability tables.
[^c2]

At inference, the current utterance is embedded and matched by cosine
similarity to the top-$k=5$ intent nodes, which are set as evidence;
variable elimination on the network yields a posterior over next intents,
which a confidence threshold ($P>0.5$) gates down to the few intents
worth surfacing — "preventing the LLM from volunteering low-confidence or
irrelevant suggestions."
[^c3]

The surviving intents are formatted as a
causal-insight block and prepended to the system prompt, so the
underlying language model is never fine-tuned; two guards keep the block
from dominating the turn: an empty gate emits no block, and the block is
explicitly subordinate to the user's stated request.
[^c4]

## Why it matters

The prior is evaluated on two separated tracks. Stripped of any
generator (ground-truth replay against actual next intents), it raises
cumulative intent-coverage AUC over 200 dialogues from 0.742 to 0.856 and
cuts the turns needed to reach 75% coverage from 3.95 to 2.73.
[^c5]

As a
next-intent predictor by itself, conditioning on the current turn's
intent (rather than only its unconditional frequency) buys a further
+24.9% relative MRR over a lag-free marginal baseline, and beats a
literal bigram-on-intents baseline, which the paper attributes to bigram
contexts being too sparse to estimate reliably.
[^c6]

The mechanism is
therefore a proactive-dialogue analogue of a stopping/selection rule:
instead of deciding when to ask or what to ask, it decides what to
volunteer next, scored by a learned, thresholded transition posterior
rather than by a hand-written recommendation rule.

## Limits

- Ground-truth replay (Track B) compares BN predictions directly to the
  actual next intent with no LLM call in the loop; the end-to-end
  effect on a generated response — as opposed to the abstraction's
  own predictive fidelity — is reported by the authors themselves as
  smaller than the Track A gain, and is not quantified in this extract
  beyond the replay numbers.
- Recall@5 is far from uniform across the 8 intents: four intents reach
  a perfect 1.00 while `book-train` reaches 0.00 and `book-hotel` 0.36,
  attributed to data sparsity on rare transitions — the aggregate MRR
  and Recall@5 hide this per-intent floor.
- The vocabulary is fixed at $K=8$ canonical intents mined from a single
  corpus (MultiWOZ 2.2) under ground-truth intent labels, not a live
  intent classifier; how the gate behaves under noisy or open-vocabulary
  intent detection is not established here.
- The confidence threshold ($\tau=0.5$) and top-$k$ ($k=5$) are reported
  as fixed settings, not shown to be tuned or swept in this extract.

## Related

[[proact-architecture]] · [[expected-information-gain]] · [[bounded-rationality]]

[^c1]: arxiv-2604-27379
[^c2]: arxiv-2604-27379 — "We learn the DAG G using the NOTEARS framework over 2K + 3 variables. To ensure physical causality, we impose a tabu-edge constraint that forbids any back-step edges (jt+1 → it )."
[^c3]: arxiv-2604-27379
[^c4]: arxiv-2604-27379
[^c5]: arxiv-2604-27379 — "The BN-guided arm raises Coverage AUC by +0.114 (from 0.742 to 0.856) and shortens the path to 75% intent coverage by 1.22 turns (3.95 → 2.73, a −30.9% relative reduction)."
[^c6]: arxiv-2604-27379
