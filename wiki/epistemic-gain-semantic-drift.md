---
description: "An oracle answer can lower a person's self-reported confusion while moving their starting thought away in embedding space; across the eight table rows the two measures rise together."
aliases: ["drift–gain coupling", "epistemic gain versus semantic drift"]
sources: ["arxiv-2601-00938"]
---
# Epistemic gain versus semantic drift

A reply to a question can act on the person who asked in two ways. It can reduce their confusion, and it can move the thought they started with. The paper measures both on one benchmark. Epistemic gain is the reduction in self-reported confusion, mapped to a 0–5 scale: "gain is reduction in self-reported confusion (mapped to 0–5)."[^c1] Semantic drift is a distance between two embeddings: "Drift is cosine distance between initial thought embedding" and the embedding of the oracle's completion.[^c2] The benchmark is reported as N = 200, with one row per oracle.[^c3]

The reported values rise together. The human baseline has gain 1.2 and drift 0.12. The seven models run from gain 3.1 with drift 0.68 (Llama 3 70B) up to gain 4.9 with drift 0.89; the largest drift, 0.91, sits at gain 4.7.[^c3] The paper calls this "drift–gain coupling."[^c4] Its own wording is coupling, not a trade-off, and it gives no optimum along the pair. My reading is that the table shows co-movement across eight oracle-level values. It does not show that any one person's gain tracks their own drift.

What the pair is meant to capture is the double effect of an answer: how much it resolves the question and how far it displaces the asker's starting point. Drift here is a distance, not an error measure. The text read does not score it against correctness, so a large drift is not shown to be a bad answer. This is my reading of the definitions above.

## Limits

- Gain is self-reported on a mapped 0–5 scale. A lower confusion rating is not shown to mean understanding, and no reliability or validity check appears in the text read.
- Drift is a cosine distance in an embedding space the text does not fix. My inference is that the ordering of oracles could change with another encoder; the paper does not test this.
- The coupling rests on eight means and one drift value per row. The table gives standard deviations for gain only, reports no test of the association, and does not break the N = 200 down by oracle.
- The "drift–gain scaling analysis" named among the contributions has no text in the version read; the section heading appears with nothing under it.[^c5] The coupling claim therefore rests on the table and the figure alone.
- The table's rows were aligned by me from a text extraction, so the individual numbers above are approximate.
- The benchmark compares oracles. It does not test the compressed-query method the paper proposes, so it says nothing about whether compression changes gain or drift.

## Related

- [[query-relative-token-overflow]] — both ask whether a compressed or returned answer is adequate for the question asked; that note measures the answer's sufficiency, this one measures the asker's shift.
- [[value-of-information]] — a gain measured as reduced confusion is a subjective stand-in for the information an answer adds; the paper does not connect the two.

[^c1]: arxiv-2601-00938 — "gain is reduction in self-reported confusion (mapped to 0–5)"
[^c2]: arxiv-2601-00938 — "Drift is cosine distance between initial thought embedding"
[^c3]: arxiv-2601-00938 — "Table 2. Benchmark B (𝑁 = 200): epistemic gain vs. semantic drift across oracles."
[^c4]: arxiv-2601-00938 — "drift–gain coupling"
[^c5]: arxiv-2601-00938 — "drift–gain scaling analysis"
