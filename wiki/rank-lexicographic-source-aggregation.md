---
description: "Combine sources by credibility rank: higher ranks override, lower ranks fill their silences, equal ranks keep their conflicts, and closure is applied last so overridden opinions leave no trace."
aliases: ["AGR operator", "rank-based aggregation", "lexicographic source refinement"]
sources: ["maynardzhang-2003"]
---
# Rank-lexicographic source aggregation

An agent informed by sources of unequal reliability should favor the more reliable but still let less reliable sources speak where the better ones have no opinion; the paper builds an operator that does exactly this on top of belief states that distinguish [[conflict-versus-agnosticism-belief-state|conflict from agnosticism]].

## Mechanism

- Equal ranks: take the union of the sources' relations, then the transitive closure. Union keeps modularity but may lose transitivity; every opinion is taken seriously, so many conflicts can result.[^c1]
- Strict ranks: a pair (x, y) is in the result if some source ranks x before y and every higher-ranked source is agnostic on it, so lower sources are consulted when higher ones are agnostic.[^c2]
- General case: the obvious "combine equal ranks, then refine by rank" operator fails because overridden opinions leak in through the intermediate closure (Example 4: all sources agnostic over a and c, yet the result has conflict between them).[^c3] The fix, AGR, applies refinement first to the raw source states and closes afterwards.[^c4]
- Closure adds only a minimal repair: new opinions appear only between worlds already in conflict (Proposition 18).[^c5]
- AGR reduces to union-plus-closure when all ranks are equal and to pure refinement when ranks are a total order, and AGR of no sources is empty (no opinion is invented).[^c6]

Because equal-rank conflicts are explicit in the output rather than forced into a ranking, the operator meets the modified Arrow conditions (range, domain, Pareto, independence, no dictator among equals) — the paper's claim that it escapes Arrow's impossibility result by widening the output class.[^c7]

## Limits

- Ranks are an ordinal credibility order supplied from outside; the paper does not say how to learn or calibrate it.
- Majority or quantity of support is ignored by AGR itself; voting is a later extension with its own closure and its own non-modular intermediate cases.
- A top-ranked source acts as dictator over everyone below it by design; where that is wrong, the operator offers no remedy.
- Verified by proofs and worked examples (a space robot scenario), not on real data. I did not read the Arrow-condition proofs in full.

## Related

- [[conflict-versus-agnosticism-belief-state]] — the representation this operator outputs
- [[agm-belief-revision]] — total-preorder belief change this extends to many sources
- [[belief-base-revision]] — revision of a stored set of beliefs by new input
- [[possible-worlds]] — the objects over which the sources order likelihood

[^c1]: maynardzhang-2003 — "Proposition 11 If S ⊆ S, then Un(S) is modular but not necessarily transitive."
[^c2]: maynardzhang-2003 — "sources, and lower ranked sources are consulted when higher ranked sources are agnostic:"
[^c3]: maynardzhang-2003 — "opinions that will eventually get overridden may still have"
[^c4]: maynardzhang-2003 — "Because of these undesired effects, we propose another aggregation operator which circumvents this problem"
[^c5]: maynardzhang-2003 — "new opinions are only added between worlds already involved in a conflict"
[^c6]: maynardzhang-2003 — "2. If wS is a total order, AGR(S) = AGRRf(S)."
[^c7]: maynardzhang-2003 — "Restricted range For our setting, the output of the aggregation function will be a modular, transitive belief state rather than a total preorder considered by Arrow."
