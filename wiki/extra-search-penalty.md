---
description: "A GRPO reward that charges a fixed penalty per search after the first, whatever the answer; on one KG verification benchmark it cut search calls from 3.24 to 1.63 without lowering accuracy."
aliases: ["per-turn search penalty", "search cost term", "extra-call penalty", "retrieval-count penalty"]
sources: ["doi-10-48550-arxiv-2607-09092"]
---
# Extra-search penalty

A search agent can be trained to search less by putting the number of searches into its reward. In the knowledge-graph fact-verification framework, the trajectory reward is a sum of two terms, a correctness term and a search term. The search term is built so that "The first search incurs no penalty, because at least one retrieval is generally required to ground the verification, and each subsequent search incurs a fixed penalty."[^c1] Written out, the term is −α·max(0, N−1), where N is the number of retrieval calls in the trajectory and α is a small positive coefficient.[^c2]

The penalty is added to the correctness reward, so it is not gated on the answer. A trajectory that is wrong after four searches is charged for its three extra searches, as is a trajectory that is right. Each group of sampled trajectories for one triple is then scored against its own mean and spread, so that "the advantage of the i-th trajectory" is "computed by standardizing Ri against" the group's statistics.[^c3] The model is never told which search was redundant. The comparison within the group is the only signal about which trajectory searched too much.

The mechanism was introduced because a supervised first stage made the agent search more. The paper reports that "the average search calls rise on every split, because" the distilled policy "leans on the teacher's retrieve-when-uncertain behavior."[^c4] The authors read the added searches as waste: "many of the extra searches induced by Stage 1" were "redundant rather than informative."[^c5] The penalty stage then "cuts the search calls back to near the untrained level" while Macro-F1 rises.[^c6] The headline figure is "number of search calls from 3.24 to 1.63 without lowering accuracy."[^c7] In Table 1 (my reading), the same pattern holds on the unseen-predicate split, where calls fall from 3.36 to 1.80.

## Limits

The coefficient is set by hand. The paper gives "the search penalty coefficient α is set to 0.05 on T-REx and 0.12 on" the Korean enterprise graph.[^c8] The two values differ by a factor of 2.4, and the parts of the text read contain no sweep over α. How much search is removed for a given accuracy cost is therefore a tuned quantity, not a property of the method.

The penalty is not gated on correctness. A wrong answer pays for its searches, and the paper's own reasoning is that "continuing to search is always locally reasonable when" evidence is insufficient.[^c9] Whether an ungated count penalty pushes a model to stop on questions it cannot settle, or merely to stop early on questions it could settle, is not tested in the text. The contrast with [[correctness-gated-redundancy-penalty]] is the relevant one: that note exempts wrong answers, and this one does not.

The reduction cannot be attributed to the penalty alone. The ablation compares the untrained framework, the supervised stage and the supervised stage plus GRPO. The GRPO stage carries both the correctness reward and the search term, and no run with α set to zero is reported in the parts read. The drop in calls is therefore confounded with the RL update itself (my inference).

Accuracy is not uniformly held. On the Korean enterprise graph, "GRPO then raises P-F1 further, at a small cost" to the negative-class F1.[^c10] The T-REx gains are small, under one point of macro-F1 on the long-tail split, and single averages are reported with no variance estimate in the parts read (my inference).

The penalty counts calls, not cost. A cheap lookup and an expensive one weigh the same. [[correctness-gated-retrieval-cost-reward]] charges measured retrieval time instead, which makes a graph search dearer than a text search by construction; this penalty treats them alike.

## Related

- [[correctness-gated-redundancy-penalty]] — the same kind of charge per extra call, applied only to answers already correct and measured against the fewest calls earlier correct answers used
- [[correctness-gated-retrieval-cost-reward]] — charges retrieval time rather than calls, and only on correct trajectories, centred on the batch mean
- [[stop-continue-criteria-in-retrieval-loops]] — the stop rules that a fixed budget or a verifier would impose on the same loop; here the stop is a learned policy shaped by the charge
- [[step-level-retrieval-trigger]] — decides where inside a chain to retrieve; the charge here decides how many retrievals a trajectory may spend

[^c1]: doi-10-48550-arxiv-2607-09092 — "The first search incurs no penalty, because"
[^c2]: doi-10-48550-arxiv-2607-09092 — "each subsequent search incurs"
[^c3]: doi-10-48550-arxiv-2607-09092 — "computed by standardizing Ri against"
[^c4]: doi-10-48550-arxiv-2607-09092 — "the average search calls rise on every split, because"
[^c5]: doi-10-48550-arxiv-2607-09092 — "were redundant rather than informative"
[^c6]: doi-10-48550-arxiv-2607-09092 — "It cuts the search calls back to near the untrained level"
[^c7]: doi-10-48550-arxiv-2607-09092 — "number of search calls from 3.24 to 1.63 without lowering accuracy"
[^c8]: doi-10-48550-arxiv-2607-09092 — "coefficient α is set to 0.05 on T-REx and 0.12 on"
[^c9]: doi-10-48550-arxiv-2607-09092 — "continuing to search is always locally reasonable when"
[^c10]: doi-10-48550-arxiv-2607-09092 — "GRPO then raises P-F1 further, at a small cost"
