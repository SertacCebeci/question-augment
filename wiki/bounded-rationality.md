---
description: "Herbert Simon. Not optimal but **good enough**. And the stopping rule comes Simon 1956,"
aliases: ["satisficing", "aspiration level"]
sources: ["simon-1956", "simon-1969"]
---
# Bounded rationality and satisficing

> Herbert Simon. Not optimal but **good enough**. And the stopping rule comes
> from here.

## Satisficing

Simon 1956, *Rational Choice and the Structure of the Environment*[^s1][^s2]
(Psychological Review 63(2):129–138): instead of evaluating all options and
picking the best, set an **aspiration level** and take the first option that
exceeds it.

The reason is practical: search is costly and the option space is usually
inexhaustible.

Not the same as *satisficing* in the NFR / goal-modelling sense
([[goal-refinement-graph]]), where it is a qualitative satisfaction label
propagated over soft goals, not a threshold rule on a choice.

## Why it matters

Three consequences for anyone designing a questioning process:

**1. Do not search for the optimal question order.**
[[optimal-decision-tree]] says it is NP-hard; Simon already says *why you
should not look*: the cost of search consumes the gain.

**2. A "sufficiently consistent model" is legitimate.** Fixing onto a model
that is consistent *to a degree* is satisficing exactly: not a global optimum
but a solution above the aspiration level.

**3. Aspiration level and stopping threshold.** An aspiration level, the
$\alpha,\beta$ of [[sprt]] and the $D$ of [[rate-distortion-theory]] play the
same *role* — a declared threshold that ends search. This wiki treats them as
`close`, not identical: $\alpha,\beta$ are Type-I/II error probabilities of a
test, $D$ is a distortion bound on a reconstruction, and an aspiration level is
a threshold on an option's value. No source in this wiki identifies them.

## Simon's other contribution: problem representation

In *The Sciences of the Artificial* (Simon 1969; 3rd ed. 1996, ch. 5, p. 132)
Simon states that "solving a problem simply means representing it so as to make
the solution transparent" — the Number Scrabble / tic-tac-toe isomorphism is
his example. This is another statement of the **unmodelled axis** problem:
search in a wrong representation, however good, is search in the wrong space.

## Limits

- Satisficing gives **no rule for setting the aspiration level** — it names
  the threshold and defers it, which is exactly the open question elsewhere in
  this wiki.
- Descriptive of human behaviour; normative only under a cost-of-search
  argument.
- "Good enough" is undefined without a loss function.
- **Both sources are `[?]` unverified in `meta/sources.json`.** `simon-1956`
  carries status `unverified`; `simon-1969` was added from secondary
  quotations of the p. 132 passage, not from the book itself, and the 1969 and
  1996 editions differ in pagination and content.
- **The aspiration level / $\alpha,\beta$ / $D$ correspondence is a role
  correspondence asserted by this wiki, not a proved identity.** What does not
  carry over: the SPRT's optimality is optimality *relative to declared error
  rates* on a hypothesis test (Wald & Wolfowitz 1948), and rate–distortion
  optimality is relative to a distortion measure on a reconstruction. Neither
  guarantee transfers to a threshold on an option's value, and Simon proves no
  optimality for the aspiration level at all.

## Related

[[expected-utility]] · [[sprt]] · [[rate-distortion-theory]] · [[unknown-unknowns]] · [[goal-refinement-graph]]

[^s1]: simon-1956
[^s2]: simon-1969
