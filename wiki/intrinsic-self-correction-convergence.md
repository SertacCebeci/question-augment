---
description: "Repeating a generic self-correction instruction with no external feedback lowers model uncertainty and calibration error until performance converges, on average within six rounds."
aliases: ["intrinsic self-correction", "converged self-correction", "multi-round intrinsic self-correction"]
sources: ["doi-10-48550-arxiv-2406-02378", "doi-10-3389-frai-2025-1660912"]
---
# Intrinsic self-correction convergence

Intrinsic self-correction is the case where the instruction gives only the goal and no detail about what is wrong. The paper's own statement of the case is that "LLMs must rely on their internal knowledge to improve response quality, a process referred to as intrinsic self-correction."[^c1] The example instruction is abstract, "Please do not be biased or rely on stereotypes", and the authors contrast it with feedback from humans or stronger models, which the intrinsic form does without.[^c2] The pipeline is multi-round. The first instruction is concatenated with the question, and later instructions are "appended with the dialogue history as the post-hoc instruction to correct the misbehavior."[^c3]

The paper's claim is that repeated instructions make the answer converge, and it gives a chain of steps for why. Model uncertainty falls first: "The uncertainty generally decreases along with more self-correction rounds across tasks."[^c4] Calibration error then follows it down and flattens. The abstract's summary is that "iteratively applying instructions reduces model uncertainty towards convergence," and the authors say the reduction "aids LLMs in achieving lower calibration error, thereby improving self-correction performance."[^c5] The stopped state is read as the convergence of the performance curve. On average, "convergence can be achieved ... within 6 rounds of self-correction."[^c6]

The speed differs by task type. For multi-choice QA, "convergence is typically achieved after the first round, while generation tasks generally require" more rounds.[^c7] The ECE for QA "converged at the first or" second round, and the calibration error for generation "show[s] convergence since round 6."[^c8]

The theory in Section 6.2 is a probability argument, not a fitted model. It writes the probability of the positive concept at round k as a product of per-round factors, so that "the effect of the positive concept activated by self-correction instructions degrades as the interaction" proceeds, and then holds that the positive concept stays dominant once its probability is near zero.[^c9] It rests on an independence assumption: "We have the independent assumption over question x, instruction i and output y".[^c10] The argument is the paper's own derivation; the text does not test it beyond the experiments above.

## Limits

- One LLM backbone for the text tasks. The paper says "The considered model in this paper is zephyr-7b-sft-full"[^c11], and GPT-4 is used only as the vision-language backbone. Other models are not in the text read.
- The round count is fixed, not chosen by a stopping rule. The authors "set the number of self-correction rounds as a constant rather than using the correct label to determine when to stop."[^c12] So convergence is read off curves after the fact; no stopping criterion is tested.
- Reasoning tasks are excluded. The paper states it omits them "due to the existing debate about the" effectiveness of self-correction for reasoning.[^c13]
- Prior work is in tension with the result. The paper cites [29] as showing that "intrinsic moral self-correction is superficial, as it does not significantly alter immorality in hidden states."[^c14] The paper answers this with the concept measure in [[latent-concept-activation]], which is a separate claim.
- The causal arrow is not established. The authors say "The causality between model uncertainty and calibration error is bidirectional."[^c15] The evidence is co-movement across rounds, not an intervention on uncertainty.
- The uncertainty and calibration measures change by task: semantic entropy for generation, logit confidence and ECE for QA. Whether convergence holds under other estimators is not tested.
- Convergence means the score stops changing. It does not by itself say the stopped answer is the right one, and the figures use toxicity and bias scores, not correctness (my inference).
- The external-feedback case is different. Blueprint2Code's Debugging Agent reruns generated code on the question's own example pairs and "exclusively uses the original example I/O", which the paper sets against synthetic tests.[^c16] Removing that stage gives "accuracy falling to 64.6%" on HumanEval with GPT-3.5-turbo, and the paper reports that "removing the Debugging Agent results in the most" accuracy loss of its three ablations.[^c17][^c18] The removal takes out the whole retry, not only the feedback, so the ablation cannot say whether the gain comes from the execution signal or from a second attempt. The convergence result above has no external signal, so it does not transfer to that case.

## Related

- [[latent-concept-activation]] — the activated concept the paper attributes the uncertainty drop to, and the probe used to measure it.
- [[calibration]] — the calibration error whose convergence the paper tracks across rounds.
- [[semantic-entropy]] — the uncertainty estimator the paper uses for generation tasks.
- [[specific-actionable-self-feedback]] — Self-Refine supplies a feedback text the model writes about its own draft; intrinsic self-correction supplies only a goal-level instruction, so the two differ in how much the prompt says about the error.
- [[final-output-gap]] — another self-correction setting where the score improves but does not reach zero, which is a reason not to read a plateau as a removed problem.
- [[placebo-controlled-retry-evaluation]] — separates the value of retrying from the value of feedback content, the split that the Blueprint2Code debugging ablation does not make.

[^c1]: doi-10-48550-arxiv-2406-02378 — "LLMs must rely on their internal knowledge to improve response quality, a process referred to as intrinsic self-correction"
[^c2]: doi-10-48550-arxiv-2406-02378 — "not require costly feedback from humans or more advanced LLMs"
[^c3]: doi-10-48550-arxiv-2406-02378 — "The following instructions are appended"
[^c4]: doi-10-48550-arxiv-2406-02378 — "The uncertainty generally decreases along with"
[^c5]: doi-10-48550-arxiv-2406-02378 — "aids LLMs in achieving lower calibration error, thereby improving self-correction performance"
[^c6]: doi-10-48550-arxiv-2406-02378 — "convergence can be achieved, on average, within 6 rounds of self-correction"
[^c7]: doi-10-48550-arxiv-2406-02378 — "convergence is typically achieved after the first round, while generation tasks generally require"
[^c8]: doi-10-48550-arxiv-2406-02378 — "show convergence since round 6, aligning with the trend of performance curves"
[^c9]: doi-10-48550-arxiv-2406-02378 — "the effect of the positive concept activated by self-correction instructions degrades as the interaction"
[^c10]: doi-10-48550-arxiv-2406-02378 — "We have the independent assumption over question x, instruction i and output y"
[^c11]: doi-10-48550-arxiv-2406-02378 — "The considered model in this paper is zephyr-7b-sft-full"
[^c12]: doi-10-48550-arxiv-2406-02378 — "we set the number of self-correction rounds as a constant rather than using the"
[^c13]: doi-10-48550-arxiv-2406-02378 — "we omit consideration of reasoning tasks due to the existing debate about the"
[^c14]: doi-10-48550-arxiv-2406-02378 — "intrinsic moral self-correction is superficial, as it does not significantly alter immorality in hidden states"
[^c15]: doi-10-48550-arxiv-2406-02378 — "The causality between model uncertainty and calibration error is bidirectional"
[^c16]: doi-10-3389-frai-2025-1660912 — "exclusively uses the original example I/O"
[^c17]: doi-10-3389-frai-2025-1660912 — "accuracy falling to 64.6%"
[^c18]: doi-10-3389-frai-2025-1660912 — "removing the Debugging Agent results in the most"
