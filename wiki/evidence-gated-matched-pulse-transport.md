---
description: "A Bayesian probing rule that selects each diagnostic intervention by risk reduction per cost and gates severity updates behind categorical fault evidence."
aliases: ["EG-MPT", "Evidence-Gated Matched-Pulse Transport"]
sources: ["kiet-2026"]
---
# Evidence-Gated Matched-Pulse Transport

> A rule for which physical probe to run next when a component may have
> silently degraded: choose the intervention that most reduces localization
> risk per unit charge, then let its continuous amplitude update a severity
> estimate only if the same response already favors the suspected fault
> categorically — never before.

## Definition / Mechanism

Kiet & Binh (2026) address a robot or controller whose current
policy never excites a mechanism that could have degraded (a dormant
actuator), so passive observation carries no evidence about it. Their
Evidence-Gated Matched-Pulse Transport (EG-MPT) is an intervention-based
Bayesian procedure that couples fault localization with estimation of
actuator effectiveness through a shared matched-response representation,
thereby preserving diagnostic [[calibration|reliability]] while converting localized
evidence into [[recovery-postulate|recovery]]-relevant uncertainty.[^c1]

**Which probe.** At each round, Stage 1 selects the trajectory with the
greatest expected reduction in task-weighted location risk per unit charge.[^c2]
The same physical response yields two numbers from one inner product: a
detection statistic $S_q$ (noise-scale normalized) and an amplitude estimate
$z_q$ (squared-norm normalized) — no second trajectory is spent to get
both.

**When to let severity in.** The category $C_q$ alone updates the location
belief $b_t$. If that category favors the targeted fault over nominal
dynamics, $z_q$ also updates the conditional effectiveness posterior
$\varphi_{t,j(q)}$; otherwise the conditional effectiveness posterior is
unchanged.[^c3]

This positive-[[likelihood-ratio]] gate is what "evidence-gated" names: a
continuous severity signal is transported into recovery-relevant belief
only on the branch where categorical evidence already opened the door for
it. The paper proves (Proposition 1) that even a badly misspecified
continuous severity likelihood cannot alter which diagnostic trajectory is
selected, when Stage 1 stops, or which mechanism it reports, provided the
categorical channel and location-side rules remain fixed — any inaccuracy
in the severity model is prevented from contaminating localization.[^c4]

## Why it matters

This is a named mechanism for *what* an agent probes and *when* it lets a
noisier estimate influence a more consequential belief: cost-normalized
greedy selection for the "which axis" question, and a categorical gate that
decides whether a second, less reliable signal is allowed to update state
at all.

## Transfer

| | |
|---|---|
| In its home field | Control/RL: physical interventions on a dynamical system, a categorical fault-location channel and a continuous severity channel, both derived from one calibrated response model |
| Here | A question-selection rule (cost-normalized expected risk reduction) and a gate on whether a second, weaker inference is allowed to update belief |
| What survives | The idea of pricing a candidate probe by risk reduction per unit cost, and of firewalling a noisy secondary estimate behind a more reliable categorical decision |
| What does not | The formal invariance guarantee (Proposition 1) is proved for this specific two-channel calibrated-response architecture; it is not established for open-ended question selection with no such channel separation |

## Limits

- The invariance and control-value results assume a **calibrated joint
  model**: nominal and fault-conditional response distributions fit on
  calibration trajectories disjoint from evaluation data, and a gain
  vector confined to a known range.[^c5]
- The method is designed for localized, intervention-responsive dynamics
  changes with diagnostic signatures represented in the calibration
  channel; matched-response transport is most reliable when response
  amplitude varies approximately monotonically with mechanism
  effectiveness — [[saturation]], deadbands, strong mechanism coupling, or
  state-dependent effects can bias transport rather than merely make it
  less informative, and weak faults near the noise floor cannot be
  recovered from evidence the diagnostic never contained.[^c6]
- Evaluated only on simulated dormant-actuator benchmarks; a single source
  (`kiet-2026`), unverified beyond the researcher's provisional check.

## Related

[[adaptive-submodularity]] · [[expected-information-gain]] · [[value-of-information]] · [[sprt]]

[^c1]: kiet-2026 — "We propose Evidence-Gated Matched-Pulse Transport, an intervention-based Bayesian procedure that couples fault localization with estimation of actuator effectiveness through a shared matched-response representation, thereby preserving diagnostic reliability while converting localized evidence into recovery-relevant uncertainty."
[^c2]: kiet-2026 — "Stage 1 selects the trajectory with the greatest expected reduction in taskweighted location risk per unit charge."
[^c3]: kiet-2026 — "The category Cq alone updates bt . If that category favors the targeted fault over nominal dynamics, zq also updates φt,j(q) ; otherwise the conditional effectiveness posterior is unchanged."
[^c4]: kiet-2026 — "Even a badly misspecified continuous severity likelihood cannot alter which diagnostic trajectory is selected, when Stage 1 stops, or which mechanism it reports, provided the categorical channel and location-side rules remain fixed."
[^c5]: kiet-2026 — "These quantities are estimated on calibration trajectories disjoint from evaluation data. The separation is necessary because reusing evaluation outcomes to choose bins or likelihood scales would make both detection and certificate metrics optimistically biased."
[^c6]: kiet-2026 — "Its matched-response transport is most reliable when response amplitude varies approximately monotonically with mechanism effectiveness. Saturation, deadbands, strong mechanism coupling, model mismatch, or state-dependent effects can violate this structure; the additional experiments show that transport may then become biased rather than merely less informative. Likewise, weak faults near the noise floor cannot be recovered by reusing evidence that the diagnostic never contained."
