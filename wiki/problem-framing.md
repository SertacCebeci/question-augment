---
description: "The dimensions of $W$ are not read off the situation — they are **posited** Donald Schön (*The Reflective Practitioner*, 1983) separates **problem setting** from problem solving."
aliases: ["problem setting", "naming and framing", "framing (design research)"]
sources: ["dorst-2011", "kelly-2022", "schon-1983"]
---
# Problem framing

> The dimensions of $W$ are not read off the situation — they are **posited**
> by a frame, and the frame is adopted for the value it would produce, not for
> its truth. The only test of a frame is downstream.

## Definition / Mechanism

Donald Schön (*The Reflective Practitioner*, 1983) separates **problem[^s1][^s2][^s3]
setting** from problem solving. Problems do not present themselves to a
practitioner as givens; they are constructed from a problematic situation.
Problem setting is the process in which, interactively, one *names* the
things that will be attended to and *frames* the context in which they will
be attended to. Naming fixes what counts as a thing in the situation;
framing fixes the boundary of attention and imposes a coherence that makes
it sayable what is wrong and in what direction things should change.

Kees Dorst (2011, *Design Studies* 32(6):521–532) gives that move a
checkable logical form. He writes design reasoning as an equation over three
terms:

```text
WHAT   +   HOW                leads to   VALUE
(thing)    (working principle)           (aspired)
```

- **Abduction-1** — closed problem solving: `HOW` and `VALUE` are known, the
  `WHAT` is missing. Find an object that, under a working principle you
  already trust, delivers the value you already have.
- **Abduction-2** — the open case: **only `VALUE` is known.** Both the thing
  and the working principle must be created, and in parallel.

A **frame** is Dorst's name for the term that closes the second case: "the
general implication that by applying a certain working principle we will
create a specific value" — *IF* the situation is seen from this viewpoint
and that working principle is adopted, *THEN* the value sought is created.
The frame is arrived at by reasoning back from the only known term, `VALUE`;
because it is proposed rather than derived, a frame "cannot be accepted as
'definitive' until the whole equation has been filled in" and the resulting
design has been shown to deliver the value.

On where frames come from, Dorst reports that expert designers do not attack
the central paradox of a situation head-on: they search the *broader* problem
context for themes, and the frame emerges from material a problem-solving
view would judge peripheral.

## Known as

This note is named for **Dorst's frame**: the single implication term that
closes the WHAT + HOW → VALUE equation. Schön's **problem setting** is the
wider process — naming *and* framing — of which that implication is the part
this note carries; the naming step is outside it.

The bare name *design frame* is **not** an alias of this note. Kelly & Gero
(2022) find it covering three objects distinguished by where a frame is
located — an internal conceptual assemblage, an externalised representation,
or a representation together with the moves made on it — and report that
Dorst himself takes the third in 2015, defining framehood as "completely
defined by its use". The propositional model below says what a frame *does*
and is compatible with all three; the name is held by [[design-frame]].

| Field | Name there | Relation |
|---|---|---|
| Design research (Dorst 2011) | frame; framing | exact — the object this note is defined as: the implication "applying this working principle creates this value" |
| Design research (Schön 1983) | problem setting; naming and framing | close — the same commitment move, but wider in extension: problem setting also fixes what counts as a *thing* in the situation, a step Dorst's frame does not contain. Dorst traces his usage to Schön, which is provenance, not identity |
| Design research, general | *design frame* | **not this concept**: a name for three located objects, held by [[design-frame]]; this note is the propositional reading of what any of them does |
| Judgment and decision making | *framing effect* | **not this concept**: Tversky & Kahneman's framing effect is a measured preference reversal between logically equivalent descriptions of one fixed option set. Here the description is what *creates* the option set, and nothing is held equivalent |
| Design practice (Dorst 2011) | *frame creation* | **not this concept**: a named professional practice built on it, out of scope by `scope.md` (practices out, concepts in) |
| Design research | *reframing* | close: the same operation performed on a situation that already carries a frame, occasioned by that frame failing — a usage Kelly & Gero (2022) argue should be retired, since it does not say whether a deliberate strategy or an observed change is meant ([[frame-change-trigger]]) |

## Why it matters

Stall 1 asks what the dimensions of $W$ are. Every other entry on
Axes either denies that the question is answerable from inside
([[expected-information-gain]], [[unknown-unknowns]]) or supplies a
*generator* of candidate axes ([[grand-tour-question]], [[premortem]],
[[metamorphic-probes]]). Framing says something the generators do not: the
axis set is not discovered at all, it is **committed to**, and the criterion
for the commitment is not "is this axis real" but "would this way of seeing
produce the value I am after".

Two consequences for a questioning procedure:

1. **The axis set has a warrant, and the warrant is prospective.** A frame is
   an implication whose antecedent is a way of seeing. It is therefore not
   confirmable before an answer set is complete — you cannot ask a question
   that tests the frame directly, only questions that fill in the equation
   whose success or failure tests it.
2. **A stuck inquiry has two repairs, not one.** Either the answers are wrong
   (fill the equation differently) or the value/working-principle pairing is
   wrong (adopt another frame). Schön's separation makes the second a
   distinct, nameable move rather than an unexplained restart.

## Transfer

| | |
|---|---|
| **In its home field** | A designer facing an under-determined brief adopts a standpoint from which a problematic situation becomes workable; the frame is judged by whether the finished artifact delivers the aspired value to a client. |
| **Here** | An asker facing $|W| \gg 1$ with no stated axes adopts a frame that fixes which distinctions of the world will be attended to at all, and hence which questions are formulable. |
| **What survives** | The three-term equation as a *bookkeeping* device: an inquiry that cannot name its `VALUE` has no criterion for choosing a frame, and one that has fixed both `HOW` and `VALUE` is in Abduction-1 and does not need framing. Also survives: the claim that the frame is untestable until the equation is complete, which forbids scoring an axis set before any answer arrives. |
| **What does not** | Dorst's "abduction" carries no soundness property — it is not inference to the best explanation with any truth-preservation, and nothing licenses transferring an inference guarantee. And the design setting supplies `VALUE` from outside (a client, a brief); in a general asking setting the aspired value is often exactly what is unknown, in which case the equation has three unknowns and Dorst's asymmetry — "start from the only known" — has no starting point. |

## Limits

- **The load-bearing claim of this note — that framing is a *commitment* with
  a prospective warrant rather than a discovery — is Schön's and Dorst's
  descriptive account of professional practice, not a result.** Neither source
  measures anything. Dorst himself says new frame creation "often looks to be
  a largely informal activity"; there is no procedure here, and no way to tell
  a good frame from a bad one before the work is done.
- `schon-1983` is a book this note did not read in full: the naming/framing
  wording is taken from secondary quotation, and sources disagree on the page
  (40 vs 52), so the book is cited and no page is claimed.
- Dorst's expert/novice contrast (experts frame, novices match `WHAT` to `HOW`
  at random) is asserted in the 2011 paper on the strength of Lawson & Dorst
  2009's interview material, not on a controlled comparison; this note does
  not rest on it.
- The equation is a notation, not a formalism: `leads to` is not defined, and
  nothing in it says when two frames are the same frame or how many exist.
- The 2011 propositional model is not stable across its own author: per
  kelly-2022, Dorst (2015) defines a frame by its use rather than by the
  implication, so "Dorst's frame" names two objects four years apart. The
  2015 book was not read here [?].

## Related

Axes · [[unknown-unknowns]] · [[bounded-rationality]] · [[question-as-partition]] · [[problem-solution-coevolution]] · [[design-frame]]

[^s1]: dorst-2011
[^s2]: kelly-2022
[^s3]: schon-1983
