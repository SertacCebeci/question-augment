---
description: "A reference-free SQL accuracy score built from orthogonal filter-alignment and verdict components, multiplicatively discounted by the judge's own reported confidence tier."
aliases: ["STEF composite score", "confidence multiplier scoring"]
sources: ["arxiv-2604-28049"]
---
# Confidence-discounted composite score

> Score the answer on what it got right, then shrink the score by how
> sure the judge was that it got it right — uncertainty spends its own
> points rather than hiding inside the verdict.

## Definition / Mechanism

Arif & Singh (2026) score a generated SQL query
against a natural-language question with no gold SQL and no schema
available to the evaluator: "STEF extracts semantic specifications from
both natural language and SQL representations, performs normalized
feature alignment, and produces an interpretable 0 to 100 accuracy
score via a composite metric that encompasses filter alignment,
semantic verdict, and confidence of the evaluator."[^c1]

The score is a product, not a sum: a base score built from two
independently-graded orthogonal components, multiplied by a confidence
term. "B denotes the base score, computed as the sum of the filter
alignment score, the semantic verdict score, and an optional leniency
boost, and Γ denotes the confidence multiplier derived from the
evaluator's reported confidence." Each component is a small ordinal set: "σfilters ∈ {0, 3, 4, 5} is the filter
alignment score, σverdict ∈ {0, 2, 3, 5} is the semantic verdict score,
and δlenient ∈ {0, 1} is a leniency boost applied in cases where
normalization rules determine that a borderline filter classification
is attributable to a benign production SQL pattern rather than a
genuine semantic error." Filter alignment is a deterministic,
rule-based classification against the extracted filter predicates; the
verdict is the LLM judge's own four-point holistic call. Keeping them
separate means a query is diagnosed component-by-component instead of
collapsing to one opaque number.

The multiplier is what does the calibration work. It is piecewise on
the judge's self-reported confidence γ, not learned end-to-end: three
tiers {1.0, 0.8, 0.5} at thresholds 0.85 and 0.65. "The confidence
multiplier serves a dual function. First, it transforms evaluator
uncertainty from a noise source into an explicit scoring signal:
queries where the LLM evaluator expresses low confidence are penalized
in proportion to that uncertainty, ensuring that high scores are only
achievable when the evaluator is strongly confident in its
assessment." The thresholds and values are fitted, not arbitrary:
"determined empirically through calibration against developer-assessed
correctness labels on a held-out sample of production queries,
selecting thresholds that maximized the correlation between composite
score tiers and human correctness judgments. The multiplier values
{1.0, 0.8, 0.5} were chosen to produce a meaningful score depression at
moderate confidence (20% reduction) and a strong penalty at low
confidence (50% reduction), reflecting the asymmetric cost of false
positives in production monitoring contexts." An overconfidently wrong high
score costs a deployment more than an underconfident low score on a
query that was fine, so the multiplier is steeper below the
low-confidence threshold than above the high one.

## Why it matters

This makes a judge's self-reported certainty load-bearing without a
separate abstention decision. Most judge pipelines ignore confidence or
gate on it. Here confidence multiplies through to the same scalar the
correctness components produce, so one number reflects both "how
wrong" and "how sure," thresholded into tiers for triage.

## Limits

The thresholds (0.85, 0.65) and multiplier values (1.0, 0.8, 0.5) were
tuned to one held-out sample against one organization's developer
labels; the paper reports no cross-deployment validation. The confidence score is self-reported by the same LLM
producing the verdict — the paper does not verify that γ tracks actual
correctness likelihood rather than fluency at stating a number, and
notes residual "stochastic variation … on borderline query instances
despite temperature-0 inference" as an open weakness
(unverified). The score sets ({0,3,4,5}, {0,2,3,5}) are hand-picked
integers, not fitted to a loss.

## Related

- [[rubric-complexity-normalized-reward]] — another composite score
  that keeps per-criterion grading separate before combining.
- [[calibration]] — the general property this multiplier is trying to
  buy at the level of a single score rather than a population.
- [[business-truth-rate]] — a different reference-free production
  text-to-SQL metric, scored over tasks rather than per-answer
  components.
- [[context-dominates-model-choice]] — same domain (production
  text-to-SQL), a different question (what drives accuracy, not how to
  score it).
- [[effective-independent-votes]] — another attempt to make a judge's
  expressed uncertainty count rather than being absorbed.

[^c1]: arxiv-2604-28049 — "STEF extracts semantic specifications from both natural language and SQL representations, performs normalized feature alignment, and produces an interpretable 0 to 100 accuracy score via a composite metric that encompasses filter alignment, semantic verdict, and confidence of the evaluator."
