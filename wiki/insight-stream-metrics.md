---
description: "Three proposed metrics for scoring an agent's stream of ask/notify/draft/stay-silent decisions — timing correctness (IDQ), evidentiary grounding (CGS), and improvement from feedback (LL)."
aliases: ["Insight Decision Quality", "IDQ", "Context Grounding Score", "CGS", "Learning Lift", "LL"]
sources: ["bui-2026"]
---
# Insight-stream metrics (IDQ, CGS, LL)

> Score the decision stream, not just the task: did the agent act at the
> right moment, on the right evidence, and did it learn from being told no.

## Definition / Mechanism

Bui & Evangelopoulos (2026) propose scoring a [[proactivity-taxonomy|Level-3 agent's]]
sequence of notify/question/draft/stay-silent decisions, rather than only
whether a downstream task is completed, with three targets:

- **Insight Decision Quality (IDQ)** averages a per-decision score
  $S_{\mathrm{dec}}(a^\pi_t, a^\star_t, s_t)\in[0,1]$ over all $T$ decision
  points, giving full credit for the reference action, partial credit for
  reasonable alternatives, and penalties for false interruptions, missed
  opportunities, wrong action type, and bad timing; unlike an acceptance
  rate, it scores deliberate silence as well as shown insights.[^c1]
- **Context Grounding Score (CGS)** is restricted to the decision points
  where the agent did not stay silent, and multiplies the F1 overlap
  between the agent's cited support facts and the reference support facts
  by a binary faithfulness check on the message's factual claims; it is
  reported as not applicable rather than zero when nothing was shown.[^c2]
- **Learning Lift (LL)** is the difference in IDQ between a policy that
  updates from prior developer feedback and an identical policy frozen at
  its starting point, evaluated on the same later decisions — positive LL
  means feedback improved future timing or action choice, not merely
  repetition of an earlier message.[^c3]

Read together rather than collapsed into one score: high IDQ with low CGS
means the agent times its interruptions well but justifies them poorly;
high CGS with low IDQ means it can ground a message but surfaces it badly.[^c4]

## Why it matters

This answers what a "selection" evaluation should score once staying
silent is a candidate action: not just whether the shown outputs were
correct, but whether the *decision to show or not show* was correct at
that moment (IDQ), whether what was shown was actually supported (CGS),
and whether the policy gets better at both after a developer's response
(LL) — three axes existing pass/fail benchmarks for clarifying questions
collapse into a single ask-rate or accuracy number.

## Limits

- Unvalidated as protocols: the paper states these are "evaluation targets
  rather than a completed benchmark" and reports no measured scores for
  any system.[^c5]
- Both IDQ and CGS require a human-labelled reference action $a^\star_t$
  and reference support facts $G^\star_t$ at every decision point,
  produced by an annotation protocol the paper sketches but does not run;
  inter-annotator agreement is unmeasured.
- LL requires recurring but non-identical scenarios and a held-out later
  decision to separate genuine adaptation from repeating the same message;
  the paper proposes this design without executing it.
- The metrics are adapted from an active-user-simulation protocol (Nathani
  et al., cited in the source) for a different task; that source is not
  read here, so the adaptation's fidelity to the original is not checked.

## Related

[[proactivity-taxonomy]] · [[clarification-benchmarks]] · [[value-of-information]]

[^c1]: bui-2026 — "Here 𝑆dec ( 𝑎𝜋𝑡 , 𝑎★𝑡, 𝑠𝑡 ) ∈ [0, 1] is the decision score at time 𝑡 . It gives full credit to the reference action, partial credit to reasonable but weaker alternatives, and penalties for false interruptions, missed opportunities, wrong action types, and bad timing."
[^c2]: bui-2026 — "where M is the set of times for which 𝑎𝜋𝑡 is not the stay silent action, |M | is the number of shown insights, 𝐺𝑡 and 𝐺★𝑡 are the agent and reference support facts, 𝐹1 ( 𝐺𝑡 , 𝐺★𝑡) is the harmonic mean of evidence precision and recall, and 1[faithful( 𝑚𝑡 , 𝐺𝑡 )] equals 1 only when the factual claims in 𝑚𝑡 are supported by 𝐺𝑡 ."
[^c3]: bui-2026 — "LL = IDQ( 𝜋adapted ) − IDQ( 𝜋frozen ) ."
[^c4]: bui-2026 — "High IDQ and low CGS means the agent has timing judgment but weak justification; high CGS and low IDQ means it can ground messages but surfaces them poorly."
[^c5]: bui-2026 — "These metrics are evaluation targets rather than a completed benchmark."
