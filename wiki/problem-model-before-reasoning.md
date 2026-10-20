---
description: "Writing a problem's entities, state variables, actions and constraints out before reasoning, so the answer is constrained to that model rather than to implicit latent state."
aliases: ["Model-First Reasoning", "MFR", "explicit problem representation", "explicit problem modeling", "representational commitment"]
sources: ["arxiv-2512-14474"]
---
# Problem model before reasoning

Model-First Reasoning (MFR) splits one prompt into two phases. In the first, the model is told to "explicitly define the problem model" by listing entities, state variables, possible actions with preconditions and effects, and constraints, and it is told not to propose a solution yet.[^c1] In the second, it plans using only the model it has just written. The paper calls the first phase "a representational commitment that constrains all downstream reasoning."[^c2] The model is therefore not a scratch step that reasoning may ignore: actions "must respect stated preconditions," state transitions must follow the stated effects, and constraints must hold at every step.[^c3] Because the representation is written out, a broken step shows up as a mismatch between plan and model: "violations become visible and diagnosable."[^c4]

The mechanism rests on a diagnosis. The authors locate many planning failures not in inference but in the representation: they "arise not from deficiencies in reasoning itself, but from the absence of an explicit problem representation."[^c5] Chain-of-thought and ReAct leave the problem's structure to whatever the model keeps latent. In the ReAct case, "state tracking remains informal and distributed across free-form text."[^c6] Classical planning avoids this by fixing a domain model before planning: "Classical AI planning systems formalize this principle through explicit" domain models, the PDDL tradition.[^c7] MFR asks the LLM to produce an analogue in natural language, semi-structured text or pseudo-formal notation, and states that it does not require "a fixed formalism."[^c8] The transfer is the part that survives: the structure is written before any solving, and the solving is conditioned on it. What does not survive is the formal guarantee, since the model is only as good as the LLM's own modeling.

The method needs no training. It "does not require architectural changes," and it needs no "external symbolic solvers, or additional training"; it is only a prompt design.[^c9] Its appeal for the wiki is that it turns a hidden step into a written object that can be inspected, which is the answerer-side move of making a commitment visible before it is acted on.

## What the evidence is

The comparison is qualitative. CoT, ReAct and MFR were run on hand-picked planning tasks (medication scheduling, route planning, resource allocation, logic puzzles, procedural synthesis), and "selected examples from each task were evaluated qualitatively by the authors."[^c10] The headline result is that "Reasoning consistently exhibits lower constraint violations and implicit assumptions while maintaining higher structural clarity."[^c11] The ratings are ordinal labels (Low, Medium, Frequent, Rare) applied to these examples. The abstract also says "Ablation studies confirm that separating modeling from reasoning is critical to these gains."[^c12] The body that was read reports no ablation: a search of the full text finds that sentence and no ablation section (my reading). So the causal part, that the separation and not the longer, more structured prompt is the cause, rests on the authors' assertion.

## Limits

- No benchmark. "The evaluation is based on selected task examples rather than exhaustive benchmarking."[^c13] The authors add that "Qualitative ratings provide conservative assessments but may not capture fine-grained performance differences."[^c14]
- Dependence on the model's own modeling. "Effectiveness depends on accurate model construction by the LLM; errors in modeling directly affect plan quality."[^c15] A wrong entity or missing constraint in the model is carried into the plan with the same confidence as a right one.
- Not a verifier. "While MFR reduces risk, it does not guarantee correctness."[^c16]
- Cost is asserted, not measured. Building the model lengthens prompts and outputs; the authors argue the trade-off is offset by better correctness, but the text read reports no number for either side.[^c17]
- Scope. "The benefits of MFR are most apparent in structured," constraint-driven planning.[^c18] Nothing in the text tests open questions, dialogue, or cases where the missing piece is information the user holds and the model does not.

## Relation to asking

The paper never has the model ask the user about a missing entity or constraint; the gap it closes is an "unstated assumption" the model would otherwise fill silently. My inference, not the paper's: a model with explicit slots for entities, state and constraints makes a missing slot visible, and a visible empty slot is exactly what a question could fill. The paper does not test that step, so it belongs to the wiki's question side only as a conjecture.

## Related

- [[information-need-reification]] — the same move (write the reading out as an inspectable object before acting), but there the object is executable and the user edits it; MFR's model is a prompt-internal scaffold that no one edits.
- [[interpretation-externalization]] — exposes a reading after the system has committed to it; MFR fixes the representation before any solving begins.
- [[reference-world-model]] — also treats hallucination as a modeling problem relative to an explicit reference; the MFR paper's claim that "many observed LLM planning failures are fundamentally representational rather than inferential" is the same diagnosis.[^c19]
- [[implicit-to-explicit-restatement]] — restating an implicit query in explicit terms before a grounding step; a measured instance of the same step in a perception task.

[^c1]: arxiv-2512-14474 — "explicitly define the problem model"
[^c2]: arxiv-2512-14474 — "a representational commitment that constrains all downstream reasoning."
[^c3]: arxiv-2512-14474 — "Actions must respect stated preconditions."
[^c4]: arxiv-2512-14474 — "violations become visible and diagnosable."
[^c5]: arxiv-2512-14474 — "the absence of an explicit problem representation"
[^c6]: arxiv-2512-14474 — "state tracking remains informal and distributed across free-form text"
[^c7]: arxiv-2512-14474 — "Classical AI planning systems formalize this principle through explicit"
[^c8]: arxiv-2512-14474 — "We do not require a fixed formalism"
[^c9]: arxiv-2512-14474 — "external symbolic solvers, or additional training"
[^c10]: arxiv-2512-14474 — "evaluated qualitatively by the authors."
[^c11]: arxiv-2512-14474 — "Reasoning consistently exhibits lower constraint violations and implicit assumptions while maintaining higher structural clarity."
[^c12]: arxiv-2512-14474 — "Ablation studies confirm that separating modeling from reasoning is critical to these gains."
[^c13]: arxiv-2512-14474 — "The evaluation is based on selected task examples rather than exhaustive benchmarking."
[^c14]: arxiv-2512-14474 — "Qualitative ratings provide conservative assessments but may not capture fine-grained performance differences."
[^c15]: arxiv-2512-14474 — "errors in modeling directly affect plan quality"
[^c16]: arxiv-2512-14474 — "it does not guarantee correctness."
[^c17]: arxiv-2512-14474 — "While MFR increases prompt and output size"
[^c18]: arxiv-2512-14474 — "The benefits of MFR are most apparent in structured,"
[^c19]: arxiv-2512-14474 — "We conclude that many observed LLM planning failures are fundamentally representational rather than inferential"
