---
description: "Group evidence records by a canonicalized, question-specific key, then resolve each group: merge duplicates, keep complements, settle only true conflicts by source authority."
aliases: ["evidence reconciliation", "reconciliation agent"]
sources: ["arxiv-2604-22294"]
---
# Primary-key evidence reconciliation

> Do not compare every extracted claim to every other claim. Group them by
> what would make two claims about the same thing, then resolve
> disagreement only inside a group, and only after asking whether it is a
> disagreement at all.

## Definition / Mechanism

SLIDERS (2026) extracts one evidence record per
(chunk, evidence-variable) pair from a document set, so the same fact
about the same entity accumulates many separate, differently-worded rows
before anything is checked against anything else. Comparing every pair of
$n$ records is $O(n^2)$ and "infeasible when the evidence table is
large." The paper's fix is to make coherence-checking a database
operation, not a pairwise one:

1. **Pick question-specific key columns.** For a given question, the
   system selects primary-key variables $K_q = \{k_1, \dots, k_m\}$ from
   the evidence schema — "a financial question may use company and fiscal
   year as primary-key variables, while a clinical question may use
   intervention, population, outcome, and time point." The key is not
   fixed by the domain; it is chosen per question.
2. **Canonicalize before grouping.** Key values are normalized so that
   surface variants of the same referent collide — "'J. Smith' and 'John
   Smith' may refer to the same person" — because grouping on raw
   strings would silently split one entity into many groups and hide the
   very conflicts reconciliation exists to find.
3. **Group, then compare only within a group.** Records sharing a
   canonicalized key tuple form one group $g_a$; reconciliation runs
   separately per group, cutting the comparison cost from $O(n^2)$ over
   the whole table to $\sum_{g} O(|g|^2)$ over the groups.[^c4]
4. **Classify what a group's disagreement actually is before resolving
   it.** A conflicting field is first checked for whether it is a
   *true* conflict or two legitimate, coexisting facts: "if conflicting
   field is a temporal/event field... and both values are equally valid
   → these represent separate events, keep all rows... if conflict is
   due to measurement error → resolve by selecting most reliable value."
 Two numbers under the same key are not automatically a
   contradiction — a segment total and a company total can both be true.
5. **Resolve a true conflict by source authority, not by vote or
   recency.** The agent ranks competing values by field-definition
   alignment, extraction-location relevance (a formally-reported figure
   over one mentioned in passing), source authority (structured tables
   over descriptive text, primary sections over explanatory ones), quote
   quality and rationale clarity — in that order — and keeps the single
   highest-ranked row, carrying its original quote and rationale forward
   as provenance.[^c6]
6. **What is not resolvable is marked, not forced.** Groups reduce to
   "merge duplicate records, combine complementary records, preserve
   meaningful distinctions, and mark unresolved conflicts" rather
   than being collapsed to a single value regardless.

Removing this stage is the paper's own ablation of the mechanism, not
just of the note's claim about it: on two benchmarks with large,
distributed evidence tables, accuracy drops from 78.91 to 60.50 and from
55.22 to 35.81 when reconciliation is skipped and extraction output is
passed straight to synthesis, while on a benchmark whose table already
fit in context, skipping it costs only 2.67 points.[^c8]

## Why it matters

The mechanism separates three questions that a naive "compare everything,
flag mismatches" repair conflates: which records are even candidates for
comparison (the grouping key), whether a comparison that disagrees is a
real contradiction or two true things under different scope (the
temporal/measurement split), and, only for real contradictions, which
value wins (the authority ranking). A repair procedure that skips the
middle step will "resolve" a segment-versus-total pair into one number
and destroy real information; one that skips the key step pays $O(n^2)$
for a check that grouping makes near-linear.

## Limits

- **The grouping key is chosen, not derived**, per question and per
  domain; a badly-chosen key either splits one entity across groups
  (missing a real conflict) or merges distinct entities into one
  (manufacturing a false one) — the paper names this failure mode
  directly: "aggressive canonicalization can collapse genuinely distinct
  entities, particularly in domains with high-cardinality keys or
  near-duplicate naming conventions."[^c9]
- **The temporal/measurement split is a heuristic, not a general
  taxonomy** of what counts as a real conflict; it is reported for this
  paper's evidence-variable schema, `unverified` beyond it.
- **Provenance can itself be wrong.** When a source span is misattributed,
  the authority ranking ranks a wrong quote as authoritative and the
  conflict is resolved to the wrong value with no downstream signal —
  the paper reports this as an open failure mode it does not detect for.
- **No inter-annotator or human check of resolution correctness** is
  reported in the extract read here; the accuracy gain is measured on
  downstream answer quality, not on whether individual reconciliation
  decisions were themselves correct.

## Related

[[atomic-entailment-repair-loop]] · [[conditional-functional-dependency]] ·
[[constraint-as-information]] · [[truth-maintenance-system]] ·
[[np-completeness]]

[^c4]: arxiv-2604-22294 — "the comparison burden is reduced from O(n2 ) over the full evidence table to"
[^c6]: arxiv-2604-22294 — "Direct measurements or final values over constituent parts or supplementary details - Structured presentations (tables, statements, forms, labeled fields) over descriptive text (discussions, notes, commentary) - Primary data sections over explanatory sections - Explicit field labels over derived mentions"
[^c8]: arxiv-2604-22294 — "removing it drops performance from 78.91 to 60.50 on WikiCeleb100 and from 55.22 to 35.81 on FinQ100"
[^c9]: arxiv-2604-22294 — "Aggressive canonicalization can collapse genuinely distinct entities, particularly in domains with high-cardinality keys or near-duplicate naming conventions."
