---
description: "Detects which reward feature is underspecified by the high variance of its values across demonstrations, then asks a targeted natural-language question naming that feature."
aliases: ["ASQ", "Ambiguity-Sensitive Querying", "variance-based underspecification detection"]
sources: ["merker-2026"]
---
# Ambiguity-sensitive querying

> A robot learning a reward from demonstrations treats the spread of each
> feature's observed values as a signal of which feature it should ask
> about next.

## Definition / Mechanism

Under a linear reward $R(s)=\theta^T\phi(s)$ learned from demonstrations
modelled as Boltzmann-rational with a *per-feature* rationality vector
$\beta$, a feature the demonstrator reliably attends to ($\beta_i$ high)
produces tightly clustered values across demonstrations, while a feature
left unattended ($\beta_i\approx 0$) produces high variance — and the
likelihood is flat in $\theta_i$, so no amount of the same data resolves
it: "features that are consistently optimized show little variation
across demonstrations, while features that are underspecified vary
widely."[^c1]

[[efe-planning-as-variational-inference|Ambiguity]]-Sensitive Querying (ASQ) turns this into a selection rule.
Given the empirical per-feature variance $\sigma_i^2$ of an initial
demonstration set, it treats "which features are underspecified" as
Bayesian model selection over subsets $\phi_{hyp}\subseteq\phi$: "We frame
detection as a Bayesian model selection problem," scoring each hypothesis
by the product of per-feature likelihoods $P(\sigma_i^2\mid o_i,\phi_i)$
and picking the maximum-a-posteriori set, $\phi_{under}=\arg\max_{\phi_{hyp}}P(\phi_{hyp}\mid\{\sigma_i^2\})$.[^c2]

The raw variance is uninterpretable alone (scale differs per feature), so
ASQ calibrates it against reference distributions built by simulating
trajectories under policies that include or exclude each feature from
their objective; the authors report these empirical sample variances are
"approximately Chi-squared distributed, which facilitates subsequent
likelihood computation."[^c3]

Having selected $\phi_{under}$, the robot does not just re-query
generically: it generates a fixed-template natural-language explanation
naming the uncertain features and asks for demonstrations that attend to
them — "we generate a natural language explanation that communicates
which features the robot is uncertain about," which the authors frame as
"a causal intervention" that separates genuine indifference from
incidental neglect.[^c4]

In simulation (a 7-DoF manipulation task, JacoRobot), this selection rule
beats baselines that query about random features: "ASQ outperforms the
random baselines in all four conditions... ASQ recovers reward more
quickly and achieves higher final performance."[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| robot-learning | Ambiguity-Sensitive Querying (ASQ) | exact |
| robot-learning | variance-based underspecification detection | close — names only the detection half of the pipeline, not the explanation-query step |

## Why it matters

This is a formal trigger for stall 2 (which axis first) that needs no
manually declared uncertainty over features: the axis to ask about is
read off the *shape* of the answers already given, not asked for
separately. It also couples selection to formulation directly — the
selected feature becomes the content of the question, named in the
explanation the demonstrator receives.

## Transfer

| | |
|---|---|
| Home field | Bayesian model selection (statistics) |
| Here | choosing which reward feature/axis needs more human supervision from the variance pattern of past answers |
| What survives | scoring candidate "underspecified" hypotheses by their likelihood under calibrated reference distributions and picking the MAP set |
| What does not | any guarantee that the reference distributions (built by simulating synthetic policies) match a real demonstrator's variance; the [[possible-worlds|hypothesis space]] is exponential in the number of features, so the method needs an external (LLM-supplied) prior to stay tractable |

## Limits

The variance signal cannot on its own distinguish "the human doesn't care
about this feature" ($\theta_i^*\approx0$) from "the human didn't attend
to it" ($\beta_i\approx0$) — this is exactly why the method still needs a
follow-up query rather than reading $\theta^*$ off the variance directly.
The reference distributions are estimated from simulated policies, not
from the actual demonstrator, and the reward is assumed linear in a
pre-given feature set $\phi$; a feature the wrong choice of $\phi$
omitted is invisible to the whole pipeline.

## Related

[[value-of-information]] · [[target-ambiguity-triggers-clarification]] · [[clarification-benchmarks]] · [[expected-information-gain]]

[^c1]: merker-2026 — "features that are consistently optimized show little variation across demonstrations, while features that are underspecified vary widely."
[^c2]: merker-2026 — "We frame detection as a Bayesian model selection problem."
[^c3]: merker-2026 — "we empirically find that their sample variances are approximately Chi-squared distributed, which facilitates subsequent likelihood computation."
[^c4]: merker-2026 — "we generate a natural language explanation that communicates which features the robot is uncertain about"
[^c5]: merker-2026
