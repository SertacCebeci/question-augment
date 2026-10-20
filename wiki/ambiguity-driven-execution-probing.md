---
description: "SOMA-SQL resolves NL2SQL ambiguity by turning candidate-SQL disagreement and a taxonomy into probe SQL queries, executing them, and reading results as disambiguation evidence — no clarification turn."
aliases: ["ambiguity-driven execution probing", "SOMA-SQL", "execution-grounded probing", "disagreement-triggered tool recruitment"]
sources: ["somayajula-2026", "arxiv-2512-07132", "arxiv-2511-21402"]
---
# Ambiguity-driven execution probing

> A question about the true intent behind an underspecified NL query is
> answered by executing SQL against the database instead of asking the user —
> the database, not a person, fills the constraint slot.

## Definition / Mechanism

Somayajula, Liu & Lei (2026) build a diagnostic set of
candidate SQL queries for one NL question, then use disagreement between
them together with a fixed [[ambiguity-taxonomy|ambiguity taxonomy]] to locate what is
underspecified: "cross-candidate disagreements expose the unresolved
semantic ambiguities. SOMA-SQL then maps these conflicts, guided by a
predefined ambiguity taxonomy, into structured [[efe-planning-as-variational-inference|ambiguity]] dimensions, and
probes the database with targeted SQL queries to gather evidence for each."
[^c1]

Instead of asking the user which option is intended, the system executes a
query per candidate option and reads the results as evidence: "SOMA-SQL
generates targeted probe SQLs and executes them on the database instance D.
Probe SQLs are executable queries designed to gather evidence for a
specific ambiguity dimension rather than answer the user query directly."
For a "churn" query, for instance, if the canceled-subscription reading of
churn returns stronger, more temporally consistent evidence than the
alternatives, the probe results select that reading; an LLM resolver then
reads the compiled evidence across all probed dimensions and repairs the
seed SQL under the resolved intent.[^c2]

Across five text-to-SQL benchmarks this raised execution accuracy: "SOMA
-SQL improves execution accuracy by 13.0% on average over state-of-theart
baselines, with gains of up to 16.7% on ambiguous questions."[^c3]

## Why it matters

For stall 4 (where does the constraint come from — who answers?), this
names a third answerer besides the user and a fixed knowledge base: the
**environment itself, queried**. The taxonomy names which axis is open (the
[[text-to-sql-ambiguity-taxonomy]] supplies it here); execution probing is
the mechanism that fills that axis's slot without a clarification turn, by
treating each candidate option as a hypothesis and the database's own
response as the constraint.

## The same trigger with vision tools

The shape recurs outside text-to-SQL. In DART, a multi-agent visual question-answering system, an LLM recruiter reads the answering agents' reasoning and names where they disagree, then picks a tool from a pool to address that point: "DART adaptively calls tools based only on the points which the VLMs disagree on."[^c4] The recruiter "proceeds to construct a vision tool set and corresponding input parameters," and the tool outputs return to the debate, whose stated purpose is "for fruitful multi-agent discussion by introducing new information."[^c5][^c6]

The probe here is a specialist vision model, not a database query, and the evidence feeds a discussion and an aggregator rather than one execution. What carries over is the trigger: disagreement among candidate answers selects which evidence to gather. What does not carry over is a check that the gathered evidence is decisive. A SQL result can be compared against the database; a detector's output on a disputed scene is an expert opinion, and the wiki has no way to score it as ground truth (my inference). The debate side of this is in debate-without-new-information, and the use of the tool output as a per-agent weight is in [[tool-agreement-weighting]].

## Probing without a named ambiguity

DSR-SQL (Hao et al., 2025) also probes the database, but not against a candidate reading. Before generation, "An LLM first generates a small set of simple probing queries" such as "SELECT COUNT(*)" and "SELECT DISTINCT) to inspect key value distributions and entity relationships", and a second prompt condenses the results into a note on enumerations, units and synonyms that the generator reads.[^c8] The probe is a survey of the data, chosen before any ambiguity is named. The ablation locates its value in the grounded content: "using Summarization alone," without the probe results, "can even be detrimental, yielding results comparable to a simple divide-and-conquer approach".[^c9] So a summary written without data behind it does not help. The paper does not compare this survey with candidate-disagreement probing, so which design needs fewer probes is not settled by either source (my inference).

## Limits

The mechanism only works when the environment is queryable and each
candidate option is executable and separable by its results (SQL against a
concrete database instance); it gives no procedure for a domain without an
executable ground truth. Its coverage is bounded by the ambiguity taxonomy
used to generate taxonomy-induced dimensions — a dimension the taxonomy
does not name is never probed. The 13.0%/16.7% figures are execution
accuracy on five benchmarks with GPT-5.3-class backbones; no result is
reported for weaker backbones or dimensions the paper's own taxonomy omits. The vision analogue is one other paper's result: on A-OKVQA its tool-recruited discussion beats the next-best debate baseline "by 3.4% on A-OKVQA," and the sections read do not check the recruiter's choices against a reference.[^c7]

## Related

[[text-to-sql-ambiguity-taxonomy]] · [[automated-clarification-proxy-bound]] · [[data-processing-inequality]] · [[clarification-benchmarks]]

[^c1]: somayajula-2026
[^c2]: somayajula-2026
[^c3]: somayajula-2026
[^c4]: arxiv-2512-07132 — "DART adaptively calls tools based only on the points which the VLMs disagree on"
[^c5]: arxiv-2512-07132 — "proceeds to construct a vision tool set and corresponding input parameters"
[^c6]: arxiv-2512-07132 — "for fruitful multi-agent discussion by introducing new information"
[^c7]: arxiv-2512-07132 — "by 3.4% on A-OKVQA"
[^c8]: arxiv-2511-21402 — "An LLM first generates a small set of simple probing queries"
[^c9]: arxiv-2511-21402 — "can even be detrimental, yielding results comparable to a simple divide-and-conquer approach"
