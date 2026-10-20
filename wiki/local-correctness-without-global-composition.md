---
description: "Most local judgments can be right while the joint state is wrong: a partial score can stay high beside the low whole-output success that exact matching records."
aliases: ["local-global gap", "native-versus-complete gap", "partial correctness without composition", "composition failure in structured answers"]
sources: ["doi-10-48550-arxiv-2609-38409"]
---
# Local correctness without global composition

Structured-answer benchmarks can report two numbers that measure different things. The strict one is complete-task success, and for structured outputs "this requires exact recovery of the required structured output."[^l1] The generous one is a native score: "Each task also returns a native score in [0, 1] that captures task-specific partial correctness."[^l2] The ArgGYM paper reports both, and insists they are not merged: native scores "are interpreted only within the corresponding task and are never averaged into a benchmark-wide score."[^l3]

The gap between the two is large. "Qwen3.5-27B with thinking enabled reaches 88.7 native on status_query but only 35.8% complete success, while DeepSeek-v4.1-Flash reaches 89.7 native but only 34.2% complete success on the same task."[^l4] The gap widens with structure. On status_query, the same model falls to "only 10.0% complete success while retaining an 84.5 native score" in the richest curriculum band, from 72.5% complete success in the simplest.[^l5]

The paper's reading is that integration fails, not knowledge. "An answer can therefore contain many correct local judgments while still representing the overall argumentative state incorrectly."[^l6] It adds that "integration of those components is itself a major source of failure."[^l7] The discussion states the asymmetry in one line: "local argumentative competence is more reliable than global argumentative composition."[^l8]

The mechanism, as far as the paper shows it: a state is a joint object. Each support, attack, or status is a local verdict that a native score can credit one by one. A complete answer is right only if all of them hold together and agree with one another, so one wrong link can change what follows from the rest. The native score does not penalise that dependence, and the complete score does. (My inference: a per-item accuracy that is steady across items still gives a whole-output success that falls as the number of joint items grows. The paper does not vary structure at fixed accuracy to show this.)

## Limits

- The gap partly measures the metric. Complete success is an exact test, so a looser threshold would narrow the gap. The paper does not vary the threshold, so how much of the gap is the model and how much is the all-or-nothing criterion is not separated. (My inference.)
- The paper ties the curriculum bands to "increasing structural richness rather than a guaranteed monotonic ordering of empirical difficulty."[^l9] A band that is harder in structure is not automatically harder in the same way for every model, so the decline should not be read as a single difficulty curve.
- Native scores are task-specific by design. Comparing the gap across tasks compares different partial-credit definitions, and the paper forbids the aggregation that would make such a comparison simple.
- The formalization task uses template-generated descriptions, so the joint-state failures are measured on controlled language. Whether the same gap appears on open text is not tested.[^l10]

## Related

- [[recall-only-partial-credit]] — partial credit that counts only captured items; here the partial credit is what hides a whole-output failure
- [[false-credit-propagation]] — a locally correct judgment that still feeds a wrong total, the same joint dependence on the reward side
- [[detection-correction-gap]] — another split between getting the parts right and getting the final answer right
- [[compositional-inference-leakage]] — fragments that reveal nothing alone and a conclusion when combined, the same joint structure on the disclosure side
- [[grounded-argument-acceptance]] — the joint state that these local verdicts together fix

[^l1]: doi-10-48550-arxiv-2609-38409 — "this requires exact recovery of the required structured output"
[^l2]: doi-10-48550-arxiv-2609-38409 — "Each task also returns a native score in [0, 1] that captures task-specific partial correctness"
[^l3]: doi-10-48550-arxiv-2609-38409 — "are interpreted only within the corresponding task and are never averaged into a benchmark-wide score"
[^l4]: doi-10-48550-arxiv-2609-38409 — "Qwen3.5-27B with thinking enabled reaches 88.7 native on status_query but only 35.8% complete success"
[^l5]: doi-10-48550-arxiv-2609-38409 — "to only 10.0% complete success while retaining an 84.5 native score"
[^l6]: doi-10-48550-arxiv-2609-38409 — "An answer can therefore contain many correct local judgments while still representing the overall argumentative state incorrectly"
[^l7]: doi-10-48550-arxiv-2609-38409 — "integration of those components is itself a major source of failure"
[^l8]: doi-10-48550-arxiv-2609-38409 — "local argumentative competence is more reliable than global argumentative composition"
[^l9]: doi-10-48550-arxiv-2609-38409 — "rather than a guaranteed monotonic ordering of empirical difficulty"
[^l10]: doi-10-48550-arxiv-2609-38409 — "its descriptions are template-generated"
