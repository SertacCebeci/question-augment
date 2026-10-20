---
description: "Synthetic data inherits the score profile of its seeds: per-sample scores barely track each other, but dataset medians rank-correlate, so seed choice steers what gets generated."
aliases: ["steerability of synthetic data", "property inheritance in synthetic data", "synthetic data steerability"]
sources: ["arxiv-2512-00884"]
---
# Seed property inheritance

A teacher turns each seed into a new sample: it rephrases the question, complicates or simplifies it, and writes a rationale. At the level of single items the link between a seed and its output is weak. The paper says that the score of "an individual seed sample and its corresponding generated sample" "appear to have little to do with each other".[^p1]

The regularity is at the level of the dataset. Comparing the median score of the seed set with the median score of the generated set, the paper finds "high rank correlation between the median score of the seed and generated datasets", and all such correlations are "highly significant (p < 0.001)".[^p2][^p3] The paper's reading is that this is why seed choice matters: "Generated samples inherit underlying properties from the" data used to produce them, and attributes such as the student's loss "shape the student's optimization trajectory and generalization capabilities".[^p4]

The inheritance has a behavioural consequence. When the seeds are chosen as hard for the student, the output is hard for it too: "synthetic data from the teacher is difficult as well, resulting in lower student accuracies on these" samples than under random selection.[^p5] Samples with high student loss "tend to also be samples for which the student model struggles to obtain a correct" answer.[^p6] The paper's summary is that "synthetic data are partially steerable, with teacher outputs reflecting the properties of selected" seeds.[^p7]

The mechanism is therefore a transfer of a ranking, not of an item. Selecting seeds by a score moves the distribution of that score in the output, which is what the selection in [[loss-based-seed-selection]] exploits when it picks high-loss seeds for the next round of [[student-in-the-loop-synthetic-generation]].

## Limits

- The rank correlation is between dataset medians. A per-item prediction, "this seed's output will have this loss", is not supported; the paper states that the item-level relation is loose.[^p1]
- The evidence is two properties, the student's loss and a reward model's score. "the ability to add further desirable properties is left for future work."[^p8] Whether other properties (correctness, style, coverage) transfer the same way is not tested here.
- The reward-based part is biased. The paper finds the reward scorer "prefers longer responses", so its inherited property may partly be length rather than quality.[^p9]
- The trend is not uniform across tasks: "The trend is least clear for the ProntoQA dataset".[^p10]
- The paper cannot guarantee that a seed's desirable properties survive generation: "can guarantee that synthetic data retains desirable properties from the seed dataset" is an open question it raises.[^p11]
- Rank correlation says the order is kept, not the level; a shift in the median that keeps the order would pass this test. This is my reading of the statistic, not a claim the paper makes.

## Related

- [[student-in-the-loop-synthetic-generation]] — the loop whose benefit depends on this transfer
- [[loss-based-seed-selection]] — the seed score whose property passes into the output
- [[llm-judge-biases]] — judge and reward biases that a selection rule can pass on to the data it steers
- [[knowledge-distillation]] — the teacher-student transfer that this inheritance is one side of; the inheritance concerns which inputs are chosen, not the teacher's output distribution

[^p1]: arxiv-2512-00884 — "appear to have little to do with each other"
[^p2]: arxiv-2512-00884 — "find high rank correlation between the median score of the seed and generated datasets"
[^p3]: arxiv-2512-00884 — "All rank correlations are highly significant (p < 0.001)."
[^p4]: arxiv-2512-00884 — "Generated samples inherit underlying properties from the"
[^p5]: arxiv-2512-00884 — "synthetic data from the teacher is difficult as well, resulting in lower student accuracies on these"
[^p6]: arxiv-2512-00884 — "tend to also be samples for which the student model struggles to obtain a correct"
[^p7]: arxiv-2512-00884 — "synthetic data are partially steerable, with teacher outputs reflecting the properties of selected"
[^p8]: arxiv-2512-00884 — "add further desirable properties is left for future work."
[^p9]: arxiv-2512-00884 — "is because the reward scorer introduces biases; specifically, it prefers longer responses"
[^p10]: arxiv-2512-00884 — "The trend is least clear for the ProntoQA dataset"
[^p11]: arxiv-2512-00884 — "can guarantee that synthetic data retains desirable properties from the seed dataset."
