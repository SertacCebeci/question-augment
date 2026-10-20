---
description: "A reward that credits each reasoning tier and subtracts when the chosen tier exceeds the minimal one that suffices, so an RL router is not drawn to the most expensive strategy."
aliases: ["hierarchical-aware reward", "simplest-sufficient-strategy reward", "tier overshoot penalty"]
sources: ["arxiv-2512-15089"]
---
# Minimal-sufficient level reward

A router that picks among reasoning strategies of different cost needs a signal that prices the choice, not only the answer. If the reward counts only whether the final answer is right, a more expensive strategy is never penalised for being unnecessary. The CogER paper adds a term that does this. Its total reward is a sum of three parts, and the third, the hierarchy term, is written as a base credit minus a penalty: the reward "encourages the agent to solve queries with the simplest sufficient strategy".[^h1]

The accuracy part is separate and simple. It gives a positive reward "only when the predicted result matches the expected outcome".[^h2] The hierarchy part works on the tier the router selected, against the lowest tier that solves the query. The base credit grows with the tier: the paper writes the base credit as "increases linearly with the reasoning level", at 0.5 per step above the first.[^h3] The penalty applies when the router goes above the required tier, in the paper's words "the use of unnecessarily complex strategies when a simpler level suffices".[^h4] The term is defined against L_min, which the paper describes as "the minimal level required to solve" a query.[^h5]

The mechanism, as I read it: the base credit rewards reaching a higher tier, so a higher tier is worth choosing only if its extra accuracy outweighs the penalty for overshooting. Without the penalty, the credit alone would push the router upward. The text does not show this derivation; it is my reading of the formula.

What was measured. Removing the hierarchy term lowers performance overall, and it changes the policy's behaviour: the paper reports that it "causes the agent to excessively favor the L4" tier, with the most expensive strategy chosen at "(Delegate) strategy (88.46%), as reported in Table 4".[^h6] [^h7] So the term is measured as the thing that keeps the router off the costliest tier. The paper treats this as the reason for the extra compute, and the latency table is the cost side of the same trade.

## Limits

The label L_min must exist for every training query. The text defines it as the minimal level needed to solve the query, but the part I read does not say how that label is obtained, whether by a measured check or a proxy. Whether the term still works when L_min is noisy is not tested in the text.

The penalty term is named but its form is not given in the part I read, so the trade-off between tiers depends on constants the reader cannot inspect here.

The only ablation shown is removal of the whole hierarchy term. No alternative cost penalty, such as a flat per-token cost or a fixed budget, is compared in the text I read, so the claim is that this term helps relative to none, not that it is the best way to price tiers.

The authors name the weakness themselves. "The current reward function may be too coarse to capture" the quality of complex reasoning, and a sparse signal "can lead to unstable policy learning or unintended" reward hacking.[^h8] [^h9] Those limits apply to this term too, and no run in the text tests them.

## Related

- [[complexity-tiered-strategy-routing]] — the routing this reward trains; the reward is what makes the tier ladder a price ladder.
- [[slo-reward-profile]] — the same design question for a per-query RAG router: the scalar weights of the reward decide what the router learns, and cheap weights collapse it.
- [[sufficiency-gated-imagination]] — a policy that first judges whether current evidence suffices, a related idea of stopping at the cheapest adequate step.

[^h1]: arxiv-2512-15089 — "to solve queries with the simplest sufficient strategy"
[^h2]: arxiv-2512-15089 — "only when the predicted result matches the expected outcome"
[^h3]: arxiv-2512-15089 — "increases linearly with the reasoning level"
[^h4]: arxiv-2512-15089 — "the use of unnecessarily complex strategies when a simpler level suffices"
[^h5]: arxiv-2512-15089 — "the minimal level required to solve"
[^h6]: arxiv-2512-15089 — "causes the agent to excessively favor the L4"
[^h7]: arxiv-2512-15089 — "(Delegate) strategy (88.46%), as reported in Table 4"
[^h8]: arxiv-2512-15089 — "The current reward function may be too coarse to capture"
[^h9]: arxiv-2512-15089 — "can lead to unstable policy learning or unintended"
