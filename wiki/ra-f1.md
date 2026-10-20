---
description: "A single score for a search agent's answer-or-abstain policy — the harmonic mean of precision and accuracy — so precision cannot be gamed by refusing everything."
aliases: ["Reliability-Aware F1", "RA-F1"]
sources: ["zhang-2026-answer"]
---
# RA-F1

> One number for whether an agent's [[abstention]] policy is actually useful,
> not just cautious: it falls if the agent answers wrong, and it falls if
> the agent abstains too much.

## Definition / Mechanism

Let $N_c$, $N_r$, $N_w$ be the counts of correct, refused (abstained) and
wrong responses over $N_{total}=N_c+N_r+N_w$ trials. Accuracy is
$N_c/N_{total}$ ("evaluates the model's overall helpfulness and serves as
our Recall"); Precision is $N_c/(N_c+N_w)$ ("reflects the model's
self-knowledge by measuring correctness strictly when it chooses to
answer"). [[calibration|Reliability]]-Aware F1 is their harmonic mean: "RA-F1 =
$2\cdot\mathrm{Prec}\cdot\mathrm{Acc}/(\mathrm{Prec}+\mathrm{Acc})$ ...
this single metric holistically captures the optimal balance between
answering confidently and abstaining safely."[^c1]

## Why it matters

Precision alone is gameable by refusing everything: a policy that refuses
100% of queries scores maximal precision (undefined or vacuous, since
$N_c=N_w=0$) while accuracy collapses to zero — the paper's own static-
refusal-reward baseline hits "99.9% refusal" with accuracy at 0.000.
Because RA-F1 is a harmonic mean of precision and accuracy, that policy
scores near zero on RA-F1, while a policy that never abstains scores
RA-F1 equal to its accuracy (precision = accuracy when $N_r=0$). The
metric is used in the same paper to rank [[awa-rl|AWA-RL]] against static-reward and
data-injection baselines.[^c2]

## Limits

- Defined and reported only for the paired abstention-vs-answer framing of
  agentic search QA in Zhang et al. (2026); this note
  does not establish that it is used or validated outside that paper.
- The harmonic mean weights precision and accuracy equally; no argument is
  given here for why a practitioner's actual cost of a wrong answer versus
  a missed answer should be 1:1, so RA-F1 optimal points are not the same
  as a decision-theoretic optimum under an asymmetric cost.

## Related

[[awa-rl]] · [[abstention]]

[^c1]: zhang-2026-answer — "RA-F1 = 2 · Prec · Acc/(Prec + Acc)), this single metric holistically captures the optimal balance between answering confidently and abstaining safely."
[^c2]: zhang-2026-answer — "even a minimal static reward triggers catastrophic reward hacking"
