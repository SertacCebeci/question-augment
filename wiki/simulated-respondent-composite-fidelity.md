---
description: "LLM respondents track item-level patterns but not a test's subscale-weighted composite, so item agreement alone does not validate a simulated scale."
aliases: ["composite fidelity of simulated respondents", "scale-level validity of simulated respondents", "test-level fidelity of LLM survey responses"]
sources: ["doi-10-48550-arxiv-2505-21997"]
---
# Simulated-respondent composite fidelity

Agreement between a simulated respondent and a human is usually checked item by item: the simulated answer to item i is set against the human answer to item i. A scale, however, is scored by combining items, and a simulator can fit the items while failing the combination. The check that matters for the scale is therefore a different one from the check on items.

The study that shows this is a simulation of the Behavioral Regulations in Exercise Questionnaire (BREQ), a 15-item instrument whose items form four subscales.[^k1] The relative autonomy index (RAI) is a weighted sum of those four subscale scores, so it is one total per person that depends on how the items are grouped and weighted.[^k2] At the item level the agreement was real: the average Pearson correlations between chatbot responses and human responses "show that there are medium to high relationships."[^k3] At the test level the picture changes. The authors write that "LLMs struggle to grasp the overall psychometric structure of the test when item scores are aggregated and weighted by subscales,"[^k4] and summarise the contrast as "while they can mimic individual item patterns, LLMs have difficulty reproducing the underlying psychometric relationships of the whole test."[^k5]

The paper's explanation is that the RAI calculation needs an understanding of how the study variables relate, an understanding it takes to be "not included in the training of LLM chatbots."[^k6] That is the authors' reading. The study does not test it.

Adding personal content did not close the gap at the composite level. Only Claude, with the prompts that carried person-level content (interview, demographics, or both), showed higher alignment with humans on the RAI than the baseline prompt. For the other two chatbots, the authors found that "more personal information in the prompts (e.g., interview data and demographic information) may not necessarily improve the alignment between LLMs and humans towards the RAI."[^k7] So the interview that helped item-level agreement in the same study (see [[narrative-over-demographic-persona-conditioning]]) did not carry over to the total for two of the three models.

What this means for asking and answering: a simulator that passes an item-level check has shown that it reproduces the answers, not that it reproduces the scale. A composite built from simulated answers can be wrong even when every item looks right, because the error sits in the weights and groupings, which an item-by-item comparison never reads. The same item-level look also hides unevenness. The item RMSEs were relatively higher for items 6, 7 and 11, which "contain relatively negative emotional words," so averaging item agreement across a scale can mask the items the simulator gets wrong.[^k8]

## Limits

- One study, one instrument, 19 respondents, three chatbots at one point in time. The composite comparison rests on one total per person and on the four-subscale weighting the paper uses. Other scales with different groupings were not tested.
- The paper reports test-level RMSE on totals. It does not split the composite error into a mean part and a spread part, so it cannot say whether the failure comes from the level of the scores, their spread, or the weights. (My reading; the paper does not separate them.)
- "Psychometric structure" in the paper means the RAI relation among subscales. No factor analysis, reliability estimate or measurement-invariance check is reported, so the claim does not extend to those.
- The authors' explanation (missing training on the RAI definitions) is untested. A simulator with more explicit scoring rules might do better on the composite; this was not tried.
- Whether composite misfit also biases a parameter estimated from simulated respondents is not tested here. See [[simulated-respondent-icc]] for the item-parameter case, where the same check would apply. (My inference.)

## Related

- [[simulated-respondent-variance-deficit]] — the same study's spread result: the simulator matches item means and misses spread; the composite result adds that it can also miss the scale's structure
- [[narrative-over-demographic-persona-conditioning]] — the same prompts judged on item agreement, where interview content helped more clearly than demographics
- [[simulated-respondent-icc]] — uses a simulated respondent to estimate item parameters, where a composite-level check would be a further test (my inference)

[^k1]: doi-10-48550-arxiv-2505-21997 — "The BREQ contains four subscales"
[^k2]: doi-10-48550-arxiv-2505-21997 — "the relative autonomy index of person p, which can be calculated as the weighted sum of four subscale scores"
[^k3]: doi-10-48550-arxiv-2505-21997 — "there are medium to high relationships"
[^k4]: doi-10-48550-arxiv-2505-21997 — "struggle to grasp the overall psychometric structure of the test"
[^k5]: doi-10-48550-arxiv-2505-21997 — "while they can mimic individual item patterns, LLMs have difficulty reproducing the underlying psychometric relationships of the whole test"
[^k6]: doi-10-48550-arxiv-2505-21997 — "which is not included in the training of LLM chatbots"
[^k7]: doi-10-48550-arxiv-2505-21997 — "may not necessarily improve the alignment between LLMs and humans towards the RAI"
[^k8]: doi-10-48550-arxiv-2505-21997 — "contain relatively negative emotional words"
