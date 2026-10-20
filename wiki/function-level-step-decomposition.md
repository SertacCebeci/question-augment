---
description: "Code has no natural reasoning steps, so a process reward model can treat each generated function as one step, the boundary induced by a prompt rather than found in the code."
aliases: ["Chain-of-Function", "function-as-step decomposition", "function-granularity reasoning steps", "code step decomposition for PRMs"]
sources: ["arxiv-2512-15000"]
---
# Function-level step decomposition

A process reward model (PRM) scores a partial solution, so it needs a unit called a step. In mathematical chain-of-thought the unit is supplied by the language: reasoning "naturally decomposes into steps." Generated code does not supply one. The work names two existing answers and why it finds them weak. Using a line of code as a step "significantly increases computation cost due to too many" steps.[^c1] Defining steps in a natural-language plan outside the code "ignor[es] inherent reasoning process in programming code itself."[^c2]

The alternative makes the code carry its own steps. A Chain-of-Function prompt asks the generator to put high-level functions first and helper functions after, to avoid nested functions, and to write a docstring in each. The aim is "producing independent code blocks whose logic can be isolated and encapsulated into separate functions."[^c3] Each function then "can [be treated] as a coherent reasoning step," and the PRM is trained and applied as it would be on a mathematical chain.[^c4] At test time the per-step scores are averaged over a candidate's steps, and the highest-scoring candidate is kept.[^c5]

The mechanism has two parts. The prompt induces a structure in which function boundaries mark where a reasoning unit ends; the scorer then uses those boundaries as its steps. So the step unit is a property of what was generated, not of the programming language. The authors argue this gives "clear intermediate reasoning states for PRM evaluation."[^c6]

What was measured. On LiveCodeBench, with o4-mini-high as the generator producing four candidates per problem, the function-step PRM reached 80.9 pass@1 overall. The strongest listed leaderboard model scored 77.1, which the text states as a 3.8-point gap.[^c7] The output-level comparison, an outcome reward model (ORM) on the same generator, scored 79.4 in the table as extracted. The authors attribute the gap over ORM to "decomposing code generation into intermediate steps and assigning rewards at a finer granularity."[^c8] That is their reading of the comparison, not a separate test of granularity.

## Limits

- No run compares function steps with line steps, or with whole-solution scoring, under the same PRM training. The ORM comparison changes the scoring target and the training data together, so the gain cannot be assigned to granularity alone.
- The step boundaries exist only where the generator obeys the prompt. Code that is one function, or that comes from a different prompt, has one step or steps of unknown shape. This is my inference from the method, not something the paper tests.
- One benchmark, one generator (o4-mini-high), and one PRM (a 3B Qwen coder with its head replaced for step scores). The test split is 131 problems "published after 2025-02-01 as the test split."[^c9] The PRM's training trajectories were produced by a different model, "Qwen3Coder-30B-A3B … to generate both Chainof-Function (CoF) trajectories for PRM training."[^c10] Transfer to other generators is untested.
- The reported 80.9 is one run per configuration, with no variance or interval in the text.
- The mathematical comparison is by analogy. The paper argues that the PRM machinery transfers, but does not test a math PRM built on the same step scheme.
- A step-level score can still reward plausible steps. This work does not test for that; see [[process-reward-model-hackability]].

## Related

- [[process-reward-model-hackability]] — step-level scores can track fluency rather than logic; a function boundary does not by itself rule that out.
- [[meta-label-correction]] — the noisy intermediate labels that the function steps receive, and how a clean final test corrects them.
- [[answerability-delta-process-reward]] — another step-level reward, assigned per search turn without an oracle.
- [[requested-span-granularity-gradient]] — granularity of the code task itself, a different unit from the reasoning step.

[^c1]: arxiv-2512-15000 — "significantly increases computation cost due to too many"
[^c2]: arxiv-2512-15000 — "instead of in the generated code, ignoring inherent reasoning process in programming code itself"
[^c3]: arxiv-2512-15000 — "producing independent code blocks whose logic can be isolated and encapsulated into separate functions."
[^c4]: arxiv-2512-15000 — "can treat each function as a coherent reasoning step"
[^c5]: arxiv-2512-15000 — "aggregation over the per-step reward scores produced by"
[^c6]: arxiv-2512-15000 — "This structured decomposition not only provides clear intermediate reasoning states for PRM evaluation"
[^c7]: arxiv-2512-15000 — "outperforms the strongest baseline, o4-mini-high, by 3.8 points"
[^c8]: arxiv-2512-15000 — "decomposing code generation into intermediate steps and assigning rewards at a finer granularity"
[^c9]: arxiv-2512-15000 — "published after 2025-02-01 as the test split"
[^c10]: arxiv-2512-15000 — "to generate both Chainof-Function (CoF) trajectories for PRM training"
