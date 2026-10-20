---
description: "Teacher feedback on a student's own attempt helps most where early errors would otherwise propagate: early for stepwise math, mid-dialogue for non-stepwise code."
aliases: ["assessment timing", "feedback position effect", "mid-assessment versus pre-assessment"]
sources: ["arxiv-2512-13102"]
---
# Feedback timing and error derailment

Corrective feedback on a learner's attempt can be given at different points of a dialogue, and the point matters. In the Socratic Students setup, the student first attempts the problem, the teacher assesses that attempt for correctness and points out errors, and the assessment "appended to the conversation history, grounding all" later turns.[^d1]

The paper's result is that the best insertion point depends on the domain. On math, an early assessment works best: "produces a large boost at Turn 0 that persists across" the remaining turns.[^d2] On coding the early boost is short-lived: the gain is "transient: assessment at Turn 0 boosts Turn 0, but" it "is soon overtaken by assessments at Turns 1 and 2."[^d3] Later assessments do better on code, and the paper's account of why is about how errors propagate. "Later assessments yield better performance because coding problems are not stepwise," and "early incorrect attempts often derail the solution," so "a delayed assessment can correct accumulated" errors.[^d4] Math is the stepwise case, where an early correction carries forward; code is the non-stepwise case, where a wrong early start contaminates everything that follows and a later correction acts on a fuller record of the mistake. The summary the paper gives is that the optimal position is "dependent: Pre variant works best" for math, with mid-dialogue best for code.[^d5]

The mechanism, as the paper states it: the value of feedback is set by whether the student's earlier commitments carry forward. Where a step is built on the previous one, a correction at the first step keeps paying on every later step. Where a mistake can sit unnoticed and then derail a whole solution, a correction that arrives after the student has committed to more of the dialogue acts on accumulated errors. The paper reports the two regimes as "reflecting fundamental differences in their problem structures" between stepwise and non-stepwise tasks.[^d6]

## Limits

- One student model is reported for the position sweep. The paper states that "Figure 7 reports Pass@5 for Qwen-7B across all assessment positions," so the timing effect is not shown across student models.[^d7]
- Two domains only (math and code). The stepwise and non-stepwise split is the paper's own classification of those tasks; it is not measured separately from the domain label.
- The teacher is assumed reliable. The paper's limitations say "Performance may degrade if the teacher is noisy, biased, or weaker than the student."[^d8]
- The error-propagation account is the paper's explanation of the empirical ordering. The paper does not report an experiment that isolates propagation from domain, so the explanation is offered rather than tested here.
- The coding gain fades, so the best position is a function of the measured horizon. The paper's ranking is at Pass@5 at the turns it measured; a different horizon could reorder the positions.

## Related

- [[clarification-timing-decay]] — a clarifying request's value falls as execution proceeds, and the decay differs by kind of clarification; the same timing question on the asking side.
- [[gated-socratic-scaffolding]] — its Socratic prompts are triggered by need rather than fixed to a turn, a different answer to when a tutor should intervene.
- [[turn-efficiency-of-questioning]] — the per-turn progress measure that the feedback position changes.

[^d1]: arxiv-2512-13102 — "appended to the conversation history, grounding all"
[^d2]: arxiv-2512-13102 — "produces a large boost at Turn 0 that persists across"
[^d3]: arxiv-2512-13102 — "transient: assessment at Turn 0 boosts Turn 0, but"
[^d4]: arxiv-2512-13102 — "Later assessments yield better performance because coding problems are not stepwise,"
[^d5]: arxiv-2512-13102 — "dependent: Pre variant works best"
[^d6]: arxiv-2512-13102 — "reflecting fundamental differences in their problem structures"
[^d7]: arxiv-2512-13102 — "Figure 7 reports Pass@5 for Qwen-7B across all assessment positions."
[^d8]: arxiv-2512-13102 — "Performance may degrade if the teacher is noisy, biased, or weaker than the student"
