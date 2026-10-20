---
description: "Reasoning models often detect that a question is under-specified inside their own reasoning trace, yet still emit an unsupported final answer instead of abstaining."
aliases: ["detection-to-abstention gap", "Abstention@Detection", "A@D"]
sources: ["arxiv-2604-09408", "gu-2026"]
---
# Detection-to-abstention gap

> A model can name the missing premise in its own reasoning trace and still
> answer as if it had it — detecting insufficiency is not the same
> achievement as acting on the detection.

## Definition / Mechanism

Gu et al. (2026) separate what a reasoning model's intermediate
trace shows from what its final answer does: "We formalize this mismatch as
the detection-to-[[abstention]] gap, where detected insufficiency fails to
translate into final abstention."[^c1]

The gap is measured with three metrics over under-specified questions: "DR
measures whether the reasoning trace explicitly recognizes missing or
ambiguous conditions, OAR measures final-answer abstention, and A@D measures
abstention conditioned on detection," formally $A@D = |\{i:
\mathrm{Detect}(y_i)=1 \wedge \mathrm{Abstain}(y_i)=1\}| / |\{i:
\mathrm{Detect}(y_i)=1\}|$ — so DR and OAR can diverge even when the model's
detection is largely correct.[^c2]

On base (untrained) reasoning models the divergence is large: "DeepSeek
obtains a DR of 45.3% but only an OAR of 18.6%, and Qwen obtains a DR of
52.9% but only an OAR of 21.1%," i.e. roughly a third to a fifth of detected
cases in the base models translate into an abstaining final answer.[^c3]

The same dissociation appears outside single-turn math/QA, in an agentic
tool-use setting where "abstaining" means calling a help tool instead of
submitting. On [[ask-f1-selective-escalation-metric|Ask-F1]]-scored SWE and
SQL tasks, Claude Opus 4.6 "explicitly recognizes in its reasoning trace
that it is stuck and submits anyway" in 45% of its alignment failures —
manual review found it was the only tested model that ever verbalized a
task as infeasible, yet detection did not convert into an `ask_human()`
call: in tool use and logic it explored extensively "without ever executing
the critical step." The gap is not confined to a metric artifact of one
scoring protocol; it recurs whenever detection and the committing action
(abstain, or ask) are measured separately.

## Why it matters

This gives the answerer's side of the wiki (stall 10) a *measured*, named
gap between recognising that a question needs a constraint the answerer
does not have and committing to say so — distinct from not recognising it
at all. A selection criterion or benchmark that scores only the final
answer (OAR alone) cannot tell whether a failure to abstain is a detection
failure or a translation failure; A@D isolates the second. That the same
split shows up in an agentic help-seeking benchmark, with a different model
family and a tool call standing in for abstention, argues the gap is a
property of committing to an uncertain output in general, not an artifact
of one abstention metric.

## Limits

- Detection (DR) is itself judged by an LLM-as-judge protocol reading the
  reasoning trace, validated only by a 200-example human audit on
  *abstaining* responses, not on the full DR-labelled set; DR's own error
  rate on non-abstaining traces is not separately reported here.
- Measured on math/QA missing-premise datasets (MissingPremise,
  AbstentionBench subsets) and, in the agentic case, on SWE/SQL coding
  tasks; whether the same divergence holds for
  [[efe-planning-as-variational-inference|ambiguity]] that is neither a
  missing numeric premise nor a coding blocker (e.g. an open-ended
  underspecified goal) is untested.
- The agentic-setting figure (45%, Claude only) comes from one model
  family's manual-review self-assessment failures in one benchmark, not a
  DR/OAR-style paired measurement; it is supporting evidence of the same
  pattern, not a second calibrated A@D number.
- The gap is defined for a single-turn final answer versus abstain; it does
  not distinguish abstaining from asking a clarifying question — both count
  as "abstain" in this metric.

## Related

[[recognition-refusal-dissociation]] · [[judge-then-solve]] · [[abstention]] · [[ask-f1-selective-escalation-metric]] · Commitment

[^c1]: gu-2026 — "We formalize this mismatch as the detection-to-abstention gap, where detected insufficiency fails to translate into final abstention."
[^c2]: gu-2026 — "DR measures whether the reasoning trace explicitly recognizes missing or ambiguous conditions, OAR measures final-answer abstention, and A@D measures abstention conditioned on detection"
[^c3]: gu-2026 — "DeepSeek obtains a DR of 45.3% but only an OAR of 18.6%, and Qwen obtains a DR of 52.9% but only an OAR of 21.1%."
