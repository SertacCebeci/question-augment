---
description: "**The stopping rule with an optimality proof.** Among all tests of two simple Accumulate the log-likelihood ratio: At every step, three options: ```text S_n ≥ A → accept H1, STOP S_n ≤ B → accept H0,"
aliases: ["sequential probability ratio test", "Wald's sequential test", "SPRT"]
sources: ["wald-1945", "wald-1948", "kullback-1951", "fischer-2024"]
---
# SPRT — Sequential Probability Ratio Test

> **The stopping rule with an optimality proof.** Among all tests of two simple
> hypotheses meeting given error rates, it minimises the expected number of
> observations (Wald & Wolfowitz, 1948).

## The rule (Wald, 1945)

Accumulate the log-[[likelihood-ratio|likelihood ratio]]:[^s1][^s2][^s3][^s4]

$$S_n = \sum_{i=1}^{n} \log\frac{p_1(x_i)}{p_0(x_i)}$$

At every step, three options:

```text
S_n ≥ A     →  accept H1, STOP
S_n ≤ B     →  accept H0, STOP
B < S_n < A →  CONTINUE, take one more observation
```

Thresholds come from the target error rates:
$A \approx \log\frac{1-\beta}{\alpha}$, $B \approx \log\frac{\beta}{1-\alpha}$.
These are **approximations by construction**: Wald (1945, §3.3) derives them as
_inequalities_ on the exact boundaries and then recommends using them as
equalities, because the exact values are laborious and the loss is small.

## Optimality (Wald & Wolfowitz, 1948)

Among **all** tests — sequential or fixed-sample — of the two simple hypotheses
whose error probabilities are no larger than $\alpha,\beta$, the SPRT with those
error rates **minimises the expected number of observations**, under both
hypotheses, for independent identically distributed observations.

Wald (1945, §A) reports the size of the gain against the _current most powerful
test_ — the fixed-sample Neyman–Pearson test controlling the same $\alpha$ and
$\beta$: the SPRT "frequently results in a saving of about 50% in the number of
observations as compared with the current most powerful test". The figure is
Wald's comparison, not part of the 1948 optimality theorem, and it is attached to
his worked binomial and normal cases.

## Known as

| Field                       | Name there                                                                                                                                                                                                    | Same thing?                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Sequential analysis         | sequential probability ratio test, SPRT                                                                                                                                                                       | exact                                                                                       |
| Detection & estimation      | Wald's sequential test                                                                                                                                                                                        | exact                                                                                       |
| Statistical quality control | sequential sampling plan                                                                                                                                                                                      | close — an SPRT instantiated for attributes inspection, with the lot as the hypothesis pair |
| General statistics          | **"Wald test"** — _not this concept_: the asymptotic $\chi^2$ test on a maximum-likelihood estimate. Fixed sample, no stopping rule, no $\alpha,\beta$-optimality claim. The shared surname is the only link. |

## Why it matters

It is the theoretical answer to **"what is the [[stopping-rules|stopping condition]]?"**: not a
fixed number of questions, but _accumulated evidence against a threshold_. The
question count is never the target; it is the **output**. An easy topic crosses
in 3 questions, a hard one in 300.

> **Conjecture (this wiki), not a consequence of Wald's theorem.** A questioner
> that stops after five rounds and one that goes on for thirty differ in their
> **thresholds** — loose versus tight $(\alpha,\beta)$ — rather than in their
> algorithm; and the warning _never stop at a round number_ is this wiki's
> reading of the rule, not a corollary of it. No measurement supports either
> yet: nothing here estimates a questioner's $\alpha,\beta$, and the Transfer
> table below says the threshold formulas do not survive the import.

## Expected number of questions

Wald (1945, §4.1) derives the identity behind the count: with
$z = \log\frac{f_1(x)}{f_0(x)}$ per observation, $E(n) = E(Z_n)/E(z)$ — the
accumulated evidence at stopping divided by the evidence per observation, which
under the boundary approximation gives
$E(n) \approx \big((1-\gamma)\log B + \gamma \log A\big)/E(z)$.

$$\mathbb{E}[N] \approx \frac{\text{total evidence required}}{\text{evidence per observation}}$$

Under $H_1$ the denominator $E(z)$ is exactly the [[kl-divergence]]
$D(f_1\|f_0)$ — Kullback and Leibler (1951) introduce it as the mean information
per observation for discriminating $H_1$ from $H_0$.

_This wiki's inference, not a corollary:_ read per question, the denominator says
**good questions shrink the count**, so quality and count are not rivals. This
holds only once a surrogate for $\log\Lambda$ per answer is fixed
([[semantic-entropy]], a judge). Without one there is no denominator to enlarge.

## Transfer

|                   |                                                                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In its home field | i.i.d. draws from one of two fully specified densities $p_0,p_1$; $\log\Lambda$ computable per draw; $\alpha,\beta$ declared in advance                                                                                                           |
| Here              | one answer per step; the hypotheses are "the design goes this way / that way" — no densities; $\log\Lambda$ needs a surrogate ([[semantic-entropy]], a judge)                                                                                     |
| What survives     | stop on **accumulated** evidence, not on a count; the count is an output of thresholds and evidence rate; a higher evidence rate per step shortens it                                                                                             |
| What does not     | Wald–Wolfowitz optimality (needs two simple hypotheses and i.i.d. draws); the threshold formulas $A,B$ (need $\alpha,\beta$ on a specified pair); the "50% saving" (a comparison against a fixed-sample test on Wald's binomial and normal cases) |

## Limits

- Assumes two simple hypotheses; design spaces are composite and
  multi-hypothesis. The multi-hypothesis generalisation (MSPRT) is more complex
  with weaker guarantees.
- Assumes independence for the optimality result. Wald (1945, §3.2) notes the
  _error_ inequalities survive some dependence; the 1948 optimality proof does
  not.
- **The thresholds are Wald's approximation.** The walk overshoots the boundary,
  so the realised rates are only bounded — $\alpha' \le \alpha/(1-\beta)$,
  $\beta' \le \beta/(1-\alpha)$, and $\alpha'+\beta' \le \alpha+\beta$ (Wald,
  1945, §3.3) — not equal to the targets. Fischer and Ramdas (2024) show that
  with $\beta > 0$ the approximate boundaries guarantee **neither** error control
  at $(\alpha,\beta)$ **nor** optimality.
- Optimality assumes one of the two hypotheses is true. Under misspecification —
  the normal case when questioning, where the real answer space is neither
  hypothesis — the theorem says nothing and the ratio can drift to a boundary for
  the wrong reason.
- The count-as-output reading of this note needs a per-answer $\log\Lambda$
  surrogate to exist at all. Without one there are no thresholds and no $E[N]$,
  only the qualitative instruction to stop on evidence rather than on a count.

## Related

[[likelihood-ratio]] · [[hypothesis-testing]] · [[cusum]] · [[value-of-information]] · [[twenty-questions]] · [[kl-divergence]]

[^s1]: wald-1945
[^s2]: wald-1948
[^s3]: kullback-1951
[^s4]: fischer-2024
