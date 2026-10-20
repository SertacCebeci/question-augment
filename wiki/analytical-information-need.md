---
description: "Analytical needs ask for a conclusion built from several pieces of evidence, leave scope, baseline and criteria implicit, and come as descriptive, predictive or prescriptive."
aliases: ["analytical information need", "analytical needs", "analytical queries"]
sources: ["openalex-org-w7128864259"]
---
# Analytical information need

An analytical information need is a request whose answer is a conclusion reached by reasoning over several pieces of evidence, not the retrieval of one fact. The authors set it against naive information finding in one sentence: "Analytical information needs refer to user queries that require systematic reasoning" over multiple pieces of evidence.[^a1] Such queries "rarely correspond to a single retrievable" fact. They "require decomposition into multiple interdependent subquestions," such as identifying entities, collecting longitudinal evidence, performing comparisons, or estimating effects.[^a2][^a3]

The work sorts these needs by analytical depth. It follows a taxonomy "widely used in data" analytics and statistics, and yields three kinds.[^a4]

- **Descriptive.** The need is about "understanding and summarizing what has happened, often" through aggregation, comparison and pattern identification, such as counting, ranking or temporal trends.[^a5]
- **Predictive.** "Predictive analytics aims to predict future outcomes or latent relationships based on observed" evidence. The asker wants a causal or extrapolated claim, and the answerer "needs to reason about uncertainty, temporal dependency, and" confounding.[^a6][^a7]
- **Prescriptive.** "Prescriptive analytics represents the most decision-oriented form of analytical reasoning." It evaluates alternative actions under constraints, and it needs "but also explicit modeling of objectives," not only accurate evidence.[^a8][^a9] The authors note that these queries "often build upon descriptive and predictive" analyses.[^a10]

## What the asker leaves out

The distinctive feature the work stresses is the gap between the wording of the question and the need behind it. "Users often omit temporal scopes, comparison baselines, evaluation criteria, or even the precise analytical goal."[^a11] Their example, "Has policy A improved urban air quality?", "implicitly assumes a time window, a definition of improvement, and one or more baseline conditions."[^a12] On the answerer's side, the consequence is that "systems must reconstruct latent analytical intent rather than merely" read the surface of the query.[^a13]

The unstated parts matter because the sub-tasks depend on one another. The paper says "decomposition can propagate through the analytical pipeline" when an early omission is carried forward.[^a14] A missing baseline is therefore not a small gap in the answer; it changes which evidence is looked for at every later step. My inference from this, not a claim of the paper: the three classes ask for different kinds of unstated parts. A descriptive need mostly needs its scope, a predictive need needs a comparison baseline, and a prescriptive need needs its criteria.

## Limits

- The typology is imported from data analytics and statistics. What survives the transfer is the ordering by depth, from summary to inference to choice. What does not obviously survive is the claim that the classes are separable in real questions. The text gives examples for each class and no coding scheme, no labelled set of questions, and no frequency of each class.
- The boundaries are soft, and the work says so only in passing: prescriptive queries "often build upon descriptive and predictive" analyses. A single question can carry all three.
- The claim that analytical needs are "prevalent across various domains including law, finance, science" is asserted in the introduction and not measured here.
- The work does not show that askers recognise which class their question belongs to, or that a system can classify a question into one before answering it.
- The concept is defined inside a proposal for a search paradigm. Nothing here reports that people or systems answer analytical needs better when they are typed this way.

## Related

- [[levels-of-information-need]] — Taylor's ladder describes how the asker's need is formed in words; this note classifies the need by the analysis it demands, a different axis.
- [[information-need-reification]] — one route to making the unstated scope, baseline and criteria explicit before answering.
- [[demand-typed-query-classification]] — sorts queries by the operations their answer needs in order to choose a pipeline; the typology here sorts by analytical depth, and the two overlap only partly.
- [[analytical-search]] — the search paradigm the work proposes for needs of this kind.

[^a1]: openalex-org-w7128864259 — "Analytical information needs refer to user queries that require systematic reasoning"
[^a2]: openalex-org-w7128864259 — "analytical queries rarely correspond to a single retrievable"
[^a3]: openalex-org-w7128864259 — "fact and require decomposition into multiple interdependent subquestions"
[^a4]: openalex-org-w7128864259 — "Following the taxonomy widely used in data"
[^a5]: openalex-org-w7128864259 — "understanding and summarizing what has happened, often"
[^a6]: openalex-org-w7128864259 — "Predictive analytics aims to predict future outcomes or latent relationships based on observed"
[^a7]: openalex-org-w7128864259 — "needs to reason about uncertainty, temporal dependency, and"
[^a8]: openalex-org-w7128864259 — "Prescriptive analytics represents the most decision-oriented form of analytical reasoning."
[^a9]: openalex-org-w7128864259 — "but also explicit modeling of objectives,"
[^a10]: openalex-org-w7128864259 — "prescriptive queries often build upon descriptive and predictive"
[^a11]: openalex-org-w7128864259 — "Users often omit temporal scopes, comparison baselines, evaluation criteria, or even the precise analytical goal."
[^a12]: openalex-org-w7128864259 — "implicitly assumes a time window, a definition of improvement, and one or more baseline conditions."
[^a13]: openalex-org-w7128864259 — "systems must reconstruct latent analytical intent rather than merely"
[^a14]: openalex-org-w7128864259 — "decomposition can propagate through the analytical pipeline."
