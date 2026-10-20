---
description: "Training over a difficulty grid starts at the easiest cell and admits a harder neighbouring cell only once the frontier's running reward passes a threshold, so it never outruns competence."
aliases: ["diagonal wavefront scheduling", "competence-aware frontier curriculum", "gated grid curriculum"]
sources: ["arxiv-2601-00887"]
---
# Competence-gated wavefront curriculum

A curriculum orders training items from easy to hard. Most versions order them on one axis. The VideoCuRL paper argues that a linear order "risks overfitting to one modality," so it places the items on a grid and moves a frontier across it: "Instead of a linear progression, which risks overfitting to one modality, we propose a Diagonal Wavefront strategy driven by model competence."[^c1] The grid cells are the two-axis buckets of [[orthogonal-difficulty-decomposition]].

## Mechanism

Each cell B_ij carries a local competence score, an exponential moving average of the rewards its samples earn. The update is LCS(t) = γ·LCS(t−1) + (1−γ)·R̄batch, where "R̄batch is the mean reward of the current" batch drawn from the cell.[^c2] The competence is thus a smoothed training-reward signal, not a held-out test.

The active set starts at the easiest corner, B_00, and grows. A neighbouring cell with both indices no smaller (i′ ≥ i, j′ ≥ j) joins the active set only when the frontier's competence passes a threshold T, so expansion is gated and one-directional in the text as extracted: no cell is dropped.[^c3] The gate encodes a rule the authors state directly: the model "must demonstrate fundamental proficiency in simpler visual-linguistic grounding before attempting samples with high temporal" loads or complex causal chains.[^c4] The shape is a front that advances from the easy corner, so the hardest corner is reached last.

The proxies that place items on the grid are computed offline, "using only training-free proxies" that are "computed offline on CPUs."[^c5] The schedule is compared in Table 1 against random shuffling and against single-scalar curricula (length-based, generation-based); the text notes that the scalar curriculum "outperforms the random baseline," so ordering by difficulty helps even before the grid.[^c6]

## Why a gate, not a timetable

A fixed timetable would advance the curriculum regardless of whether the model has learned the current cell. The gate makes the advance depend on the observed reward, so the schedule adapts per run. The same principle appears in phase-gated curricula elsewhere in the wiki (see [[scenario-curriculum-rl]]), but there the phases form a fixed sequence, while here the gate applies to each cell of a grid and the frontier can branch.

## Limits

- The ablations read in the paper remove an axis or a stabiliser; none removes the wavefront schedule while keeping the grid, or compares it with a linear or ungated order over the same grid. The benefit of the schedule alone is therefore not isolated in the sections read.
- The threshold T, the decay γ, and the sensitivity to K = 4 are in the paper's appendices, which I did not read.
- The gate reads training reward. In the hardest cells "the model may initially fail to generate any correct responses," so the signal stays at zero and the gate never opens there. The paper pairs the schedule with a KL change for this situation (see [[zero-variance-group-waste]]); the schedule alone does not handle it.[^c7]
- Gating on the reward of the cell the model is training on can reward easy items in a cell that has mixed difficulty. This is my inference; the paper does not discuss within-cell spread.
- The paper's own limitations note leaves room for "difficulty manifold, leaving room for future refinement in continuous curriculum modeling," i.e. the grid is an approximation of a continuous landscape.[^c8]

## Related

- [[scenario-curriculum-rl]] — a five-phase curriculum gated on measured mastery; a fixed sequence rather than a grid with branching frontier
- [[learnability-posterior-curriculum]] — a learnability-guided curriculum that selects challenger tasks by posterior, rather than by a grid gate
- [[orthogonal-difficulty-decomposition]] — the two-axis grid this schedule walks
- [[zero-variance-group-waste]] — the within-group reward-variance signal, which is the same kind of training-reward signal the gate reads, for prompt selection rather than cell advance

[^c1]: arxiv-2601-00887 — "Instead of a linear progression, which risks"
[^c2]: arxiv-2601-00887 — "where R̄batch is the mean reward of the current"
[^c3]: arxiv-2601-00887 — "frontier exceeds a threshold T"
[^c4]: arxiv-2601-00887 — "must demonstrate fundamental proficiency in simpler visual-linguistic grounding before attempting samples with high temporal"
[^c5]: arxiv-2601-00887 — "that are computed offline on CPUs"
[^c6]: arxiv-2601-00887 — "easy to hard is generally beneficial"
[^c7]: arxiv-2601-00887 — "the model may initially fail to generate any correct responses"
[^c8]: arxiv-2601-00887 — "difficulty manifold, leaving room for future refinement in continuous curriculum modeling"
