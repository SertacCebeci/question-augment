---
description: "Noisy gripper telemetry is fused into a discrete execution-outcome label that gates a bounded, deterministic policy: retry once, finalize, or escalate to the user."
aliases: ["Watchdog", "physical agentic loop", "execution-state monitoring", "bounded recovery policy"]
sources: ["arxiv-2604-07395"]
---
# Watchdog outcome escalation

> A grasp is not a single shot: it is a tool call whose outcome must be read off the hardware before the agent is allowed to decide anything.

## Definition / Mechanism

Wang et al. (2026) wraps an unmodified language-guided
grasping primitive (ForceSight) with two layers instead of retraining it.
**Watchdog** turns continuous, noisy execution feedback — gripper effort,
closure, contact and micro-lift cues — into one of six discrete labels
$S=\{$SUCCESS, EMPTY, SLIP, WEAK, STALL, TIMEOUT$\}$ using "contact-aware
fusion and temporal stabilization": outcome emission "requires a short
settle window where effort/closure cues remain consistent," and micro-lift
evidence rejects contact-only false positives. A **bounded decision
policy** $\pi:(S,G)\to U$ then maps the label (plus goal $G$ and an optional
semantic-verification signal) to one of three actions,
$U=\{$FINALIZE, RETRY/RESELECT, WAIT_CLARIFY$\}$, under a fixed rule set:
"SUCCESS: output FINALIZE if semantic evidence is consistent (when
enabled); otherwise output WAIT_CLARIFY. EMPTY: output RETRY/RESELECT if
the retry budget remains; otherwise output WAIT_CLARIFY." SLIP, WEAK,
STALL and TIMEOUT finalize under the conservative default, "with optional
escalation to WAIT_CLARIFY when the next action depends on user intent."[^c2]
The retry budget is one automatic retry by default, so "the system always
transitions to either FINALIZE or WAIT_CLARIFY after a finite number of
attempts, preventing unbounded execution in ambiguous or failure-prone
scenes." [[clarification-request|Asking]] here is one branch of an
outcome-conditioned switch, not a separate module: the same event stream
that gates a retry also gates an escalation, and both are bounded by the
same budget.

## Why it matters

Across seven real-robot scenarios (ambiguity, distractors, domain shift,
induced empty grasps, infeasible targets, mid-task goal revision), the
wrapped system holds high success where the open-loop baseline collapses:
"Table II shows that open-loop execution performs reasonably under trivial
single-target conditions, but degrades substantially under ambiguity and
distractor interference. In contrast, the proposed agentic loop maintains
high success rates across the structured scenarios, consistent with the
benefits of explicit execution-state monitoring and bounded recovery."[^c4]
A component ablation isolates the two layers: removing Watchdog or the
semantic perception conditioning drops success under ambiguity, and
disabling retry drops it too, "confirming that bounded recovery contributes
beyond improved target selection alone." The escalation trigger itself
is measured, not asserted: on 50 controlled empty-grasp trials Watchdog
correctly labeled EMPTY 43 times and mislabeled 5 of 50 successful grasps
as EMPTY, so the signal that decides retry-vs-finalize-vs-clarify carries a
known, nontrivial error rate.[^c6]

## Limits

- The policy is hand-set and conservative, not learned or tuned: EMPTY gets
  exactly one retry, every other failure label finalizes by default, and
  escalation to WAIT_CLARIFY beyond that is optional and scenario-specific
  — the paper flags label-specific recovery (regrasp after SLIP,
  re-approach after WEAK) as future work, not evaluated here.
- Validated on one manipulation primitive (ForceSight, unmodified), one
  platform (Hello Robot Stretch, eye-in-hand D405), and 180 final-system
  trials across ten trials per configuration — not a claim about
  escalation policies for other primitives or embodiments.
- Watchdog's own error rate (5/50 false EMPTY on successful grasps) is
  unverified against downstream effect: the paper does not report how often
  a false EMPTY caused an unnecessary retry or escalation.
- What happens after WAIT_CLARIFY — how the user's answer is parsed and
  re-injected as a revised goal $G$ — is asserted architecturally (Agent
  Core reprocesses the instruction) but not measured as its own step.

## Related

[[clarification-request]] · [[decision-centric-design]] · [[compound-ai-systems]] · [[embodied-instruction-abstention-taxonomy]] · [[robot-response-mode-taxonomy]]

[^c2]: arxiv-2604-07395 — "SUCCESS: output FINALIZE if semantic evidence is consistent (when enabled); otherwise output WAIT CLARIFY."
[^c4]: arxiv-2604-07395 — "Table II shows that open-loop execution performs reasonably under trivial single-target conditions, but degrades substantially under ambiguity and distractor interference. In contrast, the proposed agentic loop maintains high success rates across the structured scenarios, consistent with the benefits of explicit execution-state monitoring and bounded recovery."
[^c6]: arxiv-2604-07395 — "For empty-grasp cases, the watchdog correctly detected EMPTY in 43 out of 50 trials. For successful grasps, 5 out of 50 trials were incorrectly classified as EMPTY."
