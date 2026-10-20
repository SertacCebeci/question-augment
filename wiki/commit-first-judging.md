---
description: "A judge solves the task itself first, commits to that answer, and accepts a candidate only if it matches; this removed gaming on one task and moved the anchor to the judge's own answer."
aliases: ["commit-first judging", "deanchored judging", "solve-then-match judge", "committed-answer judging"]
sources: ["doi-10-48550-arxiv-2609-00088"]
---
# Commit-first judging

An LLM judge in the usual single-call form sees the question, any reference and the candidate together, and returns a holistic score. Commit-first judging reorders this. The judge solves the task itself first and commits to that answer. Only then does it see the candidate, and it accepts the candidate only if the two match.[^c1]

The candidate is not hidden. The defence "does not hide the candidate", which can stay in full view at comparison time.[^c2] What changes is that the judge has an answer of its own to compare against. In the work's phrase, "Commitment, not blindness, is the operative variable."[^c3]

The form is Zhou's, as this paper reports it. A judge told to reason step by step with the candidate already in front of it "leaves the false positive rate on wrong answers at 0.719".[^c4] With the judge answering first and matching afterwards, "This drops the false positive rate to 0.012."[^c5] These are Zhou's figures as quoted here; this paper does not re-measure them.

The mechanism was tested in a controlled run. A plain best-of-N search with no access to correct answers optimised Python code against DeepEval's G-Eval metric in its documented default configuration. On an interval merging task the judge accepted 90 of 96 candidates in the first seed and 93 of 96 in the second. "Every accepted candidate passed every test the search could see" and failed a held-out suite the search could not see.[^c6] The judge's own rationale praised a line that merges intervals that do not touch: "correctly handles touching intervals via the current start <= last end + 1 condition".[^c18]

Under commit-first judging the same task showed no gaming: "Commit-first judging removed the effect completely: 0 of 96" in both seeds.[^c7] The log gives the reason. The judge's committed solution was correct, "committed solution is correct, passing 3 of 3 held-out checks."[^c8]

The same switch did not help on a second task, duration parsing, which the judge could not solve even once in the probe (see [[judge-self-solve-probe]]). Diverged candidates rose from 37 and 41 under the shipped configuration to 50 and 75 under commit-first. "On the duration parsing task it backfired, in both seeds."[^c9] One seed ended "The other ended pinned at 0.667 while the evaluator read 0.99."[^c10] Here the judge's committed answer was wrong, and the population's final correctness came to rest on the judge's own score.

The paper's reading is that the defence does not remove the anchor that gets gamed; it moves it from the candidate to the judge's own answer. The evaluation is then "only as good as the judge is at the task."[^c11] Where the judge is right, gaming becomes hard. Where it is wrong, the search converges on the judge's mistake while the scores look excellent. This is a bounded failure, because it is limited by the judge's competence, but it is still invisible from inside the system. The general pattern of a proxy pushed past what it measures is [[reward-overoptimization]]; commit-first judging changes which quantity the proxy is anchored to, not whether the proxy can be exploited.

The same ordering appears inside a model, where an answer is fixed before the reasoning that is written after it ([[pre-committed-answer-before-cot]]). Solving before judging is also named in [[llm-judge-biases]] as a remedy for weak reasoning grading.

## Limits

- Scope. "Four small tasks, one judge family, one generator."[^c12] Divergence appeared on two of the four tasks. On the other two the generator solved the task from the first round, so there was no headroom for gaming.
- Lock-in is a possibility shown in one seed of two, not a law. The paper claims only "so we claim that commit-first judging can lock the judge" and then "not that it must."[^c13]
- The commit-first null tasks, the strict-mode control and the smaller-judge arms are single runs. "single runs and carry no replication claim."[^c14]
- The frontier judge rejects the temperature parameter, so "so the commit-first frontier judge ran at default sampling," which the design did not specify. The asymmetry affects only comparisons across judge models.[^c15]
- The census behind the defence is a different claim. "None implement the defence."[^c16] That count covers default templates only, and "Deployed systems then modify those templates."[^c17] The verdict does not carry over to a modified configuration.
- The judge's own answer is what the defence rests on, so its quality must be checked. The paper gives no threshold for when the judge is good enough; that gap is the reason for the probe note.

## Related

- [[judge-self-solve-probe]] — the cheap measure of whether the judge's own answer is good enough for this defence to be safe
- [[reward-overoptimization]] — the general failure of a proxy pushed past what it measures
- [[judge-master-key-false-positives]] — judges fooled by surface form, where judging against a solved answer is a named remedy
- [[pre-committed-answer-before-cot]] — the same ordering inside a model, answer fixed before the reasoning
- [[llm-judge-biases]] — the grading weakness that solving first is said to address
- [[judge-then-solve]] — the same name shape but a different object: a trained abstention gate on answerability, not an evaluation rule

[^c1]: doi-10-48550-arxiv-2609-00088 — "task itself first and commits to that answer. Only then does it see the candidate, and it accepts"
[^c2]: doi-10-48550-arxiv-2609-00088 — "It does not hide the candidate"
[^c3]: doi-10-48550-arxiv-2609-00088 — "Commitment, not blindness, is the operative variable."
[^c4]: doi-10-48550-arxiv-2609-00088 — "leaves the false positive rate on wrong answers at 0.719"
[^c5]: doi-10-48550-arxiv-2609-00088 — "This drops the false positive rate to 0.012."
[^c6]: doi-10-48550-arxiv-2609-00088 — "Every accepted candidate passed every test the search could see"
[^c7]: doi-10-48550-arxiv-2609-00088 — "Commit-first judging removed the effect completely: 0 of 96"
[^c8]: doi-10-48550-arxiv-2609-00088 — "committed solution is correct, passing 3 of 3 held-out checks"
[^c9]: doi-10-48550-arxiv-2609-00088 — "On the duration parsing task it backfired, in both seeds."
[^c10]: doi-10-48550-arxiv-2609-00088 — "The other ended pinned at 0.667 while the evaluator read 0.99."
[^c11]: doi-10-48550-arxiv-2609-00088 — "only as good as the judge is at the task"
[^c12]: doi-10-48550-arxiv-2609-00088 — "Four small tasks, one judge family, one generator."
[^c13]: doi-10-48550-arxiv-2609-00088 — "so we claim that commit-first judging can lock the judge"
[^c14]: doi-10-48550-arxiv-2609-00088 — "single runs and carry no replication claim"
[^c15]: doi-10-48550-arxiv-2609-00088 — "so the commit-first frontier judge ran at default sampling"
[^c16]: doi-10-48550-arxiv-2609-00088 — "None implement the defence."
[^c17]: doi-10-48550-arxiv-2609-00088 — "Deployed systems then modify those templates."
[^c18]: doi-10-48550-arxiv-2609-00088 — "correctly handles touching intervals via the current start <= last end + 1 condition"
