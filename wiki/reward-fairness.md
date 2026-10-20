---
description: "A reward model is delta-fair across strategies if equal-quality responses in different strategies score within delta; unfairness biases advantages toward reward-preferred strategies."
aliases: ["delta-reward fairness", "reward fairness problem"]
sources: ["tong-2026"]
---
# Reward fairness

> When an agent may legitimately ask, answer directly, update on progress,
> or confirm before acting, a reward model that scores these differently
> for equal-quality responses is not measuring quality — it is measuring
> which behaviour it prefers.

## Definition

Tong, Faith, Marcus et al. (2026) define a reward model $R$
as $\delta$-fair with respect to a strategy set $S$ if, for any prompt $x$
and any two responses $y_i, y_j$ that follow *different* strategies but are
of *equal quality*, $|R(x,y_i) - R(x,y_j)| \le \delta$. $R$ is fair when
$\delta = 0$ and unfair — carrying systematic bias across strategies — when
$\delta > 0$.[^c1]

## Consequence for group-based RL

Group-based RL (GRPO and its relatives) estimates an advantage by
centering the reward within a sampled group of rollouts for the same
prompt, which is interpretable only when the group's rollouts are
behaviourally comparable. When multiple strategies — answer directly, ask
for clarification, give a progress update, confirm before acting — are all
valid for one prompt and are compared inside one group, an unfair reward
model's cross-strategy bias enters the centered advantage directly: "cross-strategy comparison biases group-relative advantage estimation and can
skew optimization toward reward-preferred interaction styles."[^c2]

## Known as

| Field | Name there | Match |
|---|---|---|
| LLM training / RL (Tong et al. 2026, Definition 1) | $\delta$-Reward Fairness | exact — this note's object |
| LLM training / RL (Tong et al. 2026, prose) | reward fairness problem | exact — the same criterion named as the failure mode it diagnoses |

## Limits

- The definition is stated for pairs of responses of "equal quality," a
  term the paper does not operationalise independently of the reward model
  itself being checked — there is no quality oracle outside $R$, so $\delta$
  cannot be measured directly, only its downstream effect (variance,
  optimisation drift) can be.
- Evidence for unfairness in practice ("reward models depend on spurious
  attributes such as response length and stylistic form") is cited from
  prior work on reward-model bias generally, not measured for the specific
  strategy taxonomy this paper uses.
- The definition covers strategy-conditioned comparison only; it says
  nothing about whether a fair reward model is otherwise well-calibrated to
  task success.

## Related

[[strategy-conditioned-rollout-grouping]] · [[investigative-question-grpo-training]] · [[certainty-weighted-grpo-reward]] · [[value-of-information]]

[^c1]: tong-2026
[^c2]: tong-2026 — "as the reward fairness problem: when multiple strategies are valid for the same prompt, cross-strategy comparison biases group-relative advantage estimation and can skew optimization toward reward-preferred interaction styles."
