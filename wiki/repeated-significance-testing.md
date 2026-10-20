---
description: "**A stopping threshold means nothing without saying how often it is Armitage, McPherson and Rowe (1969) state it in one sentence: if significance tests at a fixed level are repeated at stages durin…"
aliases: ["repeated significance tests", "repeated testing on accumulating data"]
sources: ["armitage-1969", "lan-1983", "pocock-1977"]
---
# Repeated significance testing

> **A stopping threshold means nothing without saying how often it is
> consulted.** Apply the same fixed cut to a growing record after every answer
> and the chance it fires for no reason rises above the level it was set at;
> consult it without limit and, for one standard boundary shape, it fires with
> probability one.

## The result

Armitage, McPherson and Rowe (1969) state it in one sentence: if significance[^s1][^s2][^s3]
tests at a fixed level are repeated at stages during the accumulation of data,
the probability of obtaining a significant result when the null hypothesis is
true rises above the nominal significance level. They report numerical results
for cumulative binomial, normal and exponential series.

The limiting case is sharper. Lan and DeMets (1983, §3), considering the
natural continuous version of Pocock's (1977) constant boundary,
$b(t)=c\sqrt{t}$ on a standard Brownian motion, invoke the law of the iterated
logarithm:

$$\Pr\{B(t) \ge c\sqrt{t}\ \text{for some}\ t \in (0,1]\} = 1,$$

**no matter how large $c$ is.** Unlimited consultation of a boundary of that
shape is certain to stop, under the null. Their own repair is not a larger $c$
but a delay: a small $\varepsilon > 0$ before the first examination.

The size of the required correction is visible in Lan & DeMets's Table 1(b).
For $K=5$ equally spaced looks at one-sided $\alpha=0.05$, Pocock's (1977)
constant boundary is $z=2.12$ against the fixed-sample $1.645$ — both figures
as used here are read off that table, the 2.12 being Lan & DeMets's tabulation
of Pocock's constant rather than a number quoted from Pocock's own paper.
*Arithmetic by this wiki on that table:* a Bonferroni split ($\alpha/5 = 0.01$,
$z=2.326$) would demand a higher bar than 2.12 — the looks are tests of one
hypothesis on nested data and are strongly positively dependent, so a
correction built for independent tests over-pays.

## Known as

| Field | Name there | exact / close |
|---|---|---|
| Biostatistics, sequential analysis | repeated significance tests | exact — Armitage, McPherson & Rowe's own term for the object |
| Biostatistics, sequential analysis | repeated testing on accumulating data | exact — the descriptive form of the same object, from the title of Armitage et al. (1969) |
| Clinical trial design | interim analysis multiplicity | close — names the design problem created by the inflation, and is used for the whole correction apparatus rather than the inflation itself |
| Clinical trial design | multiple looks | close, and **not declared an alias here** — bare, it names the consultation schedule (the looks), whereas this note's object is the error inflation that schedule causes; only the compound "the multiple-looks problem" points at the inflation |
| Multiple comparisons | *not this concept* — there the tests are of different hypotheses on one sample, here of one hypothesis on nested samples; the dependence structure differs and so does the correction, as the Bonferroni comparison above shows |

## Why it matters

[[guarded-threshold]] locates the unreliability of a cut **at** the cut. This
result locates a second, independent source of it in the **number of times the
cut is consulted** — and every online stopping rule consults its cut after
every answer by construction. [[qualitative-saturation]] is the wiki's clearest
instance: its rule inspects a novelty cut after each additional interview and
stops at the first empty run. [[sprt]] is the clearest exception: its
boundaries were derived for a rule evaluated at every step, so the cost of
looking is already inside them.

## Transfer

| | |
|---|---|
| In its home field | a fixed-level significance test of a fully specified null, applied to a nested sequence of samples from one trial |
| Here | an asker re-evaluating a stopping statistic against a fixed cut after each answer received |
| What survives | the direction and the mechanism: the more often one cut is applied to a growing record, the larger the chance it fires without cause; and the structural point that the correction belongs to the *schedule*, not to the statistic |
| What does not | the magnitudes. Armitage's figures are computed for named distributions and the certainty result is for Brownian motion under a $\sqrt{t}$ boundary. An asker's stopping statistic — a novelty rate, a judge's score — has neither a specified null nor independent increments, so neither the inflation's size nor the probability-one conclusion follows here |

## Limits

- **This note quotes no inflation figure.** Armitage et al.'s numerical tables
  were not read for it; only the claim of their abstract, and its direction, is
  used. A derivation that needs a number must go to the paper.
- The probability-one statement is Lan & DeMets's, for standard Brownian motion
  and the specific boundary $c\sqrt{t}$. A constant boundary, a bounded horizon,
  or a non-Brownian statistic are different cases and this note does not cover
  them.
- Pocock (1977) is cited here only for the boundary's *form* — a constant
  adjusted critical value over a pre-specified number of looks — as that form
  is reported by Lan & DeMets (1983). Pocock's own derivation and tables were
  not read.
- **The result is entirely about the null.** It says nothing about how repeated
  looks change the chance of stopping when there *is* something to find, which
  is the side an asker usually cares about.
- The Bonferroni comparison is this wiki's arithmetic at one setting ($K=5$,
  one-sided $\alpha=0.05$) on Lan & DeMets's table. No general claim about the
  two corrections is made, and none is proved here.
- The whole result presumes a **declared hypothesis that does not change
  between looks**. An asker who opens a new axis mid-inquiry is not running
  repeated tests of one hypothesis, and the inflation calculated here does not
  describe that case.

## Related

[[alpha-spending-function]] · [[sprt]] · [[hypothesis-testing]] · [[guarded-threshold]] · [[qualitative-saturation]] · [[stopping-rules]]

[^s1]: armitage-1969
[^s2]: lan-1983
[^s3]: pocock-1977
