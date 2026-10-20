---
description: "For sequential tests on a Markov chain, expected stopping time scales as log(1/alpha) over a stationary-weighted KL projection onto the null; the weights are fixed by the data, not chosen."
aliases: ["Markovian sequential testing lower bound", "stationary-weighted KL divergence", "Markov KL projection hardness"]
sources: ["arxiv-2602-17587"]
---
# Stationary-weighted KL hardness of sequential testing

When observations come from an ergodic finite-state Markov chain with unknown transition matrix Q, the number of samples any valid sequential test needs to reject a null class P of matrices is governed by one quantity: the divergence between Q and the nearest member of P, with each state's row-wise KL weighted by how often Q visits that state. This is the Markovian counterpart of the i.i.d. rule that expected sample size is roughly the evidence required divided by the per-observation KL (see [[sprt]], [[kl-divergence]]).

## The quantity

Definition: D_M(Q,P) = sum over states i of pi_i * KL(Q(i,.), P(i,.)), where pi is the stationary distribution of Q.[^c1] The hardness of certifying Q against the null class is the infimum of this over P in the null class, written D_M^inf(Q, P-class).[^c2]

## The bound

For every alpha in (0,1), any alpha-correct, power-one test satisfies, for every P in the null, E_Q[tau] >= (log(1/alpha) - Poisson correction) / D_M(Q,P). The correction is the expected difference of a Poisson-equation solution between start and stopping state.[^c3] Optimising over P and bounding the correction uniformly gives a second form, in which log(1/alpha) is reduced by 2C_Q / min_i pi_i before dividing by D_M^inf.[^c4] As alpha goes to 0 the ratio E_Q[tau]/log(1/alpha) is at least 1 / D_M^inf, and the paper gives a test that matches this to first order.[^c5]

The proof applies a Markov-chain version of Wald's lemma to write the expected log-likelihood ratio as E[tau] D_M plus a Poisson-solution term, then uses data processing to link that ratio to the error level.[^c6] The constant C_Q depends on how well Q mixes; in the i.i.d. case (identical rows) it is exactly 2.[^c7]

## Why the weights matter

Earlier non-asymptotic bounds from MDP best-policy identification optimise the state weights, giving denominators sup over w of inf over P of w'f_P. In the Markov-chain testing setting this is loose: the optimiser puts all mass on the state with the largest KL term, which cannot be achieved because visitation is dictated by Q.[^c8] The asker cannot steer the data to the most informative state; the chain's own occupancy decides which rows of evidence arrive. (This reading as a statement about questioning is mine.)

A composite null is also harder than a known singleton: the test must rule out every P in the null while keeping uniform Type-I control, which is why the infimum over P appears.[^c9] The correction term depends on P, so taking a supremum over P as in the i.i.d. analysis can make it arbitrarily large; the paper controls it using a constant depending only on Q.[^c10]

## Limits

- Finite-state, ergodic chains with a known state space; the bound's non-asymptotic form carries a mixing constant and a 1/min pi factor that can be loose for slowly mixing or rarely visited states.
- Matching test is optimal only to first order as alpha goes to 0; at moderate alpha the gap is not characterised here.
- The tractable test variant, built from a Pinsker-type lower bound, is described as conservative; its sample cost was not measured against the bound by me.
- Nothing here concerns questioning directly; the questioner reading is my inference, with no measurement.

## Related

- [[sprt]] — the i.i.d. two-simple-hypotheses ancestor; this bound replaces per-sample KL with a stationary-weighted one
- [[kl-divergence]] — the row-wise divergence being weighted
- [[hypothesis-testing]] — the composite-versus-composite setting
- [[stopping-rules]] — stopping on accumulated evidence, here under dependence

[^c1]: arxiv-2602-17587 — "DM ( Q, P) := ∑ πi DKL ( Q(i, ·), P(i, ·)) ,"
[^c2]: arxiv-2602-17587 — "inf ( Q, P ) is the fundamental instance-dependent"
[^c3]: arxiv-2602-17587 — "Theorem 3.3 (Lower bound). Fix α ∈ (0, 1) and an ergodic Q ∈ Q with stationary distribution π ⊤ ∈ Rm ."
[^c4]: arxiv-2602-17587 — "To obtain (3), we optimize over P ∈ P and"
[^c5]: arxiv-2602-17587 — "We then construct a sequential"
[^c6]: arxiv-2602-17587 — "Proof sketch. We apply a Markov-chain version of Wald’s lemma (Moustakides, 1999) to express the"
[^c7]: arxiv-2602-17587 — "When γps = 1, the chain behaves as in the i.i.d. case: P has identical rows equal to its stationary"
[^c8]: arxiv-2602-17587 — "all mass on the state with the largest KL term, which is not achievable when the visitation proportions"
[^c9]: arxiv-2602-17587 — "the test must rule out every P ∈ P while maintaining uniform Type-I control. This necessity of"
[^c10]: arxiv-2602-17587 — "can make the correction term arbitrarily large and destroy the bound. We avoid this"
