---
description: "Change the finite set of sentences the agent was actually given, not its A **belief base** $B$ is a set of sentences that is *not* closed under consequence. The agent's beliefs are $Cn(B)$;"
aliases: ["base revision", "base contraction", "belief base contraction"]
sources: ["alchourron-1985", "fuhrmann-1991", "hansson-1991", "hansson-1992", "hansson-2006"]
---
# Belief base revision

> Change the finite set of sentences the agent was actually given, not its
> deductive closure — and the repair candidates become exactly the answers it
> can go back and re-ask.

## Definition / Mechanism

A **belief base** $B$ is a set of sentences that is *not* closed under[^s1][^s2][^s3][^s4][^s5]
consequence. The agent's beliefs are $Cn(B)$; the elements of
$Cn(B) \setminus B$ are, in Hansson's words, "merely derived", i.e. they have
no independent standing, whereas the elements of $B$ are held independently of
any other belief (Hansson, *Logic of Belief Revision*, SEP). Operations —
contraction $B \div p$, non-closing expansion $B +' p = B \cup \{p\}$,
revision — apply to $B$; the belief set moves as a side effect.

Three consequences the framework is built on.

**Base dependence.** One belief set has many bases, and they behave
differently. Hansson's example: Abe holds $\{p, q\}$, Bob holds
$\{p, p \leftrightarrow q\}$; the two bases have identical consequences, but
after taking in $\neg p$ Abe still holds $q$ and Bob does not. The record of
*what was asserted* is therefore part of the state, not presentation.

**Different postulates.** Partial meet contraction on a base is characterised
(Hansson 1999, as presented in the SEP entry) by **success**, **inclusion**,
**relevance** — if $q$ is lost then some $A'$ with $A \div p \subseteq A'
\subseteq A$ has $p \notin Cn(A')$ but $p \in Cn(A' \cup \{q\})$ — and
**uniformity**. [[recovery-postulate]], AGM's guarantee that a retraction is
undone by putting the sentence back, is absent, and Hansson (1991) is the
paper that shows workable contraction without it.

**A second route for revision.** With a base, the intermediate state of a
revision may be inconsistent, so *external* revision $(B +' p) \div \neg p$ —
take the answer in first, repair afterwards — is available beside the AGM
order $(B \div \neg p) +' p$. For a closed belief set the external route is
empty: the only inconsistent closed set is the whole language.

Base contraction was developed independently by Fuhrmann (1991), who obtained
theory contraction *through* base contraction; Hansson (1992) defended it
against the objection that a belief state should not depend on syntax.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Belief revision | base contraction / base revision | exact — the same operations on the same object |
| Belief revision | **base-generated contraction** ($K \div p = Cn(A - p)$) | *not this concept*: it is the operation induced on the closure, characterised by its own postulates (finitude, symmetry, conservativity) and measured on belief sets |
| Epistemology, AI (Doyle, Harman) | foundations theory (vs. coherence theory) | close — the philosophical position that beliefs need reasons; this note is one formal system compatible with it, not the position |
| Belief revision | AGM revision | *not this concept*: $K$ is deductively closed there, and the scope call of 2026-09-08 records that the literature measures the two as different objects ([[agm-belief-revision]]) |

## Why it matters

Consistency records that no field on stall 6 says *which* constraint
to give up. This one narrows the question before answering it. A questioning
agent's constraints arrive as answers; everything else it holds is inferred.
[[agm-belief-revision]] cannot represent that difference — its own `## Limits`
says so — and therefore cannot say which of the sentences in a clash is one
the agent could go back and re-ask. On a base the retraction candidates are
the received answers, the set is finite, and the derived constraints die on
their own when their support is cut, with no separate decision.

Base dependence turns a bookkeeping choice into a decision-relevant one: two
agents whose current beliefs coincide but whose answer logs differ will repair
differently, and neither is wrong. Keeping the raw answers rather than the
closure is not tidiness, it changes the outcome.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a finite set $B$ of sentences in a fixed logic, not closed under $Cn$ | the log of answers as received, one entry per assertion actually made to the agent |
| Derived belief | an element of $Cn(B) \setminus B$ | a constraint the agent inferred but was never told |
| Operation | contraction / internal or external revision on $B$ | dropping a received answer, or taking a contradicting one in and repairing after |
| What survives | the explicit/derived split, which makes the retraction candidate set finite and equal to the answer log; base dependence, which makes the record load-bearing; the availability of the external order (accept the answer, repair after) that closure forbids | |
| What does not | decidability — "merely derived" is computable only if $Cn$ is, and the consequences of a natural-language answer are not enumerable; the assumption that the base is the agent's own assertions rather than a mixture of answers, defaults and inferences it forgot to mark; and any account of where the base came from — cost, source and re-askability of an answer play no role in any of these operators | |

## Limits

- **The identification of a base element with a received answer is this
  note's own transfer, not a result.** None of the cited sources discusses
  asking; if the agent logs an inferred commitment as if it were an answer,
  the explicit/derived distinction it is buying disappears silently.
- **Base dependence is also the standing objection.** If two records of the
  same belief state repair differently, an arbitrary logging convention
  produces an arbitrary repair; Hansson (1992) is a defence because the charge
  is live, not because it was settled.
- **Which element to cut is still stipulated.** The framework says the
  culprit is drawn from the base; the selection is a function the theory takes
  as given, exactly as AGM takes entrenchment as given. [[kernel-contraction]]
  constrains that function but does not derive it.
- **Success survives.** Base revision still accepts the incoming sentence
  unconditionally; the operator family in which a late answer may be the one
  rejected is a separate construction and is not in this note.
- The postulate lists and the Abe/Bob example are taken from Hansson's SEP
  survey rather than from the 1991/1992 papers, which I did not read in full.

## Related

[[agm-belief-revision]] · [[kernel-contraction]] · [[recovery-postulate]] · [[truth-maintenance-system]] · [[constraint-as-information]] · [[conflict-driven-clause-learning]]

[^s1]: alchourron-1985
[^s2]: fuhrmann-1991
[^s3]: hansson-1991
[^s4]: hansson-1992
[^s5]: hansson-2006
