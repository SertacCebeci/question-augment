---
description: "A distribution-free lower confidence bound on predicted task return that decides, per candidate task, whether to deploy a recovered policy or abstain to a fallback."
aliases: ["task readiness certificate", "readiness certificate", "deploy-or-abstain certificate"]
sources: ["kiet-2026"]
---
# Task readiness certificate

> After probing, an agent must still decide how much of its belief to act
> on: commit to a task-specific policy, or admit the evidence is not
> enough and hand off to a safe fallback. This certificate makes that call
> from one number — a lower bound on predicted return — compared against
> a fixed threshold.

## Definition / Mechanism

Kiet & Binh (2026) propagate the posterior formed by
[[evidence-gated-matched-pulse-transport|Evidence-Gated Matched-Pulse
Transport]] through a world-model ensemble to a posterior-predictive
distribution of return $\hat J_\kappa$ for each candidate task $\kappa$,
with predictive mean $\hat\mu_\kappa$ and variance $\hat\sigma_\kappa^2$
combining world-model disagreement and remaining fault uncertainty.[^c1]

Assuming only finite variance and a calibrated posterior-predictive
distribution (no Gaussian assumption), Cantelli's inequality gives a
lower confidence bound $L_\kappa = \hat\mu_\kappa -
\sqrt{(1-\alpha)/\alpha}\,\hat\sigma_\kappa$ with
$\Pr(\hat J_\kappa \ge L_\kappa) \ge 1-\alpha$.[^c2]

The operational rule is: if $L_\kappa \ge J_{\min}$, deploy the recovered
policy $\pi_\kappa$; if $L_\kappa < J_{\min}$, abstain and execute the
fallback $\pi_\kappa^{\text{fallback}}$; and [[calibration]] is checked
empirically through held-out certificate violations, because the bound is
conditional on the modeled change family and predictive model.[^c3]

Even when the diagnostic budget is exhausted without a fault alarm, the
certificate does not treat the system as certainly nominal: the
undiscarded posterior uncertainty still propagates into $L_\kappa$ and can
force [[abstention]] for tasks whose return the evidence does not adequately
support.[^c4]

## Why it matters

This is a concrete instance of stall 10 (how much to commit, and how to
say the rest): commitment is not binary confidence but a threshold
comparison on a calibrated lower bound, and "the rest" is stated
explicitly as a named fallback policy rather than a hedge in language.

## Limits

- The certificates are **empirical and distribution-dependent, not formal
  closed-loop safety guarantees**; they cover a finite task and correction
  library, and their conclusions need not transfer to unseen objectives,
  operating regions, simultaneous faults, or adversarial changes.[^c5]
- A readiness certificate is only as meaningful as its task library, loss
  model, calibration data, and fallback policy; the paper itself frames
  EG-MPT as one component of a broader assurance process, not a
  standalone safety guarantee.[^c6]
- The Cantelli bound is one-sided and distribution-free, which buys
  robustness to the predictive shape at the cost of looseness relative to
  a bound that assumed (and got right) a specific distribution family.
- Evaluated only on simulated dormant-actuator benchmarks; a single
  source (`kiet-2026`), unverified beyond the researcher's provisional
  check.

## Related

[[evidence-gated-matched-pulse-transport]] · [[value-of-information]] · [[sprt]] · [[expected-utility]]

[^c1]: kiet-2026 — "By the law of total variance, this predictive variance is the sum of world-model disagreement at fixed dynamics and uncertainty over the changed mechanism and its effectiveness. We use the combined quantity because both sources can invalidate a deployment claim."
[^c2]: kiet-2026 — "Assume Jbκ has finite variance and the posterior-predictive distribution is calibrated for the modeled change family. Cantelli’s inequality states that, for every a > 0"
[^c3]: kiet-2026
[^c4]: kiet-2026
[^c5]: kiet-2026 — "Our certificates are empirical and distribution-dependent, not formal closed-loop safety guarantees. They cover a finite task and correction library, and their conclusions need not transfer to unseen objectives, operating regions, simultaneous faults, or adversarial changes."
[^c6]: kiet-2026 — "A readiness certificate is only as meaningful as its task library, loss model, calibration data, and fallback policy. In high-consequence applications, EG-MPT should therefore be used as one component of a broader assurance process that includes physical constraints, independent monitoring, operator oversight, and domain-specific validation."
