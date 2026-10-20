---
description: "Verbal confidence predicts an LLM's later commit-or-abstain decision more than answer correctness across eight models; log-probability confidence shows no such gap."
aliases: ["decision-truth gap", "commit-readiness signal"]
sources: ["kumaran-2026"]
---
# Verbal-confidence commit-readiness dissociation

> The model's stated confidence tells you more about whether it will stand
> behind an answer than about whether the answer is right.

## Definition / Mechanism

Using the [[two-stage-abstention-paradigm]], Kumaran (2026)
defines the decision–truth gap $\Delta_{DT} = \mathrm{AUROC}_{[[abstention]]} -
\mathrm{AUROC}_{correctness}$ for a Phase-1 confidence signal, computed on
the same trials. Class-based and numeric verbal confidence (VC) show
positive gaps in nearly every model–dataset cell — "every cell (Table 5;
Figure 2). Class-based VC gaps ranged from +0.05 to +0.26 across the
eight" model–dataset cells — while calibrated log-probability confidence
(Cal-LP) "predicts abstention substantially better than correctness,
whereas Cal-LP discriminates abstention" and correctness comparably (i.e.
near-zero gap).[^c1]

Residualising VC on Cal-LP isolates the part of verbal confidence Cal-LP
does not explain: "For Class-VC, the residual signal remained predictive
of abstention in all eight non-reasoning model" cells, while its
correctness discrimination collapsed to chance. This residual is "truth;
it is preferentially aligned with the model's later commit/abstain
decision. This pattern matches" a decision-aligned component in verbal
confidence that is independent of truth-tracking evidence, not
truth-evidence Cal-LP simply missed.[^c2]

In Gemma 3 and Gemma 4, a post-answer activation state — read out before
the abstention prompt is shown — already separates trials the model will
later commit to from ones it will abstain on: "classes. Crucially, this
state was not merely predictive. Steering along the VC-specific component
of" that state "causally shifted later abstention behaviour in Gemma 4."[^c3]

Kumaran frames the result against first/second-order confidence accounts
in humans: verbal confidence functions as "a partial self-report of an
internal commit-readiness state rather than of a pure correctness
estimate. This" reframes verbal confidence as a behaviour-facing readout,
not a correctness estimate.[^c4]

## Known as

Not this concept: the **decision–truth gap** ($\Delta_{DT}$) is the
measurement this note reports, not a separate object; [[calibration]]
error and [[sequence-likelihood-confidence|Cal-LP's AUROC weakness]]
describe a *different* failure — a confidence score that fails to rank
correct above incorrect at all — whereas this dissociation is about a
score that ranks well for one outcome (commitment) and poorly for another
(correctness) on the *same* trials.

## Why it matters

On stall 10, this blocks reading a model's verbal confidence as a
correctness estimate even when it looks well-behaved behaviourally: high
verbal confidence predicts the model will commit, not that the commitment
is right. On stall 7, it means a confidence-gated stopping rule built on
verbal confidence can look decisive (the model commits) while the
underlying answer correctness is no better anchored than chance-level
residual discrimination (median AUROC 0.49) shows.

## Limits

- Four non-reasoning and four reasoning models, English-language QA
  benchmarks (SimpleQA, MMLU-Pro, SuperGPQA, HLE); the claim rests on
  AUROC-based discrimination, not on a causal account of what verbal
  confidence is computed *from*.
- The residualisation uses Cal-LP as a proxy for the latent truth signal,
  not the truth signal itself; the paper is explicit this only requires
  Cal-LP to capture the bulk of shared correctness variance, not to equal
  it exactly.
- Mechanistic (activation-level) evidence is reported only for Gemma 3 and
  Gemma 4, where internal activations were accessible; the steering result
  is reported causally in Gemma 4 only.

## Related

[[abstention]] · [[sequence-likelihood-confidence]] · [[two-stage-abstention-paradigm]] · [[calibration]] · [[semantic-entropy]]

[^c1]: kumaran-2026 — "every cell (Table 5; Figure 2). Class-based VC gaps ranged from +0.05 to +0.26 across the"
[^c2]: kumaran-2026 — "For Class-VC, the residual signal remained predictive of abstention in all eight non-reasoning model"
[^c3]: kumaran-2026 — "classes. Crucially, this state was not merely predictive. Steering along the VC-specific component of"
[^c4]: kumaran-2026 — "self-report of an internal commit-readiness state rather than of a pure correctness estimate. This"
