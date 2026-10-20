---
description: "A database that names fiscal periods by an unstated convention makes agents query the wrong period even when they read the question right; in one benchmark that was nearly two-thirds of errors."
aliases: ["period convention misalignment", "fiscal year labeling convention", "start-year versus end-year naming"]
sources: ["arxiv-2603-04403"]
---
# Fiscal-period label mismatch

When a structured financial database names a period by its own convention, a retrieval agent must translate the question's period into that convention before it can read any value. The database in FinRetrieval, Daloopa, labels a fiscal year by the calendar year in which it starts, so its "2022FY" covers April 2022 to March 2023.[^c1] An agent that reads a March year-end company's fiscal 2023 as the calendar year ending in 2023 queries a row that holds a real number for the wrong year. The answer is well formed and the question was understood; only the lookup key is wrong.

The mechanism is measured in the best configuration. Claude Opus 4.5 with reasoning and the structured tools scored 90.8%, and of its 46 errors, 29 are period confusion, which the paper summarizes as: "Period confusion alone accounts for nearly two-thirds of all failures."[^c2] The authors' reading is that agents "understood the questions correctly but queried incorrect periods due to undocumented" tool conventions.[^c3] The claim concerns where the error sits, not the reasoning: the agent can parse the question and still fail at the key.

The same mismatch appears at the first lookup. For Claude, 58 first structured searches failed. Re-run without period constraints, the search succeeds in 26 of them, so the period filter, not keyword matching, is the cause in those cases.[^c4] Of those 26 period failures, the paper assigns 46 percent to convention misalignment, 27 percent to granularity (an annual query against quarterly data), and 23 percent to guidance indexed by announcement period rather than target period.[^c5]

The geographic gap is the same mechanism. Claude scores 93.4% on US questions and 87.8% on non-US ones. At a December year-end, non-US accuracy (95.8%) slightly exceeds US accuracy (95.6%). The gap comes from non-standard year-ends: March year-end companies score "64.7% accuracy (17 questions)" and September year-end companies 78.6% on 42 questions.[^c6] The paper's conclusion is that "The gap is not inherent to geography."[^c7] For quarterly questions, a non-December year-end maps fiscal quarters onto different calendar months entirely.[^c8]

What this means for asking: a question that names its period by a fiscal label carries a convention the asker may not share with the data source. The paper's proposed fixes sit on the tool side, in the tool descriptions and in what the API accepts: "Adding explicit convention details to tool descriptions could address the majority of current failures without" changing the model.[^c9] In the terms of [[retrieval-utilization-gap]], a period that never maps to the right key is a retrieval-side failure, since the evidence never surfaces. That classification is my reading; the paper does not use those terms.

## Limits

The benchmark was generated with period handling in mind: the question-generation prompt carried task instructions for "disambiguation rules, sign conventions, period" naming.[^c10] The paper does not report how often a question's text names a fiscal convention itself. How much of this error occurs on the period-ambiguous questions real users ask is therefore untested, and the 63% share may overstate or understate it for live use.

The "undocumented convention" diagnosis is the authors' reading. They did not rerun the same agents against documented conventions. Their statement that "Better tool documentation could address nearly two-thirds of current errors." is a projection from an error taxonomy, not a measured intervention.[^c11]

Subgroups are small. The March and September year-end cells hold 17 and 42 questions, and the paper notes that "statistical power is limited for fine-grained subgroup analyses."[^c12] The error taxonomy covers only the best configuration (46 errors); the error mix for the other models is not reported. The data source is one database, so these conventions are Daloopa's; other providers may label periods differently or not at all.

## Related

- [[context-dominates-model-choice]] — the same shape: a missing piece of information about the source, not model capability, decides accuracy
- [[retrieval-utilization-gap]] — the retrieval-side reading of this failure (my classification)
- [[search-effort-accuracy-decoupling]] — a first lookup that misses on a period key is one route by which effort and accuracy come apart

[^c1]: arxiv-2603-04403 — "queried 2023FY, but Daloopa uses starting-year convention where"
[^c2]: arxiv-2603-04403 — "Period confusion alone accounts for nearly two-thirds of all failures."
[^c3]: arxiv-2603-04403 — "agents understood the questions correctly but queried incorrect periods due to undocumented"
[^c4]: arxiv-2603-04403 — "period filter failures where the target is found when the period"
[^c5]: arxiv-2603-04403 — "guidance is indexed by announcement period rather than target period."
[^c6]: arxiv-2603-04403 — "March FYE (common for Japanese companies): 64.7% accuracy (17 questions)"
[^c7]: arxiv-2603-04403 — "The gap is not inherent to geography."
[^c8]: arxiv-2603-04403 — "For quarterly queries, fiscal quarters map to different calendar months entirely."
[^c9]: arxiv-2603-04403 — "Adding explicit convention details to tool descriptions could address the majority of current failures without"
[^c10]: arxiv-2603-04403 — "disambiguation rules, sign conventions, period"
[^c11]: arxiv-2603-04403 — "Better tool documentation could address nearly two-thirds of current errors."
[^c12]: arxiv-2603-04403 — "statistical power is limited for fine-grained subgroup analyses"
