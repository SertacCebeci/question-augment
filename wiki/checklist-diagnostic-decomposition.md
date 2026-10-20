---
description: "Replacing one holistic label question with ten independent binary concept questions, answered by an LLM and aggregated by a small tree, trades in-domain accuracy for cross-dataset robustness."
aliases: ["xList-Hate", "checklist-based classification", "diagnostic reasoning reframing", "factorized predicate checklist"]
sources: ["arxiv-2602-05874"]
---
# Checklist diagnostic decomposition

Instead of asking a model "is this hate speech?", xList-Hate asks ten binary questions, each a separate conceptual factor drawn from legal definitions, platform policies and academic frameworks (targeting a protected group, derogation, dehumanization, endorsement, incitement and so on). A language model answers each question independently, giving a 10-bit vector. A decision tree trained on those bits makes the final call.[^c1]

## Mechanism

The design splits two jobs. The LLM does the semantic judgment on well-defined, self-contained predicates. A learned, transparent layer does the decision policy.[^c11] The authors say the aggregation is deliberately not a fixed rule. Hate-speech datasets carry different implicit definitions, and a hard-coded rule "would impose a normative definition that may systematically misalign with the labeling criteria of" a given dataset.[^c2] The tree therefore learns which combinations of factors a given dataset treats as decisive, while each prediction stays a readable conjunction of satisfied predicates.[^c3]

Because the questions are fixed and answered without supervision, the feature space does not move with the labels. The authors argue that this stops the system from fitting isolated annotation errors. In their qualitative cases, a mislabelled example with an explicit slur followed the same decision path as similar correctly labelled ones, and their word is that the diagnostic "space itself is constrained by explicit conceptual questions answered in an unsupervised manner, preventing the system".[^c4] The same transparency lets a disagreement be attributed to a mislabel or to a definitional choice. One case was a quoted song lyric with no speaker endorsement, rejected explicitly through the endorsement question.[^c5]

## What was measured

Robustness is scored by relative AUC, the out-of-domain AUC divided by the in-domain AUC of the same trained model; values near or above 100% mean performance survives the shift.[^c6] Across training sets and backbones, supervised fine-tuning "typically yields the strongest in-domain AUC", but the checklist preserves more of its performance under domain shift. The authors also report that encoder-based classifiers degrade more than causal LLMs and checklist pipelines.[^c7] When trained on Measuring Hate Speech, fine-tuning led on absolute OOD AUC, but the "gap closes as the model size increases".[^c8] The checklist consistently beat zero-shot LLM classification.[^c9]

## Limits

- The gain is in relative robustness, not absolute performance. The authors concede slightly lower absolute out-of-domain performance than fine-tuning in some settings.[^c9]
- Cost: it needs "multiple LLM calls per input", so inference is several times dearer than one classification call.[^c9]
- The noise-robustness claim rests on a handful of hand-picked disagreement cases and an argument, not a controlled noise-injection experiment. The text calls the cases evidence the framework "can be less sensitive". This is my reading of what was shown, not a measured effect size.
- The ten questions were chosen by the authors; the work does not test how sensitive results are to which questions are included or how they are worded.
- The closing claim that any task expressible as interpretable semantic factors may benefit is untested outside hate speech.[^c10]
- The tree is trained on one dataset's labels, so its aggregation still inherits that dataset's definition; only the features are definition-neutral.

## Related

- [[self-ask-decomposition]] — also splits one question into sub-questions, but to answer one query rather than to build a stable feature space for a classifier
- [[factored-versus-entangled-supervision]] — a related argument for factored structure over a single entangled target
- [[dependency-aware-checklist-scoring]] — checklists used to grade, not to classify
- [[definition-blindness]] — the failure of treating a contested concept as if its definition were fixed

[^c1]: arxiv-2602-05874 — "decompose the task into a set of ten"
[^c2]: arxiv-2602-05874 — "would impose a normative definition that may systematically misalign with the labeling criteria of"
[^c3]: arxiv-2602-05874 — "each prediction can be explained as a conjunction of satisfied predicates"
[^c11]: arxiv-2602-05874 — "This design intentionally separates semantic judgment from classification"
[^c4]: arxiv-2602-05874 — "space itself is constrained by explicit conceptual questions answered in an unsupervised manner, preventing the system"
[^c5]: arxiv-2602-05874 — "The third example involves a song lyric"
[^c6]: arxiv-2602-05874 — "A relative AUC close to or above 100% indicates strong robustness under domain"
[^c7]: arxiv-2602-05874 — "supervised fine-tuning typically yields the strongest in-domain AUC"
[^c8]: arxiv-2602-05874 — "gap closes as the model size increases"
[^c9]: arxiv-2602-05874 — "requiring multiple LLM calls per input"
[^c10]: arxiv-2602-05874 — "classification problem that can be expressed as a set of interpretable semantic factors may benefit from this approach,"
