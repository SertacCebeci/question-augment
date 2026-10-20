---
description: "Rating confidence in the same generation that solves the problem flips the confidence-accuracy direction from weakly aligned to opposed; a separate confidence-only pass avoids it."
aliases: ["reasoning contamination effect", "joint solve-and-rate interference"]
sources: ["arxiv-2603-25052"]
---
# Reasoning contamination of verbalized confidence

Miao and Ungar (2026) probe three open-weight 7-8B models and find that the internal signal for "how likely am I to be correct" and the signal for "how confident do I say I am" are separate, nearly orthogonal linear directions: ridge-probe weight vectors have cosine similarity below 0.04 at all layers.[^c1] Their reading is that miscalibration is a readout failure rather than a knowledge deficit: the accuracy signal is present in the residual stream, but generation does not use it.[^c2]

## The effect

Two prompt conditions are compared. In the pure condition the model rates its confidence without solving the problem. In the joint condition it solves and rates in one generation. For each, a contrastive confidence direction (high-confidence minus low-confidence activations) and a contrastive accuracy direction are extracted per layer and compared by cosine similarity.[^c3]

Under the pure condition the two directions are orthogonal early and become weakly positive, reaching +0.26 at layer 21. Under the joint condition they are anti-correlated across all layers, reaching -0.63 at layer 15. The authors call this the reasoning contamination effect: the confidence-encoding direction actively opposes the correctness direction.[^c4] When steering verbalized confidence in joint generation, the more the stated confidence was moved, the more accuracy eroded.[^c5]

## What follows from it

The paper's pipeline separates the passes. A pure-confidence pass is read with a linear probe for the internal accuracy estimate, and contrastive activation addition steers the verbalized output to match it; solving runs untouched in a separate pass. Reported ECE falls 4-7x against unsteered verbalized confidence; Mistral drops from 35.1 to 3.3 ECE.[^c6] Token-probability baselines were far worse (ECE of 68 or more).[^c6b]

For asking and answering, the claim is that the stated confidence of an answer produced in the same breath as its reasoning is a worse guide to correctness than one elicited separately. The paper's candidate explanation is that effort-related activations during reasoning are read as engagement rather than difficulty, inflating confidence on the hardest questions. The authors present this as a hypothesis, not a tested result.[^c7]

## Limits

- Only 7-8B models and question answering with verifiable answers; whether linear encoding and orthogonality hold at larger scale or in open-ended generation is open.[^c8]
- The mechanism for contamination is conjectured, not isolated by intervention.
- The fix needs a second generation pass; single-pass steering is future work.[^c8]
- Orthogonality of two fitted linear readouts is shown with extra subspace analyses in an appendix, but I did not review those in detail.
- Calibration is measured at question level against empirical accuracy over 50 samples; behaviour per single response is not established.

## Related

- [[knowledge-verbalization-dissociation]] — same split (internal knowledge vs. what is said) shown for unsolvability rather than confidence
- [[verbal-confidence-commit-readiness-dissociation]] — another gap between stated confidence and a downstream signal
- [[top-skewed-confidence-floor]] — the overconfident clustering of verbal scores this work tries to correct
- [[calibration]] — the target property
- [[gated-activation-steering-for-abstention]] — activation steering used as a causal lever on a stated output

[^c1]: arxiv-2603-25052 — "the cosine similarity between the two ridge probe weight vectors remains below 0.04 across all layers."
[^c2]: arxiv-2603-25052 — "verbalized miscalibration in LLMs is a readout failure, not a knowledge deficit."
[^c3]: arxiv-2603-25052 — "a joint condition, where the model solves the problem and rates its confidence in the same generation."
[^c4]: arxiv-2603-25052 — "Joint prompts produce representations in which confidence and accuracy point in opposite directions."
[^c5]: arxiv-2603-25052 — "the more we influenced the verbalized confidence output, the more we erode the model’s accuracy performance."
[^c6]: arxiv-2603-25052 — "Adaptive steering reduces ECE by 4–7× relative to unsteered verbalized confidence."
[^c6b]: arxiv-2603-25052 — "is severely miscalibrated across all models (ECE ≥ 68)"
[^c7]: arxiv-2603-25052 — "We hypothesize that reasoning contamination reflects a conflict between two computationally distinct tasks."
[^c8]: arxiv-2603-25052 — "Our experiments use 7–8B parameter models"
