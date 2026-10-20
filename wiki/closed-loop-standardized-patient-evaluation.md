---
description: "A clinical agent is scored over a whole simulated encounter: role-split packets hide the facts it must elicit, and timed rubric items are checked against the trajectory, not the final answer."
aliases: ["SP-style interactive evaluation", "standardized-patient simulation benchmark", "process-level SP evaluation", "MedSP1000-style closed-loop evaluation"]
sources: ["doi-10-48550-arxiv-2606-05112", "arxiv-2512-10195"]
---
# Closed-loop standardized-patient evaluation

Medical education has long measured clinicians with standardized patients. "Trained actors who consistently portray clinical cases to enable learners to practice in safe simulations" are the SPs.[^c1] In an objective structured clinical examination, a trainee meets the SP and faculty score the encounter against predefined rubrics, so every examinee faces the same case. The mechanism that transfers to language models is the split between what the examinee starts with and what the other roles hold.

Concretely, the MedSP1000 work converts each source case into role-specific packets. The examinee model receives only a scenario-initialization packet, and "it needs to progressively interact with other agents" to obtain the rest.[^c2] A patient agent holds the patient script. An environment controller holds the results of tests and procedures, and it "advances the clinical scenario only when permitted by the source materials."[^c3] The scoring rubric goes to a separate evaluator. The pipeline's aim is that the examinee never sees the answer key: the source is partitioned into "four role-specific packets containing only the information" that role may use, followed by a leakage audit.[^c4]

Scoring happens over the run, not on the last message. After the encounter, an evaluator agent judges each rubric item "as completed or not based on the full interaction trajectory."[^c5] The stated purpose is "process-level evaluation of what the model did, omitted or did at the wrong time."[^c6] The rubric items are therefore partly about timing: a drug that should be given before thrombolysis counts as missed if it comes late. The primary number is the case-level rubric completion rate, averaged over cases.

What the mechanism measured in this paper: the strongest of seven models, GPT-5.5, "completes only 60.4% of expert-defined rubric items."[^c7] Practice-based learning and improvement is the weakest competency, and "PBLI completion does not exceed 30% in any model."[^c8] A small set of 100 verified cases was used to test test-time strategies. The single-pass baseline scored 67.1%, Best-of-5 67.8%, and a five-specialist consultation 68.0%.[^c9] The authors conclude that "Additional test-time scaling does not improve interactive performance."[^c10] The one competency that rose consistently under both strategies was interpersonal communication.[^c11]

The reason the encounter form matters, as I read it, is that a failure can be an omission in the middle of a dialogue. "Adequate information gathering does not guarantee optimal care recommendations," the authors write in a case discussion, which is a statement about the gap between asking and acting.[^c12] A single final answer cannot show whether the model asked the question that changes the plan. This is my inference from the design, not a result the paper isolates: in the parts I read I did not find the same cases scored once as a static question and once as an encounter.

The same split and the same static pairing appear in AutoMedic, a text simulator with a doctor agent, a patient agent and a clinical staff agent. The staff agent holds the test results and "is unavailable if it is not in the profile, preventing" data hallucination, so an absent result is said to be absent rather than invented.[^c17] Each item is also scored as a static multiple-choice question with the full vignette, and "static QA responses are subsequently compared" with the dialogue answers.[^c18] That is the pairing the paragraph above says was not found in the parts of the SP paper read. The two papers differ in what the examinee is scored on: AutoMedic checks a final diagnostic answer against the static baseline, while the SP rubric checks timed actions across the encounter.

## Limits

- The scenarios are teaching simulations. The authors say they "remain idealized" and that the benchmark is "a standardized, pre-deployment assessment" rather than evidence of bedside readiness.[^c13]
- Both the patient and the environment are LLM agents, and so is the evaluator: "evaluation is conducted through LLM-driven patient and environment agents."[^c14] The clinician checks cover a sample (100 cases, two annotators each), not every run.
- The test-time comparison uses 100 cases. Its differences are "less than one percentage point," and the paper calls them not significant.[^c15] A null on this sample does not exclude a moderate gain. The overconfidence explanation for the flat result is the authors' attribution, supported by one case study.[^c16]
- The domain is medicine and the rubric is organised by six ACGME competencies. Whether the split-packet design transfers to other interactive tasks is not tested here.

## Related

- [[clarification-benchmarks]] — the field's interactive benchmarks; this one scores a whole encounter, of which asking is one part, not the ask decision alone
- [[expert-report-derived-atomic-rubrics]] — rubrics for a final written report; here the items are timed actions inside a trajectory
- [[has-bench]] — process-level metrics computed from an execution trace, the same move of scoring the path rather than the outcome
- [[constitutive-rubric-criteria]] — whether an evaluator can judge a rubric item from the transcript alone, which is the question the evaluator agent faces here
- [[gated-socratic-scaffolding]] — an SP-based OSCE trial on the training side of the same tradition
- [[direct-interactive-accuracy-gap]] — the same static-versus-interactive pairing in a PL/SQL benchmark, where asking can lose to a full up-front spec

[^c1]: doi-10-48550-arxiv-2606-05112 — "trained actors who consistently portray clinical cases to enable learners to practice in safe simulations"
[^c2]: doi-10-48550-arxiv-2606-05112 — "It needs to progressively interact with other agents"
[^c3]: doi-10-48550-arxiv-2606-05112 — "The environment controller advances the clinical scenario only when permitted by the source"
[^c4]: doi-10-48550-arxiv-2606-05112 — "four role-specific packets containing only the information"
[^c5]: doi-10-48550-arxiv-2606-05112 — "item as completed or not based on the full interaction trajectory"
[^c6]: doi-10-48550-arxiv-2606-05112 — "process-level evaluation of what the model did, omitted or did at the wrong time"
[^c7]: doi-10-48550-arxiv-2606-05112 — "completes only 60.4% of expert-defined rubric items"
[^c8]: doi-10-48550-arxiv-2606-05112 — "PBLI completion does not exceed 30% in any model"
[^c9]: doi-10-48550-arxiv-2606-05112 — "the single-pass baseline reaches a macro completion rate of 67.1%"
[^c10]: doi-10-48550-arxiv-2606-05112 — "Additional test-time scaling does not improve interactive performance."
[^c11]: doi-10-48550-arxiv-2606-05112 — "the only dimension in which both strategies consistently improve over single-pass is interpersonal and"
[^c12]: doi-10-48550-arxiv-2606-05112 — "Adequate information gathering does not guarantee optimal care recommendations."
[^c13]: doi-10-48550-arxiv-2606-05112 — "the resulting scenarios remain idealized"
[^c14]: doi-10-48550-arxiv-2606-05112 — "evaluation is conducted through LLM-driven patient and environment agents"
[^c15]: doi-10-48550-arxiv-2606-05112 — "the differences among the three strategies are less than one percentage point"
[^c16]: doi-10-48550-arxiv-2606-05112 — "We attribute this to multi-agent prompting strategies instead introducing overconfidence"
[^c17]: arxiv-2512-10195 — "is unavailable if it is not in the profile, preventing"
[^c18]: arxiv-2512-10195 — "static QA responses are subsequently compared"
