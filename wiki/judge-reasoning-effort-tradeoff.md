---
description: "For LLM judges of rubric criteria, thinking tokens raise agreement with humans on multi-step criteria but cost orders of magnitude more and may raise bias toward particular generators."
aliases: ["judge thinking budget", "reasoning effort for LLM judges", "judge output budget"]
sources: ["doi-10-48550-arxiv-2510-18941", "arxiv-2512-01232"]
---
# Judge reasoning effort trade-off

When a language model judges whether a response fulfils one rubric criterion, its thinking budget is a setting that can be chosen apart from which model is used. The paper's comparison runs the two extremes. Non-reasoning judges were allowed one output token, Yes or No, while reasoning judges could use "up to 32,000 tokens".[^c1] That formulation sets the cost: non-reasoning judges are "approximately two to three orders of magnitude" cheaper in practice, since the paper's setup gives them no trace to produce.[^c2]

Thinking helps, but by a varying amount. Enabling it on the same model raised agreement with humans by "0.7% for Claude-Sonnet-4 to 4.8% for Gemini-2.5-Flash".[^c3] In the GPT-5 series, moving from minimal to low reasoning raised performance by 4.4% to 18.6%, yet "the gain between low, medium and high reasoning effort is not consistent".[^c4] So more effort is not a monotone improvement, and the best setting differs by model.

A later study of Gherkin test-coverage judging, which scores coverage from 0 to 100 against expert percentages, finds the dial turns in opposite directions by model family. "Reasoning effort is model-family dependent."[^c14] Within GPT-5, "higher reasoning effort consistently improves accuracy at the cost of increased inference expenditure."[^c15] For open-weight models the reverse holds: "where increased reasoning effort degrades both accuracy and reliability while increasing costs."[^c16] Reliability here means the share of judge outputs that parse on the first attempt, which is why the same effort setting also changes what a usable judgement costs; see [[retry-adjusted-cost]]. For one of the open-weight judges the high setting was the least reliable of all, with "The high reasoning configuration degrades accuracy" and a first-attempt completion rate of 85.4%.[^c17]

Where the extra effort pays is also specific. The paper finds the largest gains in Physics, Chemistry and style criteria, which "often entail multi-step reasoning to ensure that the response fulfills the criteria, instead of a simple answer-matching."[^c5] A criterion that asks for a stock-price rounding or a chemical quantity cannot be checked by matching a phrase; the judge has to carry out the check.

The same extra effort is linked to bias. The paper reports that "increasing reasoning effort generally increases alignment with human annotations but also increases bias to specific models", and offers greater self-enhancement with more thinking as a possible explanation.[^c6] The bias is measured by the spread described in [[cross-generator-judge-bias-index]]. Self-enhancement is discussed in [[llm-judge-biases]], where the evidence is mixed. The paper reports the bias rising with effort "consistently across all models (except for o3)", which is its observation and not a mechanism it tests.

The authors act on this trade-off. Their final judge, GPT-OSS-120B, was run at high effort for Physics, Chemistry and style criteria and at low effort for the rest: "the high reasoning effort version does better on Physics, Chemistry and Style-related criteria, while the low reasoning effort version does better on others."[^c7] They describe the switch as "alter[ing] the reasoning effort based on the domain/criterion type encountered", chosen "to balance quality and cost."[^c8] The result, in their words, "performs as well as the best proprietary model" at 78.2% overall, and the benchmark run costs $0.70 against $1320 for PaperBench's judge.[^c9][^c10]

Read together, the thinking budget is a dial with three readings: agreement with humans on criteria that need multi-step checks, spread across generators, and cost. The paper's choice of judge by overall score, Macro-F1 minus the bias index, prices the second. The cost reading is the one the paper stresses. The switch by criterion type is a way of spending effort where the criteria need it, which is my reading of the authors' stated aim.

## Limits

- Each judge was run once. The authors say they "only run with each judge once to save cost".[^c11]
- The per-domain effort rule was chosen with the same benchmark's labels. The paper states that experiments use "only half of the dataset as we plan for this to be the public dataset".[^c12] The text read does not show the rule being checked on the private half.
- Cost is an upper bound: it multiplies "the number of input and output tokens" by public prices and excludes caching.[^c13] Caching "will reduce the cost to as low as one-tenth as stated cost for judges whose costs are dominated by input tokens."[^c13]
- The non-reasoning arm is the one-token formulation only. The comparison does not show what a short written justification, or an intermediate budget, would have done for a non-reasoning judge.
- The bias rise with effort is observed across models except o3, and the explanation is the paper's guess. The mechanism is not measured.
- The results are on one benchmark of binary, expert-written criteria. Whether the same trade-off holds for other rubric sets, or for graded rather than binary criteria, is not tested.
- The family result comes from a different setting: a coverage score, not a yes/no criterion, judged on "on 100 expert-annotated scripts" over five runs.[^c18] The two papers agree on non-monotone effort but not on direction within one family; the text read gives no mechanism for the open-weight decline, and the sign of the effect is not shown to carry over to other families.

## Related

- [[cross-generator-judge-bias-index]] — the measure in which the effort-bias link appears
- [[llm-judge-biases]] — position, verbosity and self-enhancement; the effort result bears on the last
- [[judge-then-solve]] — another lever on judge reasoning weakness: solve first, then judge
- [[reasoning-judge-adversarial-policy]] — the same thinking dial seen from RL, where a reasoning judge can be exploited by a policy
- [[tokens-per-correctness]] — the same cost-against-correctness framing applied to search effort
- [[retry-adjusted-cost]] — the same paper's reliability measure; effort can change how often a judge's output parses, and so the price of a usable judgement

[^c1]: doi-10-48550-arxiv-2510-18941 — "up to 32,000 tokens for reasoning LLMs"
[^c2]: doi-10-48550-arxiv-2510-18941 — "approximately two to three orders of magnitude in practice"
[^c3]: doi-10-48550-arxiv-2510-18941 — "0.7% for Claude-Sonnet-4 to 4.8% for Gemini-2.5-Flash"
[^c4]: doi-10-48550-arxiv-2510-18941 — "the gain between low, medium and high reasoning effort is not consistent"
[^c5]: doi-10-48550-arxiv-2510-18941 — "since they often entail multi-step reasoning to ensure that the response fulfills the criteria"
[^c6]: doi-10-48550-arxiv-2510-18941 — "increasing reasoning effort generally increases alignment with human annotations but also increases bias to specific models"
[^c7]: doi-10-48550-arxiv-2510-18941 — "the high reasoning effort version does better on Physics, Chemistry and Style-related criteria, while the low reasoning effort version does better on others"
[^c8]: doi-10-48550-arxiv-2510-18941 — "we decided to alter the reasoning effort based on the domain/criterion type encountered"
[^c9]: doi-10-48550-arxiv-2510-18941 — "The resulting judge performs as well as the best proprietary model"
[^c10]: doi-10-48550-arxiv-2510-18941 — "ProfBench-Judge only costs $0.70 vs. $1320 for PaperBench JudgeEval"
[^c11]: doi-10-48550-arxiv-2510-18941 — "therefore we only run with each judge once to save cost"
[^c12]: doi-10-48550-arxiv-2510-18941 — "For experimental purpose, we only use half of the dataset as we plan for this to be the public dataset"
[^c13]: doi-10-48550-arxiv-2510-18941 — "caching alone will reduce the cost to as low as one-tenth as stated cost for judges whose costs are dominated by input tokens"
[^c14]: arxiv-2512-01232 — "Reasoning effort is model-family dependent"
[^c15]: arxiv-2512-01232 — "higher reasoning effort consistently improves accuracy at the cost of increased inference expenditure"
[^c16]: arxiv-2512-01232 — "where increased reasoning effort degrades both accuracy and reliability while increasing costs"
[^c17]: arxiv-2512-01232 — "The high reasoning configuration degrades accuracy"
[^c18]: arxiv-2512-01232 — "on 100 expert-annotated scripts"
