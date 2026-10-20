---
description: "A paired McNemar benchmark finds three frontier text-to-SQL models statistically indistinguishable with and without a business-context document — only the document predicts accuracy."
aliases: ["context dominates model choice", "the clustering result", "semantic-layer clustering result", "tool availability dominates performance"]
sources: ["arxiv-2604-25149", "arxiv-2601-02598", "arxiv-2603-04403"]
---
# Context dominates model choice

> Hold the question set and the judge fixed, vary only the model and
> whether it was given the business semantics: the semantics predict the
> answer's correctness, the model does not.

## Definition / Mechanism

Rumiantsau & Fokeev (2026) run a strictly paired
benchmark — three frontier models (Claude Opus 4.7, Claude Sonnet 4.6,
GPT-5.4), each on the same 99 natural-language analytics questions, each
scored twice: once given only the warehouse schema, once given the
schema plus a 4 KB hand-authored document of the dataset's measures,
conventions and disambiguation rules. Supplying the document raises
every model's pass rate by 17–23 points, and the six resulting
configurations split into exactly two statistically homogeneous
clusters rather than three model-ordered ones: "Adding the document
improves accuracy by +17 to +23 percentage points across all three
models (paired exact McNemar, p ≤ 0.0015). With it, the three models are
statistically indistinguishable (67.7–68.7%); without it, they are also
indistinguishable (45.5–50.5%). Every cross-cluster comparison is
significant at p < 0.01. The presence of the semantic-layer document
accounts for essentially all of the significant variance; model choice
within tier does not."[^c1]

The pairwise McNemar matrix over all six configurations confirms the
split is clean, not a trend: no within-cluster comparison reaches
significance, and every cross-cluster comparison does. "Two clusters
emerge cleanly. Within the semantic-layer cluster — Opus+Sem, Sonnet+Sem,
GPT-5.4+Sem — none of the three pairwise comparisons is statistically
significant (all p ≥ 0.79). Within the raw cluster — Opus raw, Sonnet
raw, GPT-5.4 raw — none of the three pairwise comparisons is
statistically significant either (all p ≥ 0.42). Every one of the nine
cross-cluster comparisons is significant at p < 0.01, and most at
p < 0.001."[^c2]

The paper's reading of the mechanism: absent the document the model must
guess which columns, joins and conventions a phrase like "return rate"
or "last quarter" refers to; the document turns that guess into a
lookup. "Schema linking becomes a lookup, not a guess. Without semantic
context, the model faces a raw schema of dozens or hundreds of tables
and must guess which columns and joins correspond to the user's intent.
With semantic context, the mapping from user phrasing to data structures
is given explicitly."[^c3]

So the document is read as changing *what the model is asked to do*
(retrieve a stated answer) rather than *how capable* the model is.

## Why it matters

Whether an answer is informative depends on what constrained it, and
this result locates that constraint precisely: on this benchmark, once
the business semantics a question needs are made explicit and available
as context, three frontier models of different vendors and price points
converge to statistically the same accuracy — the binding resource is
the semantics, not the model. A practitioner budgeting for answer
quality should spend on writing and maintaining the context document
before spending on the strongest available model; once the document
exists, model choice is legitimately decided on cost and latency instead
of accuracy (the paper reports an ~28% input-token difference between
the two models at matched accuracy).

The same shape appears when the scarce input is structured-data access rather than a document. FinRetrieval (Kim and Huang, 2026) runs fourteen agent configurations on the same 500 financial retrieval questions, with and without three structured-data tools exposed over the Model Context Protocol. With reasoning enabled, the structured-tool configurations land between 86.0% and 90.8%, and the web-search-only ones between 19.8% and 70.8%.[^c9] The authors read this as tool availability dominating model choice: "Tool availability is the dominant factor."[^c10] The tool plays the part the document plays above: it turns a guess about where a value lives into a lookup, and once the lookup exists the models converge.

Two cautions keep this from being the same result. The web-only gap is partly behavioural. Claude often found relevant results and then did not commit to an answer, a pattern the authors say accounts for about 35 points of its 71-point gap.[^c11][^c12] And the cross-provider comparison is between whole vendor stacks, so "performance differences reflect complete systems"; model, agent SDK and web tool are not separated.[^c13]

## Limits

The clustering claim is explicitly scoped by its own authors to one
99-question benchmark over one retail schema and three specific models:
"We emphasize that this is a within-study statistical claim on a
99-question benchmark, not a universal one. A dataset with different
error-class composition, a larger question set, or different frontier
models might yield a detectable intra-cluster gap."[^c4]

Absence of a
significant pairwise difference is also not evidence of equivalence — a
non-inferiority test would be needed to bound how close the clusters
truly are, and none is run. The paper does not report a separate
hallucination-rate metric (it names but does not measure "silent
hallucination" as distinct from ordinary failure), so this note's
support is for accuracy convergence only, not for a hallucination-rate
claim. The document was hand-authored by the paper's own team for the
same dataset the questions were drawn from, so the result bounds a
best-case document, not an average one.

A second benchmark points the same way from another domain. LongDA poses 505 analytical queries over U.S. national surveys whose documentation is long, "with an average length of 263k tokens."[^c5] Each query fixes the analytical goal, but the agent must first learn which variables to use, and "assign weights, and define populations before performing multi-step computations."[^c6] The authors find that explicit reasoning does not help: it "does not provide clear performance improvements on LongDA," and they read the core difficulty as "discovering and extracting sufficient information from long, complex documentation."[^c7][^c8] The lookup, not the inference, is again where the difficulty sits. LongDA does not run the paired with-and-without-documentation comparison this note rests on, so it is consistent with the document carrying the difficulty without establishing that alone.

## Related

[[rule-gated-behavior-gate]] · [[black-box-correctness-ceiling]] · [[text-to-sql-ambiguity-taxonomy]] · [[calibration]]

[^c1]: arxiv-2604-25149 — "Adding the document improves accuracy by +17 to +23 percentage points across all three models (paired exact McNemar, p ≤ 0.0015). With it, the three models are statistically indistinguishable (67.7–68.7%); without it, they are also indistinguishable (45.5–50.5%). Every cross-cluster comparison is significant at p < 0.01. The presence of the semantic-layer document accounts for essentially all of the significant variance; model choice within tier does not."
[^c2]: arxiv-2604-25149 — "Two clusters emerge cleanly. Within the semantic-layer cluster — Opus+Sem, Sonnet+Sem, GPT-5.4+Sem — none of the three pairwise comparisons is statistically significant (all p ≥ 0.79). Within the raw cluster — Opus raw, Sonnet raw, GPT-5.4 raw — none of the three pairwise comparisons is statistically significant either (all p ≥ 0.42). Every one of the nine cross-cluster comparisons is significant at p < 0.01, and most at p < 0.001."
[^c3]: arxiv-2604-25149
[^c4]: arxiv-2604-25149 — "We emphasize that this is a within-study statistical claim on a 99-question benchmark, not a universal one. A dataset with different error-class composition, a larger question set, or different frontier models might yield a detectable intra-cluster gap."
[^c5]: arxiv-2601-02598 — "with an average length of 263k tokens"
[^c6]: arxiv-2601-02598 — "assign weights, and define populations before performing multi-step computations"
[^c7]: arxiv-2601-02598 — "explicit reasoning does not provide clear performance improvements on LongDA"
[^c8]: arxiv-2601-02598 — "in discovering and extracting sufficient information from long, complex documentation"
[^c9]: arxiv-2603-04403
[^c10]: arxiv-2603-04403 — "Tool availability is the dominant factor."
[^c11]: arxiv-2603-04403 — "failed to commit to an answer, instead continuing to search until timing out or explicitly declining to answer."
[^c12]: arxiv-2603-04403 — "This behavioral pattern accounts for approximately 35pp"
[^c13]: arxiv-2603-04403 — "performance differences reflect complete systems"
