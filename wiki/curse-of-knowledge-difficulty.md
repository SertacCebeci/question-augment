---
description: "A model that knows an item's answer cannot unsee it: its correctness-based difficulty tracks student struggle worse than its explicit estimate, and proficiency prompts barely shift it."
aliases: ["curse of knowledge", "knowledge curse", "capability-perception gap"]
sources: ["arxiv-2512-18880", "arxiv-2511-21692"]
---
# Curse of knowledge in difficulty estimation

A solver can be asked two different questions about an item. One is its explicit estimate of how hard the item is for a learner, given the item, the correct answer and an optional proficiency prompt. The other is behavioural: whether the solver itself gets the item right. The second is what a difficulty parameter is built from when a pool of solvers is scored. In a study of over 20 LLMs across four educational domains, the behavioural signal agreed with human field-test difficulty even less than the explicit estimate did.[^c1][^c8]

The authors call the failure the Curse of Knowledge. Their account is that correctness and difficulty are different objects: items that are conceptually hard for people are often easy for models, so the hard end of the human scale is flat in model terms.[^c2] The Savant Rate makes this a count. It is the share of items in the top third of human difficulty that more than 90% of the models solve, and on USMLE it is 70.4%.[^c4] Read this as a diagnostic of the model pool. It depends on the cut-offs the authors chose, and it does not measure a fixed property of the items.

## The measurement and what transfers

To put correctness on a difficulty scale, the authors treat the model pool as a cohort of synthetic examinees and fit a one-parameter logistic (Rasch) model to the binary correctness matrix; the item's b-parameter is then its machine difficulty.[^c3] Its rank correlation with human difficulty is lower than that of the explicit estimate, which the authors describe as a "Cognitive Divergence".[^c9] The formalism is imported from psychometrics ([[item-characteristic-curve]]), and what survives the transfer is the ordering: an item that most strong solvers fail is hard in the sense the model is used for. What does not survive is the examinee population. The models are not a sample of learners with a matched ability distribution, and they share training data, so the independence that the Rasch likelihood assumes is doubtful (my inference; the paper does not test it).

## The inertia under proficiency prompts

The proficiency prompts were meant to break the curse: told to answer as a weaker student, a model should lose the answer it already has. The accuracy moved in the expected direction, but the shift was small: it "is negligible (typically < 1% change)."[^c5] The paper's word for this is inertia: the capability "exhibits significant inertia: even when explicitly prompted to simulate a lower-proficiency" student.[^c7] The authors' explanation is that a model "cannot unsee the correct" answer while it acts out a learner's misconception.[^c6] The experiment shows the inertia; it does not separate knowledge from a model that simply ignores role instructions (my inference).

The explicit estimates fail in a different way. Model predictions "are narrowly clustered and systematically" low, so they lack the spread to order items the way learners do.[^c10] Averaging over proficiency prompts raised the correlation for frontier models, but the authors refuse to read that as simulation: the gain "does not indicate successful student simulation, but rather reflects noise".[^c11]

A second study reaches the same divergence from the other side. It fits the Rasch model to the responses of thousands of LLMs on six benchmarks and compares the result with human-side measures such as grade level, answer length and number of reasoning steps. Its verdict is that "most datasets show very little to no positive correlation between IRT difficulty scores and human-based metrics."[^c14] The human-side measures do not even agree in sign across datasets: "these correlations are inconsistent".[^c15] The model-side difficulty here is the one used to sort training data into bins, see [[cross-difficulty-generalization]].

## Limits

- The study is zero-shot. The authors did not test few-shot prompting with real student errors, nor fine-tuning on response logs: "We did not explore few-shot prompting with real".[^c12] Fine-tuned simulated respondents are a different regime, see [[simulated-respondent-icc]].
- The ground truths are not one scale. USMLE uses transformed p-values, Cambridge uses rescaled IRT b-parameters, and the SAT sets use three classes, where "difficulty values are provided as discrete categories:".[^c13] Spearman correlations across these mix label types, and three-class labels produce many ties (my inference).
- About 21 models give few examinees for a Rasch fit; the b-parameters are noisy and the text read here reports no intervals (my inference).
- The curse is the authors' explanation for a pattern. No ablation isolates what the solver knows from how it follows instructions.

## Related

- [[pre-generation-success-probe]] — a model's own success is also read from its activations, and that signal is likewise model-relative and diverges from human difficulty.
- [[individuated-metacognition]] — the same models' difficulty judgments track a shared axis rather than their own correctness.
- [[simulated-respondent-icc]] — the fine-tuned counterpart: IRT parameters from simulated respondents, where this note is zero-shot.
- [[simulated-respondent-variance-deficit]] — persona-conditioned respondents also lose spread across respondents; here the shrinkage appears in the predictions.
- [[saturated-performance-measure]] — a ceiling removes spread from a measure; here the ceiling is in the solver's correctness.
- [[item-characteristic-curve]] — the logistic form the Rasch model fits.

[^c1]: arxiv-2512-18880 — "correlates even worse with human than what they"
[^c2]: arxiv-2512-18880 — "items that are conceptually difficult for humans are frequently"
[^c3]: arxiv-2512-18880 — "cohort of students to estimate intrinsic machine"
[^c4]: arxiv-2512-18880 — "The Savant Rate of 70.4%"
[^c5]: arxiv-2512-18880 — "is negligible (typically < 1% change)."
[^c6]: arxiv-2512-18880 — "they cannot unsee the correct"
[^c7]: arxiv-2512-18880 — "exhibits significant inertia: even when explicitly prompted to simulate a lower-proficiency"
[^c8]: arxiv-2512-18880 — "over 20 models across diverse domains such as"
[^c9]: arxiv-2512-18880 — "where the correlation of model IRT difficulty is even lower than the model perception."
[^c10]: arxiv-2512-18880 — "model predictions are narrowly clustered and systematically"
[^c11]: arxiv-2512-18880 — "This improvement does not indicate successful student simulation, but rather reflects noise"
[^c12]: arxiv-2512-18880 — "We did not explore few-shot prompting with real"
[^c13]: arxiv-2512-18880 — "difficulty values are provided as discrete categories:"
[^c14]: arxiv-2511-21692 — "We find that most datasets show very little to no positive correlation between IRT difficulty scores and human-based metrics."
[^c15]: arxiv-2511-21692 — "these correlations are inconsistent"
