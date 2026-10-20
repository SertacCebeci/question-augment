---
description: "A stop action that holds the agent at the answer, rewarded when taken there and penalized when taken early, lets a reasoner learn when to halt instead of walking a fixed length."
aliases: ["STOP self-loop action", "stop signal", "learned halting action", "answer-hold action"]
sources: ["doi-10-1007-s11280-021-00911-5"]
---
# Learned stop action

A reasoner that walks a graph or a chain of steps can be given a way to end its walk early: an extra action that keeps it at the current position. In the paper's formulation the agent takes one hop per step, and one more option is added to every entity, a self-loop labelled STOP. "We add a self-loop action" to every entity "to encourage the agent to hop at the same place."[^c1] Taking STOP means the agent has settled on its current entity as the answer. The paper states the rule for its use: STOP "can only be chosen once for each round."[^c2]

The reward is shaped around the action. A STOP taken at the answer is rewarded, and a STOP taken before the answer is punished: the agent is rewarded "that chooses STOP right after reaching the answer."[^c3] Hops after the first STOP receive a per-hop penalty, so the agent gains nothing by walking on from an answer it has already reached. At test time the answer is read off at the first STOP: "the STOP action is taken as the predicted answer."[^c4] The agent therefore decides when to halt, which is what the fixed-length baselines cannot do. The paper's account of them is that "these baselines do not learn when to stop during the reasoning process."[^c5]

The measured effect is an ablation. Removing the stop component, and separately the worth-trying reward, lowers performance on the three benchmarks: "both two components contribute to the performance of RL-MHR," with WN18RR the exception for the second.[^c6] The paper reports the stop component's gain largest on FB15K-237, where most queries are one-to-many.

The idea transfers to any sequential answering process where an answer can appear before the scheduled end and continuing afterwards can change the result. A stop action turns "when to halt" into something the policy learns from reward, rather than a fixed budget. This is my inference from the mechanism; the paper tests only knowledge-graph path reasoning.

## Limits

- Learning the stop depends on the reward structure. The paper's STOP is rewarded only in combination with the hop penalty and the encouragement reward, and the constants are tuned in ranges the paper states (the encourage reward in (1, 2], the punish reward in (0, 0.5]).[^c7] The paper does not report how sensitive results are to those ranges.
- Longer walks weaken the stop. The paper's own account of the decline at long lengths is that "the longer path increases the search space of the agent," and that after the answer "it might not select STOP in the rest of the hops."[^c8] The concept does not remove the horizon; it moves the difficulty into the reward.
- The paper's error analysis is that "the times of making wrong decisions of the agent also increase" with length, so the final reward of a correct early answer can turn negative.[^c9] This is a limit the paper reports, not one it solves.
- Only one identical connecting entity is used for every STOP, and the answer is the entity before the first STOP. A different convention for where the stop lands could change the scores; this was not tested.
- The ablation is one run per configuration, on three graphs. Results are reported as Hits@1, Hits@10 and MRR, and the parts read do not give variance.
- Whether a learned stop of this kind helps language-model reasoning, where "stay in place" has no natural meaning, is not tested. The mechanism carries over only as a pattern: a halting option whose reward depends on whether the answer is already reached.

## Related

- [[fixed-horizon-false-negative]] — the failure this action is designed to remove: an early correct answer labelled wrong by a fixed final step
- [[stop-continue-criteria-in-retrieval-loops]] — retrieval loops that stop at a fixed budget rather than by a learned or confidence-based rule
- [[answer-agreement-safe-stop]] — an early stop judged safe by agreement with the full trace, a different criterion for the same decision
- [[implicit-stopping-knowledge]] — whether models already know when to stop, the question a learned stop answers by reward
- [[forced-exit-label]] — a per-position label for whether stopping there would be correct, an alternative supervision for the same halting choice

[^c1]: doi-10-1007-s11280-021-00911-5 — "we add a self-loop action"
[^c2]: doi-10-1007-s11280-021-00911-5 — "STOP can only be chosen once for each round"
[^c3]: doi-10-1007-s11280-021-00911-5 — "reward the agent that chooses STOP right after reaching the answer"
[^c4]: doi-10-1007-s11280-021-00911-5 — "the STOP action is taken as the predicted answer"
[^c5]: doi-10-1007-s11280-021-00911-5 — "these baselines do not learn when to stop during the reasoning process"
[^c6]: doi-10-1007-s11280-021-00911-5 — "both two components contribute to the performance of RL-MHR"
[^c7]: doi-10-1007-s11280-021-00911-5 — "the encourage reward re is tuned within (1, 2]"
[^c8]: doi-10-1007-s11280-021-00911-5 — "it might not select STOP in the rest of the hops"
[^c9]: doi-10-1007-s11280-021-00911-5 — "the times of making wrong decisions of the agent also increase"
