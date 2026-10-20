---
description: "A certificate-aware trigger that decides when to actively probe a latent noise parameter, by bounding the excess suboptimality a stale noise estimate would cause a certified policy."
aliases: ["VoNI", "Value of Noise Information"]
sources: ["yoon-2026-active"]
---
# Value of noise information

> A decision-maker running a certified policy does not need to know the
> physical noise floor exactly — only enough that its certificate still
> holds. VoNI prices *how wrong the certificate would be* if the maker kept
> acting on its current noise estimate instead of probing for a better one,
> and triggers probing only when that price exceeds the probe's cost.

## Definition / Mechanism

Yoon (2026) builds VoNI on top of Finite [[calibration|Reliability]]
Representations (FRR), a prior certificate that bounds the suboptimality of
a cell-constant policy by $2\varepsilon/(1-\gamma)$ whenever the physical
noise parameter $\theta=(\sigma_y,\sigma_u)$ used to calibrate the policy's
belief cover is the true one. When the cover is instead calibrated to a
current estimate $\hat\theta$ that may differ from the true $\theta$, the
excess loss beyond that certified floor is
$G_\varepsilon(b,\hat\theta;\theta) := [V^*_\theta(b) - V^{\bar\pi_{\hat\theta,\varepsilon}}_\theta(b) - 2\varepsilon/(1-\gamma)]_+$.
VoNI is this excess loss averaged over the current posterior $q$ on
$\theta$: $\mathrm{VoNI}_\varepsilon(b,\hat\theta;q) := \mathbb{E}_{\theta\sim q}[G_\varepsilon(b,\hat\theta;\theta)]$ — it is zero whenever the estimate keeps the
policy inside its certified tolerance for every $\theta$ the posterior puts
mass on, and positive only when posterior mass reaches parameter values the
current cover cannot cover.[^c1]

A bi-level decision maker computes, for each diagnostic probing action
$a^H$, the myopic expected reduction in VoNI net of the probe's cost,
$I^H_\varepsilon(b,q,a^H) := \mathrm{VoNI}_\varepsilon(b,\hat\theta;q) - c(a^H) - \mathrm{VoNI}^+_\varepsilon$,
and probes with the maximizing action only when
$\max_{a^H} I^H_\varepsilon(b_t,q_t,a^H) > 0$; otherwise it exploits the
current cell-constant policy. The rule rewards an action expected to
*reduce* VoNI, not one that reports a large VoNI value.[^c2]

On a closed-loop unicycle-model UGV with EKF innovation residuals (50 Monte
Carlo trials), VoNI detected an abrupt sensing-noise jump after
$126.48\pm2.58$ steps versus $185.08\pm7.32$ for a posterior-[[entropy]]
probing baseline (about 69% less delay) while probing on only
$13.93\pm1.16\%$ of steps versus $95.21\pm1.09\%$ for entropy (about 85%
fewer probes); on a gradual drift scenario VoNI's tracking error was
$0.1407\pm0.0150$ m versus $0.2394\pm0.0172$ m for entropy, using
$39.96\pm1.87\%$ of steps for probing versus $96.77\pm0.75\%$ (about 59%
fewer probes).[^c3]

Under a stationary, identifiable, persistently-exciting noise regime, the
paper proves the VoNI-guided estimate converges to the true parameter
almost surely and the induced policy loss converges to the ordinary FRR
approximation floor $2\varepsilon/(1-\gamma)$ (Theorem 2).[^c4]

## Why it matters

VoNI is a worked instance of "ask only if the answer would change what
gets done" (stall 2) built for a setting where the "decision" is a
*certified* one: the object being protected is not a generic utility but a
policy-[[sufficient-statistic|sufficiency]] guarantee, so the trigger compares posterior mass
against the certificate's own tolerance region rather than against raw
entropy — which is why it out-probes and out-detects an entropy-driven
trigger in the paper's experiments.

## Transfer

| | |
|---|---|
| **In its home field** | Control theory / POMDP reliability certification: a known physical noise floor $\theta$ yields a certified cell-constant policy via FRR; VoNI extends this to unknown $\theta$ by bounding the excess certificate gap a stale estimate can cause |
| **Here** | The general question of when an agent should probe (ask) for disambiguating information about a latent parameter versus act on its current belief |
| **What survives** | The structural test shared with [[value-of-information]] — probe only if the expected gain (here, certificate-gap reduction) exceeds the probe's cost — and the demonstrated payoff of pricing a *decision-relevant* quantity instead of raw posterior entropy |
| **What does not** | The certified bound itself: it presumes an existing policy-sufficiency guarantee (FRR) with a known Lipschitz sensitivity $L_V(\theta)$ and a computable cell cover; a domain without such a certificate has no $2\varepsilon/(1-\gamma)$ floor to measure excess loss against, and VoNI is not defined for it |

## Limits

- The bound and the convergence result (Theorem 2) hold only under
  well-specified, stationary, identifiable, persistently-exciting noise
  and an FRR certificate that holds uniformly near the true $\theta$;
  the paper itself flags the drift scenario as a tracking result, not a
  convergence one, once $\theta$ moves.[^c5]
- Numerical validation is a single simulated unicycle/EKF UGV system with
  a calibrated certificate-gap proxy rather than exact POMDP value
  iteration; the author's own discussion calls this "certificate-level
  validation rather than full-stack autonomous-vehicle validation."
- `yoon-2026-active` is a single arXiv preprint, unverified beyond the
  researcher's provisional check; the analytical bound (Theorem 1) is
  cited here only by what Definition 1 and the algorithm state, not by
  reproducing the theorem's proof.

## Related

[[value-of-information]] · [[task-readiness-certificate]] · [[sprt]] · [[expected-information-gain]]

[^c1]: yoon-2026-active — "Definition 1 (Value of Noise Information). Fix a decision tolerance ε > 0 and a posterior distribution q over the physical noise parameter. For belief b ∈ Breach and current estimate θ̂, define"
[^c2]: yoon-2026-active — "Thus a diagnostic action is chosen only when its expected reduction in the excess FRR certificate gap exceeds its immediate task-level cost. This rule does not reward a large VoNI value; rather, it values an action that is expected to reduce VoNI."
[^c3]: yoon-2026-active — "VoNI detects an abrupt sensing-noise jump substantially earlier than posterior-entropy probing, reducing post-jump detection delay by approximately 69%. Second, in the gradual drift scenario, VoNI achieves lower tracking error while using approximately 59% fewer probing actions than the posteriorentropy baseline."
[^c4]: yoon-2026-active — "Then: (i) θ̂t → θtrue almost surely; and (ii) for fixed FRR tolerance ε,"
[^c5]: yoon-2026-active — "For gradual drift, exact convergence to a fixed θtrue is not the correct claim. Under bounded drift and persistent excitation, the posterior tracks the moving physical noise floor with a nonzero steadystate error"
