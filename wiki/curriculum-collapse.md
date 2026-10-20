---
description: "Self-evolving questioners drift into a few high-reward problem types; a persistent cluster-visit memory with a rarity bonus gated by solvability restores semantic coverage of generated questions."
aliases: ["diversity illusion", "cross-iteration coverage reward", "question-side mode collapse", "Prism"]
sources: ["arxiv-2603-13309", "arxiv-2512-18160"]
---
# Curriculum collapse

In a questioner-solver loop, the questioner's output is the solver's whole training distribution. If the questioner's reward only checks difficulty, it converges on a narrow set of problem types that reliably score, and the solver stops meeting new strategies. The work calls this curriculum collapse: "the Questioner concentrates on a narrow slice of the problem space as training progresses, reducing semantic coverage across iterations".[^c1] It argues the bottleneck is therefore upstream of the solver: "a solver cannot learn strategies it is never prompted to exercise."[^c2]

## Why difficulty gating and lexical penalties do not prevent it

A solvability gate (reward only questions the solver gets right about 50-90% of the time) controls difficulty but puts no pressure on where in problem space questions fall. R-Zero's BLEU-based repetition penalty is lexical, batch-local and has no memory across iterations, so it cannot see that two differently worded questions are the same problem.[^c3] The measured result: under R-Zero, active semantic clusters (of 128) fell from 89 for the base model to 65, the Gini coefficient rose to 0.90, and one cluster held 951 questions, mostly structurally near-identical polynomial-divisibility problems.[^c4]

## The countermeasure measured

Questions are embedded and assigned to one of K=128 fixed k-means clusters built once from the MATH training set. A per-cluster visit count is kept as an exponential moving average and warm-started across iterations, giving memory a batch penalty lacks. A question's reward is the solvability gate multiplied by (1 + lambda times a rarity bonus exp(-n_c / mean n)). The product form means a rare-cluster question that is trivial or unsolvable still earns zero.[^c5] A second change initialises each iteration's questioner from the latest solver rather than the previous questioner.

Measured coverage: Prism reached 107 of 128 active clusters, normalised entropy 0.83 and Gini 0.66, below the base model's 0.81.[^c6] On Qwen3-4B-Base it gave the best Pass@1 on six of seven math benchmarks, e.g. AMC 61.25 vs 57.27 for R-Zero.[^c7] In a 2x2 ablation on MATH-500, the diversity reward alone gave 80.46 against 79.60, solver-initialisation alone gave 79.12, and both gave 81.02. The authors' reading is that a solver-derived prior is not calibrated for proposing questions, so it needs an explicit question-side objective.[^c8] The weight matters: lambda=1 gave 78.32 and lambda=8 gave 78.80, against 81.02 at lambda=5. The authors say too large a weight makes the questioner chase obscure clusters at the cost of edge-of-solvability quality.[^c9] The overhead was about 1.7% of iteration time.[^c10]

## A context-side countermeasure

A different remedy appears in PSV, a proposer-solver loop for verified Rust. There the proposer's in-context examples are resampled every round from the growing pool of problems, not fixed. The ablation replaces that with "sampling only once from the seed dataset", and the authors report that it "causes an average drop of 10.6% across all metrics."[^c12][^c13] The diversity effect is measured as uniqueness, not as semantic coverage: the refreshed prompt gives "rate on average (45.3% vs 29.3%), which leads to 2.48×" more unique questions than the fixed one.[^c14] So the fix works on the proposer's input rather than on its reward. It does not supply a cluster-level coverage measure of the kind used here, and the two are not compared in the source.

## Limits

- The partition is static, built from MATH training problems, so the method is not data-free and cannot represent problem types outside that corpus; it does not reward composing skills across clusters.[^c11]
- Coverage is both optimised and measured in the same embedding space, with one embedding model and no ablation over others; the authors concede independent metrics would strengthen the analysis.[^c11]
- One base model, one domain (math), outcome-only rewards, 4 iterations, single reported runs; no variance is shown (my observation). The gain from coverage alone on MATH-500 (+0.86) is small, and causal attribution of benchmark gains to coverage is correlational (my inference).
- The "collapse" claim rests on one baseline reimplemented by the authors; the gains on AIME 2025 went to another system (SPICE, 19.10 vs 12.92).[^c7]

## Related

- [[questioning-diversity]] — a question-set pairwise embedding distance; the same redundancy concern, measured rather than rewarded
- [[learnability-posterior-curriculum]] — also steers a self-play questioner by learnability, but through topic posteriors rather than a coverage count
- [[self-evolving-visual-questioner]] — another questioner trained by self-play where diversity is a monitored quantity
- [[avg-bleu]] — the lexical similarity measure this work shows to be insufficient
- [[sound-verifier-self-play]] — the verified proposer-solver loop whose refreshed proposer prompt is the context-side countermeasure above

[^c1]: arxiv-2603-13309 — "the Questioner concentrates on a narrow slice of the problem space as training progresses, reducing semantic coverage across iterations and"
[^c2]: arxiv-2603-13309 — "a solver cannot learn strategies it is never prompted to exercise."
[^c3]: arxiv-2603-13309 — "However, lexical signals fail to detect semantic equivalence, operate only locally within"
[^c4]: arxiv-2603-13309 — "Active clusters drop from 89 to"
[^c5]: arxiv-2603-13309 — "but an unsolvable question receives zero reward regardless of cluster rarity."
[^c6]: arxiv-2603-13309 — "With 107 of 128 clusters active, normalised entropy reaches 0.83 and"
[^c7]: arxiv-2603-13309 — "On AIME 2025, SPICE achieves the highest score (19.10)."
[^c8]: arxiv-2603-13309 — "The Solver-initialised Questioner alone does not improve over the baseline (−0.48)."
[^c9]: arxiv-2603-13309 — "The sweet spot at 𝜆=5.0 balances"
[^c10]: arxiv-2603-13309 — "The embedding and clustering step adds only ∼2.4 minutes (+1.7%) per iteration"
[^c11]: arxiv-2603-13309 — "The semantic partition is static."
[^c12]: arxiv-2512-18160 — "sampling only once from the seed dataset"
[^c13]: arxiv-2512-18160 — "causes an average drop of 10.6% across all metrics"
[^c14]: arxiv-2512-18160 — "rate on average (45.3% vs 29.3%), which leads to 2.48×"
