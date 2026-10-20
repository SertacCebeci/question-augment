---
description: "Removing a constraint from a task description degrades LLM code correctness far more, and more uniformly across model scale, than vague wording or surface-format noise."
aliases: ["defect-type severity asymmetry", "under-specification robustness gap"]
sources: ["arxiv-2604-24703"]
---
# Under-specification severity asymmetry

> Not every way a request is underspecified costs the same: dropping a
> constraint hurts every model at every scale, vague wording hurts only
> some benchmarks, and typos barely register.

## Definition / Mechanism

Akli, Cordy, Papadakis & Le Traon (2026) mutate[^s1]
working task descriptions from three code-generation benchmarks
(HumanEval, MBPP, LiveCodeBench) along three independent axes and
measure the Pass@1 cost on ten LLMs spanning 6B to frontier scale:

- **Under-Specification (US)** — delete one explicit constraint (a
  numeric bound, an edge-case behavior, an output-type requirement)
  while keeping the description grammatical.
- **Lexical Vagueness (LV)** — replace precise vocabulary and
  identifiers with vaguer synonyms; no constraint is removed.
- **Syntax/Formatting (SF)** — inject typographical and layout noise
  with no semantic change.

Holding the reference solution and tests fixed isolates the wording
change as the only cause of any Pass@1 delta. The three axes are not
interchangeable: "Not all defect types harm code generation equally:
Under-Specification degrades performance by up to 15% on HumanEval and
MBPP, LV causes moderate losses, and SF is negligible." US costs
7.9–15.3% Pass@1 on HumanEval and 5.1–10.8% on MBPP across every model
tested, including frontier reasoning models with baselines above 95%:
"GPT-5-mini and Claude Sonnet 4, despite baselines of 96.3% and 95.7%
respectively, each decline by 9.7%." LV's cost is
benchmark-dependent (1.3–12.2% on HumanEval, only 1.5–3.2% on MBPP's
shorter descriptions) and SF's is negligible, staying below 3.7% on
HumanEval and 1.6% on MBPP with several models gaining slightly.

**Context buffers all three defects at once.** LiveCodeBench, whose
problem statements carry explicit numerical bounds, formal I/O
contracts and worked examples, stays within ±2.0% Pass@1 under every
defect type, because the removed constraint is often still recoverable
from the surviving example: "descriptions with richer context leads
to more robustness in code generation." Model scale does not
predict robustness — GPT-5-mini and Claude Sonnet 4 lose as much to US
as small open models do — so the moderating variable is the
description's structure, not the model reading it.

The same asymmetry surfaces where no injected mutation is involved.
A classifier trained only on the injected defects, run on 456
originally "clean" benchmark descriptions, flags 83 (18.2%) as
defective — every one of them as under-specified, none as vague or
malformed — and those flagged descriptions fail almost every model:
"90.9% failure rate on MBPP, 98.0% on LiveCodeBench", with 72.7%
of the inspectable MBPP cases confirmed under-specified on manual
review. Missing constraints, not surface wording, are the recurring
fault line in descriptions nobody flagged as broken.

## Why it matters

A framing/wording intervention on a request is not one lever with one
effect size: whether the change removes a constraint, replaces a
term, or scrambles formatting predicts the size of the damage far
better than which model reads it. A practitioner auditing task
descriptions for quality should weight constraint completeness far
above lexical polish or formatting hygiene, and should expect a
benchmark or prompt style with explicit bounds and worked examples to
mask under-specification that a terser one would expose.

## Limits

Defects are synthetically injected by an LLM (gpt-5-mini) and judged
for compliance by another LLM, with only a 100-instance stratified
human check; the under-specification mutation itself is the
hardest to keep natural (0.61 naturalness on LiveCodeBench). The result
is scoped to Python code-generation Pass@1 under greedy decoding, one
constraint removed at a time; whether the same asymmetry holds for
non-code tasks or for descriptions missing more than one constraint is
**unverified**. The three benchmarks differ in more than description
richness (task style, difficulty, domain), so "richer context" is a
plausible rather than isolated cause of LiveCodeBench's resilience.

## Related

- [[format-restriction-effect]]
- [[ambiguity-taxonomy]]
- [[survey-response-model]]

[^s1]: arxiv-2604-24703
