---
description: "Scoring whether a user can anticipate that a model will be wrong on an instance, before answering it, showed a teaching effect where AI-assisted team accuracy had shown none."
aliases: ["error predictability", "anticipating LLM failures", "predicting when a model is likely wrong", "error-predictability metric"]
sources: ["arxiv-2512-21422"]
---
# Error-anticipation accuracy

A user who is taught a model's weak spots can be scored in two ways. The usual score is AI-assisted team accuracy: whether the human-plus-model answer is correct. The alternative scores whether the user can predict, from the instance, that the model will be wrong. The user does not have to solve the question; they only have to decide whether the model should be used for it.[^c1] The paper's argument is that the team score mixes two things. A user who sees that a model is unreliable on a region may still defer to it when they are unsure, and a user who cannot solve a problem cannot reach a correct team answer even when correctly refusing the model.[^c2]

The paper sets the metric against prior work on human error prediction, which it describes as a known weakness: humans "struggle to predict when an AI system is likely to make an error."[^c3] The metric asks whether teaching can change that prediction.

**The study.** The paper repeats a two-part study of Mozannar et al. (2023) on MMLU. Users first see 20 multiple-choice questions and record whether they would use the AI, would not, or are uncertain, with a reason. They are then taught descriptions of the model's strengths and weaknesses, and tested again on the same 20 questions.[^c4] Five questions per set match none of the taught patterns, so that the test can show whether users apply the rules beyond the cases they were meant for.[^c5] Prior team-accuracy work had found no gain from teaching: "teach users in this way has not improved the accuracy of people when assisted by an LLM."[^c6]

**The result.** With the anticipation metric, 18 of 20 participants improved after teaching. A paired t-test gave p = 0.0009 and Cohen's d was 0.88.[^c7] Teaching also helped by subject: it "improved user accuracy in anticipating LLM failures for questions from 10 subjects," and declined for 4. Nearly every subject that improved was named in the taught descriptions, the exception being business ethics. The authors read the declines as failures of matching: "matching instances to failure descriptions is nontrivial and can impact teaching effectiveness."[^c8]

What the metric separates is knowledge of where a model fails from skill at the underlying task. That is the part that carries over. It is a per-instance discrimination score, close in form to the signal-detection d' used for over-reliance in [[over-reliance-discrimination-failure]], but applied before a candidate answer exists. Whether the same separation holds for other tasks is my inference, not something the paper tests.

## Limits

- Teaching did not make users reliable. Even after teaching, "use LLMs could still be as low as 25%," the paper says, and the authors name "how to guide users who recognize they should not use an LLM, yet cannot complete the task on their own" as open.[^c9]
- Twenty participants, recruited from the authors' personal network of NLP doctoral students and their friends, because a six-person pilot on a crowdworker platform produced "a mix of poorfaith attempts" and misread instructions.[^c10] The authors say a larger sample "would benefit" the findings.[^c11]
- MMLU only. The metric is not run on MathCAMPS, where the failure groups are defined by educational standards.
- Test and training use the same 20 questions. Transfer to new instances is checked only through the five non-matching questions, which measure over-application, not generalisation.
- The metric scores prediction, not use. A user who predicts failures well may still act on the model's output, and the paper does not observe real use.

## Related

- [[failure-group-coverage-and-error-ratio]] — the groups whose descriptions a teaching study presents; the metric depends on those groups being real and matchable.
- [[over-reliance-discrimination-failure]] — the same question asked after an answer is given (can a student tell a wrong AI answer from a right one), with a near-zero d' in that sample.
- [[calibration-training]] — another route to a better-judged answerer, where scored feedback helps once and transfers modestly; the same caution about per-task gains applies here.
- [[failure-pattern-description-recall]] — the stage that must produce the descriptions before this teaching can happen.

[^c1]: arxiv-2512-21422 — "This metric does not require users to answer"
[^c2]: arxiv-2512-21422 — "to a model for low-confidence tasks, even when"
[^c3]: arxiv-2512-21422 — "Recent research has highlighted how humans struggle to predict when an AI"
[^c4]: arxiv-2512-21422 — "Initially, users are presented 20 multiple-choice questions and asked to"
[^c5]: arxiv-2512-21422 — "These questions allow us to measure whether users apply"
[^c6]: arxiv-2512-21422 — "teach users in this way has not improved the accuracy of people when assisted by an LLM."
[^c7]: arxiv-2512-21422 — "value of 0.88 suggests a large effect size."
[^c8]: arxiv-2512-21422 — "matching instances to failure descriptions is nontrivial and can impact teaching effectiveness."
[^c9]: arxiv-2512-21422 — "an open challenge is how to guide"
[^c10]: arxiv-2512-21422 — "examining the free response explanations given during a pilot study with 6 users"
[^c11]: arxiv-2512-21422 — "Our findings would benefit from a larger sample size,"
