---
description: "Spatial ability split into five levels, observation to planning; on SpatialBench MLLM accuracy falls as level rises, failures cascade from level three, and humans score 96.40."
aliases: ["hierarchical spatial cognition framework", "five-level spatial cognition taxonomy", "ability-oriented spatial evaluation", "SpatialBench levels"]
sources: ["arxiv-2511-21471"]
---
# Spatial cognition hierarchy

Spatial ability can be decomposed into levels that stack, each resting on the one below. The SpatialBench paper proposes a framework that "decomposes spatial intelligence into five progressively complex levels from basic observation to high-level planning."[^c1] The levels are observation (L1), topology and relation (L2), symbolic reasoning (L3), causality (L4) and planning (L5). The authors take the framework from cognitive map theory, which they read as a picture of spatial knowledge in which "we conceptualize spatial cognition as a hierarchical process that evolves from low-level perception to high-level reasoning and decision making."[^c2] Its 15 task categories are each tied to one level, "each aligned with a distinct stage of spatial cognition,"[^c3] so a model's results can be reported per level instead of as one task average.

The dependence between levels is the part the work measures. Its claim is that spatial cognition in MLLMs "is strictly hierarchical and tightly coupled," and that "success in higher-order reasoning is fundamentally bottlenecked by accurate lower-level perception."[^c4][^c5] On the benchmark, "Performance precipitously declines as cognitive complexity increases, with most models exhibiting cascading failures from the third level onward."[^c6] So the five per-level scores are not independent readings. A failure at a low level is taken as the cause of failures above it, which is why a model that describes a scene well can still fail the causal and planning items built on that scene.

The paper also replaces the task average with an ability score. It is meant to "integrate performance across the five hierarchical cognitive levels,"[^c7] and its level weights are chosen to "emphasize higher-level reasoning while preserving balance."[^c8] The weights are fitted rather than fixed by theory: they are optimized under a stated constraint, "Under the monotonicity constraint," which requires each level's weighted contribution to exceed the one below it.[^c9]

A human run on the same benchmark gives a reference point. "33 human participants are presented with SpatialBench," answering without guidance, and reach "near-perfect performance across nearly all tasks with an overall score of 96.40."[^c10][^c11] The paper sets the two groups' attention against each other: "humans perform selective, goal-directed abstraction, while MLLMs tend to over-attend to surface details without coherent spatial intent."[^c12] In the one worked example, a model "describes the entire scene in a more exhaustive but unfocused manner," and the authors conclude that models "lack selective attention and directional understanding, leading them to infer by association rather than by reasoning about movement and geometry."[^c13][^c14]

For question-asking, the hierarchy suggests stratifying items by the level each one tests, so that a failure can be located rather than averaged away. That use is my inference; the paper does not test it.

## Limits

- The five levels are the authors' decomposition, motivated by cognitive map theory. The sections read do not test whether the levels separate in human performance, or whether another decomposition fits the same results better.
- The cascade is read from the performance pattern across models on one benchmark of "117 / 3.1k+" videos and questions.[^c15] In the sections read, no experiment isolates a level's perception from its reasoning, so "bottlenecked" is a pattern in scores, not a demonstrated mechanism (my inference about what this design can show).
- The overall score's weights and monotonicity constraint are design choices. Another weighting could change the model ranking; no sensitivity analysis appears in the sections read.
- The human run is 33 participants on one benchmark. The attention contrast rests on one qualitative example (Fig. 5), not on a measured attention statistic. "Over-attend" is therefore a description of outputs, not of what the models attended to.
- The data are self-recorded indoor and outdoor video. Whether the level profile holds for other spatial data, or for static images, is not tested here.

## Related

- [[perception-cognition-gap]] — a perception failure that remains after the figure is read: the model reads the values but not the symbol's rule. It is the same kind of break between a lower and a higher level that the hierarchy above describes, though the two papers measure different things.
- [[attention-entropy-ambiguity-signature]] — diffuse attention measured directly on an ambiguous prompt, and concentrated again once the referent is fixed. The "over-attention" claim here is not measured that way, so the two should not be read as the same finding.

[^c1]: arxiv-2511-21471 — "decomposes spatial intelligence into five progressively complex levels from basic observation to high-level planning"
[^c2]: arxiv-2511-21471 — "we conceptualize spatial cognition as a hierarchical process that evolves from low-level perception to high-level reasoning and decision making"
[^c3]: arxiv-2511-21471 — "each aligned with a distinct stage of spatial cognition"
[^c4]: arxiv-2511-21471 — "spatial cognition in MLLMs is strictly hierarchical and tightly coupled"
[^c5]: arxiv-2511-21471 — "success in higher-order reasoning is fundamentally bottlenecked by accurate lower-level perception"
[^c6]: arxiv-2511-21471 — "Performance precipitously declines as cognitive complexity increases, with most models exhibiting cascading failures from the third level onward"
[^c7]: arxiv-2511-21471 — "integrate performance across the five hierarchical cognitive levels"
[^c8]: arxiv-2511-21471 — "To emphasize higher-level reasoning while preserving balance"
[^c9]: arxiv-2511-21471 — "Under the monotonicity constraint"
[^c10]: arxiv-2511-21471 — "33 human participants are presented with SpatialBench"
[^c11]: arxiv-2511-21471 — "near-perfect performance across nearly all tasks with an overall score of 96.40"
[^c12]: arxiv-2511-21471 — "humans perform selective, goal-directed abstraction, while MLLMs tend to over-attend to surface details without coherent spatial intent"
[^c13]: arxiv-2511-21471 — "they often lack selective attention and directional understanding, leading them to infer by association rather than by reasoning about"
[^c14]: arxiv-2511-21471 — "describes the entire scene in a more exhaustive but unfocused"
[^c15]: arxiv-2511-21471 — "117 / 3.1k+"
