---
description: "Meta-training sequences that mix chain-of-thought and direct-answer examples at a power-law rate keep models reasoning without worked examples in context; all-chain training does not."
aliases: ["CoT-Recipe", "chain-of-thought exemplar mixing ratio", "CoT probability schedule in meta-training", "CoT and standard example mix in training sequences"]
sources: ["arxiv-2512-05318"]
---
# Reasoning-exemplar mixing in meta-training

An in-context learner infers a task from the examples in its prompt. Some examples carry a chain of intermediate steps before the answer; others give only the question and the answer. Kothapalli et al. treat the share of the first kind as a variable of the training data, not as a fixed feature of the prompt. Each training sequence gets a chain-of-thought probability: "Instead of designing a sequence with only standard or CoT examples, we employ a CoT probability parameter rCoT and diversify the sequences with a mix of both types."[^c1] Each example in the sequence is then written with its chain or without it, by a draw against that probability.

The probability is not the same for every sequence. The recipe is "a partial power-law function with offset," assigned "based on the sequence index" so that it "control[s] the expected proportion of CoT versus standard examples in context."[^c2][^c3] The exponent α sets the shape of the mix. At α = 0 every sequence is all-chain; at very large α almost none is. With a = 1, b = 0 and α = 1 the probability is simply the position j/T in the dataset (my reading of the formula).

The failure the recipe targets is over-reliance on whatever the training shows. Without modulation, the authors write, the result is "to over-reliance on CoT/standard examples."[^c4] A model trained with α = 0 never sees a sequence without chains, and so "they tend to rely on the CoT examples for" generating outputs.[^c5] At test time the paper removes chains from the prompt (K′ examples converted to standard) and forces the model to think. For the largest transformer, TF-12, forced thinking "exhibits a reduction in accuracy from" about 0.93 to about 0.18 as the prompt loses its chains.[^c6]

The same model trained with α = 2 keeps reasoning when the prompt has no chains. The abstract puts the gain as "CoT-Recipe can increase the accuracy of transformers on novel tasks by up to 300% even when there are no CoT examples available."[^c7] The main text gives the endpoints: about 0.18 at α = 0 against about 0.78 at α = 2, which is roughly a 330% relative gain by my arithmetic. The authors' reading is that "one can train models to be good at thinking even when there are no CoT examples available in-context."[^c8]

The same design was carried to pretrained models. Six Qwen-2.5 models and two DeepSeek-distilled variants scored zero under CoT prompting alone: "all the 8 models scored an accuracy" of 0 across the prompt conditions.[^c9] After supervised training with the recipe on a symbolic task, the larger model gained: "Given a large enough model such as 7B-Instruct," choosing α = 2 gives "accuracy improvements of over 130%" when no chains are in context.[^c10][^c11]

What transfers from this work is the variable, not a number. Whether a model reasons when the prompt does not show reasoning depends on the proportion of reasoning-bearing examples in its meta-training distribution, and intermediate proportions (α in {0.5, 1, 2}) did better than the two extremes in the paper's runs.

## Limits

- The main experiments are synthetic. The transformers are trained from scratch on abstract-token tasks: "We study this problem in a controlled setting using the CoT-ICL Lab."[^c12] Nothing here tests natural-language tasks trained from scratch.
- The pretrained test is small: "Given that we use only 1000 prompts,"[^c13] and the 0.5B model reaches a peak accuracy of only 0.004.[^c18] The gain is shown on one symbolic task, CIL-LangSym, against a zero baseline. It does not show the recipe helps on a task the model already knows.
- The best α is not constant. For the longer-input test the paper says α = 2 "tends to" be the best choice for TF-12.[^c14] The sweep was over {0, 0.5, 1, 2, ∞}; the text read gives no rule for choosing α in advance.
- Out of distribution, the advantage of forced thinking shrinks. The paper calls it "a failure mode where the model is unable to generate the required" number of steps, and forced answering can match forced thinking.[^c15] So reasoning under this recipe is not reliable beyond the training length.
- Correct steps do not guarantee correct answers: "Correct thinking steps do not necessarily imply a correct final answer."[^c16]
- The paper leaves the mechanism open. It says "understanding the role of model size and pre-training datasets can be an interesting avenue for future research."[^c17] The contrast with the Force Answer trend in pretrained models is noted but not explained.

## Related

- [[scaffold-withdrawal-gap]] — the evaluation-time version of the same dependence: guidance removed at test time, here withheld from the training distribution.
- [[cot-capacity-responsiveness]] — chain-of-thought benefit also depends on model size; the pretrained result here shows the same kind of size threshold.
- [[reasoning-trace-behavioral-transfer]] — both ask what a training set of reasoning traces teaches beyond its content (my comparison).
- [[similarity-selected-exemplars]] — chooses which exemplars enter a prompt; this note varies how many of the exemplars carry a chain.

[^c1]: arxiv-2512-05318 — "Instead of designing a sequence with only standard or CoT examples, we employ a CoT probability parameter rCoT"
[^c2]: arxiv-2512-05318 — "is a partial power-law function with offset as"
[^c3]: arxiv-2512-05318 — "control the expected proportion of CoT versus standard examples in context"
[^c4]: arxiv-2512-05318 — "to over-reliance on CoT/standard examples"
[^c5]: arxiv-2512-05318 — "they tend to rely on the CoT examples for"
[^c6]: arxiv-2512-05318 — "exhibits a reduction in accuracy from"
[^c7]: arxiv-2512-05318 — "CoT-Recipe can increase the accuracy of transformers on novel tasks by up to 300% even"
[^c8]: arxiv-2512-05318 — "one can train models to be good at thinking even when there are no CoT examples available in-context"
[^c9]: arxiv-2512-05318 — "all the 8 models scored an accuracy"
[^c10]: arxiv-2512-05318 — "Given a large enough model such as 7B-Instruct"
[^c11]: arxiv-2512-05318 — "accuracy improvements of over 130%"
[^c12]: arxiv-2512-05318 — "We study this problem in a controlled setting using the CoT-ICL Lab"
[^c13]: arxiv-2512-05318 — "Given that we use only 1000 prompts"
[^c14]: arxiv-2512-05318 — "α = 2 tends to"
[^c15]: arxiv-2512-05318 — "where the model is unable to generate the required"
[^c16]: arxiv-2512-05318 — "Correct thinking steps do not necessarily imply a correct final answer"
[^c17]: arxiv-2512-05318 — "of model size and pre-training datasets can be an"
[^c18]: arxiv-2512-05318 — "peak accuracy attained by 0.5B-Instruct is only"
