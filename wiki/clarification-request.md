---
description: "The answerer's third move: not the answer and not silence, but a question **Schlangen (2004)** takes the defining feature of a clarification request to be that, unlike a normal question,"
aliases: ["CR", "clarification requests", "clarification move"]
sources: ["dingemanse-2015", "ginzburg-2004", "schlangen-2004", "tsvilodub-2026", "doi-10-1007-s10849-020-09328-1"]
---
# Clarification request

> The answerer's third move: not the answer and not silence, but a question
> *about the previous utterance* — and its content is which task of
> understanding failed.

## Definition / Mechanism

**Schlangen (2004)** takes the defining feature of a clarification request to[^s1][^s2][^s3][^s4]
be that, unlike a normal question, it is not about the state of the world but
about an aspect of a previous utterance: it signals a problem in understanding
that utterance and requests repair of it. He classifies CRs along three
dimensions:

| Dimension | Values | What it encodes |
|---|---|---|
| **level** | which task of understanding failed | contact and attention; speech recognition; meaning and understanding — refined into parsing, resolving underspecification (reference, scope, lexical [[efe-planning-as-variational-inference|ambiguity]]), and contextual relevance; recognising intention |
| **severity** | repetition request vs confirmation request | whether the answerer has a hypothesis at all |
| **extent** | points at a problematic element of the original utterance, or does not | how much of the original is under repair |

The level dimension is taken from the hierarchically ordered tasks of
communication of Clark (1996) and Allwood (1995). "Peter?" after "Did you talk
to Peter?" is a reference-level CR. The taxonomy is the payload: a CR carries
information back to the asker only if its level is recoverable.

**The decision is three-way, not binary.** Schlangen's second move is to
extend the confidence score that spoken dialogue systems take from the speech
recogniser to *every* processing stage where the system relies on a guess, and
to combine those values. The combined confidence selects a strategy over one
scale: **reject** (a repetition request), **confirm** — explicitly ("Did you
say you want to leave from Potsdam?") or implicitly ("From Potsdam. To
where?") — or **accept**. Implicit confirmation answers *and* checks in the
same turn, so "answer or ask back" is not a partition of the options.

**When to ask back.** Tsvilodub, Mulligan, Snider, Hawkins & Franke (2026)
model the choice as **expected regret**: the loss from acting now rather than
first seeking information. Across two experiments, uncertainty and the cost of
the alternative action interact — uncertainty drives clarification most when
acting wrongly is expensive.

**The CR is itself ambiguous.** Ginzburg & Cooper (2004) show the same
fragment carries two *readings*: *clausal* ("Are you asking whether Bo left?")
and *constituent* ("Who is Bo?"). Their result is that the update an utterance
makes to context cannot be defined in purely semantic terms — resolving
clarification ellipsis needs operations on the antecedent utterance's form,
not only its content.

## Known as

| Name | Field | Relation |
|---|---|---|
| clarification request, CR | dialogue semantics, spoken dialogue systems | exact |
| clarification move | dialogue systems | exact — Schlangen's own alternate term |
| other-initiated repair | conversation analysis | close — *not* this concept: a broader category with its own measurement (Dingemanse et al. 2015: about once per 1.4 minutes across 12 languages of 8 families), covering initiations that are not questions. Its own note |
| clarifying question | information retrieval, LLM evaluation | close — *not* this concept: measured by whether asking improves retrieval or task success ([[clarification-benchmarks]]), and typed by the ambiguity in the request rather than by the level that failed |
| confirmation request | dialogue systems | *not* this concept — one value of the severity dimension |

## Why it matters

1. **Stall 9 gets an output channel.** Comprehension failure need not be
   silent or guessed through. But an untyped CR ("What do you mean?") tells
   the asker nothing about which task failed, so the repair is unaimed.
2. **The ask/answer question is mis-posed.** The middle region costs no extra
   turn: implicit confirmation commits to a reading, delivers the answer, and
   exposes the reading for correction at once.
3. **Where the thresholds sit is a decision problem, not a linguistic one.**
   Schlangen supplies the scale and leaves the cut points open; Tsvilodub et
   al. supply the shape of the cut. Their regret criterion plays on the
   answerer's side the role [[value-of-information]] plays on the asker's; the
   two are not shown to be the same functional.
4. **Asking back has an ambiguity cost of its own.** The CR the answerer emits
   is itself open to the two readings Ginzburg & Cooper describe, so a
   deferral can be mis-comprehended in turn.
5. **Placement is a cost as well as a choice.** Where a CR falls relative to the unit it repairs is constrained by the answerer's processing: in the BNC sample most CRs (91%) follow an end-complete utterance, and the experimental work the paper cites finds CRs more disruptive when "produced mid-constituent rather than between constituents".[^s5][^s6] This bears on when a clarifying question is put, not on whether it is put; the paper's own CR counts are small (see [[feedback-relevance-space]]).

## Transfer

| | |
|---|---|
| **Home field** | spoken dialogue systems and dialogue semantics: co-present participants, a speech recogniser emitting scored hypotheses, a narrow task domain |
| **Here** | any answerer — human or agent — deciding, on one received question, whether to answer, to answer-and-check, or to return a question |
| **What survives** | classifying a comprehension failure by the *level* that failed; the severity split; the three-region strategy over a confidence scale; the demand for a confidence at every guessed stage |
| **What does not** | the acoustic levels, which have no analogue for a text-only answerer; the co-presence that makes a repetition request cheap; the [[calibration]] — Schlangen assumes a scored recogniser, and the pragmatic-level confidences he needs are the ones nobody supplies |

## Limits

- Schlangen states explicitly that no psychological status is claimed for the
  postulated levels — only that they distinguish types of CR. The corpus
  analysis of the model's coverage is described as in progress.
- **The combination rule is the hole.** "Combined in some principled way (for
  example by taking a weighted average)" is as far as the paper goes; no
  threshold between reject, confirm and accept is derived, so point 3 names
  the missing piece rather than filling it.
- The implementation Schlangen reports is a proof of concept: not connected to
  a recogniser, modelling an overhearer, handling two hypotheses differing in
  one constituent.
- Tsvilodub et al. (2026) is a descriptive two-experiment study of humans in
  constructed scenarios; nothing there shows an agent trained on the regret
  criterion clarifies better, and neither paper identifies regret with
  value of information — the pairing in point 3 is this wiki's.
- That the failure mode *recurses* under deferral (point 4) is this note's
  inference from the two-reading ambiguity, not a claim of Ginzburg & Cooper.
- Ginzburg & Cooper's constituent reading carries a phonological-identity
  condition that reformulation CRs violate, so the two-reading account does
  not cover every CR the taxonomy admits.
- The re-posing of the ask/answer binary (point 2) is this wiki's framing of
  Schlangen's strategy scale, not a claim he makes about the subject.

## Related

[[question-under-discussion]] · [[abstention]] · [[clarification-benchmarks]] · [[ambiguity-taxonomy]] · [[value-of-information]] · [[uncertainty-decomposition]] · [[feedback-relevance-space]] — where feedback, CRs included, is licensed inside an utterance

[^s1]: dingemanse-2015
[^s2]: ginzburg-2004
[^s3]: schlangen-2004
[^s4]: tsvilodub-2026
[^s5]: doi-10-1007-s10849-020-09328-1 — "produced mid-constituent rather than between constituents"
[^s6]: doi-10-1007-s10849-020-09328-1 — "543 acknowledgements (83%) and 105 CRs (91%) occurred"
