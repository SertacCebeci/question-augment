---
description: "An LLM judge that scores an artifact against pre-decomposed binary sub-requirements, not one holistic grade, is argued to be steadier; the ablations do not isolate the decomposition."
aliases: ["problem specification", "requirement decomposition for LLM judges", "decomposed rubric judging", "MADE problem specification", "judge against sub-requirements"]
sources: ["arxiv-2511-19489"]
---
# Decomposed requirement judging

When an LLM grades a subjective output with one holistic score, the score is one draw, and the grader has to weigh every criterion implicitly while producing it. The MADE framework proposes a different shape for the same judgment. A requirement decomposer turns the user instruction into a set of sub-requirements, each "an assertion describing a specific criterion that the final artifact" must meet.[^d1] The judge then answers against that list. Its output is "a k-dimensional scoring vector", one entry per sub-requirement, plus natural-language feedback.[^d2] The scalar used for selection is obtained by aggregating the vector, which "converts the scoring vector v into a scalar fitness value."[^d4]

The mechanism the authors give is a change of unit. A vague question such as "Is this chart good?" is replaced by narrow ones such as "Is the chart a scatter plot?" and "Does the title exist?", and the paper describes this as turning "a high-variance evaluation task" into "a series of clear, specific, low-variance" judgments.[^d3] The step is named the cornerstone of the framework.[^d13] What the list does concretely is fix the weighting in advance: the criteria are written down before any artifact is seen, so a count of satisfied items replaces a verdict that mixes them. The noise of the judge is then spread over several small checks rather than concentrated in one large score. That is the authors' account; it is a reading of the design, not a measured effect.

## What was measured

The stability evidence concerns the judge as a whole, on chart images, not a comparison of a decomposed judge against a holistic one. At temperature 0.8 the paper reports "The single-rating absolute ICC reached 0.895", and under input noise the judge's scores stay consistent for good solutions.[^d5][^d14] Across both conditions the paper finds a negative relation between a case's mean score and its spread: "when the judge evaluates a solution highly, its scoring is more consistent."[^d6] This is evidence that a high-quality output is judged reliably. It does not show that the decomposition is the reason.

The end-to-end gains come from the whole loop. On the Requirements Met (D) metric, the paper attributes "a 13.43 percentage point gain entirely attributable to 3 rounds of evolutionary" iteration to evolution.[^d7] The run used "a population size of 4 and 3 rounds of evolutionary iterations," with the creator on gpt-4.1-nano and the judge on gpt-4o.[^d10][^d11][^d12]

## Limits

- The ablations do not isolate the decomposition. The two ablation sections are "Necessity of the Evolutionary Process" and "Importance of Semantic Feedback."[^d8] Removing the natural-language feedback lowered the MatPlotBench score from 59.85 to 54.30,[^d15] which is evidence about feedback in a selection loop, not about the list of sub-requirements. Whether a decomposed judge is steadier than a holistic one on the same items is asserted, not shown (my reading).
- Stability is not correctness. The authors name the failure the method must avoid: an evolutionary loop "could easily fall into chaos or evolve exploitative solutions that merely cater to LLM biases rather than being genuinely superior."[^d9] A checklist the judge can verify is also a target the creator can meet by satisfying the items without the quality the items were meant to stand for. The paper does not test this (my inference).
- The judge's accuracy is taken, not measured, in the parts of the text read here. The judge is a stronger model than the creator, chosen "to ensure evaluation accuracy."[^d10] A consistent judge with a wrong checklist is still wrong.
- The decomposer runs once, before the loop begins.[^d16] A criterion it omits is invisible to the judge, and the paper does not report how often the list misses a requirement a human would count (my inference).
- The domains are software requirements, instruction following and chart images, where a reader can write checkable items. The extension to open-ended output with no listable checks is the paper's claim, not a result shown here.

## Related

- [[llm-judge-score-instability]] — the run-to-run spread that decomposition is meant to damp; that note also records rubric ambiguity as a rival source of the same spread
- [[explicit-verifiable-criteria]] — the same separation on the prompt side: success conditions named as checkable items
- [[expert-report-derived-atomic-rubrics]] — atomic yes/no checklists used as a benchmark; there the list measures, here it is the judge's specification
- [[dependency-aware-checklist-scoring]] — a flat count of checklist items hides chain failures, which bears on the counting step here
- [[llm-judge-biases]] — systematic skews a judge carries whichever way its criteria are split

[^d1]: arxiv-2511-19489 — "an assertion describing a specific criterion that the final artifact"
[^d2]: arxiv-2511-19489 — "is a k-dimensional scoring vector"
[^d3]: arxiv-2511-19489 — "into a series of clear, specific, low-variance"
[^d4]: arxiv-2511-19489 — "converts the scoring vector v into a scalar fitness value"
[^d5]: arxiv-2511-19489 — "The single-rating absolute ICC reached 0.895"
[^d6]: arxiv-2511-19489 — "when the judge evaluates a solution highly, its scoring is more consistent"
[^d7]: arxiv-2511-19489 — "a 13.43 percentage point gain entirely attributable to 3 rounds of evolutionary"
[^d8]: arxiv-2511-19489 — "Importance of Semantic Feedback"
[^d9]: arxiv-2511-19489 — "solutions that merely cater to LLM biases rather than being genuinely superior"
[^d10]: arxiv-2511-19489 — "used the more powerful gpt-4o model"
[^d11]: arxiv-2511-19489 — "a population size of 4 and 3 rounds of evolutionary iterations"
[^d12]: arxiv-2511-19489 — "used the gpt-4.1-nano model"
[^d13]: arxiv-2511-19489 — "This step is the cornerstone of our framework"
[^d14]: arxiv-2511-19489 — "the judge can still provide stable and consistent scores"
[^d15]: arxiv-2511-19489 — "the evaluation score of MAS on MatPlotBench dropped from 59.85 to 54.30"
[^d16]: arxiv-2511-19489 — "The evolutionary loop officially begins after the Requirement Decomposer Agent transforms the user instruction"
