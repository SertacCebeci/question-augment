---
description: "Each erroneous instant of a held decision is classed as judgment, latency or compound error, by whether its source is still current and whether its answer was right for that source."
aliases: ["stale decision", "latency error", "compound error"]
sources: ["doi-10-48550-arxiv-2609-38612"]
---
# Judgment versus latency error in a held decision

A decision that an application holds until the next one can be wrong in two ways that look identical in the output. One is wrong judgment: the answer is wrong for the state it answered. The other is a late answer: the answer is right for the state it came from, but a newer state has changed the reference before the answer takes effect. Scoring only the output cannot tell these apart. Scoring the decision in force can, because each erroneous instant is checked against two conditions: "whether its source time step j is still current", and whether the answer was right for that source.[^d1]

The paper's four classes follow from those two conditions. A current source with a wrong answer is a judgment error.[^d2] An outdated source with a right answer is stale: "a latency error".[^d3] When both conditions fail the error is compound. Before the first acceptance there is no decision at all, which the paper also counts as a latency error. Judgment and compound errors together are "the errors incorrect for their source", so they are the part a better model can fix without touching timing.[^d4]

One case is credited as correct. "An outdated wrong answer that happens to match" the new reference is lucky, and it counts as correct in the in-force score.[^d5] The paper treats this as a small share, since an outdated wrong answer rarely matches the new reference.[^d6]

The split admits a decomposition, which is the paper's formula and not something measured here. Let O be the share of time whose source is current, that is the in-force accuracy of the reference answers at the component's recorded latencies. Let U_cur be the accuracy while the source is current, and λ the lucky share. The in-force accuracy A is then O·U_cur + λ. The decisive property is that O depends only on timings: "Because acceptance depends only on arrival times" and source order, never on the answers, O can be computed from the trace without knowing whether any answer was right.[^d7] Latency therefore enters through O, and judgment enters through U_cur.

Used on the benchmark, the split says which limit binds. The attribution "separates speed-limited from judgment-limited models".[^d8] Slower, more accurate models lose more time to stale answers, while a fast model loses its time to wrong ones: "more accurate models lose 42–51% of the time" to outdated answers.[^d9] The paper reads its own decomposition as the way to see which intervention helps: "Its partition and factorization identify" what limits a component.[^d10] One reading it draws is that "Shorter outputs help only where judgment survives".[^d11]

## Limits

- The partition is only as good as the reference. The references "implement the declared public rules", so an error is an error against those rules, not against a domain's full practice.[^d12]
- The factorization is exact as a bookkeeping identity, but the simpler form A ≈ U·O needs "If judgment errors are unrelated to timing" and a near-zero lucky share.[^d13] The paper states that this form is tested in a later section, which this note did not read, so the approximation is not verified here.
- The lucky rule credits coincidental matches. The split therefore does not separate skill from luck in the stale class; it relies on λ being small, which the paper argues from the rarity of such matches.[^d14]
- The partition describes a single held decision. It does not say which of two components should be applied when both answer. The paper states that "a more accurate correction can still reduce" in-force accuracy by replacing a fresher decision, so arbitration needs its own rule.[^d15]
- The split is from synthetic scenarios and single-model settings. Whether the same proportions hold in logged streams is not shown.

## Related

- [[decision-in-force-accuracy]] — the metric whose erroneous instants this note partitions
- [[insight-stream-metrics]] — also scores decision timing, as part of a stream score with a penalty for bad timing; it does not split held errors into causes
- [[cost-priced-joint-selection-and-stopping]] — latency also enters the choice of when to stop; there it is a cost in the decision rule, here a term in the error split

[^d1]: doi-10-48550-arxiv-2609-38612 — "whether its source time step j is still current"
[^d2]: doi-10-48550-arxiv-2609-38612 — "current source is a judgment error; with an outdated"
[^d3]: doi-10-48550-arxiv-2609-38612 — "source and a right answer it is stale, a latency error"
[^d4]: doi-10-48550-arxiv-2609-38612 — "together the errors incorrect for their source"
[^d5]: doi-10-48550-arxiv-2609-38612 — "an outdated wrong answer that happens to match"
[^d6]: doi-10-48550-arxiv-2609-38612 — "an outdated wrong answer rarely matches"
[^d7]: doi-10-48550-arxiv-2609-38612 — "Because acceptance depends only on arrival times"
[^d8]: doi-10-48550-arxiv-2609-38612 — "from judgment-limited models"
[^d9]: doi-10-48550-arxiv-2609-38612 — "more accurate models lose 42–51% of the time"
[^d10]: doi-10-48550-arxiv-2609-38612 — "Its partition and factorization identify"
[^d11]: doi-10-48550-arxiv-2609-38612 — "Shorter outputs help only where judgment survives"
[^d12]: doi-10-48550-arxiv-2609-38612 — "The executable references implement the declared public rules"
[^d13]: doi-10-48550-arxiv-2609-38612 — "If judgment errors are unrelated to timing"
[^d14]: doi-10-48550-arxiv-2609-38612 — "an outdated wrong answer rarely matches"
[^d15]: doi-10-48550-arxiv-2609-38612 — "a more accurate correction can still reduce"
