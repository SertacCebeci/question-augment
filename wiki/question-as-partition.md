---
description: "A question's meaning *is* the cut it makes in $W$. The cut and its Three results, in the order they were established. **Hamblin (1958).** Three postulates: an answer to a question is a statement;"
aliases: ["partition semantics of questions", "Groenendijk–Stokhof partition", "question partition", "erotetic semantics"]
sources: ["belnap-1976", "ciardelli-2018", "groenendijk-1984", "hamblin-1958"]
---
# Question as a partition of possible worlds

> A question's meaning *is* the cut it makes in $W$. The cut and its
> presupposition are fixed when the question is formulated — before any answer
> arrives, and independently of who answers.

## Definition / Mechanism

Three results, in the order they were established.[^s1][^s2][^s3][^s4]

**Hamblin (1958).** Three postulates: an answer to a question is a statement;
to know the meaning of a question is to know what counts as an answer to it;
the possible answers to a question exhaust the possibilities. The second is
the operational one — a question whose answer set you cannot enumerate has no
meaning yet, only a mood.

**Belnap & Steel (1976).** A question *presupposes* a statement iff the truth
of that statement is a logically necessary condition for the question's having
a true answer. Hamblin's own example: *"In which continent is Honolulu?"*
presupposes that Honolulu is on a continent. When the presupposition is false
no direct answer is true, and the cooperative reply is a **corrective** — a
reply that is not a member of the question's answer set.

**Groenendijk & Stokhof (1984).** A question denotes, at each world, the
proposition that is the true exhaustive answer there. Since these propositions
are mutually exclusive and jointly exhaustive, the question *is* a **partition
of logical space**: each cell is one complete answer, and two worlds in the
same cell are worlds the question cannot tell apart.

```text
question Q  ≡  partition {A₁ … Aₙ} of W
presupposition of Q  ≡  A₁ ∪ … ∪ Aₙ   (the worlds where Q has a true answer)
answer  ≡  the cell containing the actual world
```

## Known as

| Name | Field | Relation |
|---|---|---|
| partition semantics of questions | formal semantics | exact |
| Groenendijk–Stokhof partition | formal semantics | exact |
| question partition | formal semantics, epistemic logic | exact |
| erotetic semantics | erotetic logic / philosophy of language | close — names the broader programme of which the partition account is one theory |

## Why it matters

1. **The resolution is set at formulation, not at answering.** The finest
   distinction a question can ever return is the cell boundary. An axis that
   runs *inside* a cell cannot be named by that question however honest or
   verbose the informant is. This is the erotetic form of the stall-1 problem:
   [[expected-information-gain]] cannot score an unmodelled axis, and erotetic
   semantics adds that the question cannot *address* one either.
2. **Asking is already an update.** By Belnap & Steel, posing $Q$ commits to
   $\bigcup_i A_i$. If the presupposition is false, that commitment deletes the
   actual world from $W$ — a destructive move, not a merely uninformative one.
   Corrective replies are therefore not answer failures; they are the only
   channel by which a presupposition error can be caught, and any answer schema
   that admits only cells discards them ([[elicitation-protocols]]).
   **This wiki's inference** (no source cited here states it): information-
   theoretic scoring is blind to this, because expected gain is computed over
   the answer set, which in the false-presupposition case is exactly the set
   that excludes the true world.
3. **A complete answer has a definition.** On stall 5: a reply is a constraint
   iff it identifies a cell. A reply that narrows without selecting a cell is a
   partial answer; a reply outside the union is a correction; a reply inside
   every cell is nothing.
4. **This wiki's inference** (neither Filmus & Mehalel nor the erotetic sources
   make the connection): it may explain the restriction [[twenty-questions]]
   leaves open. Filmus & Mehalel quantify over "restricted question sets"
   without saying where the restriction comes from; the candidate answer is
   that in natural language a question can only denote the partitions an
   interrogative can denote, not arbitrary subsets of $W$.

## Transfer

| | |
|---|---|
| **Home field** | formal semantics of natural-language interrogatives; a fixed logical space, an idealised competent speaker, truth-conditional meaning |
| **Here** | an agent choosing and formulating one question to an informant with a modelled $W$ |
| **What survives** | question = partition of the modelled $W$; presupposition = union of the cells and hence a commitment made by asking; enumerability of answers as a well-formedness test; corrective reply as a distinct reply type |
| **What does not** | exhaustivity — an agent's real questions are often mention-some ("give me one example that would break this"), which partition theory cannot type; and the assumption that $W$ is given, which is precisely what stall 1 lacks |

## Limits

- The theory **presupposes $W$**. It says which distinctions a question can
  make in a space already laid out; it generates no axis and cannot say that a
  space is missing one. On stall 1 it is a constraint on questions, not a
  discovery procedure.
- Partition semantics over-generates exhaustivity. Ciardelli, Groenendijk & Roelofsen (2018) replace the partition with a downward-closed set of
  resolving propositions to cover conditional, alternative and mention-some
  questions — under which "the cell containing the actual world" is no longer
  the right notion of an answer.
- These are semantic theories with no cost model, no noise model and no notion
  of a partly cooperative answerer. Nothing here says which partition to
  choose; that is stall 2.
- The second half of point 2 and all of point 4 in *Why it matters* are this
  wiki's own inferences, marked in place; no source cited here states either.
- Whether the false-presupposition case is *frequent* for LLM agents is an
  empirical question this note does not touch and no source cited here
  addresses.

## Related

[[possible-worlds]] · [[twenty-questions]] · [[expected-information-gain]] · [[constraint-as-information]] · [[elicitation-protocols]] · [[ambiguity-taxonomy]]

[^s1]: belnap-1976
[^s2]: ciardelli-2018
[^s3]: groenendijk-1984
[^s4]: hamblin-1958
