---
description: "A policy that writes its own rubrics as its RL reward goes non-monotonic: reasoning scores peak at the first self-generated step, dip at the second, and recover at the third."
aliases: ["self-generated rubrics", "bootstrap rubric generation", "self-bootstrapped rubric reward"]
sources: ["doi-10-48550-arxiv-2606-01091"]
---
# Bootstrap rubric generation

In rubric-based reinforcement learning the rubric is usually written by a stronger external model. Bootstrap rubric generation removes that dependency: at each iteration the policy being trained takes over the evidence gathering and constraint writing, and the rubrics it writes become the reward for the next update.[^c1] Each iteration is therefore a loop in which the policy writes rubrics for new queries and is then trained on them with GRPO.[^c2]

A rubric is a set of atomic constraints, and a response's reward is the arithmetic mean of its per-constraint 0/1 judgments.[^c3] What the loop changes across iterations is the rubric, not the optimizer. The authors report that the rubrics' structure moves a lot between steps: verifiability jumps from 3.8% at the first step to 41.7% at the second, then levels off at 40.2%.[^c4]

The resulting reward trajectory is not monotonic. The first self-generated step gives the strongest reasoning scores; the second dips as the rubric structure shifts; the third recovers and gives the best expert-reasoning results.[^c5] The authors call this "a transition from reasoning specialization to task rebalancing" rather than steady improvement. A control supports reading the effect as a property of the rubrics: a fresh-start run that re-initialises from the base model and uses only one step's rubrics reproduces the dip.[^c6]

Rubric source also shapes what is rewarded. Benchmark-native, GPT-5-generated, Gemini-generated and bootstrap rubrics each produce a different balance of agentic and reasoning scores, and the authors conclude that "rubric source determines" the reward structure.[^c7] Their explanation for the strong first step is that self-generated rubrics fit the model's own range of ability and so apply a stronger pressure to optimise.[^c8] The loop is bounded by that same capacity: "a self-improvement loop bounded by the model's own reasoning capacity".[^c9]

## Limits

- Every evaluation used a shared mock retrieval backend; the paper says an appendix checks consistency with live web search, which is a narrower check than a full live run.[^c10]
- The trajectory rests on three steps at one 8B scale. The conclusion names "instability under over-bootstrapping beyond the recommended stopping point" and "the need for broader large-scale validation" as open issues.[^c11]
- The rubric-quality measures (verifiability, constraint length, cross-step similarity) are keyword and regex heuristics: "indicators use regex pattern matching for numerical thresholds, percentages, formulas, and citation".[^c12] They say how rubrics differ in surface form, not whether they are correct.
- Self-generated rubrics can carry errors into the reward. In one clinical case, "bootstrap Step 1 can introduce factual errors that" propagated into training, and later steps corrected them, but the authors offer one case, not a rate.[^c13]
- The "capability boundary" explanation for the strong first step is the authors' argument, not a measured quantity. My inference, untested here: the same loop without any external check could drift in ways a single run would not reveal.

## Related

- [[pretraining-grounded-rubric-self-play]] — another route to a self-written reward, where the grader is grounded in a sampled pre-training document
- [[rubric-formation-gap]] — the bottleneck is deciding what to check; bootstrap moves that decision into the policy itself
- [[repository-grounded-agentic-rubrics]] — an external-evidence rubric writer of the kind this loop replaces
- [[reward-polarization-stopping-signal]] — the diagnostic the authors use to stop the loop before its scores collapse

[^c1]: doi-10-48550-arxiv-2606-01091 — "Bootstrap generation breaks this dependency"
[^c2]: doi-10-48550-arxiv-2606-01091 — "In bootstrap iteration t, the current policy πθt directly takes over the evidence collection and constraint"
[^c3]: doi-10-48550-arxiv-2606-01091 — "The final reward R(p, x) is the arithmetic mean over all constraint scores, aggregating"
[^c4]: doi-10-48550-arxiv-2606-01091 — "verifiability jumps from Step 1 to Step 2 then saturates (3.8% → 41.7% → 40.2%)."
[^c5]: doi-10-48550-arxiv-2606-01091 — "BS-3 recovers and achieves the best expert reasoning"
[^c6]: doi-10-48550-arxiv-2606-01091 — "Fresh-start BS-3 closely matches cumulative BS-3 across all benchmarks"
[^c7]: doi-10-48550-arxiv-2606-01091 — "Analysis reveals that rubric source determines"
[^c8]: doi-10-48550-arxiv-2606-01091 — "as self-generated rubrics closely match the model’s capability boundary and induce"
[^c9]: doi-10-48550-arxiv-2606-01091 — "This recurrence constitutes a self-improvement loop bounded by the model’s own reasoning capacity"
[^c10]: doi-10-48550-arxiv-2606-01091 — "All evaluations use a shared mock retrieval backend for reproducibility"
[^c11]: doi-10-48550-arxiv-2606-01091 — "Current limitations include instability under"
[^c12]: doi-10-48550-arxiv-2606-01091 — "indicators use regex pattern matching for numerical thresholds, percentages, formulas, and citation"
[^c13]: doi-10-48550-arxiv-2606-01091 — "bootstrap Step 1 can introduce factual errors that"
