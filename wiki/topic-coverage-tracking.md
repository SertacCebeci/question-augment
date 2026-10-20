---
description: "A background LLM classifier marks scripted topics addressed in real time from a sliding transcript window, letting an interviewer see which axis is still open without re-reading the script."
aliases: ["topic tracking", "script management", "topic-coverage tracker"]
sources: ["singhal-2026"]
---
# Topic coverage tracking

> A visible, continuously-updated map of which scripted topics are already
> covered — so "which axis next" is read off a display instead of held in
> the interviewer's memory.

## Definition / Mechanism

In an AI-assisted requirements-elicitation interview, incoming speech turns
are aggregated into a sliding four-turn window; on each window boundary a
background process submits the window together with the interview's scripted
topic list to an LLM (gpt-5-mini) via a topic-classification prompt, marking
a topic as addressed "only when it is explicitly mentioned or substantively
discussed in the excerpt," with a transcript excerpt attached as evidence,
and surfacing the marking on the interviewer's screen next to each scripted
topic.[^c1]

The tracker's output agreed closely with post-hoc LLM coding of covered
topics on the study's transcripts (F1 ≈ 0.91, precision ≈ 0.96).[^c2]

## Why it matters

In a between-subjects quasi-experiment (21 AI-assisted vs. 22 training-only
interviewer–stakeholder dyads), the AI-assisted condition — script generation
plus this tracker plus on-demand follow-ups — covered fewer distinct topics
(9.6 vs. 14.5) but a higher share of its own scripted questions (86% vs.
69%) and produced goal models with a higher lowest-level-goal fraction
(0.653 vs. 0.598, p = .005).[^c3]

Interviewers rated topic-coverage tracking the most useful workflow feature
(M = 4.29, 86% agreement ≥ 4), above every other assisted capability
including the follow-up generator.[^c4]

For stall 2 (which axis first), this is an operational answer distinct from
the criteria on Selection: it does not rank candidate topics by an
information or value score — it renders the coverage state of every axis and
leaves the order to the interviewer, who empirically converges on staying
longer per axis rather than cycling through more of them.

## Limits

- The claim rests on one study, one task family (19 consumer-app interview
  scenarios), and one topic granularity chosen by the same LLM pipeline that
  generated the script; the tracker's precision was validated against
  post-hoc LLM coding, not independent human coders.
- The design does not isolate tracking from the paired follow-up generator
  or from the script-quality difference between conditions — the workflow
  is evaluated as a whole, so the topic-coverage share of the effect is not
  separated from script design or from [[on-demand-follow-up-generation]].
- "Fewer topics, more per-topic follow-ups" is reported as a between-
  condition association, not a randomized manipulation of the tracker alone.

## Related

Selection · [[on-demand-follow-up-generation]] · [[stage-specific-elicitation]] · [[constraint-seeking]]

[^c1]: singhal-2026 — "a background process submits the window—together with the interview’s scripted topic list—to gpt-5-mini via a topic-classification prompt. The prompt instruction is to mark a topic as addressed only when it is explicitly mentioned or substantively discussed in the excerpt"
[^c2]: singhal-2026 — "The topic tracker agreed closely with post-hoc LLM coding of covered scripted topics (F1 ≈ 0.91, precision ≈ 0.96"
[^c3]: singhal-2026 — "AI-assisted interviews cover fewer topics (9.6 vs. 14.5), cover more scripted questions (86% vs. 69%), ask more follow-ups per topic (3.43 vs. 1.15), and produce more refined goal models (lowest-level goal fraction 0.653 vs. 0.598)"
[^c4]: singhal-2026 — "Topic-coverage tracking received the highest ratings (M = 4.29; 86% agreement), followed by support for transitioning between topics (M = 4.00; 81%)"
