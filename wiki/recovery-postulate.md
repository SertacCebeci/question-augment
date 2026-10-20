---
description: "Whether putting a retracted answer back restores everything that died with **Recovery** is the fifth of the AGM contraction postulates (Alchourrón, Gärdenfors & Makinson 1985): Give $p$ up,"
aliases: ["recovery", "recovery postulate"]
sources: ["alchourron-1985", "hansson-1991", "hansson-2006", "makinson-1987"]
---
# The recovery postulate

> Whether putting a retracted answer back restores everything that died with
> it is not a free design choice: on a deductively closed state it is forced
> by a condition as weak as core-retainment, so an agent that wants a
> non-recoverable repair must give up closure.

## Definition / Mechanism

**Recovery** is the fifth of the AGM contraction postulates (Alchourrón,[^s1][^s2][^s3][^s4]
Gärdenfors & Makinson 1985):

$$K \subseteq (K \div p) + p$$

Give $p$ up, then put it back, and every belief you had is back. It is the
postulate that makes a retraction *reversible in the bookkeeping*, and it is
the one that has drawn the most criticism of the six — Makinson (1987)
devoted a paper to its status.

**The structural result.** Recovery is not simply a strong axiom one may
choose to drop and keep everything else. Hansson's survey states that an
operator $\div$ for a belief **set** $K$ which satisfies **core-retainment** —
the much weaker-looking demand that nothing be given up unless it contributes
to $K$ implying $p$ — thereby satisfies recovery. So on a deductively closed
state, the plausible weakening delivers the contested postulate back. The
escape route runs through closure, not through the postulate: Hansson (1991)
obtains workable contraction without recovery for *non-closed* bases, and
states the negative side as a judgement rather than a theorem — reasonable
contraction operators without recovery do not seem possible for closed belief
sets. That is why [[belief-base-revision]] is a different object rather than a
variant of AGM.

**What the failure looks like** (the coin-toss case, adapted by Hansson's SEP
entry from an example of Levi's). A base contains $c$, "the coin was tossed",
and $h$, "it landed heads", where $h$ implies $c$. Giving up $c$ must take $h$
with it. Putting $c$ back yields the consequences of the remaining base plus
$c$ — which does not contain $h$, and should not: learning again that the coin
was tossed is no reason to believe it landed heads.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Belief revision | recovery, the recovery postulate | exact |
| Belief revision | relative closure, core-retainment, relevance | *not this concept*: separate postulates that appear where recovery is dropped; core-retainment is the one that entails it on closed sets ([[kernel-contraction]]) |
| Decision theory | reversibility of a decision | *not this concept*: [[reversibility]] measures the cost of undoing an act in the world, this measures whether a belief state returns to itself; a repair can satisfy one and violate the other |

## Why it matters

For an agent that asks, recovery answers a question the rest of stall 6 does
not raise: **after a repair, how much has to be re-asked?**

Under recovery, re-obtaining the retracted answer restores the whole prior
state, so the cost of a wrong retraction is one question. Without it — which
is the situation of any agent that keeps only what it was actually told — the
answer comes back alone, and every commitment that rested on it is gone and
must be re-derived or re-asked. The two representations therefore assign
different sizes to the re-ask set after a repair, and the choice between them
is made when the agent decides what to store, long before the clash.

The result above says the two cannot be cheaply mixed. An agent that keeps a
closed state and retracts only what contributed to the implication thereby
reinstates, on re-obtaining the answer, beliefs it had good reason to abandon;
the coin-toss case is exactly the shape of a questioning failure, where a
specific answer entails a weaker one and the weak one is later re-obtained
from elsewhere.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a contraction operator on a belief set $K$ in a fixed logic | the agent's repair procedure over constraints it holds |
| $p$ | the sentence contracted | a constraint withdrawn after a clash |
| What survives | the conditional with both its premises — closure **and** core-retainment $\Rightarrow$ recovery $\Rightarrow$ "one re-ask suffices" — and the contrapositive only in its qualified form: an agent whose repairs are not recoverable either is not keeping a closed state, or is discarding answers that played no part in the implication (a core-retainment violation) | |
| What does not | the equality of "re-obtaining $p$" with "asking again and getting $p$" — the second costs a question, may return a different answer and may come from a different source, none of which the postulate models; and the assumption that the beliefs restored by $+p$ are the ones the agent wanted back rather than merely the ones the logic returns | |

## Limits

- **The core-retainment result is cited from a survey without a proof or an
  internal attribution.** Hansson's SEP entry states it; I did not verify a
  primary source for it, and the exact conditions on $K$ and $\div$ under
  which it holds are not restated here. It is the load-bearing claim of this
  note, so that gap is the note's main weakness.
- **The unqualified reading — that closure alone forces recovery — is not
  supported by anything cited here, and is not this note's claim.** An
  operator on a closed set that violates core-retainment may fail recovery;
  Hansson (1991)'s stronger statement about closed sets is a hedged judgement
  ("do not seem possible"), not a theorem, and is used here only as such.
- **Makinson (1987) is cited for the standing of the postulate, not for a
  particular result.** I confirmed the paper's bibliographic record and its
  subject, not its argument.
- **The re-ask consequence is this note's own inference.** No cited source
  discusses asking; recovery is a property of an operator, and the claim that
  it bounds the number of questions a repair costs assumes the agent's
  commitments are exactly the logical consequences of its answers.
- Recovery's failure is not by itself a recommendation: dropping it on belief
  sets has its own prices, and the operators that do so on closed states are
  not covered here.

## Related

[[belief-base-revision]] · [[kernel-contraction]] · [[agm-belief-revision]] · [[reversibility]] · [[truth-maintenance-system]]

[^s1]: alchourron-1985
[^s2]: hansson-1991
[^s3]: hansson-2006
[^s4]: makinson-1987
