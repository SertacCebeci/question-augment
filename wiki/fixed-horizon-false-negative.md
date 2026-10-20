---
description: "When a reasoner is credited only at a fixed final step, a correct answer reached earlier is scored as wrong; the error grows with the horizon, so accuracy falls as the path length is raised."
aliases: ["false-negative problem in path reasoning", "fixed-length false negative", "short-path false negative", "terminal-only reward mislabeling"]
sources: ["doi-10-1007-s11280-021-00911-5"]
---
# Fixed-horizon false negative

Some reasoners are trained to walk a fixed number of steps and are scored only where the walk ends. In multi-hop reasoning over a knowledge graph, the agent hops along relations from a query entity, and the label is whether the entity it finishes on is the answer. If the walk is fixed at T hops, the agent is rewarded only for paths that land on the answer at hop T. The paper's account of the consequence is direct: a path that reaches the answer at hop 2 of a 4-hop walk gets no credit at hop 2 and is scored as a failure. "We term this as a false-negative problem."[^c1]

The mechanism is the reward structure, not the answer. Under the usual formulation, the agent "gets a positive reward when they arrive at the answer entity" only at the last step, and the paper notes that "there are only a few positive instances for learning the policy network" once short paths are discarded.[^c2] The fixed horizon therefore does two things at once. It makes the positive signal sparse, and it mislabels correct early arrivals as negatives, so the policy is pushed away from them. The paper's example is easy queries: "some of the queries are very easy and can be answered in a small number of hops," and their correct short paths are the ones that get penalized.[^c3]

The effect is measurable in the paper's own sweep. In the path-length analysis, "the performance of other methods decreases while that of RL-MHR rises and then stabilizes" as the walk is lengthened.[^c4] The baselines, which fix the length and score only the last hop, lose accuracy as the horizon grows, because the queries they can answer in fewer hops are increasingly labelled wrong. The paper reads this as the reason its baselines, once the agent "tries to meet the path length and ignores those" short correct paths, must have their path length tuned to each dataset.[^c6]

The same concept applies beyond knowledge graphs wherever a process has an answer that can appear before its scheduled end, and a grader or reward reads only the final state. A correct intermediate answer is then the "wrong" one by construction. This is my inference from the mechanism; the paper tests it only on knowledge-graph path reasoning, on three benchmarks.[^c5]

## Limits

- The paper establishes the effect on reinforcement-learning path reasoning over three benchmark graphs (FB15K-237, WN18RR, NELL-995).[^c5] Whether the same mislabeling drives error in language-model reasoning chains, or in retrieval loops, is not tested here.
- The paper's fix (a stop action, see [[learned-stop-action]]) is not the only remedy. Its ablation shows that the other added signal, the worth-trying reward, also contributes, so the fixed horizon is not shown to be the sole cause of the gap to baselines.
- "False negative" presumes that the gold answer is the right label for the path. The paper scores a path by whether it reaches the answer entity, not by whether each hop is a valid inference. A short path that reaches the answer by accident is counted as correct, and the paper notes, citing an earlier work, that "some reasoning paths are illogical" in the baseline formulation, which this scoring does not screen out.[^c7]
- The accuracy trend in the length sweep is one curve per method on one setup. The paper does not report variance across seeds in the parts read.
- Early correct arrivals are only a false negative if the walk may stop there. Where the task forbids stopping early, the label is correct and the concept does not apply.

## Related

- [[learned-stop-action]] — the paper's remedy: a stop action that lets the agent halt at the answer, so the early arrival is rewarded
- [[stagewise-judged-credit]] — denser credit than one terminal reward, the same remedy applied to long agent runs
- [[rare-correct-rollout-reinforcement]] — sparse rewards in RL, where few rollouts succeed at all
- [[stop-continue-criteria-in-retrieval-loops]] — how retrieval loops choose their stopping point, usually by a fixed budget
- [[answer-agreement-safe-stop]] — an early stop judged safe by agreement with the full trace, the same question of whether an earlier answer is already right

[^c1]: doi-10-1007-s11280-021-00911-5 — "We term this as a false-negative problem."
[^c2]: doi-10-1007-s11280-021-00911-5 — "there are only a few positive instances for learning the policy network"
[^c3]: doi-10-1007-s11280-021-00911-5 — "some of the queries are very easy and can be answered in a small number of hops"
[^c4]: doi-10-1007-s11280-021-00911-5 — "the performance of other methods decreases while that of RL-MHR rises and then stabilizes"
[^c5]: doi-10-1007-s11280-021-00911-5 — "comprehensive experiments are carried out on three benchmark knowledge graphs"
[^c6]: doi-10-1007-s11280-021-00911-5 — "the agent tries to meet the path length and ignores those"
[^c7]: doi-10-1007-s11280-021-00911-5 — "some reasoning paths are illogical"
