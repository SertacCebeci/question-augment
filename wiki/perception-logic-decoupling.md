---
description: "Free-form reasoning mixes what a model perceived with what it concluded; emitting timestamped evidence units first makes each perception claim checkable against its own segment."
aliases: ["decoupled perception and logic", "DPL", "evidence-unit output format", "perception-reasoning decoupling"]
sources: ["arxiv-2511-18463"]
---
# Perception-logic decoupling

In a free-form chain of thought, what the model saw and what it concluded often sit in the same span of text. The Video-DPL paper names the problem: "free-form CoT often mixes visual perception and logical reasoning in the same text span."[^c1] Its remedy is an output with two parts. First the model writes perception as fixed-format evidence units, each with a start time, an end time and a description. Then "the remaining content is treated as logical reasoning and final answer generation."[^c2] The format is the mechanism: perception is taken out of the reasoning text and kept as a list. In the paper's words, "perception is converted from holistic descriptions into timestamped evidence units", so each claim has a span that a checker can look at.[^c3]

The paper gives two consequences of the split. The first is locality. A claim tied to a time span can be "verified independently on its corresponding video segment", which the authors say reduces noise and ambiguity when the video is long.[^c4] A holistic description of the whole video has no such span, so it can only be judged as a whole. The second is separability of reward. With perception in its own list, one signal can score factuality of the perception and another can score whether the answer follows from it. The authors summarise the effect as "process rewards become more computable, attributable," and scalable.[^c5] Both consequences concern what a reward can see. Neither is a measured gain from the format alone in the parts of the paper I read.

The format is also a training target. The cold-start traces are built by rewriting aggregated frame captions into reasoning that "explicitly include DPL perception units, followed by logic and the final answer."[^c6] So the split is produced in the data before any reward is applied, and the reward then checks that the model keeps producing it.

The format is not stable on its own. In the reinforcement-learning ablation the authors report that the consistency reward "eliminates out-of-format perception outputs, enabling the anti-hallucination reward to function effectively."[^c7] A decoupled output can drift back into prose, and something has to hold the list in place.

## Limits

- The parts of the paper I read compare reward terms and the scale of cold-start data. They do not compare the decoupled output against a free-form chain of thought trained with the same rewards, so the benefit of the split itself is not measured here.
- Locality assumes the model's timestamps are right. A unit with a wrong span is checked against the wrong clip, and the text does not test span error or how often it happens.
- Only video is tested. Whether the same split helps for text evidence, images or documents is my inference, not a result of this paper.
- The fixed format is the paper's own choice. Other separations (for example free text with a verifier) are not compared.
- The reading does not say how much of the format's benefit survives when the reward is removed; the format is trained with rewards in every reported run I read.

## Related

- [[unit-averaged-grounding-reward]] — the reward that scores each perception unit against its clip, and how averaging over units can be exploited
- [[evidence-only-answer-recovery]] — the second reward, which uses the split to test whether the final answer follows from the listed evidence
- [[decoupled-modality-verification]] — a different split: generation and verification are kept in separate modalities, not perception and reasoning in one output
- [[answer-reasoning-consistency-reward]] — a consistency term over a reasoning trace, measured against a gold answer rather than against an evidence list

[^c1]: arxiv-2511-18463 — "free-form CoT often mixes visual perception and logical reasoning in the same text span"
[^c2]: arxiv-2511-18463 — "The remaining content is treated as logical reasoning and final answer generation"
[^c3]: arxiv-2511-18463 — "from holistic descriptions into timestamped evidence units"
[^c4]: arxiv-2511-18463 — "verified independently on its corresponding video segment"
[^c5]: arxiv-2511-18463 — "process rewards become more computable, attributable,"
[^c6]: arxiv-2511-18463 — "DPL perception units, followed by logic and the final answer"
[^c7]: arxiv-2511-18463 — "eliminates out-of-format perception outputs, enabling the anti-hallucination reward to function effectively"
