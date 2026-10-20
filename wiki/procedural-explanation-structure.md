---
description: "A procedural explanation carries three inferential structures, causal transitions, teleological linkage and decomposition; fluent prose can hide their absence, and each can be rated apart."
aliases: ["inferential structure of procedural explanation", "causal teleological compositional dimensions", "procedural inferencing", "procedural skill explanation structure"]
sources: ["arxiv-2511-20942"]
---
# Procedural explanation structure

An answer to a how-question about a skill can be a list of correct steps and still miss what an instructor teaches. The authors say an explanation must convey "the causal, goal-directed, and compositional logic behind them".[^c1] They name three structures for that logic, and they make each one explicit in a formal model of the skill.

The first is causal transitions: what must hold before a move can follow. In their finite-state encoding a move between states is allowed only under a safety predicate, and "if a guard fails, control routes to the Failure state".[^c2] The second is teleological linkage: why a step serves the goal. Completion is defined by reaching the "goal state RG S3(SafeConfig) for the parent ReturnGuard goal", not by finishing some steps.[^c3] The third is decomposition: how the goal breaks into parts. Each state "names the operation or subgoal it invokes".[^c4]

The three can come apart. An answer can state the guards and omit the goal they serve, or name the subgoals and never say why a move is legal now. The authors' baseline shows the second case. Generic answers from a prose-only model are "fluent yet generic: they gesture at what to do, but not" say why a move is legal, how it advances the goal, or which operation is run.[^c5]

The paper scores each structure on a three-level scale. The middle level, "Implicit / Generic: Present but vague or not", sits between absent and explicit.[^c6] So a structure is a matter of degree, and an answer can be explicit on one dimension and generic on another. The authors' concern is that language models "often produce fluent yet shallow responses that miss this" structure.[^c7] Fluency is what hides the absence: a reader sees a coherent explanation and does not see that the guard or the goal is missing.

The measured effect is on the rated structure of correct answers. Over 80 responses, four systems and 20 questions, "experts rated Ivy+TMKStructured highest on every dimension",[^c8] and "the largest margin appears on problem decomposition",[^c9] where the structured system scored 1.5 against 1.3 for the looser model and 0.6 to 0.7 for the two unstructured baselines. Independent raters, scored against the expert's expected dimensions, agreed most with the structured system; teleology reached "teleology F1 = 0.843, Acc = 0.792".[^c10]

My reading, not the paper's: the first structure is the kind of thing the causal model of explanation covers, since it asks for the cause of a step's legality (see [[causal-model-of-explanation]]). The second is a goal-directed why, which that model does not supply on its own. The paper's why-questions are about each step, not about a fact against a foil, so [[contrastive-explanation]] is a different axis that the paper does not vary.

## Limits

- The dataset is small: "dataset is modest (5 questions per system over four skills)".[^c11]
- Correctness rests on one expert per skill: "one domain expert per skill, so inter-rater reliability on correctness is not measured".[^c12]
- The expert who rated structure built the model being rated: "a domain expert who constructed the TMK model".[^c13] The structural scores are also "computed only over fully correct responses",[^c14] so they say nothing about the wrong or partial answers.
- The independent raters are described as "familiar with TMK modeling but not involved in designing" the model.[^c15] They are developers, not the novice learners the paper uses as its label, so the novice-validity claim is weaker than its name suggests.
- The paper measures explanation quality, not learning: "quality, not learning outcomes, so effects on transfer or student performance are out of scope".[^c16]
- The three structures are the authors' decomposition. The text does not argue that they are complete, or that a procedure needs no other structure. My reading: a different skill may need a structure the three do not name.
- Structure ratings rose while correctness did not rise over the looser model. The structure is a separate property from being right, and this note does not show that it helps a learner.

## Related

- [[symbolic-scaffold-generation]] — the design that the paper uses to produce these three structures
- [[causal-model-of-explanation]] — explanation as giving causes; covers the causal-transition structure, not the goal-directed one (my reading)
- [[contrastive-explanation]] — a different axis of why-questions, fact against foil, which the paper does not vary
- [[over-reasoning-in-explanations]] — excess explanation can bury the fault a learner needs; a structure-rich answer can still be too long (my reading)

[^c1]: arxiv-2511-20942 — "the causal, goal-directed, and compositional logic behind them"
[^c2]: arxiv-2511-20942 — "if a guard fails, control routes to the Failure state"
[^c3]: arxiv-2511-20942 — "goal state RG S3(SafeConfig) for the parent ReturnGuard goal"
[^c4]: arxiv-2511-20942 — "names the operation or subgoal it invokes"
[^c5]: arxiv-2511-20942 — "they gesture at what to do, but not"
[^c6]: arxiv-2511-20942 — "Implicit / Generic: Present but vague or not"
[^c7]: arxiv-2511-20942 — "often produce fluent yet shallow responses that miss this"
[^c8]: arxiv-2511-20942 — "experts rated Ivy+TMKStructured highest on every dimension"
[^c9]: arxiv-2511-20942 — "The largest margin appears on problem decomposition"
[^c10]: arxiv-2511-20942 — "teleology F1 = 0.843, Acc = 0.792"
[^c11]: arxiv-2511-20942 — "dataset is modest (5 questions per system over four skills)"
[^c12]: arxiv-2511-20942 — "one domain expert per skill, so inter-rater reliability on correctness is not measured"
[^c13]: arxiv-2511-20942 — "a domain expert who constructed the TMK model"
[^c14]: arxiv-2511-20942 — "computed only over fully correct responses"
[^c15]: arxiv-2511-20942 — "familiar with TMK modeling but not involved in designing"
[^c16]: arxiv-2511-20942 — "quality, not learning outcomes, so effects on transfer or student performance are out of scope"
