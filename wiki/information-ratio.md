---
description: "The price of exploring, in bits: how much expected regret an algorithm must For any online decision algorithm and period $t$, with $x^*$ the (unknown) optimal action and $(x_t,"
aliases: ["information ratio"]
sources: ["russo-2014", "russo-2016", "russo-2017"]
---
# Information ratio

> The price of exploring, in bits: how much expected regret an algorithm must
> pay per bit of mutual information it gains about which action is optimal.

## Definition (Russo & Van Roy, 2016)

For any online decision algorithm and period $t$, with $x^*$ the (unknown)[^s1][^s2][^s3]
optimal action and $(x_t, y_t)$ the action taken and outcome observed at $t$:

$$\Gamma_t = \frac{\big(\mathbb{E}[\mu(x^*,\theta) - \mu(x_t,\theta)]\big)^2}{I\big(x^*; (x_t,y_t) \mid H_{t-1}\big)}$$

the squared expected single-period regret divided by the conditional mutual
information between the optimal action and the impending observation — not
information about $\theta$ in general, but specifically about *which action
is optimal*. $\Gamma_t$ is a property of the algorithm's action distribution
at period $t$, not of any single action: it is defined by what the rule
plays, in expectation over its own randomization and the posterior.

## The regret bound

Russo & Van Roy (2016) show, for $\Gamma = \max_t \Gamma_t$:

$$\mathbb{E}[\mathrm{Regret}(T)] \le \sqrt{\Gamma \, H(x^*) \, T}$$

where $H(x^*)$ is the [[entropy]] of the prior over the optimal action. The
argument is a direct use of the wiki's own [[mutual-information]] [[chain-rule|chain rule]] plus Cauchy–Schwarz: the information gained about $x^*$ summed over
$T$ periods cannot exceed $H(x^*)$, and each period's regret is bounded
through $\Gamma_t$ by that period's information gain. The inequality is a
consequence of the ratio, not the ratio itself (see *Known as*).

The bound is established for [[thompson-sampling]], whose $\Gamma$ Russo &
Van Roy (2016) bound for several problem classes; the value of $\Gamma$ is
model-dependent. Russo et al. (2017, §8.1.2) illustrate on a $d$-edge
shortest-path bandit, distinguishing three feedback regimes by what is
observed after a path is chosen: only the path's total travel time
($\Gamma \le d/2$); the travel time of every edge in the graph
($\Gamma \le 1/2$); the travel times of the edges traversed, when every
path has $m$ edges ($\Gamma \le d/2m$). The link to UCB algorithms is a
different route: Russo & Van Roy (2014) show that Thompson sampling's
Bayesian regret is bounded by that of any UCB algorithm built from the same
confidence sets, so a UCB regret bound transfers to Thompson sampling — no
information ratio of a UCB algorithm is bounded by the sources this note
cites.

## Why it matters here

This is a sharper answer than [[expected-information-gain]] to "how much is
exploring this candidate worth": EIG scores a query by how much it shrinks
uncertainty about the full state; the information ratio prices a query by
how much it shrinks uncertainty about *which candidate is the answer*, per
unit of expected regret paid for asking it. A candidate can carry high EIG
about the full state while contributing little to resolving which candidate
is best — the two need not rank the same way. Russo et al. (2017, §8.2.4,
"a revealing action") give a case with an action that is never itself
optimal but whose outcome reveals which other action is: Thompson
sampling's information ratio in that example is far above the achievable
minimum precisely because Thompson sampling never plays the revealing
action, and a rule that plays it — [[information-directed-sampling]] —
drives the ratio down.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Bandit / online-decision theory (Russo & Van Roy 2016) | information ratio | — |
| Bandit / online-decision theory | information-theoretic regret bound | close — the inequality the ratio yields (Russo & Van Roy 2016), not the ratio itself; not an alias of this concept |

## Transfer

| | |
|---|---|
| **Home field** | Repeated online decision-making with a Bayesian prior over $\theta$, a known reward/observation model, and regret defined against a fixed optimal action $x^*$ |
| **Here** | Any rule for choosing the next axis to query, scored by how much it is expected to narrow down which axis (or which value of it) actually matters |
| **What survives** | The reframing: price a candidate query by the regret paid for asking it per bit of information gained about *the optimum specifically* — a sharper cut than EIG's raw entropy-reduction score, and one that explains exactly when EIG-style scoring misses a valuable but never-optimal query |
| **What does not** | The bound's numbers. $\Gamma$'s value ($1/2$, $d/2$, $d/2m$ in the tutorial's examples) is derived from a fully specified observation model for each query; no such model exists ready-made for a free-text answer, so no $\Gamma$ can be computed here without first supplying one |

## Limits

- The bound integrates over the *prior* (Bayesian/expected regret); it says
  nothing about performance on one fixed, adversarially chosen instance.
- $H(x^*)$ can be infinite when the number of candidate axes is unbounded,
  making the bound vacuous exactly where an open-ended axis space is the
  norm (Russo et al. 2017, §8.2.3).
- $\Gamma$ itself must be bounded by a separate, model-specific argument for
  each problem class; the ratio is a diagnostic quantity, not by itself a
  computable number for an arbitrary question.
- Established here for Thompson sampling; the UCB connection is the
  russo-2014 Bayesian-regret transfer, not a shared $\Gamma$. Whether the
  bound is tight for other selection rules on this map (e.g.
  [[generalized-binary-search]]) is not addressed by this note.
- The three shortest-path $\Gamma$ values are quoted from Russo et al.
  (2017, §8.1.2) as read by the researcher; the verifier could not read §8
  directly, so they rest on that reading.

## Related

[[thompson-sampling]] · [[information-directed-sampling]] · [[expected-information-gain]] · [[mutual-information]] · [[value-of-information]]

[^s1]: russo-2014
[^s2]: russo-2016
[^s3]: russo-2017
