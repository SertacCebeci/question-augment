---
description: "Splitting a problem into disjoint, exhaustive sub-problems. Named and **MECE** — **M**utually **E**xclusive,"
aliases: ["MECE", "logic tree", "hypothesis tree"]
sources: ["minto-1987", "rasiel-1999"]
---
# Issue tree

> Splitting a problem into disjoint, exhaustive sub-problems. Named and
> taught by Minto (1987) at McKinsey, structurally identical to any question
> tree.

## Definition / Mechanism

**MECE** — **M**utually **E**xclusive, **C**ollectively **E**xhaustive — is[^s1][^s2]
Minto's (1987) criterion for the branches under any node of a pyramid:

```text
Mutually exclusive      →  branches do not overlap  (no redundancy)
Collectively exhaustive →  branches cover everything (no gaps)
```

Minto invented the term at McKinsey in the late 1960s; it reached general
consulting practice through her book and through Rasiel (1999), who reports
it as "a sine qua non of the problem-solving process" there.

Minto's chapter 9 (*Structuring the Analysis of the Problem*) separates two
kinds of structure, and the split survives outside consulting:

```text
DIAGNOSTIC FRAMEWORK   "why did this happen?"    —  cause tree
LOGIC TREE             "what could we do?"       —  action / option tree
```

An inquiry uses both: design decisions form an option tree, contradiction
hunting a cause tree.

## Known as

| Name | Match | Note |
|---|---|---|
| logic tree | exact | Minto's own term for the option/action side of the same structure |
| hypothesis tree | close | the hypothesis-first variant: branches are candidate answers, tested rather than enumerated |
| MECE | close | **not a synonym.** MECE is the criterion a node's branches must satisfy; a tree can be drawn without it and usually is |

## Why it matters

The two halves of MECE bear on two separate concerns when asking. The
correspondence below is this note's own reading, not a result: submodularity
penalises redundant *gain*, while mutual exclusivity constrains the
*partition*, and no derivation connects them.

| MECE half | Concern when asking | Nearest formal counterpart |
|---|---|---|
| Mutually exclusive | question repetition / redundancy | [[adaptive-submodularity]] |
| Collectively exhaustive | coverage / unmodelled axis | [[unknown-unknowns]] |

And MECE has a known weakness: **you cannot prove exhaustiveness.** A
tree's completeness is defined only relative to a taxonomy; you cannot see
outside the taxonomy.

## Its practical value

Still worth it: because the tree is **written down**, which branch remains
unopened is visible. A **frontier** — the list of unopened branches — is
exactly this: bookkeeping, not measurement.

## Limits

- Exhaustiveness is unprovable; it is relative to the taxonomy — the note's
  own point.
- The frontier is complete bookkeeping only over the taxonomy in force when
  the tree was drawn. Discovering a new axis silently invalidates a frontier
  that reads as empty, so "no branches left" is not "nothing left to ask"
  ([[unknown-unknowns]]).
- "Mutually exclusive" has no formal criterion for fuzzy categories.
- Trees force hierarchy onto problems that are graphs.
- Both sources are practitioner books, not results: the MECE criterion has
  no proof attached, and nothing here is an empirical claim about whether
  MECE-structured inquiry performs better.

## Related

[[unknown-unknowns]] · [[adaptive-submodularity]] · [[stopping-rules]] · [[optimal-decision-tree]]

[^s1]: minto-1987
[^s2]: rasiel-1999
