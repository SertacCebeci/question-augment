---
description: "a synthetic benchmark parameter is accepted as ground truth only after it passes monotonicity, isolation and separability checks against held-out behavior."
aliases: ["construct validation of synthetic ground truth"]
sources: ["lu-2026"]
---
# Ground-truth admission test

> Writing a parameter into a generator's code does not make it ground truth;
> a constraint someone claims to have observed needs the same check before
> it is trusted.

## Definition / Mechanism

A synthetic agent's behavior is scripted by explicit parameters
$\theta_k\in[0,1]$; before any parameter is used as a ground-truth label for
scoring an inference method, it is swept over six levels with five random
seeds each (n=30 runs) and admitted only if three conditions hold together
on a signature metric $m_k$ held out from the parameter's own definition: C1
monotonicity — the parameter correlates with $m_k$ at Spearman ρ≥0.6 with no
significant non-monotone segment; C2 isolation — varying the parameter
induces no systematic drift in the signature metrics of the other
dimensions; C3 separability — between-level differences exceed seed-induced
variance. A parameter that fails any condition is reported as rejected or
non-identifiable and does not enter the benchmark.[^c1]

## Why it matters

All four trait dimensions in the source's benchmark passed admission, but
their distinguishable resolutions differed sharply on a held-out
identifiability probe: Skill was easiest to separate from behavior alone
(collision ratio r=.51) and Collector hardest (r=.82), meaning two agents
with nearly identical behavior can still hold far-apart Collector
parameters even though the parameter itself passed the admission test.[^c2]
The test converts [[recovery-postulate|recovery]] evaluation "from a weakly supervised,
difficult-to-falsify problem into a controlled and falsifiable one" — a
labeled parameter that has not passed it is not a safe stand-in for what an
inference method should be scored against.[^c3]

## Transfer

| | |
|---|---|
| **In its home field** | Psychometric construct validation (Cronbach & Meehl 1955; convergent/discriminant validity, Campbell & Fiske 1959) judges whether a measurement instrument tracks the construct it claims to, using correlations across independently collected human data. |
| **Here** | A *known-by-construction* generative parameter in a scripted synthetic agent, tested against behavior the same agent produces, before that parameter is used as the ground-truth label for scoring an external (e.g. LLM) reader. |
| **What survives** | The logic of convergent validity (C1, a consistent signature) and discriminant validity (C2, no bleed into other dimensions), and the general principle that a construct's truth-status is earned by a test, not asserted by definition. |
| **What does not** | Psychometric validation is normally run on independently sampled human respondents with unknown true scores; here the "true" parameter is already known by construction, so the test only screens out parameters whose own causal effect is too weak or entangled to be recoverable — it cannot detect a construct that is invalid for reasons outside the simulation (e.g. one that does not correspond to anything in real players). |

## Limits

The test is only meaningful because the parameter's true value is fixed by
the code that generated the behavior; it does not transfer to a setting
where the "true" trait is itself unobservable, which is the setting the
admitted parameters are ultimately meant to stand in for. The thresholds
(ρ≥0.6, the effect-size and discriminability cutoffs for C2/C3) were frozen
before observing any model response, but they are the source's own choice
of cutoff, not a result derived independently. Source lu-2026 is an
arXiv preprint (2026), not verified against a peer-reviewed venue.

## Related

[[behavior-inferred-player-profile]] · [[constraint-as-information]]

[^c1]: lu-2026 — "Each parameter is swept over L = 6 levels (θk ∈ {0, 0.2, . . . , 1.0}) with five random seeds per level (n = 30 runs per dimension), and admitted only if three conditions hold together, instantiating construct validation (Cronbach and Meehl 1955)"
[^c2]: lu-2026 — "Skill is easiest to identify (r = .51) and Collector hardest (r = .82): two agents with nearly identical behavior can hold collector parameters far apart."
[^c3]: lu-2026
