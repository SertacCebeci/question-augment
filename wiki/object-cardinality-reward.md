---
description: "An RL reward that scores an object list by its size against the count the question or answer implies, penalising too few objects and capping the reward for too many."
aliases: ["object count reward", "blueprint cardinality reward", "capped object-count reward"]
sources: ["arxiv-2601-01984"]
---
# Object cardinality reward

The reward scores a reasoning trace by the size of the object list it builds, measured against how many objects the question or answer refers to. Call that reference count K. It is read from the answer when the answer is a count (for example "How many chairs are there? 4" gives K = 4), and otherwise from the objects the question names. Let |O| be the number of objects in the trace's blueprint. The reward encourages a sufficient number of objects while |O| is at most λK, and is capped once |O| exceeds λK, with λ an integer tolerance.[^c1] The paper sets λ to 2.[^c2] The cap is there to stop excess objects from earning reward.

The reason for shaping the count, rather than maximising it, is the paper's account of how the blueprint fails in each direction. With too few objects the analysis rests on incomplete information. With too many, "irrelevant objects may dominate and mislead the reasoning process."[^c3] The reward therefore penalises shortfall and caps excess, so the object list is pushed toward the right order of magnitude and no further.

Two implementation details shape what is counted. Only objects with distinct positions and sizes count, "determined by an IoU threshold of" 0.3 between bounding boxes, so near-duplicate boxes do not inflate |O|.[^c4] The cardinality term is multiplied by the format reward, not added to it, "rather than their sum because Rfmt tends to saturate early in training."[^c5] Once the format is stable, the multiplier leaves the gradient on the count term while keeping valid output.

The reference K is precomputed from the training data, "K is precomputed either by extracting it directly from the answer".[^c6] So the reward needs labelled answers during training, the same supervision the accuracy reward already uses.

## Limits

- The reward measures count, not identity. A blueprint with the right number of objects but the wrong ones receives the same cardinality credit. In the paper, only the accuracy term and the consistency term check whether the objects are the relevant ones (my inference from the reward definitions).
- K is a proxy. When a question names objects without asking for a count, the number of named objects is taken as the target size; that the named objects are the ones the answer needs is assumed, not tested.
- λ = 2 is a single fixed setting. The text I read reports no sweep over λ or over the IoU threshold, so how sensitive the result is to either choice is unknown.
- The ablation removes the blueprint-aware rewards together, and the paper reports the resulting drop as a group.[^c7] The cardinality term's own contribution is not isolated in the text I read.
- The reward is trained on SAT-style synthetic scenes. Whether the count target transfers to real scenes with clutter and partial occlusion is not shown.

## Related

- [[object-centric-blueprint]] — the blueprint this reward shapes; the reward is a constraint on its object list, not on its analysis
- [[answer-reasoning-consistency-reward]] — the companion reward that checks the answer against the reasoning, which the count term does not do

[^c1]: arxiv-2601-01984 — "rewarded to encourage exploration of a sufficient number of objects"
[^c2]: arxiv-2601-01984 — "controlling the tolerance and is set to 2 in our implementation"
[^c3]: arxiv-2601-01984 — "irrelevant objects may dominate and mislead the reasoning process"
[^c4]: arxiv-2601-01984 — "determined by an IoU threshold of"
[^c5]: arxiv-2601-01984 — "rather than their sum because Rfmt tends to saturate early in training"
[^c6]: arxiv-2601-01984 — "K is precomputed either by extracting it directly from the answer"
[^c7]: arxiv-2601-01984 — "removing blueprint-aware rewards (row (C)) leads to clear performance declines across all benchmarks"
