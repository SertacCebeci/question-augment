---
description: "Ranking and exemplar-selection queries carry more bits per answer than binary labels, but the best query type and set size flip once response time is priced in."
aliases: ["rich queries beyond labels", "listwise queries vs label queries"]
sources: ["arxiv-2602-15738"]
---
# Ranking-query information rate

A binary label query returns at most one bit per human interaction.[^c1] Two richer query types lift that cap: selecting the most representative exemplar from a set, and ranking the set and marking the last positive item. Which query to ask then depends on whether the cost to minimize is the number of interactions or the time spent.

## Mechanism

Annotator answers are modelled probabilistically on off-the-shelf embeddings. A ranking is a sequential selection process, the Plackett-Luce model, and marking the last positive item yields a threshold that implicitly labels every item in the list.[^c2] Selection queries gather up to log2 |S| more bits than a binary label, and a ranking returns a full ordering and complete labeling.[^c3] Under the response model, ranking queries subsume exemplar selection, so they give strictly more information; information gain also rises with set size |S|.[^c4]

The paper bounds the expected stopping time of the active-learning algorithm. Both bounds are lower for ranking than for selection, since ranking has more possible answers and a larger information lower bound. They grow with embedding dimension d.[^c5]

When cost differs across queries, the paper selects queries by information rate, the expected bits gained per unit cost.[^c6] With response-time models fitted from human experiments on word sentiment, ranking beats selection at every fixed |S|. Ranking's rate grows with |S| over the feasible range (|S| up to 10). Selection's rate peaks at |S| = 3 and falls on either side.[^c7] The optimum depends on the gain and cost models: changing the response-time model makes a two-word selection optimal.[^c8] In wall-clock time, selection from 10 words reduces error more slowly than selection from 3, because the extra time offsets the sample-complexity gain.[^c9]

## Limits

- Annotators are simulated from crowdsourced word-sentiment and image-aesthetic datasets, not live humans answering the new query types; the response-time models come from separate human experiments (my reading of the setup).
- The response model assumes perceived score relates to distance from the classifier in an embedding space; where that relation is weak (the abstract's reported fit is modest, R = 0.443 in one figure), the gains may not carry over.
- The reported savings (up to 85% fewer interactions, more than 57% less time) are task-specific and depend on the cost model.
- Binary classification only.
- Set sizes were capped at 10 by feasibility, and the cost models are estimated, so the optimal query is not stable across settings.

## Related

- [[voi-per-cost-modality-selection]] — the same gain-over-cost ratio, applied across query modalities in preference elicitation

[^c1]: arxiv-2602-15738 — "binary classifications, for which the information gained is inherently capped at just one bit"
[^c2]: arxiv-2602-15738 — "This response model is known as the Plackett-Luce model"
[^c3]: arxiv-2602-15738 — "gathering up to log2 |S| more bits of information per"
[^c4]: arxiv-2602-15738 — "Under our response model, ranking queries subsume exemplar selection queries; thus, they"
[^c5]: arxiv-2602-15738 — "Consequently, both bounds on the stopping time are lower for ranking queries,"
[^c6]: arxiv-2602-15738 — "the expected bits of information gained per unit cost:"
[^c7]: arxiv-2602-15738 — "questions, however, the information rate peaks at |S| = 3"
[^c8]: arxiv-2602-15738 — "query becomes a selection question with two words."
[^c9]: arxiv-2602-15738 — "selection from 10 words reduces error more slowly in time"
