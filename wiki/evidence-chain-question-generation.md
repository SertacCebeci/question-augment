---
description: "Making a question-writer build an explicit cross-document evidence chain before writing the question cut pseudo multi-hop questions and raised true multi-hop yield from 24% to 46% (79% trained)."
aliases: ["Evidence-Chain Generator", "ECG", "pseudo multi-hop avoidance"]
sources: ["doi-10-48550-arxiv-2608-01822"]
---
# Evidence-chain question generation

A model that is told to write a multi-hop question often writes one answerable from a single document: it either stays near the seed and asks a surface fact, or it visits related documents but never encodes their links in the question.[^c1] Evidence-chain generation turns proposing into explicit chain construction. From a seed document the proposer repeatedly selects a salient entity, searches for a connected document, identifies a new entity or fact and extends the chain; the question is then derived from the full chain with requirements of full-chain necessity and no single-document answer.[^c2]

Candidates are then filtered before any solver sees them: too few search or open actions, a chain with fewer than two evidence items, a validity check by a verifier, and removal of questions the verifier answers without tools.[^c3]

Measured on 1,000 seed documents (10 tasks each, judged by a GLM-5 judge), adding the chain prompt to the base model raised true multi-hop tasks from 24.2% to 45.6% and cut invalid tasks from 28.7% to 15.8%; after self-play training, true multi-hop reached 78.6% and pseudo multi-hop fell to 15.0%.[^c4]

## Limits

The labels come from a single LLM judge, not humans. The setting is a local search environment with seed documents, and the gain is shown for one backbone (Qwen3.5-9B). How much of the downstream accuracy gain comes from the chain alone, versus the filters and rewards used with it, is only partly separated by the paper's ablation. Whether the same chain-first discipline helps a human or a model ask clarifying questions is my inference, untested here.

## Related

- [[self-answer-driven-search-depth]] — another way to define how much search a question needs
- [[pretraining-grounded-rubric-self-play]] — self-play where the generated task is anchored in source material

[^c1]: doi-10-48550-arxiv-2608-01822 — "the Proposer stays close to the seed, searching for surface-level facts and asking a question answerable from the seed alone."
[^c2]: doi-10-48550-arxiv-2608-01822 — "The question is then generated with explicit requirements for full-chain necessity and"
[^c3]: doi-10-48550-arxiv-2608-01822 — "Parametric-knowledge filter: removes questions the"
[^c4]: doi-10-48550-arxiv-2608-01822 — "adding ECG to the base model increases"
