---
description: "An interview orchestrator ranks candidate symptom clusters by current estimated severity times inverse scorer confidence, and routes the interviewer to the top-ranked cluster each turn."
aliases: ["symptom priority ranking", "severity-confidence priority score"]
sources: ["gong-2026"]
---
# Confidence-weighted symptom prioritization

> Once a depression-screening agent has moved past its precomputed
> openers, an orchestration layer decides the next axis live: rank the 7
> symptom clusters by a score combining how severe the symptom is
> estimated to be and how unsure the scorer still is about it, and route
> the interviewer to the top of that list.

## Definition / Mechanism

In Gong & Guecha (2026)'s multi-agent screening system, a
scorer agent re-estimates all 21 BDI-II symptom scores and per-symptom
confidence after every turn; the orchestration layer "groups the 21
BDI-II symptoms into seven thematic clusters and ranks them based on a
[[priority-scored-candidate-ranking|priority score]] combining current estimated severity and inverse
confidence to direct the interviewer toward the least diagnosed symptoms
at each turn," then "embeds cluster-specific instructions into the
interviewer's prompt dynamically."[^c1]

The axis is re-scored after every turn using the scorer's live output, so
selection tracks the same running belief state the orchestrator also uses
to decide when to stop (four stopping criteria on turn count, per-symptom
confidence, score stability and coverage). No explicit information measure
([[entropy]], [[mutual-information|mutual information]]) is computed; severity and inverse confidence
are heuristics read directly off the scorer agent's own 0-3 and 0-1
outputs. This mechanism, together with the [[precomputed-dialogue-tree-routing|dialogue tree]] and
[[calibration|reliability]]-weighted aggregation, is credited with a hybrid-configuration
ADODL of 0.9063 (2nd place among 21 teams).[^c2]

## Why it matters

This is a second, independent answer to stall 2 on the same system: after
the precomputed tree runs out, live axis selection is not information-
theoretic but a hand-designed heuristic priced directly from the scorer's
own uncertainty output — "inverse confidence" stands in for the entropy or
mutual-information term the wiki's other stall-2 rows compute formally. It
is a case where the acting axis-selection criterion and the stopping
criterion draw on the same live confidence estimate rather than on two
separate objectives.

## Limits

- "Confidence" here is the scorer LLM's self-reported 0-1 number per
  symptom, not a calibrated probability; the paper reports no calibration
  check, so the priority score's relation to true diagnostic uncertainty
  is unverified.
- The severity × inverse-confidence combination rule is not derived or
  compared against an information-theoretic alternative (e.g.
  [[expected-information-gain]] or [[adaptive-submodularity]]'s marginal
  gain) within the paper; the only comparison offered is against a simpler
  single-model prototype and a paid-interviewer baseline, both of which
  also used priority-based routing to some degree, so the isolated
  contribution of this scoring rule is not measured.[^c3]
- Reported only on one task (eRisk 2026 Task 1) and 20 personas.

## Related

[[precomputed-dialogue-tree-routing]] · [[expected-information-gain]] · [[adaptive-submodularity]] · [[value-of-information]]

[^c1]: gong-2026 — "it groups the 21 BDI-II symptoms into seven thematic clusters and ranks them based on a priority score combining current estimated severity and inverse confidence to direct the interviewer toward the least diagnosed symptoms at each turn"
[^c2]: gong-2026 — "Hybrid Run 3 achieved an ADODL of 0.9063, ranking 3rd among all complete-submission runs and placing DS@GT 2nd among the 21 teams overall"
[^c3]: gong-2026 — "ranks them based on a priority score combining current estimated severity and inverse confidence"
