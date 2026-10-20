---
description: "A split-conformal calibration scoring each example by its worst risk underestimate across all candidate actions, giving one finite-sample bound valid for all actions without a union bound."
aliases: ["simultaneous prefix-risk certificate", "simultaneous upper-risk certificate"]
sources: ["saliencro-2026"]
---
# Simultaneous prefix-risk certificate

> Calibrating a risk bound separately for each candidate next step and then
> letting a policy pick among them needs a union bound over every candidate;
> calibrating on the *worst* underestimate across all candidates at once does
> not.

## Definition / Mechanism

Saliencro et al. (2026) note the problem a pointwise risk
estimate has near a decision boundary: "A point estimate is unsafe near a
stopping boundary."[^c1]

Their fix scores each disjoint [[calibration]] example by the largest amount any
candidate action's predicted risk underestimates its true risk, then takes a
conformal quantile of that single per-example score; the resulting bound is
added to every candidate's predicted risk to form its certificate. They state
the reason for taking the maximum over candidates rather than calibrating
each one on its own: "Using a maximum score is more conservative than
calibrating each prefix separately, but it protects the adaptive policy that
chooses which prefix to inspect."[^c2]

Theorem 1 (their numbering) gives finite-sample validity of the resulting
certificate simultaneously over every candidate action, for an exchangeable
calibration set and test example, and the paper draws out what that buys an
adaptive policy: "Consequently, adaptively selecting a site and prefix from
these certificates does not require an additional union bound over actions."[^c3]

The proof mechanism is ordinary split-[[conformal-prediction|conformal calibration]] applied to a
different scalar than usual: "Theorem 1 follows by applying split-conformal
calibration to the scalar maximum residual $s_n$: exchangeability gives the
rank guarantee for the test maximum, which simultaneously dominates every
action residual."[^c4]

## Why it matters

On stall 7, this is the certificate that lets [[vi-mole|VI-MoLE]]'s greedy
allocator compare many candidate next-acquisition actions against one shared,
already-valid bound and stop exactly when the best certified gain is
non-positive, instead of paying a per-comparison statistical cost (a union
bound that would shrink with every additional candidate considered) for the
privilege of comparing them.

## Transfer

| | |
|---|---|
| **In its home field** | Split-conformal prediction: one nonconformity score per calibration point, exchangeable with a single test point, giving marginal coverage for that one point |
| **Here** | Many candidate next actions (expert prefixes) are live at once, and a policy adaptively picks among them after seeing the certificates |
| **What survives** | The finite-sample, distribution-free guarantee; the trick of folding "which candidate might be picked" into the calibration score itself (the max over candidates) instead of paying for it after calibration |
| **What does not** | The guarantee's exchangeability requirement, and its conservatism: bounding the *worst* candidate's underestimate is tighter for one action but looser for every action than separate per-candidate calibration would be for that action alone |

[^c5]

## Limits

- Needs calibration and test examples to be exchangeable; distribution shift
  between calibration and deployment breaks the guarantee, which the paper
  reports as a monitored failure mode ("the certificate can fail under
  shift") rather than a solved one.
- The bound is a probabilistic guarantee at a chosen level $1-\delta$, not a
  worst-case deterministic bound; it says nothing about any single draw
  falling outside it, only about the long-run rate.
- Distinct from [[round-wise-regret-conformal-acceptance]]'s guarantee: that
  result is per-round, conditional on reaching a round, and covers one
  controller's proposed action; this one is simultaneous across every
  candidate action available at one decision point and says nothing about
  validity across a sequence of such points.

## Related

[[vi-mole]] · [[round-wise-regret-conformal-acceptance]] · [[abstention]] · [[sprt]]

[^c1]: saliencro-2026 — "A point estimate is unsafe near a stopping boundary."
[^c2]: saliencro-2026 — "Using a maximum score is more conservative than calibrating each prefix separately, but it protects the adaptive policy that chooses which prefix to inspect."
[^c3]: saliencro-2026 — "Consequently, adaptively selecting a site and prefix from these certificates does not require an additional union bound over actions."
[^c4]: saliencro-2026
[^c5]: saliencro-2026 — "Using a maximum score is more conservative than calibrating each prefix separately, but it protects the adaptive policy that chooses which prefix to inspect."
