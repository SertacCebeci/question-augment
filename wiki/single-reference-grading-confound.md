---
description: "Grading judgment answers against one expert's solution scores professional disagreement as error; independent analysts graded against each other agree only at a median 0.33, so use practice envelopes."
aliases: ["one analyst is not ground truth", "practice-envelope grading", "single-expert reference grading"]
sources: ["doi-10-48550-arxiv-2607-24889", "doi-10-48550-arxiv-2605-23454"]
---
# Single-reference grading confound

Many benchmarks anchor correctness to one expert-authored solution, numerical targets or a detailed rubric. That carries a hidden assumption: when the answerer differs from the reference, the answerer is wrong.[^c1] The assumption holds where the domain has a unique answer and fails where competent experts legitimately differ.

## The test

The GAUGE paper tests the assumption by grading independently built professional financial models of the same company against one another. Across 108 same-company pairs from 65 companies the median score was 0.33, and 92.6% of pairs fell below 0.70 under standard tolerances.[^c2] Even at four times the tolerances, a third still fell below 0.70, and among models built from the same fiscal-year data no pair agreed on implied share price within 10%.[^c3] Disagreement was concentrated on the quantities where judgment matters, not spread evenly.[^c4] A single-reference rule therefore confounds professional disagreement with error.

## The remedy as a split

The proposed principle is to use exact answers where the domain gives them and professional practice where judgment can differ.[^c5] Mechanical properties (historical figures match, balance sheet balances, live formulas) are checked deterministically. Judgment-bearing quantities are compared with an envelope: a range observed across many professional workbooks. Qualitative aspects go to a frozen LLM judge under explicit rubrics.[^c6]

The split was validated as an instrument. Senior analysts, junior analysts and students scored 88.3, 66.0 and 43.2, and the ordering survived robustness checks.[^c7] The measured payoff: every one of 24 LM agents did better on mechanical construction than on judgment, a median gap of 26 points, against a 3.6-point gap for senior analysts.[^c8] Under a single reference that gap would be unreadable, since judgment error and legitimate difference would be mixed.

The same rule appears as an RL reward in a different domain. In an ablation over seven benchmarks, a reward that compares each response with one reference answer was strongest on HealthBench but the least stable across task types: it "drops sharply on IFEval (10.54)".[^c11] Its average was the lowest of the four rewards compared, "despite its strong HealthBench performance".[^c12] The authors read this as the limit of one reference answer as the reward target for heterogeneous tasks. It is a reward-design result, not a finance grading result, so it supports the rule's scope without measuring the envelope.

## Limits

- The authors say the envelope is a "reference distribution of observed practice, not ground truth": an in-band value is defensible, which is weaker than correct.[^c9]
- Observed workbook differences mix legitimate choice with date, horizon, purpose and quality heterogeneity, so the 0.33 figure overstates pure judgment disagreement. The authors scope their conclusion to the single-reference rule itself.[^c10]
- Only 17 undirected pairs support the implied-price disagreement tail, and all data come from one commercial provider network with a US skew.[^c10]
- Finance only. Whether other open-ended domains show similar inter-expert spread is not tested here; that extension is my inference.

## Related

- [[reference-answer-defect-audit]] — another way a reference answer misleads: defects in it, rather than legitimate plurality
- [[question-specific-rubric]] — the ablation in which the single-reference reward is compared with a per-question rubric as the RL reward

[^c1]: doi-10-48550-arxiv-2607-24889 — "assumption: one expert solution can serve as ground truth. This is appropriate when"
[^c2]: doi-10-48550-arxiv-2607-24889 — "the median score is only 0.33, and"
[^c3]: doi-10-48550-arxiv-2607-24889 — "Even at four times these tolerances, a third"
[^c4]: doi-10-48550-arxiv-2607-24889 — "with disagreement concentrated"
[^c5]: doi-10-48550-arxiv-2607-24889 — "use exact answers where finance provides them, and"
[^c6]: doi-10-48550-arxiv-2607-24889 — "Quantities that depend on financial judgment"
[^c7]: doi-10-48550-arxiv-2607-24889 — "This ordering remains unchanged across our robustness checks"
[^c8]: doi-10-48550-arxiv-2607-24889 — "senior analysts show only a 3.6-point gap on the same facets, suggesting that"
[^c9]: doi-10-48550-arxiv-2607-24889 — "The envelope is a reference distribution of observed practice, not ground truth"
[^c10]: doi-10-48550-arxiv-2607-24889 — "observed workbook differences mix legitimate choice"
[^c11]: doi-10-48550-arxiv-2605-23454 — "it drops sharply on IFEval (10.54)"
[^c12]: doi-10-48550-arxiv-2605-23454 — "obtains the lowest average score despite its strong HealthBench performance"
