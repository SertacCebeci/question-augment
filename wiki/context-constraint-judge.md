---
description: "An LLM judges whether one recommendation fits the user's stated context (distance, hours, cost, cuisine, rating) as correct or incorrect; best F1 0.99 on synthetic cases."
aliases: ["LLM-based judgment of contextual understanding", "context-alignment judge", "contextual understanding benchmark", "in-car ConvQA judge"]
sources: ["arxiv-2512-12042"]
---
# Context-constraint judge

A context-constraint judge is an LLM prompted to check one given answer against the situational constraints that the request states. In the instance studied here, the input is a user block, a request in natural language together with its context (time, location, cost level, cuisine, rating threshold), and a system block, one recommendation with its attributes (distance, opening hours, cost, cuisine, rating). The output is a boolean: 1 if the recommendation is correct, 0 if it is not.[^c1]

The correctness condition is not left to the model's sense of "fits". It is written into the prompt as a rule list: a recommendation is incorrect if the location is too far away, the restaurant is closed at the requested time, the cost or rating deviates from the user's parameters, or the cuisine does not match the request.[^c2] The judge's verdict is then compared with the label the input was built with, and agreement is summarised as an F1 score.[^c3]

The motivating failure is a venue that does not match the request, "a restaurant that is too far away or closed", which the authors say lowers user trust.[^c4] The judge does not produce the answer. It inspects an answer that already exists and tests whether that answer respects the context. A system can fail the context in two ways: the answer is wrong for the request, or the system does not notice that it is wrong. The judge addresses the second, and this is my reading of the design rather than a claim the paper makes in these words.

## Construction and what was measured

The dataset is synthetic. It has 100 user blocks, and for each one a correct system block plus five incorrect ones "with misalignments based on induced errors."[^c5] The authors had eight annotators check 20 randomly drawn user–system pairs, and the dataset's mean human-rated validity came to "human-rated validity score of 3.95 out of 5, indicating high overall quality."[^c6][^c7]

Across the judges tested, the best F1 was 0.990, reached by DeepSeek-R1 with CoT-1 and with self-consistency prompting.[^c8] The best non-reasoning model was DeepSeek-V3: "Overall, the best tradeoff between effectiveness and cost/time efficiency is achieved with the nonreasoning model DeepSeek-V3."[^c9] The weakest result was GPT-3.5 Turbo with the multi-agent debate prompt.[^c10]

F1 was chosen over accuracy because it "is therefore more informative than accuracy in the presence of class imbalance, as in our case."[^c11] The formalism survives the transfer in one form: F1 measures how well the judge's positive calls match the positive labels, balancing precision and recall. What does not survive is any reading of the score as a human's verdict on a restaurant. The labels were assigned by the induction procedure, and the human check covered a small sample.

## Limits

- One case study: restaurant recommendations in one car context. "Our evaluation is based on a single case study."[^c12]
- Correctness is defined by the prompt's rule list and the labels are built from the same rules. A high F1 therefore shows rule-following on these error types. It does not show that a rider would accept the venue. This is my inference from the design.
- Single-turn requests only. The authors list multi-turn dialogue as future work, "rather than single-turn queries, would offer deeper insights into the".[^c13]
- Reproducibility is partial. Temperature was set to 0 where possible, but for OpenAI reasoning models "control is not supported, and we used the default setting."[^c14] Proprietary model sizes are unknown, so no size-performance claim is made for them: "the model size is not publicly shared".[^c15]
- The per-category breakdown of where the judge fails is a separate result; see [[error-category-judge-blind-spot]].

## Related

- [[error-category-judge-blind-spot]] — which kinds of constraint violation this judge misses, and which models miss them
- [[dual-track-rubric-constraints]] — constraints read from the query as one track of a rubric, the same move of checking an answer against stated constraints
- [[judge-coverage-overestimation]] — judges that accept surface coherence as completeness, a failure a context check could also hit
- [[task-conditional-prompt-gain]] — how a prompting package's effect on this judge depends on the model class

[^c1]: arxiv-2512-12042 — "judgment result in terms of a boolean score, where 1 corresponds to the"
[^c2]: arxiv-2512-12042 — "A recommendation is considered incorrect if one of the following applies"
[^c3]: arxiv-2512-12042 — "Based on the agreement and disagreement results with the actual recommendation alignment"
[^c4]: arxiv-2512-12042 — "(i.e., a restaurant that is too far away or closed), user trust may decline."
[^c5]: arxiv-2512-12042 — "five incorrect recommendations with misalignments based on induced errors."
[^c6]: arxiv-2512-12042 — "human-rated validity score of 3.95 out of 5, indicating high overall quality."
[^c7]: arxiv-2512-12042 — "The human evaluation of 20 randomly selected user–system block pairs"
[^c8]: arxiv-2512-12042 — "all models and techniques of 0.990 is achieved by DeepSeek-R1 with CoT-1"
[^c9]: arxiv-2512-12042 — "Overall, the best tradeoff between effectiveness and cost/time efficiency is achieved with the nonreasoning model DeepSeek-V3."
[^c10]: arxiv-2512-12042 — "The worst result is achieved with GPT-3.5"
[^c11]: arxiv-2512-12042 — "and is therefore more informative than accuracy in the presence of class imbalance, as in our case."
[^c12]: arxiv-2512-12042 — "Our evaluation is based on a single case study."
[^c13]: arxiv-2512-12042 — "rather than single-turn queries, would offer deeper insights into the"
[^c14]: arxiv-2512-12042 — "control is not supported, and we used the default setting."
[^c15]: arxiv-2512-12042 — "the model size is not publicly shared"
