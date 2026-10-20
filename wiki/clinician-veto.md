---
description: "Three conditions a clinician survey says autonomous prescribing needs before it is trusted — a calibrated confidence gate, uncertainty-differentiated disclosure, transparent reasoning."
aliases: ["clinician's veto", "minimum architectural requirements for autonomous prescribing", "calibrated action-gated confidence threshold"]
sources: ["larocco-2026"]
---
# Clinician's veto

> An autonomous prescribing agent is not trusted to act just because its
> aggregate accuracy clears a bar. Clinicians surveyed by
> LaRocco et al. (2026) want it gated per-case by a
> calibrated confidence threshold, want the escalation interface's content
> to depend on *why* the agent is uncertain, and only accept personal
> liability when that reasoning is exposed.

## Definition / Mechanism

Three conditions, argued to be jointly minimal for safe autonomous
prescribing and each validated by a survey of 136 U.S. prescribing
clinicians (H1–H3): (1) a calibrated, action-gated confidence threshold
that halts the agent and routes the case to clinician review below the
threshold; (2) [[uncertainty-decomposition|differentiated uncertainty communication]] — the escalation
interface's content depends on whether the uncertainty is epistemic (model
ignorance) or aleatoric (irreducible clinical [[efe-planning-as-variational-inference|ambiguity]]); (3) inferential
transparency — exposing the reasoning behind an autonomous action so
liability can be allocated. Support for full autonomy was near-absent:
opposition exceeded 83% for all new prescriptions and high-risk refills
across both complex and non-complex patients, with meaningful support only
for low-risk refills.[^c1]

(H1) 67.4% of clinicians chose the strongest endorsement — "I would not
permit AI agents to prescribe drugs without it" — for a calibrated
confidence-based escalation mechanism (one-sided binomial vs. 0.5,
p < 0.001), and rated an agent "to be significantly worse than the
calibrated agent (mean 3.71, SD 1.07; p < 0.001) relative to an agent with
no escalation mechanism at all" when the escalation mechanism was
uncalibrated (mean 2.06, SD 1.05).[^c2]

(H2) Preferred escalation content shifts with uncertainty source: "While
71.0% preferred a competing-options summary and 15.3% preferred [[abstention]]
… in aleatoric scenario, the distribution shifted significantly: abstention
rose to 46.9% and competing-options dropped to 36.9% (p < 0.001 for both)"
in the epistemic scenario, both contrasts significant after
Holm–Bonferroni correction. The epistemic scenario did not produce a
majority for abstention — preference split between abstention and
competing-options.[^c3]

(H3) Across four adverse-outcome vignettes varying the agent's confidence
and whether it escalated, "mean responsibility assigned to the
organization was significantly higher than that assigned to the
individuals in all four scenarios" (Holm-adjusted p < 0.005 for three,
p = 0.017 for the fourth). When the agent escalated and the clinician
concurred, "overseeing clinicians were assigned less responsibility when
the AI had been highly confident than when it had been low-confident
(Δmean = −0.16, p < 0.05), suggesting that clinicians accept additional
responsibility when inferential transparency enabled them to make a
substantive judgment under acknowledged uncertainty." Patients were
assigned the least responsibility in every scenario despite documented
consent.[^c4]

## Why it matters

The three conditions together push an "autonomous" agent back toward a
heavily supervised decision-support tool: it must stop and ask a human
below a confidence threshold, must change what it discloses at that
handoff by uncertainty type, and must show its reasoning before anyone
will accept blame for its errors. For this wiki, the framework fixes *who
answers* (a human, gated by confidence) and *what the answerer commits to
saying* (competing options vs. abstention, chosen by uncertainty type) as
one coupled design, validated by stated preference rather than derived
from a formal model.

## Limits

- All three findings are **stated preference** from a hypothetical-scenario
  survey (N = 136 U.S. prescribing clinicians, self-selected via
  multi-institutional email lists), not measured behaviour with a deployed
  autonomous prescriber; no real-world escalation or liability outcome was
  observed.
- The sample skews toward clinicians already familiar with AI (96.3%
  generative-AI familiarity, 86% current AI use in their role), which may
  overstate comfort with the calibrated-escalation framing relative to a
  less AI-exposed population.
- H2's headline contrast (aleatoric → competing-options, epistemic →
  abstention) holds directionally, but the epistemic scenario itself splits
  clinicians rather than producing a majority for abstention — the
  disagreement inside the field is part of the finding, not noise around
  it.
- Single domain (U.S. prescribing) and a single 2026 arXiv preprint, not
  yet peer-reviewed `[?]`; whether the same three conditions generalize to
  other high-stakes autonomous-agent settings is not tested here.
- No consensus threshold-setting authority: 59.5% of respondents favoured
  some organizational body over the AI company (5.3%) or the individual
  clinician for setting the confidence threshold itself, so condition (1)
  names a gate without settling who calibrates it.

## Related

[[uncertainty-decomposition]] · [[value-of-information]] · [[bayesian-self-escalation]] · [[detect-verify-escalate-pipeline]]

[^c1]: larocco-2026 — "Results show that opposition exceeds 83% for all new prescriptions and high-risk refills across both patient types, with the only non-trivial support shown for low-risk refills."
[^c2]: larocco-2026 — "67.4% of clinicians chose the strongest endorsement (“To a great extent — I would not permit AI agents to prescribe drugs without it”)."
[^c3]: larocco-2026 — "While 71.0% preferred a competing-options summary and 15.3% preferred abstention (Fig. 4) in aleatoric scenario, the distribution shifted significantly: abstention rose to 46.9% and competing-options dropped to 36.9% (p < 0.001 for both)"
[^c4]: larocco-2026 — "mean responsibility assigned to the organization was significantly higher than that assigned to the individuals in all four scenarios above"
