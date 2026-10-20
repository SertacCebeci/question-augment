---
description: "Merging per-stream wealth by max, average or product gives different stopping times under sparse versus dense alternatives; averaging average and product gets the better of both."
aliases: ["balanced sequential test", "merging test martingales for global null", "multi-stream sequential auditing", "product versus average wealth merging"]
sources: ["arxiv-2602-21479"]
---
# Balanced evidence merging for a global sequential null

The setting is auditing k data streams (demographic groups, imaging modalities) at once. Each stream i has a null that its bounded mean is zero. The global null says all k hold. Each stream gets a wealth process, a betting-based test martingale, and a global test must merge the k wealth values into one alarm rule.[^c1] The choice of merging rule decides how fast the alarm fires, depending on how many streams are actually non-null.

## Three merging rules and their stopping times

**Max (Bonferroni).** Reject when the largest wealth reaches k/alpha. Its expected stopping time is of order ln k / alpha in both sparse and dense settings, because it uses only the maximum mean and ignores evidence in the other streams.[^c2]

**Product.** Multiply the k wealths; reject at 1/alpha. When all k streams are non-null, each wealth grows and the product compounds, so the dominating term falls to (1/k) ln(1/alpha), far below the Bonferroni rate.[^c3] When only one stream is non-null, the other k-1 wealths fluctuate around 1 and inhibit growth, so the bound worsens to roughly k ln k plus ln(1/alpha).[^c4]

**Average.** Reject when the mean wealth reaches 1/alpha. With one non-null stream the average is about 1/k of the maximum, so it behaves almost exactly like Bonferroni; with many non-null streams it still beats Bonferroni, but only down to ln(1/alpha), not to the product's rate.[^c5]

**Balanced.** Take W_balance = (W_ave + W_prod)/2. An average of test martingales is a test martingale, so validity is kept. The proved bound is the minimum of the product bound and the Bonferroni bound, so it behaves like the product when evidence is dispersed and like the average (and Bonferroni) when evidence is concentrated.[^c6] The paper states the consequence directly.[^c7]

## Why the rules differ

Merging by product rewards agreement across streams; merging by average survives when only a few streams carry evidence. The product dominates other rules at a fixed time when all streams show evidence, but that dominance requires independent wealth processes.[^c8] The paper's contribution is to turn these fixed-time dominance facts into expected-stopping-time guarantees, which they were not before.

## Limits

- The guarantees are upper bounds on expected stopping time, not lower bounds. "Best of both worlds" means matching the better of two upper bounds, not proven optimality.
- Streams are bounded-mean tests on i.i.d. data in [-1, 1]; the product's validity and dominance need independence across streams.[^c8]
- Sparse and dense are the two extremes analysed (one non-null stream, or all); intermediate sparsity is read off the formula, not separately proved by me.
- Tested on synthetic and real-world ML auditing data. Nothing here concerns questions, answers or people; applying it to choosing or stopping a set of probes is my own inference and untested.

## Related

- [[multi-armed-testing-by-betting]] — also a global null over several sources, but chooses which source to sample rather than merging all of them
- [[sequential-graphical-testing]] — another route to multiple sequential hypotheses, with error control by graph rather than by merging
- [[sprt]] — the single-stream ancestor of the wealth processes merged here
- [[repeated-significance-testing]] — why a stream that can be stopped at any time needs sequentially valid tests

[^c1]: arxiv-2602-21479 — "Testing this global null is equivalent to testing the intersection of k hypotheses"
[^c2]: arxiv-2602-21479 — "ϕbonf fails to fully use the evidence within all k streams"
[^c3]: arxiv-2602-21479 — "Dense alternative γ = k. In the large k and small α regime, the dominating term is 1/k ln 1/α."
[^c4]: arxiv-2602-21479 — "from the single non-null stream is heavily inhibited by the remaining streams fluctuating around 1."
[^c5]: arxiv-2602-21479 — "This analysis indicates that ϕave is effective when evidence is concentrated in only a few streams,"
[^c6]: arxiv-2602-21479 — "Moreover, under H1global , its expected stopping time obeys E[τ ] ≤ min{T prod , T bonf }."
[^c7]: arxiv-2602-21479 — "ϕbalance always rejects nearly as quickly as the best possible test, regardless of the sparsity of the alternative."
[^c8]: arxiv-2602-21479 — "This dominance result requires the wealth processes be independent."
