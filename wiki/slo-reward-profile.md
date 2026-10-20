---
description: "The weights of a scalar SLO reward decide what a per-query RAG router learns: quality weights let it edge past the best fixed action, cheap weights collapse it to refusal."
aliases: ["SLO-conditioned reward", "SLO profile", "scalarised SLO reward", "quality-first versus cheap profile"]
sources: ["arxiv-2601-00841"]
---
# SLO reward profile

A per-query controller for retrieval-augmented generation can be trained against one scalar that writes the operator's priorities into a single number. In Nunepalli's offline study the reward is r(q, a) = w_acc · Acc − w_cost · Cost − w_hall · Hall + w_ref · Ref, where Acc is answer correctness, Cost is token cost, Hall is hallucination or incorrect answering, and Ref rewards correct refusals and penalizes incorrect ones.[^c1] A profile is one setting of those weights: "An SLO profile is represented by a vector of weights that trades" answer quality against cost and risk.[^c2] Two profiles are compared, and the text read gives no numeric values for their weights; the quality-first profile puts its weight on correctness and hallucination avoidance, and the cheap profile on token cost.[^c3]

The profile does two jobs. First, it fixes the training label. The target for each state is "the empirically best action for state s under the training SLO," with ties broken deterministically.[^c4] The action set is small: a retrieval depth k in {2, 5, 10} with guarded or auto generation, or a refusal without retrieval.[^c5] Two learners are fitted to those labels: Argmax-CE is supervised multi-class classification of the best action,[^c6] and Argmax-CE-WT adds "weighting proportional to the action-margin between the" best and second-best action.[^c12] Second, the profile fixes what counts as a good router, because the same action can win under one weighting and lose under another.

The measured effect is the clearest case. Under quality first, Argmax-CE moved the average reward "ward from −0.0419 (best fixed) to −0.0287 and accuracy from 0.250 to 0.275" against the best fixed action.[^c7] Under cheap, the same learner refuses almost everything: "under cheap, Argmax-CE collapses to refusal (94.5%), yielding" near-zero accuracy.[^c8] The comparator matters as well. The best fixed action in every condition was the conservative one, "underscoring how strong conservative fixed policies,"[^c9] so a learned router is judged against a strong default, not against no policy.

My reading, not the paper's claim: the profile is therefore part of the question. "Does a learned router help?" has no answer until the weights that price cost against correctness and refusal are written down, and a router that is an improvement under one profile can be a degenerate policy under another.

## Limits

- One dataset and one generator. The results are SQuAD 2.0 dev with N = 200 per condition, point estimates only. The paper warns that "percentage points) should not be over-interpreted."[^c10]
- Two profiles are a sample of the weight space. Where the regime changes between them is not located; my inference, the paper does not sweep the weights.
- The logged rewards depend on one retriever and one generator. "learned policies may not transfer without re-logging."[^c11]
- Cost is a proxy. "Token count is used as the primary cost proxy," and latency and vendor pricing are left out.[^c13]
- Nothing here says how a real operator's priorities should be turned into weights. The paper offers no procedure for that step; my inference.

## Related

- [[abstention]] — the refusal action is the one the cheap profile drives to dominance; the collapse is a reward artifact here.
- [[abstention-base-rate-sensitivity-in-rl]] — an always-abstain collapse driven by the share of unanswerable training items, not by the weights; the two are alike in outcome, not shown alike in cause.
- [[routing-ceiling]] — when one mode already recovers nearly all accuracy, a profile can add little whatever its weights.
- [[compensatory-leakage]] — a general flaw of combining criteria into one scalar, not tested in this study.
- [[calibrated-retrieval-budget-allocation]] — a per-query choice among retrieval modes and abstention made by thresholding a calibrated confidence rather than by a learned policy over a weighted reward.

[^c1]: arxiv-2601-00841 — "where Acc is answer correctness, Cost is token cost"
[^c2]: arxiv-2601-00841 — "An SLO profile is represented by a vector of weights that trades"
[^c3]: arxiv-2601-00841 — "profiles are considered: quality first"
[^c4]: arxiv-2601-00841 — "the empirically best action for state s under the training SLO"
[^c5]: arxiv-2601-00841 — "choose a retrieval depth k ∈ {2, 5, 10} and a generation mode (guarded vs. auto), or"
[^c6]: arxiv-2601-00841 — "Argmax-CE: supervised multi-class classification of"
[^c7]: arxiv-2601-00841 — "ward from −0.0419 (best fixed) to −0.0287 and accuracy from 0.250 to 0.275"
[^c8]: arxiv-2601-00841 — "under cheap, Argmax-CE collapses to refusal (94.5%), yielding"
[^c9]: arxiv-2601-00841 — "underscoring how strong conservative fixed policies"
[^c10]: arxiv-2601-00841 — "percentage points) should not be over-interpreted"
[^c11]: arxiv-2601-00841 — "so learned policies may not transfer without re-logging"
[^c12]: arxiv-2601-00841 — "weighting proportional to the action-margin between the"
[^c13]: arxiv-2601-00841 — "Token count is used as the primary cost proxy"
