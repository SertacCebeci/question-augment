---
description: "Laser's retrospection lets a search agent discard a faulty decomposition and rebuild the whole plan; the paper finds plan rebuilds more common than re-solving single sub-answers."
aliases: ["replanning", "revisit-task retrospection", "plan-level self-correction"]
sources: ["arxiv-2512-20458"]
---
# Plan-level retrospection

A multi-hop search agent commits early: it writes a decomposition and then solves the parts. Laser adds a retrospection space to its action set with two actions. The first, revisit-task, applies "when a previously solved sub-task is suspected to be incorrect, which may potentially block the progress of the current reasoning path": the agent "re-executes the sub-task to produce corrected results."[^c1] The second, replanning, applies "when the current reasoning trajectory becomes unsolvable due to an insufficient or flawed DAG decomposition, this action triggers reconstruction of an improved DAG plan."[^c2]

The distinction matters. Revisit repairs an answer; replanning repairs the decomposition that produced the question set. The authors read their own counts this way: "when encountering impasses, the agent is more inclined to restructure the global DAG plan rather than re-solving individual sub-tasks."[^c3] Their inference from that is that "inadequacies in the initial task decomposition may be a more common bottleneck than isolated sub-task errors."[^c4] The claim is about where errors sit in a multi-hop run: in the plan, more often than in a single hop.

Discarded plans are kept, not thrown away. The planning-history slot of the [[context-register]] archives every plan that was dropped, and its stated purpose is "preventing the agent from re-entering previously invalid planning states."[^c5] A retrospection step is therefore a move forward through plans, with a record of the dead ends already tried. Without the archive, a rebuild could return to a decomposition the agent had already rejected.

On the evidence side the paper reports two things. Samples with correct final answers "exhibit substantially higher execution rates of retrospection actions than those with incorrect answers."[^c6] And removing the retrospection actions lowers scores: the authors write that the result "demonstrates the necessity of incorporating structured retrospection: complex multi-hop tasks rarely follow a perfect reasoning trajectory on the first attempt."[^c7] The second result is the causal one; the first is a comparison of groups.

The paper's own framing is that a plan is a decomposition into sub-tasks linked by dependencies, so a bad plan is a bad graph. Related trigger designs exist elsewhere. [[confidence-gated-query-decomposition-tree]] splits a query when the model's token-probability confidence is low, which is a local decision made at the query level. [[entropy-gated-forced-reconsideration]] forces a second look when uncertainty is high. Laser's replanning fires on the agent's own judgment that a trajectory is stuck. These are different triggers for a similar repair, and no source here compares them. (My inference.)

## Limits

- The correct-versus-incorrect comparison groups samples by whether a retrospection action occurred. Harder questions plausibly trigger more retrospection and also get more wrong answers, so the group difference does not show that retrospection causes correct answers. Only the removal ablation speaks to cause, and it is run on one system.
- The trigger is the model's judgment that a trajectory is "unsolvable." The text does not measure false triggers, meaning a replan on a plan that was in fact fine, or what those cost in tokens and calls.
- The experiments use Qwen2.5 and Qwen3 models with search tools on multi-hop QA. "Solved" there is a checkable answer. For open-ended questions with no sub-answer that can be wrong, the notion of an impasse has nothing to bite on. (My inference.)
- Laser's "problem framing" means building the DAG of sub-tasks. That is a different sense from the problem-setting framing in [[problem-framing]], where the dimensions of the problem are posited rather than decomposed. The two should not be merged.
- The paper's own inference that decomposition is the usual bottleneck rests on which action was taken, not on an independent measure of decomposition quality. It is a reading of the counts, not a separate finding.

## Related

- [[context-register]] — holds the discarded-plan archive that retrospection draws on
- [[confidence-gated-query-decomposition-tree]] — a confidence-triggered split of a query, a different trigger for decomposing again
- [[entropy-gated-forced-reconsideration]] — a forced second look on uncertainty, close in spirit to a revisit
- [[problem-framing]] — the other sense of "framing"; Laser's version is decomposition, not problem setting
- [[plan-prefix-rewind]] — a judge-gated rejection of a short plan that resamples only the prefix; Laser's replanning is self-triggered and rebuilds the whole DAG

[^c1]: arxiv-2512-20458 — "When a previously solved sub-task is suspected to be incorrect, which may potentially block the progress of the current reasoning path, the agent re-executes the sub-task to produce corrected results."
[^c2]: arxiv-2512-20458 — "When the current reasoning trajectory becomes unsolvable due to an insufficient or flawed DAG decomposition, this action triggers reconstruction of an improved DAG plan."
[^c3]: arxiv-2512-20458 — "when encountering impasses, the agent is more inclined to restructure the global DAG plan rather than re-solving individual sub-tasks."
[^c4]: arxiv-2512-20458 — "inadequacies in the initial task decomposition may be a more common bottleneck than isolated sub-task errors"
[^c5]: arxiv-2512-20458 — "preventing the agent from re-entering previously invalid planning states."
[^c6]: arxiv-2512-20458 — "samples with correct final answers exhibit substantially higher execution rates of retrospection actions than those with incorrect answers."
[^c7]: arxiv-2512-20458 — "demonstrates the necessity of incorporating structured retrospection: complex multi-hop tasks rarely follow a perfect reasoning trajectory on the first attempt"
