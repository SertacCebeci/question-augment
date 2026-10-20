---
description: "A one-call gate runs a self-verification prompt beside the solver and overrides its answer to abstention whenever the verifier reports a factual contradiction in the input."
aliases: ["contradiction gate", "P1 pipeline"]
sources: ["sadowski-2026"]
---
# Contradiction gate

> Do not train the solver to notice a defect it already has the words for
> under a different prompt — ask it separately, and let that answer veto
> the first.

## Definition / Mechanism

Sadowski & Chudziak (2026) define two pipelines over the
same solver call: "P0 is the solver alone: its output is whatever number or
null the model returns. P1 is the contradiction gate: take the P0 output,
but override it to [[abstention]] (null) whenever the verifier returns
contradiction. The gate is deliberately contradiction-specific: it does not
act on missing, because the solver already abstains on missing facts (§4)
and gating there would conflate the two effects. P1 adds exactly one model
call to P0 and changes nothing on inputs the verifier passes."[^c1]

The abstract states the design goal and cost bound directly: "We wire that
verification call into a simple contradiction gate: one extra call that
abstains when the model reports a conflict. Across all six models it
recovers most of the missed contradiction abstention at a clean-accuracy
cost of at most about 5 percentage points, with no training and no external
tooling."[^c2]

Measured effect: "Applying P1 raises contradiction abstention to 70-83%
across all six models, from a P0 baseline as low as 0%... the share of
contradicted inputs answered with the clean-input value drops from 63-76%
to 11-15%."[^c3]

## Why it matters

The gate converts [[solve-verify-detection-gap]] — a capability the solve
framing leaves unused — into abstention without fine-tuning, external
tooling, or a second model: it is a prompting-and-routing fix, not a
capability fix, priced entirely in one extra call and a bounded
clean-accuracy cost.[^c4]

## Transfer

| | |
|---|---|
| Home field | LLM-based tax/legal reasoning pipelines, same-model solve and verify calls |
| Here | any answerer pipeline where a generative step could silently commit to a defective input |
| What survives | overriding a commit decision with a single, narrowly-scoped secondary check rather than retraining the primary call; scoping the override to one named failure mode (contradiction) instead of a blanket confidence threshold |
| What does not | the specific accuracy-cost bound (0-5.1 points) and detection rate (70-83%), which are this benchmark's and this same-weights verifier's, not a property of gating in general |

## Limits

- The verifier shares weights with the solver (§3.6 of the source): "This
  holds the model fixed (same weights, solve versus verify), at the cost of
  correlated errors" — a correlated blind spot in the solver could be a
  blind spot in the gate too, untested here.[^c5]
- Evaluated only against a single injected contradiction per case; the paper
  does not test the gate against multiple simultaneous contradictions or
  contradictions the perturbation pipeline did not construct.
- The gate is proposed "to test whether the detected conflict converts into
  abstention, not as a system we propose for deployment" — the authors
  themselves do not claim it as a finished component.

## Related

[[solve-verify-detection-gap]] · [[abstention]] · [[conflict-aware-belief-gate]] · Commitment

[^c1]: sadowski-2026 — "P0 is the solver alone: its output is whatever number or null the model returns. P1 is the contradiction gate: take the P0 output, but override it to abstention (null) whenever the verifier returns contradiction. The gate is deliberately contradiction-specific: it does not act on missing, because the solver already abstains on missing facts (§4) and gating there would conflate the two effects. P1 adds exactly one model call to P0 and changes nothing on inputs the verifier passes."
[^c2]: sadowski-2026 — "We wire that verification call into a simple contradiction gate: one extra call that abstains when the model reports a conflict. Across all six models it recovers most of the missed contradiction abstention at a clean-accuracy cost of at most about 5 percentage points, with no training and no external tooling."
[^c3]: sadowski-2026 — "Applying P1 raises contradiction abstention to 70-83% across all six models, from a P0 baseline as low as 0% (Fig. 2). The answer-preservation rates that defined the diagnosis fall accordingly: for the high-accuracy models, the share of contradicted inputs answered with the clean-input value drops from 63-76% to 11-15%."
[^c4]: sadowski-2026 — "a trivial one-call check, using the model itself as an input verifier and abstaining when it reports a contradiction (the contradiction gate), recovers 70-83% contradiction abstention at 0-5.1 percentage points of clean-accuracy cost, across all six models with no fine-tuning and no external tooling."
[^c5]: sadowski-2026 — "The verifier is the same model as the solver: this holds the model fixed (same weights, solve versus verify), at the cost of correlated errors (§6)."
