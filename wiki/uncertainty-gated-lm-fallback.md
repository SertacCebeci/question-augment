---
description: "An RL policy's total MC-Dropout uncertainty gates, at each step, whether the trained policy acts alone or a small LM overrides its action."
aliases: ["ASK", "Adaptive Safety through Knowledge", "uncertainty-gated language assistance"]
sources: ["arxiv-2604-02226"]
---
# Uncertainty-gated LM fallback

> Query the language model only where the trained policy is out of its depth.

## Definition / Mechanism

Adaptive Safety through Knowledge (ASK) wraps a[^s1]
trained RL policy $\pi_\theta$ with a small language model $G_\phi$ that
intervenes only when the policy is uncertain: "We introduce Adaptive
Safety through Knowledge (ASK), which combines smaller LMs with trained RL
policies to enhance OOD generalization without retraining. ASK employs
Monte Carlo Dropout to assess uncertainty and queries the LM for action
suggestions only when uncertainty exceeds a set threshold." At each
observation $o$, $N=100$ dropout-enabled forward passes through $\pi_\theta$
give an epistemic estimate $U_e(o)$ and an aleatoric estimate $U_a(o)$; "If
the total uncertainty exceeds a predefined threshold $\tau$, we override the
agent's action by querying $G_\phi$ with a prompt $Pr$ and the current
observation to obtain an alternative action $G_\phi(Pr, o)$." The
prompt includes the policy's own choice as an "autopilot suggestion," so
the LM validates or overrides it rather than planning from scratch; a
malformed LM output falls back to the policy's action, and the LM is never
fine-tuned. $\tau$ is fixed per LM size in advance (Bayesian optimization
over held-out episodes), not adapted online.

The mechanism is measured by two step-level rates rather than only the
episode reward: "Intervention rate (IR)… measures the proportion of steps
where uncertainty exceeds the threshold $\tau$ and the LM is consulted… A
low intervention rate indicates that the agent operates autonomously, while
a high rate suggests frequent uncertainty requiring assistance." "Overwrite
rate (OR)… measures how often the recommended action differs from the
original policy's suggestion when consulted… A high overwrite rate
indicates that the LM frequently disagrees with the policy in uncertain
states, suggesting it offers complementary reasoning rather than redundant
confirmation." IR prices the computational cost of the gate; OR prices
whether a consulted LM is actually contributing a different action rather
than rubber-stamping the policy.

## Why it matters

On FrozenLake maps of the size the policy was trained on, gating buys
nothing: "Contrary to our expectations… integrating LMs does not
consistently improve over the PPO baseline" — most LM sizes match the
PPO-only reward and mid-size models (7B, 14B) slightly degrade it. The
gate earns its keep only under distribution shift: policies trained on
8×8 grids and evaluated on smaller, unseen grids see PPO alone collapse to
zero reward, and LMs alone are also near-zero, but "a sharp capability
threshold emerges at 32B parameters. Both 32B and 72B models achieve
exceptional performance: 0.95 ± 0.22 reward on 4×4… This success persists
across all sizes… where all other configurations fail completely." The
paper's own framing: "their uncertainty-gated combination achieves up to
0.95 reward, demonstrating a strong synergy that emerges only at sufficient
model scale." Overwrite rate tracks this: a 0.5B gate overwrites 61–100%
of consulted steps and degrades performance (overconfident intervention),
while 32B/72B gates overwrite a moderate 46–68% and the interventions help
— the same threshold-crossing event is useful only when the model behind
the gate is itself well calibrated.

## Limits

- Evaluated on one toy environment (FrozenLake, 4×4 to 8×8) with a sparse
  binary reward; whether the IR/OR pattern holds for continuous-control or
  language-native tasks is untested.
- One LM family (Qwen, 0.5B–72B) and one RL algorithm (PPO); the U-shaped
  size curve (small and large models succeed, mid-size fails) is observed,
  not explained, and could be family-specific.
- The gate benefits only appear at 32B+ parameters — the mechanism is
  model-agnostic in principle, but the paper's own results show it is
  useless below a capability threshold the authors did not predict in
  advance.
- $\tau$ is tuned offline per LM size by Bayesian optimization over 22
  studies, not learned or adapted at run time; the paper reports this as a
  practical trade-off, not a limitation it solves.
- No comparison to a learned (rather than fixed-threshold) gating policy,
  and no human-in-the-loop baseline — the "assistance" is one model asking
  another, never a person.

## Related

[[decision-centric-design]] · [[value-of-information]] · [[calibration]] · [[abstention]]

[^s1]: arxiv-2604-02226
