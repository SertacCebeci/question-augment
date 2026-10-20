---
description: "A four-stage pipeline that turns a single-pass video caption into a caption Gupta et al. (2026) build BodyCam-VQA for police body-worn-camera (BWC) footage,"
aliases: ["BodyCam-VQA"]
sources: ["gupta-2026"]
---
# Probe-question video captioning

> A four-stage pipeline that turns a single-pass video caption into a caption
> built from questions the system asks itself and answers by re-querying the
> video — and the measured gain from doing so.

## Mechanism

Gupta et al. (2026) build BodyCam-VQA for police body-worn-camera (BWC)[^s1]
footage, where a direct multimodal summary "frequently overlooks critical
forensic details" because the video is noisy, low-quality, and full of rapid
interaction. The pipeline runs four stages on every 60-second clip:

```text
V (video)      --VLM-->            S (initial summary)
S, V           --structured extraction--> D = {D_scene, D_entity, D_action, D_semantic}
D              --generative model G-->    Q = G(D)      (targeted investigative questions)
V, Q           --VLM, VQA pass-->         A              (one answer per question)
S, Q, A        --LLM-->                   C              (final synthesised caption)
```

The question set $Q$ is not generated from the raw video directly; it is
generated from the structured JSON record $D$, so a candidate question is
grounded in a fact the extraction stage already committed to rather than
free-floating over the whole clip.

## Why it matters

On 359 annotated 60-second COPA clips, judged by a human factual-accuracy
score (0-1) and two automatic checklist-recall scores — completeness and
visual enrichment, see [[dual-judge-completeness-recall]] — every
probe-question-then-VQA configuration beat its own direct-summarisation
baseline with the video and the final-synthesis step held fixed: Gemini's QA
pipeline reached 0.89 factual accuracy / 0.62 completeness / 0.61 visual
enrichment against its own direct-summary baseline's 0.86 / 0.51 / 0.51 — a
gain of 0.11 completeness and 0.10 visual enrichment — and DeepSeek's QA
pipeline reached 0.90 / 0.58 / 0.63 against the same 0.86 / 0.51 / 0.51
baseline — a gain of 0.07 completeness and 0.12 visual enrichment. Gupta et
al. report the aggregate gain across all four question-generator
configurations they tested — these two plus the SFT- and GRPO-trained
question generators built on Qwen3, see
[[investigative-question-grpo-training]] — as 0.04-0.13 points of
completeness and 0.03-0.09 points of visual enrichment. Gemini's and
DeepSeek's own visual-enrichment gains (0.10 and 0.12) sit above that
range's stated upper bound, so these two illustrated configurations are not
its representative bounds; the low end of the range is set by one of the
Qwen3-based question generators, not detailed here. Because only the
presence of the probe-question/VQA round varies between a pipeline and its
baseline, the source of the gain is the question-then-answer round itself,
not a stronger summariser.

## Known as

| Field | Name there | Match |
|---|---|---|
| Computer vision (Gupta et al. 2026, paper title) | BodyCam-VQA | exact — the authors' own name for the whole four-stage system this note describes |

**Not this concept.** "Probe question generation" (also in the paper's
title) names only the third stage — turning $D$ into $Q$ — in isolation. No
number in this note or its source scores that stage on its own: every
comparison of question-generator implementations is read off the whole
pipeline's final-caption metrics, so the stage-level term is not carried here
as a second alias for the whole system. [[self-ask-decomposition]] names a
structurally similar "ask yourself, then the world" loop — a model emitting
and answering a sub-question — but it is one prompt producing one
sub-question at a time inside a single forward pass, optionally routed to a
search engine, measured on 2-hop text QA; BodyCam-VQA batch-generates a whole
question set from a separately extracted structured record and answers all
of them through one VQA call, measured on 60-second video. The resemblance is
noted in `## Related`, not claimed as one object.

## Limits

- One domain (BWC forensic video), one clip length (60 seconds); the authors
  themselves flag "no evaluation of long-horizon temporal reasoning or
  maintaining coherent context across multiple linked segments."
- The gain is reported only against the same model's own direct-summary
  baseline, not against a stronger single-pass captioner tuned specifically
  for this domain; whether a better one-shot summariser would close the gap
  is not tested.
- Completeness and visual enrichment are scored by two LLM judges (Gemini,
  DeepSeek), not by human annotators — this note's numbers inherit the
  limits of [[dual-judge-completeness-recall]].
- The evaluation is, in the authors' own words, a "proof-of-concept ...
  controlled evaluation setting," with no comparison to officer-written
  reports and no deployment in an operational law-enforcement workflow.

## Related

[[self-ask-decomposition]] · [[dual-judge-completeness-recall]] · [[investigative-question-grpo-training]] · [[elicitation-protocols]] · [[compound-ai-systems]]

[^s1]: gupta-2026
