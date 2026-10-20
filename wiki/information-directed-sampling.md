---
description: "Instead of sampling the action that might be optimal (Thompson sampling), At each period $t$, with history $H_{t-1}$, optimal action $x^*$ and observation $y_t$,"
aliases: ["IDS", "information-directed sampling"]
sources: ["russo-2017", "russo-2018"]
---
# Information-directed sampling

> Instead of sampling the action that might be optimal (Thompson sampling),
> sample the action that teaches the most about the optimum per unit of
> reward given up — including an action that can never itself be optimal.

## Definition / Mechanism (Russo & Van Roy, 2018)

At each period $t$, with history $H_{t-1}$, optimal action $x^*$ and[^s1][^s2]
observation $y_t$, define for any action distribution $\pi$ the expected
one-period regret and the expected information gain about $x^*$:

$$\Delta_t(\pi) = \sum_x \pi(x)\,\mathbb{E}\big[\mu(x^*,\theta) - \mu(x,\theta)\mid H_{t-1}\big],
\qquad
g_t(\pi) = \sum_x \pi(x)\, I\big(x^*; y_t \mid x_t = x, H_{t-1}\big).$$

IDS chooses the action distribution that minimises the
[[information-ratio]] $\Delta_t(\pi)^2 / g_t(\pi)$ and then samples the
action from it:

$$\pi_t \in \arg\min_{\pi} \frac{\Delta_t(\pi)^2}{g_t(\pi)}, \qquad x_t \sim \pi_t$$

(Russo & Van Roy 2018). [[thompson-sampling]] instead samples $x_t$ from
the posterior probability that each action is optimal, $\pi^{TS}_t$. The
two rules give the same action distribution exactly when $\pi^{TS}_t$
itself attains the minimum of the ratio; they diverge whenever some other
distribution — possibly one putting mass on an action that is never
optimal — buys more information about $x^*$ per unit of squared expected
regret.

## Why it matters here

Thompson sampling only ever tries an axis that could itself be the true
optimum (Russo et al. 2017, §8.2.4). In the tutorial's "revealing action"
example, one action never yields the highest reward but perfectly reveals
the optimal action's identity when tried; Thompson sampling never tries it
and needs on the order of $k$ periods to find the optimum by elimination,
while minimising the information ratio identifies it in one period. The
same pattern is shown for a sparse linear bandit (Thompson sampling needs
$d/2$ periods where a bisection-capable rule needs $\log d$) and for
assortment recommendation, where diversifying the offered set — something
Thompson sampling never does on its own — accelerates learning by a factor
equal to the assortment size.

What IDS adds over each of the map's other selection criteria is narrower
than "ask about an axis not in doubt", which [[value-of-information]]
already licenses:

- against [[thompson-sampling]] (posterior sampling): TS never tries a
  never-optimal axis; IDS does when that is the cheapest route to $x^*$.
- against [[expected-information-gain]]: EIG scores information about the
  whole state $\theta$; IDS scores information about $x^*$ only, so an axis
  that resolves structure irrelevant to which axis is best scores under EIG
  and not under IDS.
- against [[value-of-information]]: VoI and IDS *agree* on the revealing
  action — an observation that changes the decision scores high under both.
  They differ in the currency: VoI is a one-step utility difference within
  a fixed decision problem with no guarantee attached, while IDS prices the
  query by [[mutual-information|mutual information]] about $x^*$ divided by squared expected regret
  and, through the [[information-ratio]], carries a cumulative-regret bound
  (Russo & Van Roy 2018).

## Known as

| Field | Name there | Relation |
|---|---|---|
| Bandit / online-decision theory (Russo & Van Roy 2014, 2018) | information-directed sampling | — |
| Bandit / online-decision theory | IDS | exact |

## Transfer

| | |
|---|---|
| **Home field** | Repeated online decisions where the information ratio can be computed or approximated for every candidate action distribution at every period |
| **Here** | Deciding whether to spend a question on an axis that is not itself in question, because answering it is expected to resolve a different axis more cheaply than asking about that axis directly |
| **What survives** | The principle that a query's worth is its information about *the thing actually being decided*, discounted by what asking it costs — and that this can favour a query whose own answer is not the one wanted |
| **What does not** | The optimisation itself. Minimising the ratio over action distributions needs the same fully specified observation model the information ratio needs; the tutorial itself notes the computation is heavier than Thompson sampling's single posterior draw and "may not be practical across the range of applications for which TS is well suited" (Russo et al. 2017, §8.2.4) |

## Limits

- Requires computing or approximating the information ratio over
  candidate action distributions at every step — strictly more computation
  than Thompson sampling, and the tutorial names this as the reason it is
  not always the practical choice.
- The examples establishing its advantage (revealing action, sparse linear
  model, assortment diversification) are constructed cases chosen to expose
  Thompson sampling's blind spot; no claim is made here about how often such
  cases arise in an open-ended axis-selection setting.
- The contrast with value-of-information above rests on VoI being read as
  Howard's one-step, fixed-decision-problem quantity as the wiki's
  [[value-of-information]] note states it; a multi-step VoI with a regret
  bound would close most of the gap claimed here.
- Inherits, like [[information-ratio]], the requirement of a Bayesian model
  with a computable $I(x^*; y_t \mid x_t = x, H_{t-1})$ — unavailable off
  the shelf for a free-text answer.

## Related

[[information-ratio]] · [[thompson-sampling]] · [[expected-information-gain]] · [[value-of-information]] · [[adaptive-submodularity]]

[^s1]: russo-2017
[^s2]: russo-2018
