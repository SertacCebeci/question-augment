---
description: "An IDE-embedded multi-agent tutor scores a prompt on eight dimensions and asks Socratic questions on the weakest; developers' prompt quality rose 13.7% (p<.001) after one 60-min session, tool revoked."
aliases: ["Prompt Coach", "PC"]
sources: ["mehra-2026"]
---
# Prompt Coach

> A dimensional prompt-quality evaluator picks which weakness to question,
> a hidden simulation of the target LLM's output grounds the question in a
> concrete failure, and one 60-minute session moved developers' prompt
> quality on exactly the dimensions the evaluator had scored low.

## Definition / Mechanism

Mehra, Singi, Kaulgud et al. (2026) build Prompt Coach (PC), a
multi-agent IDE extension for teaching code-generation prompt engineering.
A Prompt Evaluator Agent scores each submitted prompt on eight
independently defined dimensions (clarity, specificity, context awareness,
adaptability, inclusion of constraints, error handling, output
requirements, testability), each 0–100 with a rationale from an
LLM-as-judge. A [[staged-socratic-hint-policy|Socratic]] Guidance Agent then turns the low-scoring
dimensions into targeted questions rather than direct fixes, grounded in
two sources: the developer's own codebase (via a retrieval store) and a
Consequence Preview Agent that silently invokes the same class of LLM the
developer is targeting to generate the code the current prompt would
produce — that preview is never shown to the developer, only mined for
concrete failure modes the question can reference (e.g., asking what the
function should do on empty input after the preview shows it would fail).[^c1]

## Why it matters

In a within-subjects study, 15 professional developers (mean 9.6 years'
experience) wrote baseline prompts for three APPS-benchmark tasks, used PC
for 60 minutes on those same prompts, then wrote prompts for three new
tasks with PC access revoked. Overall prompt-quality score rose from 63.04
to 71.69 (+13.73%, paired Wilcoxon p<.001) on prompts written without the
tool present.[^c2]

The gain was not uniform across dimensions: it concentrated on the ones the
evaluator had scored lowest at baseline and that developers habitually
neglect — Inclusion of Constraints (+31.63%, p<.001) and Error Handling
(+30.66%, p<.001) — while Clarity, already the highest-scoring dimension at
baseline (79.87), showed no significant change (−0.19%, p=0.577).[^c3]

Because the post-learning prompts were written with PC's live scaffold
removed, the measured effect is a within-session skill change that
persisted at least ten minutes without the tool present, not just a
same-session score with the tool answering the question for the developer.[^c4]

## Transfer

| | |
|---|---|
| **Home field** | The Socratic method's constructive, education-style variant (guided discovery ending in a revised belief, not aporia) — the sense [[socratic-method]] itself flags as a *different* object from the philosophical elenchus. |
| **Here** | A rubric (eight named dimensions) selects *which* weakness to question, and a hidden LLM simulation of the prompt's own consequences supplies the concrete failure the question references. |
| **What survives** | Guided discovery through targeted questioning rather than direct correction still produced a measured, dimension-specific skill gain outside the tool. |
| **What does not** | Nothing about elenctic refutation or aporia — PC never argues the developer into a contradiction; it scores and asks. The paper does not isolate the rubric's or the preview's individual contribution from an ablation, so which piece of the transfer is doing the work is unmeasured. |

## Limits

- n=15, single organisation's delivery centres, single-arm pre/post design
  with no control tutor and no comparison to an alternative learning
  method; the authors themselves note this is an early study intended to
  precede a comparative evaluation.
- Post-learning testing happened immediately (same ~2.5-hour session, PC
  access revoked for roughly ten minutes of prompt-writing per task); no
  measurement of retention over days or weeks, and no test of prompting on
  tasks outside the APPS benchmark's three complexity bands.
- All quality scoring — both dimension scores and the "ground truth" the
  gain is measured against — is itself an LLM-as-judge (GPT-4.1), not an
  independent human rater; a systematic bias in the judge would inflate or
  deflate every number reported above together.
- The Consequence Preview Agent's contribution is architectural, not
  isolated experimentally: no ablation compares PC with and without the
  preview, so the claim that grounding in a simulated failure mode helps
  is this note's reading of the design rationale, not a measured effect on
  its own.

## Related

[[socratic-method]] · [[gated-socratic-scaffolding]] · [[socratic-guidance-transfer-effect]] · [[staged-socratic-hint-policy]]

[^c1]: mehra-2026 — "Rather than applying a monolithic notion of prompt quality, the evaluator scores the prompt across a set of explicitly defined dimensions configured in a Dimension Registry. Each dimension receives a score between 0-100, along with a brief rationale, using an LLMas-a-judge evaluation."
[^c2]: mehra-2026 — "Overall 63.04 71.69 + 13.73 % <.001"
[^c3]: mehra-2026
[^c4]: mehra-2026 — "Post-Learning Phase: Participants wrote code-generation prompts for three additional APPS tasks at the same complexity levels (10 minutes per task), with access to PC revoked during this phase. The tasks were distinct from those in the baselining phase to prevent memorization effects."
