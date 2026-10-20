---
description: "Omni-modal models abstain too often when one clean modality suffices and too rarely when all three are corrupted, staying confident; chain-of-thought aids answering but worsens confidence."
aliases: ["calibrated abstention under cross-modal conflict", "omni-modal over- and under-abstention"]
sources: ["arxiv-2603-27187"]
---
# Dissonance-graded abstention miscalibration

OMD-Bench starts from trimodal items (video, audio, text) whose modalities all present the same anchor, then corrupts k = 0..3 of them. Human annotators decide per instance whether the remaining evidence suffices or abstention is right. That gives a graded test of whether a model's refusal tracks the evidence left, not just whether it refuses.

**Two-sided error.** Abstention rises monotonically with k for every model and setting, so models notice conflict. But the sensitivity is miscalibrated both ways: models abstain too often when evidence is sufficient (k<=2, where humans almost never abstain) and too rarely at k=3.[^c1] At k=3 humans abstain on about 98% of instances and no model exceeds 82%.[^c2] At k=2 the answer is almost always recoverable from the one clean modality, so abstaining there is an error of caution, not prudence.[^c3] Two models (VideoLLaMA2, Phi-4) almost never abstain even under full corruption.[^c4]

**Confidence does not follow.** At k=2 mean accuracy falls to about 61% while every model's mean confidence stays at or above 78%.[^c5] The extreme case is Gemini 2.5, whose confidence moves from 99.7% to 98.5% as accuracy falls from 96.5% to 70.5%.[^c6]

**Chain-of-thought trade-off.** CoT improved abstention alignment for eight of ten models, mostly by helping models answer at k=2 instead of over-abstaining.[^c7] But it can hurt abstention where it is needed: Gemini 2.0 rose from 90% to 96% at k=0 while its k=3 abstention fell from 81% to 51%.[^c8] Under CoT six of eight models with token-level data show confidence saturated near 100% at every corruption level, erasing the gradient visible zero-shot.[^c9] My reading, not the paper's test: extended reasoning commits the model to an answer, so it raises answering and lowers refusal together. The authors suggest the same.

## Limits

- Corruption is synthetic and targeted at one anchor per item; the authors report real-split results within 2 pp of synthetic, but natural conflict may differ.
- Humans' near-universal abstention at k=3 is the reference; this is a judgment protocol, not a ground-truth risk cost, so the optimal abstention rate under different error costs is untested.
- Only ten models and two prompt styles; CoT effects are mixed by model (VideoLLaMA2, Uni-MoE-2 degrade slightly).
- The mechanism for CoT overconfidence is inferred, not isolated.

## Related

- [[calibration]] — the general notion of confidence matching accuracy that fails here
- [[conflict-aware-abstention-score]] — a score for abstaining under conflicting evidence
- [[post-hoc-abstention]] — abstention decided after generation, the regime these models are tested in
- [[detection-to-abstention-gap]] — noticing a problem without acting on it, as here

[^c1]: arxiv-2603-27187 — "too rarely when evidence is genuinely conflicting"
[^c2]: arxiv-2603-27187 — "(k=3, where humans abstain on ≈98% of instances"
[^c3]: arxiv-2603-27187 — "almost always recoverable from the single remaining clean modality, CoT helps models correctly"
[^c4]: arxiv-2603-27187 — "they almost never abstain,"
[^c5]: arxiv-2603-27187 — "confidence stays at or above 78% for every model."
[^c6]: arxiv-2603-27187 — "barely moves from 99.7% to 98.5% as accuracy"
[^c7]: arxiv-2603-27187 — "CoT improves abstention calibration for"
[^c8]: arxiv-2603-27187 — "yet drops k=3 abstention from 81%"
[^c9]: arxiv-2603-27187 — "at or near 100% across all corruption levels under CoT"
