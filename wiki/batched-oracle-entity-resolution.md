---
description: "Choosing which bounded batch a limited oracle resolves next is NP-hard in general, but a heaviest-subgraph greedy step is exactly optimal under a stated condition on entity sizes."
aliases: ["progressive batched entity resolution", "batched entity resolution", "oracle batch selection"]
sources: ["balzotti-2026"]
---
# Batched oracle entity resolution

> An oracle that can only be shown a bounded batch of records at a time, not
> a pair: which batch to show it next so the next query recovers the most
> matches is NP-hard to choose exactly, but a graph-heaviest-subgraph greedy
> step is provably optimal under a stated condition on entity sizes.

## Definition / Mechanism

Balzotti, Firmani, Gagliardelli & Simonini (2026) formalise
an oracle `Oracle : R^b → {0,1}^(b choose 2)` that, given a batch $B$ of at
most $b$ records, returns every pairwise match/non-match decision inside $B$
at once — an LLM prompted with a batch, a crowd worker shown a small group,
or a set-transformer clustering head are named as concrete oracles of this
shape.[^c1]

Progressive batched entity resolution asks, after a sequence of batches
already queried, which next $b$-batch $q$ maximises the number of *newly*
discovered match edges — the gain $\Delta_q^Q$.[^c2]

**NP-hardness.** Given any weight function $\hat g$ on record pairs that
estimates this gain, finding the $b$-batch maximising the total estimated
gain is NP-hard: the paper reduces from the Heaviest Subgraph Problem (an
instance of HSP embeds directly as a batch-selection instance with an empty
query history).[^c3]

**Optimal solution under a condition.** Define a weighted graph
$\mathrm{Gain}^b_Q$ on the current records whose edge weights favour pairs
inside larger not-yet-resolved entities. Selecting, at each step, the batch
that solves the Heaviest Subgraph Problem on $\mathrm{Gain}^b_Q$ always
picks a batch with maximal true gain $\Delta_q^Q$ (Proposition 1) — this
holds unconditionally.[^c4]

If every entity in $R$ needs at most one batch to be
reduced to a single representative once its within-entity records are all
processed together (formally $r_b^{\mathrm{rec}}(|e|)=1$ for every entity
$e$), then repeating this HSP-greedy step is $b$-optimal for the whole
dataset — it matches, at every step $t$, the best possible cumulative match
count of any $b$-batch schedule.[^c5]

At $b=2$ (pairwise matching) this
condition holds for every entity, so an optimal schedule always exists in
the classical pairwise case, recovering an existing pairwise result.[^c6]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Database systems (Balzotti et al. 2026) | progressive batched entity resolution | exact — the per-step maximisation object (Problem 2) this note's optimality result is stated for |
| Database systems (Balzotti et al. 2026) | batched entity resolution | close — the whole-dataset resolution task (Problem 1); Theorem II.4 shows the progressive greedy rule solves it optimally under the stated condition, so the two names cover the same object only in that regime |
| Database systems | oracle batch selection | close — this wiki's shorthand for the per-step decision problem |
[^c14]

## Why it matters

This is a batch-query analogue of [[optimal-decision-tree]]'s two-part
result for a very different object: exact optimal *selection* of what to
show a bounded oracle next is intractable in general, yet a specific greedy
rule is guaranteed optimal under a checkable structural condition (rather
than only an approximation ratio, as in [[adaptive-submodularity]]). It
gives asking-under-a-bounded-oracle a second regime: when the condition
holds, "ask greedily" is not a compromise but the exact answer.

## Transfer

| | In its home field | Here |
|---|---|---|
| Objects | records and a match/non-match equivalence relation over a dataset | any two candidate constraints a bounded oracle could be asked to jointly resolve |
| Guarantee | greedy Heaviest-Subgraph batch selection is $b$-optimal for full match discovery when $r_b^{\mathrm{rec}}(\lvert e\rvert)=1$ for every entity | the shape — exact optimality of a greedy step, conditional on a structural property of the target's clusters — but not the entity-resolution formalism itself |
| What survives | the general lesson that a bounded-batch selection problem can be NP-hard yet admit an exactly optimal greedy rule on a distinguished substructure | |
| What does not | the numeric condition $r_b^{\mathrm{rec}}(\lvert e\rvert)=1$, the bin-packing/HSP machinery, and the "entity" object itself, none of which are defined outside record matching | |
[^c7]

## Limits

- The oracle is assumed **consistent** — it returns only correct match
  decisions; the paper states explicitly that noisy or inconsistent oracle
  answers are left to future work, so nothing here bounds performance when
  an LLM- or human-oracle batch answer is wrong.[^c8]
- The $b$-optimality guarantee (Theorem II.4) holds only under the stated
  condition on entity sizes; Theorem II.1 shows a $b$-optimal schedule does
  not always exist once that condition fails, so the greedy rule is not a
  general-purpose answer to "which batch next."[^c9]
- `balzotti-2026` is an arXiv preprint (2026-06-23); not yet checked against
  a peer-reviewed venue listing.

## Related

[[optimal-decision-tree]] · [[adaptive-submodularity]] · [[generalized-binary-search]] · [[perbacco]]

[^c1]: balzotti-2026 — "We assume access to an oracle Oracle : Rb → {0, 1}(2) , which, given a batch B ⊆ R of b ≥ 2 records, returns a match/non-match decision for every unordered pair of records in B."
[^c2]: balzotti-2026 — "Given a set of records R, an integer b, and a sequence of queries Q, find a b-batch q that maximizes MatchQ◦q , where Q◦q denotes the sequence Q extended by q."
[^c3]: balzotti-2026
[^c4]: balzotti-2026
[^c5]: balzotti-2026 — "If rbrec (|e|) = 1 for each entity e in R, then Q is b-optimal for R."
[^c6]: balzotti-2026 — "We observe that when b = 2, rbrec (|e|) = 1 for every entity e, so an optimal solution for pairwise batches always exists by Theorem II.4. In addition, the optimal solution described in Theorem II.4 coincides with the one described in [10]."
[^c8]: balzotti-2026
[^c9]: balzotti-2026 — "A b-optimal solution for R does not always exist for every integer b and set of records R."
[^c14]: balzotti-2026
[^c7]: balzotti-2026
