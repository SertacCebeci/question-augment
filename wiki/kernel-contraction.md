---
description: "To give up a constraint you must cut every minimal set of held constraints Hansson (1994) fixes a belief base $B$ and a sentence $\\alpha$ to be given up."
aliases: ["kernel contraction"]
sources: ["alchourron-1985", "alchourron-1985-safe", "hansson-1994", "hansson-2006", "wassermann-2000"]
---
# Kernel contraction

> To give up a constraint you must cut every minimal set of held constraints
> that implies it — and the cut can be chosen one clash at a time, with no
> ranking of the agent's beliefs as a whole.

## Definition / Mechanism

Hansson (1994) fixes a belief base $B$ and a sentence $\alpha$ to be given up.[^s1][^s2][^s3][^s4][^s5]

**Kernels.** $X \in B \perp\!\!\!\perp \alpha$ iff (1) $X \subseteq B$, (2)
$\alpha \in Cn(X)$, (3) for all $Y \subset X$, $\alpha \notin Cn(Y)$. The
elements of $B \perp\!\!\!\perp \alpha$ are the **$\alpha$-kernels**: the
minimal subsets of the base that imply $\alpha$.

**Incision function.** $\sigma$ is an incision function for $B$ iff for every
$\alpha$: (1) $\sigma(B \perp\!\!\!\perp \alpha) \subseteq \bigcup (B
\perp\!\!\!\perp \alpha)$, and (2) if $\emptyset \neq X \in B
\perp\!\!\!\perp \alpha$ then $X \cap \sigma(B \perp\!\!\!\perp \alpha) \neq
\emptyset$. It cuts only sentences that take part in implying $\alpha$, and it
cuts at least one from **every** kernel.

**Kernel contraction.** $B \div_\sigma \alpha = B \setminus \sigma(B
\perp\!\!\!\perp \alpha)$.

**The characterisation.** Hansson (1994) gives an axiomatic characterisation:
an operation is a kernel contraction for $B$ iff it satisfies

- **success** — if $\alpha \notin Cn(\emptyset)$ then $\alpha \notin Cn(B \div \alpha)$;
- **inclusion** — $B \div \alpha \subseteq B$;
- **core-retainment** — if $\beta \in B$ and $\beta \notin B \div \alpha$,
  there is $B' \subseteq B$ with $\alpha \notin Cn(B')$ and $\alpha \in
  Cn(B' \cup \{\beta\})$: nothing is given up that plays no part in the
  implication;
- **uniformity** — if for all $B' \subseteq B$, $B' \vdash \alpha$ iff
  $B' \vdash \beta$, then $B \div \alpha = B \div \beta$;

and adding **relative closure**, $B \cap Cn(B \div \alpha) \subseteq B \div
\alpha$, gives the smooth kernel contractions.

Two placement facts from the paper's abstract: kernel contraction is a
**non-relational** generalisation of safe contraction (Alchourrón & Makinson
1985, which selects by a hierarchy over sentences), and it **includes all
partial meet contractions** — the construction of [[agm-belief-revision]] —
while the converse fails.

## Known as

Naming of the *object cut* is contested across fields; these are names for the
kernel, not for this operation, and are not aliases of this note.

| Field | Name there | Relation |
|---|---|---|
| Belief revision | $\alpha$-kernel | exact — the object of this note |
| TMS | nogood, minimal inconsistent environment (de Kleer 1986) | exact only for $\alpha = \bot$; a kernel for a contingent $\alpha$ is a minimal *implying* set, which is strictly more general ([[truth-maintenance-system]]) |
| SAT | minimal unsatisfiable subset (MUS), unsatisfiable core | exact for $\alpha = \bot$, same caveat |
| Model-based diagnosis | conflict set; an incision function is a hitting set of them | close — the diagnosis literature ranks hitting sets, which Hansson's $\sigma$ leaves free |
| Belief revision | safe contraction, partial meet contraction | *not this concept*: they are the two constructions this one generalises, each with its own representation theorem |

## Why it matters

Consistency records that AGM and TMS both stop one step short of
saying what to drop. Kernel contraction changes the shape of that step twice.

**The unit of repair is the minimal implying set, and every one of them must
be hit.** If two independent chains of answers each entail the constraint to
be given up, retracting inside one chain leaves $\alpha$ derivable — the
success condition fails. "Take back the last answer" is therefore not a
repair; the agent must enumerate the minimal sets and cut in each. This is the
precise sense in which a single nogood from a [[truth-maintenance-system]] is
not enough to act on.

**The choice need not be a global order.** AGM reduces the repair decision to
an entrenchment ordering over sentences — a ranking the agent must be able to
produce for pairs it will never meet. An incision function is constrained only
locally: hit each kernel, cut nothing irrelevant. Hansson's "non-relational"
is exactly this: the decision can be made per clash. Core-retainment is then
the guarantee that a repair damages no answer unrelated to the conflict, and
uniformity is the requirement that two constraints supported by exactly the
same subsets of the record be treated alike.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | sentences of a belief base under a consequence operation $Cn$ | the constraints the agent was actually told, with $Cn$ standing for the agent's own inference over them — which the "what does not" row shows the transfer cannot take for granted |
| $\alpha$ | the sentence to be given up | the constraint a clash forces out — the offending answer, or $\bot$ itself |
| $\sigma$ | an incision function on kernels | the per-conflict choice of which received answers to withdraw |
| What survives | kernels as the unit of repair; the requirement that the cut hit *every* minimal implying set (so a repair guided by one conflict set is incomplete); core-retainment as a no-collateral-damage test on a proposed repair; and the demonstration that the repair decision does not require a global ranking | |
| What does not | **the success guarantee itself**, because the construction presupposes a *Tarskian* $Cn$ (inclusion, monotony, iteration) and compactness: monotony is what makes removing an element of every kernel actually stop $\alpha$ from being derived, and compactness is what makes a *finite* minimal implying set exist at all in a growing record. An agent whose inference over natural-language answers is defeasible has neither — a set can imply $\alpha$ and a superset not, so "minimal implying set" is unstable, and cutting every kernel it found leaves $\alpha$ possibly still inferable. What transfers is the discipline (hit all currently known implying sets), not the guarantee. Also: computation — enumerating all kernels is the expensive half and the characterisation says nothing about it; uniformity, which presumes "implied by the same subsets" is checkable; and any *preference* between admissible cuts — cost of re-asking, source [[calibration|reliability]] and recency are outside $\sigma$'s constraints, so the theorem admits the worst legal repair as readily as the best | |

## Limits

- **This note's own load-bearing claim — cut every minimal implying set or
  $\alpha$ stays derivable — holds only for a monotonic, compact consequence
  operation.** That is the assumption imported with the formalism and not
  supplied by a questioning agent: under defeasible inference the kernels are
  not stable under later answers, so hitting all of them buys no success
  property, only a better-defined repair step.
- **The theorem constrains $\sigma$, it does not supply one.** Every choice
  that hits each kernel is a kernel contraction, so this note does not close
  the "which constraint to give up" gap on Consistency; it replaces a
  global ordering with a family of local choices and leaves the choice open.
- **Incompleteness fails silently.** The success guarantee holds only if
  *all* kernels were found. An agent that enumerates some of them gets a base
  that still implies what it thinks it dropped, with no signal.
- The definitions here are quoted from Wassermann's (2000) restatement and
  the postulate list from Hansson's SEP survey; I verified the paper's
  bibliographic record and abstract but not Hansson's exact stated conditions
  on $Cn$, so the standing assumptions above are the ones the construction
  needs, not ones I confirmed against his text.
- The identification of base sentences with received answers is inherited
  from [[belief-base-revision]] and is that note's transfer, not a result.

## Related

[[belief-base-revision]] · [[agm-belief-revision]] · [[recovery-postulate]] · [[truth-maintenance-system]] · [[conflict-driven-clause-learning]] · [[backbone-of-a-formula]]

[^s1]: alchourron-1985
[^s2]: alchourron-1985-safe
[^s3]: hansson-1994
[^s4]: hansson-2006
[^s5]: wassermann-2000
