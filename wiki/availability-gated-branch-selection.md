---
description: "Scores which tree node to expand next from accuracy/efficiency plus the fraction of its own hypotheses still untested, adapting exploration to what a branch has left to teach."
aliases: []
sources: ["arxiv-2604-12999"]
---
# Availability-gated branch selection

> Which branch of a tree of experiments to expand next is scored not only by
> how well it has done, but by how much of its own hypothesis space is still
> unasked — so a strong branch that has exhausted its questions loses to a
> weaker branch that has not.

## Definition / Mechanism

HypoExplore (Koo et al. (2026)) runs an evolutionary[^s1]
search over neural-architecture "hypotheses" arranged in a trajectory tree.
Before deciding *which hypothesis to test*, it first decides *where in the
tree to test from*: "we compute a branch quality score by combining task
performance and execution efficiency" — normalized validation accuracy
traded off against how close a node's training run came to a wall-clock
budget, weighted by $\lambda_{acc}$.

Quality alone would keep re-expanding the single best-scoring node forever.
The method adds a second, orthogonal score: "We define an availability
score" as one minus the fraction of a node's *active* hypotheses (those
neither confirmed nor refuted) that have already been tested, "with the
convention avail($n$) = 0 if" the node has no active hypotheses left at all
 — a node that has asked everything it can ask is worth zero regardless of
its accuracy. The two scores are combined linearly, and "where
$\lambda_{parent}$ ... trades-off branch quality and remaining search
potential. We then select as parent the expandable node with the highest
score." This makes the branch-level choice of *where to look next* a
function of local exhaustion, not just of the best number seen so far.

## Why it matters

Ablating the mechanism shows it is load-bearing, not decorative. Replacing
it with greedy, accuracy-only selection collapses to the same failure mode as
removing hypothesis-driven search altogether: "the system follows a
trajectory similar to that of the variant without hypothesis-driven search,
confirming that intelligent parent selection is critical for escaping local
optima." Against a fixed schedule — "Exploration-Exploitation annealing
(EE annealing) starts at 50% exploration and anneals toward exploitation. It
discovers high-accuracy architectures faster than other methods but
saturates shortly after, as its fixed schedule cannot adapt to accumulated
knowledge. Greedy selection plateaus earliest and lowest, exhibiting the
exploitation collapse reported in prior work" — availability gating keeps
adapting because it is read off the tree's own state at each step, not off a
clock. Any selector that must choose where to spend a next round of asking
among branches of unequal remaining potential faces the same trap a
performance-only or a time-only schedule falls into.

## Limits

Availability is defined over a fixed, enumerable hypothesis family per node
(active hypotheses excluding confirmed/refuted ones); it does not say how
that family is bounded or when a branch should be pruned outright rather
than merely deprioritized. The weighting $\lambda_{parent}$ between quality
and availability is a hand-set constant (0.60 in the paper's experiments),
not learned or adapted; a wrong weighting could still starve a promising
branch. The evidence is a single-domain ablation (image-classification
architecture search on CIFAR-10); whether availability gating transfers to
domains where "hypotheses" are not discrete, countable objects is
unverified.

## Related

- [[exploit-explore-union-selection]] — the hypothesis-level choice that runs
  inside whichever branch this mechanism selects.
- [[expected-information-gain]] — an alternative scoring criterion for what
  to ask next, computed from a single posterior rather than tree exhaustion.
- [[generalized-binary-search]] — another selection rule that scores
  candidates by how much of the space they resolve.
- [[thompson-sampling]] — the exploitation half of the companion
  hypothesis-selection mechanism.

[^s1]: arxiv-2604-12999
