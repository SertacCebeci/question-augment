---
description: "An interview whose next question is computed, whose \"no\" is inadmissible Fix a finite attribute set $M$ and start from whatever objects are already recorded (possibly none). Then loop (Ganter 1984;"
aliases: ["attribute exploration"]
sources: ["felde-2022", "ganter-1984", "guigues-1986"]
---
# Attribute exploration

> An interview whose next question is computed, whose "no" is inadmissible
> without a witness, and which stops by running out of questions rather than
> by crossing a threshold. What it returns is the
> [[canonical-implication-basis]] of the domain, not of the transcript.

## Mechanism

Fix a finite attribute set $M$ and start from whatever objects are already[^s1][^s2][^s3]
recorded (possibly none). Then loop (Ganter 1984; restated by Felde & Stumme 2022):

1. **Compute the next premise.** Take the lectically next set $R$ that is
   closed under the implications accepted so far, via `NextClosure`.
2. **Ask.** "Does $R \to S$ hold in the domain?", where $S$ is the largest
   conclusion that follows from $R$ given the objects recorded so far.
3. **Confirm** → the implication joins the base, and every later question is
   computed modulo it.
   **Refute** → the expert *must* hand back an object $g$ with
   $R \subseteq g'$ and $S \not\subseteq g'$. That object joins the context.
   The implication $R \to S$ can never come up again, but the *premise* does:
   $R$ is put again with the conclusion recomputed in the enlarged context —
   strictly smaller each time — until it is accepted or nothing nontrivial
   follows from $R$ any more.
4. Stop when no premise remains. Every implication over $M$ then either
   follows from the accepted set or is contradicted by a recorded object.

Three things this changes for an asker:

- **Selection without a value function.** The next question is fixed by what
  has already been accepted, not by expected reduction in uncertainty.
  [[expected-information-gain]] and [[generalized-binary-search]] rank
  candidate questions by what they would buy; exploration does not rank at
  all. Its warrant is structural: the question is *determined* rather than
  chosen, no implication is ever asked twice, and no accepted implication is
  redundant. That warrant is not a budget — by step 3 a run asks one question
  per implication of the final basis **plus one more for every counterexample
  the answerer supplies**. (This accounting is read off the loop's structure
  as described above; neither ganter-1984 nor felde-2022 is cited here for
  the equality itself.)
- **A refusal is a data format.** "No" alone stalls the loop; the answerer
  owes a counterexample, fully specified over $M$. Rejection is thereby
  converted into a constraint that enters the record
  ([[constraint-as-information]]) instead of merely blocking a branch.
- **Termination is internal.** There is no $\alpha$, no $\beta$, no fidelity
  level and no novelty rate: the procedure halts because its enumeration is
  exhausted. Against [[stopping-rules]] and [[qualitative-saturation]], which
  both consume a number the asker must supply, this one supplies its own —
  at the price priced in [[unbudgetable-completeness]].

## Known as

| Name | Where | exact / close | Gloss |
|---|---|---|---|
| attribute exploration | formal concept analysis | exact | Ganter's (1984) name for this loop |
| conceptual exploration | FCA (Ganter & Obiedkov's book title) | *not this concept* | the umbrella for the family of exploration algorithms — with background implications, partial experts, multiple experts — of which this is the basic member |
| expert / oracle | knowledge acquisition | *not this concept* | names the answerer the loop requires, not the loop |
| exact learning from equivalence queries with counterexamples | computational learning theory | not claimed | the resemblance is visible but no source read here establishes the correspondence; logged as a gap rather than asserted |

## Transfer

| | |
|---|---|
| **In its home field** | knowledge acquisition: a domain expert with a complete view of a mathematical or taxonomic domain is interrogated until the implication theory of that domain is recorded |
| **Here** | the asker is the algorithm and the answerer is the expert; the attributes are the propositions the asker has declared, and the artifact is the rule set constraining $W$ |
| **What survives** | the control structure — a next-question rule with no utility, a rejection format that forces a witness, and a halt condition read off the enumeration; none of the three depends on the expert being human or the domain being mathematical |
| **What does not** | the guarantee. It holds only for an expert with a complete and correct view of the domain; against a partial or erring answerer the output is the basis of *something else*, which is exactly why Felde & Stumme (2022) had to rebuild the method for contradicting partial experts. Also lost: the assumption that a question can be *posed* as an implication over declared attributes — nothing here converts one into natural language |

## Limits

- **The load-bearing assumption is the all-knowing expert.** This note's claim
  that the output describes the domain rather than the transcript is false the
  moment the answerer guesses; a wrong "yes" is absorbed as an implication and
  silently prunes every later question that would have exposed it.
- **$M$ is fixed before the first question**, so exploration discovers
  dependencies among declared axes and never a new axis — the same relocation
  onto stall 1 that [[version-space]] makes. A counterexample that would need
  a column that does not exist cannot be entered.
- **The counterexample duty may be unpayable.** The expert must produce a
  fully specified object, not merely doubt the implication; an answerer who
  knows the rule is wrong but cannot instantiate it has no move in this
  protocol.
- **Refutation is not free, and the [[run-length|run length]] is not the basis size.** The
  question count is *at least* the number of implications in the final basis —
  itself unbounded in $|M|$ ([[canonical-implication-basis]]) — and exceeds it
  by one question per counterexample. Nothing in the protocol bounds how many
  counterexamples one premise may cost.
- **Locators are unconfirmed here.** Both works are verified to exist and to be
  on this topic, but ganter-1984's primary text could not be read in this pass
  (the reprint sits behind a publisher login) and felde-2022 only through its
  abstract. The loop above follows independent secondary restatements, so no
  section locator is claimed for it and the exact wording of the
  single-all-knowing-expert condition is unconfirmed.
- The identification of a questioning session with an exploration run is this
  wiki's; Ganter's setting is a knowledge engineer at a table of traits.

## Related

[[canonical-implication-basis]] · [[unbudgetable-completeness]] · [[version-space]] · [[generalized-binary-search]] · [[stopping-rules]] · [[elicitation-protocols]]

[^s1]: felde-2022
[^s2]: ganter-1984
[^s3]: guigues-1986
