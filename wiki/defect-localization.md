---
description: "Before a coding agent can ask a good clarifying question about a Task 2 of Ma, Zhao, Wu,"
aliases: ["defect localization"]
sources: ["ma-2026"]
---
# Defect localization

> Before a coding agent can ask a good clarifying question about a
> research-method specification, it has to find *which part* of the
> specification is the actually unresolved one — and that step, not the
> question that follows it, is where every tested model mostly fails.

## Definition / Mechanism

Task 2 of Ma, Zhao, Wu, Patwardhan & Cohan's (2026) IdeaAMBIG[^s1]
benchmark gives a model a specification that contains exactly one
implementation-critical gap (drawn from 163 real cases mined from
reproducibility reports and GitHub issues, or one of 497 synthetic gaps
injected into a specification already verified buildable) and asks it to
return a diagnosis: a category from the paper's taxonomy of gap types
([[efe-planning-as-variational-inference|ambiguity]], incompleteness or inconsistency, adapted for this setting from
prior requirements-quality work), a finer subcategory, and a
natural-language description of the defect. Success — Macro Defect [[recovery-postulate|Recovery]]
Rate (Macro-DRR) — "requires recovering the annotated blocker and both
taxonomy labels" (Ma et al. 2026, Appendix F): the score is compound, not a
pure location check, so a model that points at the right gap but assigns
the wrong category also scores a failure. The model receives only the
specification text, with no hint of where the gap is.

Across 13 LLMs, the best model's Macro-DRR on the real-world instances is
9.6%. The same paper's Task 3 ([[clarification-action-generation]]) gives a
model the specification *plus* the annotated defect and asks it to propose
a resolution; there the best model's Macro Clarification Action Success
Rate (Macro-CAS) is 80.6%, graded only on whether the proposed action
"addresses the blocker, obtains sufficient information, and avoids
unsupported assumptions" (Ma et al. 2026, Appendix F) — a criterion that
does not require reproducing the taxonomy label at all. Ma et al. read the
gap between the two numbers as the paper's headline finding: "defect
localization is the main bottleneck, with stronger clarification given the
defect" (Ma et al. 2026, abstract).

## Why it matters

This is a direct measurement on stall 2 (which axis first?) in a setting
most rows on Selection do not model: instead of ranking several
*already-enumerated* candidate axes by an information or value score, the
agent must first find which single axis, out of an entire specification's
worth of stated and unstated content, is the one that is actually
unconstrained. [[expected-information-gain]] and the other criteria on that
map presuppose the candidate question set already exists; this result
measures the step that produces that set. But the two numbers are not a
clean isolation of "find the axis" from "act on the axis": Macro-DRR scores
location *and* two-level classification together, while Macro-CAS does not
score classification at all, so a model that locates the gap correctly but
mislabels it fails Macro-DRR for a reason that has nothing to do with
Task 3's criterion. The 9.6% figure is therefore an upper bound on pure
localization difficulty, not a measurement of it in isolation — the true
gap between "find the axis" and "act on it, once found" could be narrower
than 9.6% vs. 80.6% suggests, though the paper gives no way to recover the
location-only number from what it reports. Even read this way, the result
still says that whatever a model must do to pass Macro-DRR is far harder
than what it must do to pass Macro-CAS, and reframes "ask a good question"
as (at least) two separably-measured steps rather than one.

## Transfer

| | |
|---|---|
| In its home field | an LLM graded on locating and classifying one deliberately present, evidence-grounded gap in a written research-method specification, against an annotated gold location and a two-level taxonomy label |
| Here | the general problem of deciding which axis of $W$ a specification leaves open, prior to ranking or wording any question about it |
| What survives | the separation of "find (and classify) the axis" from "act on the axis" as two differently-measured capabilities, and the finding that the former is the harder one in this domain |
| What does not | the specific 9.6% figure as a pure localization number (it is a compound location+classification score), the exact taxonomy category list (not independently confirmed in this reading), and any mechanism for *why* localization is hard — the paper reports the gap, not an explanation of it |

## Limits

- Macro-DRR is a compound metric: it "requires recovering the annotated
  blocker and both taxonomy labels" (Ma et al. 2026, Appendix F), while
  Macro-CAS scores only whether the proposed action resolves the blocker
  and never requires a taxonomy label. The two scores are not graded on the
  same kind of criterion, so 9.6% is an upper bound on how hard pure
  axis-finding is, not an isolated measurement of it — some unknown share
  of the 90.4% failure rate is a model that found the right location but
  named the wrong category.
- The 9.6%/80.6% contrast is read from the paper's abstract and its
  appendix's metric definitions; the per-model breakdown and the full
  taxonomy table (reported by secondary summaries as Table 8) were not
  independently confirmed in this reading and no per-model number is
  claimed here.
- Every instance is constructed to contain exactly one gap; a specification
  with zero or several unresolved axes is outside what Macro-DRR measures,
  so "localization is the bottleneck" is established for the single-gap
  case only.
- The synthetic majority of the benchmark (497 of 660 instances) injects a
  gap into an already-good specification; whether localization is equally
  hard on a specification that was simply never finished, rather than
  damaged, is not separated out in the abstract-level numbers used here.

## Related

Selection · [[clarification-action-generation]] · [[codification-readiness]] · [[expected-information-gain]] · [[ambiguity-taxonomy]] · [[clarification-benchmarks]]

[^s1]: ma-2026
