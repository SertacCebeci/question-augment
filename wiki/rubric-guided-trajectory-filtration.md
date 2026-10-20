---
description: "A rubric judge picks among candidate steps during rollout, and the terminal reward then gates which trajectories enter fine-tuning data; the intermediate choice is no longer left to the final outcome."
aliases: ["rubric-based GRM filtering", "GRM-guided trajectory sampling", "rubric-guided rejection sampling", "turn-level and segment-level GRM filtration"]
sources: ["doi-10-48550-arxiv-2604-16335"]
---
# Rubric-guided trajectory filtration

Rejection sampling for agent fine-tuning keeps a rollout only if its terminal outcome passes. This method moves a second filter inside the rollout. At each step the agent samples several candidate actions, a generative reward model (GRM) scores them against human-written rubrics and keeps one, and the rest are discarded. The rollout then continues from the kept action. Only at the end does the verifiable reward decide membership in the training set: "we add the trajectory to the RFT dataset if and only if the terminal verifiable reward is 1; otherwise, we reject it."[^c1]

The stated reason is that a terminal binary reward cannot see some behaviour. One case is a bad step that is later corrected, so the final result does not reflect it; the paper describes agents that "may repeatedly invoke the same tool, or trigger recoverable execution errors."[^c2] The other is a good step inside a run that fails for a small final reason; such trajectories get the same zero reward as completely unstructured attempts.[^c3] The rubric judge scores the intermediate choice itself, so a desirable pattern can be promoted even when the run ends in failure.

Two variants set how often the judge is called. In the turn-level variant the agent "independently samples N candidate actions at each step, where each action corresponds to a single tool call."[^c4] The GRM chooses among them without the execution results: "turn-level GRM selection does not condition on execution results."[^c5] In the segment-level variant the judge is called less often, since "we query the GRM in less frequency by evaluating and filtering multi-step" continuations.[^c6] The paper states the trade: the segment-level judge "inherently trades off filtering frequency for evaluation accuracy."[^c7] Segment-level filtration is expected to help when the judge is weak and single-step differences are subtle (the paper's reasoning, not a measurement).[^c8]

The rubrics are four criteria (workflow alignment, information gain, strategic view, error control), and "We define four rubrics, each assigned weight 0.25 in the overall GRM score."[^c9] The GRM also receives "The ground-truth git patch to fix the issue."[^c10] So the judge scores candidates against a known fix, not against general quality.

In the paper's one experiment, a seed-OSS-36B agent on OpenHands is fine-tuned on an RFT set kept at "the RFT dataset size to 500 for consistency."[^c16] "Collecting RFT dataset with our rubric-based GRM approach leads to higher test accuracy."[^c11] The table reports 36.6% on SWE-bench Verified for the terminal-reward baseline, 39.3% and 42.6% for turn-level GRM with N=3 and N=5, and 40.2% and 40.5% for two segment-level settings. The filter also shifted behaviour toward efficiency: "The intervention of rubric-based GRM notably improves efficiency on the test set."[^c12]

## The judge need not be stronger than the generator

The GRM itself scored 43% on the test set, "which is higher than the 28% by the base model reported in Sec. 5.2."[^c13][^c27] To test a case where the generator is stronger, the authors added 500 trajectories from Claude Opus 4 to the SFT data,[^c26] which lifted the base to 48%, "surpassing that of the GRM."[^c14] Filtering still helped: 50.6% for turn-level GRM with N=3, against 46.8% for the terminal-reward baseline.[^c28] The authors conclude "the GRM need not be an expert generator," and read this through the generation-verification gap.[^c15] That reading is the paper's; the wiki's contribution here is only to record the comparison.

## Limits

- One backbone (seed-OSS-36B), one scaffold (OpenHands), and one training pool of 1.2k tasks.[^c24] The test set is SWE-bench Verified alone.[^c25] The authors say "we believe our approach holds promise beyond" software engineering,[^c17] but the text tests only that domain.
- Each setting appears as a single number in the text read. No seeds, variances or significance tests are reported. The stronger-base baseline fell, which the authors attribute to "a normal fluctuation when the performance is close to its" ceiling.[^c18] Gaps of two to four points are therefore not separated from run-to-run noise here (my inference).
- The behavioural measures are counts of test and reproduction behaviour, identified "via keyword-based regex matching."[^c19] They show that such patterns occur more often under the filter, not that they cause the accuracy gain.
- The judge depends on the ground-truth patch. The weaker-judge result also rests on it: a weaker model that evaluates "rubric-aligned behavior (especially with access to ground-truth side information) can still guide the learning."[^c20] Without the patch, nothing here shows the filter works.
- The rubrics are hand-written, and the authors single this out as open: "the design of effective rubrics remains a challenging and largely" manual process.[^c21] No method for building or choosing rubrics is tested.
- The judge is a proprietary thinking model, "seed-1.6-thinking."[^c22] No open judge was tried.
- Turn-level selection ignores execution results, by design, for cost. Whether that costs quality is not measured.
- The filter only shapes data for supervised fine-tuning. The authors list "extend our approach to" the reinforcement learning stage as future work, so its effect on RL is untested.[^c23]

## Related

- [[generate-then-verify-candidate-pipeline]] — a generator and a verifier split a candidate list into recall and precision; here the judge sits inside the generation loop, not after it.
- [[process-outcome-consistency-verification]] — another way to look past the outcome, by checking the derivation against the answer rather than the answer alone.
- [[information-utility-retrieval-control]] — a dense per-step score for search agents against outcome-only training; the same motivation, with a learned utility in place of a rubric judge.
- [[process-reward-model-hackability]] — step-level reward models can be driven up without correct logic; here the GRM only chooses among sampled candidates and is not optimised against.
- [[reward-overoptimization]] — the general pattern of a proxy reward pushed past its validity, which the terminal gate partly guards against.
- [[pretraining-grounded-rubric-self-play]] — uses the same generation-verification gap to explain why a grader can be weaker than the generator.
- [[pessimistic-min-judge-aggregation]] — combining several rubric judges into one reward; a different use of rubrics from selecting steps.

[^c1]: doi-10-48550-arxiv-2604-16335 — "we add the trajectory to the RFT dataset if and only if the terminal verifiable reward is 1; otherwise, we"
[^c2]: doi-10-48550-arxiv-2604-16335 — "agents may repeatedly invoke the same tool, or trigger recoverable execution errors"
[^c3]: doi-10-48550-arxiv-2604-16335 — "patterns but fail due to a minor final mistake receive the same zero reward as completely unstructured"
[^c4]: doi-10-48550-arxiv-2604-16335 — "independently samples N candidate actions at each step, where each action corresponds to a single tool call."
[^c5]: doi-10-48550-arxiv-2604-16335 — "turn-level GRM selection does not condition on execution results."
[^c6]: doi-10-48550-arxiv-2604-16335 — "we query the GRM in less frequency by evaluating and filtering multi-step"
[^c7]: doi-10-48550-arxiv-2604-16335 — "GRM inherently trades off filtering frequency for evaluation accuracy."
[^c8]: doi-10-48550-arxiv-2604-16335 — "In such cases, segment-level filtration can be more effective."
[^c9]: doi-10-48550-arxiv-2604-16335 — "We define four rubrics, each assigned weight 0.25 in the overall GRM score."
[^c10]: doi-10-48550-arxiv-2604-16335 — "The ground-truth git patch to fix the issue."
[^c11]: doi-10-48550-arxiv-2604-16335 — "Collecting RFT dataset with our rubric-based GRM approach leads to"
[^c12]: doi-10-48550-arxiv-2604-16335 — "The intervention of rubric-based GRM notably improves efficiency on the test set."
[^c13]: doi-10-48550-arxiv-2604-16335 — "our GRM achieves 43% test accuracy"
[^c14]: doi-10-48550-arxiv-2604-16335 — "surpassing that of the GRM."
[^c15]: doi-10-48550-arxiv-2604-16335 — "Overall, these findings suggest that the GRM need not be an expert generator,"
[^c16]: doi-10-48550-arxiv-2604-16335 — "the RFT dataset size to 500 for consistency."
[^c17]: doi-10-48550-arxiv-2604-16335 — "we believe our approach holds promise beyond"
[^c18]: doi-10-48550-arxiv-2604-16335 — "method results in a performance drop, which we interpret as a normal fluctuation when the performance is close to its"
[^c19]: doi-10-48550-arxiv-2604-16335 — "via keyword-based regex matching."
[^c20]: doi-10-48550-arxiv-2604-16335 — "rubric-aligned behavior (especially with access to ground-truth side information) can still guide the learning"
[^c21]: doi-10-48550-arxiv-2604-16335 — "the design of effective rubrics remains a challenging and largely"
[^c22]: doi-10-48550-arxiv-2604-16335 — "We employ seed-1.6-thinking as the GRM"
[^c23]: doi-10-48550-arxiv-2604-16335 — "it would be valuable to extend our approach to"
[^c24]: doi-10-48550-arxiv-2604-16335 — "1.2k tasks sampled from SWE-Gym [19] (200 tasks)"
[^c25]: doi-10-48550-arxiv-2604-16335 — "we adopt SWE-bench Verified, a curated subset of 500 human-validated samples"
[^c26]: doi-10-48550-arxiv-2604-16335 — "augment the SFT dataset with 500 additional resolution trajectories generated by"
[^c27]: doi-10-48550-arxiv-2604-16335 — "which is higher than the 28% by the base model reported in Sec. 5.2."
[^c28]: doi-10-48550-arxiv-2604-16335 — "Our approach still yields a better performance."
