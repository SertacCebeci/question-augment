---
description: "When answers are costly and partial, choosing whom to ask as well as what to ask, and propagating answers over a respondent-similarity graph, beat question-only selection (12.6% relative at 10%)."
aliases: ["adaptive group elicitation", "whom to query for what", "group-relational respondent selection"]
sources: ["arxiv-2602-14279"]
---
# Joint question and respondent selection

Most adaptive-questioning methods optimise what to ask while the answerer is fixed. Ding et al. argue that in surveys the bottleneck is the number of completed responses, so the asker must also decide who to ask, and must let a few answers inform the many unasked.[^c1] They call this adaptive group elicitation: each round an agent picks a question and a subset of respondents, under a query budget and a participation budget, to reduce uncertainty about a latent group quantity.[^c2]

## Mechanism

Two parts are coupled. A meta-trained LLM scores candidate questions by [[expected-information-gain]] given the interaction history. A heterogeneous graph neural network over respondents and attributes aggregates observed answers and demographics to impute missing answers and to rank respondents. Each round's new observations are written back into the graph, which improves later imputations and the LLM's uncertainty estimates.[^c3] Uncertainty about the latent group state is measured as predictive entropy over future answers, following a de Finetti-style argument that the latent entity is reachable only through the predictions it induces.[^c4]

Selection is two-stage greedy: first the question with the largest gain over the whole pool, then the respondent subset with the largest gain for that question. The authors prove that, if the utility is monotone and submodular and an alignment assumption holds, both joint greedy and two-stage greedy are within a constant factor of the optimal sequence.[^c5] This extends the classic submodular guarantee (see [[adaptive-submodularity]] for the adaptive version). They add that multi-step planning gave only marginal gains at substantial cost.[^c6]

## What was measured

On three opinion datasets the method beat baselines at every budget; at a 10% respondent budget on CES the relative gain was 17.1% at round 1 and 12.6% by round 4. The authors read this as showing that one must reason about who to ask and what to ask together.[^c7] LLM imputation alone (Meta-Greedy-Imp) did not reliably beat no imputation, so the graph propagation, not the LLM's guess about missing answers, carries the imputation benefit.[^c8] Gains concentrate on high-sensitivity respondents, those whose observed answers most improve accuracy, reaching up to 20% relative recovery at a 50% budget.[^c9] My reading: selection spends budget on the individuals the similarity structure explains worst.

## Limits

- The near-optimality theorems rest on submodularity and an alignment assumption stated in the appendix; I did not read the proofs, and nothing checks the assumptions on real survey data.
- Constants in the guarantees are unspecified, so the result is an order claim, not a budget.
- Evidence is population-level prediction of opinion answers on three survey datasets, in simulation from recorded responses. Real respondents who refuse, break off or answer strategically are not tested.
- Gains depend on population structure being informative (attributes that predict answers); how it degrades when similarity is weak was not isolated here.
- The sensitivity tiers use ground truth for stratification, so "who benefits" is an after-the-fact analysis, not something the asker can observe.

## Related

- [[expected-information-gain]] — the question-scoring objective used here
- [[adaptive-submodularity]] — the greedy-guarantee family the theorems extend
- [[noisy-expert-channel-local-query-elicitation]] — another case of choosing queries under a costly answerer

[^c1]: arxiv-2602-14279 — "improving efficiency therefore also requires deciding who to ask, and leveraging population structure"
[^c2]: arxiv-2602-14279 — "a multi-round interaction in which a central agent jointly selects the next question to ask and a subset of respondents to"
[^c3]: arxiv-2602-14279 — "the updated node embeddings enhance the accuracy"
[^c4]: arxiv-2602-14279 — "we treat reductions in"
[^c5]: arxiv-2602-14279 — "both the joint and two stage"
[^c6]: arxiv-2602-14279 — "more complex multi step planning methods provide only marginal improvements while incurring"
[^c7]: arxiv-2602-14279 — "relative improvements ranging from 17.1% at"
[^c8]: arxiv-2602-14279 — "suggesting that LLM-based imputation alone is unreliable"
[^c9]: arxiv-2602-14279 — "reaching up to 20% relative recovery under a 50% budget across both datasets"
