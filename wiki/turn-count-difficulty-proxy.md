---
description: "The turns an agent spends on a task track how often it resolves it, so turn count can sort training trajectories into difficulty tiers without training a separate difficulty scorer."
aliases: ["trajectory-length difficulty", "turn-count difficulty", "effort-based difficulty proxy"]
sources: ["arxiv-2601-01426"]
---
# Turn count as a difficulty proxy

A curriculum needs an ordering of the training data by difficulty. The usual sources are a human rating, or a model trained to predict one. SWE-Lego uses a third signal that comes free with the data: how many turns the agent took to finish each trajectory. Across instances the authors find "a strong negative correlation (r = −0.95) between instance resolve rate and the number of turns in the trajectory."[^c1] They cut the data into three tiers, "Easy (0-50 turns), Medium (50-70 turns), and Hard (70-100 turns)", and train on them in stages.[^c2]

The alternative they tested was a scorer. A Qwen2.5-Coder-32B model fine-tuned on 1.5k human-labelled (task, difficulty) pairs "achieves 70% accuracy on a held-out test set" and sorts tasks into three estimated solving-time tiers.[^c3] The turn-count heuristic came out ahead: the authors report that it "outperformed the modelbased approach by 0.5 points", and that it is "more computationally efficient and less prone to mislabeling."[^c4][^c7]

The curriculum is cumulative. Each stage trains only on its own tier, but "the training data for each subsequent stage is augmented with all data from the preceding stages", which the authors use against forgetting.[^c5] They read the staging as easy tasks first, to fix basic reproduction failures, then hard tasks, to build the planning that avoids running out of turns; the text says the model "first grounds" on easy tasks.[^c6]

The mechanism, as I read it (my inference, not the paper's stated account): an agent that keeps acting on a task for many turns is either still making progress on something hard or failing to converge, and a solver that resolves a task quickly has a short trajectory. Turn count is therefore a behavioural measure of difficulty for the solver that produced the trajectories, not a property of the task alone.

## Limits

- The correlation is between resolve rate and turn count within one family of rollouts. The signal is relative to the solver that generated the trajectories, so a different solver could order the same tasks differently. Not tested here.
- Rollouts were capped at 100 turns (the paper sets "the maximum number of interaction turns to 100"),[^c8] so the Hard tier is bounded by the cap, and tasks that run out of turns all land in the same place.
- The tier edges at 50 and 70 turns are the authors' choice. The text shows no sensitivity analysis over them.
- The margin over the scorer is 0.5 points in one ablation, with no variance reported in the slices read.
- The data come from one teacher, one scaffold and SWE-bench-style issues. The transfer to other agent tasks is not shown.

## Related

- [[curriculum-collapse]] — a curriculum that narrows what it covers; the turn tiers here order difficulty but say nothing about how many distinct problem types each tier contains
- [[stage-level-hallucination-loss-masking]] — the same SFT run also masks erroneous steps; that masking is independent of which tier a trajectory falls in

[^c1]: arxiv-2601-01426 — "a strong negative correlation (r = −0.95) between instance resolve rate and the number of turns in the trajectory"
[^c2]: arxiv-2601-01426 — "Easy (0-50 turns), Medium (50-70 turns), and Hard (70-100 turns)"
[^c3]: arxiv-2601-01426 — "This scorer achieves 70% accuracy on a held-out test set"
[^c4]: arxiv-2601-01426 — "it outperformed the modelbased approach by 0.5 points"
[^c5]: arxiv-2601-01426 — "the training data for each subsequent stage is augmented with all data from the preceding stages"
[^c6]: arxiv-2601-01426 — "it first grounds the model on"
[^c7]: arxiv-2601-01426 — "more computationally efficient and less prone to mislabeling"
[^c8]: arxiv-2601-01426 — "set the maximum number of interaction turns to 100"
