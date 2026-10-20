---
description: "LLM judges of recommendations miss some constraint violations more than others: non-reasoning models most often misjudge time and cost errors, while reasoning models stay high across categories."
aliases: ["per-category judge failure", "constraint-category detection gap", "error-category misjudgment"]
sources: ["arxiv-2512-12042"]
---
# Error-category judge blind spot

A judge that checks an answer against several constraints does not fail uniformly. Its accuracy depends on which constraint is violated. In the in-car recommendation benchmark, each incorrect system block carries one induced misalignment from a fixed set of categories (location, time, cuisine, cost, rating), plus a set of correct positives, and the judge's accuracy is reported per category.[^c1] The failure analysis reports that non-reasoning models most often misjudge the time and cost categories, and that GPT-3.5 Turbo was weakest.[^c2]

The shape of the result matters more than the ranking. Reasoning models and large non-reasoning models "generally achieve a high accuracy across misaligned recommendations," and the one category where their accuracy falls below 1 is cost.[^c3][^c7] A single aggregate F1 would hide this: a judge can score well overall while missing one constraint type systematically. The per-category breakdown is the measurement that shows it.

The paper does not isolate why each category is hard. A plausible account, which is my reading and not tested here, is that the categories differ in how the constraint is stated. The prompt rule for time is a check of a given hour against opening hours. The cost constraint is stated in the user block through paraphrases: the dataset draws from "Cost categories (low, medium, high) with 15 paraphrases each," so the judge must map many surface forms onto three levels.[^c4] The rating rule is a tolerance: "exceeding a range of 0.2 around the requested rating."[^c5] Whether these differences explain the category gaps was not tested.

## Limits

- The per-category figure reported for the category analysis is for one model. "Figure 9: DeepSeek-R1 accuracy results based on the category of data used."[^c6] The model-class statement is coarser and is not broken down per model in the part read here.
- Five error categories in one domain. Whether the blind spot is in the judge or in these particular inductions is not separated.
- Accuracy per category is computed on the same synthetic labels that define the rule list. The category gap is a gap in following the rules on these error types. It does not show what a rider would miss.
- No ablation of prompt wording per category. The paper does not change the cost paraphrases or the time phrasing to see whether the gap moves.

## Related

- [[context-constraint-judge]] — the judge whose category-level behaviour this note describes
- [[under-specification-severity-asymmetry]] — a parallel in code generation: removing some constraints costs far more than others
- [[judge-coverage-overestimation]] — another judge blind spot, where a missing step is not noticed; here a violated constraint is not noticed

[^c1]: arxiv-2512-12042 — "location-error, time-error, cuisine-error, cost-error, and rating-error, along"
[^c2]: arxiv-2512-12042 — "containing time or cost errors, with GPT 3.5 Turbo showing the weakest performance."
[^c3]: arxiv-2512-12042 — "generally achieve a high accuracy across misaligned recommendations,"
[^c4]: arxiv-2512-12042 — "Cost categories (low, medium, high) with 15 paraphrases each"
[^c5]: arxiv-2512-12042 — "exceeding a range of 0.2 around the requested rating."
[^c6]: arxiv-2512-12042 — "Figure 9: DeepSeek-R1 accuracy results based on the category of data used."
[^c7]: arxiv-2512-12042 — "with cost errors being the only category where accuracies drop below"
