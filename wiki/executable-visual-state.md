---
description: "Executable visual states: the model writes code that draws its working diagram, runs it, and revises it next turn, keeping geometric constraints explicit where text-only chains drift."
aliases: ["executable visual construction", "code-rendered diagram as reasoning state", "executable and revisable visual states"]
sources: ["arxiv-2512-24297"]
---
# Executable visual states

A reasoning model can carry its intermediate structure as a diagram that is computed rather than only described. At each step the policy either writes text or emits a code snippet. A code snippet "is executed by a sandboxed interpreter"[^c1], which returns text feedback and, when the code draws something, a rendered figure. That figure is appended to the context and read again at the next step. The paper calls these "figures as explicit, stateful feedback"[^c2], and says that "By representing diagrams as executable and reproducible states," the model gets precise, controllable visual feedback across the reasoning process.[^c3]

What does the work is revision. A diagram that exists as code can be changed by changing the code and re-rendering, so a wrong placement in one turn is corrected by redrawing it, not by re-deriving every algebraic consequence of that placement. My reading: this is why the approach is aimed at problems where a constraint such as tangency or a fixed angle has to hold across several steps, which a text chain has to re-carry symbolically each time.

The paper compares this with the two other ways a model can use images. Unconstrained image generation is not grounded: "Since image generation is not grounded in executable constraints, even small spatial inconsistencies can propagate across reasoning"[^c4]. Predefined tools such as zoom or crop are controllable, since "their visual operations are deterministic and explicitly defined"[^c5], but "Consequently, they lack the ability to" construct a diagram that is not already in the input.[^c6] The executable route is the only one of the three that both builds a new figure and keeps it checkable.

A static diagram is not enough. Two baselines injected diagrams generated from the problem text as fixed context, and the paper reports that "passively injected visual inputs, without executable construction or feedback integration, fail" to act as reliable intermediate states.[^c7] Such images "neither enforce global constraints nor provide actionable feedback for subsequent reasoning steps."[^c8] The feature that matters, on this evidence, is the closed loop of draw, execute, read back, not the presence of a picture. The paper's own ablation agrees. Removing visual feedback while keeping multi-turn code execution still lowers results: "Both ablations lead to performance degradation compared to the full" system.[^c9]

On the paper's own evaluation, a Qwen3-VL-32B-Instruct policy trained with reinforcement learning gains "base model by 13.12% on AIME 2025 and" over the base model, with a further 11.00% reported on BeyondAIME.[^c10]

## Limits

- Evaluation is on mathematical benchmarks only. The paper says "Our evaluation focuses on mathematical reasoning benchmarks"[^c11], and extension to scientific or other domains is left open. The geometry example is illustrative; the text reports no measure of whether the drawn figure matches the question's constraints.
- The method costs more: "additional computational cost due to multi-turn reasoning and code execution."[^c12] The paper gives a three-round cap and does not report the cost per solved problem against text-only sampling.
- The benefit is task-dependent. The paper concedes that "or purely symbolic reasoning may see less benefit"[^c13], and that "More precise identification and characterization of such task regimes" is still open.[^c14]
- One base model and one training set. The ablations remove one component each from a single trained system; they do not show that the gain would survive another base model or a longer interaction budget.
- The gains are single reported figures. The parts of the text read give no variance across training seeds or runs, so how stable the 13.12% is cannot be judged from it.

## Related

- [[suitability-gated-visual-reward]] — the training reward that decides when this kind of drawing is worth invoking.
- [[sufficiency-gated-imagination]] — also decides when to add visual evidence, but for rendered views of a scene, gated at inference by the policy's own sufficiency judgement.
- [[tool-type-confidence-dichotomy]] — code interpreters as verification tools; relevant to what an executed result does to an agent's confidence, which this work does not measure.

[^c1]: arxiv-2512-24297 — "When a code action is emitted, it is executed by a sandboxed interpreter"
[^c2]: arxiv-2512-24297 — "figures as explicit, stateful feedback"
[^c3]: arxiv-2512-24297 — "By representing diagrams as executable and reproducible states,"
[^c4]: arxiv-2512-24297 — "grounded in executable constraints, even small spatial inconsistencies can propagate across reasoning"
[^c5]: arxiv-2512-24297 — "provide strong controllability, as their visual operations are deterministic and explicitly defined."
[^c6]: arxiv-2512-24297 — "Consequently, they lack the ability to"
[^c7]: arxiv-2512-24297 — "passively injected visual inputs, without executable construction or feedback integration, fail"
[^c8]: arxiv-2512-24297 — "neither enforce global constraints nor provide actionable feedback for subsequent reasoning steps."
[^c9]: arxiv-2512-24297 — "Both ablations lead to performance degradation compared to the full"
[^c10]: arxiv-2512-24297 — "base model by 13.12% on AIME 2025 and"
[^c11]: arxiv-2512-24297 — "Our evaluation focuses on mathematical reasoning benchmarks"
[^c12]: arxiv-2512-24297 — "additional computational cost due to multi-turn reasoning and code execution."
[^c13]: arxiv-2512-24297 — "or purely symbolic reasoning may see less benefit"
[^c14]: arxiv-2512-24297 — "More precise identification and characterization of such task regimes"
