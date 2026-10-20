---
description: "The share of temporally adjacent event pairs in a video that are not causally linked; a high share makes temporal order a misleading cue, so it can select videos that test causality."
aliases: ["ANCD", "adjacent non-causal density"]
sources: ["arxiv-2511-19923"]
---
# Non-causal adjacency density

A question that asks whether one event caused another can often be answered from order alone, when the two events sit next to each other in the video. The cheap cue (the later event follows the earlier one) and the target relation (the earlier one made the later one happen) agree on most adjacent pairs, so a model that learned the cue would score well without the relation. The density is a count that exposes how often the two come apart in a given piece of material.

CounterVQA computes it from the causal graph its pipeline has already built. Each video's key events are nodes and accepted causal dependencies are edges.[^a1] Adjacent Non-Causal Density (ANCD) is the ratio of adjacent pairs that are not linked causally to all adjacent pairs.[^a2] A video with many adjacent but unlinked events offers many places where order and cause disagree; a video whose neighbours are all causal offers none. This is a property of the video, computed before any question is written, and it is used as a filter on which videos enter the benchmark.

The work states the purpose plainly: the density checks "whether a video contains sufficient temporal correlations that must be distinguished from true causality".[^a3] The intended item is an adjacent counterfactual, which "intervenes on action ai with an alternative" and asks about its direct successor.[^a4] The authors' reason for keeping high-density videos is that "A higher value indicates more challenging scenarios for Level 1, as models must carefully differentiate" spurious adjacency from cause.[^a5] The threshold they use is ANCD ≥ 0.2.[^a6]

What transfers, in my reading and not as a measured result of the work: a selection statistic can be defined as a disagreement rate between a cheap cue and the target relation over the material. Asking about adjacent pairs is then a choice about which disagreements the question is allowed to probe. The same count can be taken over any sequence where order and cause are both available, such as steps in a procedure or turns in a dialogue, provided a relation graph exists for it.

## Limits

- The density inherits the error of the graph under it. The work reports that "Human evaluation indicates that roughly 90% of the extracted relations" match human judgments of causal correctness.[^a7] A wrong "non-causal" label moves the ratio directly, and the text read gives no per-video error figure.
- The threshold 0.2 is a choice. The text gives no sensitivity check, and the stated reason is only that it ensures "sufficient difficulty".[^a6]
- The claim that higher density makes Level 1 harder is the authors' design rationale. The text read reports accuracy by level, not accuracy as a function of ANCD, so whether a denser video lowers a model's accuracy is not tested here.
- ANCD was applied together with two other graph metrics (causal depth and a semantic outlier score), and the candidate set fell from 1,200 videos to 700+ under the three together.[^a8] Its effect alone is not separated.
- The density measures disagreement in the authors' graph, not in the video. A pair the graph calls non-causal may still be causal in a way the annotators did not record.

## Related

- [[hop-depth-difficulty-with-entropy-check]] — the other graph statistic used to select items in this pipeline; causal depth sets how long a chain a question may span, where ANCD sets how often order misleads.
- cross-modal-causal-transfer — the same work's training stage, which takes causal structure from text rationales built over these videos.
- [[text-modality-dominance]] — a related pattern in which one channel answers for another; ANCD is a way to make such a shortcut visible in the material before a model is tested.

[^a1]: arxiv-2511-19923 — "where nodes V represent key events and edges E capture"
[^a2]: arxiv-2511-19923 — "Adjacent Non-Causal Density (ANCD): To assess"
[^a3]: arxiv-2511-19923 — "whether a video contains sufficient temporal correlations that must be distinguished from true causality,"
[^a4]: arxiv-2511-19923 — "An adjacent counterfactual question intervenes on action ai with an alternative"
[^a5]: arxiv-2511-19923 — "A higher value indicates more challenging scenarios for Level 1, as models must carefully differentiate"
[^a6]: arxiv-2511-19923 — "We retain videos with ANCD ≥ 0.2 to ensure"
[^a7]: arxiv-2511-19923 — "Human evaluation indicates that roughly 90% of the extracted relations"
[^a8]: arxiv-2511-19923 — "These metrics filtering reduces the candidate set"
