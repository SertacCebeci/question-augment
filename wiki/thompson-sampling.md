---
description: "An algorithm for the exploration/exploitation trade-off: draw one plausible Given actions $x \\in \\mathcal{X}$, an unknown parameter $\\theta$ with prior $p$, and a reward $r(y)$ observed after acting,"
aliases: ["Thompson sampling", "TS", "posterior sampling", "probability matching"]
sources: ["russo-2014", "russo-2016", "russo-2017"]
---
# Thompson sampling

> An algorithm for the exploration/exploitation trade-off: draw one plausible
> truth from what you currently believe, act on it as if it were certain, then
> update. No separate [[value-of-information]] computation is needed.

## Definition / Mechanism (Thompson, 1933; exposited by Russo et al., 2017)

Given actions $x \in \mathcal{X}$, an unknown parameter $\theta$ with prior[^s1][^s2][^s3]
$p$, and a reward $r(y)$ observed after acting, Thompson sampling repeats,
each period $t$:

1. **Sample** $\hat\theta \sim p$ from the current posterior — not from the
   predictive distribution of the observation itself, a distinction the
   tutorial flags directly (Russo et al. 2017, §3): $\hat\theta$ is a
   statistically plausible *parameter*, not a statistically plausible
   *observation*.
2. **Act greedily under the sample**: $x_t = \arg\max_{x\in\mathcal{X}}
   \mathbb{E}_{q_{\hat\theta}}[r(y_t) \mid x_t = x]$.
3. **Update** $p$ by conditioning on $(x_t, y_t)$.

For the Beta-Bernoulli bandit this is: draw $\hat\theta_k \sim
\mathrm{Beta}(\alpha_k,\beta_k)$ for each arm $k$, play $\arg\max_k
\hat\theta_k$, and increment $\alpha_k$ or $\beta_k$ by the observed success
or failure (Russo et al. 2017, §3, Algorithm 3.2).

The only difference from a plain greedy rule (same tutorial, §2) is step 1:
greedy plugs in the posterior *mean* every period and therefore only
exploits; Thompson sampling plugs in a posterior *draw*, so an action is
tried in exact proportion to the current probability that it is optimal —
its uncertainty, not just its estimate, drives how often it is tried.

### Guarantees

Two results the tutorial reports (Russo et al. 2017, §8.1):

- **UCB transfer.** The Bayesian regret of Thompson sampling is bounded by
  the Bayesian regret of any upper-confidence-bound algorithm built from the
  same confidence sets, so every regret bound proved for a UCB rule carries
  over to Thompson sampling without a new proof (Russo & Van Roy 2014,
  `russo-2014`; restated in Russo et al. 2017, §8.1).
- **[[entropy|Entropy]] scaling.** Via the [[information-ratio]], the Bayesian regret is
  bounded by a term that grows with the entropy of the prior over *which
  action is optimal*, not with the number of actions (Russo & Van Roy 2016,
  `russo-2016`; restated in Russo et al. 2017, §8.1).

Both are averages over the prior and over many periods $T$; neither says
anything about a single run.

## Why it matters here

Stall 2 asks *which axis first*. The map's other selection rows —
[[expected-information-gain]], [[generalized-binary-search]],
[[adaptive-submodularity]] — score a candidate query by how much its answer
is expected to tell about the unknown $\theta$; the query itself pays
nothing. Thompson sampling scores an action by its expected *reward* under
one posterior draw; exploration is not computed at all, it falls out of the
draw's uncertainty. The two families share the same inputs (a known
observation model and a prior over $\theta$, updated after each answer); what
differs is the objective, and that is this wiki's reading of the tutorial's
own §8.2.2, not a claim the tutorial makes about question-asking. The
consequence: Thompson sampling is the right rule for stall 2 only when each
question has a payoff of its own — each answer is consumed downstream as it
arrives, or the axes are options whose answers directly pay off — so that
asking is simultaneously learning *and* earning. When the only goal is to
find out which axis is best and nothing is earned along the way, the
tutorial's own verdict (§8.2.2, below) is that a pure-information rule does
better.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Bandit / sequential decision theory | Thompson sampling | — |
| Bandit / sequential decision theory (Russo et al. 2017, §1) | posterior sampling | exact |
| Per Russo et al. (2017, §1)'s own gloss | probability matching | exact as used in the tutorial; not checked here against the separate psychology literature on probability matching as a documented (suboptimal) human choice bias, which may not be the same measured object |

## Transfer

| | |
|---|---|
| **Home field** | Repeated online decision-making: a fixed action set $\mathcal{X}$ pulled over many periods $t=1,\dots,T$ against a *stationary* $\theta$, with a known observation model $q_\theta(y\mid x)$ and reward function $r$ |
| **Here** | Choosing which axis of $W$ to query next when each question carries a payoff $r(y)$ of its own — the answer is used as soon as it arrives (a slot filled, a sub-task unblocked, a respondent's patience spent) — and which axis pays best is uncertain and learned only from answers already received |
| **What survives** | The recipe — draw one plausible hypothesis of "which candidate is best," act on it as if certain, then update — spends more queries on candidates that could still plausibly be optimal and stops probing ones that almost certainly are not, without an explicit value-of-information integral |
| **What does not** | The two guarantees under *Guarantees* are averages over many repeated, structurally identical periods against one fixed $\theta$; a single asking episode rarely repeats the same axis choice enough times to converge, so "regret vanishes as $T\to\infty$" has no direct reading for a one-shot or short-horizon session. When no reward per query exists — pure information-gathering, where nothing is earned until the session ends — the rule has nothing to maximise in step 2 and degenerates to the best-axis-identification case of §8.2.2, where the tutorial itself says it is the wrong choice. The observation model $q_\theta(y\mid x)$ must also be specified in advance — for open-ended natural-language answers this model is not available ready-made, unlike a slot machine's payout distribution |

## Limits

Four cases from Russo et al. (2017, §8.2) where the algorithm is the wrong
choice, each a live warning for a "sample-and-commit" axis-selection rule:

- **No exploration needed.** When passive information (randomised context,
  or a backtestable history) already resolves the uncertainty, Thompson
  sampling still pays an active-exploration cost a plain greedy rule would
  not (§8.2.1).
- **No exploitation needed.** In a pure best-axis-identification setting
  (find which candidate is best, reward collected while finding out does not
  matter), standard Thompson sampling converges too slowly: once fairly
  confident, it exploits and under-samples the runners-up (§8.2.2). A
  modified pure-exploration variant is named by the tutorial (Russo,
  "Simple Bayesian algorithms for best arm identification", 2016) — not
  read for this note, no source key.
- **Time-sensitive settings.** The algorithm keeps sampling any axis that
  could still be optimal, so its regret bound scales with the entropy of the
  belief over the best axis, which can be unbounded when candidates are
  numerous; a [[bounded-rationality|satisficing]] rule that stops at "good enough" can dominate it
  (§8.2.3).
- **Informative-but-never-optimal candidates.** Thompson sampling only ever
  tries axes that could themselves be the answer. An action that can never
  be optimal but is highly diagnostic of which other action is (the
  "revealing action" example, §8.2.4) is never tried, so the algorithm can
  take far longer to converge than a rule that explicitly values information
  over reward. See [[information-ratio]] and [[information-directed-sampling]].

The "Why it matters here" reading rests on one assumption of this wiki's
own: that a per-question payoff $r(y)$ exists and is observable as each
answer arrives. If it does not, the note's case for Thompson sampling at
stall 2 collapses into its second bullet above. The mechanism section
states the algorithm as the tutorial exposits it; Thompson (1933) is named
as the origin only on Russo et al.'s (2017) account — the 1933 paper itself
was not read for this note. The two guarantees are cited as restated in the
tutorial; `russo-2014` and `russo-2016` were not read whole for this note.

## Related

[[expected-information-gain]] · [[information-ratio]] · [[information-directed-sampling]] · [[value-of-information]] · [[adaptive-submodularity]] · [[bayesian-estimation]] · [[forgetting-factor-beta-bernoulli]] (the same posterior with a decay that drops the stationarity assumption)

[^s1]: russo-2014
[^s2]: russo-2016
[^s3]: russo-2017
