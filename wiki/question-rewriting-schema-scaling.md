---
description: "Ablating a question-clarifying rewrite step in a Text-to-SQL pipeline costs accuracy everywhere, most where the schema and knowledge it compresses are largest and noisiest."
aliases: []
sources: ["arxiv-2604-07041"]
---
# Question rewriting scales with schema complexity

> A clarifying rewrite of the question is nearly free, helps in every
> setting tested, and helps most exactly where the raw question is
> hardest to act on — a large, noisy schema and knowledge document.

## Definition / Mechanism

AV-SQL (2026) puts one agent, $LLM_{Rewriter}$, before
a multi-stage Text-to-SQL pipeline: "This stage employs a single agent,
𝐿𝐿𝑀𝑅𝑒𝑤𝑟𝑖𝑡𝑒𝑟 , to reformulate the user request into a clearer and more
explicit form for downstream agents (e.g., the view generator, planner,
and SQL generator). It takes as input the original natural-language
question Q and optional external knowledge K, and produces a rewritten
question Qrewrite that explicitly states the user intent, key
constraints, and necessary domain assumptions."[^c1]

The rewrite is bound to a form constraint, not left free: "Formally, the
overall rewriting objective is:

Qrewrite = 𝐿𝐿𝑀𝑅𝑒𝑤𝑟𝑖𝑡𝑒𝑟 Q, K | Q ,
(4)
s.t.

Intent(Qrewrite ) = Intent(Q, K)," — the surface form changes (structure,
length, explicitness) but the expressed intent must not.[^c2]

The paper's own reason to expect the effect to scale with input size:
"K frequently consists of lengthy documents filled with noisy or
question-irrelevant details. Providing the full K directly to downstream
LLM agents increases prompt length and can distract the model, degrading
Text-to-SQL reliability."[^c3]

An ablation (ablate-one-component, all else held fixed) removes the
rewriter and measures execution accuracy (EX) against the full pipeline,
across four benchmarks and backbones:

| benchmark (backbone) | w/o rewriter | full pipeline | gap |
|---|---|---|---|
| Spider2-Snow (GPT-5-mini) | 57.22 | 65.08 | 7.86 |
| Spider2-Snow (Gemini-3-Pro) | 64.90 | 70.38 | 5.48 |
| Spider (Llama-3.3) | 78.34 | 83.66 | 5.32 |
| Spider (Gemini-3-Pro) | 84.53 | 85.59 | 1.06 |
| BIRD (Llama-3.3) | 65.45 | 68.19 | 2.74 |
| BIRD (Gemini-3-Pro) | 71.64 | 72.16 | 0.52 |
| KaggleDBQA (Llama-3.3) | 48.65 | 53.51 | 4.86 |
| KaggleDBQA (Gemini-3-Pro) | 62.16 | 63.78 | 1.62 |

The gap is positive in all eight cells and is largest on Spider2-Snow —
the benchmark whose schemas and external-knowledge documents the paper
itself describes as the largest and noisiest (^c3) — and smallest on
Spider and BIRD, whose external knowledge is "typically brief (often
just 1–2 sentences)."

The intervention is cheap: "the rewriter is the lightest stage at 1.83%
of tokens and 3.9% of runtime" of the whole pipeline (measured with
Gemini-3-Pro on Spider2.0-snow).[^c5]

## Why it matters

This is a measured, not asserted, effect of a question's *form* on what
a downstream system can do with it: the same question content, passed
either raw-plus-context or pre-compressed into an explicit
task/outputs/filters/sort structure, produces different execution
accuracy from the same downstream agents. For a practitioner assembling
any agentic pipeline that must decompose a long, heterogeneous context
(not only SQL schemas), the actionable result is not just "add a
rewriting step" — most pipelines already do — but that the step's payoff
is not uniform: it is worth budgeting for specifically when the input the
question must be read against is large and noisy, and is close to free
when it is small and clean. A fixed per-pipeline rewriting budget sized
for the easy case would under-invest exactly where it matters.

## Limits

- The ablation removes the rewriter entirely; it does not vary rewriting
  *quality* (a worse or better rewriter), so the note's "scales with
  complexity" reading is this note's generalization from the pattern
  across eight cells, not a claim the paper makes about a controlled
  sweep over schema size — it is drawn from four benchmarks that differ
  in schema size and knowledge length simultaneously with which backbone
  was tested on them (Spider2-Snow uses GPT-5-mini/Gemini-3-Pro; Spider,
  BIRD and KaggleDBQA use Llama-3.3/Gemini-3-Pro), so backbone and
  benchmark are confounded in the table above.
- The rewriter's output is graded only by its downstream effect on EX,
  never scored directly for how well it preserves intent (the
  $Intent(Q_{rewrite})=Intent(Q,K)$ constraint,[^c2], is stated as a
  design goal, not measured).

## Related

[[reformulation-pattern-library]] · [[format-restriction-effect]] · [[text-to-sql-ambiguity-taxonomy]] · [[black-box-correctness-ceiling]] · [[rewriting-repairability-ceiling]]

[^c1]: arxiv-2604-07041 — "This stage employs a single agent, 𝐿𝐿𝑀𝑅𝑒𝑤𝑟𝑖𝑡𝑒𝑟 , to reformulate the user request into a clearer and more explicit form for downstream agents (e.g., the view generator, planner, and SQL generator). It takes as input the original natural-language question Q and optional external knowledge K, and produces a rewritten question Qrewrite that explicitly states the user intent, key constraints, and necessary domain assumptions."
[^c2]: arxiv-2604-07041
[^c3]: arxiv-2604-07041 — "K frequently consists of lengthy documents filled with noisy or question-irrelevant details. Providing the full K directly to downstream LLM agents increases prompt length and can distract the model, degrading Text-to-SQL reliability."
[^c5]: arxiv-2604-07041 — "tokens and 7.8% of runtime, while the rewriter is the lightest stage at 1.83% of tokens and 3.9% of runtime."
