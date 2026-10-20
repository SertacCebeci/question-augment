---
description: "A single agent-evaluation score is one draw from a variable execution process, so the run-to-run spread must be measured before a difference between two systems is credited."
aliases: ["run-to-run variance", "seed variance", "single-run comparison", "one run is one draw", "repeat-run spread"]
sources: ["doi-10-48550-arxiv-2608-13867", "arxiv-2511-19730"]
---
# Run-to-run spread

An agent evaluation usually arrives as a table with one row per system and one score per row, and the score hides the process that produced it. Each cell has layers behind it: the public benchmark, the harness that "checks out the repository, supplies the task, invokes the agent, applies its change, runs the tests," and the comparison assembled from many such executions.[^c1] A score can aggregate hundreds of tasks and still be a single run, if each task was attempted once under one set of conditions.[^c2]

The hidden variation is measurable. Across 60,000 SWE-bench-Verified trajectories, single-run pass@1 "varied by 2.2 to 6.0 percentage points."[^c3] At decoding temperature 0 the spread still exceeded 1.5 points: "the standard deviation still exceeded 1.5 percentage points because of infrastructure nondeterminism."[^c4] The trajectories diverged within the first few percent of generated tokens, and each difference changed the context for the next token, so the divergence cascaded through the run.[^c4] Temperature 0 therefore does not make a code-generation evaluation deterministic.

The monograph's own case is small. One configuration led another by +0.054 on a task family, with one task contributing +0.300. Rerunning each configuration three times, the difference fell to +0.0035, and the paired t statistic of 2.41 "fell below the critical value of 2.776" with 4 degrees of freedom.[^c5] The apparent advantage came from one unusually low baseline: "score created the apparent advantage, and it disappeared under repetition."[^c6] The three-decimal display "described the representation of the score, not the stability of the process that produced it."[^c6]

The same mechanism appears in the older literature the text cites. Reimers and Gurevych "compared one score from each of two identical systems and found apparent significant differences in" up to 26% of comparisons at p < 0.05.[^c7] A significant test on two single runs describes those two runs; it cannot show that the methods differ, because the experiment has not sampled the method-level spread.

The same measurement appears for a model that proposes experiments rather than answers questions. In a materials-science study of LLM-guided active learning, responses "can vary even when using identical input prompts and a temperature of 0".[^c14] Repeated runs at one seed were set against runs across five seeds, and the repeated-run variance "is of magnitude similar to the variance across different seeds", which the authors read as variability "intrinsic to the LLM itself rather than" to the initial pool.[^c15][^c17] Each setting was run as "five random seeds and five repeated runs", ten runs in all, and the sections read report no significance test on the gap to the baselines.[^c16] The paper's claim that this spread lies "within the variability range typically observed for traditional ML approaches" can be checked only against the run-level spread it measured.[^c18] My inference: this is the design the note asks for, applied to a different kind of system.

The operational rule is narrow: "Measure the local run-to-run spread, and do not credit a difference" that stays inside it.[^c8] Reporting only the best run "identifies the luckiest draw, not how the configuration performs across draws."[^c9] Repetition costs: three runs need roughly three times the model calls and execution capacity of one.

## Limits

- The 2.2 to 6.0 point envelope belongs to SWE-bench-Verified-class tasks, models and execution conditions; the text says it "is not a universal constant."[^c10]
- The CodeProbe case covers five fixed tasks scored by a deterministic test-suite oracle, and the text limits it: "The conclusion covers these five fixed tasks and no wider population."[^c11] The tight repeat scores certify scorer stability, not agent determinism.
- Prompt wording is a separate nuisance source. The text notes that the prompt studies "do not establish an equivalent variance rate for long-horizon agents."[^c12]
- Repetition alone does not say how many runs suffice: "Repetition alone does not establish that a detected difference" is large enough to matter.[^c13] That needs a decision threshold and a power calculation (see [[minimum-detectable-effect]]).
- My inference: a score whose spread is unknown can still rank systems correctly when the gap is large; the note's claim is only that a small gap cannot be credited without the spread.

## Related

- [[minimum-detectable-effect]] — the resolution that a given number of repeats can reach
- [[multi-seed-bias-score-averaging]] — the same seed spread in a bias benchmark, handled by averaging 50 seeds
- [[answer-stability-abstention]] — run-to-run answer instability treated as signal rather than noise
- [[agentabstain-paired-benchmark]] — its reported numbers carry run-to-run variance that was not measured

[^c1]: doi-10-48550-arxiv-2608-13867 — "checks out the repository, supplies the task, invokes the agent, applies its change, runs the tests"
[^c2]: doi-10-48550-arxiv-2608-13867 — "still be a single run, if each task was attempted once under one instantiation of the surrounding"
[^c3]: doi-10-48550-arxiv-2608-13867 — "Across 60,000 SWE-bench-Verified trajectories, single-run pass@1 varied by 2.2 to 6.0 percentage points."
[^c4]: doi-10-48550-arxiv-2608-13867 — "the standard deviation still exceeded 1.5 percentage points because of infrastructure nondeterminism."
[^c5]: doi-10-48550-arxiv-2608-13867 — "The paired t statistic of 2.41 fell below the critical value of 2.776."
[^c6]: doi-10-48550-arxiv-2608-13867 — "score created the apparent advantage, and it disappeared under repetition."
[^c7]: doi-10-48550-arxiv-2608-13867 — "compared one score from each of two identical systems and found apparent significant differences in"
[^c8]: doi-10-48550-arxiv-2608-13867 — "Measure the local run-to-run spread, and do not credit a difference"
[^c9]: doi-10-48550-arxiv-2608-13867 — "identifies the luckiest draw, not how the configuration performs across draws."
[^c10]: doi-10-48550-arxiv-2608-13867 — "it is not a universal constant"
[^c11]: doi-10-48550-arxiv-2608-13867 — "The conclusion covers these five fixed tasks and no wider population."
[^c12]: doi-10-48550-arxiv-2608-13867 — "Those results do not establish an equivalent variance rate for long-horizon agents."
[^c13]: doi-10-48550-arxiv-2608-13867 — "Repetition alone does not establish that a detected difference"
[^c14]: arxiv-2511-19730 — "responses can vary even when using identical input prompts and a temperature of 0"
[^c15]: arxiv-2511-19730 — "is of magnitude similar to the variance across different seeds"
[^c16]: arxiv-2511-19730 — "five random seeds and five repeated runs were performed"
[^c17]: arxiv-2511-19730 — "intrinsic to the LLM itself rather than"
[^c18]: arxiv-2511-19730 — "within the variability range typically observed for traditional ML approaches"
