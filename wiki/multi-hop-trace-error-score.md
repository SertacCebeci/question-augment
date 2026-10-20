---
description: "Correct-answer multi-hop traces are filtered by a gold sub-answer recall gate and a judge's step-error count, so the kept trace is the least flawed one, not merely a correct one."
aliases: ["sub-answer recall gate", "trace error score", "weighted step-error score for reasoning traces", "answer-correct trace filtering"]
sources: ["arxiv-2512-05336", "doi-10-48550-arxiv-2609-01658"]
---
# Multi-hop trace error score

A search that rewards only the final answer produces many traces that end correctly, and some of them reach the answer through flawed steps. PATHFINDER keeps one trace per question with a two-stage filter. The concept is a choice of unit: the trace is scored by how many of its steps are wrong, and the answer is only one input to that score.

The first stage is a recall gate. "All traces with a sub-answer" recall of the golden sub-answers below 1 are discarded, so every fact the question needs must appear among the answered steps.[^c1]

The second stage is an LLM judge, Qwen2.5-72B-Instruct,[^c2] that is "instructed to output the number of erroneous steps in the CoT, along with a justification for each."[^c3] It scores four aspects. Incorrectness covers a step that "introduces unsupported entities or information".[^c4] Redundancy covers a sub-question that "attempts to retrieve information that has already been" obtained.[^c5] Irrelevance covers an answer that is "neither used directly in obtaining the final answer" nor used to reach a later useful sub-question.[^c6] Sub-answer faithfulness covers an answer where "the answer lacks clear supporting evidence in the context."[^c7]

The decision rule is two-part. Traces are discarded when the judge "flags issues related to the incorrectness or faithfulness".[^c8] Survivors receive "a weighted error score" built from their redundant and irrelevant steps.[^c9] The trace with the minimum score is kept, and "in case of a tie, we pick the one with the shortest length."[^c10] The text does not state the weights.

The reported effect is small at the first stage and larger at the second. The table caption describes the ablation as "Ablation analysis of PATHFINDER using Qwen-2.5-7BInstruct model".[^c11] Reading the table columns (my reading; the layout is not explicit in the text), 2WikiMultiHopQA exact match goes from 71.40 with shortest-path selection alone, to 71.90 with the recall gate, to 75.00 with the judge. On HotpotQA, the out-of-distribution set, it goes 39.30, 39.20, 39.70. The authors observe that "we see the biggest jump in accuracy with" the judge step.[^c12]

## Limits

- The judge is a 72B model from the same family as the teacher that generated the traces (Qwen-2.5-72B-Instruct). The text I read reports no agreement with human annotators, so whether the error counts match what a careful reader would flag is untested.
- The weights of the redundancy and irrelevance terms are not given, so the score cannot be reproduced from the text.
- The ablation is one model and one run per row, with no variance reported. The recall gate's 0.5-point gain on 2Wiki is within the spread one would expect from resampling (my inference), and on HotpotQA it is slightly negative.
- The shortest-trace tie-break favours shorter chains. A longer chain may carry a verification step that a shorter one drops; this is not tested.
- The recall gate needs golden sub-answers, which exist for the two training datasets (2WikiMultiHopQA and MuSiQue). A question with no decomposition annotation gives the gate nothing to check (my reading).
- The paper measures the filter only through downstream answer accuracy. It does not report the judge's error counts in aggregate, or the rate at which lucky guesses survive each stage.

## Related

- [[process-outcome-consistency-verification]] — the same failure, a right answer reached by a wrong route; there it is checked by a product of outcome and consistency indicators, here by counting erroneous sub-steps.
- [[mcts-training-trace-generation]] — the tree search that produces the traces this score filters.
- [[failed-retrieval-reformulation]] — the redundancy rule exempts a reissued sub-question after a failed lookup, so the score does not penalise a retry.
- [[refutation-based-entailment-check]] — a formal route to checking that a chain entails its conclusion; not applied to these traces in either work.
- [[evidence-grounded-step-reward]] — the step-level counterpart of this filter: a PRM scores each step inside a search tree for logic and grounding, so flawed steps lose value before a trace is kept.[^c13]

[^c1]: arxiv-2512-05336 — "All traces with a sub-answer"
[^c2]: arxiv-2512-05336 — "For LLM-as-Judge, we use the Qwen2.5-72B-Instruct model"
[^c3]: arxiv-2512-05336 — "The LLM Judge is instructed to output the number of erroneous"
[^c4]: arxiv-2512-05336 — "introduces unsupported entities or information"
[^c5]: arxiv-2512-05336 — "sub-question attempts to retrieve information that has already been"
[^c6]: arxiv-2512-05336 — "neither used directly in obtaining the final answer"
[^c7]: arxiv-2512-05336 — "the answer lacks clear supporting evidence in the context"
[^c8]: arxiv-2512-05336 — "Judge flags issues related to the incorrectness or faithfulness"
[^c9]: arxiv-2512-05336 — "score is assigned based on the number of redundant and irrelevant"
[^c10]: arxiv-2512-05336 — "In case of a tie, we pick the one with the shortest length"
[^c11]: arxiv-2512-05336 — "Ablation analysis of PATHFINDER using Qwen-2.5-7BInstruct model"
[^c12]: arxiv-2512-05336 — "we see the biggest jump in accuracy with"
[^c13]: doi-10-48550-arxiv-2609-01658 — "spurious successes where flawed retrieval coincidentally produces the correct answer"
