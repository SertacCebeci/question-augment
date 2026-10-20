---
description: "A rhetorical question is an interrogative that presupposes its answer is already common ground, so accepting it adds no inquisitive update but still commits the hearer to the answer."
aliases: ["RhQ", "rhetorical interrogative", "severing asking from questioning", "interrogative form puzzle"]
sources: ["biezma-2017"]
---
# Rhetorical question

A rhetorical question (RhQ) is an interrogative in form that behaves like an assertion in effect. Biezma & Rawlins (2017) take three hallmarks as the definition: RhQs do not expect an answer, they have the feel of an assertion, and they can optionally be answered.[^c1]

## The puzzle

Interrogatives canonically signal ignorance and request information, whereas a RhQ signals that all participants already hold the answer. The authors call this the Interrogative Form Puzzle: why utter an interrogative at all?[^c2]

## Mechanism: asking is separate from questioning

The account separates two steps of an interrogative utterance. Asking proposes to update the context with the question. Accepting the proposal is what actually changes the question under discussion (see [[question-under-discussion]]).[^c3] In a RhQ the questioning step is trivial, because the resulting question is already resolved by the context and so is cleared automatically. The proposal step is not trivial.[^c4]

The sufficient condition is that a question can be rhetorical in a context if the projected update with it is non-inquisitive.[^c5] Non-inquisitiveness comes from a presupposition, either carried by a linguistic trigger or adopted from the speaker, that the context entails the answer. A hearer may accommodate that presupposition (see [[presupposition-accommodation]]).[^c6]

## Why a question rather than an assertion

By accepting a RhQ, the hearer is committed to the presupposition that makes it rhetorical, whether or not they state the answer. To avoid the commitment they must reject the presupposition at the proposal stage.[^c7] Assertions introduce new commitments. RhQs are suited to extracting a commitment that the speaker believes should already have been given.[^c8] This is the paper's answer to the puzzle. It is a theoretical proposal, not an experimental result.

## Signals

Common ground status of the answer is necessary, not sufficient. A prosecutor's questions to a coached witness, or an exam question to an A+ student, meet the condition but are not rhetorical. The question must conventionally signal the speaker's attitude.[^c9] Signals vary:

- Doubled alternative questions ("Is John an idiot or is he an idiot?") reduce to a single alternative and presuppose exhaustivity, so the answer is the one alternative.[^c10]
- The German particle *schon* forces a rhetorical reading and presupposes that the update is non-inquisitive.[^c11]
- Prosody and strong polarity items ("lift a finger") work only together with context. "Where on earth do I find a mechanic?" need not be rhetorical.[^c12]

## Diagnostics

Responses differ from those to an assertion. "You are right" is fine after a RhQ, but "That's not true!" is not. The authors read this as showing that rhetorical content is not propositional content at the proposal stage.[^c13] A RhQ whose answer was just stated is redundant, like a repeated assertion.[^c14]

## Limits

- The paper is formal-semantic with constructed and corpus-attested examples. It reports no experiment and no measurement on humans or models.
- The formal system has no notion of commitment, and prosodic cues are explicitly left unanalysed.[^c15]
- Monologue questions such as a presenter's "Can we find an answer?" are left out of scope.
- The account assumes the common ground is closed under entailment when signalled. The authors say closure without signalling is too strong.[^c16]
- That RhQs are suited to commitment extraction is the authors' explanation, not a tested claim. Any use for LLM question handling would be my own inference, untested.

## Related

- [[question-under-discussion]] — the discourse stack that a RhQ proposes to update and that clears when resolved
- [[presupposition-accommodation]] — the mechanism by which the hearer takes in the presupposed answer
- [[rhetorical-intent-direction-divergence]] — a different literature that treats rhetorical question as a probed signal in models

[^c1]: biezma-2017 — "RhQs don’t expect an answer."
[^c2]: biezma-2017 — "This is what we will term the Interrogative Form Puzzle (IFP)."
[^c3]: biezma-2017 — "asking a question proposes to update the context with that question, and accepting a proposed question leads to that update happening."
[^c4]: biezma-2017 — "In the case of rhetorical questions, in context the questioning part of the update is trivial but the proposal part isn’t."
[^c5]: biezma-2017 — "A question Q can be rhetorical in c if Fc+pQq is non-inquisitive."
[^c6]: biezma-2017 — "Minimally, that the context entails the answer is a speaker presupposition"
[^c7]: biezma-2017 — "they will typically need to reject some presuppositions of the question at the proposal stage in order to reject the question itself."
[^c8]: biezma-2017 — "RhQs are very well-suited for extracting commitments"
[^c9]: biezma-2017 — "while we follow C&S in taking the common ground generalization to describe"
[^c10]: biezma-2017 — "identical denotations will lead to a singleton set denotation for the question."
[^c11]: biezma-2017 — "the presence of schon forces it to be rhetorical."
[^c12]: biezma-2017 — "rhetoricity is not conventionalized in the semantics of the NPIs above."
[^c13]: biezma-2017 — "rhetorical ‘contents’ are not contents at all"
[^c14]: biezma-2017 — "it feels redundant, as if there is no need to ask a rhetorical question."
[^c15]: biezma-2017 — "While for space reasons this formal system does not directly implement a notion"
[^c16]: biezma-2017 — "However, closure without signalling is much too strong"
