---
description: "Under one scalar reward, a rollout that satisfies a criterion can get a non-positive group advantage, so the behaviour that criterion rewards is penalized or ignored instead of reinforced."
aliases: ["suppressed rubric criteria", "suppressed-criterion signal loss", "criterion signal suppression", "negative-advantage suppression"]
sources: ["doi-10-48550-arxiv-2607-18082"]
---
# Suppressed criteria

A criterion is *suppressed* when some rollouts satisfy it, yet the group-relative advantage those rollouts receive is not positive, so the behaviour the criterion rewards gets no push upward. The work gives two cases. In negative-advantage suppression, "where the advantage sum across all satisfying rollouts is negative."[^c1] In zero-advantage suppression the sum is zero, and the criterion is "rarely satisfied (e.g., by not more than half of the group)."[^c2]

The mechanism is reward ambiguity. Several criteria are folded into one scalar, and that scalar is "broadcast uniformly to the entire response."[^c3] A response can satisfy criterion C3 and miss others, and receive one number for all of its tokens. The text's example: "y2 and y3 satisfy criterion C3, but their advantage sum is negative."[^c4] The criterion-satisfying rollouts "receive negative or negligible aggregate advantages," which means "useful criterion-satisfying behaviors" are "penalized or ignored rather than reinforced."[^c5][^c6] The work's summary is that aggregating criteria into one scalar "obscures" each criterion's contribution.[^c7]

The failure is not rare in the work's one measured setting. Over 25% of samples carry a suppressed criterion throughout training of Qwen3-4B on RaR-Medicine.[^c8] The work states the scale of the problem in its own words, not as a benchmark result.

A point that is mine, not the work's: the same fact bears on how a rubric grades an answer. If a grader gives credit criterion by criterion, a response that gets one criterion right can still be pushed down by what it gets wrong elsewhere, once that grade is turned into a single number for learning. What a rubric measures and what a learner receives from it can therefore diverge. This is an inference from the mechanism; the text does not test it for answer evaluation.

## Limits

- The definition in the text is for binary criterion scores, where satisfaction means a score of 1.[^c9] Graded scores are not covered by the cases given.
- The zero-advantage case uses a cut at half the group. That cut is a choice in the definition, not a derived boundary (my inference).
- The sign of an advantage depends on group composition and on the group's mean and standard deviation. A criterion can be suppressed in one group and not in another, so the rate is a property of a sample, not of the criterion alone (my inference).
- The prevalence is reported for one model and one dataset in the introduction. Other settings and LLM judges are in an appendix: "More statistics of these two failure modes on other settings" that I did not read.[^c10]
- The text shows that suppression occurs. It does not, in the parts I read, isolate how much accuracy the lost signal costs. The work's remedy for it is evaluated in its own experiments on "five medicine and science benchmarks,"[^c11] which I did not check here.

## Related

- unexplored-criteria — the other failure in the same work: criteria that no rollout satisfies at all, so nothing is lost because nothing was found.
- [[ideal-solution-distance-reward]] — also treats a gain on one rubric as not automatically cancelling a loss on another, but changes the reward's distance rather than the group advantage.
- [[compensatory-leakage]] — another flaw of scalar combination, where a lower-priority gain overturns an earlier criterion's decision; there the flaw is in the decision rule, here in the advantage.
- [[within-group-ordinal-utility-aggregation]] — reduces each criterion to within-group outcomes before fusing them, so raw score magnitudes do not enter the reward: another response to the scalar-combination problem named here.

[^c1]: doi-10-48550-arxiv-2607-18082 — "where the advantage sum across all satisfying rollouts is negative"
[^c2]: doi-10-48550-arxiv-2607-18082 — "rarely satisfied (e.g., by not more than half of the group)"
[^c3]: doi-10-48550-arxiv-2607-18082 — "broadcasts it uniformly to the entire response"
[^c4]: doi-10-48550-arxiv-2607-18082 — "y2 and y3 satisfy criterion C3, but their advantage sum is negative"
[^c5]: doi-10-48550-arxiv-2607-18082 — "receive negative or negligible aggregate advantages"
[^c6]: doi-10-48550-arxiv-2607-18082 — "causing useful criterion-satisfying behaviors to be penalized or ignored rather than reinforced"
[^c7]: doi-10-48550-arxiv-2607-18082 — "aggregating multiple criteria into a single scalar reward obscures"
[^c8]: doi-10-48550-arxiv-2607-18082 — "over 25% of samples contain suppressed criteria throughout training"
[^c9]: doi-10-48550-arxiv-2607-18082 — "Consider the setting where each criterion-wise score is binary"
[^c10]: doi-10-48550-arxiv-2607-18082 — "More statistics of these two failure modes on other settings"
[^c11]: doi-10-48550-arxiv-2607-18082 — "Experiments on five medicine and science benchmarks"
