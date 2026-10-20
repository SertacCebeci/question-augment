---
description: "A question that presupposes a concept's existence (asking its date, place or meaning) makes an LM roughly twice as likely to hallucinate as a question that asks about existence directly."
aliases: []
sources: ["jung-2026"]
---
# Presupposition-hallucination gap

> The same unanswerable concept, asked two ways: "does X exist?" gets a
> correct "no"; "when was X invented?" gets a confident, fabricated date.

## Definition / Mechanism

Jung & Gonen (2026) design prompts that either "explicitly
query the existence of a concept" ("Does X exist?") "or implicitly assume
its existence by asking about one of its attributes" ("Where did X
happen?", "When was X established?").[^c1]

Measured across [[phantombench|PhantomBench]]'s non-existent concepts, models "correctly
acknowledge that the concepts do not exist when queried explicitly about
their existence (HR of 16.2%)" but fail "especially when queried about the
meaning of a concept (HR of 33.4%)" — roughly double the hallucination
rate for the presupposing form of the question over the direct one, on
the same underlying concept. The paper's own reading: "models are more
likely to fabricate information once the existence is presupposed in the
user input."[^c2]

The effect is not uniform across attribute types: "date and place
questions typically require more constrained responses" and show lower
hallucination than "etymology, application, and relation," which "impose
weaker constraints on the expected answer" — the paper's candidate
explanation for the gap within the presupposing forms themselves.[^c3]

A separate, converse asymmetry appears on concepts that *do* exist: models
more often abstain by "presum[ing]" — declining to answer the queried
attribute while accepting the concept's existence (e.g. claiming it has no
recorded date) — showing the existence check and the attribute check can
fail independently in either direction.[^c4]

## Why it matters

It locates the failure at the question's own form, not only at the
answerer's knowledge: the same knowledge gap about the same concept is
exposed by one phrasing and hidden by another, because a presupposing
question removes "does this exist?" from what the answerer treats itself
as having been asked. For stall 3 (how a question touches an axis), this
is evidence that a question's presuppositions are themselves an axis the
asker's phrasing sets, independent of the axis the question nominally
targets.

## Limits

- Measured with an LLM judge (validated on a 120-response human sample,
  not the full set) and on synthetically-generated non-existent concepts,
  not on naturally occurring unanswerable questions; whether the gap holds
  the same size on real user queries is untested here. [?]
- The 16.2%/33.4% figures are aggregates over the tested prompt types and
  models in this benchmark; the paper reports the gap's direction
  consistently but not a per-model or per-domain breakdown of its size.
- The paper's explanation (weaker constraint on the expected answer) is
  offered as a plausible account for graded differences *among* the
  presupposing forms, not as a tested mechanism for the existence-vs-
  presupposition gap itself.

## Related

[[phantombench]] · [[abstention]] · [[clarification-benchmarks]] · [[semantic-entropy]]

[^c1]: jung-2026 — "We design prompts that either explicitly query the existence of a concept or implicitly assume its existence by asking about one of its attributes."
[^c2]: jung-2026 — "especially when queried about the meaning of a concept (HR of 33.4%), even though they often correctly acknowledge that the concepts do not exist when queried explicitly about their existence (HR of 16.2%)"
[^c3]: jung-2026 — "date and place questions typically require more constrained responses, questions about etymology, application, and relation"
[^c4]: jung-2026 — "(E) presume abstains from answering about a specific attribute while implicitly assuming the concept does exist"
