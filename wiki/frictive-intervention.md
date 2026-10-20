---
description: "Defines a class of dialogue actions — clarify, verify, challenge, redirect, refuse, meta-dialogue — by their function of resisting task completion to cut epistemic risk, not by surface form."
aliases: ["frictive interventions", "epistemic intervention taxonomy"]
sources: ["arxiv-2604-25136"]
---
# Frictive intervention

> Two interrogatives can both be questions and still differ in kind: one asks
> for a missing fact, the other blocks an action.

## Definition / Mechanism

Pustejovsky & Krishnaswamy (2026) classify a family of
dialogue moves — clarification, verification, challenge, redirection,
refusal, and meta-dialogical comment on the model's own limits — not by
their linguistic surface (question, assertion, request) but by a single
functional criterion: whether the move temporarily resists immediate task
completion in order to reduce epistemic, normative, or safety risk in the
interaction.

> "A frictive intervention is defined not by
> its surface form, but by its role in regulating epistemic commitment and risk
> within an interaction."[^c1]

Formally, "a frictive intervention is an intentional communicative act that
temporarily resists immediate task completion in order to reduce epistemic,
normative, or safety risk in an interaction."[^c2]

The six classes are
defined only functionally — for example, clarification is the class that
"seek[s] missing constraints or resolve[s] underspecification before
acting."[^c3]

The category boundary is drawn by three joint properties, not by
appearance: intentionality —

> "The intervention is not noise or
> uncertainty leakage, but a deliberate control decision."[^c4]

— resistance (the move
delays, redirects, or blocks task execution), and risk reduction (its
purpose is to improve epistemic quality or prevent a downstream failure).
Under this test, unmotivated hedging, generic verbosity, and stylistic
hesitation are excluded: they resist nothing and reduce no risk, so they do
not count as frictive interventions even though they may look similar on
the surface.

This taxonomy is deliberately the action space of a control problem, not an
exhaustive theory of dialogue acts: it exists to be selected *from*, by a
policy, at each turn (see [[risk-conditioned-trust-region]] and the
[[threshold-optimality-of-clarification|threshold theorem]] that motivates
when clarification, specifically, belongs in that selection).

## Why it matters

Most clarification/abstention work in this wiki treats "ask" as a single
undifferentiated action opposed to "answer." This taxonomy insists that
*why* a move resists completion is the thing that should be modeled and
rewarded — a verification move and a refusal move both resist, but for
different epistemic reasons, and collapsing them into one "intervention"
signal (as scalar reward shaping tends to) discards exactly the information
a risk-sensitive policy needs to choose among them.

## Limits

The six classes are asserted, not derived: the paper states they are "not
intended as an exhaustive theory of dialogue, but as a minimal set of
epistemic control actions sufficient to capture the dominant alignment
failure modes in current language models," with the full fine-grained
taxonomy deferred to a companion paper (Pustejovsky and Zhu, 2026) this
wiki has not read. Whether a given utterance is "intentional" versus mere
uncertainty leakage is not itself operationalized here — it is measured
indirectly through the components of the [[friction-functional]].

## Related

- [[friction-functional]] — the scalar surrogate built from these classes'
  characteristic failure modes.
- [[threshold-optimality-of-clarification]] — the dominance condition for
  when clarification, one of these classes, is the optimal action.
- [[risk-conditioned-trust-region]] — a training method that grants a
  policy more room to deviate from its base model precisely when a frictive
  intervention is warranted.
- [[abstention]] — refusal and abstention overlap but are not identical:
  abstention withholds an answer, refusal blocks an action.
- [[decision-centric-design]] — shares the commitment to an explicit,
  deterministic action-selection layer over generation.

[^c1]: arxiv-2604-25136 — "A frictive intervention is defined not by its surface form, but by its role in regulating epistemic commitment and risk within an interaction."
[^c2]: arxiv-2604-25136 — "A frictive intervention is an intentional communicative act that temporarily resists immediate task completion in order to reduce epistemic, normative, or safety risk in an interaction."
[^c3]: arxiv-2604-25136 — "Clarification, which seek missing constraints or resolve underspecification before acting."
[^c4]: arxiv-2604-25136 — "The intervention is not noise or uncertainty leakage, but a deliberate control decision."
