---
description: "A dialogue model's own uncertainty over its next action predicts human clarification timing only weakly, so human timing is a poor training signal for a model's ask-trigger."
aliases: []
sources: ["testoni-2024", "doi-10-48550-arxiv-2609-34506"]
---
# Human-model uncertainty dissociation

In the CoDraw collaborative drawing task, a Drawer agent's predictive
uncertainty (the score assigned to a candidate clipart, or the [[entropy]] of
its distribution over an attribute like size or orientation) is only a weak
predictor of the turns at which *human* Drawer players actually ask a
clarification question. A logistic regression fit on the model's own
uncertainty to predict human clarification-asking turns yields an Average
Precision of 0.188 (epoch 15; average across 5 different initialization
seeds). This result is above the random baseline (0.188 vs. 0.142, p <
0.05), indicating that model uncertainty has some degree of predictive
power. Nevertheless, performance is poor. Only clipart-selection
uncertainty carries significant predictive power among the four
uncertainty types tested; size, orientation and position uncertainty do
not.[^c1]

A follow-up keyword-matching analysis of under-specified Teller
instructions shows the same players do not follow one consistent
clarification strategy: for instructions omitting an object's size, only
23% of follow-up Drawer turns include any clarification question; for
instructions omitting location, 49% do — and only a minority of those
questions target the missing attribute itself. This high human
disagreement on deciding whether to clarify or not suggests that learning
when to ask clarification questions from human clarification behaviour may
not be optimal.[^c2]

The dissociation motivates Testoni & Fernández (2024)'s
own design choice: rather than training a "when to ask" module to imitate
the turns at which humans asked (their comparison baseline reaches only
0.35 Average Precision against the same human-turn target), they trigger
clarification directly from the Drawer's own uncertainty and show this
yields the larger task-success gain (see
[[entropy-threshold-clarification-trigger]]).

The same gap shows up in image classification, measured against a vote distribution rather than clarification timing. Across eight fine-tuned vision models on two multi-annotator benchmarks, the authors find that "model uncertainty correlates only weakly to moderately with human disagreement".[^c3] Unanimity among the models does not separate contested from uncontested images: "unanimity itself is uninformative about ambiguity, that is, the models are unanimous on 93% of images where humans agree, but also on 78% of images where they disagree".[^c4] Thresholding does not repair it: "A confidence threshold does little to remove this ambiguity."[^c5] The authors also add the disagreement among the models themselves, [[predictive-multiplicity]], and report that it gives "only modest improvement".[^c6]

## Limits

Established in one task (CoDraw, template-generated size questions), one
architecture (an LSTM-based Drawer), and one [[clarification-request]]
annotation source (Madureira & Schlangen's CoDraw-iCR). The uncertainty
measures compared are a raw softmax score and label entropy, not a
calibrated probability; the paper's own follow-up check (ensemble-based
epistemic/aleatoric uncertainty) found no better correlation, but neither
was tested against modern LLM-native uncertainty measures such as semantic
entropy over generated text.

## Related

[[clarification-benchmarks]], [[semantic-entropy]], [[constraint-seeking]]

[^c1]: testoni-2024 — "yields an Average Precision of 0.188 (epoch 15; average across 5 different initialization seeds). This result is above the random baseline (0.188 vs. 0.142, p < 0.05), indicating that model uncertainty has some degree of predictive power. Nevertheless, performance is poor."
[^c2]: testoni-2024 — "This high human disagreement on deciding whether to clarify or not suggests that learning when to ask clarification questions from human clarification behaviour may not be optimal."
[^c3]: doi-10-48550-arxiv-2609-34506 — "model uncertainty correlates only weakly to moderately with human disagreement"
[^c4]: doi-10-48550-arxiv-2609-34506 — "unanimity itself is uninformative about ambiguity, that is, the models are unanimous on 93% of images where humans agree, but also on 78% of images where they disagree"
[^c5]: doi-10-48550-arxiv-2609-34506 — "A confidence threshold does little to remove this ambiguity."
[^c6]: doi-10-48550-arxiv-2609-34506 — "predictive multiplicity provides only modest improvement"
