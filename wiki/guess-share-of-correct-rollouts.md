---
description: "Given accuracy and option count k, a uniform-guess model puts the share of correct answers that guessing could produce at (1/k)(1−s); it is large on small-option benchmarks."
aliases: ["random-guess share", "guess hit rate", "random-guess floor"]
sources: ["doi-10-48550-arxiv-2609-04063"]
---
# Guess share of correct answers

A benchmark's accuracy mixes reasoning with guessing. The measure here asks how much of a correct answer a guesser could have produced. For a k-option multi-choice benchmark, "a uniform random-guess policy attains" an accuracy of at least 1/k.[^c1]

The work turns this into a share. Let s = (acc − 1/k)/(1 − 1/k), the accuracy above chance rescaled to [0, 1]. Under a first-order uniform-guess assumption, the share of correct rollouts that a uniform guess could produce is (1/k)(1 − s).[^c2] The formula is the work's; the reading that s is the part of accuracy not explained by guessing is mine.

## Measured values

On the untrained Qwen2.5-0.5B-Instruct model, the work reports "this share is 53.4% on AQuA (k=5)," and "30.1% on MMLU-math (k=4), and 22.8% on SATMath (k=4)".[^c3] Its reading is that bounded-answer benchmarks feed the estimator a within-group composition that is partly random-guess even before training begins. This is the source of the pg term in [[spurious-advantage-grpo]].

On open-answer math, the same model has no finite candidate set, so the floor is zero by construction: "the random-guess floor is 0 and the share is 0".[^c4] That zero is a property of the measure. It does not show that open-answer math is free of guessing. The work's own figure shows a constant policy that emits one popular answer string scoring on MATH-7.5K, and says "Even on a freeform math benchmark, there is a measurable lowerbound score from guessing".[^c5]

## Guess hit rate by answer shape

The guess hit rate is the probability that a random answer matches the gold answer exactly. It is "exactly matches the gold answer, i.e., 1/S for a category" with a finite answer surface of size S, and 0 when the surface is open-ended.[^c6] The work groups MATH-7.5K into 11 answer-shape categories by the syntactic form of the gold answer. Reading Table 1, the per-category hit rates run from 0% to 20%; the 20% belongs to the finite-set category, and the largest category, integers in [-10, 10], has about 4.8%. That range is my reading of the table.

Five of the 11 categories are flagged as bounded and cover 55.95% of the set. The work states that "55.95% of MATH-7.5K, indicating that even an open-answer benchmark can contain a sizeable subset with closed answer form."[^c7] The categorisation is syntactic, so a problem counts as bounded because its gold answer has a closed shape, not because the problem is easy.

## Limits

- The share assumes a uniform guess over the k options and is first-order. A policy that guesses non-uniformly, for instance by favouring popular options, breaks the assumption, and the work's own figure shows that popular strings can score.
- In the parts I read, the share is computed on the untrained 0.5B model. How it moves as RL training proceeds is not given there.
- The zero for open-answer sets is a convention, not a measurement. Hit rates for open answers are set to 0 for the same reason.
- Answer shape is a syntactic category. It does not measure difficulty, and two categories with the same hit rate may differ in how guessable they are for a given model.
- The 55.95% figure depends on the authors' grouping into 11 categories and on which five they flag as bounded. I did not check the grouping against other corpora.

## Related

- [[spurious-advantage-grpo]] — the estimator that turns a guessed correct answer into weight. This note measures how much of the correct mass a guesser can supply, which is the input to that term.
- [[distractor-strength-reward-signal]] — on the reward side, how strong the wrong options are decides how much of a multiple-choice reward a guesser can collect.

[^c1]: doi-10-48550-arxiv-2609-04063 — "a uniform random-guess policy attains"
[^c2]: doi-10-48550-arxiv-2609-04063 — "Under a first-order uniformguess assumption"
[^c3]: doi-10-48550-arxiv-2609-04063 — "this share is 53.4% on AQuA (k=5),"
[^c4]: doi-10-48550-arxiv-2609-04063 — "the random-guess floor is 0 and the share is 0"
[^c5]: doi-10-48550-arxiv-2609-04063 — "Even on a freeform math benchmark, there is a measurable lowerbound score from guessing"
[^c6]: doi-10-48550-arxiv-2609-04063 — "exactly matches the gold answer, i.e., 1/S for a category"
[^c7]: doi-10-48550-arxiv-2609-04063 — "55.95% of MATH-7.5K, indicating that even an"
