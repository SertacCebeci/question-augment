---
description: "Diminishing returns generalised to policies that observe as they go: it is An item's contribution shrinks as the set you already hold grows."
aliases: ["adaptive greedy", "diminishing returns for policies"]
sources: ["golovin-2011", "golovin-2010"]
---
# Adaptive submodularity

> Diminishing returns generalised to policies that observe as they go: it is
> why an asker who simply takes the best next question is provably near the
> best possible sequence, and why each further question buys less.[^c1]

## Submodularity

$$f(A \cup \{x\}) - f(A) \ \geq\ f(B \cup \{x\}) - f(B) \quad \text{for } A \subseteq B$$

An item's contribution shrinks as the set you already hold grows.
**Diminishing returns.**[^c2]

## Adaptive submodularity (Golovin & Krause, 2011)

The same notion for **policies**: the objective is adaptive submodular when
the *conditional expected* marginal gain of an item, given the answers seen
so far, does not increase as that record of answers is extended.[^c3]

Adaptive monotone: no answer can make the objective fall.[^c4]

**The guarantee, with its quantifiers.** Golovin & Krause (2011) prove that
if $f$ is adaptive monotone and adaptive submodular with respect to a
**known** prior over realisations, then the *expected* value of the adaptive
greedy policy run for $k$ steps is at least $(1-1/e) \approx 0.63$ times the
expected value of the *best policy of $k$ steps* under the same prior and the
same objective.[^c5]

Both sides are expectations over the prior; the optimum
ranges over policies of the same budget, not over an omniscient oracle that
knows the answers in advance.[^c6]

The policy called *adaptive greedy* is named
after the property, and this note covers both the property and this guarantee
for that policy.[^c7]

Their active-learning instance is the reduction in **[[version-space]]
probability mass**: tests whose outcome is consistent with a determinate
subset of hypotheses — the noiseless case.[^c8]

## What follows for asking

**1. Greedy is sufficient — provably.** Taking the question with the largest
expected narrowing at each step lands within a constant factor of the best
$k$-question policy, whenever the conditions above hold.[^c9]

Lookahead search over
question orders is not needed to be near-optimal (Golovin & Krause, 2011).[^c10]

**2. Marginal value is non-increasing.** That the gain of a question shrinks
in what has already been asked and answered *is* submodularity — it is the
assumption, restated.[^c11]

This is what the theorem gives, and it gives nothing
more about the shape of the decline.[^c12]

**Conjecture (this wiki's extrapolation, not in Golovin & Krause).** Over a
long run of cheap self-answered questions the profile might look like:

```text
questions 1–50      :  large entropy drop
questions 50–500    :  moderate
questions 500–5000  :  small
questions 5000+     :  very small but NOT ZERO
```
[^c13]

The bands are an illustration of a monotone-decreasing marginal, not a result:
golovin-2011 establishes an approximation ratio, no decay profile over
question index, no threshold at 50 or 500 or 5000, and nothing about
natural-language questions.[^c14]

The same holds for the cost reading also inferred
here — that a large batch of self-answered questions pays *because* the
questions are cheap, while the same volume put to a person would not.[^c15]

The
mathematics is silent on the price of asking; the asymmetry is an assumption
about cost, imported from outside the theorem. See [[value-of-information]].[^c16]

## Where diversity fits

Also this wiki's inference, not a result of golovin-2011: a submodular
objective depresses the marginal gain of a similar question **only through
overlap in what the two questions rule out**.[^c17]

So the diversity that comes
free is diversity in the *partition of worlds induced*, not diversity in
wording — two near-identical phrasings that elicit disjoint answers are not
redundant under the objective, and two very differently worded questions that
cut the same worlds are.[^c18]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Submodular optimisation | adaptive greedy | close — the *policy* whose guarantee this property enables; named after it, covered here, but one can hold without the other being run |
| Economics / operations research | diminishing returns for policies | close — the descriptive name for the property, without the conditional-expectation formalism |
[^c19.1][^c19.2][^c19]

Not an alias: *Golovin–Krause*. That is a source label (`golovin-2011`), not a
name the concept goes by.[^c20]

## Transfer

| | In its home field | Here |
|---|---|---|
| Items / policy | tests with observable outcomes, chosen adaptively | questions, chosen after each answer |
| State | drawn from a known prior over realisations | "the design" — the prior is not known |
| What survives | greedy is within $(1-1/e)$ of the best equal-length policy; overlapping questions depress each other's marginal gain | |
| What does not | the numerical $0.63$ once the [[possible-worlds|hypothesis space]] grows during asking; and the guarantee itself once answers are noisy rather than determinate — the free-text case | |
[^c21.1][^c21.2][^c21.3][^c21.4][^c21]

## Limits

- The $(1-1/e)$ bound needs the objective to be adaptive **monotone** and
  adaptive **submodular** under a **known** prior, and compares against the
  best policy *of the same length* — not against an ideal answer.[^c22]

- **Noise.** Adaptive submodularity of the version-space / information-gain
  objective is established for *noiseless* observations, where an answer is
  consistent with a determinate subset of hypotheses.[^c23]

Golovin, Krause & Ray (2010) show that [[generalized-binary-search|generalized binary search]] — greedy on that objective —
  can perform very poorly when observations are noisy, and had to build a
  different objective (EC²) to recover a guarantee.[^c24]

Natural-language answers
  are the noisy case, so this note's guarantee does not transfer to them as
  stated.[^c25]

- [[entropy|Entropy]] reduction qualifies only for a *fixed* hypothesis space; when new
  axes appear mid-process the objective is no longer the one the theorem is
  about.[^c26]

- The "diversity comes free" reading holds only insofar as similarity between
  questions actually shows up as overlap in the worlds they eliminate.[^c27]

Where
  the objective is not the one that measures those worlds, similar wording
  buys no redundancy penalty.[^c28]

- Guarantees are against the optimal policy *for the same objective*.[^c29]

They say
  nothing about whether information is the right objective
  ([[value-of-information]]).[^c30]

## Related

[[generalized-binary-search]] · [[optimal-decision-tree]] · [[chain-rule]] · [[cramer-rao-bound]] · [[value-of-information]]

[^c1]: golovin-2011
[^c2]: golovin-2011
[^c3]: golovin-2011 — "Definition 3 (Adaptive Submodularity) A function f : 2E × OE → R≥0 is adaptive submodular with respect to distribution p (φ) if the conditional expected marginal benefit of any fixed item does not increase as more items are selected and their states are observed."
[^c4]: golovin-2011 — "A function f : 2E × OE → R≥0 is adaptive monotone with respect to distribution p (φ) if the conditional expected marginal benefit of any item is nonnegative, i.e., for all ψ with P [Φ ∼ ψ] > 0 and all e ∈ E we have ∆(e | ψ) ≥ 0."
[^c5]: golovin-2011
[^c6]: golovin-2011
[^c7]: golovin-2011
[^c8]: golovin-2011 — "In both domains we want to pick examples / tests to shrink the remaining version space (the set of consistent hypotheses) as quickly as possible. Here, we show that the reduction in version space probability mass is adaptive submodular, and use that observation to prove that the adaptive greedy algorithm is a near-optimal querying policy."
[^c9]: golovin-2011 — "We introduce the concept of adaptive submodularity, and prove that if a problem instance satisfies this property, a simple adaptive greedy policy performs near-optimally, for both adaptive stochastic maximization and coverage, and also a natural min-sum objective."
[^c10]: golovin-2011 — "We introduce the concept of adaptive submodularity, and prove that if a problem instance satisfies this property, a simple adaptive greedy policy performs near-optimally, for both adaptive stochastic maximization and coverage, and also a natural min-sum objective."
[^c11]: golovin-2011
[^c12]: golovin-2011
[^c13]: golovin-2011
[^c14]: golovin-2011
[^c15]: golovin-2011
[^c16]: golovin-2011
[^c17]: golovin-2011
[^c18]: golovin-2011
[^c19.1]: golovin-2011
[^c19.2]: golovin-2011
[^c20]: golovin-2011
[^c21.1]: golovin-2011 — "Let E be a finite set of items (e.g., sensor locations). Each item e ∈ E is in a particular (initially unknown) state from a set O of possible states"
[^c21.2]: golovin-2011 — "We take a Bayesian approach and assume that there is a known prior probability distribution p (φ) := P [Φ = φ] over realizations"
[^c21.3]: golovin-2011
[^c21.4]: golovin-2011
[^c22]: golovin-2011 — "Theorem 5 Fix any α ≥ 1. If f is adaptive monotone and adaptive submodular with respect to the distribution p (φ), and π is an α-approximate greedy policy, then for all policies π ∗ and positive integers ` and k,"
[^c23]: golovin-2011 — "Theorem 21 and the extensions mentioned so far are in the noise free case, i.e., the result of query x and observes h∗ (x), where h∗ is the target hypothesis. Many practical problems may have noisy observations."
[^c24]: golovin-2011
[^c25]: golovin-2011
[^c26]: golovin-2011 — "Let E be a finite set of items (e.g., sensor locations). Each item e ∈ E is in a particular (initially unknown) state from a set O of possible states"
[^c27]: golovin-2011
[^c28]: golovin-2011
[^c29]: golovin-2011
[^c30]: golovin-2011
[^c19]: golovin-2011
[^c21]: golovin-2011
