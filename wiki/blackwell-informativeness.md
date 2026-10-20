---
description: "When is one question better than another **for every purpose**? Almost An **experiment** is a Markov kernel $P(\\text{signal} \\mid \\text{state})$ on a known state space."
aliases: ["Blackwell order", "Blackwell sufficiency"]
sources: ["blackwell-1953"]
---
# Blackwell informativeness

> When is one question better than another **for every purpose**? Almost
> never.

## Definition

An **experiment** is a Markov kernel $P(\text{signal} \mid \text{state})$ on a[^s1]
known [[possible-worlds|state space]]. $Q$ is a **garbling** of $P$ when $Q = P M$ for some
stochastic matrix $M$ — $Q$'s output can be produced by feeding $P$'s output
through noise that does not see the state. Write $P \succeq_B Q$ when $Q$ is a
garbling of $P$.

## Blackwell's theorem

Blackwell (1951, 1953) proved the equivalence — Blackwell (1951) introduced
the comparison of experiments and the [[sufficient-statistic|sufficiency]] criterion; Blackwell (1953)
gave the proof without the restriction to finitely many outcomes:

$$P \succeq_B Q \iff \text{for every utility function and every decision
problem, the value of } P \ge \text{the value of } Q.$$

Blackwell (1953) states the value-side comparison as the one introduced for
finite outcome spaces by Bohnenblust, Shapley and Sherman, and removes the
finiteness restriction.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Statistical decision theory | Blackwell order | exact |
| Statistical decision theory / information economics | Blackwell sufficiency | exact |

Two names that are **not** aliases of this concept: *comparison of
experiments* is the problem area the theorem lives in, not the ordering;
*garbling* is the noise-adding operation the ordering is defined by, a
distinct object (defined above).

## Critical: the ordering is very incomplete

The Blackwell order is **partial**. Incomparability is generic: for two
experiments neither of which is a garbling of the other, the theorem supplies
no ranking, and by the equivalence there exist decision problems ranking them
in opposite directions.

## The hard consequence

**Conjecture (this wiki), not part of the theorem.** If a question set behaved
like an experiment — a kernel from an unformalised world state to answers —
then question sets built on different framings would typically be
Blackwell-incomparable, since neither would be a noisy version of the other.
No concrete pair of question sets has been shown incomparable here, and the
mapping from natural-language questions to kernels over a fixed state space is
not established (see `## Transfer`). *If* the analogy holds, then: "which
questioner is better" has an answer only after a specific utility is fixed;
you cannot make a question set universally better, only better relative to a
targeted decision problem; and what could be task-independent is the
**process** of asking, never the set of questions.

## Transfer

| | |
|---|---|
| In its home field | An experiment is a Markov kernel $P(\text{signal}\mid\text{state})$ on a *known, fixed* state space with a shared prior; garbling is a stochastic matrix. |
| Here | A question or question set over an unformalised world space: no fixed state space, no enumerated answer alphabet, no kernel given. |
| What survives | The structural conclusion — a "better for every purpose" ranking demands universal dominance, so absent a fixed utility the comparison of two information sources is a *partial* order, and incomparability is the default rather than an accident. |
| What does not | The equivalence proof, the garbling construction (there is no $M$ to exhibit between two question sets), and any claim that a *specific* pair of question sets is incomparable — that is unproved. |

## Limits

- A partial order: a **negative** result about universal comparison, not a
  tool for choosing.
- Requires experiments as Markov kernels over a known state space with a
  common prior; the theorem says nothing where the state space is not fixed.
- Once a utility is fixed the order is irrelevant; [[value-of-information]]
  does the work.
- `blackwell-1953` carries `verified: prior` in `wiki/meta/sources.json` and
  is `[?]` for this note's claim until the verifier confirms it against the
  published text; the 1951 Berkeley Symposium paper cited in the body has no
  key of its own yet.

## Related

[[value-of-information]] · [[bayesian-experimental-design]] · [[expected-information-gain]] · [[expected-utility]]

[^s1]: blackwell-1953
