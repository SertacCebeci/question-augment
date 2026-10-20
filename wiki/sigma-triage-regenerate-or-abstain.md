---
description: "A three-way rule — accept, regenerate with constraint feedback, or abstain — gated by thresholds on ensemble uncertainty and constraint violation for a ranked candidate answer."
aliases: ["σ-triage", "sigma-triage", "two-pass inference loop", "regenerate-or-abstain policy"]
sources: ["manchingal-2026"]
---
# Sigma-triage regenerate-or-abstain policy

> After ranking candidate answers, do not always commit to the top one: read its own uncertainty and constraint state off first, and let that decide between committing, asking once more, or refusing.

## Definition / Mechanism

Given the top-ranked first-pass candidate y1*, its ensemble-uncertainty score σ and its (deterministic) constraint-violation score C are checked against two thresholds θσ < θabstain: if σ ≤ θσ ∧ C = 0, accept action(y1∗ ) = regenerate if σ ≤ θa ∨ C > 0, abstain if σ > θa, where σ = σquality(y1∗), C = Econstraint(y1∗). On regenerate, the constraint violations are turned into natural-language feedback and used to draw a second batch of candidates, which are pooled with the first, re-ranked, and re-checked for a final accept/abstain decision.[^c1]

## Known as

| Field | Name there | Relation |
|---|---|---|
| machine-learning (this paper) | σ-triage | exact |
| machine-learning (this paper) | two-pass inference loop | exact |
| this wiki (paraphrase) | regenerate-or-abstain policy | close |

## Why it matters

The regenerate step's effect is task-dependent rather than uniformly helpful: on TravelPlanner (Qwen-only generator pool, used to isolate the feedback effect from candidate diversity), it improves pass@1 from 74.0% to 80.0% (+6.0 pp). On TACO (deconfounded), two-pass is neutral (88.6%); on GSM8K, it is mildly counterproductive (−1.7 pp) precisely because the generator has memorised the answer and feedback distracts retrieval.[^c2]

The abstain branch is likewise task-dependent as a *[[abstention|selective-prediction]]* signal: abstaining on 40% of problems raises pass@1 from 28.0% to 36.7% (+8.7 pp); on MuSR, σ does not signal correctness (AUROC 0.44), and the verifier is honest about where it cannot triage rather than offering an unreliable signal.[^c3]

## Limits

The policy's three branches assume the constraint checker Econstraint is exact and the uncertainty estimate is task-appropriate — both fail differently: regeneration backfires when the answer is already memorised rather than under-determined (GSM8K), and the abstain branch is useless when σ does not track correctness (MuSR, AUROC 0.44). The paper frames this as σ-triage detecting *which regime* a task is in rather than as a universal stopping rule, so the policy needs a per-task check of whether σ correlates with correctness before it is trusted — this note's own inference from the reported cross-task spread, not a claim the paper states as a precondition.

## Related

[[heterogeneous-lora-ensemble-uncertainty]] · [[vote-margin-gate]] · [[task-readiness-certificate]] · [[agentabstain-paired-benchmark]]

[^c1]: manchingal-2026
[^c2]: manchingal-2026 — "on TravelPlanner (Qwen-only generator pool, used to isolate the feedback effect from candidate diversity), it improves pass@1 from 74.0% to 80.0% (+6.0 pp). On TACO (deconfounded), two-pass is neutral (88.6%); on GSM8K, it is mildly counterproductive (−1.7 pp) precisely because the generator has memorised the answer and feedback distracts retrieval"
[^c3]: manchingal-2026 — "abstaining on 40% of problems raises pass@1 from 28.0% to 36.7% (+8.7 pp); on MuSR, σ does not signal correctness (AUROC 0.44), and the verifier is honest about where it cannot triage rather than offering an unreliable signal."
