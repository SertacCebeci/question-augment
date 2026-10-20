---
description: "The same nearest-hierarchy problem that is linear-time when the answer may Take the median procedure of median-procedure-for-n-trees: for a profile $P = (T_1,\\dots,T_k)$ of hierarchies on one leaf …"
aliases: ["median binary tree problem", "complexity of the median procedure for binary trees"]
sources: ["barthelemy-1986", "jansson-2013", "mcmorris-1994"]
---
# Binary median tree hardness

> The same nearest-hierarchy problem that is linear-time when the answer may
> leave things unresolved becomes NP-hard the moment the answer is required
> to be fully resolved. Full resolution is what costs; the median itself is
> cheap.

## Definition / Mechanism

Take the median procedure of [[median-procedure-for-n-trees]]: for a profile[^s1][^s2][^s3]
$P = (T_1,\dots,T_k)$ of hierarchies on one leaf set and the symmetric
difference metric $d$, find $T$ minimising $\sum_i d(T,T_i)$. Over *all*
n-trees the minimiser is the majority-rule tree (Barthélemy & McMorris 1986
for the characterisation), and that tree is built in $O(kn)$ time — linear
in the size of the input profile — by the algorithm of Jansson, Shen & Sung 2013 (§1.2; see [[median-procedure-for-n-trees]]). A majority-rule tree is
in general **not binary**: wherever no cluster wins a strict majority it has
a polytomy — an unresolved node.

**Theorem** (McMorris & Steel 1994). Restrict the candidate set to *binary*
n-trees — every internal node with exactly two children, every grouping
decided. Then computing a median binary tree for a profile is NP-hard.

The mechanism of the loss of tractability is visible from the decomposition
of $d$: each cluster contributes independently, and the majority rule picks
the independent optimum cluster by cluster. Requiring binarity couples the
choices — a resolved node must pick *some* cluster among the sub-majority
candidates, and the candidates are mutually incompatible — so the
cluster-by-cluster argument no longer applies and the problem inherits the
combinatorics of choosing a compatible set. McMorris & Steel draw the
practical conclusion: the result argues for allowing consensus trees to
remain unresolved rather than demanding binary output.

## Why it matters

Distillation's point-versus-region disagreement — MAP wants one
world, [[rate-distortion-theory]] wants a region — has here a computational
face. Demanding a *fully resolved* distillate (one full world, no component
left open) is exactly the restriction that turns a linear-time nearest-world
computation into an NP-hard one, while permitting unresolved components
keeps it linear. The partially resolved median is not a compromise between
point and region; it is the point that is cheap to find, and full resolution
is a separately priced step. The analogy with [[backbone-of-a-formula]] is
one of *where the price sits*, not of which side is hard. Both notes divide
the distillate at the same boundary — between what the survivors force and
what the distiller chooses. The backbone theorems price *locating* that
boundary: deciding which literals every survivor carries is NP-hard, and
only a sound under-approximation is cheap. McMorris & Steel price *crossing*
it: on hierarchies the boundary is located in linear time (the majority
count), and it is committing to what lies beyond it — choosing among the
sub-majority clusters to reach a binary tree — that is NP-hard. Same
boundary, opposite step priced.

## Transfer

| | In its home field | Here |
|---|---|---|
| Binary tree | a fully resolved phylogeny, every clade decided | a fully committed world — every open component of the distillate settled |
| Polytomy | an unresolved node in a consensus tree | a component left open, parked for a later trigger |
| What survives | the cost structure: the nearest partially resolved distillate is linear-time, the nearest fully resolved one is NP-hard, and the gap is the sub-majority components | |
| What does not | the worst-case sense of NP-hardness (a small profile is resolvable by enumeration); the metric being the symmetric difference — under another loss the tractable case may differ; the fixed leaf set | |

## Limits

- **Read from the abstract.** McMorris & Steel 1994 was read at
  abstract level (Springer chapter page); the theorem statement above is
  what the abstract asserts, the "coupling" explanation of *why* is this
  note's reading and not the paper's proof, and no theorem number is cited.
- **Worst-case.** NP-hardness forbids a general polynomial guarantee; it
  does not say the median binary tree is far from the majority tree, nor
  that a given small profile is hard.
- **Binary is one notion of full resolution.** For a question tree whose
  nodes may legitimately have three or more children, "fully resolved" is not
  "binary", and the theorem as stated does not cover that case.
- **The application to distillation is this note's inference.** The cited
  source discusses phylogenies; the reading of a polytomy as a parked
  component and the "same boundary, opposite step" reading of the backbone
  analogy are the wiki's, not the sources'.

## Related

[[median-procedure-for-n-trees]] · [[backbone-of-a-formula]] · [[rate-distortion-theory]] · [[majority-distillate]] · [[bayesian-estimation]]

[^s1]: barthelemy-1986
[^s2]: jansson-2013
[^s3]: mcmorris-1994
