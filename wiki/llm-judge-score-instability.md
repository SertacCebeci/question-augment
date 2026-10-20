---
description: "LLM judges assigning numeric scores to identical inputs give different scores across repeated runs, even at temperature 0, and differ by model family and criterion, most on completeness."
aliases: ["score-based LLM judge inconsistency", "LLM-as-a-judge scoring stability", "same input different scores"]
sources: ["arxiv-2603-04417", "doi-10-35377-saucis-1835608", "doi-10-48550-arxiv-2603-13691", "arxiv-2512-20159", "arxiv-2512-09555", "arxiv-2601-04196", "arxiv-2511-19489"]
---
# LLM judge score instability

When an LLM is asked to grade an answer with a number (for example 0 to 1 for relevance), the number is one draw from a distribution, not a fixed property of the answer. Lau (2026) measured this for score-based judging, which earlier consistency work had not covered because it studied multiple-choice or selection tasks.[^c1]

## What was measured

Five models (GPT-4o, GPT-4o-mini, Gemini-2.5-Flash, Claude-Haiku-4.5, Claude-Sonnet-4.5) scored real question-answer pairs from an enterprise retrieval-augmented chatbot on three criteria: relevance, reliability (accuracy) and completeness. The same prompt was used throughout, each model ran at temperature 0 and 1, and the standard deviation over ten runs per question was the stability measure.[^c2]

## Findings

**Temperature 0 is not determinism.** Identical prompts at nominally deterministic sampling still produced different numeric ratings, and none of the evaluated models reached full determinism.[^c3]

**The criterion matters.** Completeness varied most, accuracy next, relevance least. The authors note completeness is the criterion that probes whether retrieval supplied enough information, so the least stable score is on the dimension a retrieval pipeline most needs.[^c4]

**Temperature helps unevenly.** Gemini's deviation dropped to zero or near zero at temperature 0; GPT models improved clearly; the Anthropic models improved only marginally, and Claude at temperature 0 was sometimes more variable on completeness than at temperature 1. Mean scores barely moved with temperature, so temperature changes stability, not the direction of scoring.[^c5]

**Cross-model disagreement is systematic.** Gemini was the most generous on completeness. On one item both Claude models gave near-zero relevance and accuracy because they read the answer as describing business tools rather than the assistant's own capabilities, while GPT and Gemini rated it positively. On another, Gemini gave completeness 1 and GPT gave 0.5. The models differ in what they take relevance, accuracy and completeness to mean, not only in strictness.[^c6]

**Instability is concentrated.** Mean deviation was low, but boxplots showed many outlier questions; Gemini at temperature 1 flipped between 1 and 0 across runs on a few questions while rating the rest consistently.[^c7]

**Format failures add a second noise source.** Outputs sometimes deviated from the required structure and broke regex parsing, producing invalid scores even when the underlying judgment was similar.[^c8]

**Procedural complexity and variance (code, 2025).** On code, the AXIOM paper compares judges by how many LLM calls one score needs, and finds that more calls means less stable scores. CodeVisionary, which gathers test and lint results with tools and then negotiates among several judges, "behaves notably more inconsistently" than the single-call metrics: each planning and tool step "introduces stochasticity, leading to high variance in" the final score.[^c27][^c28] The authors state the general rule as "Simpler metrics that require only a few LLM invocations exhibit high consistency."[^c29] The most stable metric, CodeJudge, follows "a JSON report template with manually-curated fault categories"[^c33] and "provides the highest Eq% of over 80 for Python".[^c30] Here consistency is the share of samples on which five runs give the same score. It is not agreement with humans, so it sits beside the points above, not in place of them.

**A vision-language quality predictor.** The same run-to-run noise appears when a vision-language model answers an image-quality prompt with a quality word rather than a number. Li et al. test each sample "five times per sample" in each of three sessions, and define the instability ratio as "the frequency of generating inconsistent or uncommon predictions".[^c34][^c35] On a mixed set of 3,000 authentic SPAQ and KONIQ images, the one-stage tuned baseline is compared with a two-stage tuning that first learns visual descriptions and then infers quality from them; the abstract reports that the approach "reduces prediction instability from 22.00% to 12.39%".[^c36] The lever here is the training of the model, not the decoding setting, so this bears on a different knob than the temperature results above (my inference). The limits are that it is one backbone measured by the authors' own definition, and the work reports no temperature variation for it, so whether the reduction holds under other decoding settings is not shown.

**A per-item spread reported beside the score.** Murugaraj et al. (2025) propose a calibration value for each case: the same metric is run under several (model, temperature) configurations, and the agreement is one minus the gap between the highest and the lowest score.[^c37] The authors say this "exposes the reliability of evaluation signals themselves", so a metric's output is marked robust or brittle case by case rather than averaged into one number.[^c38] The paper defines the value and does not test it: there is no check against human judgment, and no result showing that low-agreement cases are the ones a judge gets wrong (my reading).

## Consequence for using scores as gates

A threshold, routing or triage rule applied to a single judge score inherits this noise: the same item can land on either side depending on the run, the model or the family. This is the authors' stated concern, and the step from variance to misrouting is shown by examples rather than a measured misclassification rate (my reading).[^c9]

**Run-to-run agreement is not agreement with experts.** A Turkish short-answer study measured the same noise with a test-retest design. Each response was scored in "three independent, stateless inference runs (test-retest) at a temperature of 0.1", and agreement across the runs was summarised with Fleiss' kappa.[^c10] Models "exhibit high self-consistency under both zero-shot and one-shot conditions", with κ roughly 0.70 to 1.00.[^c11] Accuracy against expert scores was a separate measure, and on the binary item it ranged from 0.48 to 0.85 across models.[^c12] A stable scorer was therefore not shown to be a correct one. A single worked example also moved consistency unevenly. On the multi-level item, for LLaMA 3 70B and Gemini 2.0 Flash "the κ values of the same models decreased under one-shot conditions", and the authors tie this to the point that "models guided by a single example can increase decision variance".[^c13][^c14]

## Instability placed in the rubric

A different reading puts the noise in the grading criteria rather than in the judge. QuarkMedBench, which scores clinical answers with weighted per-query criteria, states that scoring instability "primarily originates from insufficient contextual information—specifically, semantic ambiguity within the rubrics".[^c15] Its diagnostic is a per-criterion measure: the authors track "scoring volatility for identical responses alongside inter-rubric score correlations" to find criteria to rewrite.[^c16] They also name redundancy and contradiction between criteria as a source of variance, which can "significantly inflate the variance of the aggregate score".[^c17] These are the authors' design reasons. The parts read report no before-and-after volatility figure for the rewriting, so whether the screen lowers judge variance is not shown (my reading). The two readings are compatible: the Gemini completeness flips above could come from either the judge or an ambiguous criterion, and the studies cited here do not separate the two (my inference).

**Score level sets the spread.** In a sensitivity analysis of a judge scoring evolved chart images, the spread depends on the score itself: "when the judge evaluates a solution highly, its scoring is more consistent," and "Conversely, for lower-scoring solutions, its scores are more volatile."[^c39][^c41] The authors read this as the merits of a good output being "clear and easy to agree upon", while poor outputs have flaws that vary.[^c40] So a judge can look stable on the top of the range and be noisy on the rest, which is where a selection step must separate candidates (my inference). The result is for one task and one judge model, and it measures the judge's own consistency, not agreement with humans. The same paper's decomposed-checklist judge is treated in [[decomposed-requirement-judging]].

## Limits

- One fixed prompt, no prompt-engineering or chain-of-thought variants; the authors name this as untested.
- Only proprietary models, only temperatures 0 and 1; top-p, top-k and seed were not varied.
- The dataset is private, so the result cannot be reproduced or benchmarked; ten runs per item is a small sample for tail behaviour.
- No human baseline: stability was not related to agreement with human judgment, so a stable judge is not shown to be a correct one.
- The suggestion that non-determinism reflects architectural or decoding differences is the authors' speculation, not tested.
- The code-side consistency test uses five runs per metric,[^c31] on code in three languages. The agentic metric's weaker Java results are attributed by its authors to environment construction, since the approach "is more likely to fail for Java than for Python and C++".[^c32] The comparison does not separate depth of procedure from the tool environment, so the complexity effect is not isolated. (my inference)

## Related

- [[llm-judge-biases]] — systematic skews of a judge; this note is the random, run-to-run counterpart
- [[cross-provider-judge-ensemble]] — combining families is one response to family-specific interpretations
- [[multi-seed-bias-score-averaging]] — the same remedy shape: one pass is unreliable, average over runs
- [[dual-judge-completeness-recall]] — another completeness judging setup whose scores would inherit this noise

[^c1]: arxiv-2603-04417 — "None of the studies address the instability of a score-based judging system, where the LLM is required to generate a numerical score to a given response."
[^c2]: arxiv-2603-04417 — "Figures 1 and 2 illustrate the standard deviation of scores across ten runs for each model at temperature = 1 and temperature = 0"
[^c3]: arxiv-2603-04417 — "Even at temperature 0, none of the evaluated models achieve full determinism"
[^c4]: arxiv-2603-04417 — "Models rate more consistently in relevance and accuracy than in completeness"
[^c5]: arxiv-2603-04417 — "temperature affects stability rather than the direction or tendency of scoring"
[^c6]: arxiv-2603-04417 — "model families differ not only in strictness or generosity but also in their interpretation of what constitutes relevance, accuracy, and completeness"
[^c7]: arxiv-2603-04417 — "Gemini rate the question either 1 or 0, across multiple runs, hence the high inconsistency."
[^c8]: arxiv-2603-04417 — "relying solely on structural assumptions or simple pattern matching"
[^c9]: arxiv-2603-04417 — "a single question could be classified differently depending on the model used"
[^c10]: doi-10-35377-saucis-1835608 — "the model performed three independent, stateless inference runs (test-retest) at a temperature of 0.1"
[^c11]: doi-10-35377-saucis-1835608 — "models exhibit high self-consistency under both zero-shot and one-shot conditions"
[^c12]: doi-10-35377-saucis-1835608 — "Accuracy rates for Q1 range from 0.48 to 0.85."
[^c13]: doi-10-35377-saucis-1835608 — "the κ values of the same models decreased under one-shot conditions"
[^c14]: doi-10-35377-saucis-1835608 — "models guided by a single example can increase decision variance"
[^c15]: doi-10-48550-arxiv-2603-13691 — "primarily originates from insufficient contextual information—specifically, semantic ambiguity within the rubrics"
[^c16]: doi-10-48550-arxiv-2603-13691 — "volatility for identical responses alongside inter-rubric score correlations to isolate and rectify problematic"
[^c17]: doi-10-48550-arxiv-2603-13691 — "among criteria significantly inflate the variance of the aggregate score"
[^c27]: arxiv-2512-20159 — "behaves notably more inconsistently"
[^c28]: arxiv-2512-20159 — "introduces stochasticity, leading to high variance in"
[^c29]: arxiv-2512-20159 — "Simpler metrics that require only a few LLM invocations exhibit high consistency"
[^c30]: arxiv-2512-20159 — "provides the highest Eq% of over 80 for Python"
[^c31]: arxiv-2512-20159 — "five metric runs generate the same score"
[^c32]: arxiv-2512-20159 — "is more likely to fail for Java than for Python and C++"
[^c33]: arxiv-2512-20159 — "a JSON report template with manually-curated fault categories"
[^c34]: arxiv-2512-09555 — "quality predictions are tested five times per sample to assess stability"
[^c35]: arxiv-2512-09555 — "we define the instability ratio as the frequency of generating inconsistent or uncommon predictions"
[^c36]: arxiv-2512-09555 — "reduces prediction instability from 22.00% to 12.39%"
[^c37]: arxiv-2601-04196 — "quantifies agreement across multiple judge configurations"
[^c38]: arxiv-2601-04196 — "exposes the reliability of evaluation signals themselves"
[^c39]: arxiv-2511-19489 — "when the judge evaluates a solution highly, its scoring is more consistent"
[^c40]: arxiv-2511-19489 — "the merits of a high-quality output are clear and easy to agree upon"
[^c41]: arxiv-2511-19489 — "Conversely, for lower-scoring solutions, its scores are more volatile"
