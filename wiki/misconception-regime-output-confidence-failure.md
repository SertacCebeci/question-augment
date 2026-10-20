---
description: "Output-based confidence (P(True), entropy, semantic entropy) fails on adversarial misconceptions, where internal correctness probes still work; on standard QA the two tie."
aliases: ["regime-specific internal advantage", "centroid sufficiency", "confidently wrong misconception regime"]
sources: ["arxiv-2602-08159"]
---
# Misconception regime: output confidence fails, internal correctness survives

Output-distribution signals encode what the model believes, not whether the belief is right. Where the model confidently asserts the wrong answer, such signals carry no information about correctness, yet a residual-stream probe can still separate true from false statements.[^c1] On TruthfulQA, output methods (P(True), token entropy, semantic entropy) score 0.44-0.64 AUC while probes reach 0.80-0.94.[^c2] On standard QA (SciQ, CSQA, FEVER) on Qwen2-7B, P(True) reaches 0.93-0.95, comparable to centroid distance at 0.91-0.97; only TruthfulQA gives a large gap (P(True) 0.48 vs centroid 0.93).[^c3] The authors' own summary: "The claim we carry forward is therefore centroid sufficiency, not internal superiority."[^c4]

## The detector is simple

Distance to two class centroids in a supervised 2-8 dimensional subspace matches a trained linear probe within about 0.02 AUC; per-class distributions are unimodal, so a single mean shift is the decision rule.[^c5] Twenty-five labeled examples recover 90% of full-data AUC on GPT-2.[^c6] The unsupervised probe CCS also breaks in this regime (0.54-0.85 against 0.80-0.94 for supervised).[^c7]

## For asking and answering

My inference: a questioner who uses an answerer's fluency or self-reported confidence as a correctness check is safe on ordinary factual items and blind on misconception-laden ones, which is the regime where checking matters most.

## Limits

Everything is teacher-forced, with labeled contrastive pairs at a single token position; the authors say this is unavailable in deployment. White-box access and labels are required. The regime split is shown mainly on one adversarial dataset (TruthfulQA). Causal tests (steering, erasure) are in-distribution.

## Related

- [[pre-generation-success-probe]] — another supervised activation probe for success, with its own limits.
- [[accuracy-masks-selective-reliability]] — aggregate scores hiding regime-specific failure.
- [[correct-answer-trap]] — fluent, confident answers that are wrong.
- [[adaptive-conformal-semantic-entropy]] — the output-uncertainty method this regime defeats.

[^c1]: arxiv-2602-08159 — "the model confidently asserts the wrong answer, so"
[^c2]: arxiv-2602-08159 — "output methods (P(True), token entropy,"
[^c3]: arxiv-2602-08159 — "only TruthfulQA produces a large separation"
[^c4]: arxiv-2602-08159 — "The claim we carry forward is therefore centroid sufficiency,"
[^c5]: arxiv-2602-08159 — "the per-class"
[^c6]: arxiv-2602-08159 — "25 labeled examples recover 90% of full-data AUC on GPT-2."
[^c7]: arxiv-2602-08159 — "reaches 0.54–0.85 against 0.80–0.94 for supervised probes."
