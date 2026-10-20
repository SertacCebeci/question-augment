---
description: "Agents who share one of M hidden best options can be grouped by their own samples; the sample lower bound is the larger of two sub-task terms, not their sum."
aliases: ["Cl-BAI", "BAI-Cl", "clustered federated best-arm identification", "clustered federated bandits"]
sources: ["doi-10-48550-arxiv-2505-10147"]
---
# Clustered best-arm identification

Take N agents, each learning one of M stochastic bandits drawn from one common set of K arms. The mapping from agents to bandits is unknown to the learner. Each bandit has its own best arm, so the agents in one cluster share a best option.[^c1] The learner must name the best arm for every agent with probability at least 1 − δ, and every pull is paid for. The task is therefore two tasks at once: finding the best arm of each cluster, and finding which cluster each agent belongs to.

The first algorithm, Cl-BAI, clusters before it identifies. Each agent runs successive elimination on its own arms, and the agents are then linked in a graph whose connected components are the clusters.[^c2] The authors chose successive elimination "primarily because of its simplicity and easy-tuning" ability.[^c3] Once the clusters exist, one representative per cluster finds the best arm, and "declares that arm as the best arm for all the agents in the corresponding cluster."[^c4] The first phase therefore has one job: sort agents by the bandit they learn. It does not have to find anyone's best arm, and the best-arm search runs once per cluster rather than once per agent.

The second algorithm, BAI-Cl, reverses the order. It finds one representative from each cluster first, "we first identify representatives from each" cluster, using a coupon-collector argument.[^c5] It then builds a small candidate set of arms from those representatives, and "each remaining agent indicates one amongst" that set as its best arm.[^c6]

The lower bound explains why the work splits this way. For the class of instances considered, the paper states a minimax lower bound of the form "max{M ·(K −M ),N }" times log(1/δ) over the squared gap. The extracted text is garbled, so I read the display as that maximum and did not check it against the typeset form.[^c7] The paper's reading of the two terms is that "it is the maximum of two terms, each" corresponds to a different sub-task. One sub-task is identifying the set of best arms across the M bandits. The other is "identifying for each agent the index of the bandit problem" that it is learning.[^c8][^c9] Read as a maximum rather than a sum, the two sub-tasks overlap in the sample count rather than add, so the group structure does not double the cost of the shared answers. That reading is mine, drawn from the stated form of the bound.

The authors also measure the gain. In a movie setting with "application with 100 users, clustered into 6 different age" groups, from MovieLens-1M, BAI-Cl++ gave a "72% improvement in the sample complexity over a naive" cluster-oblivious scheme. A Yelp experiment gave "A 65% improvement is observed."[^c10][^c11]

For asking, this is my inference, not the paper's claim: when a population of respondents shares a hidden type that fixes the best answer, the type can be located from the respondents' own responses, and the search for the answer can be paid once per type rather than once per respondent. The bound says the saving is limited by the two sub-tasks, not by the population size alone.

## Limits

- **Separability.** Cluster recovery needs "a separability condition (for identifiability) across clusters."[^c12] Assumption 2.1 requires that "each of the M bandit instances have a different best arm," and that the best arm of one bandit be worse under another by at least η.[^c13] The algorithm takes η as an input ("Input: δ, η").[^c14] A population where two groups share a best option, or where the gap is unknown, is outside what the text establishes.
- **Uniform clusters.** The BAI-Cl analysis assumes that "each agent belongs to one of M clusters uniformly."[^c15] Unequal cluster sizes appear only in a remark, as an unequal-probability coupon problem, and the text read does not prove them.
- **Worst-case bound on a restricted class.** The lower bound holds on a class with a gap condition, and the paper says it will "restrict attention to unit variance Gaussian rewards for" simplicity.[^c16] It is also called "a worst-case bound," so it does not say what an easy instance costs.[^c17] The instance-dependent version is deferred.
- **Narrow optimality claim.** The minimax statement is for "(a variant of) BAI-Cl is (order-wise) minimax," not for Cl-BAI, and the abstract ties it to a small number of clusters.[^c18]
- **Evaluation.** The 72% and 65% figures come from the paper's own experiments on MovieLens-1M and Yelp. The comparison in the text read is with a naive cluster-oblivious scheme, not with other clustered-bandit methods.[^c10][^c11]
- **Scope of the reading.** I read the introduction, setup, the two algorithms, the lower-bound section and the coupon remark. The proofs and most of the appendix were not checked.
- **Model.** Agents are i.i.d. draws from fixed reward distributions. A respondent whose preferences drift, or who answers differently across asks, is outside the model. Carrying the mechanism to question-asking is my inference; the paper's agents are bandit learners, not people.

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — the single-learner version of this kind of sample bound; the clustered bound adds a cluster-level term.
- [[thompson-sampling]] — another adaptive sampler, for one bandit rather than many bandits sharing one arm set.
- [[agreement-based-annotator-clustering]] — also groups respondents by how they respond, but from labels on shared items, with no best-option search.
- [[clustered-question-elicitation]] — clusters questions rather than respondents, a different object.

[^c1]: doi-10-48550-arxiv-2505-10147 — "We consider N agents grouped into M clusters"
[^c2]: doi-10-48550-arxiv-2505-10147 — "first clusters agents based on the bandit problems"
[^c3]: doi-10-48550-arxiv-2505-10147 — "primarily because of its simplicity and easy-tuning"
[^c4]: doi-10-48550-arxiv-2505-10147 — "finds the best arm for that agent, and then declares that arm"
[^c5]: doi-10-48550-arxiv-2505-10147 — "we first identify representatives from each"
[^c6]: doi-10-48550-arxiv-2505-10147 — "each remaining agent indicates one amongst"
[^c7]: doi-10-48550-arxiv-2505-10147 — "max{M ·(K −M ),N }"
[^c8]: doi-10-48550-arxiv-2505-10147 — "it is the maximum of two terms, each"
[^c9]: doi-10-48550-arxiv-2505-10147 — "identifying for each agent the index of the bandit problem"
[^c10]: doi-10-48550-arxiv-2505-10147 — "application with 100 users, clustered into 6 different age"
[^c11]: doi-10-48550-arxiv-2505-10147 — "72% improvement in the sample complexity over a naive"
[^c12]: doi-10-48550-arxiv-2505-10147 — "a separability condition (for identifiability) across clusters"
[^c13]: doi-10-48550-arxiv-2505-10147 — "each of the M bandit instances have a different best arm"
[^c14]: doi-10-48550-arxiv-2505-10147 — "Input: δ, η"
[^c15]: doi-10-48550-arxiv-2505-10147 — "each agent belongs to one of M clusters uniformly"
[^c16]: doi-10-48550-arxiv-2505-10147 — "we will restrict attention to unit variance Gaussian rewards for"
[^c17]: doi-10-48550-arxiv-2505-10147 — "bound proposed in Theorem 7.1 is a worst-case bound"
[^c18]: doi-10-48550-arxiv-2505-10147 — "(a variant of) BAI-Cl is (order-wise) minimax"
