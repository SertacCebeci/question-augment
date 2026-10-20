---
description: "How much information an observation carries about a parameter, **locally**. Fisher (1922) introduced the quantity as the *intrinsic accuracy* of an error curve and named it the *amount of informati…"
aliases: ["Fisher information matrix", "score variance"]
sources: ["fisher-1922", "fisher-1925", "lehmann-1998", "amari-2000", "efron-1978", "arxiv-2512-19057", "arxiv-2512-00439"]
---
# Fisher information

> How much information an observation carries about a parameter, **locally**.

## Definition (Fisher, 1922; 1925)

$$\mathcal{I}(\theta) = \mathbb{E}\left[\left(\frac{\partial}{\partial\theta}\log p(X\mid\theta)\right)^2\right] = -\mathbb{E}\left[\frac{\partial^2}{\partial\theta^2}\log p(X\mid\theta)\right]$$[^s1][^s2][^s3][^s4][^s5]

Fisher (1922) introduced the quantity as the *intrinsic accuracy* of an error
curve and named it the *amount of information* in Fisher (1925).

**The two forms are one quantity only under the usual regularity conditions**
(Lehmann & Casella, 1998): the support of $p(x\mid\theta)$ does not depend on
$\theta$, $\log p$ is twice differentiable in $\theta$, and differentiation may
be exchanged with integration. Those same conditions give
$\mathbb{E}[\partial_\theta \log p] = 0$, which is what makes the first form a
*variance* of the score rather than a bare second moment. Where the support
moves with $\theta$ — a uniform on $[0,\theta]$ — the identity fails and this
note does not apply.

Under them, $\mathcal{I}(\theta)$ measures the **sharpness** of the
log-likelihood peak. A sharp peak means little uncertainty, hence much
information.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Estimation theory, vector $\theta$ | Fisher information matrix | exact — the same quantity with entries $\mathbb{E}[\partial_i\ell\,\partial_j\ell]$ |
| Mathematical statistics | score variance | exact — the score has mean zero under the regularity conditions above, so the first form *is* its variance |
| Likelihood inference | observed information | **not this concept.** $-\partial^2_\theta\log p(x\mid\theta)$ evaluated at the realised sample (usually at $\hat\theta$) — a random quantity, of which $\mathcal{I}(\theta)$ is the expectation. Efron & Hinkley (1978) compare the two precisely because they differ sample by sample, and argue for the observed one as the variance estimate. A separate object, not a name for this one. |

## Relation to KL

$$\mathcal{I}(\theta) = \left.\frac{\partial^2}{\partial\delta^2}\,D_{KL}\!\left(p_\theta \,\|\, p_{\theta+\delta}\right)\right|_{\delta = 0}
\quad\Longrightarrow\quad
D_{KL}(p_\theta \| p_{\theta+\delta}) = \tfrac{1}{2}\mathcal{I}(\theta)\,\delta^2 + o(\delta^2)$$

The exact statement: Fisher information is the **Hessian of
[[kl-divergence]] at $\delta = 0$** — the leading term of a small-$\delta$
expansion, since $D_{KL}$ is minimised (and its first derivative vanishes) at
$\delta = 0$. It is this Hessian that information geometry takes as a
Riemannian metric on the parameter manifold (Amari & Nagaoka, 2000).

So the two **agree locally and not globally**. For $\delta$ not small the
expansion carries no guarantee, and $D_{KL}$ can be infinite where
$\mathcal{I}(\theta)$ is finite. That is why [[kl-divergence]] files this note
under `equivalence.close` and not `exact`.

## Why it matters

It supplies a distinction between two kinds of uncertainty:

```text
Entropy  →  "how many distinct worlds are possible"   (global, discrete)
Fisher   →  "how much play is there around the right
             answer"                                   (local, continuous)
```

Most design questions are discrete ([[entropy]] applies). Some are continuous:
"refresh interval in seconds", "character limit". For those, entropy is coarse;
the real issue is **how precisely** we need to know — the domain of
[[cramer-rao-bound]] and [[rate-distortion-theory]].

## Transfer

| | |
|---|---|
| In its home field | a parametric likelihood $p(x\mid\theta)$ over a continuous $\theta$, regular in the sense above, with observations drawn from it |
| Here | a continuous design axis — refresh interval in seconds, character limit — with no likelihood over answers, and answers that are not draws from one |
| What survives | the distinction between *counting* worlds and *measuring the residual play* around a value; and that on such an axis the floor on attainable precision is set by the curvature of the evidence, not by the number of questions asked |
| What does not | the scalar $\mathcal{I}(\theta)$ itself — there is nothing to differentiate until a likelihood surrogate is chosen; the additivity $\mathcal{I}_n = n\mathcal{I}_1$, which needs independent answers ([[cramer-rao-bound]]); and any numeric precision claim |

## Used as a design criterion

Where the matrix is the object to be chosen, not only read, it is optimised.
In preference-query design for a regularised multinomial logit model, the
inverse of the regularised matrix at the true parameter bounds the mean
squared error of the regularised maximum-likelihood estimate: the error matrix
"matrix of θλ is controlled by the inverse of the" regularised information,[^s6]
up to a constant that depends on a local consistency radius and holds under
"mild conditions (Appendix B.1)".[^s7] So the inverse matrix is an upper bound
on error, not the error itself. The criteria built on it are in
[[optimal-experimental-design]].

## Used as an item-selection weight

In computerized adaptive testing the same matrix is computed per item. For a
logistic response model with item vector $\alpha_j$ and examinee ability
$\theta$, the paper takes the item's information to be $p_j(1-p_j)\,\alpha_j\alpha_j^\top$,
then replaces the matrix by a scalar, its Frobenius norm, which reduces to
$|\alpha_j|^2\,p_j(1-p_j)$.[^s8] The scalar is normalised over the unselected
pool and used as a sampling distribution for choosing which item to insert in
a mutation step; the paper's stated reason for the scalar is that "directly
manipulating this matrix in the mutation operator is computationally
inefficient" when many candidates are compared.[^s9] The use is in
[[one-shot-adaptive-testing]], where the selected set is fixed before any answer
is seen. The Fisher quantity is the same; the decision it feeds is not.

## Limits

- **Proxy in use.** The scalar is an approximation of the matrix, not the matrix.
  Two items with the same $|\alpha_j|$ and $p_j$ receive the same weight whatever
  direction they load on the ability dimensions. The text read does not compare
  the scalar against the full matrix. This is my inference from the formula.
- **Regularity.** The note's central identity — score variance $=$ expected
  negative Hessian — holds only under the conditions in the Definition
  (fixed support, twice differentiability, differentiation under the integral;
  Lehmann & Casella, 1998). Where they fail, the two displayed expressions are
  different numbers and nothing below survives.
- **Local.** A curvature at a point. Meaningless far from the true parameter or
  for multimodal likelihoods.
- **The KL relation is second-order.** It fixes $\mathcal{I}$ as the Hessian at
  $\delta = 0$ and says nothing about the error at finite $\delta$; "KL and
  Fisher measure the same thing" is false as a global claim.
- Needs a differentiable likelihood in a continuous parameter. Most asking is
  discrete.
- Ties to [[cramer-rao-bound]] only for unbiased estimators.
- Says nothing about **observed information** (see *Known as*): the
  sample-by-sample discrepancy between the two is Efron & Hinkley's (1978)
  subject and is not covered here.

## Related

[[kl-divergence]] · [[cramer-rao-bound]] · [[bayesian-estimation]] · [[entropy]] · [[rate-distortion-theory]] · [[one-shot-adaptive-testing]] (item information as a selection weight)

[^s1]: fisher-1922
[^s2]: fisher-1925
[^s3]: lehmann-1998
[^s4]: amari-2000
[^s5]: efron-1978
[^s6]: arxiv-2512-19057 — "matrix of θλ is controlled by the inverse of the"
[^s7]: arxiv-2512-19057 — "mild conditions (Appendix B.1)"
[^s8]: arxiv-2512-00439 — "Frobenius norm (Peng et al. 2018) as a scalar proxy, yielding"
[^s9]: arxiv-2512-00439 — "directly manipulating this matrix in the mutation operator is computationally inefficient"
