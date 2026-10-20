---
description: "In a modular pipeline, asking splits into which module to query and whether to query; stopping when confidence gain falls below scaled query cost beats confidence-only choice when costs vary."
aliases: ["workload-aware querying", "what and when to ask in modular policies"]
sources: ["arxiv-2602-10289"]
---
# Cost-aware module selection for help queries

A system built from chained modules (perception, planning, control) that can ask a human for help faces two separate decisions, not one: which module to ask about, and whether to ask at all or to act. Banerjee et al. formalise both against a single weighted objective, and the split is the transferable idea.

## Mechanism

Each module carries a confidence score in [0, 1] and a time-dependent cost of querying the human about it; the pipeline is a graph in which one module's output feeds the next.[^c1] The goal is a module selector and a querying algorithm that minimise a weighted sum of query cost and task cost over the interaction horizon, with weight w trading human workload against recovery.[^c2] Workload and query cost are treated as the same quantity.[^c3]

Because failure is not observable beforehand, the selector minimises a one-step proxy built from confidences. Redundant modules (any one succeeding suffices) combine as a union and non-redundant ones (all must succeed) as an intersection, so the reward estimate sums or multiplies confidences accordingly.[^c4] Human answers replace the module's output and set its confidence to an expert confidence.[^c5]

The querying algorithm decides when to stop. "Query-until-Confident" keeps selecting modules until the estimated reward passes a threshold. The workload-aware variant "repeatedly calls the module selector until the confidence gain due to querying module Mi, c_expert − c_i, is less than the scaled cost of querying".[^c6] That is a marginal-benefit-versus-marginal-cost stopping rule.

## What was measured

In a synthetic logic-gate simulation, confidence-only selection (ask the least confident module) was the most scalable, with linear time in the number of modules.[^c7] When query costs differed across modules, a cost-aware graph selector beat confidence-only selection on task cost and total timesteps, most when confidences overlap or workload variance is high. The reason given is that an upstream module with low confidence and high workload may actually succeed, while a downstream module with higher confidence and low workload fails; confidence-only selection picks the upstream one first.[^c8] Query-until-confident was the most robust to overlapping confidences, and any method sufficed when confidences were well separated.[^c9] The authors also report a real bite-acquisition robot deployment with emulated and real mobility limitations; I did not read that section and make no claim about it.

My own inference: the result shows that a bare confidence rank is a poor query-targeting signal once the asker has heterogeneous costs of being answered, and that the question of what to ask and whether to ask can be optimised separately.

## Limits

- The main comparisons use synthetic Boolean modules with confidences set to high or low values and treated as true success probabilities; the paper itself notes real module confidences are often miscalibrated.[^c10]
- Performance degrades as expert confidence falls; the headline results assume a noiseless expert.[^c11]
- Query cost is a scalar supplied to the system; how to estimate real human workload is not derived here.
- The workload-aware stopping rule has the highest computation time, so it is not recommended where runtime is crucial.[^c12]
- Grounded in robot failure recovery; transfer to language-model clarifying questions is my analogy, not tested.

## Related

- [[elicitation-burden-tradeoff]] — also trades linear query burden against error, in a user-LLM model
- [[optimal-question-asking]] — what to ask, the half this note adds a cost term to
- [[temperature-scaled-deferral-gate]] — a confidence-threshold gate for deferring, without query-cost terms
- [[cold-start-value-of-information]] — value of information as a reason to ask

[^c1]: arxiv-2602-10289 — "𝑐 : X → [0, 1] is a confidence score, and 𝑞(𝑡) is a time-dependent cost for querying the human about the module."
[^c2]: arxiv-2602-10289 — "where 𝑤 ∈ [0, 1] determines the trade-off between minimizing human workload and recovering from failures efficiently"
[^c3]: arxiv-2602-10289 — "we use the terms workload and query cost interchangeably."
[^c4]: arxiv-2602-10289 — "where reward estimate 𝑟ˆ (Ω(𝑡)) combines sums (redundant)"
[^c5]: arxiv-2602-10289 — "we replace the module output with"
[^c6]: arxiv-2602-10289 — "repeatedly calls 𝜓𝑚𝑠 until the confidence gain due to querying module 𝑀𝑖 ,"
[^c7]: arxiv-2602-10289 — "ConfidenceQuery is the most scalable method"
[^c8]: arxiv-2602-10289 — "ConfidenceQuery incorrectly selects these"
[^c9]: arxiv-2602-10289 — "We recommend any method if the confidence"
[^c10]: arxiv-2602-10289 — "module confidence scores are often miscalibrated and do not"
[^c11]: arxiv-2602-10289 — "with performance degrading as"
[^c12]: arxiv-2602-10289 — "For large robot policy architectures, we recommend not selecting"
