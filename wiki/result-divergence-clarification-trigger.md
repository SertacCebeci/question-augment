---
description: "Execute every candidate interpretation of an ambiguous query and clarify only when their outputs diverge past a preregistered threshold, not whenever the language itself is ambiguous."
aliases: ["CLARA", "result-sensitivity criterion", "result-divergence criterion"]
sources: ["shukla-2026"]
---
# Result-divergence clarification trigger

> [[efe-planning-as-variational-inference|Ambiguity]] is only worth a question if resolving it would change the
> answer: CLARA decides whether to clarify by running the candidate
> interpretations, not by scoring how uncertain the language is.

## Definition / Mechanism

CLARA represents a natural-language query as a typed scientific
specification with a small number of unresolved dimensions (e.g. mutation
scope, assay denominator, sample context). For each unresolved dimension it
executes both candidate specifications against the database and compares
the two prevalences $p_A, p_B$ by absolute divergence
$D_{abs}=100\times|p_A-p_B|$ and relative divergence
$D_{rel}=|p_A-p_B|/((|p_A|+|p_B|)/2+\epsilon)$. A contrast is flagged
**result-sensitive** — worth a clarification question — if $D_{rel}>0.10$
OR $D_{abs}>5$ percentage points; otherwise it is **result-stable** and
CLARA answers without asking. The OR rule was chosen so a small absolute
shift at low baseline prevalence is still caught by the relative term, and
a clinically evident absolute shift is not masked by a high baseline
prevalence.[^c1]

On a 330-contrast registered benchmark (8 TCGA cohorts × 30-gene panel),
34.8% of contrasts were result-sensitive and 65.2% result-stable, and
sensitivity depended heavily on *which* dimension was unresolved: mutation
scope was sensitive in 96.3% of comparisons (median relative divergence
0.848) versus 13.7% for assay denominator and 15.3% for sample context.[^c2]

On a separate 120-question language stress test, the full system recognized
all 60 result-sensitive contrasts and unnecessarily clarified 13 of 60
result-stable ones (accuracy 89.2%, sensitivity/recall 100%, specificity
78.3%); a standalone machine-learning mechanism parser reached higher
overall accuracy (97.5%) but missed one result-sensitive contrast — the
paper's own name for this is an explicit trade-off between safety (missing
a consequential ambiguity) and burden (asking about an inconsequential
one).[^c3]

## Why it matters

Two axes can be linguistically ambiguous to exactly the same degree and
warrant opposite treatment: the criterion for asking is not how uncertain
the *parse* is but whether the uncertainty survives contact with the
downstream computation. A system that clarifies whenever a dimension is
unresolved in language (never executing) will over-ask on axes like assay
denominator, where the answer rarely moves; one that never checks will
under-ask on axes like mutation scope, where it almost always does.

## Transfer

| | |
|---|---|
| Home field | Decision-relevant querying in a database/NLP pipeline (text-to-SQL / semantic-parsing systems) |
| Here | A general test for *when to ask*: don't score the question's linguistic ambiguity, execute each candidate answer and ask only if the executions disagree past a fixed tolerance |
| What survives | The structural move — defer the ask/don't-ask decision until after the candidate interpretations are resolved into comparable outputs — applies to any domain where "interpretation" cashes out as an executable, comparable result |
| What does not | The specific thresholds (relative 0.10 / absolute 5pp) and the divergence formula are tuned to prevalence percentages in this genomics benchmark and are not shown to transfer to non-numeric or non-executable answer spaces |

## Limits

The benchmark's ambiguity space is limited to three predefined dimensions
(mutation scope, assay denominator, sample context) over one query family
(mutation-prevalence contrasts); the claim that execution-grounded
divergence separates consequential from inconsequential ambiguity rests on
that closed set of interpretations enumerated by hand, not on a system that
discovers which interpretations exist. The 120-question stress test's
question pool was not checked for inter-rater [[calibration|reliability]] on ambiguity
type, and the paper reports this itself.[^c4]

## Related

[[value-of-information]], [[entropy-threshold-clarification-trigger]],
[[mutual-information]], [[clarification-request]]

[^c1]: shukla-2026 — "We flagged a contrast as result sensitive if D_rel > 0.10 OR D_abs > 5 percentage points. If not, it was result-stable."
[^c2]: shukla-2026 — "there were 330 distinct executable comparisons in the benchmark, 115 (34.8%) of which were result-sensitive and 215 (65.2%) of which were result-stable based on the registered criterion. Sensitivity greatly differed depending on mechanism. Mutation scope was sensitive in 79 out of 82 comparisons (96.3%)"
[^c3]: shukla-2026 — "CLARA recognized all 60 result-sensitive contrasts and needlessly clarified 13 of 60 stable contrasts (accuracy 89.2%, sensitivity/recall 100%, specificity 78.3%). Standalone machine learning had superior overall accuracy (97.5%) but missed one critical contrast."
[^c4]: shukla-2026 — "They did not record categorical form for any items, hence we cannot report inter-rater reliability, and we will use this resource as a language stress test of LLM output."
