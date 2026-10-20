---
description: "Classify a follow-up-question failure as Knowledge Gap, Capability Limit, or Evaluation Noise before it can update a system, so only a genuinely repairable gap becomes a constraint."
aliases: ["collective attribution", "repairability screening"]
sources: ["yan-2026"]
---
# Repairability attribution

> A failed interaction is not automatically evidence of a knowledge gap —
> screening it against what actually could have caused it decides whether
> it belongs in the next update at all.

## Definition / Mechanism

Yan et al. (2026) classify every failure their simulated
follow-up interaction surfaces into one of three causes before deciding
whether it may drive a revision: "The Attributor compares the human
handling process, the simulated dialogue, and the Verifier's evidence...
and classifies failures by whether the Skill can repair them: Knowledge
Gap, where a stable fact present in the human reference was omitted or
answered incorrectly; Capability Limit, covering permission and tooling
restrictions, poor delivery, and infrastructure faults; and Evaluation
Noise, covering false negatives and scenario distortion. Only Knowledge Gap
is projected into the feedback; the remaining two classes are isolated
from the revision loop."[^c1]

Before attribution runs, the two sides of the interaction are scored
separately, so that a failure caused by the simulated user never raising a
topic is not confused with a failure caused by the agent answering it
badly: "SkillEvo evaluates the simulator side and the agent side
separately, rendering responsibility separable: a failure occurring where
an intent was never raised is attributed to simulation distortion rather
than to the agent's Skill."[^c2]

## Why it matters

An asking-and-revising loop that treats every failure as a constraint on
its next update will fold noise and out-of-scope failures into what it
"knows," producing the knowledge bloat and factual over-generalization the
same paper's governance layer has to repair afterward. Screening by
repairability is what keeps a follow-up-question failure from becoming a
false constraint — a version, for an iterated feedback loop, of the
general requirement that a signal must actually narrow the target concept
before it counts as an answer.

## Limits

- Requires a ground-truth human reference per episode (the paper works
  from real, human-resolved support tickets); the three-way split is not
  shown to work without one.
- The classification is itself made by an LLM-based Attributor plus
  Verifier; the paper's only [[calibration|reliability]] check is ≈90% Verifier–human
  agreement on a sampled subset, not a check on the Attributor's own
  three-way call.
- The taxonomy (Knowledge Gap / Capability Limit / Evaluation Noise) is
  built for a technical-support Skill-maintenance setting; whether it
  covers the failure modes of other feedback-driven asking loops is
  untested here.

## Related

[[self-renewing-feedback-gradient]] · [[clarification-benchmarks]]

[^c1]: yan-2026
[^c2]: yan-2026
