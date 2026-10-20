---
description: "With judge and verification fixed, swapping model-written rubrics for human ones lifts pairwise accuracy by about 26 points; the bottleneck is deciding what to check, not reasoning or compute."
aliases: ["rubric gap", "rubric mis-specification", "criteria-formation bottleneck"]
sources: ["arxiv-2603-01562", "arxiv-2512-01958"]
---
# Rubric formation gap

When an LLM judge scores a response against a list of atomic criteria (a rubric), two things can fail: writing the right criteria, or applying them. RubricBench separates the two by holding the backbone and verification procedure fixed and varying only the rubric source: none, self-generated, or human-annotated. The difference between the last two is the "Rubric Gap", defined as the deficit "solely attributable to the quality of evaluation rubrics".[^c1]

## What was measured

On 1,147 hard pairwise comparisons, self-generated rubrics beat no rubric (DeepSeek-v3.2 from 38.8% to 57.8%), but human rubrics add a large further jump. The gain from human rubrics stays near 26% across model families from lightweight judges to frontier reasoning models, so the authors conclude the limit is "not reasoning capacity, but rubric formation".[^c2] The best human-rubric configuration reached about 84.9%.[^c3]

Failure is concentrated. On safety items, self-generated rubrics score about 25-30%, because models do not propose refusal constraints; human rubrics that encode refusal logic restore accuracy above 90%.[^c4]

## Why model rubrics fail

Generated checklists show attention displacement: lists of more than 13 items still carry hallucination rates above 70% while missing nearly half of the critical constraints; shorter lists (RocketEval) gain precision by losing coverage.[^c5] Against human rubrics, model rubrics contain more low-necessity rules (17.9% vs 10.1%) and more extremely rigid rules, and rigidity is only weakly tied to necessity (corr 0.133 vs 0.306).[^c6] The consequence is judgment inversion: on an impossible task ("convert SQL to Mongo for all cases") the model rubric became an implementation checklist and penalized the correct refusal while rewarding a hallucinated solution.[^c7]

## Compute does not close it

Sampling more rubrics gives non-monotonic returns (GPT-4o-mini 48.0% at Rub@4 to 46.8% at Rub@32), and iterative refinement does not help monotonically. Scaling human rubrics, by contrast, rises (Gemini-3-Flash 75.4% to 85.3% from 2 to 8 rubrics).[^c8] Extra samples appear to add noise rather than missing constraints (the authors' reading). A method that seeds generation with human-curated high-level criteria (CheckEval) had the highest rubric recall, 53.8%, which the authors take as a sign that minimal human priors help.[^c9]

## Limits

- Even with human rubrics accuracy plateaus near 85%; the authors attribute the remainder to preference ambiguity and execution errors where correct rubrics are misapplied, so the gap is not the only bottleneck.[^c10]
- The benchmark selects hard samples with surface bias, so the size of the gap may be larger than on ordinary prompts; this is my inference, not tested.
- Human rubrics are derived strictly from instructions by experts; how much of the gain depends on that annotation protocol rather than "humanness" was not isolated.
- The result concerns judging pairs, not question asking; whether the same formation gap appears when a model must decide which clarifying questions to ask is untested here.

## Related

- [[proxy-verified-rubric-transferability]] — rubrics judged by how well they transfer, a different way to assess rubric quality
- [[rubric-complexity-normalized-reward]] — rubric-based rewards, where rubric quality sets the signal
- [[llm-judge-biases]] — the surface biases rubrics are meant to counter
- [[pretraining-grounded-rubric-self-play]] — automatic rubric generation attempts
- [[data-distilled-scoring-rules]] — a third source of criteria: rules searched from labelled data so that they fit the labels, rather than proposed by a model or written by experts[^c11]

[^c1]: arxiv-2603-01562 — "the performance deficit solely attributable to the quality of evaluation rubrics"
[^c2]: arxiv-2603-01562 — "not reasoning capacity, but rubric formation"
[^c3]: arxiv-2603-01562 — "boosts accuracy to ∼84.9% (OpenRubric with DeepSeek)"
[^c4]: arxiv-2603-01562 — "human rubrics—which explicitly encode refusal logic—restore performance to >90%"
[^c5]: arxiv-2603-01562 — "missing nearly half of the critical constraints"
[^c6]: arxiv-2603-01562 — "(corr(R,N)=0.133 vs. 0.306)"
[^c7]: arxiv-2603-01562 — "rewarding a hallucinatory solution (Response A)"
[^c8]: arxiv-2603-01562 — "GPT-4o-mini degrades from 48.0%"
[^c9]: arxiv-2603-01562 — "CheckEval achieves the highest Rubric Recall (53.8%)"
[^c10]: arxiv-2603-01562 — "accuracy plateaus around 85%"
[^c11]: arxiv-2512-01958 — "learning scoring rules from data"
