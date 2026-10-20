---
description: "Novelty as one minus mean cosine similarity to retrieved papers, gated at a threshold and used as a test-time RL reward, raised idea novelty from 49.36 to 62.06 without labels."
aliases: ["retrieval-based novelty reward", "innovation score reward", "TTRL novelty reward", "dissimilarity-to-literature reward"]
sources: ["arxiv-2512-16969"]
---
# Retrieval-dissimilarity novelty reward

An open-ended scientific output has no label to score against. The mechanism in this work replaces the label with a baseline fetched at test time. For a query, the model samples a group of candidate ideas. Each idea is embedded, and so are the embeddings of n papers returned by online search for that query. The reward then rests on how far the idea sits from that retrieved set: "We quantify novelty by measuring the vector space dissimilarity between the generated idea and the retrieved literature."[^c1] Concretely, the average cosine similarity to the retrieved papers is turned into an innovation score on a 0 to 10 scale, S_inn = clip((1 − S_avg) × 10, 0, 10). A binary gate then sets the novelty reward to 1 when S_inn passes a threshold and to 0 otherwise. The gate is set at 5, "Using a gating threshold" in the paper's words.[^c2] The total reward is the unweighted sum of a binary format term, which requires the answer to sit in the expected XML tags, and this novelty term.[^c3] The policy is then updated with GRPO over the sampled group.

The paper calls this test-time reinforcement learning (TTRL) and separates it from the original. "This framework enables models to self-evolve" on unlabeled test data, using rule-based rewards built from the model's own outputs or from the environment.[^c4] The original TTRL used consensus as the reward, which "primarily leveraged consensus-based consistency as a reward mechanism for logical reasoning tasks".[^c5] Here the reward is "constructed based on the dissimilarity between generated ideas and retrieved related works", so the signal pushes outputs away from what the literature already says.[^c6]

The reported effect is on novelty alone. The average novelty score rose "from a baseline of 49.36 to 62.06" over training.[^c7] The authors stress that "this performance gain was achieved entirely without ground-truth" labels, the only feedback being the online retrieval loop.[^c8]

What transfers is a method point: a retrieved set can stand in for a reference when no label exists, and a distance from that set can be turned into a reward. What does not transfer is any claim that distance from literature is the same as a good idea. The paper's own evaluation of novelty averages the dissimilarity with an LLM-judge win rate,[^c9] so the trained quantity and the judged quantity are not the same object.

## Limits

- The reward measures distance from whatever the search returned, through one embedding model. Whether a far idea is new science, rather than off-topic or wrong, is not tested in the slices read. My inference: an output that avoids the query's literature altogether would clear the gate, so the reward can be met by divergence without merit.
- The reward has no term for feasibility, correctness or detail. The slices read report the novelty gain and no other metric for the trained model, so the study cannot show whether novelty was bought at the cost of the other axes. Elsewhere the coupling is measured and can run either way; see [[innovation-correctness-tradeoff-in-problem-generation]].
- The gate threshold of 5 and the number of retrieved papers n appear without a sensitivity analysis in the slices read. The gain could depend on both.
- The baseline and trained scores are on the paper's own novelty scale, which in evaluation is an average with a judge win rate. The 49.36 to 62.06 figure is therefore one run on a composite scale, not an external measure. This is my reading of the metric definition.
- No comparison in the slices read sets this reward against a consensus reward or a labelled reward on the same tasks, so the claim "without ground-truth" is a claim about training data, not a claim that the method matches supervised training.

## Related

- [[verification-weighted-voting]] — the TTRL pseudo-label there is a majority answer; here it is a retrieved distance
- [[factual-novelty-elicitation-reward]] — another novelty reward, counting new named entities in a reply rather than distance from literature
- [[innovation-correctness-tradeoff-in-problem-generation]] — novelty rising while correctness falls, measured against an answer
- [[novelty-feasibility-decoupling]] — the axes a novelty reward does not score
- [[practical-inquiry-model]] — the conception quadrant this reward is aimed at

[^c1]: arxiv-2512-16969 — "We quantify novelty by measuring the vector space dissimilarity between"
[^c2]: arxiv-2512-16969 — "Using a gating threshold"
[^c3]: arxiv-2512-16969 — "defined as the unweighted sum of a format constraint and a novelty"
[^c4]: arxiv-2512-16969 — "This framework enables models to self-evolve"
[^c5]: arxiv-2512-16969 — "which primarily leveraged consensus-based consistency as a reward mechanism for logical reasoning tasks"
[^c6]: arxiv-2512-16969 — "the reward signal is constructed based on the dissimilarity between generated ideas"
[^c7]: arxiv-2512-16969 — "increased from a baseline of 49.36 to 62.06"
[^c8]: arxiv-2512-16969 — "this performance gain was achieved entirely without ground-truth"
[^c9]: arxiv-2512-16969 — "We measure novelty by computing the dissimilarity between the model-generated idea and"
