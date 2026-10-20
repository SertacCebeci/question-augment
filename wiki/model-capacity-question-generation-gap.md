---
description: "A deployed legal-intake classifier's cheap LLM ensemble classifies well but writes low-quality follow-up questions; prompt engineering fails to close the gap, only a costlier model does."
aliases: ["active listening question quality", "FETCH question quality"]
sources: ["steenhuis-2026"]
---
# Model-capacity question-generation gap

> Classification and question generation are not the same difficulty for an
> LLM: an ensemble cheap enough to classify well is not cheap enough to ask
> well.

## Definition / Mechanism

FETCH, a deployed legal-intake classifier, generates candidate follow-up
questions with an ensemble of low-cost LLMs (GPT-5-nano, gemini-2.5-flash-lite,
mistral-small-7b), semantically merges them with a fourth low-cost model, and
uses the result to refine the classification of an applicant's legal problem.
Evaluated against expert-attorney and LLM-as-judge ratings on relevance and
readability, this low-cost setup's questions did not meet human evaluators'
standards, and two rounds of prompt engineering (readability-first merging,
then explicit glossing/substitution/redundancy rules and few-shot bad-question
examples) failed to close the gap: "while low-cost LLMs perform well at
classification tasks, generating high-quality plain-language questions in
this setting appears to require a more sophisticated and higher-cost model."[^c1]

Only replacing the low-cost ensemble member with GPT-5 — not further prompt
tuning — moved the outcome: "qualitative feedback from Oregon State Bar staff
suggested that changing one of the ensemble models from GPT-5-nano to GPT-5
improved readability, relevance, and classification behavior."[^c2]

The paper reads this as a task-capability asymmetry rather than a prompting
failure: "The detailed changes required in this experiment contrast to the
immediate improvement that ensemble techniques made in improving one-shot
classification accuracy in FETCH [28], suggesting that question generation is
a more complex task that requires more explicit guidance to the model, as
well as a more capable LLM."[^c3]

## Why it matters

For stall 2 (which axis first, and with what question), this is a boundary
condition on cost-optimized elicitation pipelines: a system tuned for cheap,
accurate classification cannot assume the same cost budget suffices for the
question that elicits the next constraint. The two subtasks — deciding what
information is missing, and phrasing a plain-language question that gets it
— appear to have different minimum model capacities.

## Limits

- The claim rests on one deployed system (FETCH) and one domain (US legal
  intake); "low-cost" and "high-cost" are relative to the specific model
  generations tested (GPT-5-nano/mini/GPT-5) in 2026, not a general capacity
  threshold.
- The improvement from swapping in GPT-5 is reported as qualitative staff
  feedback ("suggested that..."), not a controlled rubric score reported
  alongside the prompt-engineering experiments' numbers — the paper itself
  frames prior experiments' scores as evidence, this one as anecdote.
- Two confounds are not separated: the model swap changed both question
  generation and semantic merging simultaneously, so the source of the
  improvement (generation quality vs. merge quality) is not isolated.

## Related

[[on-demand-follow-up-generation]] · Selection

[^c1]: steenhuis-2026 — "while low-cost LLMs perform well at classification tasks, generating high-quality plain-language questions in this setting appears to require a more sophisticated and higher-cost model"
[^c2]: steenhuis-2026 — "qualitative feedback from Oregon State Bar staff suggested that changing one of the ensemble models from GPT-5-nano to GPT-5 improved readability, relevance, and classification behavior."
[^c3]: steenhuis-2026 — "The detailed changes required in this experiment contrast to the immediate improvement that ensemble techniques made in improving one-shot classification accuracy in FETCH [28], suggesting that question generation is a more complex task that requires more explicit guidance to the model, as well as a more capable LLM."
