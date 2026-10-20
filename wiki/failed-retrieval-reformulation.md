---
description: "When a sub-question's retrieved context does not contain its answer, the model is trained to rewrite the next sub-question instead of emitting an irrelevant or 'not found' answer."
aliases: ["query reformulation after failed retrieval", "retry with a rewritten sub-query", "failed-retrieval sub-question rewrite"]
sources: ["arxiv-2512-05336"]
---
# Reformulation after failed retrieval

A multi-hop chain can stall at a lookup. The passages it retrieved do not contain the sub-answer it asked for, and the chain has to do something next. It can accept what the passages offer, or it can rewrite the query that missed. PATHFINDER trains the second move on purpose: its authors describe the method as one that "reformulates sub-queries to handle failed retrieval cases",[^c1] and the target model is trained to "reformulate sub-questions when" the sub-answer cannot be found in the retrieved context.[^c2]

The move changes the next sub-question's content, not its goal. In the paper's worked case, a question asks which of two directors died earlier, and the lookup for one director's death date returns passages about several people with the same name. The trace records the miss and rewrites the query: "we need to refine the query to include more specific details",[^c3] adding "film director" as a disambiguator before asking for the date again. The paper's contrast case, a baseline without the move, answers from passages that do not support the answer. The authors say PATHFINDER "tries to re-query the retriever by reformulating with more relevant information in the next sub-question", where the baseline produces "an irrelevant extracted answer".[^c4]

The trigger is the miss itself. The paper's own framing of the situation is "When the retrieved context does not answer the question".[^c5] The rewrite is therefore conditional on a failed lookup, and the chain's plan is otherwise left alone.

The training pipeline also has a rule that depends on this move. Its judge counts a sub-question as redundant when it "attempts to retrieve information that has already been" obtained, and it exempts a reissued query after a miss: "reformulations following a failed retrieval attempt are acceptable."[^c6] So a repeated lookup is penalised, while a retry after failure is not. The source states this difference only in that one sentence; no separate measurement is given.

## Limits

- No ablation removes the reformulation. The paper's ablation (Table 2) varies only the trace filters. The reformulation's share of the gains over DeepRAG in Table 1 is not separated from the tree-generated data or the retriever. This is my reading of the tables.
- The text makes a general claim about "sub-question reformulation capability" but gives one worked trace (Figure 3) and no count of how often the rewrite fires or how often it recovers the answer.
- The trigger is a lookup that returns nothing usable. A retrieval that returns a plausible but wrong passage is a different failure, and the paper does not separate it.
- Retrieval is ColBERTv2 over a December 2021 Wikipedia dump with top-3 passages. How often the miss occurs under other retrievers is not reported.
- The evidence is one paper on Wikipedia multi-hop QA. Nothing here tests open-ended questions, where a "failed retrieval" has no clear answer key.

## Related

- [[evidence-guided-query-reformulation]] — revises the query from evidence that was found, through a residual need; this note's trigger is evidence that was not found. Whether the two combine is not tested in either work.
- [[plan-before-search-anchoring]] — holds each query to a fixed plan step, the opposite pressure. A rewrite after a miss moves the wording while keeping the step's goal (my reading).
- [[self-ask-decomposition]] — the sub-question loop that this rewrite sits inside.
- [[step-level-retrieval-trigger]] — decides when to retrieve inside a chain; this note concerns what to ask after a retrieval has failed.
- [[multi-hop-trace-error-score]] — the judge whose redundancy rule exempts reissued sub-questions after a miss.

[^c1]: arxiv-2512-05336 — "reformulates sub-queries to handle failed retrieval cases"
[^c2]: arxiv-2512-05336 — "trains the LLM to reformulate sub-questions when"
[^c3]: arxiv-2512-05336 — "we need to refine the query to include more specific details"
[^c4]: arxiv-2512-05336 — "tries to re-query the retriever by reformulating with more relevant information in the next sub-question"
[^c5]: arxiv-2512-05336 — "When the retrieved context does not answer the question"
[^c6]: arxiv-2512-05336 — "failed retrieval attempt are acceptable"
