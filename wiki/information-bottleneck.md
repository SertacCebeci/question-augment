---
description: "Compression has no meaning until you name what the compressed thing is Given the joint $p(X,Y)$ — $X$ the record to compress,"
aliases: ["IB", "information bottleneck method", "IB Lagrangian", "IB curve"]
sources: ["kolchinsky-2019", "shamir-2010", "tishby-1999"]
---
# Information bottleneck

> Compression has no meaning until you name what the compressed thing is
> *for*. Declare the relevance variable and the distortion measure stops
> being your choice — it is derived.

## Mechanism (Tishby, Pereira & Bialek, 1999)

Given the joint $p(X,Y)$ — $X$ the record to compress, $Y$ the **relevance[^s1][^s2][^s3]
variable** — find the bottleneck $\tilde X$ minimising

$$\mathcal{L}[p(\tilde x \mid x)] = I(\tilde X;X) - \beta\, I(\tilde X;Y)$$

At a stationary point three equations hold simultaneously:

$$p(\tilde x\mid x) = \frac{p(\tilde x)}{Z(x,\beta)}\exp\big[-\beta\, D_{KL}[p(y\mid x)\,\|\,p(y\mid \tilde x)]\big]$$

with $p(\tilde x)$ and $p(y\mid\tilde x)$ the induced marginal and Bayes
update. Iterating them converges.

Two things this settles that neither neighbour does:

1. **The distortion is not an input.** Tishby et al. state the [[kl-divergence|KL divergence]]
   "emerged as the relevant 'effective distortion measure' from our
   variational principle but is not assumed otherwise anywhere". Where
   [[rate-distortion-theory]] leaves $d(x,\hat x)$ undefined for a design,
   IB replaces that free choice with a single declaration: *what is this
   distillate for?*
2. **Sufficiency becomes graded.** [[sufficient-statistic]] is a predicate —
   lossless or not. IB gives a curve: for each compression level
   $I(\tilde X;X)$, the maximum recoverable $I(\tilde X;Y)$. Exact
   sufficiency is the special case; the 1999 paper notes that only "where
   there exist sufficient statistics" can almost all relevant information be
   kept at finite $\beta$ with significant compression.

## Why it matters

Stall 8 asks how the surviving answers become one artifact. IB says the
question "what may be dropped from the record?" is unanswerable as posed and
becomes answerable the moment a target variable is named — and that the
right thing to drop is what changes $p(y\mid x)$ least, not what is
shortest or least frequent. It also replaces "distil, then check" with a
knob: $\beta$ is the price of a bit of record in units of decision-relevant
information, and moving it traces the whole family of admissible
distillates rather than one.

## Transfer

| | In its home field | Here |
|---|---|---|
| $X$ | a source variable with known statistics | the answer record |
| $Y$ | a co-occurring relevance variable (document label, word context) | the decision the distillate serves |
| $p(X,Y)$ | estimated from a corpus | **not available**; there is one session, not a sample |
| What survives | the requirement that compression declare a relevance variable; the derivation of the distortion from $p(y\mid x)$; the curve replacing the lossless/lossy predicate | |
| What does not | the algorithm — the self-consistent equations need $p(X,Y)$ and are not run on one session's transcript; the convergence guarantee, which is to a stationary point only | |

## Limits

- **Non-convexity.** The functional is convex in each distribution
  separately but not jointly; the authors state their "convergence proof
  does not imply uniqueness of the solution". Different $\beta$ schedules
  give different distillates of the same record.
- **Deterministic degeneracy.** Kolchinsky, Tracey & Van Kuyk (ICLR 2019)
  show that when $Y$ is a deterministic function of $X$, the IB curve cannot
  be recovered by maximising the Lagrangian over $\beta$, and every point of
  the curve is attained by trivial solutions. If the artifact is fully
  determined by the answers already given — the ordinary case for a
  specification — IB stops discriminating between distillates.
- **Estimation.** IB is stated over a known joint distribution; practice
  uses a plug-in empirical estimate. Shamir, Sabato & Tishby (2010) supply
  finite-sample bounds, with the gap between empirical and true $I(\tilde
  X;Y)$ controlled by $I(\tilde X;X)$ — a guarantee about a sample of pairs,
  not about a single dialogue.
- The relevance variable is an input the theory does not supply. It renames
  [[sufficient-statistic]]'s unspecified $\theta$ rather than removing it;
  what it adds is that the *distortion* need not also be specified.

## Related

[[sufficient-statistic]] · [[rate-distortion-theory]] · [[mutual-information]] · [[kl-divergence]] · [[data-processing-inequality]]

[^s1]: kolchinsky-2019
[^s2]: shamir-2010
[^s3]: tishby-1999
