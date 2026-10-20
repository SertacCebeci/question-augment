---
description: "Auditing and repairing a prompt (missing or conflicting values) through few targeted questions before code synthesis cut text-to-CAD error far more than a stronger coder alone (ProCAD)."
aliases: ["proactive clarification before code synthesis", "specification audit before generation", "ProCAD two-agent clarification"]
sources: ["arxiv-2602-03045"]
---
# Clarify-before-generate specification repair

Text-to-CAD systems usually treat the user prompt as a reliable specification. The ProCAD authors observe that fine-tuned coders "tend to reactively follow the user’s instructions and hallucinate dimensions when the text is ambiguous."[^c1] Their remedy splits the job in two: a clarifying agent audits the prompt, asks the user only about missing or conflicting dimensions, and emits a complete, self-consistent text specification; only then does a coding agent write the CadQuery program.[^c2] The repair happens upstream of generation, not by post-hoc execution feedback.

## Two defect types, built by perturbation

Ambiguity is simulated from verified specifications by an LLM, in two kinds: omitted key dimensions, and "inconsistent prompts that assign conflicting values to the same feature."[^c3] A perturbed prompt is kept only if it is demonstrably harmful: the coder does well on the original (Chamfer distance, CD, below 2e-4), badly on the perturbed one, and the CD ratio is large.[^c4] The result is a training set of 6,063 samples (test 2,469), about half ambiguous and half unambiguous, so the clarifier also learns not to ask when nothing is wrong (the abstract's "only when necessary").

## What was measured

- Input quality is a bottleneck: the authors conclude that "a key bottleneck also lies in the quality of the original" text descriptions, since the coder is strong enough when the specification is clear.[^c5]
- Headline: with the coder fixed, ProCAD cuts mean CD by 79.9% and invalidity from 4.8% to 0.9% against Claude Sonnet 4.5.[^c6] In the test table the same coder paired with Claude Sonnet 4.5 as clarifier gives mean CD 2.69 and 2.3% invalidity versus 0.63 and 0.9% with the trained clarifier (a 7B model, trained in under ten minutes). The tables show every clarifier, even weak ones, lowering invalidity versus the single-model run of the same base model (e.g. Qwen 7B 68.2% to about 4%).
- Interaction quality is scored separately: efficiency asks "whether the clarifier’s questions match the ground-truth questions without introducing" redundant ones, and resolution asks whether the clarified spec removes the ambiguity.[^c7] The trained clarifier scored efficiency about 0.97 against about 0.83-0.85 for Claude Sonnet 4.5 at similar resolution (about 0.93), so the gain is fewer, better-aimed questions rather than more questions. The authors summarise it as asking "only the most necessary, targeted questions."[^c8]
- Human-centered evaluation (Table 6) kept the ordering on efficiency and resolution (0.760/0.787 against 0.598/0.700 for Claude) and mean CD (1.28 against 9.72), with identical invalidity (12.2%) for both.

## Limits

- Ambiguity is synthetic, produced by one LLM and filtered by the same coder's failure, so the defects are those that break this coder; natural under-specification may differ.
- Users in the main tables are simulated by an LLM (GPT-5-mini; Claude Haiku for the out-of-distribution table); human evaluation is smaller and shows no invalidity gain.
- Efficiency and resolution are LLM-judged against a known ground-truth question set, which exists only because the defects were planted.
- One domain (CadQuery, DeepCAD shapes); whether a clarifier trained this way transfers to other generation tasks is not tested. The causal split between clarifier and coder gains is read from the tables, not isolated by a separate ablation I checked.

## Related

- [[underspecified-question-eager-answering]] — the failure this note addresses: models answer from an assumed reading instead of asking
- [[elicitation-burden-tradeoff]] — the cost side: questions asked versus gain
- [[sql-clause-gated-clarification]] — another code-generation setting where asking is gated on what is missing
- [[clarification-benchmarks]] — benchmarks for judging when and what to ask

[^c1]: arxiv-2602-03045 — "existing fine-tuned models tend to reactively follow the user’s instructions and hallucinate dimensions when the text is ambiguous."
[^c2]: arxiv-2602-03045 — "The clarifying agent first audits the"
[^c3]: arxiv-2602-03045 — "inconsistent prompts that assign conflicting values to the same feature."
[^c4]: arxiv-2602-03045 — "the ratio of the two Chamfer distances is at"
[^c5]: arxiv-2602-03045 — "that a key bottleneck also lies in the quality of the original"
[^c6]: arxiv-2602-03045 — "distance by 79.9% and lowering the invalidity ratio from 4.8% to 0.9%."
[^c7]: arxiv-2602-03045 — "whether the clarifier’s questions match the ground-truth questions without introducing"
[^c8]: arxiv-2602-03045 — "ProCAD-clarifier minimizes user intervention by asking only the most necessary, targeted questions,"
