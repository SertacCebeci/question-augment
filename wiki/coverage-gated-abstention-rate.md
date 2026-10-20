---
description: "With the evidence-verification threshold held fixed, the abstention rate tracks corpus coverage, not answerer competence: 40-70% narrow-corpus versus ~10% after a 80x corpus expansion."
aliases: ["quality-coverage tradeoff", "corpus-task alignment", "abstention rate as coverage signal"]
sources: ["arxiv-2604-17843"]
---
# Coverage-gated abstention rate

> An abstention rate is not a score for the answerer; held against a fixed
> threshold, it is a readout of what the corpus does not yet cover.

## Definition / Mechanism

Karnatak et al. (2026) hold AVA's
evidence-verification threshold — the rule that gates an answer on
sufficient retrieved support, otherwise [[abstention|abstains]] — fixed
across two deployments that differ only in retrieval corpus size, and read
the resulting abstention rate as a measurement of corpus–task coverage
rather than of the threshold or the model: "we instantiate this
quality–coverage trade-off by fixing the evidence-verification threshold
and treating abstention as the primary observable signal of corpus
adequacy."[^c1]

With a narrow, high-quality corpus of "roughly 50 flagship World Bank
Reports," the fixed threshold "yielded high abstention rates (40–70%)."[^c2]

Expanding the corpus roughly 80-fold, to "more than 4,000 World Bank
Reports," "leaving the verification threshold unchanged," dropped the
abstention rate to "approximately 10%."[^c3]

Because the threshold did not move, the paper attributes the entire shift
to coverage, and draws the general design principle that abstention rate is
diagnostic of corpus–task mismatch, not of the answerer's competence: "abstention should reflect epistemic humility rather than systematic
failure."[^c4]

The paper generalises this into a monitoring recipe: watch the abstention
rate alongside two other quantities that can separately explain it — "corpus–task alignment, evidence verification threshold and user behaviour
(including reformulations, abandonment, and patterns of re-engagement)" —
so that a rising rate can be attributed to a coverage gap, a threshold that
is too strict, or users giving up, rather than assumed to mean any one of
these.[^c5]

## Why it matters

A raw abstention rate is uninterpretable on its own: the same number can
mean "the corpus lacks this topic" or "the threshold is too conservative"
or "users are asking outside scope." This note gives the control that
disambiguates it — hold the threshold constant and vary coverage, or vice
versa — and reports the one data point where doing so produced an 80x
coverage change and a 4-7x drop in abstention, evidence that coverage, not
threshold miscalibration, was the dominant driver in this deployment. It
turns "why is the answerer abstaining so much" from a question about the
answerer into a question about what it has been given to work with.

## Limits

- One system, one corpus expansion, no controlled comparison — the 40-70%
  to ~10% shift is a before/after observation from one deployment, not a
  swept curve relating corpus size to abstention rate; the functional form
  of that relationship (linear, saturating, threshold-dependent) is not
  established. [?]
- The threshold itself is never varied in this study, so the claim that
  coverage (not threshold strictness) drove the change rests on the
  threshold being held literally constant, not on an ablation that also
  tried varying it. [?]
- "Approximately 10%" and "40–70%" are the paper's own rounded figures from
  a five-day query log (Figure 5), not independently reproduced.
- The three-signal monitoring recommendation (coverage, threshold, user
  behaviour) is a design recommendation drawn from this one case, not
  validated as sufficient to correctly attribute abstention-rate changes in
  general.

## Related

[[abstention]] · [[relational-humility]] · Commitment

[^c1]: arxiv-2604-17843 — "In AVA, we instantiate this quality–coverage trade-off by fixing the evidence-verification threshold and treating abstention as the primary observable signal of corpus adequacy."
[^c2]: arxiv-2604-17843 — "AVA operated over a narrowly scoped corpus of roughly 50 flagship World Bank Reports. This maximized source quality but yielded high abstention rates (40–70%)."
[^c3]: arxiv-2604-17843
[^c4]: arxiv-2604-17843 — "This leads to our core design principle: abstention should reflect epistemic humility rather than systematic failure."
[^c5]: arxiv-2604-17843 — "we recommend that future systems monitor three complementary signals in tandem with the abstention rate: corpus–task alignment , evidence verification threshold and user behaviour (including reformulations, abandonment, and patterns of re-engagement)."
