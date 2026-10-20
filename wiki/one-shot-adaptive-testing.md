---
description: "One-shot adaptive testing picks a fixed-length question set from an initial ability estimate, before any answer is seen; it trades the feedback loop of CAT for a single batch."
aliases: ["OAT", "one-time adaptive item selection"]
sources: ["arxiv-2512-00439"]
---
# One-shot adaptive testing

One-shot adaptive testing (OAT) is an assessment design in which the items are chosen before the examinee answers any of them. The selector sees only an initial ability estimate, draws a fixed-length set of questions, the examinee answers all of them, and one update produces the final estimate.[^c1] The constraint is the point. Computerized adaptive testing (CAT) differs because it "selects questions in a sequential and feedback-driven manner", revising the ability estimate after each response.[^c2] The paper's motivation is that this loop is impractical where "limitations in scenarios with high interaction costs or constrained response conditions" apply.[^c3]

Formally, the paper casts the choice as a bi-level combinatorial problem: "the outer layer selects a subset of questions, and the inner layer estimates student ability based on simulated response data."[^c4] Its search is evolutionary. Each individual in a population is a candidate test form, an ordered list of L distinct question indices drawn from the student's untested pool. Its fitness is obtained by simulation: the examinee's ability is given a virtual update from the simulated answers, and the result is scored on a reserved set of items, "the prediction quality is measured using a hybrid metric that combines AUC and accuracy".[^c5] What the search optimises is therefore the predicted accuracy of a simulated test, not the accuracy of a test the examinee took.

Two mechanism-level points survive the move out of this paper. First, once the whole test is a single batch, the selection problem is a search over subsets rather than a sequential policy, so the usual tools of combinatorial search (crossover, mutation, population selection) become available. Second, the value of a question depends on the examinee, so the starting population is seeded with ability-difficulty matching: the paper's strategies are matching, diverse and random, and the matching score is "a personalized distance vector that quantifies the matching quality between student" and the item set.[^c6] The paper reports that the evolutionary view of this task had not been developed before: "from an evolutionary optimization perspective remains unexplored".[^c7]

## Limits

- **Simulated fitness.** The search is scored against the examinee's responses on held-out items, not against the answers the examinee will give on the selected set. How closely the simulated score tracks the final estimate on real answers is not shown in the part of the text read here. My inference: this is the step where a one-shot method can be most wrong, because the selection never sees the real answers.
- **Logged data.** The evaluation uses two logged datasets, "JUNYI (Chang et al. 2015) and PTADisc (Hu et al. 2023)".[^c8] No live one-shot administration is described in the text read.
- **Length range.** The selection lengths tested are "{5, 10, 15, 20}".[^c9] Behaviour outside that range is not reported.
- **Baselines.** The comparison includes "eight CAT algorithms".[^c10] The text read does not say how these sequential methods were adapted to a single batch; this matters for reading the comparison, and is my inference from the absence of a description.
- **Backbone dependence.** The reported numbers depend on the diagnosis model (MIRT and NCD are the two backbones named), not only on the selector.

## Related

- [[fisher-information]] — the item-information quantity the paper uses to choose which question to insert in its mutation step
- [[simulated-respondent-icc]] — estimating IRT item parameters without field-test data, one way to obtain the item parameters a one-shot selector needs
- [[curse-of-knowledge-difficulty]] — item difficulty as a human or model judgement, the input that the matching step above assumes is available

[^c1]: arxiv-2512-00439 — "the OAT selects a fixed-length question set"
[^c2]: arxiv-2512-00439 — "Unlike CAT, which selects questions in a sequential and"
[^c3]: arxiv-2512-00439 — "limitations in scenarios with high interaction costs or constrained response conditions"
[^c4]: arxiv-2512-00439 — "this task can be naturally viewed as a bi-level combinatorial optimization problem"
[^c5]: arxiv-2512-00439 — "the prediction quality is measured using a hybrid metric that combines AUC and accuracy"
[^c6]: arxiv-2512-00439 — "vector that quantifies the matching quality between student"
[^c7]: arxiv-2512-00439 — "from an evolutionary optimization perspective remains unexplored"
[^c8]: arxiv-2512-00439 — "JUNYI (Chang et al. 2015) and PTADisc (Hu et al. 2023)"
[^c9]: arxiv-2512-00439 — "The one-shot selection lengths L are set {5, 10, 15, 20}"
[^c10]: arxiv-2512-00439 — "In total, eight CAT algorithms are considered"
