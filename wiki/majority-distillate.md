---
description: "**This wiki's inference, not a result.** When the surviving worlds can be Four steps; the middle two are someone else's. **1."
aliases: ["majority distillate", "three-tier distillate"]
sources: ["barthelemy-1986", "bartholdi-1989", "holder-2008", "margush-1981", "mcmorris-1994"]
---
# Majority distillate

> **This wiki's inference, not a result.** When the surviving worlds can be
> listed as nested sets of commitments over one vocabulary, the distillate
> should be built in three tiers by counting survivors per commitment:
> unanimous (entailed), strict-majority (chosen, with its support fraction
> reported beside it), and the rest (left open). The point-versus-region
> disagreement on stall 8 is then a disagreement about the loss, and the
> middle tier is where the two answers coincide.

## The claim

Four steps; the middle two are someone else's.[^s1][^s2][^s3][^s4][^s5]

**1. The wiki's own state.** Distillation carries one componentwise
rule — the unanimity of [[backbone-of-a-formula]], whose literals are
entailed by the answers — and records MAP ([[bayesian-estimation]]) against
[[rate-distortion-theory]] as point versus region with nothing deciding
between them.

**2. The median theorem.** For nested structures under the count of
differing components, the world nearest the whole surviving set is the
strict-majority collection, it is consistent by construction, one half is
the exact threshold at which that guarantee starts, and it is linear-time
(Barthélemy & McMorris 1986; Margush & McMorris 1981 —
[[median-procedure-for-n-trees]]). It is the Bayes estimator under a loss
linear in false and missing components (Holder, Sukumaran & Lewis 2008),
where MAP is the Bayes estimator under 0–1 loss.

**3. The price of full resolution.** Requiring the median — the nearest
world under the *component-count* loss — to be fully resolved makes that
problem NP-hard (McMorris & Steel 1994 — [[binary-median-tree-hardness]]).

**4. The inference.** Read the surviving $W$ as a profile and each world's
nested commitments as its clusters. Then:

- *Three tiers fall out of one count.* A commitment carried by all survivors
  is backbone — entailed, adding nothing. One carried by a strict majority is
  chosen, and the choice carries a number, its support fraction: how many
  consistent completions carry the commitment. That number is a second,
  different marker from the attribution the backbone note demands — an
  answer, a question that licensed the line ([[constraint-as-information]]'s
  hidden-assumption test) — and it is reported *beside* that missing
  attribution, not instead of it: a majority-tier line still rests on no
  answer, and the distillate says so. One carried by no majority is left
  open. The family $M_\ell$, $\ell \in (1/2, 1]$, is the dial between the
  second and first tiers, every setting consistent.
- *Point versus region dissolves into a loss.* Three objects, not two.
  (a) 0–1 loss over full worlds gives MAP: one full world, the posterior
  mode, cheap once $W$ is enumerated with weights. (b) Component-count loss
  over all partial commitment sets gives the majority tier: a point in the
  lattice of partial commitments that is at the same time a region of full
  worlds, linear-time. (c) Component-count loss restricted to full worlds
  gives the binary median: NP-hard (step 3). The point-versus-region choice
  on the map is a choice between (a) and (b) — a choice of loss; (c) is the
  price of asking for (b)'s optimality in (a)'s shape, and no cited result
  says (a) itself is hard. The open tier of (b) *is* the parked region of
  rate–distortion, but computed from the survivors rather than declared as
  a tolerance.
- *The cutoff is a function of the cost ratio.* Let $c_w$ be the cost of
  writing a wrong commitment into the distillate and $c_m$ the cost of
  leaving a true one open. A commitment of support $p$ is worth writing iff
  $(1-p)\,c_w < p\,c_m$, i.e. $p > c_w/(c_w + c_m)$. So the cutoff is
  $\ell = c_w/(c_w + c_m)$, and $\ell \ge 1/2$ exactly when $c_w \ge c_m$ —
  Holder et al.'s condition that a false grouping weighs at least as much as
  a missed one. The quantity a procedure declares is the ratio $c_w/c_m$;
  a ratio below one puts $\ell$ below one half, where the count can select
  incompatible commitments, and is inadmissible.

What changes for a derived procedure: distillation of a structured $W$ is
one count per commitment, followed by three writes — the unanimous tier as
fact, the majority tier with its fraction and an explicit "no answer
licenses this line", the remainder as an explicit open list — and the only
free parameter is the cost ratio $c_w/c_m$, not a tolerance measure
$d_{ij}$ or a relevance variable.

## Known as

| Field | Name there | Relation |
|---|---|---|
| this wiki | majority distillate, three-tier distillate | exact — the name of this inference |
| phylogenetics | majority-rule consensus tree | **not this concept** — the theorem this rests on ([[median-procedure-for-n-trees]]); this note is its application to a surviving world set |
| constraint satisfaction | backbone | **not this concept** — the unanimous tier only ([[backbone-of-a-formula]]) |

## Transfer

| | |
|---|---|
| **Home field** | Phylogenetics: a profile of trees on one leaf set — bootstrap replicates or MCMC samples drawn around one true tree — with Robinson–Foulds (symmetric-difference) loss and, in the Bayesian reading, a posterior over trees. |
| **Here** | An enumerated $W$ of nested commitment sets over one fixed vocabulary; one count per commitment across survivors; no posterior, no sampling process, no ground-truth world. |
| **What survives** | The count rule as the minimiser of summed component distance; consistency of the strict-majority collection, with one half as the exact threshold; the result being coarser than every survivor; the loss-fixes-estimator reading that turns point-versus-region into a loss choice. |
| **What does not** | The posterior, and with it the Bayes-estimator warrant for step 2 — the count here measures the geometry of the model set, not evidence; the fixed vocabulary, which stall 1 says a session does not have; nestedness of a session's commitments, which is assumed, not shown; and RF as the right loss — a different loss yields a different estimator (Brown & Owen 2020 in [[median-procedure-for-n-trees]]). |

## Limits

- **No source discusses asking.** The identification of a surviving world
  with a profile tree, and of a nested commitment (a subtree of a question
  tree, a grouping of requirements) with a cluster, is this wiki's. The
  theorem is stated for hierarchies; whether the commitments a questioning
  session produces are nested is an assumption, not a finding.
- **Survivors are not samples.** A phylogenetic profile is drawn around one
  truth; the survivors of a constraint set are all equally consistent with
  the answers. A majority among them measures the geometry of the model set —
  how many consistent completions carry a commitment — not evidence for it.
  Two survivors differing only in an irrelevant component count as two
  votes. The Bayes-estimator reading (step 2) needs a posterior over $W$ that
  nothing in the wiki supplies.
- **Enumeration is assumed.** The count needs $W$ listed. [[version-space]]
  gives the list for a declared hypothesis language and warns that its
  boundary sets can grow exponentially; the backbone note gives the models of
  a formula at NP cost. This note starts where either ends.
- **Nested structure only.** Where commitments are orderings or arbitrary
  constraints, componentwise majority can be inconsistent and the median is
  NP-hard (Bartholdi, Tovey & Trick 1989 for Kemeny's rule). A question tree
  is nested; a preference over options is not.
- **The cost-ratio reading of the cutoff is unsourced.** Holder et al. state
  the asymmetry condition; the derivation $\ell = c_w/(c_w + c_m)$ is the
  standard Bayes-threshold algebra applied by this note, not their claim,
  and it presumes the support fraction can stand in for a probability —
  which the previous bullet says it cannot without a posterior.

## Related

[[median-procedure-for-n-trees]] · [[binary-median-tree-hardness]] · [[backbone-of-a-formula]] · [[bayesian-estimation]] · [[rate-distortion-theory]] · [[version-space]]

[^s1]: barthelemy-1986
[^s2]: bartholdi-1989
[^s3]: holder-2008
[^s4]: margush-1981
[^s5]: mcmorris-1994
