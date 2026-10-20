---
description: "When wording and structure diverge, embedding retrievers rank by literal tokens: zero Hit@1 under heavy disguise in math, below chance in agent trajectories, though the answer is retrievable."
aliases: ["surface-form bias in structural retrieval", "retrieved but not ranked", "structural retrieval failure"]
sources: ["doi-10-48550-arxiv-2609-01556"]
---
# Embedding retrieval literal-token anchoring

Embedding retrieval is usually validated where wording and meaning agree. Rashid and Kellis separate them on purpose in two unrelated domains under one protocol: competition mathematics (500 queries, 117,088-item corpus) and ALFWorld agent trajectories (118 queries, 336 trajectories).[^c1]

## What was measured

- **Mathematics.** At the heaviest disguise tier strict Hit@1 is 0.0% for both production embedders, the correct item sits in the top 10 nearly always, and in 95.2 to 99.8% of misses the winning candidate is more lexically similar to the query than the correct answer.[^c2] The item is retrieved but not ranked: the failure is in ordering, not recall.
- **Trajectories.** Strict gold requires the same task type but a different target object. Embedders land at or barely above hypergeometric chance (for example 17.8% versus chance 15.3%); when gold must also differ in receptacle, "all three embedders fall below chance (Figure 3)."[^c3] Below chance is read as active steering, not indifference, and the steering is attributed to token anchoring.[^c4]
- The mechanisms differ (below chance versus zero-but-retrievable); the direction is the same: rankings follow the query's literal tokens.[^c5]

## Downstream consequence

In a paired experiment, oracle retrieval was statistically indistinguishable from adversarially bad retrieval (McNemar p = 0.678). The authors explain it by the solver's accuracy being largely a truncation proxy, leaving retrieval little headroom.[^c6] So a retrieval failure need not show up as an answer failure when the solver already succeeds without help.

## Limits

- Two domains, a few embedders; the mathematics queries were paraphrased by a Gemini-family model, a provenance confound the authors flag.
- The trajectory subsets differ (original 40 harder than added 78), a benchmark-construction effect confounded with phrasing.
- That the downstream null reflects truncation headroom is the authors' reading; it does not show retrieval is useless for harder tasks.
- The sub-chance reading under definition (ii) is an interpretation of a statistical pattern, not a direct probe of internals.

## Related

- [[lexical-reranker-sign-diagnostic]] — the cheap control that distinguishes adversarial from incidental surface variation
- [[dispersed-evidence-retrieval-collapse]] — another case where retrieval fails despite evidence being present
- [[real-query-distribution-transfer-failure]] — benchmark construction vs the target distribution
- [[prompt-content-over-surface-form]] — surface form versus content as a driver of outcomes

[^c1]: doi-10-48550-arxiv-2609-01556 — "Embedding retrieval is usually validated where surface form and meaning point the same"
[^c2]: doi-10-48550-arxiv-2609-01556 — "nearly always, and in 95.2 to 99.8% of misses the candidate that wins is more lexically similar"
[^c3]: doi-10-48550-arxiv-2609-01556 — "all three embedders fall below chance (Figure 3)."
[^c4]: doi-10-48550-arxiv-2609-01556 — "Retrieval anchors on literal tokens."
[^c5]: doi-10-48550-arxiv-2609-01556 — "In both cases these embedding models rank by literal surface content."
[^c6]: doi-10-48550-arxiv-2609-01556 — "oracle retrieval was statistically indistinguishable from adversarially bad retrieval (McNemar"
