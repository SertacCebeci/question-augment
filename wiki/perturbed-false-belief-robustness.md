---
description: "False-belief accuracy of LLMs collapses under small task perturbations, and chain-of-thought helps faithfully on most perturbation classes but lowers accuracy on others."
aliases: ["robust theory of mind", "ostensible vs robust ToM", "perturbed ToM tasks"]
sources: ["arxiv-2602-22072"]
---
# Perturbed false-belief robustness

A model that passes a classic false-belief task may only be matching surface cues. The test for this is to keep the task's logic and change one element at a time. Nickel et al. built 1088 handcrafted examples in 10 perturbation classes, each unperturbed task having up to ten perturbed variants. Every sentence is annotated with the protagonist's correct current belief, so a valid reasoning chain can be checked step by step.[^c1]

## What was found

Six open-source LLMs were tested. Without perturbation, four showed ostensible ToM-like behavior. Under perturbation, only Llama-3-70B and DBRX kept limited robustness, defined as at least 50% accuracy across five perturbation classes.[^c2] Perturbations that require spatial reasoning were hard for every model.[^c3] The authors read the drop for Transparent Container and Preposition Replacement as heuristic matching, for example "looking inside" implying "knowing", instead of a stable model of the agent. This is their interpretation.[^c4]

## Chain-of-thought is class-dependent

CoT prompting slightly improved accuracy on unperturbed tasks and overall across perturbation classes, most on Untrustworthy Testimony and Add Unrelated Information. It lowered accuracy on others, notably Conclusion from Sentiment and Automatic Change Knowledge, and on many sanity-check tasks that have a false-belief structure without testing ToM.[^c5] The authors' explanation is that CoT helps when it adds structure, but hurts when an early detail is decisive. One example is a protagonist who cannot read. Another is a question about the true world state instead of the protagonist's belief. Their conclusion is that CoT should be applied selectively.[^c6]

## Faithfulness and placebo

Faithfulness is measured as the correlation between CoT correctness and final-answer correctness, using Φ for binary and point-biserial for continuous scores. A model counts as faithful at 0.4 or above with p ≤ 0.05.[^c7] Correlations were mostly strong, and strongest in larger and more recent models, so wrong answers mostly follow flawed steps and are not post-hoc justifications of a guess.[^c8] Simpler overlap measures (Rouge-LCS, Rouge-LPS, Transition Overlap) followed the same trends with smaller correlations and some outliers, so they are less useful than the proper-subsequence measure.[^c9]

A placebo check splits answers by whether the CoT was correct. If CoT improves accuracy even when its reasoning is wrong, the gain comes from the prompt's style and not from the reasoning. Only Mixtral showed this.[^c10]

## Limits

- Six open-source models, English false-belief tasks, handcrafted data. Nothing is shown for frontier or reasoning-trained models.
- The "heuristic matching" account of the drop is the authors' reading. No intervention tests it.
- Faithfulness here is a correlation with gold reasoning chains, not a causal test of the chain.
- The reasons CoT hurts some classes are hypotheses and were not isolated.
- The relevance to asking is my inference: a question's answer can depend on one decisive early detail, so a reasoning step added before answering is not always safe.

## Related

- [[minimal-edit-prompt-attack]] — another case where small meaning-preserving changes flip correct answers
- [[cot-judge-detection-localization-gap]] — judging the correctness of chain-of-thought steps
- [[emergent-clarification-behavior]] — lists theory of mind among behaviors a model may or may not show

[^c1]: arxiv-2602-22072 — "Each unperturbed task is accompanied by up to ten perturbed variants"
[^c2]: arxiv-2602-22072 — "with only Llama-3-70B and DBRX maintaining limited robustness (limited RToM, ≥ 50% accuracy across five perturbation classes)"
[^c3]: arxiv-2602-22072 — "Especially perturbations that introduce the"
[^c4]: arxiv-2602-22072 — "rely on superficial heuristic matching (e.g., associating ”looking inside” with ”knowing”)"
[^c5]: arxiv-2602-22072 — "Surprisingly, we even observe reduced performance"
[^c6]: arxiv-2602-22072 — "ought"
[^c7]: arxiv-2602-22072 — "A model is"
[^c8]: arxiv-2602-22072 — "we observe significant, mostly strong correlations"
[^c9]: arxiv-2602-22072 — "indicating a limited utility of these simpler methods."
[^c10]: arxiv-2602-22072 — "The only exception is Mixtral, where"
