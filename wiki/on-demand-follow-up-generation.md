---
description: "An LLM suggests three follow-up questions from only the last four transcript turns when the interviewer requests them, constrained to stay inside the current topic and under twenty words."
aliases: ["follow-up question generation", "follow-up suggestions"]
sources: ["singhal-2026"]
---
# On-demand follow-up generation

> Candidate probes for the axis already open, produced only when asked for,
> from a short window rather than the whole transcript.

## Definition / Mechanism

When the interviewer presses a UI button, the four most recent transcript
turns are passed to an LLM (gpt-5-mini) that returns three suggested
follow-up questions, under a prompt that constrains them to (i) clarify
ambiguous or under-specified statements, (ii) probe for concrete detail
"without introducing topics outside the current script scope," (iii) be
open-ended, non-leading, simple, and under twenty words, and (iv) avoid
soliciting implementation detail.[^c1]

The four-turn window is adopted from a prior finding that four turns were
sufficient context for 98% of human-spoken follow-up questions in
unassisted interviews.[^c2]

## Why it matters

The AI-assisted condition asked more than double the follow-up questions of
the training-only condition (33.7 vs. 16.3 per interview, IRR = 2.06,
p = .015) and more follow-ups per topic (3.43 vs. 1.15, Hedges' g = +0.81,
p = .015), while the plain follow-up rate relative to non-follow-up
questions covered did not differ significantly between conditions (1.61 vs.
1.07, g = +0.39, p = .21) — the paper reads this as the generator not
changing how probing-heavy each question is, only how often interviewers
are prompted to probe at all.[^c3]

Telemetry showed only 28/140 (≈20%) generated follow-ups were adopted
verbatim, and interviewers rated this feature lowest of the assisted
capabilities on usefulness (M = 3.19, 48% agreement) — lower than
[[topic-coverage-tracking]] — with exit interviews suggesting interviewers
used the suggestions as a prompt for their own follow-up rather than as
text to read aloud.[^c4]

## Limits

- The four-turn context bound is carried over from a different study's
  finding about unassisted human interviewers, not re-derived for this
  generator; it is asserted as sufficient, not shown to be necessary or
  optimal here.
- The higher follow-up count is confounded with the paired topic tracker
  and with fewer, better-designed AI-generated scripts in the same
  condition; the generator's own marginal contribution is not isolated.
- Low verbatim adoption (≈20%) with a still-large follow-up count implies
  interviewers were prompted more often to ask something, not that this
  generator's specific suggestions were what got asked — the mechanism
  measured on this stall may be "reminder to probe," not "content of the
  probe."

## Related

[[topic-coverage-tracking]] · Selection · [[stage-specific-elicitation]]

[^c1]: singhal-2026 — "the four most recent turns are passed as context to gpt-5-mini via a second prompt that produces three suggested follow-up questions. The prompt enforces constraints that address common interviewer mistakes"
[^c2]: singhal-2026 — "We adopt the prior finding that four turns were sufficient context for 98% of human-spoken follow-up questions in unassisted interviews"
[^c3]: singhal-2026
[^c4]: singhal-2026 — "28/140 generated follow-ups (≈20%) were adopted verbatim by interviewers"
