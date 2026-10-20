---
description: "A dedicated critic trained on operators' accept/override feedback, gating action execution at a precision-calibrated threshold, beats using the actor's own confidence for the same gate."
aliases: ["selective LLM autonomy", "critic-based action gating", "SFT critic versus confidence baseline"]
sources: ["arxiv-2604-23855"]
---
# Critic-gated autonomy

> Whether to let an action run is not read off the actor's own confidence;
> a second model trained on operators saying yes or no to the actor's past
> proposals gates it better.

## Definition / Mechanism

Borovkov et al. (2026) separate the model that
proposes an action from the model that decides whether to run it. A
policy π<sub>θ</sub>(a | s) proposes the next UI action; a critic
c<sub>ϕ</sub>(s, a) ∈ [0, 1], a distinct network, scores that proposal. "Execution is regulated by threshold(s) τ,
optionally stratified by action importance. The policy proposes â ∼
π<sub>θ</sub> (· | s), the critic computes c<sub>ϕ</sub> (s, â), and the
action is executed only when c<sub>ϕ</sub> (s, â) ≥ τ; otherwise control
is handed to a human." The critic gate applies only to actions flagged
critical (sending a message, terminating an interaction); non-critical
actions run ungated.[^c1]

The threshold is not fixed at deployment; it is set to a business target
and then re-fit as data accrues: "We calibrate τ to meet business
precision requirements on critical actions. Among critic-approved
actions, the fraction that operators would accept must exceed a target,
for example 0.9, estimated from copilot feedback. We initialize τ
offline on held-out copilot data, then refine it online in the
calibration substage without sweeping many thresholds."[^c2]

The critic itself is [[abstention|not a thresholded reading of the
actor's own uncertainty]] — it is trained as a separate supervised
classifier on the actor's own history of accepted and overridden
proposals, then compared offline against the alternative of just using
the actor's confidence score as the gate. "The results in Table 7 show
that the critic trained with SFT consistently outperforms the
confidence-based baseline. Precision improves by 3.84%, and F1 increases
by 3.03%, while recall remains at a comparable level with only a 0.10 %
difference. These findings suggest that learning from historical accept
and reject feedback produces a more reliable execution signal than
relying on the action model's raw confidence alone."[^c3]

Deployed this way — policy trained on logged traces, then a copilot stage
that harvests accept/override labels, then critic-gated execution — the
system "reduces AAT [average active time] from 227.37 s to 139.15 s, a
39% decrease that is statistically significant at p < 0.05... In
automation mode, the system fully automates 45% of sessions," with
resolution correctness unchanged from the human-only baseline.[^c4]

## Why it matters

On stall 2 (when does an answerer commit versus defer), the standard
move a reader of this wiki already has is a post-hoc threshold cut on a
score the model produces anyway — its own [[abstention|confidence,
entropy, or margin]]. This source measures the alternative directly, in
production rather than on a static benchmark: training a *second* model
specifically on the record of when the first model's proposals were
accepted or overridden, and gating on that model's score instead, wins
on precision and F1 at matched recall. The gap is attributed to what the
signal is trained on — realized outcomes of past proposals — rather than
to anything about model scale or architecture.

## Limits

- The reported gap (+3.84% precision, +3.03% F1) is one offline
  comparison on one deployment's historical logs with a single base
  model (Qwen2.5-Instruct-7B); the extract gives no measure of how the
  gap moves with the size of the accept/override log the critic is
  trained on, or with a larger or smaller base model.
- The critic gate is evaluated only for actions the system labels
  critical; non-critical actions are not compared under both gating
  schemes, so the finding does not establish that a learned critic beats
  confidence gating for actions with lower stakes or thinner feedback.
- Threshold calibration targets a business precision number chosen by
  the deployer (e.g., "0.9 accept rate"), not a statistical guarantee;
  the paper reports online monitoring and tightening the threshold when
  slice-level risk appears, but no formal coverage bound on the gate.

## Related

[[abstention]] · [[learned-deferral]] · [[clinician-veto]] · [[calibration]]

[^c1]: arxiv-2604-23855 — "Execution is regulated by threshold(s) τ , optionally stratified by action importance. The policy proposes â ∼ πθ (· | s), the critic computes cϕ (s, â), and the action is executed only when cϕ (s, â) ≥ τ ; otherwise control is handed to a human. The critic is evaluated only for critical actions, while noncritical ones may be executed without this gating."
[^c2]: arxiv-2604-23855 — "We calibrate τ to meet business precision requirements on critical actions. Among criticapproved actions, the fraction that operators would accept must exceed a target, for example 0.9, estimated from copilot feedback. We initialize τ offline on held-out copilot data, then refine it online in the calibration substage without sweeping many thresholds."
[^c3]: arxiv-2604-23855 — "The results in Table 7 show that the critic trained with SFT consistently outperforms the confidencebased baseline. Precision improves by 3.84%, and F1 increases by 3.03%, while recall remains at a comparable level with only a 0.10 % difference. These findings suggest that learning from historical accept and reject feedback produces a more reliable execution signal than relying on the action model’s raw confidence alone."
[^c4]: arxiv-2604-23855 — "Compared with a human-only baseline, automation-enabled selective operation reduces AAT from 227.37 s to 139.15 s, a 39% decrease that is statistically significant at p < 0.05, as shown in E1, Table 3. Resolution correctness remains on par with the baseline, showing no statistically significant difference. In automation mode, the system fully automates 45% of sessions."
