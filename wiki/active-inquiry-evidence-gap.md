---
description: "Multi-turn active evidence-seeking drops clinical diagnostic accuracy 12.75% and evidence quality 24.36% vs. full-context, evidence quality decaying faster."
aliases: ["active-passive capability gap", "hallucinated reasoning", "evidence-diagnosis decoupling"]
sources: ["zhan-2026"]
---
# Active-inquiry evidence gap

> Making a model ask its own questions instead of reading the full chart
> costs it twice: it gets the diagnosis wrong more often, and it loses track
> of its own evidence even faster than that.

## Definition / Mechanism

On [[rounds-bench|ROUNDS-Bench]], Zhan, Qiu, Tan et al. (2026)
report that across 468 cases and 15 models, "multi-turn evidence seeking
reduces diagnostic accuracy by 12.75% and lowers supporting-evidence quality
by 24.36% relative to full-context evaluation; error analyses associate
these drops with premature diagnostic closure and inefficient questioning."
[^c1]

The two drops are not the same size, and the gap between them is itself the
finding: "We observe that the decline in evidence quality (StrictEQ) is
larger than the decline in diagnostic accuracy... the Evidence Gap (the
StrictEQ differential between Task 1 and Task 2) is consistently wider than
the Accuracy Gap across the majority of models. In other words, as models
transition from static to dynamic environments, their ability to retrieve
evidence decays significantly faster than their ability to output correct
diagnostic labels." The paper names the resulting case type — correct
diagnosis, incomplete cited evidence — "Hallucinated Reasoning, effectively
getting the right answer for the wrong (or non-existent) reasons."[^c2]

Error analysis also rules out a simple explanation: cases that were
strictly correct in Task 1 do not degrade to partially-correct in Task 2;
"a substantial proportion shifted directly to the Wrong category," which
the paper reads as models not becoming more conservative under incomplete
information but instead "constructing erroneous causal chains based on
fragmented or insufficient evidence."[^c3]

## Why it matters

This is a quantified cost of the answerer having to select and stop its own
questions rather than being handed everything: the two numbers (12.75%,
24.36%) give stall 7 a concrete price for [[premature-closure|premature closure]] and inefficient
questioning in one domain, and the wider evidence-gap-than-accuracy-gap
shows the price is paid disproportionately on the part of the process
(tracking and citing why) that a downstream user would need to audit the
answer, not on the surface-level correctness a benchmark usually reports.

## Limits

- Both premature closure and "inefficient questioning" are named as the
  error-analysis explanation for the drops, but this is not a causal
  mechanism distinguishing the two — only an association with the observed
  decline (see claim[^c1] above).
- The 12.75%/24.36% figures are averages across 15 models of varying scale
  and architecture (Section 2.4 reports substantial per-model variation,
  e.g. larger models buffer some of the gap); a single model's drop is not
  implied by the average.
- Grading (diagnostic accuracy, StrictEQ) is by an automated judge; no
  physician inter-rater check is reported in the slice read.
- Single benchmark, single time window (2026); whether the same
  accuracy/evidence-quality decoupling appears outside clinical diagnosis is
  not tested here.

## Related

[[rounds-bench]] · [[premature-closure]] · [[mediq]] · Stopping

[^c1]: zhan-2026 — "multi-turn evidence seeking reduces diagnostic accuracy by 12.75% and lowers supporting-evidence quality by 24.36% relative to full-context evaluation; error analyses associate these drops with premature diagnostic closure and inefficient questioning"
[^c2]: zhan-2026
[^c3]: zhan-2026 — "a substantial proportion shifted directly to the Wrong category"
