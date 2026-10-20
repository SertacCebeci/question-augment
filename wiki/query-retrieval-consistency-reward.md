---
description: "A generated query is scored by what it retrieves, not by its own appeal: a reward checks the query and the items it pulls up against ground truth, so clicks and conversions can diverge."
aliases: ["query-product consistency reward", "chain-of-retrieval outcome reward", "retrieval-outcome reward for query generation"]
sources: ["doi-10-48550-arxiv-2606-05671"]
---
# Query-retrieval consistency reward

A query offered to a user can succeed on two counts. The first is whether the user clicks the query. The second is whether the products that query retrieves are the ones the user goes on to engage with. Most generators are trained for the first count alone. QueryAgent-R1 (Sun et al., 2026) argues that this leaves a gap: "the above methods primarily optimize query-level relevance".[^c1] The authors name the failure directly: "This mismatch often leads to high query click" through rates while product conversion stays low.[^c2]

The proposed remedy has two parts. The first is to make the generator check its own output against the inventory. The agent "validate and refine queries based on retrieved" products before it returns a query.[^c3] The second is to put the downstream outcome into the reward. The paper casts the task as a chain: the objective multiplies the probability that the query is clicked by the probability that the items it retrieves are clicked, which the authors call "as a Chain-of-Retrieval optimization problem".[^c4] Because the paper has no conversion labels at training time, item clicks serve as the stand-in: "clicks as a dense proxy for sparse conversion signals".[^c5]

The reward itself is what the note is about. The paper's summary of the consistency term is "Query EM & Item Hitrate": a generated query earns credit when it exactly matches the ground-truth query, and earns item credit when the items it retrieves hit the ground-truth item set.[^c6] This is added to the reinforcement-learning signal next to a format term, so, on my reading of the figure, a rollout that is well formed but retrieves nothing relevant scores lower than one that retrieves a hit. The figure's formulas also add ROUGE terms over query text and item titles; the figure's text is rough, so that detail is my reading, not something the prose states.

What the paper measures for the reward is a set of end-to-end counts, not a separate test of the reward. On the industrial dataset, adding product retrieval to single-turn reinforcement learning "improves Cons@1 from 0.021 to" 0.031, and the paper says this shows "helps reduce invalid queries".[^c7] The memory abstraction step is credited with a larger step on the same metric: "Incorporating Memory Abstract brings the significant intermediate" gain, lifting Cons@1 from 0.031 to 0.064.[^c8] The final reranking step lifts it to 0.117: "Finally, RAG Rerank further raises" the hit rate and consistency together.[^c8] In the online A/B test on a production platform, the paper reports that QueryAgent-R1 "improves Query CTR by 2.9% and guided CVR" by 3.1%.[^c9] The authors read the online result as evidence that "This strong online performance shows that our Consistency Reward effectively bridges" the generation-retrieval gap.[^c10]

The reward is also sensitive to how several rewards are optimized together. The paper compares its own multi-reward setup under two policy-optimization methods, and reports that "GRPO often struggles to balance competing reward signals".[^c11] On the consistency score the gap is large: GDPO "reaches a plateau of approximately 0.12", while GRPO sits near half that level in the paper's figure.[^c12]

This is one object: a reward that scores a generated query by the retrieval it triggers. It is not a click model, and it is not a reward for asking a human a question. The paper's setting is query recommendation "without user input", so the transfer to a person asking a question is my inference, not a result.[^c13]

## Limits

- The evidence is one industrial system and two datasets, one of them proprietary. The online effect is reported as a relative lift of 2.9% in query CTR and 3.1% in guided CVR; the A/B design and its variance are not described in the passages read here.
- Conversion is never observed in the reward. Item clicks are a dense proxy, and the reward treats a clicked item as a hit. A query whose retrieved items are clicked and then not bought would, on my reading, still score as a success. The paper does not separate these.
- Table 2 adds components in sequence (single-turn RL, product retrieval, memory abstraction, reranking). In the rows read here no run removes the consistency reward while keeping the rest. So the reward's own contribution is not isolated; the gains are attributed to the components as a whole. This reading of the table is mine.
- The reward depends on ground-truth queries and item sets drawn from logs. A setting without logged query-to-click pairs has no target to score against, and the paper does not address that case.
- Cost: the authors say "QueryAgent-R1 is currently limited by its online" inference efficiency, and that the asynchronous deployment "it also increases system complexity and may constrain real-time responsiveness".[^c14][^c15] The full model raises p99 latency: "Although the full model increases p99 latency to 1,973 ms" the paper says the cost is handled by asynchronous precomputation.[^c16]
- The multi-reward comparison is the authors' own, on their own setup. The gradient-interference account is their explanation, not a separate measurement.

## Related

- [[feedback-gated-query-reformulation]] — also decides from what a search returns, but chooses whether to rewrite a query; here the retrieved items enter the reward used to train the generator.
- [[question-reconstructability-reward]] — another outcome-proxy reward for search, scored by whether the original question can be recovered from the trajectory rather than by retrieved items.
- [[answer-reasoning-consistency-reward]] — a consistency reward between reasoning and answer; the consistency here is between a query and the items it retrieves.
- [[recommendation-entropy-reward]] — a reward for conversational recommendation that mixes a ground-truth hit rate with another term; the same hit-based idea in a different setting.
- [[context-gated-query-rewriting]] — another deployed query rewriter read through online click-through; neither note settles what the other's reward should score.

[^c1]: doi-10-48550-arxiv-2606-05671 — "the above methods primarily optimize query-level relevance"
[^c2]: doi-10-48550-arxiv-2606-05671 — "This mismatch often leads to high query click"
[^c3]: doi-10-48550-arxiv-2606-05671 — "validate and refine queries based on retrieved"
[^c4]: doi-10-48550-arxiv-2606-05671 — "as a Chain-of-Retrieval optimization problem"
[^c5]: doi-10-48550-arxiv-2606-05671 — "clicks as a dense proxy for sparse conversion signals"
[^c6]: doi-10-48550-arxiv-2606-05671 — "Query EM & Item Hitrate"
[^c7]: doi-10-48550-arxiv-2606-05671 — "Adding Product Retrieval improves Cons@1 from 0.021 to"
[^c8]: doi-10-48550-arxiv-2606-05671 — "Incorporating Memory Abstract brings the significant intermediate"
[^c9]: doi-10-48550-arxiv-2606-05671 — "improves Query CTR by 2.9% and guided CVR"
[^c10]: doi-10-48550-arxiv-2606-05671 — "This strong online performance shows that our Consistency Reward effectively bridges"
[^c11]: doi-10-48550-arxiv-2606-05671 — "GRPO often struggles to balance competing reward signals"
[^c12]: doi-10-48550-arxiv-2606-05671 — "of GDPO reaches a plateau of approximately 0.12"
[^c13]: doi-10-48550-arxiv-2606-05671 — "our work focuses on e-commerce query recommendation without user input"
[^c14]: doi-10-48550-arxiv-2606-05671 — "QueryAgent-R1 is currently limited by its online"
[^c15]: doi-10-48550-arxiv-2606-05671 — "it also increases system complexity and may constrain real-time responsiveness"
[^c16]: doi-10-48550-arxiv-2606-05671 — "Although the full model increases p99 latency to 1,973 ms"
