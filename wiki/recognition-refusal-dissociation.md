---
description: "A linear hidden-state direction predicts if an LLM treats a prompt as answerable, but is nearly orthogonal to its safety-refusal direction; recognition and refusal are separate circuits."
aliases: []
sources: ["du-2026"]
---
# Recognition-refusal dissociation

> A model can carry a clean internal signal that a question has no admissible
> answer and still answer it, because the circuit that would act on that
> signal is not the same one wired to the signal itself.

## Definition / Mechanism

Du & Hu (2026) probe hidden states of 11 models (1.7B–70B) on
prompts built to be structurally unanswerable — e.g. computing
$\cot(-540°)$ or evaluating `(1).startswith("1")` — against matched
answerable prompts. A single linear direction, obtained as the mean
difference between answerable (A) and unanswerable (U) activations, separates
the two classes with mean AUC 0.939 (range 0.841–0.993) across an 22-cell,
11-model grid.[^c1]

That direction is almost orthogonal to the model's existing safety-refusal
direction: mean cosine similarity 0.087.[^c2]

It is also causal, not merely correlational: steering generation along it
shifts invalidity-aware behaviour (naming the prompt as unanswerable versus
answering it) bidirectionally and dose-responsively on the structural
math/code prompts, with flip rates 33–52 percentage points above a
random-direction control.[^c3]

The paper's own diagnosis: "the model has a usable 'no admissible answer'
signal, but the safety-refusal pathway is not aligned to use it" — the
confident-on-impossible failure is a *routing* failure between an existing
recognition signal and the refusal circuitry, not a failure to *encode*
that a question is unanswerable.[^c4]

## Why it matters

This gives the answerer's side of stall 10 a mechanism-level claim that
[[abstention]] leaves exogenous: abstention prices "I don't know" once the
answerer has decided to abstain, but says nothing about whether the decision
to abstain is even connected to what the model knows. Here the two are shown
measurably disconnected inside one architecture — the "whether to say the
rest" decision can fail even when the "what to say" half already has the
right answer internally.

## Limits

- Read from a single unregistered web extract (the arXiv abstract page and
  an ar5iv HTML rendering); no archived PDF or text extract is on file for
  `du-2026` yet, so quotes above are provisional until the verifier locates
  them against an archived extract.
- The unanswerable prompts are narrow: structurally invalid math and code
  (undefined operations, type errors), not open-ended factual [[efe-planning-as-variational-inference|ambiguity]] or
  missing context — the kind of unanswerability [[clarification-benchmarks]]
  measures. Whether the same dissociation holds for that broader class is
  untested here.
- The near-orthogonality (cosine 0.087) is a population statistic over the
  probed models; it does not rule out routing through a nonlinear or
  distributed pathway the linear-direction analysis cannot see.
- Steering is an intervention on a proxy for the true decision circuit, not
  a manipulation of a named, independently verified mechanism; the paper's
  causal language rests on that proxy.

## Related

[[abstention]] · [[clarification-benchmarks]] · [[preference-signal-against-asking]] · [[scope-limitation]]

[^c1]: du-2026
[^c2]: du-2026
[^c3]: du-2026
[^c4]: du-2026
