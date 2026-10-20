---
description: "A summary carrying all the information the data holds about a **named** Fisher (1922) `fisher-1922`, in the paper that also introduced consistency, efficiency and likelihood,"
aliases: ["sufficiency"]
sources: ["fisher-1922", "neyman-1935", "halmos-1949", "lehmann-1950", "cover-2006"]
---
# Sufficient statistic

> A summary carrying all the information the data holds about a **named**
> parameter. The rest may be discarded — and "the rest" is defined only once
> that parameter is named.

## Definition

Fisher (1922) `fisher-1922`, in the paper that also introduced consistency,[^s1][^s2][^s3][^s4][^s5]
efficiency and likelihood, defined sufficiency: a statistic is sufficient when
it summarises the whole of the relevant information the sample supplies about
the parameter. In the modern form, $T(X)$ is sufficient for $\theta$ iff the
conditional law of the data given the statistic is free of the parameter:

$$p(x \mid T(x) = t,\ \theta) \ \text{does not depend on}\ \theta.$$

Two things must be fixed before the definition can even be stated: a family
$\{p(\cdot\mid\theta) : \theta \in \Theta\}$, and $\theta$ itself. Sufficiency
is a two-place predicate — $T$ is never sufficient, only sufficient **for**
$\theta$.

## Fisher–Neyman factorization

Neyman (1935) `neyman-1935` characterised sufficiency algebraically: $T$ is
sufficient iff the density factorises as

$$p(x\mid\theta) = h(x)\, g_\theta(T(x))$$

*Assumptions:* the family is **dominated** — every $p(\cdot\mid\theta)$ has a
density with respect to one common $\sigma$-finite measure — and $T$ is
measurable. Halmos & Savage (1949) `halmos-1949` proved the criterion in this
general measure-theoretic form via the Radon–Nikodym theorem, and showed where
it stops: for non-dominated families the factorization criterion fails, and
only a weaker *pairwise* sufficiency survives. Read plainly: if the likelihood
touches the data only through $T(x)$, nothing else in $x$ moves the inference
about $\theta$.

## Minimal sufficiency

Many sufficient statistics exist — the data itself is one. Lehmann & Scheffé (1950) `lehmann-1950` introduced the **minimal** one: a sufficient statistic
that is a function of every other sufficient statistic, i.e. maximal
compression that is still sufficient. In inquiry terms, "the fewest fixed
decisions". Their construction runs on likelihood ratios: two samples map to
the same value iff $p(x\mid\theta)/p(y\mid\theta)$ is free of $\theta$.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Statistics (Fisher 1922) | *sufficiency* — the property; *sufficient statistic* — the function that has it | exact |

**Not this concept.** *Fisher–Neyman factorization* is not another name for a
sufficient statistic: it is the criterion characterising one — a theorem
*about* the object, holding only for dominated families, and stated in its own
section above. *Blackwell sufficiency* ([[blackwell-informativeness]]) is a
third object: an ordering of whole experiments, not a function of one sample.

## Why it matters — what distillation would have to be

> The identification of distillation with sufficiency below is **this wiki's
> conjecture, not a result**. No theorem in estimation identifies a design
> distillate with a sufficient statistic.

Sufficiency supplies the only precise form of "loses nothing": a summary loses
nothing *relative to a declared $\theta$*. Read onto stall 8:

```text
10,000 question–answer pairs
        ↓ distillation
the minimal summary sufficient for θ = the design decision
```

Two readings follow, of unequal strength:

1. **The discipline (this is what carries).** Nothing may be dropped from the
   record until the $\theta$ it would be sufficient for is named. Without a
   named target there is no lossless/lossy distinction at all — only a
   preference. [[information-bottleneck]] takes the same step by declaring a
   relevance variable $Y$.
2. **Adds nothing (a different theorem's consequence).** $T = f(X)$ is a
   processing of $X$, so by the data-processing inequality `cover-2006` it
   cannot add information about $\theta$ — see [[data-processing-inequality]].
   Practical rule: an item in the distillate that rests on no question rests
   on a hidden assumption, and should go back as an unanswered question. This
   consequence is the DPI's, not sufficiency's.

Losslessness here is **not** a guarantee. It is checkable only where
$p(x\mid\theta)$ is written down; for a design it is not written down. See
Transfer.

## Transfer

| | |
|---|---|
| **Estimation (home field)** | $x$ = observations from a dominated family $p(x\mid\theta)$; $\theta$ = a parameter of that family; $T$ = a measurable function of $x$ |
| **Here** | $x$ = the question–answer record; $T$ = the distilled specification; $\theta$ = "the design" — named nowhere, modelled by nothing |
| **What survives** | only the two-place form of the predicate: sufficiency is always sufficiency *for* a stated $\theta$, so the import forces "sufficient for what?" to be answered before anything is deleted. That is definitional, not a consequence of any theorem — and with $\theta$ unmodelled it is all that survives; the import is a discipline of naming the target, not a theorem one can apply |
| **What does not** | the factorization criterion (no likelihood, no dominated family, no measurable $T$); losslessness as a *guarantee* (a statement about $p(x\mid\theta)$, which does not exist here); minimality as something checkable (Lehmann–Scheffé's construction needs a [[likelihood-ratio|likelihood ratio]] for every pair of samples) |

## Limits

- Sufficiency is relative to a family and a parameter. For a design neither is
  specified, so "the minimal summary sufficient for the decision" is a
  metaphor until $\theta$ is defined — that is this note's own claim, and it
  is why the map row for stall 8 must not assert losslessness.
- Sufficient *for $\theta$*, nothing else. A distillate sufficient for today's
  decision may discard what tomorrow's $\theta$ needs, and the theorem gives
  no warning when $\theta$ changes.
- The factorization criterion assumes a dominated family; Halmos & Savage
  (1949) show it fails outside one.
- Minimality is not checkable from a record alone: it is defined through
  likelihood ratios, which a free-text transcript does not supply.
- Attributions here are to the published works — Fisher 1922 (*Phil. Trans. R.
  Soc. A* 222), Neyman 1935 (*Giornale dell'Istituto Italiano degli Attuari*
  VI), Halmos & Savage 1949 (*Ann. Math. Statist.* 20), Lehmann & Scheffé 1950
  (*Sankhyā* 10) — located through their published listings, not by reading
  each original page by page. `fisher-1922`, `neyman-1935` and `lehmann-1950`
  count as `[?]` until the verifier confirms them; `cover-2006` carries
  `verified: prior`. No page or theorem number is asserted.

## Related

[[data-processing-inequality]] · [[likelihood-ratio]] · [[constraint-as-information]] · [[information-bottleneck]] · [[blackwell-informativeness]]

[^s1]: fisher-1922
[^s2]: neyman-1935
[^s3]: halmos-1949
[^s4]: lehmann-1950
[^s5]: cover-2006
