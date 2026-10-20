---
description: "A distilled controller that outputs a binary sufficiency decision plus a typed, four-field gap schema, mapped directly into the next retrieval query, for iterative RAG."
aliases: ["S2G-Judge", "S2G-RAG", "Structured Sufficiency and Gap-judging RAG"]
sources: ["arxiv-2604-23783"]
---
# Structured gap-sufficiency judge

> Do not just say "not enough" — say what is missing, in a schema the next
> query can be built from.

## Definition / Mechanism

At each turn of an iterative retrieval pipeline the judge sees the question
$q$ and the accumulated evidence context $C_t$ and predicts a structured
output $y_t=(s_t,G_t)$: a binary sufficiency decision and, when $s_t$ is
false, a set of typed gap items. "Each gap item g ∈ Gt follows a normalized
schema with four fields. The category field takes values in
{bridge_entity, attribute, relation, evidence_span, other}. The target
field specifies the entity being queried. The slot field indicates a
coarse-grained attribute or relation name. The description field provides
a short natural-language clarification." When $s_t$ is true the gap set
is emitted empty and a separate reasoner answers from $C_t$; the judge
itself never generates the answer, so the sufficiency check is decoupled
from generation. The predicted gap items are mapped deterministically into
the next query — target and slot concatenated where both are present,
falling back to description, up to $K$ phrases appended to the original
question — turning "keep retrieving" into an addressable target rather
than a free-form rewrite.

Two design choices make the sufficiency check auditable rather than a
vibe. First, a **context-only constraint**: "We impose a context-only
constraint for sufficiency judgments. The judge must determine sufficiency
based strictly on evidence present in Ct , which prevents relying on
parametric knowledge when deciding whether the evidence is adequate."[^c2]
This blocks the failure mode where a model calls evidence sufficient
because *it* already knows the answer, not because the retrieved text
supports it. Second, the judge is trained by **trajectory distillation**
rather than idealized supervision: "We train S2G-Judge with process
supervision distilled from multi-turn execution traces." An unfine-tuned
backbone is rolled out on training questions to a fixed turn budget,
producing realistic intermediate contexts — redundancy and distractors
included — which a stronger teacher then labels under the same
context-only constraint; a small LoRA-tuned model is distilled on those
labels so supervision matches the states the judge meets at inference.

## Why it matters

Removing the judge is the single largest ablation drop reported: "Removing
S2G-Judge causes the largest drop (−15.8 EM, −19.0 F1), confirming the
importance of explicit retrieval control for multi-hop QA. Without the
judge, the system loses both the sufficiency check and the structured gap
signals that guide the next retrieval step." The stopping signal is
also shown to be asymmetrically reliable, not just accurate on average:
"Figure 2 indicates that S2GJudge is unlikely to over-claim sufficiency.
Conditioned on predicting sufficient, the judge is correct under Truth in
most cases. In particular, the falsepositive rate is 6.44%." That is
the shape a stopping rule wants when answering too early costs more than
one extra retrieval turn: a low false-positive rate on "stop", bought at
the price of a higher false-negative rate.

## Limits

The paper reports its own sufficiency signal is skewed toward
under-claiming: "our sufficiency predictions can be conservative, which in
practice reduces the risk of answering from borderline evidence states,
while leaving room to improve calibration so that clearly sufficient
contexts are more often recognized as such." (`unverified` — the
paper's own calibration caveat, not independently checked here.) The
ground truth used to validate the judge is itself a proxy — retrieval-only,
not whether the *answer* the reasoner would produce is correct — so a high
true-positive rate there does not certify a correct final answer. The gap
schema's four categories are fixed for multi-hop Wikipedia QA and are not
shown to transfer to domains whose missing-information types differ.

## Related

- [[evidence-gap-agent]] — a clinical-QA analogue: a separate module that
  names missing evidence rather than deciding when to stop, one input
  among several rather than the controller itself.
- [[g-steer]] — a different controller choosing among Retrieve/Ask/Stop
  per factor, trained by RL against a cost-weighted reward rather than
  distilled from teacher labels.
- [[final-sufficiency]] — sufficiency scored against ground truth
  independent of the final answer, the same separation this judge's
  context-only constraint is designed to approximate without ground truth.
- [[calibrated-completeness-stopping]]
- [[verification-aware-stopping]]

[^c2]: arxiv-2604-23783 — "We impose a context-only constraint for sufficiency judgments. The judge must determine sufficiency based strictly on evidence present in Ct , which prevents relying on parametric knowledge when deciding whether the evidence is adequate."
