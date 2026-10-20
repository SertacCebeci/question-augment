---
description: "Expert personas given to a model did not reliably raise accuracy on hard multiple-choice items; most persona conditions matched the no-persona baseline, and the few changes were mostly down."
aliases: ["persona prompting null", "expert persona accuracy null", "no-benefit expert persona"]
sources: ["arxiv-2512-05858"]
---
# Expert persona accuracy null

A persona is a line that tells a model who it is, such as "You are a world-class expert in physics." The question this measurement asks is narrow: does such a line make the answer to a hard factual question more often correct? In the Wharton "Prompting Science" study, six models were run on 198 GPQA Diamond items and a 300-item MMLU-Pro subset (engineering, law and chemistry). "We collected 25 independent responses per question for each model-prompt condition," and the sampling temperature was set at 1.0 to approximate ordinary use.[^c1] [^c2] [^c3] The primary measure is the fraction of questions answered correctly, averaged over the 25 runs per question.

The headline result is that personas did little. "Across both benchmarks, persona prompts usually had little to no effect on factual accuracy."[^c4] Most persona conditions were statistically indistinguishable from the no-persona baseline. Matching the expert to the question did not change this: a physics expert on a physics item "had no significant impact on" performance, with one exception, Gemini 2.0 Flash.[^c5] Mismatching it did not reliably help either: an off-domain expert, such as a physics expert on a law question, "resulted in marginal differences."[^c6] The authors conclude that "assigning an expert persona is not a reliable way to improve accuracy."[^c7]

Where a persona did move accuracy, the movement was more often down: "they were more often negative than positive."[^c8] Domain-tailored personas, taken as a group, "do not generally improve performance."[^c9] The exception that the authors could not dismiss is Gemini 2.0 Flash on MMLU-Pro, where "the five expert personas yielded modest positive differences relative to" the baseline.[^c10] The authors add that "The Gemini 2.0 Flash improvements may be outliers," because a sibling model, Gemini 2.5 Flash, showed no significant positive differences.[^c11]

The study also says what it did not measure. Personas "may change what factors the AI focuses on and how it approaches reasoning about a problem."[^c12] Naming a role may also serve as a cue for the asker: a persona "may serve a dual function as a prompting aid for users."[^c13] The accuracy null does not decide whether either of these is worth having; it says only that the persona line does not add correct answers on these items.

## Limits

- The test covers six models, two benchmarks and a few subdomains; the authors concede "testing only a subset of available models" and a narrow set of personas.[^c14]
- The items are academic multiple-choice questions. The authors warn that these "may not reflect all real-world use cases," and the format (a fixed one-line answer) may itself suppress the reasoning a persona is meant to activate. The rebuttal in [[expert-persona-confidence-amplification]] makes this format argument at length.
- The null is a mean over runs. The authors report that with correctness thresholds "Results are overall comparable for both benchmarks," and that the effects "tend to be more pronounced at the higher threshold levels."[^c15] The threshold tables sit in the appendix and were not checked here, so the strict-threshold reading is the authors' and not mine.
- Accuracy is the only outcome. The paper does not measure tone, calibration, or whether a persona changes which considerations a model raises. A null on correct answers is silent on those.
- The Gemini 2.0 Flash gain is not explained. Whether it is a model-specific quirk or a real but narrow effect is left open by the authors' own wording.

## Related

- [[expert-persona-confidence-amplification]] — a rebuttal to this study's null; it argues the design could not have detected a persona effect, and proposes a confidence mechanism
- [[low-knowledge-persona-accuracy-cost]] — the negative-capability personas, measured in the same runs, where the cost is larger than the expert gain
- [[narrow-role-refusal]] — a failure of the off-domain expert condition that the accuracy null partly hides, namely refusal rather than wrong answers

[^c1]: arxiv-2512-05858 — "The GPQA Diamond set comprises 198 multiple-choice PhD-level questions across biology, physics, and"
[^c2]: arxiv-2512-05858 — "We collected 25 independent responses per question for each model-prompt condition"
[^c3]: arxiv-2512-05858 — "We used a relatively high sampling temperature (1.0)"
[^c4]: arxiv-2512-05858 — "persona prompts usually had little to no effect on factual accuracy"
[^c5]: arxiv-2512-05858 — "had no significant impact on"
[^c6]: arxiv-2512-05858 — "not matched to the problem type (law problems) resulted in"
[^c7]: arxiv-2512-05858 — "assigning an expert persona is not a reliable way to improve accuracy"
[^c8]: arxiv-2512-05858 — "they were more often negative than positive"
[^c9]: arxiv-2512-05858 — "domain-tailored personas do not generally improve performance"
[^c10]: arxiv-2512-05858 — "the five expert personas yielded modest positive differences relative to"
[^c11]: arxiv-2512-05858 — "The Gemini 2.0 Flash improvements may be outliers"
[^c12]: arxiv-2512-05858 — "personas may change what factors the AI focuses on and how it"
[^c13]: arxiv-2512-05858 — "may serve a dual function as a prompting aid for users"
[^c14]: arxiv-2512-05858 — "testing only a subset of available models"
[^c15]: arxiv-2512-05858 — "tend to be more pronounced at the higher threshold levels"
