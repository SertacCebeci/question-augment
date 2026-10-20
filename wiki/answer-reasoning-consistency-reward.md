---
description: "An RL reward that scores a reasoning trace by how much it raises the probability of the correct answer over the no-reasoning baseline, so the answer must follow from the trace."
aliases: ["causal consistency reward", "probability-based consistency reward", "reasoning-answer lift reward"]
sources: ["arxiv-2601-01984", "arxiv-2512-22545", "arxiv-2511-23478"]
---
# Answer-reasoning consistency reward

A model can write a reasoning trace and then answer against it, so a correct final answer does not show that the trace supported it. The paper's causal consistency reward tests the link directly. It takes the probability the policy assigns to the gold answer's tokens given the full reasoning context (image, question, blueprint and analysis), and subtracts the probability the base model assigns to the same tokens given only the image and question.[^c1] Averaged over the answer tokens, the difference is the trace's lift on the correct answer. A trace that only decorates an answer the model would give anyway scores near zero. A trace that carries the answer scores by the size of the difference.

The estimator is a probability difference computed with teacher forcing on the gold answer, not a judgement of the trace's text. The average runs over the answer's length.[^c2] The authors adapt it from RLPR, which had replaced verifier-based rewards with probability-based ones: "While RLPR was originally proposed to replace verifier-based rewards with probability-based rewards".[^c3] The motivation in this paper is a specific failure. Even when "the blueprint is relevant and the reasoning coherent, the model may still generate a final answer that" "contradicts its own reasoning."[^c4] The reward is written to close that gap, "ensuring that the model grounds its conclusions in the reasoning derived from the blueprint rather than relying on superficial correlations."[^c5]

In the overall reward the consistency term is added to the accuracy term, while the cardinality term is multiplied by the format term, and the overall reward is defined as a sum of those parts.[^c6] The consistency term is therefore one additive piece; it does not gate the others.

The same teacher-forced log-likelihood shape appears in [[information-gain-reward]], where a clarifier's question is scored by how much it shifts the probability of the goal. The two share the estimator, but the object differs: there the probability is of the user's goal after a question, here it is of the gold answer after a trace. Whether the lift measures faithfulness is a separate question. [[alpha-gameability-of-faithfulness-metrics]] gives a formal account of how faithfulness metrics can be gamed, and a lift-type score needs the same scrutiny.

A label-free version of the same link appears among the five self-signals of SR-MCR, which scores the reasoning against the answer without any gold answer. The semantic term is a cosine similarity between sentence embeddings of the trace and the answer, and the lexical term is ROUGE-L overlap between them.[^c8] The paper says these signals need no ground truth in training.[^c9] Its own introduction warns that single proxies such as lexical overlap "miscalibrate signals" across tasks,[^c10] so these measure the surface and embedding of the link, not the lift on the gold answer that the reward above uses. How the signals are weighted is a separate device, see [[reliability-weighted-signal-fusion]] (my reading of what each measures).

Video-R2 measures the same link without a learned or probability-based score. Its [[think-answer-consistency]] is the share of correct samples whose reasoning conclusion matches the answer tag. Outcome-only GRPO on the final answer lowered that share from 96.8 to 76.8 while raising accuracy, and the authors attribute this to the reward being "only applied to the final answer".[^c11] The same paper then multiplies its temporal reward by an indicator of that agreement, so timestamp credit is paid only where the trace is consistent.[^c12] The gate is a second way the link enters training: as a multiplier on another reward, not as a term of its own.

## Limits

- The reward is anchored on the gold answer. On a rollout that is wrong, it measures how much the trace supports the correct answer, not the answer the model actually gave. That is the intended signal here, but it means the reward can be high for a trace that argues toward the right answer while the model's own answer is different (my inference from the formula).
- A difference, not a ratio. It can be negative, and its scale depends on how much the base model already believed the answer. A question the base model answers well gives little lift whatever the trace says (my inference).
- The text I read never runs the consistency term alone. The ablation removes the blueprint-aware rewards as a group, so its contribution is not separated from the cardinality reward.[^c7]
- The adoption from RLPR is explicit that the principle is taken from another setting ("inspired by"). The text shows no separate test of whether lift tracks faithfulness on this task.
- Each rollout needs a second forward pass of the base model for the no-reasoning probability, which adds cost. The text does not report the overhead.
- The reward inherits the limits of the training data, SAT-style synthetic scenes, which the paper names as its first limitation.

## Related

- [[information-gain-reward]] — the same teacher-forced log-likelihood shape, applied to a clarifier's question instead of a trace's answer
- [[process-outcome-consistency-verification]] — a verifier that also rewards an answer only when the derivation is consistent with it, catching lucky guesses
- [[object-centric-blueprint]] — the blueprint-embedded trace this reward scores
- [[object-cardinality-reward]] — the other blueprint-aware reward, which sizes the object list rather than checking its support for the answer
- [[alpha-gameability-of-faithfulness-metrics]] — how faithfulness scores can be gamed, a caution for any lift-based measure
- [[think-answer-consistency]] — the same link measured as a rate over correct samples, with no probability term
- [[evidence-only-answer-recovery]] — the same link measured against an evidence list rather than a trace: a reference model without the video must reach the policy's answer from the listed evidence

[^c1]: arxiv-2601-01984 — "conditioned on the full reasoning context"
[^c2]: arxiv-2601-01984 — "where Ta is the answer length"
[^c3]: arxiv-2601-01984 — "While RLPR was originally proposed to replace verifier-based rewards with probability-based rewards"
[^c4]: arxiv-2601-01984 — "contradicts its own reasoning"
[^c5]: arxiv-2601-01984 — "ensuring that the model grounds its conclusions in the reasoning derived"
[^c6]: arxiv-2601-01984 — "The overall reward R is defined as"
[^c7]: arxiv-2601-01984 — "removing blueprint-aware rewards (row (C)) leads to clear performance declines across all benchmarks"
[^c8]: arxiv-2512-22545 — "is cosine similarity."
[^c9]: arxiv-2512-22545 — "and thus do not require ground-truth"
[^c10]: arxiv-2512-22545 — "reward proxies (e.g., lexical overlap) miscalibrate signals"
[^c11]: arxiv-2511-23478 — "the GRPO reward is only applied to the final answer"
[^c12]: arxiv-2511-23478 — "only rewarded when reasoning is logically coherent, we apply a consistency gate"
