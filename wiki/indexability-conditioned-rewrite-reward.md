---
description: "A rewrite is rewarded for popularity only after clearing a similarity threshold, with historical query volume as a proxy for whether the search index can match it."
aliases: ["query-volume reward", "popularity-conditioned rewrite reward", "zero-recall reward shaping", "indexability reward"]
sources: ["arxiv-2602-17667"]
---
# Indexability-conditioned rewrite reward

A generative rewriter can produce a query that means the right thing but is rare or unusual enough that the search system returns nothing for it. The authors call this the zero-recall problem: generated queries "that they fail to retrieve" valid results from the existing index.[^d1] Their reward is built to address this without letting popularity override meaning.

The mechanism has two levels. A rewrite is first scored for semantic fidelity, using ROUGE-L against the target query "as the evaluation score." If that similarity is below a threshold, the reward is the similarity alone. If it clears the threshold, the reward is a base value of 1 plus a bonus. The bonus is a clipped log of the rewrite's historical query volume (how often that exact query was issued in the system logs), and that volume is the signal used as "a proxy for indexability."[^d2]

The ordering is the point. The threshold makes the model "prioritize semantic fidelity before optimizing for search popularity," so popularity only ever adds to a rewrite that already means the right thing.[^d3] The reward is then used in GRPO, which normalises each rewrite's reward against the other rewrites sampled for the same input, so no separate value network is trained.[^d4]

## What was measured

In the paper's offline ablation, the version with the query-volume bonus reached accuracy 0.583, against 0.564 for the GRPO variant without it. The authors say the bonus "further improves Acc" by that margin.[^d5] On the query-volume side, the share of generated queries whose volume improved relative to the SFT baseline "reaches 20.21%" when the bonus is in the reward.[^d6]

The accuracy metric is a weighted mix of BLEU-4, ROUGE-L and BERT-score, with weights the authors describe as "empirically set to balance lexical and" semantic terms.[^d7] So the gain is measured on that composite, not on retrieval outcomes.

## Limits

- The text does not test whether a rewrite with high query volume retrieves better results or gets more clicks. Volume is a proxy the authors chose; the online test measures the whole system, not this reward.
- The gap of 0.019 in accuracy comes from one training configuration. The text I read gives no variance across seeds, so its size is not known to be stable.
- The clipping bounds, the scaling coefficient and the threshold are named in the formula but not given numerically in the text I read.
- A volume bonus can pull generated rewrites toward head queries that are already common. That narrows the space of formulations the rewriter explores; I did not find this tested, and it is my inference.
- The index that the reward aims at covers, by the authors' account, "approximately 83% incoming queries."[^d8] Queries outside it get no retrieval benefit from the reward, and the text does not say how those queries are served.
- The whole design is for a platform with a large query log. Where no such log exists, volume is not available as a signal, and the note's mechanism does not apply.

## Related

- [[context-gated-query-rewriting]] — the other half of the same work: deciding whether to rewrite at all before deciding what a rewrite should look like.
- [[group-relative-advantage]] — the group-normalised advantage this reward is fed into under GRPO.
- [[real-query-distribution-transfer-failure]] — a neighbouring concern, a gap between the queries a system is built on and the queries it later serves; I did not read that note closely for this one.

[^d1]: arxiv-2602-17667 — "queries that are sufficiently rare or complex that they fail to retrieve"
[^d2]: arxiv-2602-17667 — "serving as a proxy for indexability"
[^d3]: arxiv-2602-17667 — "fidelity before optimizing for search popularity"
[^d4]: arxiv-2602-17667 — "we employ GRPO to optimize the policy without the"
[^d5]: arxiv-2602-17667 — "further improves Acc to 0.583"
[^d6]: arxiv-2602-17667 — "reaches 20.21%"
[^d7]: arxiv-2602-17667 — "The weights are empirically set to balance lexical and"
[^d8]: arxiv-2602-17667 — "can cover approximately 83% incoming queries"
