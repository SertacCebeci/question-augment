---
description: "A closed-choice item's difficulty can be fixed before any model is trained: the largest embedding similarity between its keyed answer and any distractor orders items into a curriculum."
aliases: ["anatomical similarity score", "S(q) option similarity", "max distractor similarity", "option-similarity difficulty"]
sources: ["arxiv-2512-19512"]
---
# Max distractor similarity as difficulty

A multiple-choice question gets harder when one wrong option looks like the right one. Anatomy-R1 turns that intuition into a number that needs no answers from a model. For each question the correct option and every distractor are embedded with the text encoder of MedCLIP, and the question's difficulty is the largest cosine similarity between the key and any distractor. The score is "defined as the maximum similarity value among all distractors",[^c1] on the ground that this distractor "represents the most challenging alternative for the model".[^c2]

## Mechanism

The score is computed from the option strings alone, once, before training. A low score means every distractor is semantically far from the key, so the question is easy; a high score means at least one distractor is a plausible rival, so the question is hard.[^c3] The authors give the reason for the choice: in anatomy, difficulty "is typically hard to define due to the inherent complexity and variability of medical data", unlike math, where the number of steps can serve.[^c4] Similarity between options stands in for that unmeasured difficulty.

The score then sets a curriculum. "Our curriculum is structured by partitioning the training data into discrete bins" by score, and "Training begins with questions from the lowest-difficulty bin", moving up when the model's performance meets a threshold.[^c5] This is a gated schedule of the kind described in [[competence-gated-wavefront-curriculum]], with the grid replaced by a single similarity score.

What was measured, in the sections read: on SGG-VQA with Qwen-2.5-VL-7B, the curriculum run is compared with plain GRPO through training-reward curves, and the authors state that "ASC-Learning significantly outperforms the GRPO strategy".[^c6] Their reading is that GRPO's reward "stops improving after an initial rise in the early training phase", which they attribute to the model learning from easy anatomies without carrying that over to hard ones.[^c7]

## Limits

- The score sees only option text, and the image plays no part in it. Two options that are far apart as strings can still be visually confusable, and the reverse can also hold. (my inference)
- It is not checked against error. The sections read do not show that high-score items are the ones the model gets wrong, nor that the bins are ordered correctly in any sense beyond the reward curve. Figure 5 plots reward and S(q) together, but the text read draws no correlation between them. (my inference)
- No ablation in the sections read runs the same bins in random order, so the gain cannot yet be credited to the similarity ordering rather than to staging or to bin-wise exposure.
- The method is described for classification tasks with a fixed option set. Open-ended questions have no distractors and fall outside it.
- The bin count and the thresholds are not given in the sections read.

## Related

- [[distractor-strength-reward-signal]] — the model-based counterpart: a distractor's strength is the share of the reference model's wrong answers that land on it. The embedding score is cheap and model-free, but it measures string closeness, not what a model is drawn to, so the two can disagree (my inference).
- [[competence-gated-wavefront-curriculum]] — the same gating rule, admitting harder items only after a performance threshold, over a difficulty grid rather than a similarity score.
- [[answer-option-surface-cue]] — the opposite failure: a key that stands out by surface form is easy without knowledge, and a similarity score would rate such an item as easy too.
- [[distractor-similarity-reasoning-inflation]] — similarity between irrelevant context and the question inflates reasoning effort; here similarity between a distractor and the key is the difficulty itself.

[^c1]: arxiv-2512-19512 — "defined as the maximum similarity value among all distractors"
[^c2]: arxiv-2512-19512 — "as this represents the most challenging alternative for"
[^c3]: arxiv-2512-19512 — "A low S(q) indicates that all distractors are semantically"
[^c4]: arxiv-2512-19512 — "this difficulty is typically hard to define due to the inherent complexity and variability of medical data"
[^c5]: arxiv-2512-19512 — "Training begins with questions from the lowest-difficulty bin"
[^c6]: arxiv-2512-19512 — "ASC-Learning significantly outperforms the GRPO strategy"
[^c7]: arxiv-2512-19512 — "GRPO’s Reward stops improving after an initial rise in the early training phase"
