---
description: "Asked which given condition a geometry proof never uses, multimodal models are scored on identifying unused premises, and that score tracks their final solving accuracy."
aliases: ["irrelevant premise filtering", "unused premise detection", "redundant premise filtering", "unnecessary premise identification"]
sources: ["arxiv-2512-24119"]
---
# Irrelevant premise filtering

A problem states a set of given conditions, and only some of them enter the reasoning that reaches the answer. GeoBench treats the ability to separate the two as a sub-skill to be measured on its own. For each problem, the premises used on the reasoning path form a subset S0 of the full premise set P, and the rest, P minus S0, is what a filter must find. The authors "systematically investigate the capability of MLLMs to filter out redundant premises and extract semantically relevant information."[^c1] The item is multiple choice: the correct option is a premise outside S0, and the distractors are premises from S0, so a model that simply picks a stated condition is wrong whenever that condition is load-bearing.[^c2] Problems are kept only where at least one premise is unused and at least three are used.

The mechanism the test isolates is the converse of solving. A solver has to choose which conditions to chain; a filter has to say which ones the chain never touches. A solver that treats every given condition as needed carries the unused ones into its proof, and the paper's error analysis describes models that "introduced hallucinated conditions" beyond what the problem supplies.[^c3]

What the paper measures about it is its relation to solving. Across MLLMs, each of the six sub-tasks is correlated (Spearman) with final-answer accuracy on the full benchmark. The first six tasks all correlate positively, and irrelevant premise filtering is one of the three strongest correlates, with sub-goal decomposition and theorem selection.[^c4] The abstract states the same result as a finding: "premise filtering critically influence final problem-solving accuracy."[^c5] The authors read the correlation as confirming that the three abilities "significantly influence" geometric problem-solving.[^c6] On out-of-distribution data (GeoQA and Geometry3K), the same task again sits among the stronger correlates, which the authors take as evidence that the benchmark's signal is not overfit to answer patterns.[^c7]

## Limits

- **A correlation across models, not an intervention.** The Spearman coefficients relate each task's score to solving score across models. They do not show that training or prompting for premise filtering raises solving accuracy; the paper does not test that.
- **The distractors are on-path premises.** Wrong options are drawn from S0, so the task asks for discrimination among conditions the solution actually uses. It says nothing about robustness to unrelated clutter, which is a different test (see [[distractor-similarity-reasoning-inflation]]).
- **"Unused" is relative to one reasoning graph.** The problems come from a symbolic generator (TrustGeoGen) with a single reasoning graph per problem. A premise marked unused is unused in that graph; another valid proof might use it. This is my inference from the construction, not a point the paper raises.
- **Synthetic, not textbook, geometry.** The items are generated and formally verified; whether the same ranking holds on human-written problems is not established by this text.
- **One question form.** The probe is a single "which premise is unnecessary" multiple-choice question. Other ways of asking about relevance are not tested here.

## Related

- [[goal-refinement-graph]] — KAOS's pertinence check, that a requirement must be used in some goal's proof, is the same usage test applied to a specification; this task measures it in a model.
- [[backward-chaining-subgoal-decomposition]] — the sibling sub-skill the same paper finds among the strongest correlates; it asks which intermediate conditions a conclusion needs, where this note asks which given conditions are not needed.
- [[distractor-similarity-reasoning-inflation]] — the converse harm: irrelevant context that resembles the question degrades reasoning, whereas here the premise is part of the problem and the task is to discard it.
- [[anchored-distractor-taxonomy-math-problems]] — distractors anchored to a problem's own entities, a closely related construction for what makes an extra condition tempting.

[^c1]: arxiv-2512-24119 — "We systematically investigate the capability of MLLMs to filter out redundant"
[^c2]: arxiv-2512-24119 — "the distractor set comprises three randomly selected premises"
[^c3]: arxiv-2512-24119 — "introduced hallucinated conditions"
[^c4]: arxiv-2512-24119 — "Among them, task I.P.F., S.D., and T.S. show the strongest correlations"
[^c5]: arxiv-2512-24119 — "premise filtering critically influence final problem-solving accuracy"
[^c6]: arxiv-2512-24119 — "confirms that Sub-Goal Decomposition, Irrelevant Premise Filtering, and Theorem Selection abilities"
[^c7]: arxiv-2512-24119 — "task S.D. and T.S. exhibit the strongest correlations, followed by I.P.F."
