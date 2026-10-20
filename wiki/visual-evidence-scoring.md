---
description: "Decomposes a VQA selector's confidence into correctness, localization and coherence sub-scores from observable outputs alone, generalizing across reasoners without logits."
aliases: ["SIEVES", "Selective Prediction through Visual Evidence Scoring", "visual evidence scoring"]
sources: ["arxiv-2604-25855"]
---
# Visual evidence scoring

> A confidence score that only guesses whether an answer is right cannot
> say why; a confidence score trained to also grade the answerer's cited
> evidence can, and that is what lets it survive a change of answerer.

## Definition / Mechanism

SIEVES (Rodriguez & Rohrbach (2026)) targets
[[abstention|selective prediction]] for visual question answering: a
reasoner with a zoom-in tool produces multimodal chain-of-thought
(crops it looked at) alongside its answer, and a separate selector model
is trained to grade that answer for release rather than to predict
correctness alone. Instead of one scalar, "the selector predicts three
signals: correctness (is the final answer accurate?), localization (did
the model look at the right part of the image?), and coherence (does the
visual evidence support the answer?)."[^c1][^c2]

Formally the selector maps the full conversation to three scalars in
[0,1]: "outputs three confidence values: ccorr that the answer is
correct, cloc that the relevant visual information was localized, and
ccoh that the final answer is coherent with the evidence."
[^c3]

The localization target is built by matching the reasoner's predicted
crops against ground-truth bounding boxes — "the model's predicted crops
are matched to the ground-truth bounding boxes" — discretized into a
binary label at an intersection-over-ground-truth threshold.
[^c7]

The coherence target asks whether the answer is actually supported by
the localized crop, not merely whether the crop was in the right place;
it is labeled automatically by an external VLM judge rather than by
hand, and checked against people: "we run a small human evaluation on
200 randomly chosen training samples and find that human annotations
match the same gcoh label in 92% of cases."
[^c4]

The three per-objective binary cross-entropy losses are summed with
fixed weights to train the selector, and the same weighted sum combines
the three predicted scores at inference into one release/abstain
confidence. Ablating which objectives are kept shows the decomposition
itself is load-bearing: "Including all objectives is better than
excluding any, and the framework is robust to changes in the weights."
[^c6]

Because every input to the selector — question, image, chain-of-thought,
answer — is something a reasoner emits regardless of whether its
internals are exposed, the selector needs no logits or hidden states from
the reasoner it grades. Trained only on a small open-weight reasoner's
traces, it transfers to reasoners it never saw during training: "the
design of the SIEVES selector enables transfer to proprietary reasoners
without access to their weights or logits, such as o3 and Gemini-3-Pro,
providing coverage boosts beyond those attributable to accuracy alone."
[^c5]

On the tested out-of-distribution VQA benchmarks this decomposition
raises coverage at fixed risk substantially over a selector that only
predicts correctness: "SIEVES ... improves coverage by up to three times
on challenging OOD benchmarks ... compared to non-grounding baselines."
[^c1]

## Why it matters

Most selective-prediction machinery (logit margins, hidden-state probes,
verbalized confidence) needs the answerer's internals or collapses the
justification for an answer into one number, which generalizes poorly
once the domain or the answerer changes. Visual evidence scoring instead
grades the *evidence the answerer already produced* — where it looked,
whether that support matches the answer — using only what any answerer,
closed or open, exposes in its output. It turns the reject-option
decision from "does this look like the training distribution's correct
answers" into "is the cited evidence adequate," a criterion a
practitioner building a task-agnostic answerer could carry over: score
the warrant for a claim, not only the claim.

## Limits

- Localization labels require ground-truth bounding boxes at training
  time — obtained automatically via a grounding VLM pipeline here — so
  the method needs a domain where the "evidence" is spatially
  well-defined and independently verifiable; it does not obviously
  transfer to domains where evidence is textual or diffuse. [?]
- Coherence labels are themselves machine-judged (92% human agreement),
  so roughly one in twelve training and evaluation coherence targets is
  itself noisy or wrong, a ceiling the paper reports but does not remove.
- Evaluated only on VQA with a zoom-in-capable reasoner; whether
  "evidence-quality scoring" generalizes to non-visual modalities (e.g.
  retrieved passages, tool-call traces) as a selector signal is not
  tested here. [?]

## Related

- [[abstention]]
- [[coverage-gated-abstention-rate]]
- [[shapley-uncertainty-localization]]

[^c1]: arxiv-2604-25855 — "SIEVES (Selective Prediction through Visual Evidence Scoring) improves coverage by up to three times on challenging OOD benchmarks (V* Bench, HR-Bench-8k, MME-RealWorld-Lite, VizWiz, and AdVQA), compared to non-grounding baselines."
[^c2]: arxiv-2604-25855 — "the selector predicts three signals: correctness (is the final answer accurate?), localization (did the model look at the right part of the image?), and coherence (does the visual evidence support the answer?)."
[^c3]: arxiv-2604-25855 — "outputs three confidence values: ccorr that the answer is correct, cloc that the relevant visual information was localized, and ccoh that the final answer is coherent with the evidence."
[^c4]: arxiv-2604-25855 — "we run a small human evaluation on 200 randomly chosen training samples and find that human annotations match the same gcoh label in 92% of cases."
[^c5]: arxiv-2604-25855 — "the design of the SIEVES selector enables transfer to proprietary reasoners without access to their weights or logits, such as o3 and Gemini-3-Pro, providing coverage boosts beyond those attributable to accuracy alone."
[^c6]: arxiv-2604-25855 — "Including all objectives is better than excluding any, and the framework is robust to changes in the weights."
[^c7]: arxiv-2604-25855
