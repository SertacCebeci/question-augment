---
description: "A label-free reward for a question-writer that contrasts its own fast answer with the Solver's majority-voted reasoned answer, paying most for questions where intuition is overturned confidently."
aliases: ["dual-track reasoning reward", "intuitive-vs-reasoned answer contrast", "V-Zero questioner reward"]
sources: ["arxiv-2601-10094"]
---
# Intuition-reasoning contrast reward

> A hard question is one where the quick answer is wrong and the careful answer is stable. Reward the question-writer for exactly that.

## Mechanism

In V-Zero, a Questioner and a Solver start from the same base vision-language model and are both trained with GRPO on unlabeled images.[^c1] The Questioner emits a question together with its own direct answer, the "intuitive track" a_fast. The Solver then samples m chain-of-thought answers; their majority vote is the "reasoning track" â, and the confidence c is the share of votes matching â.[^c2]

The reward depends on whether the two tracks agree.[^c3] If â equals a_fast (consistency case), the reward is min(c, 1 − c), which peaks at c = 0.5: the question is then "maximally confusing for the current model", sitting on the Solver's decision boundary.[^c4] If â differs from a_fast (divergence case), the reward is 0.5·c: the reasoned answer corrected the intuitive guess, so the question is a valuable learning signal, and higher Solver confidence earns more.[^c5]

The paper argues this closes the two obvious exploits. Nonsense questions give inconsistent reasoning (low c) and so little reward in the divergence case; trivial questions raise c but make the answers converge, which triggers the uncertainty branch where high confidence pays near zero.[^c6] A malformed output (not a four-option multiple-choice question in the required tags) gets −1.[^c7]

Compared with a pure 50%-agreement reward (see [[uncertainty-peaked-challenge-reward]]), the added ingredient is the second, independent answerer, the Questioner's own fast guess. It lets the reward separate "split because hard" from "stable because correct after reflection", which agreement alone cannot do. That comparison is my inference, not an experiment in the paper.

The Solver side is trained afterwards on the Questioner's questions with majority-vote pseudo-labels and a difficulty-guided filter, giving the co-evolutionary loop also seen in [[problem-solution-coevolution]].[^c8]

## Limits

- The Solver's majority vote is the only ground truth, so a confidently wrong consensus is rewarded in the divergence case; the paper's anti-hacking argument is reasoning, and I did not read an experiment that isolates it.
- The Questioner's fast answer is produced in the same generation as the question, so it may be correlated with how the question was built rather than being an independent intuition. This is my concern, untested here.
- Constants (0.5 scale, the 0.5 peak) are fixed design choices; I did not see a sweep.
- Format restricted to four-option multiple choice on images; transfer to open-ended or text-only asking is not shown.

## Related

- [[uncertainty-peaked-challenge-reward]] — the consistency branch is the same 50%-peaked agreement reward
- [[self-consistency-difficulty-score]] — majority-vote agreement as a difficulty measure
- [[problem-solution-coevolution]] — the proposer-solver loop this reward drives
- [[zero-variance-group-waste]] — why rewards that saturate at c near 0 or 1 give no gradient

[^c1]: arxiv-2601-10094 — "co-evolutionary loop between two roles"
[^c2]: arxiv-2601-10094 — "The majority vote determines â, with confidence"
[^c3]: arxiv-2601-10094 — "The dual-track reasoning reward rd is adaptive"
[^c4]: arxiv-2601-10094 — "targeting questions that are neither too simple nor"
[^c5]: arxiv-2601-10094 — "When the reasoned answer corrects the intuitive guess,"
[^c6]: arxiv-2601-10094 — "Our design"
[^c7]: arxiv-2601-10094 — "is valid only if enclosed within distinct <question> and <answer> tags"
[^c8]: arxiv-2601-10094 — "difficulty-guided data sampling to filter for quality"
