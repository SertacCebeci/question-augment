---
description: "A deterministic rule set over a semantic layer and physical catalog decides whether an analytics agent should answer, clarify, abstain or refuse, instead of letting the model judge its own situation."
aliases: ["rule-gated behavior gate", "deterministic behavior gate", "the model proposes rules dispose"]
sources: ["lee-2026-business", "arxiv-2512-22258"]
---
# Rule-gated behavior gate

> The agent never asks the model what to do next; it asks the model two
> narrow, checkable sub-questions and decides ANSWER / CLARIFY / ABSTAIN /
> REFUSE itself, from a semantic layer and a physical catalog.

## Definition / Mechanism

Lee (2026) builds QueryProof around a design
premise stated from a baseline failure: "A 7B model asked to judge its
own situation does it badly... The agent therefore never asks the model
what to do. It asks two narrow, checkable questions, which metric a
phrase means and what SQL computes it, and makes every behavioural
decision itself against the semantic layer and the physical catalog."[^c1]

The behavior decision is a single ordered rule set, checked before or
after model calls but never delegated to one: "[[abstention|Abstention]] fires when the
requested period lies outside warehouse coverage, when a filter literal
is absent from a closed dimension domain, or when a requested concept has
no metric, dimension or column. Clarification fires when a phrase matches
two or more defined metrics and the question does not pin the choice, or
when it matches only concepts the semantic layer leaves undefined."[^c2]

Before any answer can be returned it passes two further deterministic
gates: static validation against the parsed SQL (no DML/DDL, no unknown
tables/columns), then post-execution verification of the result itself.
Both directions of this verification layer were measured rather than
assumed: "Run over 140 golden SQL programs, all known to be correct, it
produced 0 false rejections... In the other direction the checks are
demonstrably incomplete. 14 of 86 answers that passed them on development
were wrong, a false-clean rate of 0.163, and 8 of 24 on validation, or
0.333."[^c3]

## Why it matters

On 80 frozen test tasks, evaluated once under a pre-registered protocol,
this gate lifted business-answer correctness well past a larger
direct-prompted model at lower cost: "QueryProof outperforms a
direct-prompted 32B baseline by +0.237 [+0.112, +0.375] Business Truth
Rate at 71.0% lower cost per correct answer."[^c4]

The gain is attributed to the deterministic gate rather than to the
routing/escalation machinery layered on top of it: "Removing the routing
layer changes little (0.562 against 0.537), so the result does not
depend on escalation."[^c5]

The same division of labour shows up at the level of a label rather than a behaviour. Logic Sketch Prompting (LSP) "separates learned pattern detection from deterministic decision logic": a set of binary checks fills typed variables, and a fixed validator maps the final variable state to the output.[^c8] The benchmarked arm, though, was a prompt rather than code. The model "receives a compact, rule-structured checklist consisting of five binary questions," and the rule that turns the answers into a label is stated in that same prompt, so the model is the one applying it.[^c9] On adverse-drug-event classification with three open-weight models, this variant is reported to reach the highest accuracy across both tasks.[^c10] My reading, not the paper's: what carries over from the gate is the allocation, in which the model supplies evidence and a fixed rule supplies the verdict. What does not carry over is the guarantee the gate gets from running its rules outside the model.

## Limits

The paper's own confirmatory claim is weakened by disclosed test-split
contamination in exactly the category ([[efe-planning-as-variational-inference|ambiguity]]/clarification) this gate
is built for: five lexicon phrases used to detect ambiguity matched only
test-split questions and "can only have been written from the held-out
split... The test split should therefore be read as a single frozen
evaluation with disclosed prior exposure, not as an uncontaminated
confirmatory test."[^c6]

Resampling by template family rather than by task — the more defensible
unit, since tasks share templates — widens the headline interval to
include zero: "+0.237 becomes [−0.125, +0.562] against the 32B
baseline."[^c7]

The gate presupposes a maintained semantic layer defining every business
metric and has nothing to say about a domain without one; a
hand-weighted confidence/routing component built on top of the same gate
also failed to generalize from validation to test (it over-abstained),
so this note's claim rests on the deterministic rules alone, not on any
learned layer above them.

The prompt variant does not inherit the gate's guarantee. Its checks are answered by the model, and the paper accepts that "LSP does not eliminate detection errors but rather constrains how such errors influence downstream reasoning."[^c11] It also says "complete end-to-end determinism is not guaranteed," because the detection stage stays with the model.[^c14] Its experiments cover two classification tasks on one corpus, and "the effectiveness of LSP for open-ended generation, creative reasoning, or functions without well-defined logical structure was not evaluated."[^c12] Writing the checks "requires domain knowledge to specify relevant variables, conditions, and decision boundaries," a cost the paper names as limiting transfer to new tasks.[^c13]

## Related

[[missing-input-clarification-gate]] · [[abstention]] · [[value-of-information]] · [[entropy-threshold-clarification-trigger]]

- [[deterministic-constraint-delegation]] — the same split in agent commerce: the model elicits constraints, a deterministic component enforces them
- [[distributional-reproducibility-vs-bitwise-determinism]] — what "deterministic" can and cannot mean when the model still produces some of the inputs

[^c1]: lee-2026-business
[^c8]: arxiv-2512-22258 — "LSP separates learned pattern detection from deterministic decision logic"
[^c9]: arxiv-2512-22258 — "The model receives a compact, rule-structured checklist consisting of five binary questions. The final decision is defined by the symbolic rule"
[^c10]: arxiv-2512-22258 — "LSP consistently achieves the highest accuracy (0.83–0.89)"
[^c11]: arxiv-2512-22258 — "LSP does not eliminate detection errors but rather constrains how such errors influence downstream reasoning"
[^c12]: arxiv-2512-22258 — "The effectiveness of LSP for open-ended generation, creative reasoning, or functions without well-defined logical structure was not evaluated"
[^c13]: arxiv-2512-22258 — "constructing LSP rules requires domain knowledge to specify relevant variables, conditions, and decision boundaries"
[^c14]: arxiv-2512-22258 — "complete end-to-end determinism is not guaranteed"
[^c2]: lee-2026-business — "Abstention fires when the requested period lies outside warehouse coverage, when a filter literal is absent from a closed dimension domain, or when a requested concept has no metric, dimension or column. Clarification fires when a phrase matches two or more defined metrics and the question does not pin the choice, or when it matches only concepts the semantic layer leaves undefined."
[^c3]: lee-2026-business
[^c4]: lee-2026-business
[^c5]: lee-2026-business — "Removing the routing layer changes little (0.562 against 0.537), so the result does not depend on escalation."
[^c6]: lee-2026-business
[^c7]: lee-2026-business — "+0.237 becomes [−0.125, +0.562] against the 32B baseline"
