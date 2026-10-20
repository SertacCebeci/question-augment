---
description: "Fine-tuning an LLM on one difficulty bin transfers only partly to other bins, and transfer falls as the train-test difficulty gap widens; easy-only or hard-only data does not cover the range."
aliases: ["easy-to-hard generalization", "hard-to-easy generalization", "difficulty transfer"]
sources: ["arxiv-2511-21692"]
---
# Cross-difficulty generalization

Cross-difficulty generalization asks whether a model trained on examples at one difficulty level improves on examples at other levels, easier or harder. The method sorts each benchmark into bins by difficulty: "we divide each dataset into ten equal-sized bins, ordered by increasing difficulty, to systematically study generalization."[^c1] Each bin is used on its own as a training set, "We train LLMs on each difficulty bin individually and evaluate them on all the other difficulty bins".[^c2] The result is a matrix of train bin against test bin. It is not a single easy-versus-hard comparison, which is how earlier studies usually framed the question.

The finding is that transfer is partial and depends on distance. Training on one bin "can sometimes generalize to easier or harder bins, but the extent of generalization is limited".[^c3] "Neither the easy nor the hard training data tends to achieve consistent generalization across the full range of difficulties."[^c4] The strongest transfer is between neighbouring bins, and it weakens with distance: "the generalization decreases as we increase the gap between train and test difficulty."[^c5] Past a large enough gap the tuned model can do worse than the untuned one: increasing the gap "can degrade the performance of the model, sometimes even below the zero-shot baseline."[^c6]

The difficulty score is what makes the matrix readable. The bins come from a Rasch (1PL) item-response model fitted to responses from many LLMs, and "we treat the different language models as the subjects."[^c7] An item's difficulty parameter is then its position on the bin axis. Difficulty here is therefore defined by which models in the pool fail the item, not by a human rating. The paper reports that the two notions come apart: "We find that most datasets show very little to no positive correlation between IRT difficulty scores and human-based metrics."[^c8] Its explanation is that "The hardest bin for models may still contain some of the easiest questions for humans".[^c9]

What the result changes in practice is the advice on selection and evaluation. The authors conclude that "training and evaluation datasets should explicitly account for difficulty alongside other desirable properties such as diversity and coverage."[^c10] For evaluation, a benchmark made only of the hardest problems says little about easy ones: "we cannot assume that it also performs well on easy benchmark problems, as we cannot assume hard-to-easy generalization."[^c11] Training only on easy data, or only on hard data, is therefore not a shortcut to the full range. Which bin to train on is a question with a distance-shaped answer.

## Limits

- The training is single-bin supervised fine-tuning: "We train the language models using supervised fine-tuning exclusively on a single difficulty bin."[^c12] Whether the same matrix holds under reinforcement learning, or with mixed bins, is not shown in this work. The authors list the curriculum case as open: "An open question remains whether a curriculum structured by model-based difficulty, such as IRT scores, can lead to cross-difficulty generalization."[^c13]
- Difficulty is estimated from stored leaderboard evaluations, not from new runs or human annotation: "We estimate difficulty from model response patterns rather than human annotation."[^c14] The bins depend on which models were evaluated. The data come from "the Open LLM Leaderboard".[^c15] My inference: a different pool of models could move items between bins, and the paper does not test this.
- The scope is six English benchmarks, and "our conclusions may not directly extend to tasks in other languages or multilingual settings".[^c16] The patterns are checked on instruction-tuned models from 1B to 14B parameters in two families, "We evaluate instruction-tuned LLMs ranging from the 1B-parameter to the 14B-parameter in Qwen and Llama model families".[^c17] Larger models are not shown.
- "Limited" is a matter of degree. The paper reports the decline with the gap but gives no threshold for what counts as consistent transfer, so the word cannot be used as a cut-off without a further test (my inference).

## Related

- [[item-characteristic-curve]] — the logistic form of the Rasch model that turns model responses into the difficulty parameter used for the bins
- [[difficulty-conditioned-evolving-item-generation]] — also uses IRT difficulty from many LLMs, to generate items at a target level; the curriculum question above is the training-side counterpart
- [[curse-of-knowledge-difficulty]] — another study in which model-based difficulty and human difficulty diverge

[^c1]: arxiv-2511-21692 — "we divide each dataset into ten equal-sized bins, ordered by increasing difficulty"
[^c2]: arxiv-2511-21692 — "We train LLMs on each difficulty bin individually and evaluate them on all the other difficulty bins"
[^c3]: arxiv-2511-21692 — "can sometimes generalize to easier or harder bins, but the extent of generalization is limited"
[^c4]: arxiv-2511-21692 — "Neither the easy nor the hard training data tends to achieve consistent generalization across the full range of difficulties"
[^c5]: arxiv-2511-21692 — "the generalization decreases as we increase the gap between train and test difficulty"
[^c6]: arxiv-2511-21692 — "can degrade the performance of the model, sometimes even below the zero-shot baseline"
[^c7]: arxiv-2511-21692 — "In our work, we treat the different language models as the subjects."
[^c8]: arxiv-2511-21692 — "We find that most datasets show very little to no positive correlation between IRT difficulty scores and human-based metrics."
[^c9]: arxiv-2511-21692 — "The hardest bin for models may still contain some of the easiest questions for humans"
[^c10]: arxiv-2511-21692 — "training and evaluation datasets should explicitly account for difficulty alongside other desirable properties such as diversity and coverage"
[^c11]: arxiv-2511-21692 — "we cannot assume that it also performs well on easy benchmark problems, as we cannot assume hard-to-easy generalization"
[^c12]: arxiv-2511-21692 — "We train the language models using supervised fine-tuning exclusively on a single difficulty bin"
[^c13]: arxiv-2511-21692 — "An open question remains whether a curriculum structured by model-based difficulty, such as IRT scores, can lead to cross-difficulty generalization."
[^c14]: arxiv-2511-21692 — "We estimate difficulty from model response patterns rather than human annotation."
[^c15]: arxiv-2511-21692 — "We collect responses from the Open LLM Leaderboard"
[^c16]: arxiv-2511-21692 — "our conclusions may not directly extend to tasks in other languages or multilingual settings"
[^c17]: arxiv-2511-21692 — "We evaluate instruction-tuned LLMs ranging from the 1B-parameter to the 14B-parameter in Qwen and Llama model families"
