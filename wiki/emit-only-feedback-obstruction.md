---
description: "Under distribution shift, a risk-control rule seeing outcomes only on inputs it answers can be forced to violate its target regardless of tuning; full feedback fixes it."
aliases: ["emit-only feedback obstruction", "Proposition 8"]
sources: ["kotte-2026"]
---
# Emit-only feedback obstruction

> Adaptive conformal inference retunes its [[abstention]] threshold online using
> the risk it observes — but it only observes risk on the inputs it
> answered. Under shift, that missing half of the feedback is enough to
> defeat any step size: the failure is a property of what the policy is
> allowed to see, not of how it is tuned. A monitor that also sees (or can
> verify) risk on what it abstained from does not fail the same way.

## Definition / Mechanism

"Under emit-only feedback (risk observed only on emitted inputs) and
arbitrary shift, any procedure that guarantees anytime emitted-risk control
at level α with probability ≥ 1 − δ (δ < 1) and emits with positive
probability can be forced to violate." Applied to the paper's own adaptive
method: "ACI uses emit-only feedback, so its failure is a property of the
feedback model, not of the step size γ; the positive guarantee requires
full feedback (a verifier, or labels on abstained inputs)."[^c1]

Adaptive Conformal Inference (ACI) retunes its threshold as
$\lambda_t=\lambda_{t-1}+\gamma(\alpha-\mathrm{eff}_t)$, where $\mathrm{eff}_t$
is the observed risk on emitted inputs and 0 on abstention; its long-run
average is pinned near $\alpha$ by construction — "the long-run effective
risk is pinned near α, which is an algebraic property of the update, not a
finite-sample guarantee on emitted risk" — which is exactly why it looks
adequate while still failing under shift.[^c2]

## Why it matters

On 16 cross-dataset transfers where the base risk exceeds the target
(µ > α), "the target is violated on 14 of 16 transfers by static CRC and
every tested ACI step size (γ ∈ [0.001, 0.1], 7 values)." Against the same
16 transfers, a monitor given full feedback rather than emit-only feedback
holds: "a full-feedback anytime-valid monitor (SAVeR-FF) that abstains
whenever it cannot certify emitted risk at level δ achieves 0/16
violations, and is non-vacuous on feasible streams, emitting 65–97% of
inputs ... at controlled risk." The paper is explicit that this monitor is
not a new construction — "closely related to A-RCPS (Xu et al., 2024),
Conformal Selective Acting (Khosravi & Huo, 2026), and anytime-valid CRC
(Hultberg et al., 2026)" — its contribution here is showing the
obstruction is real and that the fix is exactly "get a verifier or labels
on what you didn't answer," not a smarter step size.[^c3]

For an agent choosing between answering and deferring under shift, this
names precisely what closes the gap: not a better threshold-adaptation
rule, but access to ground truth (or a trusted verifier) on the inputs it
chose not to answer.

## Transfer

| | |
|---|---|
| **In its home field** | An impossibility result inside online/anytime-valid conformal inference under distribution shift, contrasting adaptive threshold updates (ACI) with full-feedback anytime-valid monitors |
| **Here** | Used to separate two failure modes of an "ask or abstain" policy under shifting conditions: a tuning failure (fixable by better hyperparameters) versus a feedback-model failure (fixable only by getting ground truth on what was skipped) |
| **What survives** | The dichotomy is formal and unconditional on the shift's size or direction: no step size $\gamma$ rescues emit-only feedback under adversarial shift (Prop. 8's "can be forced to violate") |
| **What does not** | The obstruction is stated for anytime, *emitted-risk* control specifically; it does not by itself bound how much feedback is enough, nor does it say what "labels on abstained inputs" costs to obtain in a live agent deployment |
[^c4]

## Limits

The obstruction is an existence result ("can be forced to violate") against
an adversarial shift sequence, proved in the paper's Appendix Q, which this
note does not reproduce independently. The 14/16 and 0/16 empirical
figures are drawn from three shift constructions (temporal reordering,
severity oversampling, cross-dataset transfer) on the paper's eight
[[structured-output|structured-generation]] datasets; whether the obstruction bites in other
shift regimes (e.g. adversarial inputs rather than dataset transfer) is not
tested here. The source is a single-author arXiv preprint (v2,
2026-09-07), not yet peer-reviewed.

## Related

[[conformal-abstention-floor]] · [[betting-based-conformal-risk-control]] · [[abstention]] · [[calibration]]

[^c1]: kotte-2026 — "Under emit-only feedback (risk observed only on emitted inputs) and arbitrary shift, any procedure that guarantees anytime emitted-risk control at level α with probability ≥ 1 − δ (δ < 1) and emits with positive probability can be forced to violate."
[^c2]: kotte-2026 — "the long-run effective risk is pinned near α, which is an algebraic property of the update, not a finite-sample guarantee on emitted risk."
[^c3]: kotte-2026 — "the target is violated on 14 of 16 transfers by static CRC and every tested ACI step size (γ ∈ [0.001, 0.1], 7 values)"
[^c4]: kotte-2026
