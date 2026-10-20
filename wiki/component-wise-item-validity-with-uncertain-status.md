---
description: "A benchmark question is three separately valid-or-not parts (problem, answer, rationale) with a third status, uncertain; on HLE, flawed keys depressed accuracy and inflated miscalibration."
aliases: ["component-wise benchmark verification", "HLE-Verified protocol", "verified-revised-uncertain partition"]
sources: ["arxiv-2602-13964"]
---
# Component-wise item validity with an uncertain status

A question-answer item is not one binary "good or bad" object. Zhai et al. (2026) split each Humanity's Last Exam (HLE) item into the problem (statement plus image), the final answer and the rationale (reference solution). Problem and answer are the primary objects of correctness; the rationale is "diagnostic support for detecting inconsistencies, missing assumptions, or explanation defects."[^c1] Validity is defined per component: a problem is well-posed and sufficiently specified, an answer is correct "including units, format, and acceptable equivalence classes", a rationale is sound and compatible with the answer.[^c2]

## The three-way outcome

Of 2,500 items, 668 were validated unchanged (gold), 1,143 were repaired under a preserved-evaluation-objective constraint and re-verified, and 689 stayed in an uncertain set kept with an uncertainty-source label and a required-expertise tag.[^c3] The uncertain set is meant to "separate capability limits from benchmark indeterminacy": an item lands there when resolution needs non-standard assumptions, outside references, unresolved expert disagreement or knowledge beyond the verification scope.[^c4] Items enter gold only when problem and answer are both judged unproblematic and no high-risk ambiguity remains; model pass@8 replication is used as evidence of extreme human-model disagreement, not as a replacement for experts.[^c5]

## Where defects sit

Among items that failed Stage I, reliability falls from problem to answer to rationale: problems are the most reliable, only about half of answers are fully valid, and invalid rationales outnumber valid ones.[^c6] Domains differ in kind, not only in rate. Math and biology/medicine problems exceed 92% valid, but physics shows only 30.0%; in the low-validity domains most non-valid labels are "uncertain" rather than "invalid", which the authors read as verification difficulty rather than structural error.[^c7] Within the revised subset, an incorrect answer key is the dominant answer defect in every subject, and the authors conclude that most defects come from specification or answer-key instability, not wrong task concepts.[^c8] The taxonomy has 19 categories: 5 problem, 10 rationale, 4 answer.[^c9]

## What the flaws did to measurement

On the revised subset, accuracy rose by roughly 30 to 40 points for six frontier models (for example GPT-5.2 +38.04, DeepSeek-V3.2 +39.58); on the full set by about 7.6 to 10.8 points.[^c10] Calibration error fell as well (GPT-5.2 on the revised subset, 63 to 28), so flawed keys produced confidently "wrong" responses.[^c11] On items with erroneous statements, repair raised mean self-reported confidence for every model by +1.83 to +11.08 points, while full-set shifts were near zero because most items are unchanged.[^c12] My inference: confidence drop on an item is therefore a weak flag for a flawed statement, but this paper tests it only as an aggregate before/after shift, not as a per-item detector.

## Limits

- Repair was restricted to mathematics, physics, chemistry, biomedicine and computer science; weakly verifiable domains were routed to uncertain, so the partition is conservative, not complete.[^c13]
- The verification relies on expert suppliers and the same class of frontier models that are then evaluated; no independent ground truth for "correct" exists beyond adjudication.
- Accuracy gains on revised items are not purely noise removal: repaired problems may also be easier or clearer. The paper reads the gain as flawed items suppressing performance; separating key correction from clarification is not done here (my reading).
- Defect proportions are reported for the non-gold items only, not for HLE as a whole.
- The confidence result is a mean shift with one prompt format; no per-item discrimination was measured.

## Related

- [[model-dependent-benchmark-difficulty]] — another way a benchmark score fails to be an objective cross-model measure
- [[ambiguity-versus-incapability-routing]] — separating an ill-posed question from a model's failure, as the uncertain set does for items
- [[underspecified-question-eager-answering]] — models answer underspecified statements confidently, matching the confidence-on-flawed-items finding
- [[detect-verify-escalate-pipeline]] — a staged check-then-escalate structure comparable to Stage I/II

[^c1]: arxiv-2602-13964 — "while the rationale serves as diagnostic support for detecting inconsistencies, missing assumptions, or explanation defects."
[^c2]: arxiv-2602-13964 — "including units, format, and acceptable equivalence classes."
[^c3]: arxiv-2602-13964 — "Uncertain subset (689 items): items whose validity remains indeterminate under available expertise and evidence."
[^c4]: arxiv-2602-13964 — "This design separates capability limits from benchmark indeterminacy and enables principled community refinement."
[^c5]: arxiv-2602-13964 — "Items enter the gold subset only when both problem and answer are judged unproblematic and no high-risk ambiguity is identified."
[^c6]: arxiv-2602-13964 — "Invalid rationales outnumber valid ones"
[^c7]: arxiv-2602-13964 — "Physics shows only 30.0% valid problem statements"
[^c8]: arxiv-2602-13964 — "Most defects arise from specification or answer-key instability rather than from fundamentally incorrect task concepts."
[^c9]: arxiv-2602-13964 — "organized as 5 problem-level errors, 10 rationale-level errors, and 4 answer-level errors"
[^c10]: arxiv-2602-13964 — "Claude-Opus4.6 (+30.13), and DeepSeek-V3.2 (+39.58) percentage points."
[^c11]: arxiv-2602-13964 — "Calibration error decreases consistently after revision on the same subset"
[^c12]: arxiv-2602-13964 — "with gains ranging from roughly +1.83 to +11.08 confidence points"
[^c13]: arxiv-2602-13964 — "Items in domains with weak verification boundaries or subjective conventions are handled conservatively (routed to the uncertain subset)."
