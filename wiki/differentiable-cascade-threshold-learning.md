---
description: "A cascade's discrete accept/defer thresholds are relaxed into a sigmoid gate and learned by gradient descent from streaming human-labeled feedback instead of fixed by hand."
aliases: ["online threshold learning", "online threshold optimizer"]
sources: ["arxiv-2604-12262"]
---
# Differentiable cascade threshold learning

> A cascade's accept/defer cutoff is a discrete indicator function, which
> has no gradient — so relax it into a sigmoid, learn it from a replay
> buffer of outcomes, and a single hand-picked threshold becomes a
> task-specific one that adapts on its own.

## Definition / Mechanism

Chang, Kwon, Lee & Verma (2026) start from the
obstacle: a cascade's per-stage routing rule is $\mathbb{1}[\phi_k \ge
\tau_k]$, and "since the decision to accept or defer at each stage is
discrete (based on the indicator function I[ϕk ≥ τk ]), the standard
gradient descent cannot be applied directly. To enable end-to-end
differentiability, we employ a soft relaxation technique during the
backward pass".[^c1]

Each threshold is reparameterized through a sigmoid, "τk = σ(θk ),
ensuring that the threshold remains within (0, 1)".[^c2]

The hard accept indicator is replaced during training by a
shifted-sigmoid "pass probability" whose sharpness is a temperature
parameter — so the forward pass can still route hard, while the backward
pass sees a smooth surrogate of the same decision. The thresholds are
then updated online rather than fixed before deployment: "We maintain a
replay buffer B to store recent query tuples (ϕ1:4 , ytrue , c1:4 ). In
update steps, we sample a mini-batch from B and perform a gradient update
on {θk } to minimize compound loss L using the Adam optimizer".[^c3]

The loss trades expected accuracy against expected cost across the
reached stages, so the learned thresholds settle where that trade-off is
best for the *observed* query distribution rather than for whatever
distribution the designer imagined when hand-setting a fixed cutoff. Held
against a fixed-threshold cascade on the same architecture: "Online
adaptation is critical. Fixed thresholds (τk = 0.6) perform reasonably but
plateau between base and large model performance, as a single cutoff
proves suboptimal across domains".[^c4]

The learned policy instead ends up
"learning task-specific boundaries that balance frugality and safety by
processing 44.40% of ARC-Easy queries at the first stage while
aggressively escalating only true edge cases in medical domains" — the
same mechanism produces a lenient threshold on an easy domain and a strict
one on a high-stakes domain without being told which is which.[^c5]

## Why it matters

It turns "where to set the commit/defer line" from a one-time design
choice into a parameter the system keeps correcting from its own
deployment outcomes — the same lever a fixed-threshold cascade also has,
but exercised continuously and per-domain instead of once and globally.
The differentiable relaxation is what makes this possible at all: without
it, a discrete threshold has no gradient to learn from, and the choice
would have to be re-tuned by hand for every task.

## Limits

The relaxation is a training-time device only — inference still uses the
hard indicator, so nothing here changes what the deployed decision rule
looks like, only how its parameter is found. Learning requires streaming
ground-truth feedback (a query's true label) to compute $\mathrm{corr}_k$
in the loss, which assumes a labeled feedback channel — e.g. delayed human
correction — is available post-deployment; without one, the mechanism
degenerates to the fixed-threshold baseline it is compared against. The
gain over fixed thresholds is reported on five multiple-choice benchmarks
with a two-tier, four-stage cascade; the paper does not test the learner
under adversarial or non-stationary feedback.

## Related

[[escalation-boundary-deliberation]] · [[calibration]] · [[abstention]] · [[bayesian-self-escalation]]

[^c1]: arxiv-2604-12262 — "Since the decision to accept or defer at each stage is discrete (based on the indicator function I[ϕk ≥ τk ]), the standard gradient descent cannot be applied directly. To enable end-to-end differentiability, we employ a soft relaxation technique during the backward pass"
[^c2]: arxiv-2604-12262 — "We parameterize each threshold τk as a scalar θk ∈ R such that τk = σ(θk ), ensuring that the threshold remains within (0, 1)"
[^c3]: arxiv-2604-12262 — "We maintain a replay buffer B to store recent query tuples (ϕ1:4 , ytrue , c1:4 ). In update steps, we sample a mini-batch from B and perform a gradient update on {θk } to minimize compound loss L using the Adam optimizer"
[^c4]: arxiv-2604-12262 — "Online adaptation is critical. Fixed thresholds (τk = 0.6) perform reasonably but plateau between base and large model performance, as a single cutoff proves suboptimal across domains"
[^c5]: arxiv-2604-12262 — "learning task-specific boundaries that balance frugality and safety by processing 44.40% of ARC-Easy queries at the first stage while aggressively escalating only true edge cases in medical domains"
