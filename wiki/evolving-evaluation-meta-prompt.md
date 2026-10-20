---
description: "A judge keeps one meta-prompt across a test sequence, writes a fresh evaluation prompt for each case from it, and folds its own feedback in every few cases, with no labels or validation set."
aliases: ["Learning While Evaluating", "LWE", "test-time evaluator learning", "meta-prompt evolution at test time"]
sources: ["arxiv-2512-06751"]
---
# Evolving evaluation meta-prompt

A fixed judge applies one prompt to every case, so whatever it learns from one case is gone before the next. The alternative in this work is an evaluator that carries state through a test sequence. The state is a meta-prompt: "a meta-prompt serves as a persistent repository of evaluation insights discovered during testing".[^c1] For each new case it is used to write a judging instruction tailored to that case, instead of reusing one instruction everywhere.

Each case goes through four steps. The current meta-prompt generates a sample-specific evaluation prompt: "the current meta-prompt M generates a sample-specific prompt Pt".[^c2] The judge then gives its verdict under that prompt. The judge reflects on its own decision: "The evaluator then reflects on this decision to generate feedback".[^c3] The feedback is buffered, and the meta-prompt is rewritten from the buffer once per batch, "we update the meta-prompt once per batch of b samples (with b = 4 in our experiments)".[^c4] Between batches the meta-prompt stays fixed, so each case is judged under the state left by the last update.

The design point is a split between two kinds of knowledge. The persistent part holds what should stay stable across cases, and the per-case prompt adapts it: the work "explicitly separates general evaluation principles from sample-specific prompts that adapt these principles to each case."[^c5] Nothing is trained and no labelled set is used; the approach works "without requiring training or validation sets".[^c6] The only feedback signal is the judge's own reflection.

The batch size is a real trade-off in this mechanism. Updating after every case is the most expensive setting, "(b=1) incurs the highest computational cost, mirroring the overhead of DC", and it does not necessarily judge best.[^c7] Very large batches fail in the other direction: "overly large batches (b=8) degrade performance because the context used for meta-prompt updates becomes excessively long".[^c8] The paper's reading of its own meta-prompt examples is that updates do more than collect advice; in its words, "rather than accumulating ad-hoc advice, updates progressively distill more structured evaluation principles and sharper criteria".[^c9]

What was measured. On two multimodal pairwise benchmarks, using gpt-4.1 as the evaluator, the per-case prompt alone already beats the fixed prompt, "demonstrating the benefit of tailoring the evaluation criteria to each case".[^c10] The sequential update adds more, and the headline result belongs to its selective variant, which updates only on cases where the judge's two orderings disagree: "Selective LWE achieves even larger gains".[^c11] That variant is reported at a fraction of the cost of the adaptive baselines: "Selective LWE delivers these gains with only 3.9× relative inference cost",[^c12] against "higher costs for other adaptive methods, i.e., 4.4× for TextGrad and 12.9× for DC".[^c13] The gate on which cases to update is the subject of [[self-consistency-difficulty-score]].

## Limits

- Dependence on the base model. "Our method relies on the base capability of the underlying model, making it less effective for relatively weak models."[^c14] An open model with competent vanilla performance "often fails to produce valid evaluation prompts under metaprompt updates".[^c15] The mechanism needs a judge that can already follow the meta-prompt.
- One model in the main comparison: "as a base evaluator for experiments" names gpt-4.1.[^c16] Other models appear in a further table, but the sequence effect is not shown across a range of judge strengths.
- Subsets. "we use representative subsets where necessary due to API budget constraints";[^c17] of MMRewardBench, 1,000 of 4,711 cases were run. The sizes of the test sequences are therefore modest, and behaviour over much longer streams is not reported (my reading).
- Pairwise only. The paper says "the proposed LWE can extend to direct assessment and other evaluation settings";[^c18] that extension was not tested.
- Consistent but wrong. Cases the judge gets wrong in both orders "remain indistinguishable without access to ground-truth labels",[^c19] so an update driven by disagreement cannot reach them (my inference from the paper's own admission).
- Cost is measured as "the total character length of input and output normalized to the vanilla baseline",[^c20] not in tokens or money. The paper's ratios are relative to that unit.
- The paper's support that the gains come from accumulated experience is the claim that "learning effects arise from accumulated experience, rather than incidental ordering artifacts",[^c21] backed by small variance across orderings. It is one judge family and two benchmarks.

## Related

- [[self-consistency-difficulty-score]] — the same disagreement-as-signal idea; the selective variant uses order-swap disagreement to decide which cases update the meta-prompt
- [[llm-judge-biases]] — the order sensitivity of judges that makes order-swap disagreement informative in the first place
- [[constitutive-rubric-criteria]] — the criteria a judge grades against; here the criteria are rewritten for each case
- [[experience-repository]] — the agent-side store of past trajectories prepended as context; here the stored material is the judge's own criteria
- [[zoned-experience-evolution]] — evolving a library rather than weights for a frozen agent, the same move outside evaluation

[^c1]: arxiv-2512-06751 — "a meta-prompt serves as a persistent repository of evaluation insights discovered during testing"
[^c2]: arxiv-2512-06751 — "the current meta-prompt M generates a sample-specific prompt Pt"
[^c3]: arxiv-2512-06751 — "The evaluator then reflects on this decision to generate feedback"
[^c4]: arxiv-2512-06751 — "we update the meta-prompt once per batch of b samples (with b = 4 in our experiments)"
[^c5]: arxiv-2512-06751 — "explicitly separates general evaluation principles from sample-specific prompts that adapt these principles to each case"
[^c6]: arxiv-2512-06751 — "without requiring training or validation sets"
[^c7]: arxiv-2512-06751 — "(b=1) incurs the highest computational cost, mirroring the overhead of DC"
[^c8]: arxiv-2512-06751 — "overly large batches (b=8) degrade performance because the context used for meta-prompt updates becomes excessively long"
[^c9]: arxiv-2512-06751 — "rather than accumulating ad-hoc advice, updates progressively distill more structured evaluation principles and sharper criteria"
[^c10]: arxiv-2512-06751 — "demonstrating the benefit of tailoring the evaluation criteria to each case"
[^c11]: arxiv-2512-06751 — "Selective LWE achieves even larger gains"
[^c12]: arxiv-2512-06751 — "Selective LWE delivers these gains with only 3.9× relative inference cost"
[^c13]: arxiv-2512-06751 — "higher costs for other adaptive methods, i.e., 4.4× for TextGrad and 12.9× for DC"
[^c14]: arxiv-2512-06751 — "Our method relies on the base capability of the underlying model, making it less effective for relatively weak models"
[^c15]: arxiv-2512-06751 — "the model often fails to produce valid evaluation prompts under metaprompt updates"
[^c16]: arxiv-2512-06751 — "as a base evaluator for experiments"
[^c17]: arxiv-2512-06751 — "we use representative subsets where necessary due to API budget constraints"
[^c18]: arxiv-2512-06751 — "the proposed LWE can extend to direct assessment and other evaluation settings"
[^c19]: arxiv-2512-06751 — "remain indistinguishable without access to ground-truth labels"
[^c20]: arxiv-2512-06751 — "computes the total character length of input and output normalized to the vanilla baseline"
[^c21]: arxiv-2512-06751 — "learning effects arise from accumulated experience, rather than incidental ordering artifacts"
