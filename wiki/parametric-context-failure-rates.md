---
description: "Context errors split into two conditional rates: failing to update a wrong parametric answer after correct context, and dropping a right one after misleading context."
aliases: ["over-reliance on parametric knowledge rate", "vulnerability to misleading context rate", "OR and VM failure rates"]
sources: ["arxiv-2512-02299"]
---
# Parametric context failure rates

A language model that answers a question from memory and is then shown a document can go wrong in two different ways, and a single accuracy number merges them. Zhang et al. separate them as two conditional rates computed over the same instances. The first is over-reliance on parametric knowledge: the model "fails to update an incorrect answer even when provided with correct context".[^c1] The second is vulnerability to misleading context: the model answers correctly with no context and "changes to an incorrect answer after being provided with an incorrect context".[^c2]

Each is a rate over one base condition. Over-reliance is conditioned on the no-context answer being wrong: the OR rate is the share of those instances that stay wrong when the correct document is added.[^c3] Vulnerability is conditioned on the no-context answer being right: the VM rate is the share of those that flip to the wrong answer when the incorrect document is added. The two numerators are read off the same five prompt conditions. The no-context prompt (NC) gives the parametric answer. The correct-context prompt (CC) tests whether the model can be moved toward a right answer. The incorrect-context prompt (IC) tests whether a right answer can be moved away from.

The split changes what a comparison says. In the paper, Meditron3-8B shows over-reliance in "exhibits over-reliance on parametric knowledge in 38.3% of cases" of its failures, against 66.5% for its base model Llama-3.1-8B-Instruct; it is "misled by incorrect context in 31.9% of cases", against 58.7% for the base.[^c4][^c5] The authors draw the general lesson that "language models are more likely to fail due to over-reliance on parametric knowledge than due to misleading context."[^c6] A model could be made more robust to misleading documents and still be stuck on its memory, and the two rates show which of the two is happening.

The control is kept narrow on purpose. The five prompts share one question and one instruction, and differ only in the context block: "without introducing additional variability in the phrasing of the prompt."[^c7] The rate difference between two prompts is therefore attributed to the context, not to rewording.

Reading the rates across models is my own inference, not a result of the paper. The denominators differ, so OR and VM for one model are not halves of one error count. A model with high parametric accuracy has many instances in the VM denominator; a model that mostly fails from memory has many in the OR denominator. A ranking on one rate can reverse on the other.

## Limits

- One benchmark: HealthContradict has 81 questions and 920 contradictory document pairs, and it is restricted to yes/no answers. The authors chose this "to enable controlled analysis of model behavior under conflicting contexts."[^c8] Free-form answers are not tested.
- The no-context prompt is not format-matched to the other four. The authors write that "variables exist between the Prompt NC (using only parametric" memory and the other prompts, "which could influence model performance."[^c9] A part of any gap between NC and the context prompts may be prompt format, not context.
- Two 7–8B models are compared in the failure analysis. The authors "were unable to perform experiments on even larger language models."[^c10] No claim about larger models follows from these rates.
- The rates use the argmax answer. They say nothing about whether the model's confidence moved, which the same paper reports separately through probability distributions.

## Related

- [[conflicting-evidence-order-effect]] — the same two-document benchmark, read through the order of the documents instead of through the two failure modes
- [[context-use-evaluation-axis]] — why a parametric-only score does not show these failures at all
- [[parametric-suppression]] — a layer-level account of a stored answer overwritten by a later signal, one mechanism that could produce over-reliance
- [[parametric-knowledge-gates-retrieval-noise-damage]] — retrieved noise hurts where the model's own knowledge is weak, a different gate on the same interaction

[^c1]: arxiv-2512-02299 — "fails to update an incorrect answer even when provided with correct context"
[^c2]: arxiv-2512-02299 — "changes to an incorrect answer after being provided with an incorrect context"
[^c3]: arxiv-2512-02299 — "The OR rate is then defined as"
[^c4]: arxiv-2512-02299 — "exhibits over-reliance on parametric knowledge in 38.3% of cases"
[^c5]: arxiv-2512-02299 — "misled by incorrect context in 31.9% of cases"
[^c6]: arxiv-2512-02299 — "language models are more likely to fail due to over-reliance on parametric knowledge than due to misleading context"
[^c7]: arxiv-2512-02299 — "without introducing additional variability in the phrasing of the prompt"
[^c8]: arxiv-2512-02299 — "We focused on yes/no questions to enable"
[^c9]: arxiv-2512-02299 — "variables exist between the Prompt NC (using only parametric"
[^c10]: arxiv-2512-02299 — "We were unable to perform experiments on even larger language models"
