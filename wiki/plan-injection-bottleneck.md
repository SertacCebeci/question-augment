---
description: "Injecting expert-written plans into a deep-research agent, with its retrieval and reasoning unchanged, lifted reasoning accuracy by 12 points, locating the plan as a bottleneck."
aliases: ["gold plan injection", "ground-truth plan ablation", "planning bottleneck", "plan-injection ablation"]
sources: ["arxiv-2512-00986"]
---
# Plan-injection bottleneck

A deep-research agent works in stages: it decomposes a question into sub-tasks, retrieves evidence for them, and reasons that evidence into a report. When the end score is low, the cause can sit in any of the three. A plan-injection ablation tests one stage at a time. The agent is given an expert-written plan in place of its own, while its retrieval and reasoning stay model-generated.[^p1] If the score moves, the plan was limiting it.

In the ADRA-Bank benchmark for academic research, the ablation was run on OpenAI's agent. Its reasoning accuracy "rose from 58.65% (end-to-end) to 70.93%", a gain of about 12 points, which the authors read as "a 12% gain confirming planning as a dominant bottleneck".[^p2] Their mechanism is that "high-quality plans effectively guide reasoning even with imperfect retrieval".[^p3] A right sub-task structure can carry an answer through weak search: the plan says what each piece of evidence is for, and the reasoner can work from partial evidence against a clear frame.

The gold plans are expert annotations, not a sample of what the agent could have produced. The benchmark compares agent sub-tasks "against research plans annotated by experts based on the structural outline of papers".[^p4] The mechanism matters for reading the effect. The injected plan carries structure the agent did not have, so the measured gap is what a correct plan is worth, not what an ordinary planner loses. The same paper reports that the agent's planning is the weak stage in its own runs: "while Planning hovers around 40%".[^p5]

## Limits

- The text read reports the ablation for one agent, OpenAI's. Table 9 holds the gold-plan results across modules and was not examined here, so whether the gain holds for other agents is not established by this work.
- "Dominant bottleneck" is a claim about this pipeline and this benchmark's reasoning metric (boolean diagnostics). It does not show that planning limits other tasks, question types or formats.
- The passage says retrieval stayed "model-generated" under the injected plan. It does not say whether retrieval queries were regenerated from the new plan, which would change how far the effect runs back into search.
- The plan helps but does not settle the score. Even at pass@3, the reported top reasoning score is 68.49%, so the injected plan is one factor among several (my inference from the pass@k numbers the paper gives).
- The gain is measured on expert plans that encode the paper's outline. A planner that does not have that outline is not tested; the ablation shows an upper bound on the plan's effect, not a method for producing better plans.

## Related

- [[stage-disentangled-evaluation]] — the benchmark design that scores planning, retrieval and reasoning apart, which makes this ablation readable.
- [[plan-before-search-anchoring]] — writing the sub-question plan before retrieval; that note is about what the plan does to search, this one about what it does to the answer.
- [[decomposer-planner-centric-rl]] — training the planner on rewards that ignore the answerer, the same plan-quality question from the training side.
- [[failure-mode-taxonomy]] — locating deep-research errors by stage from execution logs, a different route to the same question of where an answer failed.

[^p1]: arxiv-2512-00986 — "providing agents with ground-truth plans while keeping model-generated retrieval and reasoning"
[^p2]: arxiv-2512-00986 — "rose from 58.65% (end-to-end) to 70.93%"
[^p3]: arxiv-2512-00986 — "high-quality plans effectively guide reasoning even with imperfect retrieval"
[^p4]: arxiv-2512-00986 — "research plans annotated by experts based on the structural outline of papers"
[^p5]: arxiv-2512-00986 — "while Planning hovers around 40%"
