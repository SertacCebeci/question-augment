---
description: "An RL reward that scores a live agent's stated probability against an event's later, externally resolved real-world outcome, backfilled after the fact."
aliases: ["outcome-based RL for prediction", "live future prediction training loop", "verl-tool-future"]
sources: ["arxiv-2604-26733"]
---
# Delayed-outcome Brier reward

> The reward an agent's probability earns is not known until the world
> decides it — so the training loop has to wait.

## Definition / Mechanism

Han et al. train an agent's stated probability directly against reality
instead of against a judge or its own rollout group. Each prediction
question $q$ is issued before its outcome is known; the agent searches,
reasons, and emits a probability $\hat{\pi}_{q,k}\in[0,1]$, and the
trajectory is stored, "awaiting outcome," rather than scored. Only once
the real-world event resolves does the environment retrieve the
ground-truth label $z_q\in\{0,1\}$ and compute the trajectory-level
reward as the negative Brier loss, $r_{q,k} = -(\hat\pi_{q,k}-z_q)^2$; an
agent that fails to emit a valid probability is floored at the worst
possible reward, $-1$.[^c1]

To make this delay workable at scale, the authors "modify and extend
verl-tool ..., resulting in a new framework that we call
verl-tool-future," whose distinguishing move is that "unlike standard
reinforcement learning training frameworks that rely on immediate
rewards, verl-tool-future stores prediction-time rollouts, backfills
rewards after real-world outcomes become available, and then replays the
completed trajectories for policy update." A daily cycle issues a new
batch of questions each evening and attempts to retrieve the previous
day's outcomes twenty-four hours later; a question whose outcome cannot
yet be retrieved is simply dropped from that update rather than held
open — "an average of 35.65% of questions do not have retrievable ground
truth at the scheduled retrieval time," and when this happens "our
strategy is to discard the corresponding questions and exclude them from
training."[^c3]

## Why it matters

Training three open-source agents (Qwen2.5-3B, Qwen3-4B,
DeepSeek-0528-Qwen3-8B) for eight days of this loop moves all three
metrics that separate a committed answerer from a merely accurate one:
"Accuracy generally improves over the consecutive training days ... For
the Brier score, lower values indicate better predictions ... ECE
decreases gradually over time. All results indicate that RL training in
FutureWorld can improve agents' ability to predict future events."[^c4]
The gain is not a single-domain artifact: day-8 checkpoints outperform
the initial models across most of the paper's domain split (finance,
politics, weather, logistics and more), which the authors read as
general information-gathering and reasoning improvement rather than
overfitting to one question type.

## Transfer

| | |
|---|---|
| **Home field** | Forecasting-tournament and prediction-market infrastructure: a stream of real-world questions that resolve on their own schedule, scored by a proper rule against the realized outcome ([[calibration-training]]'s "environment that trains without training"). |
| **Here** | The same resolving stream becomes an RL training signal for an LLM *policy*: the resolved outcome is backfilled into a stored rollout and turned into a reward that updates model parameters, not a human forecaster's belief. |
| **What survives** | Externally resolved, leakage-free ground truth as the sole arbiter of the reward, and a proper score (negative Brier) that penalizes over- and under-confidence symmetrically. |
| **What does not** | The forecaster's discretion over which questions to answer, and independence from crowd beliefs — the paper does not exclude prediction markets from the agent's own search results, so "the availability of prediction markets ... can provide agents with a substantial advantage," an advantage the training signal cannot distinguish from genuine calibration. |

## Limits

- Roughly a third of issued questions are discarded for lack of a
  retrievable outcome at the scheduled check, which "wastes computation
  and potentially valuable supervision signals" and biases the trained
  set toward sources that resolve fast and cleanly.[^c3]
- The agent's search is not blocked from prediction markets and odds
  aggregators, so part of the measured accuracy and calibration gain may
  reflect reading a crowd's aggregated belief rather than an
  independently formed one; the paper reports no ablation isolating this
  (unverified).
- Evaluated on three open-source backbones up to 8B parameters and eight
  training days; whether the calibration gain continues, plateaus, or
  reverses over longer training is not reported here.
- The reward is a single scalar Brier loss on a binary-resolved event;
  it does not cover open-ended or multi-outcome questions, and carries no
  mechanism for the agent to abstain rather than commit to a probability.

## Related

[[calibration]] · [[calibration-training]] · [[savor-calibration-abstention-reward]] · [[certainty-weighted-grpo-reward]]

[^c1]: arxiv-2604-26733 — "If the agent fails to output a valid probability in [0, 1], we set rq,k = −1, the lowest possible reward."
[^c3]: arxiv-2604-26733 — "an average of 35.65% of questions do not have retrievable ground truth at the scheduled retrieval time"
[^c4]: arxiv-2604-26733
