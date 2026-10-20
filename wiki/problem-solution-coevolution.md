---
description: "A candidate answer is an **axis generator**. In Dorst & Cross's protocol Mary Lou Maher and Josiah Poon (*Microcomputers in Civil Engineering* 11(3),"
aliases: ["co-evolution of problem and solution spaces", "problem-solution co-evolution"]
sources: ["crilly-2021", "dorst-2001", "maher-1996"]
---
# Problem–solution co-evolution

> A candidate answer is an **axis generator**. In Dorst & Cross's protocol
> study of nine experienced designers the problem was never fixed first: a
> tentative solution kept exposing requirements that were not in the original
> problem space.

## The model

Mary Lou Maher and Josiah Poon (*Microcomputers in Civil Engineering* 11(3),[^s1][^s2][^s3]
1996) model design exploration as two interacting spaces evolving in step: a
problem space $P(t)$, holding the design goal at time $t$, and a solution
space $S(t)$, holding the current search space for design solutions. The
load-bearing arrow is the upward one, *solution refocuses the problem*:
$S(t)$ is not only a [[possible-worlds|state space]] in which a solution may be found, it also
prompts requirements for $P(t+1)$ that were not in the original $P(t)$. (The
primary text was not read here; the model and this arrow are taken from
Crilly's 2021 review of it — see `## Limits`.)

Each space's next population is guided by the most recent population of the
other. The model was built to let a computer perform creative design (Maher
& Poon implement it with a genetic algorithm), not as a description of how
people think — a point Crilly (2021) makes explicitly.

## The finding

Kees Dorst and Nigel Cross (*Design Studies* 22(5):425–437, 2001) ran a
protocol study of nine experienced industrial designers working the same
brief, with the resulting designs rated for overall quality and for
creativity. They observed that the designers did not treat the assignment as
a fixed problem:

> "It seems that creative design is not a matter of first fixing the problem
> and then searching for a satisfactory solution concept. Creative design
> seems more to be a matter of developing and refining together both the
> formulation of a problem and ideas for a solution, with constant iteration
> of analysis, synthesis, and evaluation processes between the two notional
> design 'spaces' — problem space and solution space."
> — Dorst & Cross 2001

They read Maher & Poon's model onto the protocols and added the distinction
between **default** and **surprise** problem/solution spaces — the creative
episodes were the ones that left the default space — and it is this pairing
that made co-evolution one of the most cited constructs in design research
(Crilly 2021).

## Known as

| Field | Name there | Relation |
|---|---|---|
| Design computing (Maher & Poon 1996) | co-evolution of problem and solution spaces | exact — the model this note names |
| Design cognition (Dorst & Cross 2001) | problem–solution co-evolution | exact — the same two-space model, read onto human protocols |
| Design research, general | *design co-evolution* | **not an alias**: an umbrella term. Crilly (2021) documents that it is used for a range of distinct things — reciprocal influence, mere alternation of attention with no change, and single non-reciprocal episodes. This note is only the strict reading, reciprocal change; the other readings are separate objects |
| Planning theory (Rittel & Webber 1973) | *wicked problem*, property 2 | **not this concept**: a property attributed to a class of problems, not a process observed in a protocol. Rittel's "the information needed to understand the problem depends upon one's idea for solving it" is the same intuition asserted a priori |

## Why it matters

Axes's three generators produce candidate axes from the informant
([[grand-tour-question]]), from mutating what is already held
([[metamorphic-probes]]), or from conditioning the generator
([[premortem]]). Co-evolution supplies a fourth mechanism that none of them
covers: **provisionally commit to one world, then read off the constraints
that commitment turns out to need.** The axis arrives from the candidate
answer, not from the asker and not from the informant.

This is a direct conflict with the selection machinery. [[expected-information-gain]]
requires the parameter space fixed before the first question is scored;
co-evolution says the operation that most enlarges the space is the one EIG
treats as terminal — proposing an answer. It also weakens the reading of
[[version-space]] on Distillation: there the hypothesis language must
be fixed before the first example, which is exactly the condition the design
protocols violate.

## Transfer

| | |
|---|---|
| **In its home field** | $P$ holds requirements for an artifact, $S$ holds candidate artifacts; both are populations evolved over time, and in Maher & Poon's implementation the transition is a genetic-algorithm step scored by fitness against the other space. |
| **Here** | $P$ is the axis set describing $W$; $S$ is a candidate world (a provisional answer to "which world is it?"). The `S → P` arrow is the claim that naming a candidate world exposes dimensions the description of $W$ did not have. |
| **What survives** | The asymmetry: the space of axes is not closed under the questions the current axes support, and at least one candidate answer must exist before the axis set can be judged. Also survives the coding consequence — an inquiry that never proposes a world never runs the arrow. |
| **What does not** | The population and fitness mechanics: a design has an external quality rating, whereas a world in $W$ carries only a probability, so there is nothing here to rank a "population" of worlds by. Nor does the symmetry survive intact — sketching a design is cheap and revocable, while committing to a world in an inquiry is the act that ends it (Distillation), so running the arrow costs something the design setting does not charge. |

## Limits

- **The claim this note makes is descriptive, and the field's own reviewer
  denies it more.** Crilly (2021) holds co-evolution "not to be a fully
  developed theory with predictive power, but simply a way of describing
  design activity". Nothing here predicts *when* a candidate answer will
  produce a new axis, or how many.
- **Two of the Crilly claims used here were not confirmed against the
  primary text [?].** The count of seven operationalisations of the model
  between 1996 and 2020, and the report that Smulders, Reyman & Dorst could
  not reliably separate problem talk from solution talk when coding
  architect–client data, are taken from crilly-2021 but were not verified in
  it; what is confirmed is the weaker abstract-level claim that the term
  covers a range of distinct concepts, so studies reporting "co-evolution"
  are not necessarily reporting the same quantity.
- **Maher & Poon 1996 was not read in the original [?]** — the full text was
  not reachable — so the two-space model and the $S(t) \to P(t+1)$ arrow are
  paraphrased from Crilly's 2021 summary of it, not quoted from the paper.
- **The problem/solution distinction the model rests on may not be stable.**
  Any item in a problem–solution hierarchy is a solution to what sits above
  it and a problem to what sits below, so which space an item is in is a
  viewpoint, not a fact. If $P$ and $S$ are not separable, "the solution
  refocused the problem" is not a measurement.
- Dorst & Cross's evidence is $n = 9$ experienced designers on one brief,
  scored by judges; there is no control condition in which the problem was
  held fixed, so the study cannot say that co-evolving *caused* the better
  designs.
- The mapping of $P$ to an axis set and $S$ to a candidate world is this
  wiki's, made in `## Transfer`; no source performs it.

## Related

Axes · [[problem-framing]] · [[expected-information-gain]] · [[version-space]] · [[unknown-unknowns]] · [[divergent-convergent]]

[^s1]: crilly-2021
[^s2]: dorst-2001
[^s3]: maher-1996
