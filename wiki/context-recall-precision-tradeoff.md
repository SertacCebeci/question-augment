---
description: "Broader context gathering by a coding agent raises recall of the human gold context and lowers precision; a more elaborate scaffold does not reliably escape the trade."
aliases: ["context recall versus precision", "gold-context recall-precision trade-off", "recall-over-precision in context retrieval"]
sources: ["doi-10-4230-lipics-esem-2026-28"]
---
# Context recall-precision trade-off

A coding agent must gather code before it can patch, and the gathering can be scored against a gold set. The gold set is a set of repository regions that expert developers judged necessary for the fix: the paper defines gold contexts as standard sets of repository artifacts "that expert developers identify as necessary to resolve a given issue."[^c1] The agent's trajectory is instrumented to log every region it inspects, and those regions are aligned with the gold set at file, block and line granularity. Recall, precision and F1 are then computed from interval overlap.[^c2]

Scored this way, the two numbers pull apart. Recall is the share of the gold that the agent touched; precision is the share of what it touched that is gold. Across four frontier LLMs the paper reports that "Recall is favored over precision in LLM context retrieval."[^c3] The mechanism it names is that models "expand retrieved contexts aggressively to achieve higher recall," which adds material that is not in the gold set and so lowers precision.[^c4] The same pattern appears across agents: Prometheus, which favours broad exploration, retrieves larger contexts and gets "higher recall but lower precision."[^c8]

The trade has a cost on both sides. The paper calls it "a clear trade-off exists between recall and precision," and it also reports that recall tracks outcome: "We also observe a positive correlation between context recall and downstream task success."[^c5][^c6] Recall is thus worth having, but the noise that comes with it can hurt: "excessive context can introduce noise and impair the" agent's reasoning.[^c7] The paper's reading is that the balance matters more than the level. Models that "balance retrieval frequency and context granularity achieve higher Pass@1 at lower cost."[^c11]

The second finding concerns the machinery around the model. The authors compare five agents, from a bash-only baseline to four published scaffolds, and report that "sophisticated agent scaffolding yields only marginal gains in" context retrieval.[^c12] Several scaffolds "often fall below those of the baseline mini-SWE-agent" on the same metrics.[^c9] The paper's interpretation is that "current agent frameworks may be over-engineered for context retrieval," because a simple loop of search and inspection "can already recover a substantial portion of the necessary" context.[^c10] So a more elaborate retrieval apparatus does not buy a better point on the trade-off; in these runs it mostly buys overhead.

This is the same shape as the shortlist result in [[candidate-set-narrowing-recall]], where the cut's recall caps what the chooser can do. Here the gold set plays the role of the right item, and the agent's exploration is the cut. The difference is that the agent here can keep looking, so recall is a count of what was touched, not a ceiling on what could be chosen. Whether touched code was used in the answer is a separate question, treated in [[retrieval-utilization-gap]]. The precision axis also has an analogue in [[cache-coverage-over-precision]], where the coverage of reasoning states, not their precision, decides how well a derivation survives compression.

## Limits

- The gold set is human-annotated from gold patches, over four benchmarks, and filtered for difficulty. Recall against it measures overlap with what annotators traced from the fix, not with every region a fix could need. The stability check is small: the paper reports that "we conduct a case study on 82 tasks," each with two patches, and an average Jaccard similarity of "is 0.9518 (average distance 0.0482)."[^c13][^c14]
- The scaffold comparison is made on one backbone: "All agents are evaluated with an advanced LLM backbone," GPT-5.[^c15] The model comparison uses a single scaffold, mini-SWE-agent. So "scaffolding adds little" is shown for this backbone and this baseline; a different model may use a richer scaffold differently (my inference).
- The link between recall and task success is reported as a positive correlation. The text read gives no coefficient, so how much of the Pass@1 difference the recall difference explains is not shown.
- Precision and recall depend on the granularity chosen. The paper reports file, block and line levels separately, and the text read does not establish that the ranking of agents or models holds at every level (my inference from the table layout).
- The trade-off is described for code. Whether the same shape holds for an agent gathering evidence in open-domain search, or for a person gathering information before answering, is not tested in this text.

## Related

- [[retrieval-utilization-gap]] — recall counts what was inspected; the gap between inspected and used code is a separate failure the same benchmark measures.
- [[candidate-set-narrowing-recall]] — the same favour-recall-first shape, for a shortlist cut where the chooser never sees what was dropped.
- [[relevance-completeness-divergence]] — topical relevance does not track sufficiency; here recall of a gold set is measured directly instead of inferred from relevance.
- [[cache-coverage-over-precision]] — the coverage-versus-precision axis in KV compression, a different object with the same split.

[^c1]: doi-10-4230-lipics-esem-2026-28 — "that expert developers identify as necessary to resolve a given issue"
[^c2]: doi-10-4230-lipics-esem-2026-28 — "we compute recall, precision, and F1 using interval overlap at three"
[^c3]: doi-10-4230-lipics-esem-2026-28 — "Recall is favored over precision in LLM context retrieval"
[^c4]: doi-10-4230-lipics-esem-2026-28 — "expand retrieved contexts aggressively to achieve higher recall"
[^c5]: doi-10-4230-lipics-esem-2026-28 — "a clear trade-off exists between recall and precision"
[^c6]: doi-10-4230-lipics-esem-2026-28 — "We also observe a positive correlation between context recall and downstream task success"
[^c7]: doi-10-4230-lipics-esem-2026-28 — "excessive context can introduce noise and impair the"
[^c8]: doi-10-4230-lipics-esem-2026-28 — "and retrieve larger contexts, achieving higher recall but lower precision"
[^c9]: doi-10-4230-lipics-esem-2026-28 — "often fall below those of the baseline mini-SWE-agent"
[^c10]: doi-10-4230-lipics-esem-2026-28 — "frameworks may be over-engineered for context retrieval"
[^c11]: doi-10-4230-lipics-esem-2026-28 — "that balance retrieval frequency and context granularity achieve higher Pass@1 at lower cost"
[^c12]: doi-10-4230-lipics-esem-2026-28 — "sophisticated agent scaffolding yields only marginal gains in"
[^c13]: doi-10-4230-lipics-esem-2026-28 — "we conduct a case study on 82 tasks"
[^c14]: doi-10-4230-lipics-esem-2026-28 — "is 0.9518 (average distance 0.0482)"
[^c15]: doi-10-4230-lipics-esem-2026-28 — "All agents are evaluated with an advanced LLM backbone"
