---
description: "In self-study QA pipelines the question-generation step is an implicit, non-uniform evidence-selection policy whose coverage saturates early and converges across prompt seeds."
aliases: ["question-generation-as-policy"]
sources: ["alimaskina-2026"]
---
# Question generation as policy

> When a model generates its own questions about a document to create training supervision, the generation step is not neutral extraction: it is a selection policy that decides which parts of the source ever become a constraint, and it does not scan uniformly.

## Definition / Mechanism
In self-study QA pipelines (Cartridges-style distillation and its relatives), one model reads a document, generates questions or requests about it, and answers them from the same text; the resulting pairs become the training signal for another model. Alimaskina et al. (2026) treat the question-generation step itself as an implicit evidence-selection policy: content the generator anchors a question on becomes supervision, while unselected content may never be practiced — regardless of how fluent or well-formed the resulting QA pairs look.[^c1]

## Why it matters
Measuring the "evidence footprint" (source spans an independent judge model can verify as the basis of a generated answer) across three corpora, the authors found generation turns most of a document into evidence, but only up to an early plateau: aggregate footprint reached 93.0–94.2% on the Cartridges corpus, 75.5–86.4% on LongHealth, and 78.4–81.6% on QASPER, while "after the initial phase, additional interactions add progressively less new evidence, suggesting that the generator increasingly revisits already covered parts of the document rather than expanding uniformly into uncovered regions."[^c2]

Adding prompt diversity does not fix this: different prompt seeds (creative, question, structuring, summarization, use-case) still converge on the same spans — "Mean pairwise Jaccard overlap reaches 0.55–0.68 on Cartridges and remains around 0.39–0.46 on the longer corpora" — so seeds act as weak, overlapping localization policies rather than jointly exhaustive ones.[^c3]

For a stall-2 selection criterion (which axis or evidence to query next), this is a measured failure mode of letting a generator's own judgment of what is "question-worthy" stand in for a selection rule: the resulting policy is neither exhaustive nor does diversifying its inputs buy proportional new coverage past the early plateau.

## Limits
The coverage and overlap numbers are specific to the self-study evidence-extraction protocol, its Qwen3-32B grounding judge, and the three tested corpora (the Cartridges paper, LongHealth, QASPER); they are this setup's measurements, not a general bound on evidence-selection policies. The source is a 2026 arXiv preprint, not yet peer reviewed.

## Related
[[expected-information-gain]] · [[generalized-binary-search]] · [[adaptive-submodularity]] · [[anchor-salience-bias]]

[^c1]: alimaskina-2026 — "We treat this step as an implicit evidence-selection policy. Content selected by the generator becomes supervision through the resulting question and answer, while unselected content may never be practiced."
[^c2]: alimaskina-2026 — "After the initial phase, additional interactions add progressively less new evidence, suggesting that the generator increasingly revisits already covered parts of the document rather than expanding uniformly into uncovered regions."
[^c3]: alimaskina-2026 — "Mean pairwise Jaccard overlap reaches 0.55–0.68 on Cartridges and remains around 0.39–0.46 on the longer corpora."
