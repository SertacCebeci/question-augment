---
description: "Removing an automatic requirements-engineering stage (defect detection, clarification, decomposition) from a runtime code-generation pipeline drops task success from 89.2% to 56.6% Pass@1."
aliases: ["automatic RE ablation", "ReqEvolve ablation study"]
sources: ["fahim-2026"]
---
# Automatic-RE ablation effect

> A runtime code-generation pipeline that clarifies and decomposes a
> user's request before generating code passes 89.2% of its test cases on
> first try; strip the whole requirements stage out and keep only the
> test-driven code generation, and that drops to 56.6% — a 32.6
> percentage-point gap, on the same 72 tasks.

## Definition / Mechanism

Fahim & Ferrari (2026) evaluate ReqEvolve, a pipeline that
runs an automatic requirements-engineering (RE) stage — rule-based defect
detection (AQUSA), [[self-hypothesized-clarification|self-hypothesized
clarification]] of the detected defects, and specification decomposition
into acceptance criteria — ahead of an iterative test-driven code
generation stage, against an ablation baseline that shares the identical
code-generation infrastructure but skips the whole RE stage (it replicates
SelfEvolve, a prior runtime self-extension framework with no RE component).
Both variants ran on the same 72 user-story tasks across 18 projects, 4
runs each (288 evaluations per system). ReqEvolve reached 89.2% Pass@1
(257/288); the ablation baseline reached 56.6% (163/288) — a 32.6
percentage-point improvement, Wilcoxon signed-rank $W = 153.0$, $p < 0.001$,
large effect $r = 0.88$ on 18 paired projects.[^c1]

The paper further reports that the gap is not uniform across task types:
"Integration and data processing tasks show larger improvements... 
Compositional tasks... show smaller gains," which the authors attribute to
decomposed requirements helping the agent navigate existing code and data,
while composition instead leans on the shared TDD component both systems
have.[^c2]

## Why it matters

This isolates the RE stage as a whole — not any one of its three
sub-components, which the authors state they did not ablate separately
("The RE sub-components are tightly linked with each other, so they are
not evaluated independently") — as the source of a large, statistically
significant gain in a concrete, end-to-end asking pipeline: interpreting
and clarifying an underspecified request before acting on it roughly
doubles the failure rate's reduction relative to acting on the raw request.
It is one of the few numbers in the wiki that prices the *entire* act of
turning an ambiguous request into a resolved one, rather than one question
at a time.[^c3]

## Limits

- The ablation removes AQUSA defect detection, clarification and
  specification decomposition together; the number cannot be attributed to
  [[self-hypothesized-clarification]] specifically, only to the RE stage as
  a bundle — the authors say so explicitly.
- Single paper (fahim-2026), single benchmark of 72 tasks the same authors
  constructed; no independent replication is cited here (`replicated:
  null`).
- Success is graded by an LLM judge (o4-mini) against binary pass/fail
  criteria, cross-checked on a 267-case stratified sample against one human
  rater (Cohen's $\kappa = 0.67$, substantial but not perfect agreement) —
  some fraction of both Pass@1 figures reflects judge noise, not the RE
  stage's true effect.
- The ablation baseline (SelfEvolve) is a real prior system, not a
  minimal control; it differs from ReqEvolve only in lacking the RE stage,
  but nothing here bounds how much of the gap a *simpler* non-RE baseline
  (e.g. no clarification but still some prompt-level intent restatement)
  would have closed.

## Related

[[self-hypothesized-clarification]] · [[clarification-action-generation]] · [[defect-localization]] · Selection

[^c1]: fahim-2026 — "ReqEvolve achieves 89.2% Pass@1 (257/288), a 32.6% improvement over the ablation baseline (56.6%, 163/288)."
[^c2]: fahim-2026
[^c3]: fahim-2026 — "The RE sub-components are tightly linked with each other, so they are not evaluated independently."
