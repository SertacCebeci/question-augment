---
description: "An answerer with missing information should ask, not abstain, exactly when a user reply could supply the missing variable; a genuinely absent topic gets abstention instead."
aliases: ["recoverable vs irrecoverable missing information"]
sources: ["arxiv-2604-04565"]
---
# Recoverability-gated ask/abstain

> The same missing variable calls for two different non-answers: ask when
> the gap could close from one more sentence, abstain when nothing the
> user says will help.

## Definition / Mechanism

Baidya (2026) splits the "missing information" case
of a three-way commit decision — a case a scalar confidence threshold
treats as one bucket — into two, by asking a further question of the
missing variable itself, not of the model's confidence: "Ask — Vmissing
̸= ∅ but missing variables are recoverable: a targeted clarification
resolves the gap. (iii) Abstain — Vmissing ̸= ∅ and missing information
is irrecoverable: no user clarification will help."
[^c1]

The criterion is operationalised, not left to judgement calls: "The
distinction between Ask and Abstain when Vmissing ̸= ∅ depends on
whether the missing information is recoverable — i.e. whether a user
clarification could plausibly supply it. This recoverability judgement
is encoded in the knowledge graph via the presence or absence of ?var
nodes: a missing variable that can be injected as a graph placeholder is
recoverable; a query whose topic has no graph nodes at all is not."
[^c2]

So recoverability reduces to a graph-membership test on the missing
variable: does the answerer's knowledge base have *any* node for what is
missing (ask about it) or *no* node at all (the topic itself is absent —
abstain).

Empirically this is the harder half of the split: across every tested
inference-time architecture, "Abstain recall peaks at 26% in baseline and
falls to 9% and 13.3% in enhanced and v3 respectively. ... Recognising
the absence of relevant information is structurally harder to gate on
than detecting ambiguity or conflict. Low confidence and coverage scores
are necessary but not sufficient signals for true irrelevance."
[^c3]

## Why it matters

A single abstention threshold on a confidence or coverage score cannot
express this distinction, because both Ask-worthy and Abstain-worthy
cases can produce the same low score — the paper's own evidence is that
low confidence is "necessary but not sufficient" for true irrelevance.
Recoverability instead asks a structural question about *what* is
missing (is there anywhere for the answer to come from) rather than a
scalar question about *how sure* the model is. That gives a designer a
second, independent gate to build: not just a sharper confidence score,
but a test of whether the missing quantity has any representation at all
in what the answerer knows.

## Limits

- The recoverability test is defined relative to one particular
  representation — a knowledge graph with typed placeholder nodes — and
  the paper does not show it transfers to answerers without a graph
  backbone (plain-text retrieval, tool-using agents).
- Whether a topic "has graph nodes" is itself a coverage question about
  the knowledge base construction, not a property of the query alone;
  a KB with sparse coverage will misclassify recoverable gaps as
  irrecoverable ones — the paper does not separately quantify this
  failure mode — [?].
- Reported only through the lens of the harder companion result
  ([[inference-time-calibration-ceiling]]): the recoverability signal is
  shown to be learnable by finetuning, not to be well-approximated by any
  inference-time heuristic tested.

## Related

[[inference-time-calibration-ceiling]] · [[abstention]] · [[gated-answerability-rule]] · Commitment

[^c1]: arxiv-2604-04565 — "Ask — Vmissing ̸= ∅ but missing variables are recoverable: a targeted clarification resolves the gap. (iii) Abstain — Vmissing ̸= ∅ and missing information is irrecoverable: no user clarification will help."
[^c2]: arxiv-2604-04565 — "The distinction between Ask and Abstain when Vmissing ̸= ∅ depends on whether the missing information is recoverable — i.e. whether a user clarification could plausibly supply it. This recoverability judgement is encoded in the knowledge graph via the presence or absence of ?var nodes (§6): a missing variable that can be injected as a graph placeholder is recoverable; a query whose topic has no graph nodes at all is not."
[^c3]: arxiv-2604-04565
