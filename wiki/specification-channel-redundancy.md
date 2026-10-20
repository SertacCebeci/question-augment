---
description: "Robustness to prompt under-specification is set by how many independent, overlapping channels a task description carries — description, constraints, examples, I/O format — not by model size."
aliases: ["specification richness effect", "multi-channel prompt redundancy", "structural robustness to under-specification"]
sources: ["arxiv-2604-24712"]
---
# Specification-channel redundancy

> Sensitivity to prompt wording is an artifact of specification structure,
> not of the model reading it.

## Definition / Mechanism

A task description can carry its content through one channel or several:
HumanEval states a task through a single short docstring (231 characters on
average, no separate constraints, no sample I/O, no input-format section);
LiveCodeBench states the same kind of task through four overlapping
channels — prose description, an explicit constraints section, multiple
worked input/output examples, and an I/O-format specification. Akli, Papadakis, Cordy & Le Traon (2026)
mutate both benchmarks with three matched transformation types (lexical
vagueness, single-constraint removal, syntax/formatting noise) and measure
Pass@1 on 10 code-generation models spanning 7B to frontier scale. The same
under-specification mutation that costs HumanEval an average −11.8% Pass@1
costs LiveCodeBench only −0.9%, and the gap widens moving from
syntax-noise to lexical-vagueness to constraint-removal mutations — the
mutation types ordered by how much semantic content they strip.[^c1]

The located mechanism is attention allocation, not capacity: on HumanEval,
where the docstring is the only specification, models concentrate 60–86% of
attention on it, so a mutation there has nowhere else for the model to
recover the missing content from; on LiveCodeBench, 30–50% of attention
falls on the I/O-format and sample-I/O regions, which a description- or
constraint-level mutation leaves untouched, so the model reads the missing
piece back out of a redundant channel.[^c2]

## Why it matters

Model scale predicted none of this: degradation under under-specification
is statistically indistinguishable across the 7B, 15–34B and API-frontier
tiers on HumanEval, and the two reasoning models tested (GPT-5-mini, Claude
Sonnet 4) lost the same ∼9.7% as the small open-weight models.[^c3]

A
practitioner or benchmark designer asking whether a prompt needs to be
complete is asking the wrong question — the right one is whether the
description's content is carried once or several times over. A task
description with redundant channels tolerates a missing constraint because
the constraint is recoverable elsewhere; a single-channel description
cannot recover anything it loses. This reframes the standard fragility
result from HumanEval/MBPP-style benchmarks (`[6, 21, 24, 30, 34, 43]` in
the source) as a property of those benchmarks' minimal, single-channel
format rather than a general property of LLM code generation.

## Limits

- Established only for Python code generation on two benchmarks and one
  family of matched mutations; not shown to generalize to natural-language
  QA or other structured-output tasks, where "channel redundancy" may not
  decompose the same way.
- The attention-allocation account is correlational (a measured
  distribution alongside a measured Pass@1 gap), not an intervention that
  manipulates attention directly to test the causal link.
- LiveCodeBench's near-zero *net* effect masks large, roughly balanced
  gross effects in both directions (see [[retrieval-cue-disruption]]);
  "robust" here means the harms and the gains cancel, not that individual
  problems are insensitive to the mutation.
- Ten models across five families is not exhaustive; closed frontier models
  beyond the two tested are unverified for this pattern.

## Related

[[retrieval-cue-disruption]] · [[format-restriction-effect]] · [[domain-breadth-question-convergence]] · [[masking-vs-mitigating-bias-reduction]]

[^c1]: arxiv-2604-24712 — "Robustness to under-specification is governed by prompt structure rather than by model size or architecture."
[^c2]: arxiv-2604-24712 — "on HumanEval, models concentrate 60–86% of attention on the description, the only available specification, whereas on LiveCodeBench, 30–50% of attention falls on I/O format and sample I/O regions that remain intact on mutated prompts."
[^c3]: arxiv-2604-24712 — "the degradation is identical across small, large, and API model groups on HumanEval, with API level reasoning models equally affected (GPT-5-mini and Claude Sonnet 4 both losing ∼9.7 % under US)."
