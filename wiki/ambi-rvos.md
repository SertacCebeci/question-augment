---
description: "A referring video object segmentation benchmark that scores a before/after accuracy gain from adding multi-turn intent clarification, not a bare ask-rate."
aliases: ["Ambi-RVOS"]
sources: ["yang-2026-guess"]
---
# Ambi-RVOS

> A referring-segmentation benchmark that measures what a clarification
> loop buys in final task accuracy, not whether a model recognises
> [[efe-planning-as-variational-inference|ambiguity]] or how often it asks.

## Mechanism

Yang et al. (2026) build Ambi-RVOS by curating videos
from ReVOS and MeViS "focusing on scenes with a high density of visually
similar objects," then constructing ambiguous queries two ways: keeping a
source query that already matches multiple objects, or progressively
stripping attributes from a unique query until it matches more than one
candidate. The benchmark "consists of 1500 curated test samples," split by
initial candidate count into Simple (400 samples, exactly two candidates),
Medium (600 samples, three to five) and Difficult (500 samples, six or
more).[^c1]

Unlike a benchmark that scores a model's ambiguity-detection label or its
raw ask-rate, Ambi-RVOS scores final segmentation accuracy (region
similarity $\mathcal{J}$ and contour accuracy $\mathcal{F}$, reported as
$\mathcal{J}\&\mathcal{F}$) for methods that never ask against
[[hi-grpo|IC-Seg]], which resolves ambiguity through multi-turn dialogue
before segmenting: "IC-Seg not only outperforms existing methods by a
large margin in resolving ambiguous queries... yielding nearly 20%
improvements in overall J&F," while it also "maintains state-of-the-art
(SOTA) performance on existing image and video reasoning segmentation
benchmarks."[^c2]

## Why it matters

This is one of the few benchmarks on this stall that measures a
clarification mechanism's downstream *payoff* rather than a model's
willingness to ask: it compares specialist RVOS models and MLLM-based
reasoning-segmentation baselines, none of which clarify, against the same
family of models equipped with a trained ask loop, on the same task and
the same metric.

## Limits

- The 1,500 samples are attribute-stripped or pre-selected from two
  existing datasets, not naturally occurring ambiguous requests; the
  Simple/Medium/Difficult split is defined by the number of visually
  similar objects the curators placed in the scene, not an independent
  severity judgement.
- The benchmark's "user" is a second MLLM (Qwen3-VL-Instruct-32B) answering
  from the ground-truth target, not a human respondent, so the reported
  gain describes performance against a simulated, always-truthful answerer.
- The ~20% J&F improvement is read from the paper's abstract; the
  per-tier numeric results table in the extract read for this note was not
  legible enough to cite a specific per-method, per-tier cell.

## Related

[[hi-grpo]] · [[clarification-benchmarks]] · [[preference-optimization-for-questions]]

[^c1]: yang-2026-guess — "The Ambi-RVOS benchmark consists of 1500 curated test samples, each comprising a video sequence and an ambiguous query."
[^c2]: yang-2026-guess — "Extensive experiments demonstrate that IC-Seg not only outperforms existing methods by a large margin in resolving ambiguous queries, but also maintains state-of-the-art performance on standard reasoning segmentation benchmarks."
