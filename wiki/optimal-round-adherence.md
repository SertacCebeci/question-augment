---
description: "A benchmark metric scoring how close a clarification dialogue's round count is to an annotated optimum, via a Gaussian penalty peaked at the key-question count plus one."
aliases: ["Optimal Round Adherence", "ORA"]
sources: ["fang-2026-clarifycodebench"]
---
# Optimal round adherence

> Treat every clarification round as a cost and score a dialogue highest
> when it stops after exactly enough rounds — not more, not fewer.

## Definition / Mechanism

Fang et al. (2026) define Optimal Round
Adherence (ORA) for ClarifyCodeBench: let $n$ be the number of rounds in
which the model asks a clarification question, and let $Q$ be the task's
annotated key-question set. The optimal round count is fixed at
$K=|Q|+1$, the extra round accounting for the step where the model stops
asking and produces code. ORA applies a Gaussian penalty on the
deviation, $\mathrm{ORA}(n,K,\sigma)=\exp(-(n-K)^2/2\sigma^2)$, with
$\sigma$ set so $\mathrm{ORA}=0.5$ at $|n-K|=0.5K$ (giving
$\sigma\approx0.425K$); the score is bounded in $(0,1]$, highest at
$n=K$, and falls off smoothly on both sides of it.[^c1]

## Why it matters

ORA is a stopping metric applied to the asking side: it penalizes both
premature code generation (too few rounds to have covered every key
question) and over-questioning (rounds spent past that point)
symmetrically, against one annotated optimum per task. On the same
six-model evaluation the scores are low — DeepSeek-V3.2 highest at 0.50,
most others below 0.35 — showing that the same models under-covering key
questions early (low [[turn-discounted-key-question-rate|TKQR]]) also
fail to time their own stopping point.[^c2]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | A Gaussian-shaped closeness score: penalize deviation from a target value smoothly rather than with a hard threshold | Applied to the number of clarification rounds a model takes, against a target fixed by the benchmark's own annotation |
| What survives | The bounded, symmetric, smoothly decaying shape, and a closed-form way to set the spread ($\sigma$) from one interpretable deviation point | Both carry over unchanged in the formula |
| What does not | A generic Gaussian penalty carries no claim about what the target value should be — that is supplied externally, from whatever the modeler decides is optimal | Here the target $K=|Q|+1$ is not derived from an optimality argument about search order (contrast the NP-hardness result behind [[optimal-decision-tree]]); it assumes exactly one round per key question is achievable and that no round is ever spent on a question the annotation did not anticipate |
[^c3]

## Limits

- $K=|Q|+1$ assumes the annotated key-question set is complete and that
  one round suffices per key question; a model that legitimately needs a
  follow-up to interpret an ambiguous answer is scored as
  over-questioning by the same formula that catches wasted rounds.
- Evaluated on the same one benchmark and six models as
  [[turn-discounted-key-question-rate|TKQR]] (419 tasks, deletion-only
  [[efe-planning-as-variational-inference|ambiguity]] injected into LiveCodeBench v6); no cross-benchmark or
  human-baseline comparison is reported.

## Related

[[turn-discounted-key-question-rate]] · [[clarification-benchmarks]] · [[sprt]] · [[value-of-information]]

[^c1]: fang-2026-clarifycodebench — "We define the optimal interaction round count as 𝐾 = |Q|+1. The additional round accounts for the final step in which the model stops asking questions and transitions to code generation."
[^c2]: fang-2026-clarifycodebench — "DeepSeek-V3.2 achieves the highest TKQR, at 0.30, and the highest ORA, at 0.50, while most other models remain below 0.30 on TKQR and below 0.35 on ORA."
[^c3]: fang-2026-clarifycodebench — "We define the optimal interaction round count as 𝐾 = |Q|+1. The additional round accounts for the final step in which the model stops asking questions and transitions to code generation."
