---
description: "Over-reasoning is excess explanation that can bury the fault a novice needs; a survey of 10 raters scored LLM fault explanations on conciseness as a dimension apart from accuracy."
aliases: ["over-reasoning", "excessive explanation"]
sources: ["arxiv-2512-03421"]
---
# Over-reasoning in explanations

Over-reasoning is a failure of the answer as delivered, not of the answer's content. The paper describes it as the case where models produce more text than the fault needs: "excessive or unnecessary explanations that may obscure the actual fault".[^c1] The cost is to the reader. The authors say the surplus "increases the cognitive load for novice programmers" and "introduces misleading information, making debugging less efficient".[^c2] A localization can be right and still reach the asker in a form the asker cannot use.

Two mechanisms are implied, and the paper states neither as a result. First, length adds load: a novice must sort through the explanation before reaching the line that matters. Second, length adds surface: each extra sentence is one more claim the reader has to check. Both are my inference from the authors' wording, not something they measured.

What the paper does measure is a rating. Ten evaluators took part, "5 novice programmers with one year of programming experience and 5 programmers with three years of experience", and each group "independently evaluated 30 randomly sampled examples".[^c3] Each explanation was scored on four criteria: usefulness, conciseness, relevance and accuracy. Conciseness was defined as "Does the explanation not contain unnecessary information?"[^c4] So the survey separates the length-related criterion from correctness, which is the separation over-reasoning needs in order to be a distinct concept at all.

The result that touches it is a between-family gap. Closed-source models beat open-source ones on conciseness by 0.30 points, "representing the largest performance gap among all evaluated metrics".[^c5] That is the widest gap of any criterion. It says the families differ most in how much unnecessary material their explanations carry, as the raters judged it. It does not say that shorter explanations help a novice find a fault.

The concept is distinct from the cost of reasoning length to accuracy. There, a longer trace lowers the answer's correctness; here the trace may be correct and still hurt the reader. The two should not be merged: a note on reasoning length cannot show that clarity to a human falls with length.

## Limits

- The paper asserts over-reasoning as "one major issue", citing prior work for it.[^c1] It does not vary explanation length, and it does not test whether a shorter explanation leads to faster or more successful debugging. The conciseness score is a rating, not a debugging outcome.
- The survey covers one dataset (BugT, from the authors' own platform) and 30 sampled examples per group.[^c3] BugT was chosen because the raters knew that platform, so the sample is not a population of novices at large.
- The conciseness gap is between closed and open families, which differ in much besides length. The paper does not attribute the gap to length.
- The one-year group rated every dimension higher than the three-year group. The paper reads the more experienced raters as better discriminators, who "show enhanced discriminatory capabilities", and as more critical of the explanations.[^c6] That reading is the authors', and was not tested.

## Related

- [[moderate-adaptive-reasoning-length]] — longer reasoning lowered accuracy on theory-of-mind tasks; the cost there falls on correctness, here on the reader
- [[concise-reasoning-mode]] — a short rationale as a decoding mode, traded against accuracy and cost rather than clarity
- [[interpretability-paradox-in-narrated-explanations]] — explanation quality as narrated by an LLM does not follow the model's own interpretability
- [[feedback-quality-bottleneck]] — explanation quality as a limit on self-repair, another place where what the explanation says sets the outcome

[^c1]: arxiv-2512-03421 — "excessive or unnecessary explanations that may obscure the actual fault"
[^c2]: arxiv-2512-03421 — "introduces misleading information, making debugging less efficient"
[^c3]: arxiv-2512-03421 — "each group independently evaluated 30 randomly sampled examples"
[^c4]: arxiv-2512-03421 — "Does the explanation not contain unnecessary information?"
[^c5]: arxiv-2512-03421 — "representing the largest performance gap among all evaluated metrics"
[^c6]: arxiv-2512-03421 — "More experienced developers appear to possess greater capacity for identifying limitations in LLM-generated explanations"
