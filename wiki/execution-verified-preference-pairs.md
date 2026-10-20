---
description: "Labeling sampled SQL queries by whether their execution matches the gold result yields preference pairs with no human labels; the Planner's BIRD dev accuracy rose from 53.65 to 59.32."
aliases: ["execution-based preference labels", "reinforcement learning from execution feedback", "RLEF", "execution-match preference pairs"]
sources: ["arxiv-2512-18622"]
---
# Execution-verified preference pairs

Preference training needs, for each prompt, a chosen output and a rejected one. Usually a human or a reward model supplies the ranking. When the task has an executable check, the check can supply the ranking instead. The paper's system, MATS, samples several SQL queries for a question, runs each against the database, and labels a query as chosen when its execution matches the ground truth. A query is rejected when it "results in a syntax error or differing execution."[^c1][^c2]

The paper calls this reinforcement learning from execution feedback (RLEF). Its alignment uses the ORPO objective, and the paper says it adopts that algorithm.[^c3] The pairs are built per prompt from the sampled actions: a sample is kept only when it has at least one chosen and one rejected action, and otherwise "the training sample is ignored."[^c4] So the database does the labelling, and the questions it cannot separate drop out of training.

The sampled set is not purely the student's own output. One action in each set comes from a larger assistant model, "and one action is sampled from the assistant agent A,"[^c13] and that assistant "generates higher-quality actions for the task."[^c5] The other actions come from multinomial decoding at a set temperature. The chosen and rejected labels therefore mix the student's own errors with a stronger model's attempts, and the execution check decides which side of the pair each one lands on.

The measured effect is on the Planner, the component that writes SQL. On BIRD dev, the text says RLEF "improves the Planner Agent's EX% from 53.65 to 59.32," where 53.65 is the SFT starting point. The paper reports the change across RLEF iterations in one figure, and the text does not say which iteration produced 59.32.[^c6] For the whole framework on BIRD dev, accuracy went from 59.06 to a peak of 64.73.[^c7] The authors conclude that "confirm that execution feedback is both helpful and essential for" small models' execution accuracy.[^c8]

Alignment algorithm matters. With PPO and a binary reward of "correct execution and 0 otherwise," the paper saw a small gain, from 53.65% to 54.95%, at a far higher training cost.[^c9] DPO in the same setup suffered "catastrophic forgetting, causing accuracy to drop to 44.98%."[^c10]

What survives the transfer: where a gold output can be run, the execution result is a free and deterministic label, and its pairs can train a generator without a human in the loop. What does not: the label is only as good as the gold and the execution match, and the setting needs a checker. The paper gives no account of open-ended questions where no such check exists.

## Limits

- The labels exist only where a gold execution exists. The paper's data is Spider and BIRD with gold SQL, and the text does not test any task without an executable reference.
- Execution match is a proxy for correctness. The paper notes that for some queries "multiple queries selecting different columns may still produce the same correct result," which means a correct query can be rejected when its column choice differs from the gold.[^c11] The same weakness applies in training, where the rejected side can be right in a way the check does not recognise.
- The gain is measured against an SFT baseline whose training data also came from a larger model: the paper generated extra training samples "to generate additional training samples for the rest" of the dataset with GPT-4o-mini.[^c12] The text does not isolate execution labels from the distillation source, so the RLEF gain is not separated from the assistant's contribution.
- The text I read reports one run per setting and no seeds or variance for the RLEF iterations. The gains are single-number differences.
- The text does not report how many samples the "ignored" rule removes, so the share of questions that actually shape training is not known.

## Related

- [[candidate-selection-gap]] — the same system's candidate pool: execution labels train the generator here, while the selector limits what is picked there.
- [[verifier-discrimination-and-calibration]] — execution verdicts as labels for verifiers; the reference "correct" inherits the limits of the tests.
- [[tool-type-confidence-dichotomy]] — verification tools return deterministic execution feedback, the kind of signal used here.
- [[preference-optimization-for-questions]] — preference optimization whose ranking is about questions themselves; here the ranking is grounded in an executed answer.

[^c1]: arxiv-2512-18622 — "matching the ground-truth execution; the rejected action is"
[^c2]: arxiv-2512-18622 — "a query resulting in a syntax error or differing execution."
[^c3]: arxiv-2512-18622 — "we adopt the ORPO algorithm"
[^c4]: arxiv-2512-18622 — "the training sample is ignored."
[^c5]: arxiv-2512-18622 — "model generates higher-quality actions for the task."
[^c6]: arxiv-2512-18622 — "EX% from 53.65 to 59.32, while on"
[^c7]: arxiv-2512-18622 — "59.06 to a peak of 64.73 before slightly stabilizing"
[^c8]: arxiv-2512-18622 — "confirm that execution feedback is both helpful and essential for"
[^c9]: arxiv-2512-18622 — "accuracy from 53.65% to 54.95%, but incurs a significantly high"
[^c10]: arxiv-2512-18622 — "catastrophic forgetting, causing accuracy to drop to 44.98%."
[^c11]: arxiv-2512-18622 — "selecting different columns may still produce the same correct result,"
[^c12]: arxiv-2512-18622 — "to generate additional training samples for the rest"
[^c13]: arxiv-2512-18622 — "and one action is sampled from the assistant agent A."
