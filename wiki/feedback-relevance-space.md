---
description: "Feedback is licensed after a complete semantic unit is parsed, not only at turn ends: 85% of corpus feedback falls at these Feedback Relevance Spaces, which are TRP-like but more common."
aliases: ["Feedback Relevance Spaces", "FRS", "backchannel relevance space"]
sources: ["doi-10-1007-s10849-020-09328-1"]
---
# Feedback relevance space

Listeners give feedback before the speaker has finished. "backchannels do not just occur at the ends of sentences" or turns; they can come before a sentence is complete, and [[clarification-request]]s can too.[^c1] Feedback is still not placed at random. In the avatar, audio and robot studies the paper reviews, randomly placed backchannels "disrupt the flow of dialogue" and make the listener look less attentive.[^c2]

The question is where feedback is licensed. Howes and Eshghi call those places Feedback Relevance Spaces (FRSs), defined as "points during processing where a semantic sub-tree has just been completed".[^c3] In the paper's Dynamic Syntax (DS) model, feedback is "licensed only after a complete semantic unit of information has been parsed".[^c4] Placement also decides which unit the feedback is about: the paper's late feedback "addresses an earlier semantic unit".[^c21]

The mechanism is what makes the place matter. Backchannels are "licensed when a complete semantic sub-tree has been compiled", because they pass up the chance to initiate repair.[^c5] A clarification request must search backward for its trouble source, and the experimental work the paper cites finds CRs are more disruptive when "produced mid-constituent rather than between constituents".[^c6] The place is therefore a cost, not only a permission.

FRSs are a superset of the places where turns may change hands. They are "analogous to, but more common than, transition relevance places (TRPs)".[^c7] Heldner et al. found far more backchannel relevance spaces than actual backchannels, "indicating that feedback is optional at these points".[^c8] So the space constrains feedback; it does not determine it.

**The measure.** The corpus is 20 British English dialogues from the BNC: "For this study we used 20 dialogues (made up of 4938 utterances)".[^c9] Of the feedback, 543 acknowledgements (83%) and 105 CRs (91%) follow end-complete utterances, which are potentially TRPs and so FRSs in the model.[^c10] The abstract puts the total at "85% of cases where feedback occurs at FRSs".[^c11] The remainder is 100 of 655 acknowledgements (15%) and 16 of 115 CRs (14%). The authors had predicted acknowledgements would fall outside FRSs more often than CRs, and the difference "is therefore not significant (see summary in Table 4), contra hypothesis 4".[^c12]

The non-FRS cases split into late and early. Late feedback follows an FRS and grounds the unit before it. The paper reports restarts more often after late feedback than after feedback at an FRS, which fits the prediction that late feedback is the more disruptive kind.[^c13] Early feedback is the subject of [[early-feedback-predictability]].

For asking and answering, the transfer is this (my inference, not the paper's claim): a question put to a speaker at a closed unit lets the speaker take it up without reopening material already built, while a question put mid-constituent forces a backward search. The paper measures restarts after late feedback, not how questions fare at either place.

## Limits

- Most FRS status is read off a proxy. The 539 cases after an end-complete tag with no overlap "were automatically annotated as occurring at an FRS", and end-completeness "was annotated purely based on the transcriptions", so the count depends on transcription.[^c14][^c15] The manual layer, three-way coding of 96 cases, reached "was κ = 0.71".[^c16]
- The paper calls FRSs constraints on the distribution of feedback "rather than determining them fully".[^c17] The 85% is a rate in one corpus, not a law of placement.
- The data are British English from one corpus, and the authors say generalisation to other languages is "a question for future work".[^c18]
- Early and late CRs are few, and "there are simply not enough cases of early and late CRs" to conclude much about them.[^c19]
- The tree test is DS-specific: complete nodes and compilation actions. A parser without these has no direct equivalent. What may survive the transfer is the constraint (feedback after a closed unit; mid-unit feedback costlier), not the test. This is my inference.
- The conclusion says FRSs are "based on low-level semantic criteria".[^c20] The corpus does not separate that from the end-completeness annotation, so the semantic reading is the authors' interpretation.

## Related

- [[clarification-request]] — the repair-initiating move; this note constrains where it may be placed
- [[grounding-act-discourse-unit]] — the grounding acts (ack, request-repair) that feedback performs; the unit closes where the FRS is
- [[early-feedback-predictability]] — feedback before the unit completes, licensed by prediction rather than by closure
- [[clarification-timing-decay]] — the value of a clarification along a trajectory; another clock for the same question of when to ask

[^c1]: doi-10-1007-s10849-020-09328-1 — "backchannels do not just occur at the ends of sentences"
[^c2]: doi-10-1007-s10849-020-09328-1 — "randomly placed backchannels disrupt the flow of dialogue"
[^c3]: doi-10-1007-s10849-020-09328-1 — "points during processing where a semantic sub-tree has just been completed"
[^c4]: doi-10-1007-s10849-020-09328-1 — "therefore licensed only after a complete semantic unit of information has been parsed"
[^c5]: doi-10-1007-s10849-020-09328-1 — "they are also licensed when a complete semantic sub-tree has been compiled"
[^c6]: doi-10-1007-s10849-020-09328-1 — "produced mid-constituent rather than between constituents"
[^c7]: doi-10-1007-s10849-020-09328-1 — "more common than, transition relevance places (TRPs)"
[^c8]: doi-10-1007-s10849-020-09328-1 — "indicating that feedback is optional at these points"
[^c9]: doi-10-1007-s10849-020-09328-1 — "For this study we used 20 dialogues (made up of 4938 utterances)"
[^c10]: doi-10-1007-s10849-020-09328-1 — "543 acknowledgements (83%) and 105 CRs (91%) occurred"
[^c11]: doi-10-1007-s10849-020-09328-1 — "The model trivially accounts for the 85% of cases where feedback occurs at FRSs"
[^c12]: doi-10-1007-s10849-020-09328-1 — "is therefore not significant (see summary in Table 4), contra hypothesis 4"
[^c13]: doi-10-1007-s10849-020-09328-1 — "are more common following late feedback than feedback at an FRS"
[^c14]: doi-10-1007-s10849-020-09328-1 — "were automatically annotated as occurring at an FRS"
[^c15]: doi-10-1007-s10849-020-09328-1 — "end-completeness was annotated purely based on the transcriptions"
[^c16]: doi-10-1007-s10849-020-09328-1 — "was κ = 0.71"
[^c17]: doi-10-1007-s10849-020-09328-1 — "rather than determining them fully"
[^c18]: doi-10-1007-s10849-020-09328-1 — "this is a question for future work"
[^c19]: doi-10-1007-s10849-020-09328-1 — "there are simply not enough cases of early and late CRs"
[^c20]: doi-10-1007-s10849-020-09328-1 — "based on low-level semantic criteria"
[^c21]: doi-10-1007-s10849-020-09328-1 — "Late feedback addresses an earlier semantic unit"
