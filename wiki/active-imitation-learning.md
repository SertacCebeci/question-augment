---
description: "Active imitation learning asks an expert for action labels on a chosen subset of visited states, correcting covariate shift under a label budget instead of labelling every state."
aliases: ["AIL", "query-efficient interactive imitation"]
sources: ["arxiv-2512-00453"]
---
# Active imitation learning

Behavioural cloning trains a policy on expert demonstrations alone, and its weakness is covariate shift: "as the agent explores, its on-policy state distribution diverges from the expert" [^a1], so small errors push the learner into states the demonstrations never covered, and the errors compound. The remedy is to keep the learner in control of its own rollouts and to bring the expert back for labels on some of the states it visits.

Active imitation learning (AIL) is that remedy with a cost term attached: "Active imitation learning (AIL) combats covariate shift by querying an expert during training."[^a2] The motivation is the price of the label. "expert action labeling often dominates the cost" in GPU-heavy simulators, in human-in-the-loop settings and in robot fleets.[^a3]

## Mechanism

The two ends of the range are fixed by the paper's definitions. Dataset Aggregation (DAgger) sits at one end: it "labels every visited state with the expert action" and aggregates the labels before retraining.[^a4] The formal statement is "For reference, DAgger corresponds to" a query set equal to every time step of every episode.[^a5] Everything else in the AIL literature is a choice of which visited states to label.

The paper writes that choice as a querying strategy. A strategy ψ maps the training history and the current trajectory to a set of time indices; the states at those indices are sent to the expert, and the learner is then updated on the new labels.[^a6] Two conditions are placed on ψ. It must be non-anticipatory across episodes, so it "does not depend on future episodes."[^a7] The labels are also only observed at the queried times: "we only observe labels at queried times."[^a8]

Training is stopped by a budget. "Training halts once either the total number of queries reaches" the query budget or the environment-step budget.[^a9] The objective is then the expected imitation loss of the final policy, so a strategy is judged by what it reaches at a fixed cost rather than by how few labels it uses.[^a10] The paper notes the two ways to fix a budget: a query budget is "more natural in deployment, while the latter is convenient" for analysis, where the latter means a fixed step budget and a comparison of query counts.[^a11]

Within this frame the older query-selection methods are gates. SafeDAgger "learns an auxiliary safety classifier that predicts whether a state is safe enough" for the learner to act on.[^a12] Ensemble methods use "disagreement or variance across multiple policies, with fixed and percentile-based thresholds."[^a13] Both need the expert to take control during the rollout. The CRSAIL line of work instead decides after each episode, so it "can be run without real-time expert takeovers."[^a14]

## What was measured

The formalism is tested on three MuJoCo control tasks, "stabilization, manipulation, and locomotion."[^a15] Baselines are DAgger, EnsembleDAgger and ThriftyDAgger; the paper dropped SafeDAgger, LazyDAgger and RNDAgger. LazyDAgger was dropped because it was "sensitive and unstable in our pilots."[^a16] [^a17] All methods get the same environment-step budget, so their total query counts can differ; that is what is compared.

## Limits

- The optimum is not computed. The result is stated against the class of strategies the paper considers: the comparison that matters is made "when Ψ is restricted to CRSAIL" and the baselines.[^a18] The paper does not claim its strategy is optimal over all admissible ψ.
- The objective is defined on the labels the learner would receive. The expert labels are "a conceptual oracle for defining the objective," [^a19] My inference: the true loss needs labels over the whole distribution the learner visits, which no learner sees in full, so the loss is an evaluation device rather than a quantity training can read off.
- The cost of the querying rule itself is treated as small by the paper: "this adds only minor overhead compared with simulation."[^a20] That is measured for one nearest-neighbour rule on the paper's tasks. It is not a general claim about every query rule.
- The expert is imperfect on the hardest task. "as our expert is imperfect" on Inverted Double Pendulum, where the initial data are mostly successful episodes, and the authors flag this as a source of difficulty.[^a21]
- Labels are counted, not priced. The introduction names operator fatigue and GPU hours as the real costs, and the experiments report labels. My inference: the two can differ by the cost per label, which the formalism does not model.
- The baseline settings are partly the authors' choice. Where the original papers did not cover an environment, gating thresholds were swept, so a comparison depends on that sweep.

## Related

- [[state-novelty-query-rule]] — a query signal for ψ that uses the distance to labelled states, not the learner's outputs
- [[query-by-committee]] — selective querying where a committee disagrees; the same filter idea in a noiseless-oracle setting
- [[active-testing]] — choosing which items to label under a budget, in evaluation rather than training

[^a1]: arxiv-2512-00453 — "as the agent explores, its on-policy state distribution diverges from the expert"
[^a2]: arxiv-2512-00453 — "Active imitation learning (AIL) combats covariate shift by querying an expert during training."
[^a3]: arxiv-2512-00453 — "expert action labeling often dominates the cost"
[^a4]: arxiv-2512-00453 — "labels every visited state with the expert action"
[^a5]: arxiv-2512-00453 — "For reference, DAgger corresponds to"
[^a6]: arxiv-2512-00453 — "a querying strategy ψ specifies, for each"
[^a7]: arxiv-2512-00453 — "it does not depend on future episodes"
[^a8]: arxiv-2512-00453 — "we only observe labels at queried times"
[^a9]: arxiv-2512-00453 — "Training halts once either the total number of queries reaches"
[^a10]: arxiv-2512-00453 — "goal is to minimize the expected imitation loss of the final"
[^a11]: arxiv-2512-00453 — "more natural in deployment, while the latter is convenient"
[^a12]: arxiv-2512-00453 — "learns an auxiliary safety classifier that predicts whether a state is safe enough"
[^a13]: arxiv-2512-00453 — "multiple policies, with fixed and percentile-based thresholds"
[^a14]: arxiv-2512-00453 — "can be run without real-time expert takeovers"
[^a15]: arxiv-2512-00453 — "We evaluate on three MuJoCo control tasks for stabilization, manipulation, and locomotion"
[^a16]: arxiv-2512-00453 — "sensitive and unstable in our pilots"
[^a17]: arxiv-2512-00453 — "We omit SafeDAgger, LazyDAgger, and RNDAgger"
[^a18]: arxiv-2512-00453 — "when Ψ is restricted to CRSAIL"
[^a19]: arxiv-2512-00453 — "a conceptual oracle for defining the objective"
[^a20]: arxiv-2512-00453 — "this adds only minor overhead compared with simulation"
[^a21]: arxiv-2512-00453 — "as our expert is imperfect"
