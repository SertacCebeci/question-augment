---
description: "Schema linking picks the schema subset a question needs; growing it step by step with schema search and trial queries reaches high strict recall without the full schema."
aliases: ["strict recall rate", "SRR", "agentic schema linking", "linked schema subset"]
sources: ["arxiv-2511-17190"]
---
# Schema linking

A model that writes a database query can be given only part of the schema. Schema linking is the step that chooses that part: the tables and columns a question needs, drawn from the whole. The target is measured as "the proportion of ground-truth schema elements that are successfully included" in the chosen subset.[^a1] The authors say why this matters: "A high SRR is paramount, as missing essential schema elements directly limits the upper bound of" SQL generation accuracy.[^a2] The subset is therefore judged by recall first, and its size only second.

The difficulty is a trade-off. Similarity retrieval over columns reaches high recall only with large candidate sets: "high SRR typically requires large candidate sets that reintroduce noise and inflate token usage."[^a3] The opposite choice fails the other way. The authors argue that methods which keep the subset minimal take on risk: "This noise-minimization strategy carries substantial risk," and one baseline with a small average subset "despite its minimal average of 21.1 recalled columns" reached a low recall.[^a4][^a5]

What the paper adds is a change in how the subset is built. It does not choose the subset once. It starts from a similarity retrieval of "to ensure a broad, albeit potentially incomplete, initial set" of columns.[^a6] An LLM agent then extends that set over several turns. It queries the live database, retrieves more columns by semantic search that excludes those already taken, and verifies the current subset by drafting a query and running it. The paper calls the whole "an iterative, agent-driven process."[^a7] The agent works "without ever seeing the full database schema."[^a8]

The verification step is where feedback enters. Error messages from the database show what is missing: "no such table: T points to an unlinked table."[^a9] The paper says verification "often forms a feedback loop with @retrieve schema and @explore schema."[^a10] Removing the retrieval action gave the largest drop: "removing schema retrieval has the largest impact."[^a12]

The growth also tends to stop early. In the turn-limit study, "the exploration process tends to converge early."[^a13] The headline recall figure is "achieving state-of-the-art strict schema linking recall of 97.4% on" Bird-Dev.[^a11] The paper also links recall to downstream accuracy: "higher SRR directly translates to improved SQL execution accuracy."[^a14]

## Limits

- The reference is the benchmark's gold query. Recall here means agreement with the elements of one reference SQL. Whether the subset holds what a user's question actually needs, in some other sense, is not tested. This is my inference from how the target is defined.
- The link between recall and execution accuracy is a correlation across the paper's systems, which differ in many ways. I did not find, in the text read, a run that varies recall alone with the model held fixed.
- The verification step needs an executor the agent can run trial queries against. Where no such feedback exists, the loop has only retrieval and exploration. The paper does not test that case. This is my inference.
- The scalability claim for schemas "where existing methods severely degrade" rests on the abstract's account.[^a15] I did not trace it to a table in the text read.
- The recall-first framing and the growth from a seed set should carry to any selection from a large environment. The SQL-specific verification step should not. This transfer is my inference, not something the paper shows.

## Related

- [[schema-vocabulary-retrieval]] — the schema also enters before generation as retrieved candidates; this mechanism adds feedback-driven growth after the first retrieval.
- [[dependency-closed-selection]] — a selected subset closed under join paths; a different constraint on the same kind of subset.
- [[sequential-window-reading]] — the same recall-against-distractor trade-off, in a ranked list of retrieved windows.
- [[question-rewriting-schema-scaling]] — the other handling of a large, noisy schema: rewriting the question rather than cutting the schema.
- [[execution-feedback-state-revision]] — revising a query from execution results, the kind of feedback the verify step supplies here.

[^a1]: arxiv-2511-17190 — "the proportion of ground-truth schema elements that are successfully"
[^a2]: arxiv-2511-17190 — "A high SRR is paramount, as missing essential schema elements directly limits the upper bound of"
[^a3]: arxiv-2511-17190 — "high SRR typically requires large candidate sets that reintroduce noise and inflate token usage"
[^a4]: arxiv-2511-17190 — "This noise-minimization strategy carries substantial risk"
[^a5]: arxiv-2511-17190 — "despite its minimal average of 21.1 recalled columns"
[^a6]: arxiv-2511-17190 — "to ensure a broad, albeit potentially incomplete, initial set"
[^a7]: arxiv-2511-17190 — "an iterative, agent-driven process"
[^a8]: arxiv-2511-17190 — "without ever seeing the full"
[^a9]: arxiv-2511-17190 — "no such table: T points to an unlinked table"
[^a10]: arxiv-2511-17190 — "often forms a feedback loop with @retrieve schema and @explore schema"
[^a11]: arxiv-2511-17190 — "achieving state-of-the-art strict schema linking recall of 97.4% on"
[^a12]: arxiv-2511-17190 — "removing schema retrieval has the largest impact"
[^a13]: arxiv-2511-17190 — "the exploration process tends to converge early"
[^a14]: arxiv-2511-17190 — "higher SRR directly translates to improved SQL execution accuracy"
[^a15]: arxiv-2511-17190 — "where existing methods severely degrade"
