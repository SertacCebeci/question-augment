---
description: "The maximum rate at which information can be sent over a noisy channel with Shannon (1948,"
aliases: ["Shannon capacity", "information capacity"]
sources: ["shannon-1948", "shannon-1956", "schalkwijk-1966", "cover-2006"]
---
# Channel capacity

> The maximum rate at which information can be sent over a noisy channel with
> arbitrarily small error — and the reason feedback makes asking cheaper
> without making it reach further.

## Definition

$$C = \max_{p(x)} I(X;Y)$$[^s1][^s2][^s3][^s4]

Shannon (1948, *A Mathematical Theory of Communication*) defined this quantity
and proved the **channel coding theorem**: for any rate $R < C$ there are codes
whose error probability goes to zero with block length; for $R > C$ it cannot.
Cover & Thomas (2006) call $\max_{p(x)} I(X;Y)$ the *information* capacity and
the largest achievable rate the *operational* capacity; the coding theorem is
the statement that the two coincide.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Information theory | Shannon capacity | exact — the standard name for $C$ of a channel |
| Information theory | information capacity | exact — Cover & Thomas's name for $\max_{p(x)} I(X;Y)$ before the coding theorem identifies it with the operational rate |
| Information theory | channel coding theorem | close — not a quantity but the theorem that gives $C$ its operational meaning; it can be stated and fail to be tight for other channel classes |
| Information theory | feedback capacity $C_{FB}$ | close — a **different** quantity, measured separately; it equals $C$ only under the memoryless assumption (Shannon 1956) and is strictly larger for some channels with memory |
| Combinatorics | Shannon capacity of a graph $\Theta(G)$ | **not this concept** — the zero-error capacity of the confusability graph, a different number for the same channel, and one that feedback *can* raise |

## What feedback buys

For a **discrete memoryless** channel, feedback does not increase capacity:
$C_{FB} = C$ (Shannon 1956, *The Zero Error Capacity of a Noisy Channel*, which
proves the ordinary capacity is unchanged by feedback while showing the
zero-error capacity may increase).

What it does buy is **engineering**: Schalkwijk & Kailath (1966) gave a scheme
for the additive white Gaussian noise channel with noiseless feedback in which
the transmitter simply corrects the receiver's current estimate, and the error
probability at fixed $R < C$ decays *doubly* exponentially in the coding delay
— far faster than the single exponential of the best feedback-free codes, and
with a much simpler encoder and decoder. Same reach, cheaper and shorter route.

## Why it matters — this note's conjecture, not a corollary

> The mapping below is this wiki's inference from $C_{FB}=C$, not a result of
> information theory. Capacity theory is about a fixed known channel; nothing
> in it is about questions.

```text
BATCH      generate the whole question set up front, then answer them all
ADAPTIVE   ask, take the answer, choose the next question accordingly
```

Read through the theorem, adaptivity is a **feedback link, not a wider
channel**: seeing each answer before choosing the next question does not raise
the total information the answerer can supply. What the feedback analogy
predicts is what feedback actually buys in the theorem — lower scheme
complexity, a shorter horizon to a given confidence, and robustness to a bad
early guess.

The *fewer questions* claim is a different result and does not come from here.
It comes from adaptivity under a non-uniform, unknown answer distribution:
splitting the remaining mass at each step ([[generalized-binary-search]],
[[twenty-questions]]), where the batch scheme must fix all its questions
against the prior alone. Capacity theory supplies no such gap.

This note's reading of the [[question-burst]] rule ("generate first, answer
none") is therefore a **phase** claim, not a resolution derived above:

- **Batch is right for divergence** — no framing collapse before information exists
- **Adaptive is right for narrowing** — each answer steers the next

## Transfer

| | In its home field | Here |
|---|---|---|
| The object | a fixed noisy map $p(y\mid x)$, input to output | the answerer, as a stochastic map from question to answer |
| Feedback | the receiver returns what arrived before the next symbol is sent | the asker reads each answer before choosing the next question |
| What survives | feedback buys complexity, delay and error exponent, not rate | the batch/adaptive difference is about horizon and robustness, not about how much can be learned in total |
| What does not | $C$ itself, which needs a known stationary $p(y\mid x)$ over a fixed input alphabet, and the asymptotic block length | no numeric capacity exists for a human or model answerer; $C_{FB}=C$ fails once the channel has memory |

## Limits

- **The transfer's own assumption**: capacity is defined only for a *fixed,
  known* channel law. The asker knows neither $p(y \mid x)$ nor the input
  alphabet of admissible questions, and the answerer's conditional
  distribution is question-dependent. So "the same total information" is a
  structural reading, not a computable equality — there is no $C$ to compare
  batch against adaptive with.
- $C_{FB} = C$ holds for **memoryless** channels. A human answerer has memory
  (fatigue, anchoring, the framing of earlier questions); a model answerer has
  context. Both are channels with memory, where feedback can change what is
  reachable — and Shannon (1956) already shows a companion quantity (zero-error
  capacity) that feedback does raise.
- Capacity is an asymptotic long-block result; a conversation is nowhere near
  that regime. Schalkwijk–Kailath is an AWGN, noiseless-feedback result and
  does not transfer to a noisy or delayed feedback link.
- `schalkwijk-1966` is recorded by one database as 1968 (the IEEE DOI and the
  journal volume are 1966); treat the year as `[?]` until the verifier settles
  it.

## Related

[[mutual-information]] · [[twenty-questions]] · [[generalized-binary-search]] · [[question-burst]] · [[sprt]] · [[renyi-ulam-problem]] · [[semiotic-channel-capacity]] (a capacity taken as a maximum over one generation knob, not over all input laws)

[^s1]: shannon-1948
[^s2]: shannon-1956
[^s3]: schalkwijk-1966
[^s4]: cover-2006
