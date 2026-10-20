---
description: "A rubric-based LLM judge behaves like a multiple-choice answerer: it prefers score options by list position, in a model-specific direction, and balanced cyclic permutations expose and cancel it."
aliases: ["rubric-based judge position bias", "score-option position bias", "criteria-order bias"]
sources: ["arxiv-2602-02219"]
---
# Rubric-option position bias

A pointwise judge given a rubric with a described score per level is not scoring in a vacuum. It must choose one option from a list, so the task resembles a multiple-choice question. The judge then shows the position effects known from multiple-choice answering, here applied to the score levels of the rubric.[^c1]

## Mechanism

The classical remedy for pairwise position bias is to swap the two responses. With several score options a swap does not work. The paper's alternative is a balanced permutation: a 5-point rubric is presented in 10 orderings, 5 forward cyclic rotations and 5 reverse ones. Each score then appears exactly twice in each position, so score identity is decoupled from position.[^c2] Aggregating the judge's choices over the orderings gives the marginal distribution over positions. A chi-square test against uniform then measures the bias.[^c3]

Measured on six open-weight judges over four datasets, the bias is statistically significant for nearly all judges. The direction is a property of the judge, not of the prompt layout. GPT-OSS-20B leans toward the first option, Gemma-3-27B and Qwen3.5-27B toward the last, and GPT-OSS-120B is near uniform.[^c4]

A second axis exists. When one prompt scores several criteria together, the order of the criteria itself shifts the scores.[^c5]

## Consequences

Permuting the options attenuates the bias. The gain in correlation with human ratings appears mainly for judges with strong bias, and a small number of random permutations suffices for most models.[^c6] The bias also propagates downstream: ordering the rubric alone flips the top-1 candidate on 15% to 41% of prompts. That affects best-of-N selection and rubric-as-reward training.[^c7]

My inference, not the paper's claim: a rubric whose score descriptions are fixed in ascending order mixes the judge's real preference with its positional prior. This cannot be separated without permuting.

## Limits

- The judges are open-weight models only.
- The datasets are MT-Bench, Vicuna-Bench, HANNA and SummEval. Human labels exist for only two of them.
- The smaller sets (n=320) have less power, so a few cells are not significant.[^c3]
- The mechanism is not explained. The paper measures where the bias points, not why.
- Whether more granular rubrics increase it is only touched on in the text and is not established here.

## Related

- [[mcq-answer-position-bias]] — the same positional skew when a model writes, rather than judges, options
- [[llm-judge-biases]] — the wider catalogue of judge biases this one joins
- [[llm-judge-score-instability]] — score variation of the same judge under surface changes

[^c1]: arxiv-2602-02219 — "show that rubric-based evaluation implicitly resembles a multiple-choice setting and therefore"
[^c2]: arxiv-2602-02219 — "This design ensures that every score"
[^c3]: arxiv-2602-02219 — "Every χ2 on"
[^c4]: arxiv-2602-02219 — "GPT-OSS-20B is more"
[^c5]: arxiv-2602-02219 — "the ordering of"
[^c6]: arxiv-2602-02219 — "are obtained primarily for models that exhibit"
[^c7]: arxiv-2602-02219 — "rubric ordering alone flips the top-1 candidate"
