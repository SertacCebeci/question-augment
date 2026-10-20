---
description: "A contradiction is not only damage. It entails a new constraint that nobody DPLL alternates decision and propagation: branch on a variable, then derive what the clauses force (Davis,"
aliases: ["CDCL", "clause learning", "conflict-driven learning", "conflict-driven clause learning"]
sources: ["bayardo-1997", "davis-1962", "haken-1985", "marques-silva-1999", "pipatsrisawat-2011", "zhang-2001"]
---
# Conflict-driven clause learning

> A contradiction is not only damage. It entails a new constraint that nobody
> supplied, and the solver's advantage comes from writing that constraint down,
> so the same combination is not re-derived while the clause is kept — the
> deletion policy being itself part of the method.

## Definition / Mechanism

DPLL alternates decision and propagation: branch on a variable, then derive[^s1][^s2][^s3][^s4][^s5][^s6]
what the clauses force (Davis, Logemann & Loveland 1962). Marques-Silva &
Sakallah (1999) added the step that defines the modern solver — GRASP is
"premised on the inevitability of conflicts" and augments backtracking with a
conflict analysis procedure that (a) adds a clause and (b) backtracks
non-chronologically to the level the analysis names.

Zhang, Madigan, Moskewicz & Malik (2001) give the mechanism. Four facts carry
the rest of this note:

- **The antecedent record.** Every implied assignment is stored with the clause
  that was unit when the implication happened. These pointers form the
  **implication graph**; a conflict is a variable with both a 0- and a 1-vertex.
  Without the record there is no graph.
- **The learned clause is a chosen cut.** A **conflict clause** is read off a
  bipartition of that graph — decisions on the *reason side*, the conflicting
  variable on the *conflict side*, the reason-side vertices with an edge
  crossing the cut forming the clause. Different cuts are different learning
  schemes; each is derived by replacing literals with their antecedent literals,
  i.e. by resolution against clauses already held, so the **learnt clause** is
  entailed by what was already there.
- **The asserting requirement.** The cut must yield an **asserting clause**:
  after backjumping it becomes unit and *forces* a value. This requires exactly
  one current-level **UIP** (a vertex dominating both vertices of the
  conflicting variable) on the reason side. A record that does not change the
  next move is not worth making. Retained clauses also make restarts cheap,
  since discarding the search is not a waste while they are present.
- **Bounded forgetting.** Bayardo & Schrag (1997) made large real-world
  instances tractable with **relevance-bounded learning** — keep a learned
  clause only while it is close to the current assignment, delete it otherwise.

Pipatsrisawat & Darwiche (2011) bound the power: for a solver with a
non-deterministic branching heuristic and restarts allowed, CDCL yields proof
systems that **p-simulate general resolution**, with no extra techniques
needed. Recording only conflicts actually hit costs nothing in principle.

## Known as

| Name | Field | Relation |
|---|---|---|
| conflict-driven learning, clause learning | SAT | exact — this note (Zhang et al. 2001 use "learning" for the conflict-driven case throughout) |
| conflict analysis | SAT | close — the sub-procedure inside CDCL that computes the learned clause and the backjump level (Marques-Silva & Sakallah 1999); CDCL names the whole decide/propagate/analyse/backjump/forget loop |
| look-back learning, relevance-bounded learning | constraint satisfaction | close — the CSP-side family Bayardo & Schrag imported from |
| nogood recording | CSP, TMS | close — a set known inconsistent, without the cut choice or the asserting requirement ([[truth-maintenance-system]]) |
| backjumping / non-chronological backtracking | SAT, CSP | close — the movement CDCL makes *after* learning; usable without learning |

## Why it matters

Consistency records that stall 6 detects and does not repair. This is
a repair, and its shape is not the one the other notes assume.

1. **The clash pays.** The conflict is resolved into a clause *entailed by the
   constraints already held*. It is information the agent obtains without
   asking anyone — a place where $|W|$ shrinks with no question spent
   ([[expected-information-gain]] prices questions; this move has no price).
2. **Nothing received is retracted.** CDCL undoes only its own **decisions** —
   the values the agent fixed where the answers left it free. [[agm-belief-revision]]'s
   question ("which constraint do I give up?") does not arise while every input
   clause is a given. What gets given up is an assumption, and the learned
   clause is precisely the reason it may never be made again.
3. **"Record the conflict" is underspecified.** Which constraint you learn is
   a cut, the cuts differ measurably in what they buy, and the good cut is the
   one that forces the next move. A conflict log that names the participants
   without asserting anything is the min-cut scheme — small, cheap, and among
   the worst performers.
4. **The record is deliberately forgotten.** The relevance bound says a
   permanent memory of every past contradiction is not the optimum; the clause
   database is pruned by distance from where the search now is.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a CNF formula and a partial assignment | the answers received, plus the values the agent fixed itself |
| Decision vs implication | branch variable vs unit-propagated literal | a silent fork the agent chose vs a value an answer forced |
| Conflict | a variable assigned both 0 and 1 | $\|W\| = 0$ on a shared variable ([[constraint-as-information]]) |
| What survives | the antecedent record as the precondition of analysis; the cut as a *choice* of what to learn; the asserting requirement; relevance-bounded forgetting; retract-your-own-decision rather than a received constraint |
| What does not | CNF and a fixed variable set (stall 1 is unsolved, and answers arrive as prose). And the fiat that input clauses are true: a learned clause is unretractable, which is sound only because SAT's inputs cannot be wrong. An erroneous answer produces learned clauses exactly as a correct one does, and they outlive it. |

## Limits

- **Requires the antecedent to have been recorded at the time.** No implication
  graph, no cut. This is the same bookkeeping precondition as
  [[truth-maintenance-system]], and an agent that reasons in prose does not
  meet it by default.
- **Detection is assumed.** Propagation finds the conflict because the
  constraints are formal and the variable set is closed. Nothing here detects
  a clash between answers that share no variable — the second open item on
  Consistency.
- **The p-simulation guarantee is about an idealised CDCL** whose decisions may
  be chosen adversarially well; it says nothing about what any particular
  branching heuristic achieves — which is why the scheme comparison below is
  empirical rather than derived.
- **Learning does not defeat hardness.** Resolution has exponential lower
  bounds — Haken (1985) proved the pigeonhole tautologies have no polynomial
  resolution proof. There are contradiction structures no amount of learning
  makes cheap.
- **1UIP's superiority is empirical and dated.** Zhang et al. measured the
  first-UIP cut at least 2x better than min-cut, all-UIP, decision, rel_sat and
  GRASP schemes in 2001, on verification benchmarks with zChaff, and note that
  learning interacts with the branching heuristic, so "effectiveness ... can
  only be determined by empirical data for the entire solution process."
- **The application to asking is this note's inference**, including the claim
  in *Why it matters* 1 that a conflict is a free $|W|$ reduction. No cited
  source discusses questions; the Transfer row names what did not come across.

## Related

[[truth-maintenance-system]] · [[agm-belief-revision]] · [[constraint-as-information]] · [[backbone-of-a-formula]] · [[expected-information-gain]] · [[possible-worlds]]

[^s1]: bayardo-1997
[^s2]: davis-1962
[^s3]: haken-1985
[^s4]: marques-silva-1999
[^s5]: pipatsrisawat-2011
[^s6]: zhang-2001
