---
description: "Across audio-aware LLMs, semantic/verification uncertainty methods beat token-level ones consistently on general reasoning benchmarks but not on hallucination/unanswerable ones."
aliases: []
sources: ["arxiv-2604-25591"]
---
# Audio-LLM trustworthiness-uncertainty instability

> The uncertainty method that reliably flags a wrong answer on a general
> audio-reasoning benchmark is not the one that reliably flags a
> hallucinated or unanswerable one.

## Definition / Mechanism

Kuan, Huang & Lee (2026) run the first systematic
comparison of uncertainty estimation methods — predictive entropy,
length-normalized entropy, semantic entropy, discrete semantic entropy,
and P(True) — for audio-aware LLMs (Qwen2.5-Omni-3B/7B, Audio Flamingo 3),
scored by AUROC (error/correct separation) and AURAC (accuracy after
rejecting the most uncertain examples) on two kinds of benchmark: general
audio understanding/reasoning (MMAU, MMAR, MMSU, SAKURA) and
trustworthiness-oriented tasks (Audio-Hallucination, AQUA-Bench
unanswerable-question QA). On the general benchmarks the ranking is
stable: "semantic-based and verification-based methods, including discrete
semantic entropy, semantic entropy, and P(True), generally outperform
token-level baselines such as predictive entropy and normalized entropy.
This trend is especially consistent on general audio understanding and
reasoning benchmarks."[^c1]

On the trustworthiness-oriented benchmarks the same methods no longer have
a fixed order: "on AQUA, P(True) performs best for Qwen2.5-Omni-7B,
whereas normalized entropy performs best for Qwen2.5-Omni-3B, and P(True)
shows particularly strong AUROC for Audio Flamingo 3. These results
suggest that uncertainty estimation in trustworthiness-oriented settings
is more model-dependent and benchmark-dependent." The
Audio-Hallucination benchmark repeats the pattern one level down: semantic
and discrete semantic entropy win for both Qwen models, but "for Audio
Flamingo 3, normalized entropy achieves the best AUROC, while predictive
entropy is also competitive," so even within one benchmark the winning
method flips with the model. The paper's own summary of the contrast:
"the trustworthiness-oriented benchmarks reveal a more heterogeneous
picture than the general understanding and reasoning benchmarks. Rather
than showing a single consistently dominant method, they highlight
stronger benchmark- and model-dependent variation in the usefulness of
uncertainty estimates... conclusions drawn from general reasoning
benchmarks do not always transfer directly to hallucination and
unanswerable-question settings."[^c4]

## Why it matters

This narrows where a fixed uncertainty-to-commitment mapping is safe to
reuse. A threshold or ranking tuned on a general-reasoning benchmark —
where semantic-level and self-verification signals dominate token-level
ones with some consistency — cannot be assumed to carry over to the
setting an abstention gate actually needs it for: telling a hallucinated
or unanswerable case from a supported one. The instability tracks the
benchmark category (general vs. trustworthiness-oriented) and the model
together, not either alone, which is a finer split than [[calibration]]
failures usually get diagnosed at, and the first report of it for
audio-conditioned generation rather than text.

## Limits

Three models, two trustworthiness-oriented benchmarks (one hallucination,
one unanswerable-QA), K=10 samples per input; whether the same
general/trustworthiness split holds for other audio tasks, larger models,
or other modalities is not established here — treat the model- and
benchmark-dependence as the finding, not the specific per-model rankings
reported. The paper does not explain why self-verification and semantic
clustering lose their edge on trustworthiness tasks, only that they do.

## Related

[[uncertainty-hallucination-relevance-gap]] · [[ue-method-scale-dependence]] · [[calibration]] · [[semantic-entropy]] · [[abstention]]

[^c1]: arxiv-2604-25591 — "semantic-based and verification-based methods, including discrete semantic entropy, semantic entropy, and P(True), generally outperform token-level baselines such as predictive entropy and normalized entropy. This trend is especially consistent on general audio understanding and reasoning benchmarks"
[^c4]: arxiv-2604-25591 — "the trustworthiness-oriented benchmarks reveal a more heterogeneous picture than the general understanding and reasoning benchmarks. Rather than showing a single consistently dominant method, they highlight stronger benchmark- and model-dependent variation in the usefulness of uncertainty estimates"
