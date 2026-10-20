---
description: "Build a comparison query by sampling diverse hypotheses from the current belief, optimising an option for each, and asking the pair with highest information gain, not a random-rollout pick."
aliases: ["counterfactual reasoning for query generation", "what-if query synthesis", "hypothesis-conditioned trajectory generation"]
sources: ["arxiv-2603-08531"]
---
# Belief-sample counterfactual query synthesis

Active preference learning scores a pair of options by information gain, but the pair must first exist. Prior methods pick from a fixed set of random rollouts or a replay buffer, which confines the search to behaviours already seen.[^c1] CRED instead generates the candidates from the learner's own uncertainty: it samples reward weights from the current Bayesian belief, and for each sample asks "what if this were the true reward?"[^c2]

## Mechanism

1. Sample N weight vectors from the belief (the posterior is learned with an adaptive Metropolis algorithm).
2. Keep the M most diverse by cosine distance, to limit objective evaluations.[^c3]
3. For each kept weight vector, generate the trajectory that maximises its reward (via reinforcement learning or trajectory optimisation).
4. Compute information gain for every pair and return the best pair as the query.[^c4]

Each option is thus the optimum of a different live hypothesis, so a pair exposes where two competing hypotheses disagree. This is close in spirit to [[query-by-committee]] (ask where sampled hypotheses disagree), but here the disagreeing items are synthesised, not filtered from a stream. The selection objective is the mutual-information criterion, a non-degenerate alternative to [[volume-removal]]. The authors state that directly optimising it is non-convex and tends to stall in local maxima.[^c5]

## Measured

Against random-rollout selection (RR) and a mean-belief policy that explores with epsilon 0.25 (MBP), CRED reached final reward accuracy of 0.998, 0.979 and 0.906 in three simulated domains, while MBP plateaued near 60%.[^c6] Removing environment design (the "CR" ablation) gave lower final accuracy or slower convergence in all domains; the ablations were read as showing the two components are complementary.[^c7] In a 25-person within-subjects study, CRED queries were rated easier to compare (median 6.0 against 4.5 and 5.0) and lower in workload.[^c8]

## Limits

- Assumes a linear reward over known trajectory features and a Boltzmann-rational answerer; nothing here covers non-linear or misspecified models.
- Needs a way to optimise a trajectory per sampled hypothesis (a planner or RL), which is costly and presupposes a simulator.
- The study ground truths were set by task instructions, not discovered preferences, with 6 queries per task; outliers were attributed (by the authors, untested) to participants ignoring instructions.
- Isolated gain from counterfactual generation alone, apart from environment choice, is only shown through ablation curves; I did not read exact numbers.
- Whether the idea transfers to verbal questions (asking a person) is my inference, not tested.

## Related

- [[environment-design-for-query-informativeness]] — the outer loop that chooses the setting in which these queries are generated
- [[query-by-committee]] — disagreement among sampled hypotheses as the selection signal
- [[volume-removal]] — the alternative query objective with a trivial-query degeneracy
- [[upper-confidence-bound-index]] — UCB is the acquisition rule used in the outer loop

[^c1]: arxiv-2603-08531 — "this confines search to previously observed behaviors and"
[^c2]: arxiv-2603-08531 — "effectively asking “what if wi or w j"
[^c3]: arxiv-2603-08531 — "from this set by sequentially computing diversity based on"
[^c4]: arxiv-2603-08531 — "identify the most informative preference query (Algorithm 1"
[^c5]: arxiv-2603-08531 — "the search space is nonconvex, and optimization often converges to local maxima,"
[^c6]: arxiv-2603-08531 — "CRED consistently achieves the highest final"
[^c7]: arxiv-2603-08531 — "reasoning are complementary. These results support H2."
[^c8]: arxiv-2603-08531 — "(4.5, 3.75) and MBP (5.0, 2.00), supporting H4."
