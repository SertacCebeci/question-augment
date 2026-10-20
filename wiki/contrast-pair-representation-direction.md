---
description: "A direction in hidden-state space, fitted by PCA on differences between correct and incorrect code for the same task, scores new candidates by a dot product, with no test run."
aliases: ["representation engineering", "RepE", "Linear Artificial Tomography", "LAT", "correctness representation", "contrast-pair representation reading"]
sources: ["arxiv-2512-07404"]
---
# Contrast-pair representation direction

A model's hidden states can carry a direction that separates correct from incorrect outputs of the same task. The direction can be fitted from a small set of pairs and then used to score new candidates, without the model being asked and without running tests. The procedure is representation engineering (RepE) with its Linear Artificial Tomography (LAT) step, moved from truthfulness to code.

It runs in three stages. First, for each programming task a correct and an incorrect implementation are placed in one prompt template, and the hidden state is read at the final token of every layer.[^c1] For each layer, the difference between the two states of a pair is taken; the differences are centred on their mean, and principal component analysis extracts the direction of greatest variation between correct and incorrect code.[^c2] Second, the layer is chosen by validation: the first component of each layer is scored on held-out pairs, and the most accurate layer is kept.[^c3] Third, a new candidate is wrapped in the same template with the concept named ("the amount of correctness"), and its hidden state is projected onto the kept vector by a dot product. The output is a scalar that ranks rather than classifies: "While this score alone does not directly classify correctness, it enables comparison among several candidate solutions."[^c4]

The pairs carry no labels in the prompt. The stated reason is that "contrasting two unlabeled examples, i.e., without telling the model what these examples are, can uncover meaningful distinctions", so the pairs are built "without explicit labels in the stimuli."[^c5] Ground truth is the test suite: "those that pass the reference suite are deemed correct, those that fail are deemed incorrect, and reference solutions are assumed correct by default."[^c6]

What the work establishes is that the signal exists and beats the usual confidence scores. On four 7–8B models and two Python benchmarks (HumanEval and BigCodeBench), the authors report that "LAT successfully extracts meaningful correctness representations from neural activations, significantly outperforming random chance and surpassing intrinsic and reflective confidence metrics across both benchmarks and all models."[^c7] Used to pick one of several sampled solutions, it "improves direct pass@1 performance and approaches the pass@10 ceiling."[^c8] The fitting is cheap by the authors' account: "Our technique, by contrast, is fitted rather than trained—requiring only PCA fitting on a small dataset."[^c9]

What transfers from the original setting is the contrast and the PCA. What does not transfer for free is the concept itself. Truthfulness in language is checked against real-world facts, which the authors call hard to evaluate; code offers a closed test set that is "more objective."[^c10] Yet even here the represented concept is only what the stimuli make it: "Since the represented concept depends on the contrasting stimuli presented to the LLM."[^c11]

## Limits

- The direction is tied to one model. The authors state that "representations captured from one LLM cannot be applied to another’s hidden states."[^c12]
- Correctness is a proxy. "We use passing unit tests as a proxy for correctness, while tests may fall short when it comes to non-functional aspects (e.g., performance and readability)."[^c13]
- Two choices shape the result: "the stimuli used and the model layer chosen to capture the correctness signal."[^c14]
- Scope is narrow: single functions, four models, two Python benchmarks. The gains "may not hold for larger or smaller models, different architectures, or other programming languages."[^c15]
- The mechanism is open. The authors "showed that this signal exists and can be leveraged but not why or how it exists."[^c16]
- My inference, not the authors' claim: because each pair shares its task text, the direction may pick up features common to correct code in general, such as length or style, rather than correctness as such. The paper runs no control that separates these.
- The incorrect candidates differ by setting (other LLMs in one, self-generated variants in the other), and the out-of-distribution results diverge: "which may partly explain divergent out-of-distribution behavior."[^c17]

## Related

- [[pre-generation-success-probe]] — a supervised linear probe trained on success labels; this direction is fitted by PCA on correct-versus-incorrect pairs and is not trained against outcomes.
- [[correctness-contrast-feature-steering]] — the same contrast between correct and wrong cases, applied to sparse-autoencoder features instead of dense hidden states.
- [[cross-layer-probe-ensemble]] — aggregates many layers into one score; this method keeps a single layer chosen on validation.
- [[test-time-scaling]] — the ranking use: choosing one of several samples when running tests for every sample is costly.

[^c1]: arxiv-2512-07404 — "we extract the model’s hidden states at the final token for each layer"
[^c2]: arxiv-2512-07404 — "we apply PCA to these normalized difference vectors to create principal components that capture the greatest variation between correct and incorrect implementations"
[^c3]: arxiv-2512-07404 — "we evaluate each layer’s first principal component on a held-out validation set"
[^c4]: arxiv-2512-07404 — "While this score alone does not directly classify correctness, it enables comparison among several candidate solutions."
[^c5]: arxiv-2512-07404 — "contrasting two unlabeled examples, i.e., without telling the model what these examples are, can uncover meaningful distinctions"
[^c6]: arxiv-2512-07404 — "those that pass the reference suite are deemed correct, those that fail are deemed incorrect, and reference solutions are assumed correct by default."
[^c7]: arxiv-2512-07404 — "LAT successfully extracts meaningful correctness representations from neural activations, significantly outperforming random chance and surpassing intrinsic and reflective confidence metrics across both benchmarks and all models."
[^c8]: arxiv-2512-07404 — "LAT-based ranking improves direct pass@1 performance and approaches the pass@10 ceiling."
[^c9]: arxiv-2512-07404 — "Our technique, by contrast, is fitted rather than trained—requiring only PCA fitting on a small dataset."
[^c10]: arxiv-2512-07404 — "the typical execution-based evaluation of code is more objective, benefiting from a closed-domain environment where correctness is tied to a specific set of test cases"
[^c11]: arxiv-2512-07404 — "Since the represented concept depends on the contrasting stimuli presented to the LLM"
[^c12]: arxiv-2512-07404 — "representations captured from one LLM cannot be applied to another’s hidden states"
[^c13]: arxiv-2512-07404 — "We use passing unit tests as a proxy for correctness, while tests may fall short when it comes to non-functional aspects (e.g., performance and readability)."
[^c14]: arxiv-2512-07404 — "the stimuli used and the model layer chosen to capture the correctness signal"
[^c15]: arxiv-2512-07404 — "the observed LAT effectiveness and ranking improvements may not hold for larger or smaller models, different architectures, or other programming languages"
[^c16]: arxiv-2512-07404 — "we showed that this signal exists and can be leveraged but not why or how it exists"
[^c17]: arxiv-2512-07404 — "which may partly explain divergent out-of-distribution behavior"
