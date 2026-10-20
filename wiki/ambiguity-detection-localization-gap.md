---
description: "In interactive NL2SQL, LLMs flag that a query is ambiguous at near-perfect rates while correctly identifying which schema elements it is ambiguous over stays far lower."
aliases: ["detection-localization gap", "DA-MA gap"]
sources: ["arxiv-2604-22313"]
---
# Ambiguity-detection-localization gap

> Knowing *that* a question is unclear is a different capacity from knowing
> *which part of it* is unclear — and the second lags the first by a wide,
> measured margin.

## Definition / Mechanism

Sullutrone et al.'s CLARITY benchmark (2026) annotates
each synthetic ambiguous or unanswerable NL2SQL query with the exact
schema-grounded span responsible (a **pivot term**) and the group of
schema columns or values it could resolve to (a **target group**), so a
system's output can be scored two ways: **Detection Accuracy (DA)** — did
the system flag the query as ambiguous at all — and **Match Accuracy
(MA)** — did the flagged ambiguity align with the ground-truth pivot term
and target group. Prior NL2SQL ambiguity benchmarks carry only
instance-level ambiguous/unanswerable labels and so can only measure DA:
"these benchmarks rely largely on instance-level labels … and do not
assess whether systems correctly localize the schema elements responsible
for uncertainty. Consequently, high ambiguity-detection accuracy may mask
failures in schema-level identification and resolution."[^c1]

Measured on CLARITY, the two metrics diverge sharply for a production
ambiguity detector (AmbiSQL): "While detection accuracy (DA) is
near-perfect, match accuracy (MA) remains substantially lower, indicating
weaknesses in schema-level localization."[^c2]

The failure is not that the
detector is silent about *where* — it produces a clarification target
every time — but that the target is often wrong: "Because MA jointly
evaluates detection and alignment with ground-truth metadata, models often
correctly flag ambiguity but produce misaligned clarification outputs."[^c3]

The stated causes are confusable spans: misidentifying which term is
ambiguous, and conflating lexical ambiguity (shared surface form) with
semantic ambiguity (shared or related meaning) between candidate schema
entities.

## Why it matters

A comprehension step that only classifies "ambiguous / not ambiguous"
is answering a different, easier question than the one an answerer needs
answered before it can ask anything useful: which axis of the schema is
open. A system can pass every prior instance-level ambiguity benchmark —
which only checks the binary flag — while asking about the wrong column
or value on a majority of the queries it correctly flagged; the binary
metric cannot see this because it never checks alignment with the true
locus of uncertainty.

## Limits

The gap is measured for one detector (AmbiSQL) on synthetic,
LLM-generated ambiguous queries over two schemas (Spider, BIRD), not
across the space of NL2SQL ambiguity detectors or on naturally occurring
ambiguous queries; the paper's own category-conformance and screening
steps (majority vote among LLM judges) certify that each instance meets
its intended ambiguity definition, not that the DA/MA gap generalizes
beyond this construction pipeline. Whether the same detect-without-localize
pattern holds in comprehension tasks outside NL2SQL — where "schema
element" has no direct analogue — is not tested here.

## Related

[[shapley-uncertainty-localization]] · [[text-to-sql-ambiguity-taxonomy]] · [[black-box-correctness-ceiling]] · [[false-premise-question]] · [[interpretation-space]]

[^c1]: arxiv-2604-22313 — "correctly localize the schema elements responsible for uncertainty. Consequently, high ambiguitydetection accuracy may mask failures in schemalevel identification and resolution."
[^c2]: arxiv-2604-22313 — "While detection accuracy (DA) is near-perfect, match accuracy (MA) remains substantially lower, indicating weaknesses in schema-level localization."
[^c3]: arxiv-2604-22313 — "Because MA jointly evaluates detection and alignment with ground-truth metadata, models often correctly flag ambiguity but produce misaligned clarification outputs."
