---
description: "An RL-trained ask-or-act policy that decides, per interaction step, whether a robot acts on its current inference or first asks, gated on contextual sufficiency from observations plus history."
aliases: ["PACT", "ask-or-act framework", "Proactive Asking for Continual Task Assistance", "ASK-RL"]
sources: ["he-2026-pact"]
---
# PACT ask-or-act

> Before acting on an inferred intent or task, a shared multimodal policy
> asks one binary question of itself — ask or act — separately at the
> intent level and the task level, and the answer is trained by
> reinforcement learning against a reward that prices a missed question
> above an unnecessary one.

## Definition / Mechanism

He, Li, Ma et al. (2026) propose PACT, "an ask-or-act
framework that determines whether clarification should be sought before
taking action. PACT leverages current observations together with
accumulated interaction history to evaluate contextual [[sufficient-statistic|sufficiency]],
enabling the robot to provide more reliable assistance and progressively
adapt to the user over time."[^c1]

For a target $m \in \{\text{intent}, \text{task}\}$, a shared multimodal
[[backbone-of-a-formula|backbone]] with separate intent, task and ask heads produces
$q_t^m = \pi^m_{\text{ask}}(x_t, \hat Y_t^m, b_t) \in \{0,1\}$ from the
robot-observable state $x_t$ (observations, temporal context, cross-day
history), the current inferred candidates $\hat Y_t^m$, and the remaining
ask budget $b_t$. In the source's own words: "$q_t^m = 1$ means that the
robot asks a clarification question about target $m$, while $q_t^m = 0$
means that it proceeds without asking."[^c2]

Each asked question consumes one unit of $b_t$; the intent and task
decisions are separate because the two uncertainty sources differ — a
high-level goal versus a concrete predicate/object choice. The primary
instantiation, ASK-RL, trains this decision with a step-wise reward that is
$+1$ for correctly skipping a question, $1-c_{\text{ask}}$ for a necessary
question asked, $-1$ for a wrongly skipped one, and $-c_{\text{ask}}$ for
an unnecessary one asked. As the source describes the optimizer: "the
policy is updated over day-level trajectories using clipped PPO with
generalized advantage estimation, value regression, and [[entropy]]
regularization."[^c3]

Across two collaboration types and four human/scene settings in a
multi-day, simulated Habitat 3.0 household-assistance benchmark, "ASK-based
methods generally outperform non-clarification variants, with clearer
gains in Collab Type 2 ... Among ASK-based methods, ASK-RL and ASK-L2D
provide consistently strong performance across both intent-level and
task-level evaluation."[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (He et al. 2026) | PACT, ask-or-act framework | exact |
| This paper, primary trained instantiation | ASK-RL | close — the specific PPO-trained policy that fills the $\pi_{\text{ask}}$ slot of the PACT framework; other instantiations (ASK-SFT, ASK-L2D, prompting variants) fill the same slot with different training objectives and score differently on accuracy and ask rate, so "ASK-RL" is not interchangeable with "PACT" |

## Why it matters

This is a per-target (intent vs. task), budget-constrained, RL-trained
instance of the ask-or-act gate for stall 2 in an embodied, multi-day
setting: it operationalises "which axis first, and whether at all" as two
independent binary decisions conditioned on accumulated cross-session
history rather than a single-turn confidence score, and reports that the
trained gate beats both an always-ask and an always-act baseline on the
same interaction protocol.

## Transfer

| | |
|---|---|
| **In its home field** | Reinforcement learning: an actor-critic policy trained with clipped PPO, generalized advantage estimation and entropy regularization on a scalar step-wise reward — standard sequential-decision tooling |
| **Here** | The binary ask-or-act choice at each interaction step, separately for intent and task targets, under a per-day ask budget |
| **What survives** | The asymmetric reward shape (missing a needed question penalized more than an unneeded ask) and the use of accumulated trajectory-level outcomes, not single-step labels, to train the gate |
| **What does not** | The reward's four cases (`correct skip` / `necessary ask` / `wrong skip` / `unnecessary ask`) are labelled by the simulator's ground truth or an LLM judge at training time; nothing in the extract states how those labels are produced for a target whose correctness is not directly observable outside simulation, so the reward signal itself does not travel to a setting without such labels |

## Limits

- Evaluated only in simulated Habitat 3.0 household collaboration with
  profile-conditioned simulated humans, not real users; the "measured
  gains over passive inference" are gains on this authors' own simulated
  benchmark and baselines, not an independently replicated result.
- `he-2026-pact` is a single 2026 arXiv preprint; verification status is
  `queued` in `wiki/meta/sources.json` — the claims above are stated as
  the source states them, unverified beyond the provisional check.
- ASK-RL's superiority over ASK-SFT/ASK-L2D/prompting baselines is a
  relative ranking on this benchmark's accuracy–ask-rate trade-off, not a
  claim that PPO training is necessary for an ask-or-act gate to work.

## Related

[[value-of-information]] · [[intervention-advantage]] · [[breakdown-aware-proactive-intervention]] · [[bounded-rationality]]

[^c1]: he-2026-pact — "an ask-or-act framework that determines whether clarification should be sought before taking action. PACT leverages current observations together with accumulated interaction history to evaluate contextual sufficiency, enabling the robot to provide more reliable assistance and progressively adapt to the user over time."
[^c2]: he-2026-pact
[^c3]: he-2026-pact — "the policy is updated over day-level trajectories using clipped PPO with generalized advantage estimation, value regression, and entropy regularization."
[^c4]: he-2026-pact
