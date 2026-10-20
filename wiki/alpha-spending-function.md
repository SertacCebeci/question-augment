---
description: "**The right to re-check \"am I done?\" is a budget, not a schedule.** Declare a The premise the whole construction prices is Armitage,"
aliases: ["alpha spending function", "Lan–DeMets spending function"]
sources: ["armitage-1969", "lan-1983", "obrien-1979", "pocock-1977"]
---
# Alpha spending function

> **The right to re-check "am I done?" is a budget, not a schedule.** Declare a
> function that says how fast the total risk of a wrong stop is spent against
> the fraction of evidence collected, and the *number and timing* of the checks
> may then be decided after the answers start arriving.

## Definition / Mechanism

The premise the whole construction prices is Armitage, McPherson & Rowe's (1969): repeating a fixed-level significance test on accumulating data raises[^s1][^s2][^s3][^s4]
the probability of a wrong stop above the nominal level, so a rule consulted
repeatedly needs a *total* risk budgeted across its consultations rather than a
level applied at each ([[repeated-significance-testing]]). $\alpha^*$ is the
instrument that prices that repetition.

Lan and DeMets (1983) construct a discrete sequential boundary from one
declared object: an increasing function $\alpha^*(t)$ on $t \in [0,1]$ with
$\alpha^*(0)=0$ and $\alpha^*(1)=\alpha$, where $t$ is the **information
fraction** — evidence accumulated so far divided by the maximum planned. For
a standard Brownian statistic $B(t)$ observed at times $t_1 < \dots < t_K = 1$,
the boundary points $b_i$ are fixed successively by

$$\Pr\{B(t_j) < b_j,\, j<i;\ B(t_i) \ge b_i\} = \alpha^*(t_i) - \alpha^*(t_{i-1}).$$

The load-bearing property is stated in their summary: $b_i$ is determined by
$\alpha^*$ and by *past and current* decision times, **but does not depend on
the future decision times or the total number of decision times**. Earlier
constructions — Pocock (1977), O'Brien & Fleming (1979), Slud & Wei (1982) —
all required $K$ in advance (Lan & DeMets 1983, §1).

They give three choices (§3), for a one-sided $\alpha$:

| $\alpha^*$ | Shape | Behaviour |
|---|---|---|
| $\alpha_1^*(t) = 2-2\Phi(z_{\alpha/2}/\sqrt{t})$ | spends almost nothing early | close to the O'Brien–Fleming boundary; "a trial is unlikely to stop very early" |
| $\alpha_2^*(t) = \alpha\log\{1+(e-1)t\}$ | $\alpha_2^*(\tfrac12)\approx 0.62\alpha$ | near-Pocock: earlier termination, "but we will suffer a reduction in power" |
| $\alpha_3^*(t) = \alpha t$ | uniform | intermediate |

Their Table 1(b) ($K=5$, one-sided $\alpha=0.05$, $t_i=i/5$) shows what the
choice costs: O'Brien–Fleming needs $z=3.92$ at the first look and $1.75$ at
the last; Pocock needs a constant $2.12$ at every look. The fixed-sample
one-sided cut is $1.645$. **Spending early raises the bar at the end.**

## Known as

| Field | Name there | exact / close |
|---|---|---|
| Clinical biostatistics | alpha spending function, $\alpha^*(t)$ | exact — Lan & DeMets's own object; the name follows their phrase "the rate at which the error level $\alpha$ is spent" |
| Group sequential theory | error spending function | close — **not an alias**: the same construction generalised to spend the type II budget as well, so it names a larger family than $\alpha$ alone |

## Why it matters

Every threshold rule on Stopping is consulted repeatedly by an asker
who checks after each answer whether $|W|$ is small enough. This is the only
construction the wiki holds that makes the *consultation schedule* part of the
declared rule rather than an afterthought — and it makes it cheap: the asker
declares a rate, not a plan. Checking more often is not forbidden; it is paid
for out of a fixed allowance, at a price fixed before the answers arrive.

## Transfer

| | |
|---|---|
| In its home field | a Brownian test statistic over accumulated information in a two-arm trial; a maximum information level declared in advance; independent increments; $\alpha$ declared for one hypothesis |
| Here | an asker's stopping statistic consulted after each answer, with $t$ = answers received ÷ the budget declared for the question ([[question-budgets]]) |
| What survives | the budget discipline — a fixed total risk of a wrong stop, divided across the occasions of consultation by a function declared before the answers; and the freedom to choose *when* to consult afterwards |
| What does not | the arithmetic. $b_i$ is computed from the Brownian null; a stopping statistic with no null distribution has nothing to integrate. Nor does $t$ exist without a declared maximum, so an open-ended inquiry has no information fraction and gets no boundary at all |

## Limits

- **The construction assumes $B(t)$ is Brownian with independent increments.**
  Lan & DeMets (1983, §1) themselves record that Slud & Wei (1982) found
  staggered entry and random loss to follow-up generally produce *dependent*
  increments; the extension to a general process $S(t)$ they sketch in §2 is
  stated to inherit the optimality only "approximately".
- **No optimality is claimed.** Their Discussion: they "did not define or
  consider the optimality of $\alpha^*$ in differing situations". The choice of
  spending function is therefore a declared preference, not a derived one — the
  same unanswered question Stopping records for every field.
- **$\alpha_1^*$ is very conservative early**, "especially for large $K$"; their
  own remedy is ad hoc — cap $c_i$ at about $3.5$ (§3).
- **It governs only the success side.** A futility boundary is a separate
  construction; Lan & DeMets (§4) point to [[stochastic-curtailment]] for it.
- **The transfer claim in this note is untested.** Nothing here estimates an
  information fraction for a question sequence, and without a declared maximum
  the whole apparatus is inapplicable rather than approximate.

## Related

[[sprt]] · [[repeated-significance-testing]] · [[stochastic-curtailment]] · [[stopping-rules]] · [[question-budgets]] · [[guarded-threshold]]

[^s1]: armitage-1969
[^s2]: lan-1983
[^s3]: obrien-1979
[^s4]: pocock-1977
