---
description: "Accumulate the log-[[likelihood-ratio|likelihood ratio]] of each observation, reset the sum to"
aliases: ["cumulative sum control chart", "Page's test"]
sources: ["lorden-1971", "moustakides-1986", "page-1954"]
---
# CUSUM — Page's cumulative sum

> Accumulate the log-[[likelihood-ratio|likelihood ratio]] of each observation, reset the sum to
> zero whenever it would go negative, alarm when it crosses a threshold — the
> procedure that minimises detection delay at a fixed false-alarm rate.

## The rule (Page, 1954)

$$S_n = \max(0,\ S_{n-1} + \log\Lambda(x_n)), \qquad \text{alarm: } S_n > h$$[^s1][^s2][^s3]

The only difference from [[sprt]] is the **reset at zero**, which lets it
continuously monitor the "no change yet" state from a fresh baseline.

## Optimality

Lorden (1971) proved asymptotic and Moustakides (1986) exact optimality: at a
given false-alarm rate (average [[run-length|run length]] to a false alarm), Page's stopping
time minimises the worst-case expected detection delay.

## Known as

| Name | Field | Relation |
|---|---|---|
| cumulative sum control chart | statistical process control | exact — the chart is this recursion plotted |
| Page's test | sequential analysis | exact — after Page (1954) |
| quickest change detection | detection theory | **not** this concept — the *problem* CUSUM solves (minimise delay subject to a false-alarm constraint), for which [[e-detector]], [[conformal-test-martingale]] and [[scan-b-statistic]] are rival procedures with different guarantees; naming the problem after one algorithm hides that the guarantees differ |

## Why it matters — ancestor–descendant contradiction

*This wiki's inference, not a result of the literature.* It holds only given a
surrogate for $\log\Lambda$ over answers, which no source read here supplies —
see Transfer.

An answer can invalidate an upstream decision, and catching this by pairwise
comparison of answers is expensive ($O(n^2)$). Monitoring the stream is the
alternative shape:

```text
For each new answer:  how surprising is it under the current model?
Accumulate:           S_n += log Λ(answer)
Threshold crossed:    "the model has shifted" — an upstream decision is strained
```

*If* a per-answer surrogate for $\log\Lambda$ exists, monitoring costs $O(n)$
per answer where pairwise comparison costs $O(n^2)$; without one the
comparison is not available, because the left-hand side is undefined. The same
condition governs the cheaper-than-re-asking reading: instead of re-asking for
a repeat-stability check, watch whether the deviation **accumulates** — again
only once something accumulable has been defined.

## The distinction: noise or real change

A single $\log\Lambda(x_n)$ is a noisy statistic: its sign flips from
observation to observation even while nothing has changed. Its *drift* does
not. Under the pre-change law the expected increment is $-D_{KL}(f_0\|f_1) <
0$, so the reset at zero pins the sum near the floor; under the post-change law
the expected increment is $+D_{KL}(f_1\|f_0) > 0$ and the sum walks up. That
sign change in the drift, not in any one observation, is what the threshold
reads — the separation Page (1954) buys (see [[kl-divergence]]).

Whether the same separation holds between *answer* noise and a genuinely
underspecified design is untested here and depends entirely on the surrogate:
the argument above is about a likelihood ratio between two known laws, which
free-text answers do not supply.

## Transfer

| | In its home field | Here |
|---|---|---|
| Stream | scalar observations | a sequence of answers |
| $\Lambda(x_n)$ | ratio of known pre/post-change densities | undefined — needs a surrogate for "how surprising under the current model" |
| Alarm | "the process has shifted" | "the model has shifted" — but not *where* |
| What survives | accumulate-then-threshold; one surprise is noise, accumulated drift is change | |
| What does not | the $O(n)$ cost as stated; the optimality results; any localisation of the strained decision; the fixed pre-change law an adaptive asker moves | |

## Limits

- Needs a per-observation log-likelihood ratio between pre- and post-change
  distributions. Free-text answers supply none; without a surrogate the
  $O(n)$ claim in this note is **not earned** — see Transfer.
- Assumes the pre-change law is fixed while the stream runs. When the asker
  changes the question adaptively, the distribution of answers moves for
  reasons that are not the answerer's drift, and the alarm cannot tell the two
  apart — the same trade-off map-consistency records for
  [[conformal-test-martingale]].
- Detects *that* a change occurred and roughly *when*. It does not say *which*
  upstream decision is strained; localisation is a separate problem this
  note does not solve.
- Lorden and Moustakides optimality assume i.i.d. observations and a known
  post-change distribution.

## Related

[[sprt]] · [[likelihood-ratio]] · [[kl-divergence]] · [[semantic-entropy]] · [[e-detector]]

[^s1]: lorden-1971
[^s2]: moustakides-1986
[^s3]: page-1954
