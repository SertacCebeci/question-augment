---
description: "What \"certain enough\" means, once a tolerance is written down. The theorem Shannon fixes a **single-letter distortion measure** in advance: a non-negative matrix $d_{ij}$,"
aliases: ["R(D)", "rate–distortion function", "lossy compression bound", "distortion-rate function"]
sources: ["shannon-1959", "cover-2006", "arxiv-2601-00938", "doi-10-48550-arxiv-2407-15504"]
---
# Rate–distortion theory

> What "certain enough" means, once a tolerance is written down. The theorem
> a [[stopping-rules|stopping condition]] can be modelled on — not a [[question-budgets|question budget]].

## Theorem (Shannon, 1959)

Shannon fixes a **single-letter distortion measure** in advance: a[^s1][^s2]
non-negative matrix $d_{ij}$, the cost of reproducing source letter $i$ as
letter $j$. For a tolerated average distortion $D$ the modern statement of
the rate–distortion function (Cover & Thomas, 2006) is

$$R(D) = \min_{p(\hat{x}\mid x)\ :\ \mathbb{E}[d(X,\hat{X})]\leq D} I(X;\hat{X})$$

Three results of the 1959 paper carry the weight here:

1. **Shape.** In the section *Convexity of the $R(d)$ Curve*, Shannon shows
   $R(d)$ is convex downward and strictly monotonically decreasing between
   $d_\min$ and $d_\max$ — **less distortion costs more bits, and the last
   bits are the dearest.**
2. **A tolerance at which nothing need be sent.** $R = 0$ holds exactly when
   the reproduction distribution does not depend on the source letter at
   all, which happens from $d_\max = \min_j \sum_i P_i d_{ij}$ upward. Above
   that tolerance the optimal system ignores the source.
3. **Operational meaning.** For coding purposes at tolerated distortion $d$
   the source behaves like one of rate $R(d)$: over a memoryless channel of
   capacity $C$ no system beats $C/R(d)$ source letters per second within
   distortion $d$, and long block codes approach it.

$R(D)$ is a function of a *given* $d_{ij}$ and a *given* source
distribution. Both are inputs, not outputs, of the theory.

## Known as

| Field | Name there | Kind |
|---|---|---|
| Information theory | rate–distortion function, $R(D)$ | exact — the function is the object this note states theorems about |
| Information theory / data compression | lossy compression bound | close — names the bound $R(D)$ imposes on lossy coders, not the function and its properties |

## What this suggests for stopping (conjecture)

**The mapping rate $\to$ number of questions is this wiki's inference, not
part of Shannon (1959).** Shannon's rate is bits per source letter under a
stated distortion matrix; a questioner has neither the matrix nor the source
distribution. What the analogy takes is the *structure* of the claim, not
its number.

Read that way, the theory answers *does a throwaway task deserve the same
question budget as a critical one?* with **no — because $D$ differs**:

```text
Low-fidelity story for personal reading  →  D large  →  R(D) small  →  (read here as) few questions
Software going to production             →  D small  →  R(D) large  →  (read here as) many questions
```

Under the same reading, *"it doesn't matter"* is not the removal of
uncertainty but a **declaration of distortion tolerance** — and result 2
gives the extreme case a precise home in the home field: past $d_\max$ the
optimal system stops listening to the source entirely.

## What convexity says

Convexity is proved; what follows it here is analogy, and this wiki's own:

- The curve's cheap end comes first and its dear end last — the *shape*,
  never a number. This note claims no split such as "the final 5% costs more
  than the first 95%"; any such figure would be illustration, not a result.
- *Parking* a question behind a trigger that reopens it is **consistent with
  that shape** — a convex curve is exactly where leaving distortion on the
  table is cheap — but the analogy establishes **no optimality**. An
  optimality claim would need a stated $d$, a cost per question and a
  decision rule; none exists here, and Shannon proves nothing about parking.

## Transfer

| | In its home field | Here |
|---|---|---|
| Source $X$ | a random sequence | the design being settled |
| Reconstruction $\hat X$ | the decoded sequence | what actually gets built |
| Distortion $d$ | a stated matrix $d_{ij}$, fixed before $R$ exists | "how wrong is acceptable" — **unstated** |
| Rate | bits per symbol | questions asked — this wiki's reading, not Shannon's |
| What survives | stopping is relative to a declared tolerance; the marginal cost of fidelity rises as $D$ falls; there is a tolerance above which zero information is required | |
| What does not | the $R(D)$ curve itself, since $d$ is undefined; the asymptotic guarantee; any optimality claim about parking a question — no such result exists in the home field to survive | |

## Limits

- Needs a distortion measure $d(x,\hat{x})$ and a source distribution.
  Neither exists for a design; see Transfer.
- $R(D)$ is asymptotic in sequence length (long block codes).
- Counting questions as rate, and the conclusion that parking is optimal,
  are this wiki's inferences (conjecture); Shannon (1959) proves neither.
  Reading *"it doesn't matter"* as raising $D$ is the same kind of
  interpretation.
- Convexity gives the *shape* of the cost curve, never a number, and only
  after $d_{ij}$ is fixed — changing the tolerance measure changes the
  curve.
- The compressed-query-delegation paper (arxiv-2601-00938) reads its query budget as a rate–distortion constraint, but its "rate" is a rank count, not an entropy.[^s3] Its budget is a proxy, the product of the retained ranks, and its distortion is the Frobenius error of a given matrix.[^s4] The optimality it proves is truncated SVD at fixed rank (Eckart–Young). My reading: that fixes no source distribution and proves neither converse nor achievability, so it is not an R(D) result.
- `shannon-1959` is the IRE International Convention Record, vol. 7, part 4
  (1959), pp. 142–163; the statements above were read from the reprint in
  Shannon's *Collected Papers*.
- The prompt-compression paper writes the same trade-off as a distortion-rate function, D\*(R): the smallest distortion reachable at rate at most R, with rate free and distortion the output.[^s5] Read as the inverse of R(D), that is my reading. Its rate is a token-length ratio, not bits, so the operational meaning above does not carry over; see [[query-aware-prompt-compression]].

## Related

[[entropy]] · [[source-coding-theorem]] · [[value-of-information]] · [[possible-worlds]] · [[information-bottleneck]] · [[bounded-rationality]]

[^s1]: shannon-1959
[^s2]: cover-2006
[^s3]: arxiv-2601-00938 — "CQD can be read as a rate–distortion constrained communication scheme"
[^s4]: arxiv-2601-00938 — "a natural budget proxy is"
[^s5]: doi-10-48550-arxiv-2407-15504 — "characterizes the fundamental trade-off between the distortion and the rate"
