---
description: "A dialogue-state-tracking failure that is formally verifiable by construction can be nearly invisible to human judgment — annotators endorsed one such injected class on only 1 of 30 turns."
aliases: ["IUV weak-salience finding", "state-only failure salience gap"]
sources: ["khoury-2026"]
---
# State-consistency human-salience gap

> A constraint can be violated in a way that is provably true of the state
> and still not read, by the people the state serves, as a violation at all.

## Definition / Mechanism

Khoury, Lin & Mishra (2026) injected a workflow failure class they call
"ignored user value" (IUV) into task-oriented dialogue transcripts — a
value the user supplied is deleted from the tracked state — and had two
annotators, blind to the injection, judge each turn from the transcript and
the state pair. "Humans endorsed the injected label on only 1/30 turns, and
29 of the 35 injected-turn human–injection disagreements are IUV." The
authors are explicit that "this is not label noise — the injection is
verifiable by construction (a user-supplied value is deleted from
$s_t$)" — the annotators saw the exact state pair and still did not flag
most instances as failures.[^c1]

The gap is concentrated in this one class: on the transcript-visible
failure classes excluding IUV, their automated evaluator's agreement with
the human consensus is statistically indistinguishable from the strongest
LLM judge tested ($\Delta F_1=-0.011$, $p=0.68$ on $n=164$ turns), while
the overall human-agreement deficit is driven almost entirely by IUV.[^c2]

The paper's own reading: IUV is "a formal state-consistency signal with
weak broad-human salience (1/30) rather than a fully human-validated
class" — a criterion can be well-defined and mechanically checkable against
the state, and still fail to be a violation *for the people evaluating
whether an answer was acceptable*, because reconciling every user-supplied
value against the tracked state turn-by-turn is not what a fluent-reading
annotator (or, by the paper's argument, a transcript-only judge) actually
does.[^c3]

## Why it matters

It is a documented case where "is what came back actually a constraint
violation" has two different answers depending on who is asked: a
state-tracking definition says yes, deterministically; a human reading the
same transcript and state pair says no on 29 of 30 turns. Any evaluator
that defines correctness purely from formal state consistency can be
correct by its own definition and still not track what its human
stakeholders would call a failure.

## Limits

- This is one injected failure class in one paper, audited by two
  annotators (inter-annotator $\kappa=0.94$ overall, but human–injection
  agreement $\kappa=0.639$) on $n=200$ turns; it is not a general claim that
  state-consistency criteria are usually unsalient — the paper's other three
  classes (PC, UV, WNF) had much higher human endorsement (1.00, 1.00,
  0.95 for PC/UV domains, 0.73 for WNF).[^c4]
- The annotators' protocol did not distinguish whether they failed to
  perform the slot-by-slot reconciliation that would surface the omission,
  or performed it and did not consider the dropped value a failure — the
  paper states this explicitly and draws no conclusion between the two.

## Related

[[sage-abstention-evaluation]] · [[abstention]] · [[semantic-entropy]] · [[clarification-benchmarks]]

[^c1]: khoury-2026
[^c2]: khoury-2026 — "The gap is concentrated almost entirely in IUV: on the transcript-visible subset (n=164) SAGE-Core reaches 0.909 versus 0.920, a difference a paired bootstrap cannot distinguish from zero (∆F1 =−0.011, p=0.68)."
[^c3]: khoury-2026 — "IUV as a formal state-consistency signal with weak broad-human salience (1/30) rather than a fully human-validated class"
[^c4]: khoury-2026
