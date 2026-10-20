---
description: "A taxonomy of three mechanisms for adding intentional constraints to one chatbot exchange — eliciting contribution, restricting access, reshaping output — to counter overreliance."
aliases: ["design friction", "turn-level friction"]
sources: ["chen-2026-probing"]
---
# Turn-level design friction

> Intentional constraints added to a single chatbot exchange — organized
> into three mechanisms — that trade a chatbot's effortlessness for user
> involvement, at a measured cost in workload and frustration.

## Definition / Mechanism

Chen & Gero (2026) synthesized 73 interaction
interventions from 24 HCI papers on digital wellbeing, decision support,
AI-assisted writing and programming education, and found that most cluster
into three recurring mechanisms for interrupting an otherwise frictionless
exchange: eliciting user contribution (requiring information, reasoning or
action beyond the default), restricting access (delaying or conditionally
withholding content), and reshaping system output (changing its amount,
form or communicative role).[^c1]

They instantiated the taxonomy as six probes, two per mechanism, and ran a
within-subjects study (24 participants, eight interface conditions
including a ChatGPT baseline and an unassisted control, short writing
tasks). All six friction probes significantly increased workload, task
duration and self-reported psychological ownership relative to the
unmodified chatbot; effects on recall and recognition — behavioral memory
measures — were mechanism-dependent rather than uniform.[^c2]

The consequence of a given friction depended on where the added effort
landed: it supported involvement when it kept users formulating,
interpreting or assembling the response themselves, and became obstructive
when the effort instead went to satisfying the constraint or managing the
interface. Physical-demand cost was concentrated in the access-restricting
probes (Hold Reveal, Timer Lockout); the largest frustration increase came
from the contribution-eliciting Think Multiplier probe, which requires a
≥20-word prompt and caps the reply at about half that length.[^c3]

One reshaping-output probe, [[socratic-method|Elenchus]], withholds a direct answer entirely:
the model responds only with [[staged-socratic-hint-policy|Socratic]]-style questions that challenge the
user's premises rather than returning content. Among the six probes it
produced the second-largest ownership gain (+2.25 on a 5-point scale,
versus +1.92 for Think Multiplier and +1.00 for Hold Reveal), but
participants who already knew their argument's direction found its
continued questioning frustrating rather than useful.[^c4]

## Why it matters

An answerer can be redesigned to push work — contribution, delay,
interpretation — back onto the asker instead of only improving what it
returns. This is a designed, turn-level manipulation of who commits what
to the exchange, evaluated on involvement and cost, not on task accuracy.

## Limits

- Single task type (short, bounded writing, 50-80 words), single backend
  (GPT-4o), 23-24 participants, one lab session per participant: no claim
  about longer or more naturalistic use is licensed.
- The mechanism taxonomy comes from an exploratory synthesis (Google
  Scholar search, author coding into three clusters plus an "Other"
  residual), not a formal or validated classification.
- Statistical comparisons are all against a single conventional-chatbot
  baseline; no probe is compared against another probe's mechanism
  directly except through that shared baseline.
- Ownership and workload are self-report; recall/recognition are the only
  behavioral measures, and only for the writing task's own content.

## Related

[[clarification-request]] · [[throughput-pressure-on-asking]] · [[preference-signal-against-asking]]

[^c1]: chen-2026-probing — "Most of these designs could be organized around three recurring interaction mechanisms: eliciting user contribution, restricting access, and reshaping system output."
[^c2]: chen-2026-probing — "In a within-subject study with 24 participants, all six probes increased workload, task duration, and perceived ownership relative to a conventional AI chatbot, while their effects on recall and recognition were more selective."
[^c3]: chen-2026-probing — "Friction could support involvement when it kept users engaged in formulating, interpreting, or assembling the response, but could instead become obstructive when effort shifted toward satisfying the constraint or managing the interface."
[^c4]: chen-2026-probing
