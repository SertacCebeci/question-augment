---
description: "**A stopping rule that prices its own early stop.** Stop when the probability At an interim point,"
aliases: ["stochastic curtailment", "stochastically curtailed test", "conditional power stopping under the design alternative"]
sources: ["chang-2004", "lan-1982", "lan-1983", "ortega-villa-2025"]
---
# Stochastic curtailment

> **A stopping rule that prices its own early stop.** Stop when the probability
> that the *remaining* evidence would change the already-scheduled conclusion
> falls below a declared $\Gamma$ — and the declared $\Gamma$ converts into a
> bounded loss of power against the design that would have run to the end.

## Definition / Mechanism

At an interim point, **conditional power** is the probability of rejecting the[^s1][^s2][^s3][^s4]
null at the *already scheduled* final analysis, given the data so far and an
assumed effect $\theta$:

$$\mathrm{CP}_t(\theta) = \Pr\{\text{reject } H_0 \text{ at the end} \mid \text{data to } t,\ \theta\}.$$

Lan, Simon and Halperin (1982) proposed stopping for futility when
$\mathrm{CP} \le \Gamma$, and bounded what that costs. As stated by
Ortega-Villa et al. (2025): if the trial is monitored continuously and CP is
computed **under the originally hypothesised treatment effect**, the type II
error rate under the curtailment rule is at most $\beta/(1-\Gamma)$, where
$\beta$ is the type II error of the same design with no monitoring. Their
worked case: $\beta=0.1$ with $\Gamma = 0.2$ gives $0.1/0.8 = 0.125$ — 90%
power becomes 87.5%. $\Gamma \le 0.2$ is the usual choice.

The rule is the missing half of [[alpha-spending-function]]: Lan & DeMets (1983, §4) recommend precisely this construction as the *lower* boundary for a
treatment–placebo trial, and add that the conditional-power level "should be
allowed to vary with time."

## Why it matters

The priced quantity is specific: **the loss from abandoning a design before its
declared final analysis**, expressed as an inflation of that design's type II
error by a factor $1/(1-\Gamma)$ that the asker fixes when it fixes $\Gamma$.
[[value-of-information]] fires on the same intuition — the remaining answers
are unlikely to change the conclusion — and supplies **no bound at all** on
what the stop costs if that judgement is wrong. Four stall-7 rules were read
for this note ([[sprt]], [[value-of-information]], [[alpha-spending-function]],
[[stopping-rules]]); **no exhaustive count of the wiki's stopping rules was
made**, so this is a comparison, not a census. [[sprt]] also carries a priced
guarantee, but of a different quantity: Wald's $\alpha' \le \alpha/(1-\beta)$
bounds the *realised* error rates of the SPRT's own boundaries, a rule with no
scheduled end; the bound here is on the damage done to an end that was already
scheduled. For an asker, conditional-power stopping is distinctive in what it
measures: nothing about present uncertainty, only the probability that the
*unspent* part of the budget flips the outcome.

## Known as

| Field | Name there | exact / close |
|---|---|---|
| Biostatistics | stochastic curtailment, stochastically curtailed test | exact — Lan, Simon & Halperin's own construction |
| Clinical trial monitoring | conditional power stopping **under the design alternative** | exact — the rule this note defines, with CP evaluated at the originally hypothesised effect |
| Clinical trial monitoring | *conditional power stopping* (bare) | close — the bare name is also used when CP is evaluated under the observed trend, which stops at different times and is outside the $\beta/(1-\Gamma)$ bound |
| Clinical trial monitoring | **futility stopping / futility monitoring** — *not this concept*: the family of rules for stopping when success has become unlikely. CP under the design alternative is one member; CP under the observed trend, predictive power (averaging over a posterior) and beta-spending boundaries are others, and they stop at different times with different guarantees (Ortega-Villa et al. 2025) | not this concept — a family, not a rule |

## Transfer

| | |
|---|---|
| In its home field | a two-arm trial with a declared final analysis, a declared alternative $\theta_A$, a normal test statistic, and a fixed maximum information |
| Here | an asker who, partway through a declared question budget, asks "if I spend the rest, how likely is my conclusion to change?" and stops when that is below $\Gamma$ |
| What survives | the shape — futility is a probability about the *future* of the same inquiry, not a measurement of present uncertainty; and the accounting, that a declared $\Gamma$ buys a declared worst case rather than an unbounded one |
| What does not | the bound. $\beta/(1-\Gamma)$ needs a $\beta$ to exist, which needs both a declared alternative and a declared final analysis. An inquiry with no horizon has no "conditional" and no CP, so the rule is not approximated there — it is undefined ([[question-budgets]] is the precondition, not a convenience) |

## Limits

- **Which $\theta$ the CP is computed under decides whether the bound holds at
  all.** It is stated for the *originally hypothesised* effect. Computing CP
  under the observed trend — common practice — is outside it: Ortega-Villa et
  al. (2025) enumerate it as a separate variant of the futility rule, and this
  note makes no claim about its error rates.
- **The bound is one-sided.** It governs the type II error; nothing here
  controls type I error. Two opposite deviations are reported in the
  literature: Ortega-Villa et al. (2025) note that re-claiming the $\alpha$ not
  spent because of a *non-binding* futility boundary inflates the type I error,
  while Chang and Chuang-Stein (2004) [?] find that a binding interim futility
  analysis in a superiority trial *reduces* the overall type I error below the
  nominal level and propose raising the final significance level to recover it.
  Either way the realised $\alpha$ is not the declared one.
- The bound is stated under **continuous** monitoring; this note does not claim
  it for an arbitrary discrete look schedule and no argument for that case is
  given here.
- **Two sources were not read in the original.** Lan, Simon & Halperin (1982,
  *Communications in Statistics C*) is cited through Ortega-Villa et al. (2025)
  and through Lan & DeMets (1983, §4); the two differ on the citation year
  (a 1984 reprint in *Comm. Statist. A* exists), and the exact conditions of the
  theorem as its authors stated them are not verified here. Chang and
  Chuang-Stein (2004, *Pharmaceutical Statistics* 3(1):51–59) is marked `[?]`:
  its metadata and abstract-level finding were checked, its full text was not,
  and it is cited by no source in this note.
- Like every rule on Stopping, it presumes a **fixed [[possible-worlds|hypothesis space]]**: CP is the probability of rejecting the hypothesis already declared.
  A question that opens a new axis is not an event this probability covers.

## Related

[[alpha-spending-function]] · [[value-of-information]] · [[stopping-rules]] · [[question-budgets]] · [[sprt]] · [[abstention]]

[^s1]: chang-2004
[^s2]: lan-1982
[^s3]: lan-1983
[^s4]: ortega-villa-2025
