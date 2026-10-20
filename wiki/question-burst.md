---
description: "Hal Gregersen (Executive Director, MIT Leadership Center), 2018 Three steps, as Gregersen states them in the article version of the protocol (*Better Brainstorming*, **Harvard Business Review**,"
aliases: ["question storming", "Gregersen's question burst"]
sources: ["gregersen-2018"]
---
# Question Burst

> Hal Gregersen (Executive Director, MIT Leadership Center), 2018
> (`gregersen-2018`): produce at least 15 questions in four minutes, and
> answer none of them.

## Protocol

Three steps, as Gregersen states them in the article version of the protocol[^s1]
(*Better Brainstorming*, **Harvard Business Review**, March–April 2018,
pp. 64–71; see Limits on its key):

1. **Set the stage** — pick a challenge you care about; invite a few people,
   two or three of whom have no direct experience with it. Take **two
   minutes** to lay out the problem "in a high-level way that doesn't
   constrain or direct the questioning". Record your mood in one line.
2. **Brainstorm the questions** — a timer, **four minutes**, collectively as
   many questions as possible, "try for at least 15", each written down
   verbatim. Two rules are spelled out before the floor opens:
   - **only questions** — anyone who offers a solution, or answers someone
     else's question, is redirected by the convener;
   - **no preambles or justifications** framing a question, "because they'll
     guide listeners to see the problem in a certain way".

   Then record your mood again.
3. **Identify a quest** — alone, pick the few questions that intrigue you,
   "strike you as different from how you've been going about things, or even
   cause you to feel a bit uncomfortable", expand them with a [[five-whys]]
   sequence, and commit to one pathway with a three-week action plan.

Gregersen recommends at least three rounds per challenge and reports that
"about 80% of the time" a burst yields at least one question that usefully
reframes the problem.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| Creativity / leadership practice | question burst | exact — Gregersen's own name for this protocol |
| Gregersen's writing | Gregersen's question burst | exact — the attributed form of the same name |
| General facilitation usage | question storming | close — a generic label for any produce-only round. It carries neither the four-minute timebox, the at-least-15 floor, nor the no-preamble rule, and the same label is applied to the Produce phase of [[question-formulation-technique]], which is a different object (QFocus → Produce → Improve → Prioritize, no timer, no volume floor). Nothing here shows the two are the same protocol |

## Why the two rules

- **No answering** — the first answer locks the framing and shrinks the space
  of remaining questions. Gregersen's own stated reason is enforcement of the
  volume floor: the time pressure "helps participants stick to the 'questions
  only' rule", and "any effort spent on answers will mean less chance of
  hitting the goal".
- **No preambles** — the rationale steers what everyone else can see next,
  which is the effect the exercise exists to avoid.

## Why it matters

The mechanism is a **volume floor enforced by a timebox**: quantity is the
declared target, and both rules exist to protect it. It is the human-side
counterpart of the phase separation in [[question-formulation-technique]] and
of the principle in [[divergent-convergent]] — production separated from
evaluation, bought with a clock rather than a facilitator's phase boundary.

> **Conjecture (this wiki, not Gregersen):** if the later questions are the
> valuable ones, it is because they jump to a new axis — returns diminish
> *within* an axis and rise at the jump. See [[unknown-unknowns]]. Gregersen
> makes no such ordering claim: he denies the numbers are special ("Is there
> some magic about precisely four minutes and 15 questions? No") and observes
> that energy "often wanes after three and a half minutes".

## Transfer

The formalism brought to bear above is [[adaptive-submodularity]]'s
diminishing-returns law; what it does and does not carry here:

| | [[adaptive-submodularity]] |
|---|---|
| In its home field | an adaptive-monotone submodular objective over an enumerated ground set; greedy attains $1-1/e$ and the marginal gain of the $k$-th item is non-increasing |
| Here | read as a prediction that question 15 is worth less than question 5, against a protocol that bets the other way by setting a floor at 15 |
| What survives | the shape of the argument — if what a question can reveal is drawn from a fixed space, later questions must pay less, so an observed rise is evidence that the space itself moved |
| What does not | the guarantee and the objective: nothing in a burst is a measured set function, no ground set is enumerated, and the within-axis / across-axis reading is this wiki's conjecture, not a corollary of the theorem |

## Limits

- `[?]` `gregersen-2018` — carried over from before verification (`[book]`,
  `verified: prior`, no archived text). The book was not inspected here. The
  parameters above were read in the article version, *Better Brainstorming*,
  HBR March–April 2018, which `wiki/meta/sources.json` does not yet carry as
  a key; until it has one, the book key stands for both and the article is
  cited by title. Any wording the book alone may use (e.g. a "15–20" target)
  is not asserted here.
- This note's earlier claim that "the turning point comes after the 15th
  question" is withdrawn: it is in neither locus, and the article says the
  opposite about the numbers being special. Stopping's
  increasing-returns row rests on the conjecture above, not a measurement.
- The 80% figure, and the claim that a burst shifts the asker's mood, are
  Gregersen's own tallies of his own consulting sessions and surveys —
  self-reported, no control condition, no independent replication.
- Designed for a small group that includes outsiders. Solo use is mentioned
  in [[proactive-expertise-clarification|passing]]; nothing in the source measures it.

## Related

[[question-formulation-technique]] · [[unknown-unknowns]] · [[divergent-convergent]] · [[adaptive-submodularity]] · [[five-whys]]

[^s1]: gregersen-2018
