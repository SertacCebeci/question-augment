---
description: "Rivin's (2026) reading of two models on hard math benchmarks - named-theorem matching, then derivation, then abstention fire in order; missing an inner layer loops or crashes instead."
aliases: ["architectural-asymmetry interpretation", "layered fallback architecture"]
sources: ["rivin-2026"]
---
# Layered reasoning fallback

> When named-theorem recognition fails to close a problem, a model with a
> working fallback drops to first-principles derivation, and when that
> also fails, drops again to calibrated [[abstention]]; a model missing one of
> these inner layers does not fail gracefully at the boundary — it loops
> or crashes.

## Definition / Mechanism

Comparing GPT and Gemini across five reasoning traces on the [[algebraic-trapdoor-benchmark|algebraic
trapdoor benchmark]], Rivin (2026) reads the cross-tabulated
outcomes — Gemini solving instantly when a named theorem matches
(McLaughlin, Coxeter) but crashing after over two hours when none does;
GPT taking minutes-to-hours via explicit derivation when no theorem
matches, and outputting DON'T KNOW rather than a wrong answer when
derivation also fails — as evidence of a three-tier fallback: "The data is
consistent with GPT having a threelayer reasoning architecture and Gemini
having only the first layer:"[^c1]

"Layer 3: calibrated abstention. GPT has this and uses it when Layer 2
also doesn’t close (the X10 DON’T KNOW). Gemini has only an implicit “try
harder” behavior that runs unbounded until something internal trips."[^c2]

The claim is explicitly an inference from behavior, not from inspecting
either model: "We do not have direct access to Gemini’s internal state and
so cannot determine whether the failure was a budget overflow, a
heuristic short-circuit, or a deliberate abdication."[^c3]

## Why it matters

This reframes calibrated abstention (stall 10) as the last rung of a
fallback ladder rather than a standalone capability: a model can have
correct named-theorem knowledge and still fail to abstain gracefully if it
has no first-principles layer beneath the theorem-matcher to fall back to
before the abstention decision is even reached. It predicts that
abstention quality should be measured together with what a model does
*before* it decides to abstain, not as an isolated score.

## Limits

- Two models, five reasoning traces, three instance families: "A more
  controlled study with more interactions per model would be needed to
  confirm; the asymmetry between the two models is, however, already
  pronounced enough to be the primary empirical finding of the paper
  alongside the X10 abstention itself."[^c4]
- The three layers are read off aggregate outcome patterns (solved fast /
  solved slow / abstained / crashed), not from any interpretability probe
  of either model's internal computation.
- Gemini's failure is an internal error with no exposed reasoning trace;
  the paper cannot distinguish a missing fallback layer from a budget cap
  or an unrelated infrastructure fault.
- This is Rivin's own reading of the cross-tabulation, offered as the
  "strongest reading consistent with" four data points, not a mechanism
  the paper demonstrates directly.

## Related

[[algebraic-trapdoor-benchmark]] · [[abstention]] · [[solve-verify-detection-gap]] · Commitment

[^c1]: rivin-2026 — "The data is consistent with GPT having a threelayer reasoning architecture and Gemini having only the first layer:"
[^c2]: rivin-2026 — "Layer 3: calibrated abstention. GPT has this and uses it when Layer 2 also doesn’t close (the X10 DON’T KNOW). Gemini has only an implicit “try harder” behavior that runs unbounded until something internal trips."
[^c3]: rivin-2026 — "We do not have direct access to Gemini’s internal state and so cannot determine whether the failure was a budget overflow, a heuristic short-circuit, or a deliberate abdication."
[^c4]: rivin-2026 — "A more controlled study with more interactions per model would be needed to confirm; the asymmetry between the two models is, however, already pronounced enough to be the primary empirical finding of the paper alongside the X10 abstention itself."
