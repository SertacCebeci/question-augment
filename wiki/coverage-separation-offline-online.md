---
description: "Offline contrastive preference methods such as DPO and IPO need global coverage of the response space to reach the optimal policy, while online RL needs only partial coverage."
aliases: ["coverage separation", "global versus partial coverage", "offline versus online coverage requirement"]
sources: ["arxiv-2601-06108"]
---
# Coverage separation between offline and online preference learning

Preference data covers only some of the responses a policy could produce. The work states a separation between two ways of learning from such data. Offline contrastive methods, DPO and IPO, learn from a fixed dataset, and the work's theorem says they "require global coverage for convergence to the optimal policy."[^c1] Online RL methods such as PPO "require only partial coverage."[^c2]

The condition is written as a density-ratio bound. A dataset satisfies global coverage with constant C when, for all policies and prompts, the expected ratio between a policy's probability and the data-collection probability, measured under the policy, is at most C. The distribution in the denominator is the one "where µ is the data collection distribution."[^c3] Partial coverage is the weaker condition in which the bound holds only for the optimal policy rather than for every policy.

The proof sketch given for the separation is about exploration. Offline methods "optimize over a fixed" dataset,[^c7] so if the dataset lacks good responses those responses get no gradient signal. An online method generates its own data, so it can reach high-reward regions "even if initially uncovered."[^c4] The work reads this as the reason for a known empirical pattern: the separation "explains empirical findings that PPO outperforms DPO when preference data is not diverse."[^c5]

The remedy the work draws from the separation is a hybrid: "The coverage separation motivates hybrid methods" that combine offline initialization with online refinement.[^c6]

## Limits

- The theorem is attributed to Song et al.; the work gives only a proof sketch and does not restate the full conditions under which convergence holds. I did not check the source.
- Whether real preference datasets meet global coverage is not measured in the work. The separation says what would be needed, not how far typical data falls short.
- The coverage constant and the partial-coverage condition are defined over policies, which is hard to evaluate for free-form text. How to estimate them for an LLM is not addressed here (my inference).
- The empirical pattern, PPO beating DPO on non-diverse data, is cited to two other papers and is not re-tested in this work.
- The hybrid method's sample-complexity claim is a separate theorem (cited to a further paper); it is not evidence for the separation itself.

## Related

- [[dpo-implicit-reward]] — the reward that the offline DPO loss is defined on; coverage decides where that reward is calibrated
- [[bradley-terry-preference-model]] — the preference model the offline methods fit to pairs
- [[reward-overoptimization]] — the same online/offline split appears when a learned reward is exploited
- [[kl-divergence]] — the penalty that keeps a policy near its reference; coverage is a different, ratio-based condition on the policy-to-data gap (my reading)

[^c1]: arxiv-2601-06108 — "Offline contrastive methods (DPO, IPO) require"
[^c2]: arxiv-2601-06108 — "Online RL methods (PPO) require only partial"
[^c3]: arxiv-2601-06108 — "where µ is the data collection distribution."
[^c4]: arxiv-2601-06108 — "even if initially uncovered."
[^c5]: arxiv-2601-06108 — "outperforms DPO when preference data is not diverse [17, 18]."
[^c6]: arxiv-2601-06108 — "The coverage separation motivates hybrid methods"
[^c7]: arxiv-2601-06108 — "Offline methods optimize over a fixed"
