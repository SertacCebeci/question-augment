---
description: "A stance score for a passage: project its sentence embedding onto the leading principal component of same-question anchor passages, giving a scalar that tracks stance."
aliases: ["PS", "polarization axis projection", "stance polarity score"]
sources: ["arxiv-2512-00804"]
---
# Polarization score

A passage's stance can be read off its sentence embedding along one direction, without stance labels on the passage itself. The method takes a set of anchor passages that answer the same question from different positions, embeds them, and runs principal component analysis on the set. The leading component becomes the polarization axis. A passage is then scored by projecting its embedding onto that axis, which gives "onto this axis produces a scalar polarization score (PS):"[^c1] The score is a single real number per passage, so passages can be compared and averaged.

The reason the leading component should track stance is that the topic is held fixed. "Because the topic is held fixed while" only the stance varies across the anchors, so the paper takes the "source of variance among their embeddings is stance polarity," rather than topic relevance or writing style.[^c2] The paper presents this as a hypothesis: "Our hypothesis is that the difference in the stance" of same-topic passages shows up as a direction in embedding space.[^c3] The statistical tools are imported from elsewhere. What carries over is the variance-maximising direction; what the paper adds is the claim that, with a fixed topic, that direction is stance.

The score has a formal property the paper calls local consistency. Decomposing the squared distance between two embeddings over an orthonormal basis, the squared distance is at least the squared difference of their scores. Two passages that are close in embedding space therefore get close scores.[^c4] This follows from the decomposition in the paper's Eq. 3 (my reading); it says nothing about whether the score is a good measure of stance.

Agreement with stance judgments is the validation. Across 350 passages from 50 questions, the score was compared with a seven-point Likert stance rating; the paper reports an average Spearman correlation of 0.91, "0.91 with Likert scores, demonstrating a strong monotonic alignment with judgments of stance polarity."[^c5] The Likert ratings were produced by asking a large model to "ask GPT-5.2 to rank each passage" on how strongly it supports or opposes the question.[^c6]

## Limits

- The reference labels are an LLM's Likert ratings, not human annotation done in this paper. The paper points to earlier work for the reliability of that judging scheme, which was "validated against human annotation in [18]."[^c7] That check belongs to the earlier work, not to this measurement.
- The axis is fit per question, so its sign and its zero are fixed by the anchor set. The paper argues that its framework "does not require consensus on what constitutes a neutral position."[^c8] The score is therefore a position relative to the anchors, not an absolute stance scale.
- Only the leading component is used. Stance that varies along a second dimension is not represented. This is my inference from the single-axis definition, not something the paper tests.
- The validation is one set of 350 passages. Sensitivity to the number of anchors and to the choice of encoder is not in the part of the paper I read.

## Related

- [[epistemic-bias-propagation]] — the change in mean score across a retrieved set, which this score makes measurable.
- [[answer-evidence-embedding-similarity]] — also reads a meaning signal off embeddings, but measures grounding of an answer in its evidence, not stance.
- [[answer-format-dependent-bias-measurement]] — another measured bias that depends on the instrument; here the instrument is the anchor set.

[^c1]: arxiv-2512-00804 — "onto this axis produces a scalar polarization score (PS):"
[^c2]: arxiv-2512-00804 — "Because the topic is held fixed while"
[^c3]: arxiv-2512-00804 — "Our hypothesis is that the difference in the stance"
[^c4]: arxiv-2512-00804 — "We call this property local consistency."
[^c5]: arxiv-2512-00804 — "0.91 with Likert scores, demonstrating a strong monotonic alignment with judgments of stance polarity."
[^c6]: arxiv-2512-00804 — "ask GPT-5.2 to rank each passage"
[^c7]: arxiv-2512-00804 — "validated against human annotation in [18]"
[^c8]: arxiv-2512-00804 — "require consensus on what constitutes a neutral position"
