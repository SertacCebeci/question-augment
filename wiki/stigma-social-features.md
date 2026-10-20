---
description: "Six social features rated per stigma (aesthetics, concealability, course, disruptiveness, origin, peril) track how often LLMs give biased yes/no advice about 93 stigmatized groups."
aliases: ["social features of stigma", "stigma dimensions", "stigma clusters", "stigma feature taxonomy"]
sources: ["arxiv-2512-19238"]
---
# Stigma social features

A stigma is "an attribute or characteristic that is devalued in a particular social context".[^c1] Psychology does not treat each stigma as a separate case. It describes stigmas along six shared features, each a graded rating rather than a yes or no: aesthetics (the potential to evoke disgust), concealability, course, disruptiveness, origin, and peril.[^c2] Two of the definitions as the paper gives them: course is "the extent to which a stigma persists over time", and peril is "the extent to which a stigma poses a personal threat or potential for contagion".[^c3]

Pachankis et al. used human ratings of these features across 93 stigmas to cluster the stigmas, and the clusters are a second layer of the same idea.[^c4] Five clusters result: Awkward, Threatening, Sociodemographic, Innocuous Persistent and Unappealing Persistent. A Threatening stigma is one "perceived as concealable, aesthetically unappealing, highly onset-controllable, and perilous"; a Sociodemographic one is "perceived highly visible and persistent with low controllability or peril".[^c5]

**How the features reach an answer.** The point of the feature view is that a stigma's position on the features may predict how a language model treats a person who has it. Gueorguieva and Caliskan put this to a test. They ran three instruction-tuned models on SocialStigmaQA, a benchmark of short social scenarios (for example an interview or a hiring decision) in which each prompt names a stigmatized identity and asks for a yes or no. Across the models, the cluster of the stigma changed the share of biased answers strongly: "models exhibit the least amount of bias towards the cluster of sociodemographic stigmas (11%)", and the most toward the perceived-as-threatening cluster, about 60%.[^c6]

Within the feature analysis, three features carried an effect on the per-stigma bias rate. Human-rated peril had the largest effect: "as human ratings of peril increase, so do biased outputs".[^c7] Human-rated course worked in the other direction, so that stigmas judged temporary drew more biased answers: "biased outputs increase moderately".[^c8] The models' own rating of concealability also predicted bias: "LLM ratings of concealability increase, so do biased outputs".[^c9] The paper reads this as evidence that the features carry information about social bias that the stigma label alone does not, but it does not test the label against the features in one model.

The models' ratings differ systematically from human ones. Asked about a stigma such as using a wheelchair, the models "on average rate it much lower and more easily concealed" than humans do.[^c10] The paper found moderate to strong agreement between models and humans on aesthetics, and reads this as models reproducing social bias through the revulsion a stigma provokes, without being able to reason about its physical signs.[^c11] This is the authors' posit, not something they tested.

For the question side of the wiki the lesson is narrow. Who or what a question names, and which features that thing has, is part of the input the answerer's bias responds to. A stigma's features are a material variable of the prompt, not a background fact about the group.

## Limits

- The 93 stigmas are US-centric, and the paper says so: "our study focuses on US-centric stigmas".[^c12] Culturally specific stigmas are not tested, and the features may differ across cultures.
- The clusters and feature ratings come from human ratings. The paper calls the clusters "clusters that emerge from human participants ratings of features", so the taxonomy is an empirical grouping, not a closed list of kinds.[^c13]
- The models' feature ratings are only weakly to moderately aligned with human ratings, and for concealability the sign flips: "All models have negative correlation of human to model concealibility ratings".[^c14] A feature that the model rates is not the feature humans rate.
- The analysis is correlational across stigmas. Nothing intervenes on a feature and watches bias move. My inference: the effect sizes are modest, and the features and clusters overlap, so peril and the Threatening cluster are partly the same signal.
- Bias is measured as an explicit yes or no, and an answer that is not one is counted as unbiased. The measured bias therefore depends on the format; see [[answer-format-dependent-bias-measurement]].
- The mechanism linking misaligned feature ratings to biased answers is not established: "Future work is necessary to determine how (mis)alignment between humans and LLMs may lead to bias".[^c15]

## Related

- [[guardrail-bias-intent-blindness]] — the same benchmark's prompts, seen from the input side of the model: whether a guardrail flags them
- [[qa-benchmark-demographic-skew]] — skew in which groups benchmarks name; this note is about which features of the named group predict the answer
- [[answer-format-dependent-bias-measurement]] — the bias figure itself changes with the answer format

[^c1]: arxiv-2512-19238 — "is devalued in a particular social context"
[^c2]: arxiv-2512-19238 — "aesthetics (the potential to evoke a disgust reaction), concealability (the extent to which a stigma is visible to others)"
[^c3]: arxiv-2512-19238 — "course (the extent to which a stigma persists over time)"
[^c4]: arxiv-2512-19238 — "the human ratings of features of stigmas to cluster five different types of stigmas"
[^c5]: arxiv-2512-19238 — "Perceived highly visible and persistent with low controllability or peril"
[^c6]: arxiv-2512-19238 — "models exhibit the least amount of bias towards the cluster of sociodemographic stigmas (11%)"
[^c7]: arxiv-2512-19238 — "as human ratings of peril increase, so do biased outputs"
[^c8]: arxiv-2512-19238 — "biased outputs increase moderately"
[^c9]: arxiv-2512-19238 — "LLM ratings of concealability increase, so do biased outputs"
[^c10]: arxiv-2512-19238 — "on average rate it much lower and more easily concealed"
[^c11]: arxiv-2512-19238 — "may replicate social biases based on the revulsion of a stigma"
[^c12]: arxiv-2512-19238 — "our study focuses on US-centric stigmas"
[^c13]: arxiv-2512-19238 — "are clusters that emerge from human participants ratings of features"
[^c14]: arxiv-2512-19238 — "All models have negative correlation of human to model"
[^c15]: arxiv-2512-19238 — "Future work is necessary to determine"
