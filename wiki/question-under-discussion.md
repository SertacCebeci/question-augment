---
description: "What the answerer must comprehend is not the interrogative that was uttered **Roberts (1996; rev. 1998; repr. *Semantics and Pragmatics* 5:6,"
aliases: ["QUD", "questions under discussion", "immediate question under discussion"]
sources: ["clifton-2012", "lewis-1979", "roberts-1996", "wu-2023"]
---
# Question under discussion

> What the answerer must comprehend is not the interrogative that was uttered
> but the question the discourse is currently committed to answering — a stack
> element that is often never spoken and has to be reconstructed.

## Definition / Mechanism

**Roberts (1996; rev. 1998; repr. *Semantics and Pragmatics* 5:6, 2012)** models[^s1][^s2][^s3][^s4]
discourse as a game whose goal is Stalnaker's: reduce the context set to a
singleton. Moves are *set-up* moves (questions) and *payoff* moves
(assertions). The information structure of a discourse is a tuple
$\langle M, Q, A, <, Acc, CG, QUD\rangle$; the last component is the load-bearing one.

**This note's concept is a single question — the one at the top of the QUD
store — not the store itself.** Roberts's $QUD$ is a push-down stack: the
ordered set of accepted questions that are, at a given move, still unanswered
and not yet determined to be unanswerable. The question *under discussion* at
move $m$ is its top element, $last(QUD(m))$, which Roberts also calls the
**immediate QUD**; that element is what an answerer must fix, and everything
below is what the framework says about how it got there and what it commits to.
Roberts's clause (c): for $q < q'$ on the stack, a complete answer to $q'$ must
contextually entail a *partial* answer to $q$ — so the stack is a fragment of a
**strategy of inquiry**, a partial order of subquestions under a superquestion,
with the "Big Question" (*What is the way things are?*) at the bottom. A
question is popped from the top when it is answered **or determined to be
practically unanswerable**, and the element below it becomes the QUD.

**Relevance is defined against that top element** (Roberts's (15)): a move $m$
is Relevant to the QUD $q$ iff $m$ introduces a partial answer to $q$ (when $m$
is an assertion) or is part of a strategy to answer $q$ (when $m$ is a
question). Answerhood is inherited from the alternative-set semantics: a
partial answer contextually entails the evaluation of at least one alternative,
a complete answer of every one.

**The QUD need not have been uttered.** Roberts follows Carlson in taking
discourse question/answer relations to be frequently implicit, retrieved by
**[[presupposition-accommodation|accommodation]]** in Lewis's (1979) sense, with prosodic focus in English
carrying a presupposition about which question the utterance answers. So the
answerer's comprehension step is an *inference to a question*, and only then an
answer to it.

Two measurements of that step:

- **Clifton & Frazier (2012)**, three eye-tracking experiments: reading of a
  verb phrase was disrupted when it failed to resolve an implicit QUD, relative
  to the same material with no clear QUD — the QUD is used online, not
  post hoc.
- **Wu, Mangla, Durrett & Li (2023)** built QUDeval, 2,190 QUD questions from
  fine-tuned systems and LLMs judged on answer compatibility, givenness and
  anchor relevance; satisfying all constraints at once remained hard for the
  models tested, while human-authored QUDs scored highly.

## Known as

| Name | Field | Relation |
|---|---|---|
| question under discussion, questions under discussion, QUD | formal pragmatics, semantics | exact |
| immediate question under discussion | formal pragmatics | exact — Roberts's own term for the top element, which is the object this note names |
| QUD stack, QUD store | formal pragmatics, dialogue systems | close — *not* this concept: the data structure whose top element is the QUD. The literature uses "QUD" for both, but the stack carries the whole strategy of inquiry and is measured differently (depth, entailment between levels), so it is left as a separate topic |
| dialogue gameboard | dialogue semantics (Ginzburg) | *not* this concept — the gameboard is a larger context record of which a QUD structure is one field; left as a separate topic |
| information structure | formal pragmatics | *not* this concept — the focus/background articulation of a sentence, which Roberts derives *from* the QUD rather than identifies with it |

## Why it matters

1. **Stall 9 has a formal object.** "What is being asked" is not the uttered
   interrogative; it is the top of a stack the asker did not utter. An answerer
   that comprehends the words perfectly and fixes the wrong stack element
   produces a reply that is true, informative and a non sequitur.
2. **Answerhood is relative, so stall 5 depends on stall 9.** Whether a reply
   is a constraint ([[constraint-as-information]]) is only decidable once the
   QUD is fixed: the same proposition is a partial answer to one stack element
   and irrelevant to another.
3. **The framework licenses a specific way of not answering.** A question is
   popped when *determined to be practically unanswerable* — a declared exit
   distinct from ignoring it, and the pragmatic counterpart of the "I don't
   know" problem on stall 10.
4. **This wiki's inference** (Roberts does not state it): mis-accommodating the
   QUD is the answerer-side twin of the false presupposition in
   [[question-as-partition]]. Both delete the actual world from the space being
   searched — one by asking inside a partition that excludes it, the other by
   answering a question no one asked. The asker-side error has a corrective
   reply as its channel; the answerer-side error has no comparable signal
   unless the answerer names the QUD it took.

## Transfer

| | |
|---|---|
| **Home field** | formal pragmatics of cooperative multi-turn human discourse: shared common ground, interlocutors who accept questions, felicity as the object of study |
| **Here** | an answerer (human or agent) receiving one question and deciding what it is being asked before committing to a reply |
| **What survives** | the QUD as an object distinct from the uttered interrogative; Relevance defined relative to it; partial vs complete answer; the entailment condition linking a subquestion to the question it serves; the licensed pop of an unanswerable question |
| **What does not** | the cooperativity assumption (the framework is a felicity condition on well-formed discourse, so an uncooperative or adversarial asker falls outside it); the monotonic common ground Roberts assumes and flags as an idealisation; and the [[recovery-postulate|recovery]] procedure — the theory says what the answerer must have inferred, never how to infer it |

## Limits

- The framework is a **well-formedness condition, not an algorithm**. Nothing
  in Roberts computes the QUD from an utterance; the accommodation step is
  stipulated to happen. The claim in *Why it matters* 1 therefore names a
  failure mode without supplying a detector for it.
- Clause (c) is an idealisation Roberts herself weakens: she gives a discourse
  (her (13)) where a follow-up question does not entail the one below it and
  repairs it by positing a bridging question — which the answerer must also
  accommodate.
- Relevance to the QUD is a **predicate, not a ranking**. It separates answers
  from non sequiturs and says nothing about which of two Relevant replies is
  better; no cost, no informativeness measure ([[expected-information-gain]]).
- Clifton & Frazier's evidence is reading-time disruption in English written
  text with constructed materials; it supports online use of a QUD, not the
  stack structure or the entailment clause.
- The QUDeval finding is reported qualitatively here — the note cites the
  dataset and its three criteria, not a per-model score.
- Point 4 in *Why it matters* is this wiki's own inference and is marked in
  place; no source cited here states it.

## Related

[[question-as-partition]] · [[presupposition-accommodation]] · [[conclusive-answer]] · [[constraint-as-information]] · [[ambiguity-taxonomy]]

[^s1]: clifton-2012
[^s2]: lewis-1979
[^s3]: roberts-1996
[^s4]: wu-2023
