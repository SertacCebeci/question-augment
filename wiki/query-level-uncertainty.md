---
description: "Uncertainty can be scored from the query alone, before any token is generated, as a knowledge-boundary signal that gates RAG, slower reasoning, cascading and abstention."
aliases: ["query-level uncertainty", "pre-generation uncertainty", "knowledge boundary detection before generation"]
sources: ["doi-10-48550-arxiv-2506-09669"]
---
# Query-level uncertainty

Most uncertainty measures for language models score an answer after it has been produced. The paper that names the alternative describes the usual target as "which measures the uncertainty associated with a specific answer".[^c1] Query-level uncertainty scores the query itself, prompt tokens included, and asks a different question: "can we determine whether the model can address it before generating any tokens?"[^c2] The shift is from post-generation to pre-generation, and the stated reason is cost: "our approach shifts from post-generation to pre-generation".[^c3] The authors add that it "approach avoids the computational cost of generating potentially long answers".[^c4]

A score needs a boundary to be checked against, and the paper defines the boundary by behaviour rather than by introspection. A query lies inside the model's knowledge boundary "if the LLM can produce a correct answer under greedy decoding"; failure to do so places it beyond.[^c5] The authors present this as a proxy, not an absolute measure: "serves as a heuristic indicator of internal knowledge".[^c6] The target is therefore indexed to one model and one decoding rule. A query beyond one model's boundary may lie inside another's; that consequence is mine, not stated in the text.

What the score buys is a decision taken before the costly step, so it can gate what comes next. The figure caption says query-level estimation "distinguishes answerable from non-answerable queries (knowledge boundary) before generating answers".[^c7] The introduction gives the purpose: if a model can "distinguish answerable from non-answerable or simple from hard queries, they can smartly perform" adaptive inference.[^c8] The adaptive moves the paper names are invoking retrieval, slow and deep thinking, cascading to a larger model, and abstaining. Each needs a cheap signal that the model may not know the answer, read before the answer is paid for.

The scope is narrow on purpose. The formulation "mostly targets epistemic uncertainty of the model"[^c9], and the study covers "queries with definite and clear-cut answers, as in factual QA".[^c10] Open and subjective questions are set aside: "contentious queries with open and subjective answers are also important".[^c11]

The same boundary can be estimated on the answer side. [[knowledge-boundary-aware-reward]] samples several responses per query and sets a solvability flag from whether any is correct, online during reinforcement learning. That route pays for generation. The query-level route reads one forward pass. My reading, not the paper's claim, is that the two estimate the same boundary at different costs, and that only the query-level one can decide before any answer exists.

## Limits

- The label is greedy success. The paper's own caveat is that greedy decoding "may not always reflect" the best a model can do, since beam search may surface a better answer.[^c12] The authors accept this for efficiency and reproducibility, treating a successful greedy decode as a fast proxy.[^c16]
- Ambiguity is set aside. "We treat such aleatoric effects as negligible for the purposes of focusing on epistemic uncertainty."[^c13] The authors also admit that "we acknowledge that residual ambiguity may persist".[^c14] So a query that is ambiguous rather than unknown may be scored as beyond the boundary. That is my inference from the setup, not a result the paper reports.
- Open-ended and subjective queries are untested, as the scope above says. Nothing here establishes the score for them.
- The best query-level measure in the paper still trails answer-level ones: "its performance still lags behind answer-level approaches".[^c15] Cheaper is the claim; more accurate is not.

## Related

- [[internal-confidence]] — the training-free readout the paper proposes for this score.
- [[pre-generation-success-probe]] — a supervised probe on the same pre-generation state, scored against greedy, Maj@K or Pass@K success on math and code rather than on factual queries.
- [[knowledge-boundary-aware-reward]] — the answer-side use of a solvability estimate from sampled responses, to set an abstention reward.
- [[abstention]] — where a query beyond the boundary is sent, one of the uses the paper names.
- [[step-level-retrieval-trigger]] — retrieval gated by an uncertainty score, but fired inside a reasoning chain rather than before the query is answered.

[^c1]: doi-10-48550-arxiv-2506-09669 — "which measures the uncertainty associated with a specific answer"
[^c2]: doi-10-48550-arxiv-2506-09669 — "can we determine whether the model can address it before generating any tokens?"
[^c3]: doi-10-48550-arxiv-2506-09669 — "our approach shifts from post-generation to pre-generation"
[^c4]: doi-10-48550-arxiv-2506-09669 — "approach avoids the computational cost of generating potentially long answers"
[^c5]: doi-10-48550-arxiv-2506-09669 — "if the LLM can produce a correct answer under greedy decoding"
[^c6]: doi-10-48550-arxiv-2506-09669 — "serves as a heuristic indicator of internal knowledge"
[^c7]: doi-10-48550-arxiv-2506-09669 — "distinguishes answerable from non-answerable queries (knowledge boundary) before generating answers"
[^c8]: doi-10-48550-arxiv-2506-09669 — "distinguish answerable from non-answerable or simple from hard queries, they can smartly perform"
[^c9]: doi-10-48550-arxiv-2506-09669 — "Our problem formulation mostly targets epistemic uncertainty of the model"
[^c10]: doi-10-48550-arxiv-2506-09669 — "Our study focuses on queries with definite and clear-cut answers, as in factual QA"
[^c11]: doi-10-48550-arxiv-2506-09669 — "contentious queries with open and subjective answers are also important"
[^c12]: doi-10-48550-arxiv-2506-09669 — "While greedy decoding ensures deterministic measurement, it may not always reflect"
[^c13]: doi-10-48550-arxiv-2506-09669 — "We treat such aleatoric effects as negligible for the purposes of focusing on epistemic uncertainty."
[^c14]: doi-10-48550-arxiv-2506-09669 — "we acknowledge that residual ambiguity may persist"
[^c15]: doi-10-48550-arxiv-2506-09669 — "its performance still lags behind answer-level approaches"
[^c16]: doi-10-48550-arxiv-2506-09669 — "treats a successful greedy decode as a signal that the model knows how to"
