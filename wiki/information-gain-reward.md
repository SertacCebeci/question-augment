---
description: "An RL reward for training LLM clarifiers that scores a clarification exchange by the teacher-forced log-likelihood shift toward the ground-truth goal, an amortized proxy for expected information gain."
aliases: ["Information Gain Reward", "Belief Update Reward", "amortized EIG proxy for clarification"]
sources: ["deng-2026"]
---
# Information gain reward

> A clarification question's value, priced not by an enumerable candidate
> set but by how much one model's own belief in the true goal moves after
> asking — turned into an RL training signal for tool-using agents.

## Mechanism

Deng et al. (ICML 2026) train a clarifier for tool-using LLM agents inside
a modified [[twenty-questions|τ-Bench]]-style POMDP where the user's true
goal $G^*$ is latent and only revealed through a user simulator's answers.
Directly maximizing [[expected-information-gain|EIG]] over the open-ended
space of latent goals is intractable — there is no enumerable $\Omega$ to
sum over, unlike the closed candidate sets of prior EIG-trained
clarifiers.[^c1]

The reward instead amortizes the computation: the same model that
generates candidate questions is reused in teacher-forcing mode as a
*belief scorer* $P_\theta(G^*\mid\cdot)$. For a candidate question $Q$ and
the user simulator's answer $A$, the reward is the shift in the
length-normalized teacher-forced log-likelihood of $G^*$ between the
post-answer and pre-answer contexts — posterior belief minus prior
belief.[^c2]

Mathematically this reward is the paper's own derived identity: it equals
the pointwise [[mutual-information|mutual information]] (PMI) between the answer and the true
goal, $\log\frac{P(A\mid G^*,Q,x)}{P(A\mid Q,x)}$ — a per-trajectory,
per-sample stand-in for the population-level EIG in Eq. 1. When the
clarifier chooses not to intervene, the posterior equals the prior and the
reward is exactly zero, so silence is never penalized on its own.[^c3]

Rewards from $K$ on-policy sampled candidates are converted to
group-relative advantages and optimize the clarifier with DAPO. A *strict*
user simulator — one that reveals task information only in answer to a
specific, relevant question — is used during training; the paper reports
this is necessary because a lenient simulator lets the clarifier collect
reward from generic questions without learning to target the missing
information (reward hacking). Evaluated on τ-Bench retail (in-domain) and
airline (out-of-distribution) tasks across five backbones, the method
raises success rate by 3.7% over a no-clarification baseline while adding
only 0.3 interaction steps on average.[^c4]

## Known as

| Field | Name there | Match |
|---|---|---|
| LLM training (this paper, main text/abstract) | Information Gain Reward | exact |
| LLM training (this paper, Figure 2 caption) | Belief Update Reward | exact — same quantity, two names used interchangeably by the authors |
| this wiki (functional description) | amortized EIG proxy for clarification | close — describes the mechanism, not a term the paper itself uses as a label |

## Transfer

| | |
|---|---|
| **In its home field** | [[bayesian-experimental-design|Bayesian experimental design]]: EIG is the expected [[entropy]] drop of the posterior over a hypothesis, computed by integrating over the answer distribution. |
| **Here** | A single-sample, closed-form-free proxy: the shift in one model's own teacher-forced log-likelihood of the (known, held-out) true goal, used as an RL reward rather than a ranking score. |
| **What survives** | The framing — a question is worth what it moves belief about the latent target — and the zero-reward-for-silence property that falls directly out of the PMI identity. |
| **What does not** | The entropy computation itself (no integral over an open [[possible-worlds|hypothesis space]] is taken); any guarantee that the log-likelihood shift is an unbiased or calibrated estimate of the true EIG; and the closed-candidate-set assumption of prior EIG-trained clarifiers such as [[preference-optimization-for-questions]]. |

## Limits

- The reward's validity depends on the belief scorer being the same model
  as the policy, on a *strict* user simulator during training, and on
  access to a normalized ground-truth goal string $G^*$ at training time —
  none of which is available at deployment, where the true goal is exactly
  what is unknown.
- Evaluated in one environment family (τ-Bench retail/airline tool-use),
  one training set size (500 trajectories, 2,676 step-level instances),
  and reported for one training [[backbone-of-a-formula|backbone]] in the ablation table read here
  (Qwen3-1.7B); the abstract's "five heterogeneous backbones" claim is not
  itself verified in the slices read for this note.
- The reported 3.7% success-rate gain is an average; the source paper's
  own ablation table shows the effect varies by domain and by ablation
  (e.g., an LLM-as-judge reward substitute changes results in both
  directions across retail and airline).
- Published at ICML 2026 (PMLR); read from the archived text extract only,
  not cross-checked against a second source.

## Related

[[expected-information-gain]] · [[preference-optimization-for-questions]] · [[value-of-information]] · [[clarification-benchmarks]]

[^c1]: deng-2026 — "a metric that quantifies the utility of clarification questions by measuring the Bayesian belief update towards the ground-truth goal induced by the clarification exchange"
[^c2]: deng-2026 — "we propose an amortized approach. We optimize a question policy πθ (Q | x) to internalize the experimental design process and directly generate high-information questions. Separately, we use the same model in teacher-forcing mode as a belief scorer Pθ (G∗ | ·)"
[^c3]: deng-2026
[^c4]: deng-2026 — "Empirical results demonstrate that our method consistently improves the success rate by 3.7% over the no-clarification baseline, while adding only 0.3 total interaction steps on average."
