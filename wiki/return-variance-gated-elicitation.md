---
description: "Ask a human only while the spread of optimal Q-values over the still-possible worlds is large; split the hypothesis set with yes/no questions until that spread, and hence the return gap, is small."
aliases: ["knowledge-gap tree elicitation", "MINT", "variance-gated questioning"]
sources: ["arxiv-2602-05048", "arxiv-2603-07824"]
---
# Return-variance-gated elicitation

An agent planning with missing facts (an unseen object, an unknown human intent) can decide whether and what to ask by measuring how much the missing fact changes the plan's value, not how uncertain the fact is. MINT represents the missing facts as a descriptor set Φu of possible worlds; each world φ is an MDP with its own transitions and rewards.[^c1] The agent is trained so that one network outputs both the mean and the variance of the optimal Q-value over φ drawn from Φu.

## Mechanism

1. Gate. At deployment, if the estimated variance exceeds a threshold δ and a knowledge gap exists, the agent marks it unresolved and switches to questioning; otherwise the unknown is deemed to have little impact and planning continues unchanged.[^c2]
2. Expand. A symbolic tree has the knowledge gap as nodes and yes/no propositions as edges; each answer shrinks the descriptor set (Φ_{k+1} is contained in Φ_k). The tree is expanded by consulting the neural policy "until reaching the depth limit or the variance/impacts" are small.[^c3]
3. Curate. A language model merges sub-trees and leaves with identical optimal actions, then writes a binary question that splits the tree to maximise information gain about the optimal-action candidates in the leaves.[^c4] Information gain is thus taken over actions, not over the hidden fact itself.
4. Only the part of the uncertainty that answers can remove is used: the authors focus on aleatoric uncertainty due to the knowledge gap, since "way to mitigate it is by obtaining more latent environmental" knowledge from humans.[^c5]

## What was proved and measured

Optimal Q-values are locally pseudo-Lipschitz in the MDP; for a ground truth lying between two known descriptors, the ideal return is bounded by the smaller of the two known returns plus a pseudo-metric distance between the MDPs. The paper reads this as: "Additional interactions to further narrow the knowledge" gap shrink the bound.[^c6] Empirically, MINT-based planning reached near-expert returns "by issuing only 1–3 binary questions per" unknown object across MiniGrid, modified Atari and an Isaac Gym rescue task.[^c7] In MiniGrid with five uncertain objects, standard MINT kept success at 98.2 percent, against 15.2 percent for DQN and 69.2 percent for PPO.[^c8]

## Planner-geometry gate without a trained value network

A later drone-planning paper (Fang et al. 2026, arxiv-2603-07824) gates the same tree on plan structure instead of Q-variance. For an obstacle gap, a branch trajectory is planned under each hypothesis (safe, dangerous); if the cost difference and path deviation are both under thresholds, the gap is irrelevant and no query is made.[^c9] For a target gap, Shannon entropy of the goal distribution decides.[^c10] In simulation the passive LLM planner succeeded 77 percent, exhaustive asking and MINT 100 percent, with 2.0 versus 1.4 average queries (a 30 percent cut).[^c11] In a 20-trial real-world box task the passive planner reached 35 percent against 100 percent.[^c12]

## Limits

- The geometry gate has hand-set thresholds (δc, δd) and is shown on one warehouse scenario with two gap types; the real-world trials are 20, with no query-count baseline.
- The bound is stated for descriptor sets that are interpolations between two known MDPs and for parametric (reward or failure-probability) gaps; it does not cover structural unknowns.
- Questions are binary and the human is assumed to answer correctly about a latent ground truth; noisy answerers are not modelled.
- The variance estimate depends on training with the true descriptor observable and randomly masked; this is my inference of what limits transfer to settings with no simulator.
- Comparison to large language models alone was in settings where those models scored near ceiling at low gap counts; the advantage appears mainly with more unknowns.

## Related

- [[value-of-information]] — the decision-relevance idea this operationalises with Q-variance as the proxy.
- [[entropy-versus-bearing-on-action]] — same distinction: uncertainty that bears on action, not entropy.
- [[candidate-set-entropy-question-selection]] — shrinking a candidate set with yes/no splits.
- [[uncertainty-source-attribution]] — only uncertainty an answer can remove is worth asking about.
- [[distribution-knowledge-gap-in-abstention]] — a knowledge gap as a trigger for asking.

[^c1]: arxiv-2602-05048 — "We can rewrite the uncertainty set using Φu ⊆ Rd , where"
[^c2]: arxiv-2602-05048 — "larger than a predefined threshold δ and a knowledge gap"
[^c3]: arxiv-2602-05048 — "until reaching the depth limit or the variance/impacts"
[^c4]: arxiv-2602-05048 — "dividing the tree to maximize the information gain relating"
[^c5]: arxiv-2602-05048 — "way to mitigate it is by obtaining more latent environmental"
[^c6]: arxiv-2602-05048 — "Additional interactions to further narrow the knowledge"
[^c7]: arxiv-2602-05048 — "near-expert returns by issuing only 1–3 binary questions per"
[^c8]: arxiv-2602-05048 — "Standard 100.0 ± 0.0 9.47 ± 0.33 100.0 ± 0.0 9.75 ± 0.66 99.4 ± 0.5 9.71 ± 1.88 98.2 ± 1.3 9.69 ± 1.91"
[^c9]: arxiv-2603-07824 — "the uncertainty is irrelevant"
[^c10]: arxiv-2603-07824 — "we calculate"
[^c11]: arxiv-2603-07824 — "we reduced the number of human interactions by 30% while maintaining a comparable task success"
[^c12]: arxiv-2603-07824 — "a success rate of only 35%"
