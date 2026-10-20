---
description: "Accuracy is class-agnostic and macro-F1 averages the classes, so either can look fine while the model misses one class; per-class recall shows which class fails under imbalance."
aliases: ["class-wise evaluation", "per-class recall", "unweighted average recall", "UAR", "class-wise reporting"]
sources: ["arxiv-2511-23101"]
---
# Class-wise recall diagnostic

On a skewed binary label, a classifier can score well on the aggregate and still fail one class. Accuracy is the share of all items answered right, so it is dominated by the majority class: a model that returns the majority label for everything keeps a high score. Macro-F1 averages the two class-level F1 scores, which narrows the gap but still does not say which class is failing. In a study of zero-shot prediction of Big Five trait presence from text, the authors state the consequence directly: "accuracy and macro-F1 mask significant asymmetries, with per-class recall offering clearer diagnostic value."[^c1]

The mechanism is arithmetic. The paper's illustration uses a model that gets 400 of 500 "high" cases and 200 of 500 "low" cases right: that yields 80% accuracy, yet the negative-class F1 would fall to about 0.3.[^c2] The general point is the paper's: "Such imbalances are hidden without class-wise reporting."[^c8] Accuracy "is class-agnostic and remains high if only the majority class is predicted, whereas UAR penalizes such imbalances."[^c3] The paper uses the name UAR without spelling it out in that footnote; reading it as the mean of the per-class recalls is my inference from the name.

Recall and precision do not carry the same information here. The paper finds that precision follows the label distribution, while recall does not: "Precision gaps mostly reflect dataset distributions, but recall behavior varies widely across models and traits."[^c4] A table of precision alone can therefore look balanced while a model misses most of the minority class. The per-class recall is the column that moves.

The gap shows up in the paper's own results. Of 135 configurations, only 13 reached a class-wise F1 of at least 0.5 on both classes, and the authors note "the rarity of balanced predictions."[^c5] Their summary is that "apparent aggregate successes often mask bias."[^c6]

Within this wiki the same move appears in other forms. [[support-skew-in-claim-verification]] shows a verifier whose balanced F1 hides a lean toward one label. [[search-decision-f1]] scores a search decision on one class alone, so an always-search policy scores zero whatever its accuracy. [[positive-first-most-ambiguous-selection]] handles rare-positive imbalance by ranking the class that matters first. The "accuracy masks" notes, [[accuracy-masks-unstable-reasoning]] and [[clean-accuracy-masks-adversarial-collapse]], hide failures of other kinds, not a class-level one.

What survives transfer is the arithmetic: class-agnostic accuracy is high under any skewed binary label when the majority is predicted. What does not follow from the paper is its choice of recall as "the most informative indicator". That is a judgement about which error matters in personality prediction, and the paper does not compare it with other diagnostics.

## Limits

- The evidence is one task family: binary trait presence, zero-shot, five language models, three datasets. The claim that per-class recall is the most informative diagnostic is the authors' reading of that setting. They do not test it against calibration measures or confusion-matrix summaries.
- The paper's screen for "informative" configurations uses a 0.5 threshold on accuracy and F1, and the authors concede that "this threshold does not represent true chance performance under class" imbalance.[^c7] The count of 13 is therefore a count against an arbitrary bar, not against a chance baseline.
- The 80% example is the paper's illustration, not a measured result, and I have not checked the numbers against a dataset.
- Per-class recall read alone is also gameable: a model that predicts the positive label for every item has perfect positive recall. Reading the two classes together is what makes the diagnostic work. This last point is my inference; the paper reports both classes but does not discuss the degenerate case.

## Related

- [[support-skew-in-claim-verification]] — a balanced F1 hiding a directional lean in a claim verifier; the same aggregate-hides-direction move in another task.
- [[search-decision-f1]] — an F1 on one class that a constant policy cannot game with accuracy.
- [[positive-first-most-ambiguous-selection]] — rare-positive imbalance handled by ranking the positive class first.
- [[accuracy-masks-unstable-reasoning]] — accuracy hiding instability, a different failure than a class-level one.
- [[clean-accuracy-masks-adversarial-collapse]] — a clean-accuracy score hiding adversarial collapse.

[^c1]: arxiv-2511-23101 — "accuracy and macro-F1 mask significant asymmetries, with per-class recall offering clearer diagnostic"
[^c2]: arxiv-2511-23101 — "yields 80% accuracy, yet the negative-class F1 would fall to"
[^c3]: arxiv-2511-23101 — "Accuracy is class-agnostic and remains high if only the majority class is predicted, whereas UAR penalizes such imbalances."
[^c4]: arxiv-2511-23101 — "Precision gaps mostly reflect dataset distributions, but recall behavior varies widely across models and traits."
[^c5]: arxiv-2511-23101 — "highlights the rarity of balanced predictions."
[^c6]: arxiv-2511-23101 — "apparent aggregate successes often mask bias"
[^c7]: arxiv-2511-23101 — "this threshold does not represent true chance performance under class"
[^c8]: arxiv-2511-23101 — "Such imbalances are hidden without class-wise reporting."
