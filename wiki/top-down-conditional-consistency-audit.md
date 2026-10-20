---
description: "Scoring a root claim, then its attribute and existence support only where the root is correct, exposes correct high-level answers that lack valid lower-level evidence."
aliases: ["top-down compositional consistency audit", "root-to-attribute-to-existence audit", "conditional attribute and existence accuracy", "RRA ACA ECA cascade"]
sources: ["doi-10-48550-arxiv-2604-01460"]
---
# Top-down conditional consistency audit

A high-level claim can be graded as the top of a chain. The audit takes a generated caption, splits it into a root relational claim and the factual claims beneath it, and checks the root first. Three accuracies follow. Root Relation Accuracy (RRA) is the accuracy of the top claim over all samples. "Attribute Conditional Accuracy (ACA), and Existence Conditional Accuracy (ECA)" are computed on subsets: ACA "asks, among samples with a correct root relation, whether the supporting attribute is also correct," and ECA is computed among samples where "both a correct relation" and a correct attribute hold.[^c1] Each level is conditioned on the level above, so a sample is counted lower down only if it passed the level before.

The mechanism is the conditioning. A plain accuracy on the root reports whether the top claim is right and nothing about what it rests on. Conditioning on a correct root asks whether that correct answer has its support. The paper's phrasing is that "these three metrics progressively test whether a caption remains correct as we descend the evidence hierarchy."[^c2] The authors read the gap they find as a model that "frequently bypasses foundational factual evidence to guess the global context".[^c3] That reading is theirs; the audit measures only the accuracies.

The gap is reported on one base model. For Qwen3-VL-8B on 200 human-created audit samples derived from AGQA-Decomp, the conditional analysis gives the following: "the supporting attribute accuracy only reaches approximately 60%, and the object-existence accuracy still falls short at around 80%," even where the root is already correct.[^c4] The same cascade idea is attributed to the VideoQA line of work: AGQA-Decomp "showed that even when a final answer is correct, its supporting sub-claims may still be inconsistent."[^c5]

The audit also works as a before-and-after diagnostic. The paper runs the same protocol on the base model and on a model post-trained with a structured reward. In the table, the rows read 36.6, 59.7, 78.3 for the base and 47.8, 78.4, 92.1 after training, for RRA, ACA and ECA. The differences printed beside them, +11.2, +18.7 and +13.8, match these rows, so I take the first row as the base model. The text states the result as "with especially large gains on the conditional attribute and existence accuracies."[^c6]

## Limits

- The sample is small. The 200 audit samples are narrowed at each level, so ECA rests only on those with both a correct root and a correct attribute. The subset sizes at the lower levels are not reported in the text I read, and no interval is given. My inference is that these two conditional numbers are the noisiest.
- The gap is shown on one base model for the diagnostic. The trained model is compared with the base on that protocol; other backbones are not run through the audit in this text.
- The ground truth is hand-built. The audit set is "human-created," so each root, attribute and existence label carries the judgement of the people who wrote it, and the cascade inherits any error in that decomposition.
- The raw conditional numbers are not directly comparable across levels. Each denominator is a different subset of the samples, so a lower ACA does not show that attribute recognition is harder than root recognition in any absolute sense. My inference.
- The audit tests whether the support is correct, not whether the model used it. A correct attribute claim under a correct root does not show that the attribute was what produced the root. The answer-blind trace test makes the same limit explicit for reasoning traces (see below). My inference.
- The setting is relational captions over video. Transfer to text-only question answering or to other claim structures is not tested in this text.

## Related

- [[grounding-answer-dual-axis-audit]] — crosses answer correctness with evidence overlap as two independent axes; the cascade instead scores the lower claims only where the top claim holds.
- [[answer-blind-trace-support]] — removes the final answer and asks whether the remaining steps support it; the cascade asks whether the sub-claims survive once the root is correct.
- [[stage-structured-visual-reward]] — a reward that pays for description content; this audit is a measurement and not a training signal.

[^c1]: doi-10-48550-arxiv-2604-01460 — "Attribute Conditional Accuracy (ACA), and Existence Conditional Accuracy (ECA)"
[^c2]: doi-10-48550-arxiv-2604-01460 — "These three metrics progressively test whether a caption remains correct as we descend the evidence hierarchy"
[^c3]: doi-10-48550-arxiv-2604-01460 — "The model frequently bypasses foundational factual evidence to guess"
[^c4]: doi-10-48550-arxiv-2604-01460 — "the supporting attribute accuracy only reaches approximately 60%, and the object-existence accuracy still falls short at around 80%"
[^c5]: doi-10-48550-arxiv-2604-01460 — "AGQA-Decomp showed that even when a final answer is correct, its supporting sub-claims may still be inconsistent"
[^c6]: doi-10-48550-arxiv-2604-01460 — "with especially large gains on the conditional attribute and existence accuracies"
