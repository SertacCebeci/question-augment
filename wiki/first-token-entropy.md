---
description: "Shannon entropy of the full-vocabulary next-token distribution at the last prompt position is a one-pass readout that shifts across prompting regimes but predicts item outcomes weakly."
aliases: ["intention entropy", "pre-collapse next-token entropy", "H_int"]
sources: ["arxiv-2601-01011"]
---
# First-token entropy

Intention entropy, written H_int(I) in the paper, is the Shannon entropy in bits of the model's next-token distribution at the moment the first output token is about to be chosen. It sums −p log p over the whole vocabulary, with p the model's probability for each token given the prompt.[^c1] It is computed from the logits at the last prompt position, using log-sum-exp for numerical stability.[^c2] A lower value means a more concentrated continuation at the moment of commitment.[^c3]

As a readout it is cheap. It needs one forward pass and no sampling, no clustering and no change to the architecture. The paper sets it against semantic entropy, which needs several outputs: "single-pass entropy at a specific pre-collapse moment, semantic entropy requires" multiple samples and a clustering step. The author says "Hint (I) is cheap and isolates a local commitment distribution", while the sampled measure captures diversity of outputs at higher compute.[^c4][^c5]

What it measures is set by the author's own scope. It is an unconstrained entropy over the full vocabulary, so it reads "local generative dispersion" at the boundary, and it is not "a calibrated measure of uncertainty over task-specific answer choices".[^c6] A decision-aligned version would restrict the distribution to option letters and report option-normalised entropy and the margin between the top options. The paper could not report those, because its "current checkpoint format stores aggregated entropy values but not per-option" log-probabilities.[^c7]

Measured. Across the 3 × 3 matrix the entropy works best as a regime signature. The paper's contrast ΔH = H(CoT) − H(baseline) has a different sign by family: "Mistral operates under lower" pre-collapse entropy under chain-of-thought, while LLaMA runs higher.[^c8] The paper reads these labels as comparative: "these regimes describe comparative uncertainty under CoT vs. baseline and do" not imply anything about token-level dynamics.[^c9] The same entropy is, in the author's words, a "regime- and model-family signature" rather than "a uniformly strong item-level predictor".[^c10]

Sensitivity. The readout is taken at the very end of the prompt, and the paper notes that "it is sensitive to prompt phrasing", including "boilerplate CoT preambles".[^c11][^c12] My inference: a change in the closing words of an instruction moves the first-token distribution whatever the problem is. A difference between two prompting regimes is therefore a mixture of what the model is preparing to say and how the instruction was worded, and the paper's own caution points the same way.

## Limits

- The predictive power at item level is weak: "is weak in several settings", and the paper reports cases where the entropy shift changes without any change in correctness.[^c13]
- No decision-aligned variant was reported in this revision, so the entropy cannot yet be compared with the option margins that multiple-choice decisions depend on.[^c7]
- The results cover three 7–8B instruct models, with the caveats on quantization and scale given in [[pre-collapse-intention-state]]. What the entropy does on base checkpoints or larger models is not measured.
- The sign of ΔH flips between families, so a single CoT effect on entropy cannot be assumed in advance. Whether a given model belongs to the lower or higher regime is an empirical question that the paper answers only for its three checkpoints.

## Related

- [[pre-collapse-intention-state]] — the position at which this entropy is read
- [[semantic-entropy]] — the multi-sample, output-side uncertainty measure the paper contrasts with this one
- [[pre-generation-success-probe]] — a probe on the same pre-generation state, scored against success rather than dispersion

[^c1]: arxiv-2601-01011 — "of the next-token distribution at the pre-collapse moment"
[^c2]: arxiv-2601-01011 — "We compute Hint (I) from the logits at the last prompt position"
[^c3]: arxiv-2601-01011 — "Lower entropy corresponds to a more concentrated"
[^c4]: arxiv-2601-01011 — "single-pass entropy at a specific pre-collapse moment, semantic entropy requires"
[^c5]: arxiv-2601-01011 — "Hint (I) is cheap and isolates a local commitment distribution"
[^c6]: arxiv-2601-01011 — "calibrated measure of uncertainty over task-specific answer choices"
[^c7]: arxiv-2601-01011 — "current checkpoint format stores aggregated entropy values but not per-option"
[^c8]: arxiv-2601-01011 — "Mistral operates under lower"
[^c9]: arxiv-2601-01011 — "these regimes describe comparative uncertainty under CoT vs. baseline and do"
[^c10]: arxiv-2601-01011 — "Hint (I) primarily behaves as a regime- and model-family signature"
[^c11]: arxiv-2601-01011 — "it is sensitive to prompt phrasing"
[^c12]: arxiv-2601-01011 — "including boilerplate CoT preambles"
[^c13]: arxiv-2601-01011 — "is weak in several settings"
