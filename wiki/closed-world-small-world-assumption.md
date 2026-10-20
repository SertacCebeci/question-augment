---
description: "Closed-world and small-world assumptions demand an exhaustive list of world states at natural granularity; a catch-all state has no specifiable consequences, so neither patch is safe."
aliases: ["closed world assumption", "small world assumption", "small world problem", "closed world problem"]
sources: ["arxiv-2512-05677"]
---
# Closed-world and small-world assumptions

Classical decision analysis is conditional analysis. The decision is analysed
"conditional on some fixed and well-defined set of hypothetical worlds", and
it must be possible "to clearly state which decision would lead to which
consequence in each of these hypothetical worlds".[^c1] A decision becomes a
random variable on those worlds: "a decision needs to be completely
identifiable with the random variable describing it on the set of states of
the world."[^c2] The two idealisations that make this possible are named
separately in the paper.

**Closed-world assumption (CWA).** Before the analysis, "an exhaustive,
informative, and mutually exclusive list of all states relevant for the
problem" can be written down, and the consequence of each act in each state is
specifiable. "Specifically, if a state is not contained in the list, it is
assumed to be impossible to occur."[^c3] The term is borrowed from database
theory, where it "states that what is currently not known about a system is
assumed to be false."[^c4]

**Small-world assumption (SWA).** "There is a natural granularity of the states
of the world" for the problem at hand, and finer or coarser partitions are
treated as unnatural.[^c5] The paper's concern is that the answer then depends
on the framing. Invariance to the granularity would fix that, but the authors
argue that a choice function with full granularity invariance is nearly
useless: "will be the identity map, which is obviously useless for any
meaningful" analysis.[^c6]

## Why the usual patches fail

The obvious repair for CWA is to add an artificial catch-all state s\* that
occurs when none of the listed states does. The paper's objection is that CWA
also needs consequences under each state. "Closer inspection clarifies that
CWA also requires that under each state the consequences of the actions must
be clearly specifiable."[^c7] A catch-all state cannot be described, so the
consequences under it cannot be given.

The two assumptions also trade against each other. The paper says they "are by
no means independent of each other": the catch-all state that rescues CWA is
"probably only in extremely rare cases" a state whose granularity can be
judged natural, so one is often violated by deliberately violating the other.[^c8]

A related sub-assumption is that acts do not affect which states occur. In
Savage's model "the acts are assumed (by construction) to not influence" the
availability and probability of states.[^c9] Newcomb-type problems, which the
paper says prominently triggered the subfield on act-state dependence, are the
known cases where this fails; the paper counts it as a sub-assumption of
SWA.[^c12]

The running example is a clock-out machine with five coloured cards. The paper
judges that "neither CWA nor SWA are sensibly acceptable", since only the
monetary outcomes are observed and no account of the dynamics is available.[^c10]

## Limits

- The paper argues the case; it does not measure how often CWA or SWA fail in
  practice, or how far the resulting decisions are off.
- The argument is about *specifiability* of states and consequences, not about
  whether a fine enough state list exists in principle. A modeller who can
  name the states and their consequences is not affected.
- The paper's own alternative does not remove the cost. It gives up the state
  space and "the sparseness of assumptions has to come at a price" in
  guarantees that stay empirical and depend on the i.i.d. sampling assumption
  ([[empirical-decision-problem]]).[^c11]

## Related

- [[possible-worlds]] — the enumerated list of worlds that CWA presupposes and that SWA asks to be natural
- [[unknown-unknowns]] — what a closed list cannot contain by construction
- [[empirical-decision-problem]] — the approach that avoids both assumptions by dropping the state space
- [[expected-utility]] — the classical rule that needs the state space to be defined

[^c1]: arxiv-2512-05677 — "conditional on some fixed and well-defined set of hypothetical worlds"
[^c2]: arxiv-2512-05677 — "random variable describing it on the set of states of the world"
[^c3]: arxiv-2512-05677 — "Specifically, if a state is not contained in the list, it is assumed to be impossible to occur"
[^c4]: arxiv-2512-05677 — "what is currently not known about a system is assumed to be false"
[^c5]: arxiv-2512-05677 — "there is a natural granularity of the states"
[^c6]: arxiv-2512-05677 — "will be the identity map, which is obviously useless for any meaningful"
[^c7]: arxiv-2512-05677 — "closer inspection clarifies that CWA also requires that under each state the"
[^c8]: arxiv-2512-05677 — "are by no means independent of each other"
[^c9]: arxiv-2512-05677 — "the acts are assumed (by construction) to not influence"
[^c10]: arxiv-2512-05677 — "neither CWA nor SWA are sensibly acceptable"
[^c11]: arxiv-2512-05677 — "the sparseness of assumptions has to come at a price"
[^c12]: arxiv-2512-05677 — "prominently triggered by Newcomb"
