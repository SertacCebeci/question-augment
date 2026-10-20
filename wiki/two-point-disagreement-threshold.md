---
description: "Deriving calibration rules only from LLM-judge/human disagreements of magnitude 2 or more on a 5-point scale, since single-point gaps are ordinary subjective variation, not error."
aliases: []
sources: ["arxiv-2604-24158"]
---
# Two-point disagreement threshold

> Not every disagreement is an error — only the ones a human would call
> wrong.

## Definition / Mechanism

When an LLM judge and a human majority score the same pairwise comparison
on a signed 5-point scale $s_d \in \{-2,-1,0,+1,+2\}$, the two can differ by
one point for reasons that are not failures: two reasonable evaluators
read the same evidence and weigh it slightly differently. The method
treats only the large gaps as evidence of a fixable error, and calibrates
against those alone: "we only include the two-point disagreements in our
misalignment analysis", because "single-point differences are common
across both human-human and judge-judge comparisons and generally reflect
acceptable subjective variation rather than errors worth correcting"
Concretely, a case enters the calibration-rule-derivation set only when
$|s_d^{llm} - s_d^{human}| \geq 2$ — a directional conflict, not a shade
of emphasis. The filtered set of large disagreements is then read for
recurring patterns (entity-type errors, ignored seasonality, unsubstantiated
claims) and turned into a small number of explicit rules and few-shot
examples that are added to the judge's prompt, evaluated against
sustainable city-trip recommendations in
Banerjee et al. (2026).

The threshold is a design choice, not a derived optimum: the paper is
explicit that it is "empirically justified" for this task rather than
proven, and flags that stacking several rules learned this way onto one
prompt is untested for interference.[^c3]

## Why it matters

A judge-calibration loop that corrects every disagreement chases noise:
on a subjective, multi-point scale, some disagreement between any two
evaluators — including two humans — is the floor, not a signal. Filtering
by disagreement *magnitude* before deriving corrective rules keeps the
loop from overfitting to idiosyncratic single-point wobble and pointed it
instead at the disagreements that indicate a judge missed something a
human evaluator reliably catches (a factual error, a violated constraint,
an unsubstantiated claim). This separates "the judge and the reference
disagree" from "the judge is wrong" — the second is what a calibration
step should actually target.

## Limits

The 2-point cutoff on a 5-point scale is tuned to this task's scale and
is not shown to transfer to a different scale or a different number of
evaluators; the paper names this directly as future work rather than a
settled result.[^c3] The method also assumes a usable notion of "the human
majority" per case, which requires multiple human raters per query — it
does not specify how the threshold behaves with a single human reference.

## Related

- [[rubric-complexity-normalized-reward]]
- [[calibration]]
- [[dual-judge-completeness-recall]]
- [[effective-independent-votes]]

[^c3]: arxiv-2604-24158 — "While the two-point threshold is empirically justified, future work should examine whether stacking multiple calibration rules introduces noise."
