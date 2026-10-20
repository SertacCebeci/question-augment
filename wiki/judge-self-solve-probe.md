---
description: "A judge's own solve rate, scored against checks it never sees, predicts in advance where committing to its answer is safe; competence depends on the judge and task, not model scale."
aliases: ["solve-rate probe", "judge self-solve test", "judge competence probe"]
sources: ["doi-10-48550-arxiv-2609-00088"]
---
# Judge self-solve probe

The probe asks a judge model to solve each task directly, with no candidate in view, and scores its answers against checks it never sees. The work used three samples per task, so twelve calls per judge: "We asked each judge model to solve each task directly, three samples per task".[^p1] The cost is trivial. In the paper's words the precondition "is measurable in advance, for pennies,"[^p2] using checks the judge has never seen.

The probe measures the judge and task together, not the model's tier. On the interval merging task the frontier judge solved the task once in three.[^p3] Its wrong answers were "variants of the same touching-intervals misconception the search exploited."[^p4] The smaller judge solved the same task three times in three, and it was the judge that resisted gaming.[^p5] On the duration parsing task neither judge solved the task even once.[^p6] The paper states the lesson as "Judge reliability is a property of the judge and task pair, not of the" model tier, and that "It also proved task local rather than scale dependent."[^p7][^p8]

The probe lined up with the outcomes of [[commit-first-judging]]. The paper says these are "exactly the two tasks where commit-first judging helped and where it backfired."[^p9] On the duration task the frontier judge's committed answer "scores 0.667 on the held-out checks, failing the one that rejects malformed duration strings"[^p10], and the probe had already shown that judge could not solve the task. That is the failure the probe is meant to flag before a search runs.

My reading, not the paper's: the probe checks a precondition. If the judge's committed answer is correct, matching candidates against it removes the gap between score and correctness. If it is wrong, the defence turns the judge's error into the target. So the judge's own solve rate, measured in advance, tells you whether its answer is a safe anchor at all. The same logic applies to any proxy that is exploited past the point where it tracks what it measures, the general pattern in [[reward-overoptimization]].

## Limits

- Three samples per task is coarse. The paper does not state a threshold. One solve in three was enough for the defence to help on one task. That is evidence against requiring that the judge always solves the task, but the cut between safe and unsafe is my inference from two tasks and was not measured.
- The probe ran separately from the search runs. "probe, not from the runs themselves"[^p11] is the paper's own caveat. The logged committed answer on the interval task was correct in that run, though the probe gave one solve in three. The two readings do not line up exactly, so the probe is an ordinal guide, not a per-run prediction.
- The evidence is "Four small tasks, one judge family, one generator."[^p12] Two of the four had headroom for gaming. One judge family and two tasks with headroom cannot establish that the probe generalises to other judges or to harder tasks.
- The probe is only as good as its checks. The paper's audit found one of thirteen held-out checks unreachable and two checks the specification does not justify. "Two flagged checks reached the paid runs anyway."[^p13] A probe scored against such checks inherits their error.
- The probe measures correctness on the task. It does not measure susceptibility to other forms of gaming. Strict-mode binarisation of the judge score "did not prevent the effect."[^p14]

## Related

- [[commit-first-judging]] — the defence this probe is a precondition for; the probe is the check that the judge's own answer can be trusted to anchor it
- [[reward-overoptimization]] — the general failure a proxy shows when pushed past what it measures
- [[llm-judge-biases]] — the reasoning-grading weakness that the note there links to solving first

[^p1]: doi-10-48550-arxiv-2609-00088 — "We asked each judge model to solve each task directly, three samples per task"
[^p2]: doi-10-48550-arxiv-2609-00088 — "is measurable in advance, for pennies,"
[^p3]: doi-10-48550-arxiv-2609-00088 — "The frontier judge solves the interval task 1 time in 3."
[^p4]: doi-10-48550-arxiv-2609-00088 — "variants of the same touching-intervals misconception the search exploited"
[^p5]: doi-10-48550-arxiv-2609-00088 — "The smaller judge solves the same task 3 of 3, and it is the judge that"
[^p6]: doi-10-48550-arxiv-2609-00088 — "Neither judge solves the duration task even once"
[^p7]: doi-10-48550-arxiv-2609-00088 — "Judge reliability is a property of the judge and task pair, not of the"
[^p8]: doi-10-48550-arxiv-2609-00088 — "It also proved task local rather than scale dependent."
[^p9]: doi-10-48550-arxiv-2609-00088 — "exactly the two tasks where commit-first judging helped and where it backfired."
[^p10]: doi-10-48550-arxiv-2609-00088 — "failing the one that rejects malformed duration strings"
[^p11]: doi-10-48550-arxiv-2609-00088 — "probe, not from the runs themselves"
[^p12]: doi-10-48550-arxiv-2609-00088 — "Four small tasks, one judge family, one generator."
[^p13]: doi-10-48550-arxiv-2609-00088 — "Two flagged checks reached the paid runs anyway."
[^p14]: doi-10-48550-arxiv-2609-00088 — "did not prevent the effect"
