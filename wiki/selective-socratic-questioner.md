---
description: "A trained VLM module that first validates its own extracted details as sufficient or not, and only when invalid launches self-directed clarifying questions to refine them."
aliases: ["Selective Socratic Questioner", "Selective Questioning Refinement", "SQR"]
sources: ["liu-2026-gold"]
---
# Selective Socratic Questioner

> Before a vision-language model asks itself anything further, it first
> checks whether what it already extracted is good enough — only a "no"
> opens a round of self-questioning.

## Definition / Mechanism

Liu et al. (2026) train a VLM module, the Selective
[[staged-socratic-hint-policy|Socratic]] Questioner, as the second of three stages in the Gold Points
Sniper (GPS) framework for fine-grained action description. It runs in two
stages on a prior module's output (a set of candidate "Gold Points" —
extracted action-relevant details, possibly incomplete or wrong): "Since
Xgold may be incomplete or flawed, Selective Socratic Questioner … trains
the VLM to validate and selectively refine these points through a
two-stage process."[^c1]

Stage 1 is a binary validity check: the VLM scores whether the extracted
points already suffice to describe the subject's action, intent and
context. Only when that check fails does Stage 2 fire: "When Xgold are
deemed invalid (y "0), Selective Socratic Questioner initiates a
refinement process featuring self-questioning (Socratic Questioning).
Specifically, a VLM Q, acting as a socratic questioner, queries itself
about omissions or inaccuracies within Xgold in order to direct its
attention to relevant visual regions." The self-questioning produces Q&A
pairs, not a free-form second pass. When the check passes, the model
skips straight to generating its final description.[^c2]

An ablation on two finetuned VLMs (LLaVA-NeXT-8B, LLaVA-OV-7B) isolates
this stage's contribution by removing it from inference while keeping the
other two GPS stages: on the whole benchmark this drops the Semantic
Entailment Score by only 0.41 and 1.11 percentage points respectively,
against 5.07/6.93 (extraction) and 6.16/6.71 (validation) point drops for
the other two stages — "Gold Points Extraction (GPE) and Gold Points
Validation (GPV) serve as foundational components, with their removal
causing the most substantial performance drops … The smaller performance
drop from SQR removal indicates its primary role is improving output
quality rather than establishing correctness."[^c3]

## Why it matters

This is a gate on whether to ask at all, decided by a self-assessment of
[[sufficient-statistic|sufficiency]] rather than by a fixed schedule or a confidence threshold
swept on held-out data: the module measures its own prior answer's
coverage before spending a further question on it, and the further
questions it does ask are themselves generated, not selected from a
candidate set. The ablation shows this gating pays off mainly in output
quality (informational richness), not in factual correctness — correctness
is bought upstream by extraction and validation.

## Limits

- The validity gate is a binary classifier trained on one dataset and
  domain: "the instruction-tuning dataset consists of 14,281 video frames
  from 80 action categories" of fine-grained human action from video
  frames; nothing in the paper shows the gate generalizes to a domain
  where "sufficient" is not settled by an entailment-style ground-truth
  comparison at training time.[^c4]
- The reported 0.41–1.11 point ablation drops are measured on finetuned
  models only; the same paper reports that this multi-stage reasoning
  degrades performance for a model that has not been finetuned on it —
  "+ Prompting caused performance degradation for nearly all lightweight
  VLMs" — so the small measured contribution of this stage is conditional
  on the other two stages already being present and trained.[^c5]

## Related

[[chain-of-self-questioning]] · [[self-questioning-vlm-grpo]] · Selection

[^c1]: liu-2026-gold — "Since Xgold may be incomplete or flawed, Selective Socratic Questioner (Fig. 2 (b)) trains the VLM to validate and selectively refine these points through a two-stage process."
[^c2]: liu-2026-gold
[^c3]: liu-2026-gold — "Gold Points Extraction (GPE) and Gold Points Validation (GPV) serve as foundational components, with their removal causing the most substantial performance drops, demonstrating that the reasoning chain depends critically on accurately extracting and verifying core factual information."
[^c4]: liu-2026-gold — "the instruction-tuning dataset consists of 14,281 video frames from 80 action categories"
[^c5]: liu-2026-gold — "+ Prompting caused performance degradation for nearly all lightweight VLMs, with only minor improvement in LLaVA-OV-7B."
