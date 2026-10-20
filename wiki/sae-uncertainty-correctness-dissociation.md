---
description: "SAE features for an LLM's uncertainty and its incorrectness are functionally distinct: uncertainty features are essential, incorrectness features inert, confounded ones harmful and predictive."
aliases: ["confounded features", "pure uncertainty features", "pure incorrectness features"]
sources: ["arxiv-2604-19974", "arxiv-2512-07730"]
---
# SAE uncertainty–correctness dissociation

> The feature that fires when a model is uncertain is not the feature that
> fires when it is wrong — and the one that fires for both is the only one
> worth touching.

## Definition / Mechanism

Patel, Chen, Wei, Papalexakis & Chen (2026) partition
multiple-choice predictions on a 2×2 grid — confident/uncertain crossed
with correct/incorrect, entropy-thresholded at the 25th/75th percentiles —
and run sparse-autoencoder (Llama Scope, Gemma Scope) features through a
Mann-Whitney U test against two contrasts: uncertain-correct vs.
confident-correct (isolates *uncertainty* features), and confident-incorrect
vs. confident-correct (isolates *incorrectness* features). A feature
significant on both is **confounded**. Suppressing each category (via an
encode–zero–decode intervention on the residual stream) reveals three
distinct functional roles rather than one shared "confidence" mechanism:
"Pure uncertainty features are functionally essential: suppressing them
severely degrades accuracy. Pure incorrectness features are functionally
inert: despite showing statistically significant activation differences
between correct and incorrect predictions, the majority produce near-zero
change in accuracy when suppressed."[^c1]

Pure uncertainty features are load-bearing at the tail: "the worst single
feature causes a −10.21% accuracy collapse at layer 31, and the surrounding
layers consistently produce the largest drops."

[^c5]

Pure incorrectness features, despite tracking the correct/incorrect split by
construction, do nothing when removed: "68% produced near-zero change in
accuracy when suppressed individually, with a mean accuracy delta of
0.03%."

[^c4]

Confounded features are the odd category out — small, but the only one
whose *suppression* is a net gain: "targeted suppression of them yields a
1.1% accuracy improvement and a 75% entropy reduction, with effects
transferring across the ARC-Challenge and RACE benchmarks."

[^c2]

The whole pattern replicates cross-architecture (Llama-3.1-8B, Gemma-2-9B)
and cross-dataset (MMLU → ARC-Challenge, RACE) without re-selecting
features.

[^c6]

## Why it matters

Confounded features are also the most *informative* ones: a 3-feature
logistic classifier from one mid-network layer predicts correctness at
AUROC ≈0.79, near the output-entropy baseline (0.805), and gating
[[abstention]] on it "raises accuracy from 62% to 81% at 53% coverage."

[^c3]

That also beats the model's own self-abstention option: "3 features from a
single layer enable accuracy-coverage tradeoffs that substantially
outperform the model's own self-abstention."

[^c7]

For a task-agnostic account of commitment, the result says the scalar an
answerer reports as "confidence" is not one signal split two ways after
the fact — a model can carry an accurate, behaviorally load-bearing sense
that *something is uncertain* while carrying a separate, behaviorally
inert trace of *having been wrong*, and only the population that mixes
both is worth reading out for a stop/abstain decision.

## Limits

- Both models tested are 8–9B parameters; scale generalization is
  untested, and the finding depends on the specific published SAE
  decomposition used for each model.[^c8]
- Evaluation is confined to multiple-choice questions; a feature inert
  under MCQ suppression may still participate in chain-of-thought or
  open-ended generation — inertness is not shown to be a general property
  of the feature, only of this protocol.[^c9]
- Thousands of features are tested at p < 0.05 with no formal
  multiple-comparison correction, which this note flags as `unverified`
  for the exact feature counts in the paper's per-layer tables, though the
  suppression and AUROC effects were validated on a held-out split.

## Related

[[abstention]] · [[calibration]] · [[knowledge-verbalization-dissociation]] · [[certainty-default-sparse-override]] · [[recognition-refusal-dissociation]]

- [[correctness-contrast-feature-steering]] — a contrast between features on correct and hallucinated answers picks one feature to steer, not to suppress; the same split, used for a different intervention, with suppression not tested there.[^c10]

[^c1]: arxiv-2604-19974 — "Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy. Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed."
[^c2]: arxiv-2604-19974 — "targeted suppression of them yields a 1.1% accuracy improvement and a 75% entropy reduction, with effects transferring across the ARC-Challenge and RACE benchmarks."
[^c3]: arxiv-2604-19974 — "the activations of just 3 confounded features from a single mid-network layer predict model correctness (AUROC ∼0.79), enabling selective abstention that raises accuracy from 62% to 81% at 53% coverage."
[^c4]: arxiv-2604-19974 — "In Llama, of 137 tested features, 68% produced near-zero change in accuracy when suppressed individually, with a mean accuracy delta of 0.03% and a mean entropy delta of +0.001 (essentially zero)."
[^c5]: arxiv-2604-19974 — "Suppressing pure uncertainty features degrades accuracy, with the effect concentrated in late layers. In Llama, the worst single feature causes a −10.21% accuracy collapse at layer 31, and the surrounding layers consistently produce the largest drops."
[^c6]: arxiv-2604-19974
[^c7]: arxiv-2604-19974
[^c8]: arxiv-2604-19974 — "Both models are in the 8-9B range; scale generalization is untested. Our conclusions depend on the specific SAE decompositions used (Llama and Gemma Scope)."
[^c9]: arxiv-2604-19974 — "Our evaluation is limited to multiple-choice tasks, and the functional roles may be task-dependent. Features inert under MCQ may participate in chain-of-thought or open-ended generation, though the quadrant framework itself is task-agnostic."
[^c10]: arxiv-2512-07730 — "explicitly contrasting activations between correct and hallucinated responses"
