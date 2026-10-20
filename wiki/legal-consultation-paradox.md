---
description: "In a multi-turn legal-consultation benchmark, LLM lawyers' fact-elicitation and legal-reasoning scores drop most for the least-forthcoming clients — precisely where proactive questioning matters most."
aliases: ["consultation paradox"]
sources: ["zhang-2026-dlawbench"]
---
# Legal consultation paradox

> An LLM lawyer's ability to elicit and use facts is worst exactly when the
> client volunteers least — the situation where asking well should matter
> most.

## Definition / Mechanism

Zhang et al. (2026) replay each of DLawBench's 461
legal-consultation cases — the underlying facts held fixed — under four
simulated client narrative styles built from the interpersonal circumplex's
agency/communion axes: "We replay each case under four narrative styles
adapted from the Interpersonal Circumplex (IPC) (Wiggins, 1979; Horowitz and
Strack, 2010; Locke, 2011): Cooperative, Dependent, Withdrawn, and
Adversarial." The styles vary only how much the client volunteers and how
much direction it needs; the client's underlying facts do not change.[^c1]

Across the 26 evaluated models, the Dependent and Withdrawn styles reduce
scores relative to Cooperative, and the drop is not spread evenly across the
benchmark's five component metrics: "these styles reduce model performance
even though they represent situations where legal guidance should be
especially valuable. The penalty is concentrated in Elicitation and
downstream Resolution, consistent with a pipeline in which missing or
under-specified facts constrain the later legal analysis."[^c2]

The Adversarial style is the exception to the pattern: a client who
challenges and questions the lawyer is easier for current models to handle
than one who under-discloses. "A client who challenges the lawyer remains
much closer to Cooperative than Dependent or Withdrawn clients."[^c3]

## Why it matters

This bears on stall 2 (which axis first) at the level of a whole
questioning strategy rather than a single choice: a fixed elicitation
strategy that performs adequately against a cooperative source degrades
exactly against a reluctant or deferential one — the case where actively
choosing the next question, instead of waiting on volunteered information,
should matter most. DLawBench measures this degradation directly but does
not test any strategy built to counter it: no client-style-adaptive
questioning policy is scored against the fixed baseline in this paper, so
the paradox is documented as a deficit, not yet closed by a proposed fix.
It sits next to, and is distinct from, the ask-rate deficits catalogued in
[[clarification-benchmarks]]: those measure *whether* a model asks; this
measures how the *outcome of asking* varies with how forthcoming the
answerer is, holding the underlying facts constant.

## Limits

- The four client styles are produced by an LLM simulator conditioned on
  annotated client beliefs and a style prompt, not observed real client
  behaviour; the paradox rests on that simulator being a faithful stand-in,
  supported only by a 96.9% segment-level style-[[recovery-postulate|recovery]] accuracy from
  human annotators (with four-way Fleiss' κ = 0.917), not a validation
  against real consultations.
- The underlying facts are held fixed across styles by construction, so
  this is a within-case, cross-style comparison, not a comparison across
  naturally varying real clients with different facts.
- Legal domain only (Chinese and U.S. law), one benchmark; whether the same
  ordering — Adversarial closer to Cooperative than Dependent or Withdrawn —
  holds outside legal consultation is not tested here.
- The scores that show the drop (Inquiry, Issue Resolution) are themselves
  LLM-judge scored, with human validation on a 422-item sample only, not
  the full rubric set.
- `[?]` This is a June 2026 arXiv preprint, not yet confirmed at a
  peer-reviewed venue.

## Related

[[clarification-benchmarks]] · [[user-driven-sycophancy]] · [[sycophantic-capitulation]]

[^c1]: zhang-2026-dlawbench — "We replay each case under four narrative styles adapted from the Interpersonal Circumplex (IPC) (Wiggins, 1979; Horowitz and Strack, 2010; Locke, 2011): Cooperative, Dependent, Withdrawn, and Adversarial."
[^c2]: zhang-2026-dlawbench — "these styles reduce model performance even though they represent situations where legal guidance should be especially valuable. The penalty is concentrated in Elicitation and downstream Resolution, consistent with a pipeline in which missing or under-specified facts constrain the later legal analysis."
[^c3]: zhang-2026-dlawbench — "A client who challenges the lawyer remains much closer to Cooperative than Dependent or Withdrawn clients."
