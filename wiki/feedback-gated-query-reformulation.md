---
description: "In iterative text-to-video retrieval, a controller decides each round whether to keep the current query or reformulate it, from how well the results so far match the request."
aliases: ["adaptive query reformulation", "explore-exploit query reformulation", "orchestrated query rewriting", "reformulate-or-exploit gate"]
sources: ["arxiv-2602-19040"]
---
# Feedback-gated query reformulation

An iterative search that returns a weak ranked list can do two things next. It can keep working through the list it already has, or it can rewrite the query and search again. Most fixed pipelines pick one of these in advance. The multi-agent retrieval framework of arXiv:2602.19040 makes the choice per round, from feedback. Its reasoning agent "is responsible for exploitation", filtering the candidates a search has returned, while a query reformulation agent "facilitates exploration by generating alternative queries".[^c1] Which of the two runs is not fixed. An orchestration agent "dynamically decides whether to continue exploiting current results or initiate exploration via reformulation".[^c2]

The mechanism has three parts. First, a scalable retrieval step ranks the corpus with a text-to-video embedding, and a reasoning step reads only the top candidates and sorts them into matches and non-matches. Second, the orchestrator reads the evaluation of the previous round and returns an action, explore or exploit, together with a textual reason. The paper's wording is that the orchestrator "determines whether to trigger query reformulation at each iteration".[^c3] The signal it reads is the share of the candidate list that the reasoning step accepted. In the paper's worked example, a round whose "match rate is only 33%" is taken as a sign that "the current query may be too broad or ambiguous".[^c4] That example is an illustration in a figure, not a measured threshold. Third, when the action is explore, the reformulation step receives "the original query q0 and the query used in the previous iteration" and writes a refined query.[^c5] Reformulation is therefore anchored to the original request, not a free walk away from it.

What the gate buys is shown only indirectly, through the ablation that adds components one at a time. Adding the reformulation agent to the retrieval-only baseline "improves performance on 165 out of 210 queries", with the paper counting 95 of those improvements on complex queries.[^c6] Adding it to a system that already had the reasoning agent is different: "it leads to performance drops", and the authors observe that "most of the queries with performance declines are relatively easy ones".[^c7] So a rewrite helps where the first query has failed and costs where the first query already worked. The ablation's reformulation-only arm rewrites "in every iteration", a greedy schedule.[^c8] The complete system, with the orchestrator added last, "yields the complete multi-agent retrieval system".[^c9] Read together, these describe the job the gate is meant to do: rewrite when the list says it should, and keep the list otherwise. Whether the gate does that better than the greedy schedule is the comparison the ablation is built to make; this note does not state its figures.

The gate is not the same as the rewrite after a missed lookup. The paper's own framing is that the reformulation agent helps "recovering performance for those that degrade over iterations".[^c10] In [[failed-retrieval-reformulation]] the trigger is a lookup that returns nothing usable, and the rewrite follows it. Here the trigger is a graded share of a ranked list, the decision is made by a language model reading the history, and a round can end with no rewrite at all. That last part is my reading of the design, not a result the paper reports.

## Limits

- The gain of the orchestrator over the greedy reformulation schedule rests on the paper's ablation table, whose figures this note did not extract. The text reports the final configuration; it does not, in the passages read here, give a standalone number for the gate.
- The controller is an LLM prompted with the evaluation history. No accuracy is reported for its explore/exploit decisions, and no fixed threshold on the match rate is compared against it.
- The reformulation's cost on easy queries is reported as a count of declines, not as a size. A gate that declines to rewrite easy queries would be expected to reduce that cost, but the paper does not test the reduction directly.
- The evaluation is TRECVid ad-hoc video search over three benchmarks, 210 queries in the eight sets. The complex-query subset was labelled by GPT-4, so the split the results depend on is itself a model judgement.
- The round budget is fixed (the text sets the retrieval iteration to T = 60). The paper does not, in these passages, vary it or show how often the orchestrator chose to explore.
- Nothing here tests open-ended search, where there is no candidate pool to score a match rate against.

## Related

- [[failed-retrieval-reformulation]] — rewrites after a lookup returns nothing usable; this gate reformulates from a graded share of a ranked list and can decline to reformulate.
- [[evidence-guided-query-reformulation]] — revises a query from evidence already found; it does not decide whether a revision should happen.
- [[response-triggered-explore-exploit-switching]] — the same explore/exploit vocabulary, applied to question pools in elicitation and switched by heuristics, not to search queries.
- query-outcome-memory-for-reformulation — the memory of earlier queries and their scores that the reformulation step reads alongside this gate.

[^c1]: arxiv-2602-19040 — "is responsible for exploitation"
[^c2]: arxiv-2602-19040 — "dynamically decides whether to continue exploiting current results or initiate exploration via reformulation"
[^c3]: arxiv-2602-19040 — "determines whether to trigger query reformulation at each iteration"
[^c4]: arxiv-2602-19040 — "The match rate is only 33%, which is relatively low"
[^c5]: arxiv-2602-19040 — "takes the original query q0 and the query used in the previous iteration"
[^c6]: arxiv-2602-19040 — "improves performance on 165 out of 210 queries when compared to the retrieval-only baseline"
[^c7]: arxiv-2602-19040 — "most of the queries with performance declines are relatively easy ones"
[^c8]: arxiv-2602-19040 — "use a greedy reformulation strategy that modifies the query"
[^c9]: arxiv-2602-19040 — "yielding the complete multi-agent retrieval system"
[^c10]: arxiv-2602-19040 — "recovering performance for those that degrade over iterations"
