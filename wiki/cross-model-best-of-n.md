---
description: "Spending one best-of-n budget across several LLMs, committing the best-scoring head at each step, beat single-model best-of-n at large n once each model's rewards were normalized."
aliases: ["routed online best-of-n", "multi-LLM best-of-n", "sequential multi-model best-of-n", "cross-model BoN"]
sources: ["arxiv-2512-05542"]
---
# Cross-model best-of-n

Best-of-n (BoN) draws n candidate answers from one model and returns the one a reward model scores highest. The cross-model variant keeps the same budget of n draws but takes them from a suite of M models, and decides at each step which model to draw from. The paper that describes it starts from the same observation as the single-model case: "traditionally best-of-n relies on a single model to generate responses".[^c1]

The mechanism is greedy and sequential. Each model holds a head, its next candidate. At each step every head is scored against the set already selected, and the procedure "commits the best candidate, and recycles the unchosen heads to the next step".[^c2] A model's head is replaced by a new draw only when that model was chosen, so the number of draws stays fixed: "the procedure draws exactly n responses in total".[^c3] When the loop ends, the answer is picked by plain best-of-n over the selected set. The score that ranks the heads, which combines reward with the agreement of final answers, is described in [[agreement-weighted-reward-score]].

The method needs no training: "This online routing requires no additional training, keeps compute parity, and works with any plug-in reward model".[^c4] The authors frame it as a sequential method, where "whereas regular best-of-n is parallel in nature",[^c5] so the two differ in when samples are drawn as well as in which model draws them. The routing is also a different kind of routing from [[model-orchestration]], where a person decides when to switch models, and from trained routers: "parametric routers that must be trained".[^c21]

**Reward normalization is a precondition.** Rewards from different models do not share a scale, so the routing compares them only after a per-model mapping. The authors "normalize rewards by their empirical CDF", and "rank the rewards and map them uniformly onto values in [0, 1]".[^c6] The paper calls the step necessary, since otherwise "rewards would not be comparable across models".[^c7] The paper reports that without normalization the method "degrades to that of the average of the individual best-of-n strategies".[^c8] The mapping is estimated from "a large pre-computed corpus of responses and rewards across datasets".[^c9] So the gain depends on that calibration step, not only on the routing.

**What was measured.** Four instruction-tuned models of 6.7–8B parameters, math and code variants among them, and one reward model, on five reasoning sets (MATH500, OlympiadBench, MinervaMath, GSM8K, MMLU-STEM), with 1-sigma intervals. At n = 1 and n = 4 the routed method does not beat the baselines. The text says "it is en par for n = 16 and significantly better at n = 64 and n = 256", with "accuracy gains of up to 3.4% over baselines".[^c10][^c11] The single-model baselines show a pattern: "the accuracy of best-of-n often starts deteriorating as n increases beyond a certain point".[^c12] The authors attribute the decline on some datasets to reward hacking, and report that the routed method suffers from it less: "the effect is significantly diminished".[^c13]

Compute is said to be asymptotically exactly on par in FLOPs. "The memory requirements grow linearly with the number of models".[^c20] In the worst case runtime is up to a factor of n larger than single-model best-of-n, "compared to standard best-of-n with a single model", because generation is sequential.[^c14] The authors decline to give a runtime-matched comparison for the regime where the method wins.[^c15]

## Limits

- Five reasoning datasets, four models and one reward model, "Skywork/Skywork-Reward-V2-Llama-3.1-8B".[^c16] No search over the model suite was done, which is a point in the method's favour, but the suite is one suite.
- The agreement term needs answers that can be compared for identity: the method is "only applicable to tasks where it can be immediately verified whether two answers are identical".[^c17] The authors suggest embedding similarity for open-ended tasks and do not test it.[^c18]
- The gains are small and appear only from n = 16 up. For n = 1 and n = 4 the method is behind, so it is not a general replacement for best-of-n at small budgets.
- No guarantee is given: "guarantees for the expected accuracy require further assumptions on the reward model".[^c19]
- The text does not say whether the normalization corpus overlaps the evaluation sets. That matters, because the CDF is built before the test. This is my inference from what is missing, not a finding.
- The text attributes the gain to "diversity across models", but the sections read do not include a run that separates model diversity from the effect of the reward model or the score. Which model is chosen is reported in an appendix not read here.
- The sequential schedule costs wall-clock time that the parallel baseline does not pay, unless memory limits force serial sampling anyway.

## Related

- [[test-time-scaling]] — the family this belongs to; here the sampling is spread over models and run in sequence, and the selection uses a reward-plus-agreement score
- [[agreement-weighted-reward-score]] — the score that decides which model's head is committed at each step
- [[model-orchestration]] — the hand-routed version of switching models; this is the automated, training-free one under a fixed sample budget
- [[reward-overoptimization]] — the proxy-reward decline with larger n; the paper ascribes the single-model decline to reward hacking, citing Skalse et al.

[^c1]: arxiv-2512-05542 — "traditionally best-of-n relies on a single model to generate responses"
[^c2]: arxiv-2512-05542 — "commits the best candidate, and recycles the unchosen heads to the next step"
[^c3]: arxiv-2512-05542 — "the procedure draws exactly n responses in total"
[^c4]: arxiv-2512-05542 — "This online routing requires no additional training, keeps compute parity, and works with any plug-in reward model"
[^c5]: arxiv-2512-05542 — "whereas regular best-of-n is parallel in nature"
[^c6]: arxiv-2512-05542 — "we normalize rewards by their empirical CDF"
[^c7]: arxiv-2512-05542 — "rewards would not be comparable across models"
[^c8]: arxiv-2512-05542 — "degrades to that of the average of the individual best-of-n strategies"
[^c9]: arxiv-2512-05542 — "a large pre-computed corpus of responses and rewards across datasets"
[^c10]: arxiv-2512-05542 — "it is en par for n = 16 and significantly better"
[^c11]: arxiv-2512-05542 — "with accuracy gains of up to 3.4% over baselines"
[^c12]: arxiv-2512-05542 — "the accuracy of best-of-n often starts deteriorating as n increases beyond a certain point"
[^c13]: arxiv-2512-05542 — "the effect is significantly diminished"
[^c14]: arxiv-2512-05542 — "compared to standard best-of-n with a single model"
[^c15]: arxiv-2512-05542 — "we decided not to include an explicit runtime comparison to regular best-of-n"
[^c16]: arxiv-2512-05542 — "We use Skywork/Skywork-Reward-V2-Llama-3.1-8B as the reward model"
[^c17]: arxiv-2512-05542 — "only applicable to tasks where it can be immediately verified whether two answers are identical"
[^c18]: arxiv-2512-05542 — "one could potentially replace this string-based comparison with embedding similarities"
[^c19]: arxiv-2512-05542 — "guarantees for the expected accuracy require further assumptions on the reward model"
[^c20]: arxiv-2512-05542 — "The memory requirements grow linearly with the number of models"
[^c21]: arxiv-2512-05542 — "parametric routers that must be trained"
