---
description: "No unbiased estimator can be more precise than the information allows. Established independently by Rao (1945) and Cramér (1946); the modern statement with its conditions is Lehmann & Casella (1998),"
aliases: ["CRLB", "Cramér–Rao lower bound", "information inequality"]
sources: ["rao-1945", "cramer-1946", "lehmann-1998"]
---
# Cramér–Rao bound

> No unbiased estimator can be more precise than the information allows.

## Theorem

Established independently by Rao (1945) and Cramér (1946); the modern[^s1][^s2][^s3]
statement with its conditions is Lehmann & Casella (1998), who call it the
*information inequality*. For an unbiased $\hat\theta$:

$$\mathrm{Var}(\hat\theta) \geq \frac{1}{\mathcal{I}(\theta)}$$

The conditions are load-bearing and are the reason the bound travels badly:
$\hat\theta$ must be **unbiased**, $\theta$ must be a real parameter with a
**regular** likelihood — support not depending on $\theta$, log-likelihood
differentiable in $\theta$, differentiation under the integral sign
permitted — and $\mathcal{I}(\theta)$ ([[fisher-information]]) must be
finite and non-zero.

Fisher information is **additive over independent observations**, so for $n$
i.i.d. observations $\mathcal{I}_n = n\mathcal{I}_1$ (Rao 1945; Lehmann &
Casella 1998), hence:

$$\mathrm{Var} \geq \frac{1}{n\,\mathcal{I}_1} \quad\Rightarrow\quad \text{std} \gtrsim \frac{1}{\sqrt{n}}$$

## Known as

| Name | Field | Relation |
|---|---|---|
| CRLB | estimation theory, signal processing | exact — the same inequality |
| Cramér–Rao lower bound | estimation theory | exact |
| information inequality | mathematical statistics (Lehmann & Casella) | exact — the textbook name for the same result |
| Fréchet–Darmois–Cramér–Rao inequality | continental statistics | exact — the same inequality with the fuller priority list |
| $\sqrt{n}$ law | *not* this concept | a corollary, and only under the extra i.i.d.-plus-attainability assumptions below; the same name also names Monte Carlo error decay in [[tree-search-methods]], a different object with a different derivation |

## The corollary under i.i.d. sampling: the $\sqrt{n}$ rate

If the observations are i.i.d. *and* an estimator attains the bound, the best
achievable standard error falls as $1/\sqrt{n}$: four times the precision
costs sixteen times the data. Both extra assumptions are needed. The
inequality itself says nothing about the rate — additivity supplies the $n$,
attainability supplies the equality.

## Why it matters — the return on 10,000 questions

This is the sharpest quantitative objection available to "more questions is
better" — but only as an analogy, and the analogy is this wiki's, not the
literature's.

> **Inference (this wiki, not Rao or Cramér).** *If* a batch of answers
> behaved like i.i.d. observations of a continuous parameter — which it does
> not; see **Transfer** below — the bound would give:
>
> ```text
> 100    questions  →  unit precision
> 400    questions  →  2× precision
> 10000  questions  →  10× precision
> ```
>
> i.e. a hundredfold increase in questions for a tenfold increase in
> precision. The transferable part is the *shape*: returns diminish but do
> **not** vanish, so cheap questions can still make 10,000 rational. The
> exponent is not transferable.

**Inference.** The lever in that shape is independence, not count: dependence
makes $\mathcal{I}_n < n\mathcal{I}_1$ and flattens the curve below even the
$\sqrt{n}$ idealisation. Read back into design, that makes diversity among
questions a *structural* requirement rather than an aesthetic one — this wiki
infers it from the additivity step; no source cited here establishes a
diversity–independence link for question design.

## Transfer

| | |
|---|---|
| **Home field** | point estimation: $n$ i.i.d. draws from a regular parametric family, one real parameter $\theta$, an unbiased estimator, variance as the loss |
| **Here** | a sequence of $n$ answers, correlated by construction (each question is chosen after the last), about a design whose unknowns are mostly discrete choices |
| **What survives** | the *form* of the trade — information is the binding resource, it accumulates only through independent observations, so returns diminish in count; and the diagnostic that dependence, not cost, is what flattens the curve |
| **What does not** | the exact $\sqrt{n}$ rate (needs i.i.d. plus attainability); unbiasedness, since an asker choosing each question from the last answer is a biased estimator by construction; and variance as the loss for discrete choices, where the relevant quantity is error probability or posterior [[entropy]] |

## Limits

- Applies to unbiased estimators of a **continuous** parameter with a regular
  likelihood. Most design questions are discrete choices, where the relevant
  quantity is error probability, not variance.
- The $\sqrt{n}$ rate needs i.i.d. observations *and* an attaining estimator.
  Self-generated questions supply neither — see Transfer.
- A lower bound on variance; it does not say the bound is reached, so it
  cannot be read as a promise of precision, only as a ceiling on it.
- The 10,000-question block and the diversity claim are **this wiki's
  inference under an idealisation the note itself denies**. Nothing in Rao
  (1945) or Cramér (1946) concerns question design; if the idealisation
  fails, only the diminishing-returns shape carries, not the number.

## Related

[[fisher-information]] · [[adaptive-submodularity]] · [[likelihood-ratio]] · [[tree-search-methods]]

[^s1]: rao-1945
[^s2]: cramer-1946
[^s3]: lehmann-1998
