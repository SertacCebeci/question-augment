---
description: "Whether extra retrieval is worth its tokens depends on recoverability: most multi-hop questions are already solved or unrecoverable, so a cheap router on first-pass features escalates only the rest."
aliases: ["RASER", "selective escalation router", "recoverability analysis", "bridgeable question routing"]
sources: ["doi-10-48550-arxiv-2606-02488"]
---
# Recoverability-aware selective escalation

Multi-step retrieval is usually applied to every question. Li, Yan and Käfer ask instead when additional retrieval is necessary, and answer by measuring, per question, what each expensive strategy would have gained over a one-shot answer.[^c1]

## Recoverability analysis

For each question they run one-shot dense RAG and bridge-style paths (PRUNE, IRCoT, Self-Ask) and compare answer F1 after the fact. This is an oracle: the gain if a router always chose the best path. Questions fall into three groups: already solved by one-shot retrieval, helped by bridging (at least 0.1 F1 better), and unrecoverable under every tested strategy.[^c2] The reported result is that only a minority gain at least 0.1 F1, many are already solved, and another 14-27% stay unrecoverable.[^c3] The share already solved by one-shot RAG ranges across readers from 53% (GPT-OSS-120B) down to 24% (Llama-3-8B), so the escalation target depends on the model as well as the question (my reading of the paper's Table 1). The reframing: the problem is "how to detect when bridge retrieval is worth paying for", not how to retrieve more.[^c4]

## The router

RASER is not a new retriever; it is a small decision layer after the first one-shot retrieve-and-answer.[^c5] Six features are available with no further LLM call: a rule-based answer confidence, draft-answer length, a bridge-cue flag (multi-hop phrasing like "X of the Y of Z"), the top-1 to top-5 dense score gap, the top-1 score, and a rule-assigned question type.[^c6]

- RASER-2: a gradient-boosted classifier estimates p(BRIDGEABLE), the chance PRUNE improves the draft; run PRUNE if it reaches a threshold, chosen as 0.20, else return the draft.[^c7] In the worked example the draft "I don't know" gave p = 0.5128, so it escalated.
- RASER-3: three regressors predict the F1 each route (one-shot, PRUNE, IRCoT) would get, then the router takes the argmax of predicted F1 minus a token penalty λ times route cost. At λ = 0 tokens are free; as λ grows an expensive route must promise more F1, and at large λ the router always stops.[^c8] Sweeping λ traces a cost-accuracy curve, so the operator picks a budget.

## What it achieved

Across six readers and three benchmarks, RASER-2 stays within 0.026 F1 of always-PRUNE using 39-57% of its tokens.[^c9] The abstract gives 41-49% for the family. RASER-3's iterative route is reader-dependent: frontier models gain little beyond cheaper routes, while mid-tier open models on MuSiQue and 2Wiki gain real value there, so RASER-3 is a higher-budget operating point, not a replacement.[^c10] Swapping Self-Ask for a ChainRAG reimplementation changed F1 by at most 0.020, supporting that the gain comes from selective routing and not from a stronger route.[^c11]

The link to asking and answering: the answer's own first-pass signals (shortness, "I don't know", flat retrieval scores) predict whether more effort can change it, and that is cheaper than always trying.

## Limits

- Three English Wikipedia-style multi-hop benchmarks and one dense retriever; other domains and retrievers untested.
- The recoverability groups are defined by the tested strategies; "unrecoverable" means unrecovered by these, not by any.
- The cost penalty uses token counts only and λ and route costs are tuned on training folds; the threshold 0.20 is a fixed choice.
- The router cannot tell a question that no route fixes from one whose first-pass features look similar to a fixable one; how often it wastes escalation on the unrecoverable group is not something I verified.
- The framing is the authors'; the oracle gain is an upper bound, not an achievable rate.

## Related

- [[syntactic-complexity-routing-between-retrieval-paths]] — routes retrieval path from question structure before answering, rather than from the first answer
- [[implicit-escalation-threshold]] — the same act-or-escalate threshold, with a cost-optimal form
- [[uncertainty-aware-router]] — routing by an uncertainty signal
- [[ambiguity-versus-incapability-routing]] — choosing a response by cause of failure
- [[cost-aware-module-selection-for-help-queries]] — selecting by expected cost

[^c1]: doi-10-48550-arxiv-2606-02488 — "This paper asks: When is additional retrieval actually necessary?"
[^c2]: doi-10-48550-arxiv-2606-02488 — "It tells us how the dataset decomposes into questions that are already solved, questions that can be helped by bridge retrieval, and questions that none of the tested methods can recover."
[^c3]: doi-10-48550-arxiv-2606-02488 — "another 14–27% remains unrecoverable under all tested strategies"
[^c4]: doi-10-48550-arxiv-2606-02488 — "how to detect when bridge retrieval is worth paying"
[^c5]: doi-10-48550-arxiv-2606-02488 — "It is a small decision layer after the first one-shot retrieval-and-answer."
[^c6]: doi-10-48550-arxiv-2606-02488 — "All of them are available after one-shot RAG, so adding the router does not require any language model"
[^c7]: doi-10-48550-arxiv-2606-02488 — "Appendix G shows why we select θ = 0.20."
[^c8]: doi-10-48550-arxiv-2606-02488 — "and at a large enough λ the router always stops."
[^c9]: doi-10-48550-arxiv-2606-02488 — "it stays within 0.026 F1 of always-P RUNE while"
[^c10]: doi-10-48550-arxiv-2606-02488 — "Thus RASER-3 should not be"
[^c11]: doi-10-48550-arxiv-2606-02488 — "RASER’s gain"
