---
description: "An answerer's read of a question is measured by the set of distinct plausible readings it generates and the share of that set an answer addresses."
aliases: ["interpretation space", "SI", "interpretation coverage"]
sources: ["arxiv-2604-15140"]
---
# Interpretation space

> A question's ambiguity is not a flag to raise or lower — it is a set to
> enumerate, and an answer's strategy is legible as the fraction of that set
> it covers.

## Definition / Mechanism

**Construction (Srikanth, Boyd-Graber & Rudinger (2026)).**
Given a question $Q$ and short context $C$ (e.g. the community it was asked
in), two LLMs (gpt-4.1 and claude-sonnet-4.6) are prompted to each generate a
variable number of candidate readings of $Q$ — a model may abstain and
generate none if it judges $Q$ clear. The pooled generations are deduplicated
(the algorithm of [[arxiv-2604-15140|Srikanth et al., cited as 2025 in the
paper]]) into a single set $S_I$, the question's **interpretation space**.
$S_I$ is built once per question, independent of any answer.[^c1]

**Coverage.** An answer's discourse is segmented (rhetorical-structure-theory
parsing) and each segment is labeled with a discourse act from a 21-act
ontology; acts that plausibly commit to a reading (e.g. asserting an answer,
giving an example) are *eligible* to be paired with an interpretation, while
acts that do not commit to one (rejecting the question's presupposition
outright) are marked ineligible and carry no interpretation. Each eligible
segment is assigned one member of $S_I$ (gpt-4.1, validated against two human
annotators: $\kappa=0.71$ on whether a segment addresses any interpretation
at all, 74% exact-interpretation agreement where both assign one). An
answer's **coverage** is the proportion of $|S_I|$ that appears among its
segments' assigned interpretations.[^c2]

**What it exposes.** Coverage varies by community and by answerer kind, not
just by question: explainlikeimfive and AskHistorians answers cover 40–45%
of $S_I$ for their questions, NoStupidQuestions only 34%; and, holding
questions fixed, LLM answers with default prompting systematically address
interpretations that fewer than 10% of human answerers address, at a rate
that reaches 20–40% depending on the model.[^c3]

## Why it matters

Comprehension is usually scored as a single decision — did the answerer
detect ambiguity, yes or no. $S_I$ replaces that binary with a partition: the
set of readings an answer *could* address is fixed independently of the
answer, so which subset an actual answer commits to is a measurable read of
the question, comparable across answerers and across communities without
requiring an oracle "correct" interpretation.

## Limits

$S_I$ is itself LLM-generated (pooled from two models, deduplicated
automatically), so it is a proxy for "reasonable readings a competent asker's
community would recognize," not a ground truth enumerated by the askers
themselves; the paper validates only the segment-to-interpretation assignment
against humans, not the interpretation set's completeness or correctness.
Eligibility (which discourse acts can carry an interpretation) is a modeling
choice baked into the 21-act ontology, developed on English Reddit answers —
whether it or the resulting $S_I$ transfer to other languages or answer
genres is unverified.

## Related

- [[question-under-discussion]]
- [[levels-of-information-need]]
- [[false-premise-question]]
- [[qud-parsing]]

[^c1]: arxiv-2604-15140 — "a space of reasonable, distinct interpretations SI from Q via direct prompting"
[^c2]: arxiv-2604-15140 — "Not all discourse acts assume or address a particular interpretation (presupposition rejection cannot adopt an interpretation, since it contests the question’s premise rather than attempting to answer it)"
[^c3]: arxiv-2604-15140 — "explainlikeimfive and AskHistorians answers cover 40-45% of SI , versus only 34% in NoStupidQuestions"
