---
description: "Restrict inference in Priest's LP to models that minimize local contradiction, recovering classical logic wherever the theory is actually consistent."
aliases: ["MiLP", "minimally inconsistent LP", "consistency as a default assumption"]
sources: ["priest-1991"]
---
# Minimally inconsistent LP

> Do not repair the contradiction and do not explode from it: rank the
> models of the theory by how inconsistent each one is, reason only from
> the least inconsistent, and classical logic falls out wherever that rank
> is zero.

## Definition / Mechanism

Priest (1991) gives a way for a paraconsistent logician to
keep all of classical reasoning without giving up paraconsistency: "take
consistency as a default assumption, and hence to work within those models
of the theory at hand which are minimally inconsistent."[^c1]

The base logic is first-order LP — Priest's own three-valued paraconsistent
logic (true, false, or both), in which a sentence and its negation can both
hold without the theory collapsing into asserting everything. Ordinary LP
entailment quantifies over *all* LP-models of a theory, including ones that
are gratuitously contradictory. This paper's move is to add a preference
order over those models by degree of inconsistency (how much of the
language is assigned "both") and let entailment look only at the minimal
ones — the same shape as preferring the least-abnormal models in
circumscription, but the abnormality being minimized is contradiction
itself. The resulting consequence relation is non-monotonic: adding a
premise can shrink the set of minimally inconsistent models and overturn
an earlier conclusion, which plain LP (monotonic) cannot do.

The paper states the payoff and its outer bound as one result. On the
payoff: "The result is a strong non-monotonic paraconsistent logic
agreeing with classical logic in consistent situations."[^c2]

And the collapse this construction is built to avoid does not reappear at
the top: "It is shown that the logical closure of a theory under this
logic is trivial only if its closure under LP is trivial."[^c3]

A theory that LP itself does not trivialize is not
trivialized by minimizing over its models either — the minimization adds
discrimination among non-trivial theories, it does not create a new way to
explode.

## Why it matters

Every other note on this stall treats a contradiction as damage to be
removed ([[agm-belief-revision]]) or as a violation to be counted and
minimized in a classical, bivalent search ([[max-sat-backbone]]). This
source does neither: the contradictory sentences are not deleted and the
theory is not made consistent — inference is simply confined to the
models where the contradiction is as small as it can be, and outside the
inconsistent region behaves exactly like classical logic. For a record of
answers that clash on one axis, this is a way to keep reasoning about
every other axis undisturbed without ever choosing which answer to drop.

## Limits

- **The archived extract is the article's abstract and reference list
  only** (a paywalled landing page); the formal definition of the
  inconsistency-minimizing order, the construction's worked examples, and
  the proof of the triviality result are not in the extract and are
  therefore `[?]` unverified — this note states only what the abstract
  itself asserts.
- **Depends on first-order LP** ([[priest-1991|Priest 1979, cited in the
  references]]), which this note does not itself establish; the semantics
  of "both true and false" and how models are compared for degree of
  inconsistency are inherited, not defined here.
- **Nothing is repaired.** The contradiction stays true-and-false in the
  minimal models; an agent that must eventually commit to one value on the
  clashing axis gets no answer from this construction alone.
- **The minimization order itself is not specified in the extract** — by
  analogy with circumscription this is a preference over models, not a
  declared cost function, so it is unclear from this reading alone whether
  it can be tuned the way [[max-sat-backbone]]'s cost can.

## Related

[[agm-belief-revision]] · [[max-sat-backbone]] · [[truth-maintenance-system]] · [[constraint-as-information]]

[^c1]: priest-1991 — "This is to take consistency as a default assumption, and hence to work within those models of the theory at hand which are minimally inconsistent."
[^c2]: priest-1991 — "The result is a strong non-monotonic paraconsistent logic agreeing with classical logic in consistent situations."
[^c3]: priest-1991 — "It is shown that the logical closure of a theory under this logic is trivial only if its closure under LP is trivial."
