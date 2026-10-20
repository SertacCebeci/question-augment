---
description: "Formalizes clinical diagnosis as a single POMDP whose action space unifies patient questioning, exam-ordering tool calls and a terminal diagnosis, with noise injected into both observation channels."
aliases: ["interactive diagnosis POMDP", "MedExAgent environment"]
sources: ["gao-2026-medexagent"]
---
# Interactive diagnosis POMDP

> Asking the patient, ordering a test, and committing to a diagnosis are
> three branches of one action space, not three separate tasks — and the
> patient's and the lab's answers are both noisy.

## The framework

Gao, Zhou, Li, Zhao & Liu (2026) formalize
interactive clinical diagnosis as a POMDP $(S, A, T, \Omega, O, R)$. The
[[possible-worlds|state space]] $S=D$ is the set of possible diseases, one ground-truth disease
$d$ sampled per episode; the transition is deterministic (the disease does
not change within an episode). The action space unifies three action types
in one policy: $A = A_{ask} \cup A_{exam} \cup \{a_{dx}\}$ — a free-form
question to the patient, an exam ordered as a tool call, or a terminal
diagnosis.[^c1]

The observation space is likewise split, $\Omega = \Omega_{conv} \cup
\Omega_{exam}$: a patient reply follows an $A_{ask}$ action, an exam result
follows an $A_{exam}$ action. Both channels are corrupted by a systematic
noise model — seven patient-noise types (e.g., misreported symptom location)
and three exam-noise types (e.g., contaminated lab results) — each applied
independently in the observation function $O(\omega\mid d,a)$ with a fixed
probability $p_{conv}$ or $p_{exam}$. Prior benchmarks and agents cover only
part of this space: questioning-only, exam-ordering-only, or noise-free.[^c2]

MedExAgent, an 8B model, is trained on this environment in two stages:
supervised fine-tuning on synthetic doctor-patient conversations structured
after the five-stage Calgary-Cambridge interview model, then DAPO
reinforcement learning against the composite reward of Equation 3 (see
[[exam-cost-reward]]). On the held-out, out-of-distribution AgentClinic-MedQA
benchmark, MedExAgent-8B "matches the strongest medical specialist in the
comparison at roughly 9× smaller parameter count."[^c3]

## Transfer

| | Home field (control theory / POMDP planning) | Here |
|---|---|---|
| Formalism | POMDP: hidden state, an observation function corrupting what the agent sees, a single action space the policy optimizes over | Hidden state is the patient's disease; the action space merges an [[epistemic-actions|epistemic action]] (ask), an information-costly tool action (order exam), and a terminal action (diagnose) into one policy |
| Survives | State/observation/action split; noise as part of the observation function rather than a separate error model; training one policy over the whole action space instead of one per action type | The unification itself — no held-out subroutine for "when to ask vs. when to test vs. when to stop" |
| Does not survive | An exact, known transition/observation model a [[planner-dynamic-stopping|planner]] can solve against | No POMDP solver is run; the policy is an LLM trained by SFT+RL against a reward, not computed against $O$ or $T$ in closed form |

## Limits

- The disease is assumed invariant over the episode and the observation
  function is assumed stationary — the paper names this explicitly as a
  simplification real critical-care patients can violate.
- Both the patient and the noise-injection are simulated (LLM patient
  simulators, PatientSim personas, a synthetic noise model); no validation
  against real patients or physicians is reported.
- The framework is one 2026 preprint's own formalization, read from the
  archived text extract only ([?] unverified as of this draft).
- English-only training and evaluation data.

## Related

[[task-alignment-pomdp]] · [[epistemic-decision-process]] · [[exam-cost-reward]] · [[value-of-information]]

[^c1]: gao-2026-medexagent — "we aim to address this gap by formalizing clinical diagnosis as a Partially Observable Markov Decision Process (POMDP) with three action types: questioning the patient, ordering medical exams as tool calls, and issuing a diagnosis."
[^c2]: gao-2026-medexagent — "We consider seven types of patient noises and three types of exam noises detailed in Table 6. Each type of noise is applied independently with a fixed probability pconv or pexam on patient responses or exam results."
[^c3]: gao-2026-medexagent — "At 8B parameters, MedExAgent matches the strongest medical specialist in the comparison at roughly 9× smaller parameter count."
