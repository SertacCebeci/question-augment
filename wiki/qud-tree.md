---
description: "Three literatures draw a picture of a text with questions in it and call it a **The measurable differences.** The first two require entailment or givenness relations *between* questions;"
aliases: ["QUD structure", "QUD tree"]
sources: ["dekuthy-2018", "ko-2023", "riester-2019"]
---
# QUD tree

> Three literatures draw a picture of a text with questions in it and call it a
> QUD tree or a QUD structure. They are not the same object and are not
> measured the same way.

## Definition / Mechanism

| The name covers | What it is | How it is measured | Note |
|---|---|---|---|
| **QUD stack / d-tree** (Roberts 1996/2012; the name *d-tree* from Büring 2003 [?]) | an ordered store of accepted, still-unanswered questions; a subquestion must entail a partial answer to the question above it; the top element is *the* QUD | not measured — a felicity condition on well-formed discourse | [[question-under-discussion]] |
| **QUD tree** (Riester 2019; De Kuthy, Reiter & Riester 2018) | a discourse tree whose non-terminal nodes are implicit questions reconstructed under Q-Givenness and its companions, terminals the text's assertions, read left to right | inter-annotator $\kappa$ between trained analysts on the span matrix: .45–.53 | [[qud-licensing-constraints]] |
| **QUD dependency structure** (Ko et al. 2023) | one edge per sentence, from an anchor sentence to the sentence that answers a generated free-form question; no relations between questions | human approval of generated questions: 71.5% plausible, 78.8% of those answered by the target sentence | [[qud-parsing]] |

**The measurable differences.** The first two require entailment or givenness[^s1][^s2][^s3]
relations *between* questions; the third explicitly leaves question–question
relations to future work, so it cannot represent a strategy of inquiry. The
first constrains that relation by clause (c) of Roberts (1996/2012) —
a complete answer to the higher question must contextually entail a partial
answer to the one below — a clause Roberts herself weakens by accommodating a
bridging question where it fails ([[question-under-discussion]]); the second
instead admits questions that are not entailed but are anaphorically dependent
on given material. That the two therefore license different reconstructions is
*this note's* reading; no source compares the two conditions. The second and
third also disagree on what a question may contain: Q-Givenness bans new
material, while Ko et al. had to mask named entities to stop their generator
from writing it in. Attachment agreement between a QUD dependency structure and
an RST tree over the same documents is 0.30 — the structures are not
interchangeable with the older discourse formalisms either.

## Known as

| Name | Field | Relation |
|---|---|---|
| QUD tree | formal pragmatics; computational linguistics | *ambiguous* — Riester's constrained tree of implicit questions in the first field, informally any of the three in the second |
| QUD structure | formal pragmatics, computational linguistics, dialogue systems | *ambiguous* — used for all three objects in this table |
| d-tree | formal pragmatics | close — a name for the stack-shaped object of row 1, not for rows 2–3 |
| question under discussion, QUD | formal pragmatics | *not* this page — the single question at the top of the store, which has its own note ([[question-under-discussion]]) |

## Why it matters

1. **Declare the structure before transferring a result.** A note or an
   answerer that imports "the QUD structure" is importing one of three objects
   with different well-formedness conditions; which one has to be named in the
   claim, or the claim is not checkable.
2. **A number measured on one does not license a claim about another.** Ko et
   al.'s 71.5% is an approval rate on independent anchor–question edges; it says
   nothing about whether a stack pops correctly or whether a subquestion serves
   its superquestion, because no question–question relation was represented or
   scored.
3. **The three [[calibration|reliability]] figures are not comparable.** A $\kappa$ between two
   trained analysts applying a written manual and a crowd approval rate on
   generated questions answer different questions; neither converts into the
   other, and the stack of row 1 has no reliability figure at all because it was
   never annotated.

## Limits

This note claims only that the three objects are distinct and differently
measured. No source compares them on the same text, so nothing here says which
representation is right. The Büring 2003 chapter ("On D-Trees, Beans, and
B-Accents") is cited `[?]` — unverified this pass, and it licenses only the
alternative name *d-tree* in row 1, no claim in the body. The reading in *The
measurable differences* that Roberts's clause (c) and Riester's anaphoric
dependency license different reconstructions is this note's own; both
constraints are cited from their sources, the comparison is not.

## Related

[[question-under-discussion]] · [[qud-licensing-constraints]] · [[qud-parsing]] · [[question-as-partition]]

[^s1]: dekuthy-2018
[^s2]: ko-2023
[^s3]: riester-2019
