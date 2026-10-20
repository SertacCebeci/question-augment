---
description: "In self-play question generation, a within-batch surface-similarity penalty gives illusory diversity: questions repeat across iterations and differ in wording but not in required reasoning skill."
aliases: ["Diversity Illusion", "local diversity illusion", "surface diversity illusion", "memory-augmented penalty", "skill-aware measurement"]
sources: ["arxiv-2602-13103"]
---
# Skill-level diversity illusion

A question generator can look diverse by its own penalty while feeding the solver the same few reasoning skills. The work names two ways this happens in challenger-solver self-play and a fix for each.

## Mechanism

In the R-Zero setup a Challenger writes questions, a Solver answers them, and the Challenger is rewarded for questions at the edge of the Solver's ability, minus a repetition penalty.[^c1]

**Local scope.** The penalty is computed only on the current batch, since the Challenger cannot see earlier questions. Minimizing it only makes questions distinct inside the batch, and they may still resemble high-reward questions from earlier iterations. The authors call this the Local Diversity Illusion: global repetition rises despite local constraints.[^c2]

**Surface metric.** The penalty uses BLEU, a token-space measure. What matters for the Solver is the reasoning skill a question requires. The map from question to skill is many-to-one, so two questions can have low BLEU yet near-identical skills. This is the Surface Diversity Illusion.[^c3]

**Fix 1, Memory-Augmented Penalty (MAP).** A memory bank stores embeddings of all valid questions from earlier iterations, where valid means passing the uncertainty filter. The penalty combines the maximum similarity to any stored item (point-to-point collision) with the mean similarity to the whole bank (point-to-region collision, a repulsion from the "center of gravity" of past questions). Each term is active only above a tolerance, and the two are weighted by gamma = 0.5.[^c4] Because exploration shifts the question distribution, the Solver is also trained with replay of historical question-answer pairs at ratio 0.3.[^c5]

**Fix 2, Skill-Aware Measurement (SAM).** A code model translates each question into a canonical solver program, with the procedure extracted and concrete entities anonymized. A code encoder embeds the program, and similarity is computed there. "Chickens/rabbits" and "cars/wheels" problems land on highly similar code even if the code is imperfect.[^c6] The same similarity feeds both the within-batch penalty and MAP.

## Measured effect

On Qwen3-4B-Base, removing MAP gives the largest ablation drop (52.59 to 49.62). Max and mean terms each cost about 2.0, and dropping both costs 2.71. Removing replay costs 1.41.[^c7] Disabling SAM costs 2.09, and removing either the abstraction or the embedding step costs 1.80 and 1.54.[^c8] On Qwen3-4B-Base the overall average rises from 27.10 (base) to 36.68, +2.04 over R-Zero.[^c9]

## Limits

- Evidence is from one family of self-play systems (Qwen3 base models, math-heavy training, seven math and three general benchmarks), not from human-posed questions.
- Skill is proxied by generated Python code from a 7B coder model; the paper concedes the code can be imperfect. Skills that do not reduce to a program (open-ended or interpretive questions) are not covered. This is my inference, not tested.
- The ablation drops are single-configuration differences; seeds and variance were not examined in the slices I read.
- The illusion is diagnosed from the penalty's design and from trend plots; I did not read a direct measure of skill diversity independent of SAM.

## Related

- [[questioning-diversity]] — embedding-space diversity of a question set; SAM argues the embedding should be of the solution procedure, not the wording
- [[curriculum-collapse]] — a related failure of self-generated curricula
- [[learnability-posterior-curriculum]] — another curriculum for self-play question selection
- [[hierarchical-error-cause-memory]] — another memory-based self-evolution method compared against R-Zero

[^c1]: arxiv-2602-13103 — "The Challenger Cθt is trained to generate questions that lie in the Solver’s “zone of proximal development”, where problems"
[^c2]: arxiv-2602-13103 — "This limitation leads to the Local Diversity"
[^c3]: arxiv-2602-13103 — "This mapping is generally many-to-one: many superficially different questions"
[^c4]: arxiv-2602-13103 — "Pmax prevents point-to-point collision, Pmean prevents point-to-region collision."
[^c5]: arxiv-2602-13103 — "ensuring these historical samples constitute a"
[^c6]: arxiv-2602-13103 — "Even when the generated code is imperfect, it typically preserves the dependency structure and operation"
[^c7]: arxiv-2602-13103 — "Removing MAP causes the largest drop"
[^c8]: arxiv-2602-13103 — "Disabling SAM degrades performance"
[^c9]: arxiv-2602-13103 — "R-Diverse raises Overall AVG from 27.10"
