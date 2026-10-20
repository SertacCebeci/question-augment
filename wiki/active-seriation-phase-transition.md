---
description: "Recovering a latent ordering from adaptively chosen noisy pairwise similarities has a sharp threshold at SNR of order ln n: below it no algorithm works, above it error decays exponentially."
aliases: ["active seriation", "ASII", "ordering recovery by iterative insertion"]
sources: ["arxiv-2603-15336"]
---
# Active seriation phase transition

Active seriation asks a learner to recover an unknown ordering of n items by choosing which pairs to measure, each measurement being a noisy similarity drawn from a permuted Robinson matrix (similarity falls as positions move apart).[^c1] It differs from active ranking, which asks "is i preferred to j?" and infers a total order from directional comparisons; seriation instead uses proximity scores that must stay globally consistent.[^c2]

## The threshold

Difficulty is governed by the signal-to-noise ratio of order Delta^2 T / (sigma^2 n): observations per item times SNR per observation. The paper reports a phase transition at SNR of order ln n: below it recovery is information-theoretically impossible, above it the error decays exponentially in the SNR, and no algorithm decays faster.[^c3] Theorem 4.2 states that below the threshold, for any algorithm some admissible matrix gives error at least 1/2.[^c4] Above it, ASII's error is at most exp(-SNR/2400).[^c5] The matching lower bound is exp(-8 SNR), so the exponent is optimal up to constants.[^c6]

## The mechanism that attains it

ASII inserts items one at a time into an ordered list by binary search. Each comparison, TEST, looks at three empirical similarities (k to l, k to r, l to r) and takes the smallest as the farthest-apart pair; if l-r is smallest, k lies between.[^c7] Each test gets only a small budget, just enough for constant success probability, so single tests are unreliable; a backtracking mechanism detects inconsistent search paths and corrects them, and the search succeeds whenever correct local decisions outweigh incorrect ones.[^c8] Reliable (larger-budget) tests are spent only at a few critical steps. The algorithm needs no knowledge of sigma or Delta.[^c9]

## What this suggests for asking (my inference)

Many cheap, individually unreliable questions plus a way to retract earlier conclusions can match what expensive reliable questions would achieve, provided answers are correct more often than not. This is my reading of the mechanism, not something the paper tests outside seriation.

## Limits

Guarantees assume a uniform minimal gap Delta between adjacent similarities (relaxed in a later theorem), sub-Gaussian noise, and a per-observation SNR at most 1. Lower bounds are proved only for a Gaussian Toeplitz instance and for from-scratch seriation; the paper notes it is unresolved whether the lower bound extends to the whole complementary regime. The constants (2400, 8) are not tight. Nothing here concerns human or language-model answerers; the link to question asking is by analogy only.

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — another sample-complexity limit on adaptive sampling, for independent arms rather than interdependent items
- [[one-bit-mean-estimation]] — also fixes what adaptivity can and cannot buy
- [[active-testing]] — adaptive choice of what to query
- [[plug-in-glr-stopping-rule]] — sequential identification under noise

[^c1]: arxiv-2603-15336 — "The observations are noisy measurements of entries"
[^c2]: arxiv-2603-15336 — "seriation relies on pairwise similarity information, which encodes proximity rather than preference."
[^c3]: arxiv-2603-15336 — "below this threshold, ordering recovery is information-theoretically impossible"
[^c4]: arxiv-2603-15336 — "Then, for any algorithm A, there exists a matrix M ∈ M∆ such that the error probability of A"
[^c5]: arxiv-2603-15336 — "Once the SNR, ∆2 T /(σ 2 ñ), exceeds a logarithmic threshold in n, the error probability of ASII"
[^c6]: arxiv-2603-15336 — "no algorithm can achieve a faster decay rate, establishing optimality in this regime."
[^c7]: arxiv-2603-15336 — "its similarity to both l and r tends to be higher than the similarity between l and r themselves."
[^c8]: arxiv-2603-15336 — "local mistakes from propagating irreversibly. Theoretical analysis shows that, as long as the number"
[^c9]: arxiv-2603-15336 — "The algorithm is fully data-driven"
