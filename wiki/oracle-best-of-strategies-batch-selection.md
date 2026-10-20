---
description: "An oracle for batch selection: many heuristics propose candidate batches, each is scored by true performance gain using labels, the best is kept; the gap to real strategies is diagnostic only."
aliases: ["BoSS", "Best-of-Strategies Selector", "oracle strategy for active learning"]
sources: ["arxiv-2603-13109"]
---
# Oracle best-of-strategies batch selection

An oracle selection strategy approximates the optimal choice of what to ask (label) next by using ground-truth information a real asker never has, such as labels or test data. Its purpose is diagnostic: comparing an oracle with practical strategies shows how far they deviate from the ideal, and whether the deviation sits in early cycles, late cycles, or all of them.[^c1]

## Mechanism

BoSS (Best-of-Strategies Selector) avoids the combinatorial search over subsets in three steps. First, an ensemble of existing selection strategies (Random, Margin, CoreSets, BADGE, TypiClust, DropQuery and others) each proposes candidate batches, from randomly sampled candidate pools of varying size. Second, each candidate batch is scored by how much the model improves once it is annotated, using ground-truth evaluation data. Third, the best batch is kept. To make scoring cheap, the pretrained backbone is frozen and only the final layer is retrained.[^c2]

Earlier oracles each lose scale in a different place. A simulated-annealing oracle searches over the whole labeled pool at high step cost. A greedy cross-domain oracle picks one instance at a time and retrains after every pick, so its authors extrapolated results for batches above 500.[^c3] BoSS sits between them: it judges the collective gain of a whole batch, and searching for a good batch in a large pool is simpler than searching for a whole labeled pool.[^c4]

## What it showed

The authors report that BoSS outperforms existing oracles under comparable compute, that state-of-the-art strategies still fall noticeably short of oracle performance, especially on large datasets with many classes, and that no single strategy dominates across all cycles.[^c5] The last point motivates an ensemble that switches strategies, since the oracle itself selects batches from different strategies over the course of a run.[^c6]

## Limits

The paper states that the oracle gap is not a reachable margin. It mixes (i) weaknesses of current strategies that could be fixed with (ii) advantages from supervised knowledge that are unattainable, and separating the two is left open.[^c7] Because every winning batch was proposed by some underlying strategy, an oracle built this way can never exceed what the ensemble can propose; this follows from the construction (my inference). The evidence is image classification with frozen pretrained backbones; transfer to asking in dialogue, where "performance gain of an answer" has no cheap evaluation set, is untested here.

## Related

- [[routing-ceiling]] — also an oracle best-case used to bound what choosing among modes could gain
- [[counterfactual-search-routing-oracle]] — hindsight oracle over alternatives, used as a diagnostic
- [[query-by-committee]] — a committee-based single strategy of the kind BoSS ensembles over
- [[optimal-question-asking]] — the ideal that oracles approximate

[^c1]: arxiv-2603-13109 — "Comparing the performance gap between selection strategies and the oracle strategy reveals how far these approaches deviate from the"
[^c2]: arxiv-2603-13109 — "training only the final layer during selection."
[^c3]: arxiv-2603-13109 — "extrapolated results for batch sizes above 500."
[^c4]: arxiv-2603-13109 — "Searching for an optimal batch from a large pool is considerably simpler than searching for a"
[^c5]: arxiv-2603-13109 — "Our experiments on a variety of image datasets demonstrate"
[^c6]: arxiv-2603-13109 — "strategy get selected at least once, confirming that no single strategy dominates an entire AL cycle, but there"
[^c7]: arxiv-2603-13109 — "(ii) advantages that"
