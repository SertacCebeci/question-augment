---
description: "Missing-information detection cast as backward reasoning: enumerate what a goal requires, then flag the requirements the question does not supply; forward reasoning flags far fewer."
aliases: ["RT-ICA", "reverse thinking for missing information detection", "reverse thinking for information completeness assessment", "backward missing-information detection"]
sources: ["arxiv-2512-10273"]
---
# Reverse-prerequisite gap detection

A question can be checked for missing information from its goal rather than from its givens. The goal is the answer the question asks for; the prerequisites are the conditions a derivation of that answer needs; a prerequisite the text neither states nor lets one infer is a gap. The paper's stated premise is that "determining what information is missing requires working backward from solution requirements to identify unsatisfied prerequisites".[^c1] The mechanism is goal regression. The reasoner first lists what the goal requires, and only then asks, for each listed condition, whether the question supplies it. The paper describes the two steps as "The system first decomposes the question into its fundamental logical constituents" and "the framework performs an exhaustive search through the question context" to see whether a condition is provided or inferable.[^c2][^c3] A condition that fails the search is reported as missing, with a description of what it is.

The effect is measured on detection, not on solving. The authors build two sets from existing benchmarks by annotators removing a needed value, definition, relation or assumption, and score a yes/no completeness decision on each. The forward baseline, which starts from the givens and derives toward an answer, is poor at the "incomplete" side: on GPT-3.5-turbo over the test-math set, its accuracy on incomplete problems is "only 20.51%", against 58.97% with the regression procedure.[^c4] Overall accuracy rises in every model and dataset row of the paper's Table 1; for GPT-3.5-turbo on test gsm8k it goes from 44.76% to 72.38%.[^c5] The authors locate the cause in the forward design itself: forward chaining operates "under the implicit assumption that the initial information constitutes a complete and consistent basis for derivation", so nothing in the chain tests whether that assumption holds.[^c6]

The concept transfers at the level of the question's shape. An asker who can list what a complete answer would require has a check on the question that does not depend on the question's surface looking odd. That is my inference from the mechanism, not a result of the paper, which tests only math word problems.

## Limits

- **Small, self-built sets.** test gsm8k has "105 problems sourced from the GSM8K benchmark", with 52 altered to be incomplete; test math has 101 items, 39 of them incomplete.[^c7] With 39 incomplete items, one item moves the "Yes" accuracy by about 2.6 points, and the paper reports no intervals. The labels were checked by annotators: "Each modified problem underwent independent verification by multiple annotators".[^c8]
- **The baseline is forward solving, not direct questioning.** The comparison is with a forward chain-of-thought prompt on the same model. The paper does not compare against asking "is anything missing?" in one pass, or against a clarification policy. The gain is over a solve-first habit, not over every other detector.
- **Over-identification.** The paper's own failure analysis: "the model may still incorrectly flag" absent values that existing constraints would determine, in problems with implicit parameters.[^c9]
- **Vague gap descriptions.** When the detector is right that something is missing, "the model tends to generate vague" accounts of what it is, which weakens the use of the finding.[^c10]
- **Depth.** With long chains of dependencies, "the reverse thinking process occasionally breaks down".[^c11]
- **Cost.** The method uses "approximately 2.3× more tokens" than chain-of-thought prompting.[^c12]
- **The theoretical bound is conditional.** Theorem 1 gives a recall bound of αβ|M*| and a false-positive bound of (1−α)(1−β), and it holds "Under the assumption that the language model M has accuracy α in prerequisite identification and β in availability verification".[^c13] The paper does not estimate α or β, so the bound is algebra on an assumption, not a measured guarantee.
- **Goal must be determinate.** The regression needs a goal with a definite answer. Whether "unsatisfied prerequisite" still names the missing piece when the question's goal is itself unclear is not tested here; it is outside the reach of the paper's math items (my inference).

## Related

- [[backward-chaining-subgoal-decomposition]] — the same backward enumeration, measured there as a recognition skill on geometry proofs; this note adds the availability check and a detection measure, which that note does not test.
- [[recoverability-gated-ask-abstain]] — decides whether a missing variable should be asked for; this note concerns the earlier question of whether one is missing at all.
- [[structured-gap-sufficiency-judge]] — names gaps in retrieved evidence to drive the next query; the gap there is in the evidence, while here it is in the question.

[^c1]: arxiv-2512-10273 — "determining what information is missing requires working backward from"
[^c2]: arxiv-2512-10273 — "The system first decomposes the question into its fundamental logical constituents"
[^c3]: arxiv-2512-10273 — "the framework performs an exhaustive search through the question context"
[^c4]: arxiv-2512-10273 — "baseline achieves only 20.51% accuracy on the"
[^c5]: arxiv-2512-10273 — "The overall accuracy on test gsm8k improves by 27.62 percentage points, rising"
[^c6]: arxiv-2512-10273 — "operating under the implicit assumption that the initial information constitutes a complete and consistent basis for derivation"
[^c7]: arxiv-2512-10273 — "The test gsm8k dataset comprises 105 problems sourced from the GSM8K benchmark"
[^c8]: arxiv-2512-10273 — "Each modified problem underwent independent verification by multiple annotators"
[^c9]: arxiv-2512-10273 — "the model may still incorrectly flag"
[^c10]: arxiv-2512-10273 — "the model tends to generate vague"
[^c11]: arxiv-2512-10273 — "the reverse thinking process occasionally breaks down"
[^c12]: arxiv-2512-10273 — "requiring approximately 2.3× more tokens"
[^c13]: arxiv-2512-10273 — "Under the assumption that the language model M"
