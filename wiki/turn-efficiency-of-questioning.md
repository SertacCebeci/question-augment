---
description: "Under a fixed turn budget a questioning strategy is judged by its performance trajectory across turns: how high it rises and how many turns it saves to reach a level."
aliases: ["questioning efficiency per turn", "turns-saved measure", "progress per turn"]
sources: ["arxiv-2512-13102", "arxiv-2512-10195"]
---
# Turn efficiency of questioning

Under a fixed turn budget, a questioning strategy is scored by how the answerer's performance moves across turns, not only by where it ends. In the Socratic Students setup a student may ask a teacher a fixed number of questions (five), and after each teacher reply the student is re-tested on the original problem by sampling answer-only attempts and computing Pass@k.[^c1] A curve that rises steadily, with faster gains early, counts as effective; a flat curve signals that the interaction brought little.[^c2]

Two measures follow from such a curve. The first is the level reached at each turn. Plain interaction with a teacher already raised Pass@k over the static, pre-interaction baseline, with "Pass@k often exceeding +0.5 and reaching as high" as +0.85 in absolute terms.[^c3] The second is the number of turns saved. Trained questioning strategies reached the performance of untrained interaction "with three fewer turns."[^c4] The two are different claims. A strategy can win by ending higher, or by reaching the same level sooner. The second is the one that matters when each turn is expensive: the paper's stated premise is that "interactions are expensive, so improvements must come from making substantial progress per turn, not simply adding more dialogue."[^c10]

The paper splits the gain into two parts. The first is progress per turn. It is scored by an LLM judge of the student's reasoning, and the score is explicitly not a correctness measure: "This score measures the student’s reasoning progress, not correctness (unlike Pass@5)."[^c5] The second is the timing of good questions. The paper compares the student's questions with the questions the baseline asks at later turns, and concludes that stronger methods "progress per turn and ask higher-quality questions" and do so "earlier in the trajectory."[^c6] A strategy's lead can therefore be read as an offset in turns: a question that the baseline asks at turn three is asked at turn one or two.

What survives the transfer from per-turn scoring is the unit of judgement. A per-turn rule such as [[expected-information-gain]] ranks each question by its immediate payoff. A turn-budgeted measure ranks the trajectory, so a question with a small immediate gain can still count if it moves the later turns. This contrast is my inference from the paper's two claims, not something the paper tests against per-turn scoring.

A cruder per-turn measure sits in a clinical dialogue benchmark. AutoMedic counts the average words per turn of the doctor agent, and scores a case as the inverse of that count only when the final answer is correct, and 0 otherwise.[^c11] The motive is that a "checklist" style is unnatural: some agents ask "asking numerous questions simultaneously to gather information quickly," which the authors treat as not representative of an effective clinical strategy.[^c12] The correctness gate "ties conversational style directly to diagnostic success."[^c13] Unlike the trajectory view above, this scores the length of one turn, not how the answerer's performance moves. My reading is that the gate keeps brevity from scoring on its own; a terse wrong dialogue earns nothing.

## Limits

- The budget is small and fixed. The paper says so itself: the efficiency gains "observed here may not directly extrapolate to settings with unbounded or variable-length conversations."[^c7] The three-turn saving is measured only inside a five-turn window.
- Progress and question similarity are both judged by an LLM (Qwen-72B), "to compute the similarity between" questions.[^c8] The outcome that is measured directly is Pass@k; progress is a judge's proxy for it.
- The outcome is evaluated on math and coding only. The paper says these tasks "do not cover broader interactive settings such as open-ended dialogue," so the turn-saving claim is not shown there.[^c9]
- Pass@k is a sampling statistic of the answerer. A rise in it after a teacher reply is evidence of a useful question only if the answerer's sampling itself is held fixed, which the paper's own limitations section doubts.
- Words per turn is a proxy for question bundling, not a count of questions. The AutoMedic method does not test whether a long turn is in fact a multi-question turn, and a long but single-question turn scores the same as a bundled one; this is my reading of the scoring rule.

## Related

- [[expected-information-gain]] — per-turn scoring of a question by immediate information gain; the trajectory view above is what that rule does not score.
- [[clarification-timing-decay]] — a clarification's value depends on how far execution has already gone; the same turn-position question, in a different task.
- [[multi-turn-clarification-plateau]] — more clarification turns stop helping after about turn four in a social-reasoning benchmark; this paper's five-turn budget is too short to test that plateau.
- [[retrieval-conditioned-question-selection]] — question selection by downstream outcome in retrieval; the same selection principle, judged per candidate rather than over a trajectory.

[^c1]: arxiv-2512-13102 — "S interacts with T for a fixed budget of N questioning turns"
[^c2]: arxiv-2512-13102 — "steadily increasing curves (with faster gains early"
[^c3]: arxiv-2512-13102 — "Pass@k often exceeding +0.5 and reaching as high"
[^c4]: arxiv-2512-13102 — "with three fewer turns."
[^c5]: arxiv-2512-13102 — "This score measures the student’s reasoning progress, not correctness (unlike Pass@5)."
[^c6]: arxiv-2512-13102 — "progress per turn and ask higher-quality questions"
[^c7]: arxiv-2512-13102 — "observed here may not directly extrapolate to settings with unbounded or variable-length conversations."
[^c8]: arxiv-2512-13102 — "to compute the similarity between"
[^c9]: arxiv-2512-13102 — "do not cover broader interactive settings such as open-ended dialogue"
[^c10]: arxiv-2512-13102 — "interactions are expensive, so improvements must come from making substantial progress per turn, not simply adding more dialogue."
[^c11]: arxiv-2512-10195 — "we calculate the average number of words per turn"
[^c12]: arxiv-2512-10195 — "asking numerous questions simultaneously to gather information quickly"
[^c13]: arxiv-2512-10195 — "ties conversational style directly to diagnostic success" 
