---
description: "Scoring an LLM's abstention by why it abstained — an underspecified question (data uncertainty) or its own capability limit (model uncertainty) — as two separate F1s, not one calibration number."
aliases: ["uncertainty attribution", "UA-Bench", "Data-Uncertain F1", "Model-Uncertain F1", "DU-F1", "MU-F1"]
sources: ["arxiv-2604-17293"]
---
# Uncertainty-source attribution

> Abstaining is cheap; naming *why* is the harder, separately-measurable
> skill — and it does not track answer accuracy.

## Definition / Mechanism

Ren et al. (2026) score abstention as a three-way decision
rather than a binary refuse/answer, because "existing methods do not
distinguish whether abstention arises from ambiguity or incompleteness in
the question itself, or from the model's own limited knowledge or
reasoning capacity." A wrong answer on a well-posed question is a failure
to attribute **model uncertainty**; correctly flagging a genuinely
underspecified question is successful attribution of **data uncertainty**:
"UA-Bench evaluates decision-oriented attribution rather than confidence
calibration. A wrong answer on an answerable question reflects a failure
to recognize capability limits, while correctly identifying missing
information or ambiguity reflects successful attribution of data
uncertainty."[^c1]

Their benchmark, UA-Bench (3,500+ knowledge- and reasoning-intensive
questions), scores each model on two independent F1s over disjoint sets —
DU-F1 on inherently unanswerable questions, MU-F1 on answerable questions
the model got wrong — rather than one pooled [[abstention]] rate, so a
model that is good at one kind of refusal but bad at the other cannot hide
behind an averaged score.

## Why it matters

Across 18 frontier LLMs, the two skills dissociate sharply and accuracy is
not a proxy for either: "on knowledge-intensive tasks, Qwen3-8B achieves a
respectable 69.8% DU-F1 but a negligible 4.0% MU-F1; similarly, even the
high-performing Gemini 3 Flash shows a stark contrast between identifying
data deficits (72.0% DU-F1) and admitting its own knowledge gaps (29.0%
MU-F1)." "Crucially, high answer accuracy does not imply strong
uncertainty attribution. On reasoning tasks, Qwen3-4B-Instruct achieves
72.3% accuracy but only 23.3% MU-F1, indicating that it frequently
misattributes its failures or hallucinates rather than acknowledging its
own limitations."[^c3]

Thinking modes make this worse, not better, for the harder of the two
skills: "A striking example is Qwen3-235B on reasoning tasks: the thinking
variant improves accuracy to 80.0% but its Model Uncertainty recognition
collapses from 84.8% to 0.0%." A model whose reasoning trace makes it more
confident a solution exists is, on this evidence, more likely to blame the
question instead of its own limits when it fails.[^c4]

## Limits

Model uncertainty is not statically labeled — it is defined post hoc as
"the model failed a theoretically answerable question," so MU-F1 is
relative to what the evaluated model, not some ground truth, could not do;
it is not a property of the question alone the way data uncertainty is. A
manual check of 100 outputs found the rule-based label extractor correct
in every case and the answer-correctness judge mismatched human judgment
in only 1 of the answerable cases inspected — evidence the metric is not
mostly judge noise, but a small sample. The benchmark covers
knowledge-intensive and mathematical-reasoning tasks only; whether the
data/model split holds for open-ended or multi-turn settings is
**unverified**.

## Related

- [[uncertainty-decomposition]]
- [[abstention]]
- [[detection-to-abstention-gap]]
- [[attribution-aware-rl-reward]]

[^c1]: arxiv-2604-17293 — "UA-Bench evaluates decision-oriented attribution rather than confidence calibration. A wrong answer on an answerable question reflects a failure to recognize capability limits, while correctly identifying missing information or ambiguity reflects successful attribution of data uncertainty."
[^c3]: arxiv-2604-17293 — "Crucially, high answer accuracy does not imply strong uncertainty attribution. On reasoning tasks, Qwen3-4B-Instruct achieves 72.3% accuracy but only 23.3% MU-F1, indicating that it frequently misattributes its failures or hallucinates rather than acknowledging its own limitations."
[^c4]: arxiv-2604-17293 — "A striking example is Qwen3-235B on reasoning tasks: the thinking variant improves accuracy to 80.0% but its Model Uncertainty recognition collapses from 84.8% to 0.0%."
