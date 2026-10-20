---
description: "In repeated-task surveys, satisficing shows up as attenuated predictive power of the attributes over task number; with 30 conjoint tasks on opt-in samples the attenuation was small and early."
aliases: ["survey satisficing", "survey fatigue", "response quality degradation over tasks"]
sources: ["bansak-2018"]
---
# Survey satisficing and the number of tasks

Survey satisficing is respondents adapting to onerous tasks with cognitive shortcuts that degrade response quality; satisficers rush, skip instructions, choose options by placement and use other effort-saving heuristics.[^c1] It is expected to grow with the total length of a questionnaire: later questions get less time and more uniform answers.[^c2] The worry is sharper when the same task is repeated, since fatigue may set in faster.[^c3]

## How it was measured

Bansak et al. (2018) had respondents complete 30 paired-profile conjoint tasks (presidential candidates), with two core attributes (education, party) always shown and 2 to 18 other attributes randomly drawn per respondent. Five Mechanical Turk surveys (4,921 respondents) and one Survey Sampling International survey (1,613) were run.[^c4] The idea: satisficing makes respondents attend less, which attenuates the predictive power of the core attributes. Two metrics were tracked task by task: the average marginal component effect (AMCE) of each core attribute, and the R-squared of responses regressed on the core attributes. Because R-squared is a function of the AMCEs under full randomization, its change across tasks is read as change in overall satisficing.[^c5]

## What was found

The first-task AMCEs were 0.186 (education) and 0.263 (party). They dropped slightly at task 2 (0.152, 0.238) and then stayed stable; at task 30 they were 0.140 and 0.233.[^c6] Partial R-squared went from about 0.104 (task 1) to 0.079 (task 2) and 0.075 at task 30.[^c7] The SSI sample replicated this.[^c8] The authors conclude that within 30 tasks satisficing should not dictate the number of tasks; this should be set by survey length, cost and power.[^c9] The one visible degradation is therefore an early drop, between the first and second task, not a steady decline. (That reading of the early drop as a warm-up or learning effect is my inference; the paper does not explain it.)

## Limits

- The test covers only up to 30 tasks, an easy, familiar comparison (presidential candidates) and experienced opt-in respondents. The authors say results may differ for people inexperienced with computer surveys, with weaker incentives, or for complex subject matter such as policy proposals.[^c10]
- The paper explicitly gives no optimal number of tasks, and notes conjoint designs have breaking points, only beyond common practice for such samples.[^c11]
- The indicator is attenuation of core-attribute effects; other forms of satisficing (straightlining, speeding) are not separately measured here. Attrition was negligible on MT, so selective dropout is unexamined as a mask.
- Whether the finding transfers to open-ended or non-conjoint question sequences, or to LLM respondents, is not tested.

## Related

- [[bounded-rationality]] — satisficing in the Simon sense; survey satisficing borrows the idea of settling for good enough effort under cognitive cost, though the paper restricts its use of the term to the survey sense.[^c12]

[^c1]: bansak-2018 — "Satisficing respondents are more likely to rush through surveys, ignore or skip"
[^c2]: bansak-2018 — "respondents take less time and provide more uniform answers"
[^c3]: bansak-2018 — "fatigue may set in more rapidly when performing the same task repeatedly"
[^c4]: bansak-2018 — "4,921 respondents we recruited via MT"
[^c5]: bansak-2018 — "any changes in the R 2 across tasks can be attributed to changes in satisficing"
[^c6]: bansak-2018 — "Even at the 30th task, the estimated AMCEs barely differ from those for the second task (0.140 and 0.233"
[^c7]: bansak-2018 — "The partial R 2 for the two core attributes is"
[^c8]: bansak-2018 — "These findings are replicated in our"
[^c9]: bansak-2018 — "satisficing is not a serious concern that should dictate the number of tasks"
[^c10]: bansak-2018 — "Survey fatigue may be more pronounced and/or set in more quickly in a more"
[^c11]: bansak-2018 — "While the results do not point to an optimal number of tasks"
[^c12]: bansak-2018 — "Here, we use the term exclusively as an"
