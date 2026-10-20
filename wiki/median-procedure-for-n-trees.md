---
description: "Given several hierarchies on the same objects, the one nearest to all of An **n-tree** (hierarchy,"
aliases: ["median procedure for n-trees", "majority-rule consensus tree", "majority-rule tree", "median tree under Robinson–Foulds distance"]
sources: ["barthelemy-1981", "barthelemy-1986", "bartholdi-1989", "brown-2020", "dong-2010", "holder-2008", "jansson-2013", "margush-1981"]
---
# Median procedure for n-trees

> Given several hierarchies on the same objects, the one nearest to all of
> them — under the count of clusters they disagree on — is built by keeping
> every cluster that a strict majority carries. The count rule *is* the
> distance-minimiser, and one half is the exact threshold at which
> cluster-by-cluster selection is guaranteed to produce a hierarchy at all.
> This note's object is the majority-rule tree $\mathrm{Maj}(P)$ as the
> canonical median; the median *set* $M(P)$ is what it is drawn from, and
> the two coincide only when no cluster sits at exactly half — always for
> odd $k$.

## Definition / Mechanism

An **n-tree** (hierarchy, rooted phylogenetic tree) on a leaf set $L$ is a[^s1][^s2][^s3][^s4][^s5][^s6][^s7][^s8]
collection $C(T)$ of subsets of $L$ — *clusters* — that are pairwise
**compatible**: any two are nested or disjoint (Jansson, Shen & Sung 2013,
§1.1). A *profile* is $P = (T_1,\dots,T_k)$ on one $L$. The **symmetric
difference metric** (Robinson–Foulds) is $d(T,T') = |C(T)\,\triangle\,C(T')|$.

**The median procedure** (Barthélemy & Monjardet 1981; Barthélemy &
McMorris 1986) on any metric space returns the *set*
$M(P) = \{T : \sum_i d(T,T_i) \text{ is minimum}\}$.

**Majority rule** (Margush & McMorris 1981): writing $n_C$ for the number of
profile trees containing cluster $C$, $\mathrm{Maj}(P)$ is the tree whose
clusters are exactly those with $n_C > k/2$ — strictly more than half
(Jansson et al. 2013, §1.1).

**Theorem** (Barthélemy & McMorris 1986). With $d$ the symmetric difference
metric on n-trees, $\mathrm{Maj}(P)$ is a median of $P$ — an element of
$M(P)$ — and $\mathrm{Maj}(P)$ is the strict consensus — the intersection —
of all medians (Dong, Fernández-Baca & McMorris 2010, §Preliminaries, citing
the 1986 paper). The two objects coincide, $M(P) = \{\mathrm{Maj}(P)\}$,
exactly when no cluster sits at $n_C = k/2$ — always for odd $k$. Barthélemy
& McMorris also give axioms that characterise $M$ on this space.

Why the count rule minimises the distance, in two steps the verifier can
check:

1. *The distance decomposes cluster by cluster.* Including $C$ in $T$ costs
   one unit against each profile tree lacking it, excluding it costs one
   against each tree having it, so $\sum_i d(T,T_i) = \sum_{C \in T}(k - n_C) +
   \sum_{C \notin T} n_C$. Including $C$ changes the sum by $k - 2n_C$:
   negative iff $n_C > k/2$, zero at $n_C = k/2$, positive below. The
   unconstrained minimiser is therefore "every cluster above half, any subset
   of those at exactly half".
2. *The unconstrained minimiser is a tree.* Two clusters each present in more
   than $k/2$ of the trees are both present in at least one of them, hence
   compatible; and a pairwise-compatible cluster family is an n-tree. So
   $\mathrm{Maj}(P)$ attains the bound (Margush & McMorris 1981 establish that
   the majority collection is itself a tree). Clusters at exactly $k/2$ are
   compatible with every majority cluster but not necessarily with each
   other, which is why the median set can be larger than $\mathrm{Maj}(P)$
   and why $\mathrm{Maj}(P)$ is its intersection. For odd $k$ no cluster sits
   at half and the median is unique.

**The threshold is exact.** At any cutoff $\ell \le 1/2$ two incompatible
clusters can both pass (each in exactly half of an even profile, or each in
40 % of it), and the selected collection is not a tree. Above $1/2$ every
cutoff yields a tree; the family $M_\ell$, $\ell \in (1/2, 1]$, runs from the
majority tree to the strict consensus.

**Cost.** The majority-rule tree is built in $O(kn)$ time, linear in the
input — as reported in Jansson et al. 2013, §1.2; the originating result is
not cited here (Jansson, Shen & Sung's own $O(kn)$ algorithm is for the
majority-rule (+) tree, a different object).

**As a Bayes estimator.** Holder, Sukumaran & Lewis (2008) show the
majority-rule consensus of a posterior sample is "the optimal tree to
report" when the loss is linear in the number of incorrect clades reported
plus the number of true clades omitted, with an incorrect grouping weighed at
least as heavily as a missing one. Brown & Owen (2020) put the general form:
when the loss in a Bayes estimator is a distance, the estimator is a median
under that distance. This adds a row to [[bayesian-estimation]]'s table —
*clade-count (RF) loss → majority-rule tree* — beside *0–1 loss → MAP tree*.

## Known as

| Field | Name there | Relation |
|---|---|---|
| phylogenetics | majority-rule consensus tree, majority-rule tree | exact when $k$ is odd (the median is unique and equals $\mathrm{Maj}(P)$); in general $\mathrm{Maj}(P)$ is *a* median and the strict consensus of the median set $M(P)$ (Barthélemy & McMorris 1986; Margush & McMorris 1981) — this note's object is $\mathrm{Maj}(P)$ as the canonical median |
| phylogenetics, tree statistics | median tree under Robinson–Foulds distance | close — Brown & Owen 2020 (§Background) name "the median tree" for the unique (odd-$k$ / generic) case; for even $k$ with clusters at exactly half, $M(P)$ is a set of which $\mathrm{Maj}(P)$ is the intersection |
| classification / social choice | the median procedure | close — the general set-valued $M$ on any metric space (Barthélemy & Monjardet 1981); this note is its n-tree instance, read through its canonical element |
| phylogenetics | strict consensus tree | **not this concept** — clusters in *all* trees; the intersection of the medians, not a median |
| phylogenetics | majority-rule (+), frequency-difference, greedy / extended majority consensus | **not this concept** — they add clusters below the majority and are not medians under $d$ (Jansson et al. 2013, §1.1–1.2) |
| phylogenetics | Adams consensus | **not this concept** — built from nestings, not clusters |
| social choice | Kemeny median ranking | **not this concept** — the median procedure on total orders under Kendall distance, where pairwise majority can cycle |
| tree statistics | Fréchet mean in BHV space | **not this concept** — minimises squared geodesic distance with branch lengths (Brown & Owen 2020) |

## Why it matters

Distillation has one componentwise rule, unanimity — the literals of
[[backbone-of-a-formula]] — and a disagreement between a point (MAP) and a
region (rate–distortion) with nothing saying which a task needs. This theorem
supplies a second componentwise rule with three properties at once: it is
consistent by construction, it is the world nearest the whole surviving set
under a stated metric, and it is linear-time. And it is *coarser* than every
input: components without a majority stay unresolved, so the same object is a
point in the space of partial hierarchies and a region of full ones. The
inference this licenses for asking is filed as [[majority-distillate]].

## Transfer

| | In its home field | Here |
|---|---|---|
| Profile $P$ | $k$ trees from bootstrap replicates or an MCMC posterior sample | the surviving worlds $W$, each a nested set of commitments over one vocabulary |
| Cluster $C$ | a clade on a fixed leaf set | one commitment (a grouping of items, a subtree of a question tree) |
| $d$ | symmetric difference of cluster sets | count of commitments two worlds disagree on |
| What survives | the decomposition of a component-count distance; the strict-majority rule as its minimiser; the guarantee that above one half componentwise selection is consistent for *nested* structures; median as a coarser object; the estimator being fixed by the loss | |
| What does not | the fixed leaf set (stall 1, unsolved); the trees being draws around one truth — survivors of a constraint set are all equally consistent, and no posterior over them exists until one is written; pairwise-implies-global compatibility, which holds for hierarchies and fails for orderings; RF as the right loss | |

## Limits

- **Read through abstracts and secondary statements.** Barthélemy & McMorris
  1986 and Margush & McMorris 1981 were read at abstract level; the theorem's
  content is taken from Dong et al. 2010, Jansson et al. 2013 and Brown &
  Owen 2020, and the two-step argument above is written out so it can be
  checked, not attributed as the 1986 proof. Holder et al. 2008 was read from
  its abstract; the account of *why* the asymmetry condition is needed (a
  cutoff below half can select incompatible clades) is this note's reading.
- **The $O(kn)$ construction is cited second-hand.** It is taken from Jansson
  et al. 2013 §1.2's survey of prior work; the paper that established it is
  not read or cited here.
- **Metric-specific.** Under a different distance (path-difference, quartet,
  BHV geodesic) the median is a different tree (Brown & Owen 2020, Related
  Work); the identity with majority rule is a property of the symmetric
  difference, whose decomposition is step 1.
- **Equal votes.** Each profile tree counts once. Weighted profiles give a
  weighted majority as the weighted median (Pattengale 2005, cited by Brown
  & Owen 2020, not read here).
- **Nested structure only.** Step 2 uses that pairwise compatibility of
  clusters suffices for a hierarchy. Where components are pairwise
  preferences the analogue fails (Condorcet cycles) and the median becomes
  Kemeny's rule, NP-hard (Bartholdi, Tovey & Trick 1989, cited for this one
  fact and read from its listing).
- **Restricting to full resolution breaks it** — see
  [[binary-median-tree-hardness]].

## Related

[[backbone-of-a-formula]] · [[bayesian-estimation]] · [[rate-distortion-theory]] · [[binary-median-tree-hardness]] · [[majority-distillate]] · [[possible-worlds]]

[^s1]: barthelemy-1981
[^s2]: barthelemy-1986
[^s3]: bartholdi-1989
[^s4]: brown-2020
[^s5]: dong-2010
[^s6]: holder-2008
[^s7]: jansson-2013
[^s8]: margush-1981
