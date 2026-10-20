---
description: "On general QA, RL raises reward almost entirely through the answer tokens while the thinking trace barely improves; a cross-generation swap of thinking and answering models exposes it."
aliases: ["thinking-answering decoupling", "cross-generation evaluation", "thinking stagnation"]
sources: ["arxiv-2603-20799"]
---
# Thinking stagnation

When reinforcement learning is run on general question answering (GQA), the reward rises but the intermediate thinking trace does not get better in any way that helps another model. Li, Pang and Yu measure this with a cross-generation swap and name the result thinking stagnation.

## The measurement

Cross-generation evaluation splits a response into a thinking trace T and a final answer A. Model X writes the thinking, and model Y receives it as a fixed pre-filled prefix and writes the answer.[^c1] Pairing a trace from an RL-trained model with the untrained answerer (Tpost + Apre) gives the value of the evolved thinking alone. Pairing an untrained trace with the trained answerer (Tpre + Apost) gives the value of the evolved answering alone.

On verifiable tasks the thinking is the bottleneck. On MATH, a 1.7B answerer rises from 67.00% to 82.50% when given an 8B-level trace, and a bigger answerer then adds almost nothing (82.50% to 83.50%).[^c2] On AlpacaEval 2.0 the pattern reverses. A stronger trace helps (45.98% to 56.59% for a 1.7B answerer), but swapping in the 8B answerer with the same 8B trace reaches 67.73%, a larger gain.[^c3]

After RL on GQA the same split appears. For Qwen3-1.7B with GRPO on ExpertQA, Tpost + Apre moves reward from 0.1842 to only 0.1849, while Tpre + Apost reaches 0.2148 against 0.2182 for the full post-trained model.[^c4] The authors read this as RL optimising "the model's ability to generate high-reward answers from existing thinking traces, rather than evolving the thinking process itself".[^c5] Models with other architectures show more thinking gain (+6.88% and +11.38% relative reward) but still far less than the answering gain (+19.29% in the Hunyuan case).[^c6] On MATH, by contrast, Tpost + Apre recovers +7.60 of the +9.20 accuracy gain, so RLVR does evolve thinking there.[^c7]

## Proposed cause

The authors hypothesise a weak coupling: a correct math solution needs an error-free chain, but GQA rewards "often admit shortcuts to high rewards", so the model can raise the reward by changing the answer tokens only.[^c8] This is a hypothesis, supported indirectly by the fix in [[separated-thinking-response-training]], which removes the shortcut and moves the Tpost + Apre numbers.

## Limits

- All trainings are small (Qwen3 1.7B and 4B, Hunyuan-1.8B, R1-Distill-1.5B); larger models were not tested here.
- The rewards come from learned reward models on ExpertQA and UltraFeedback, and quality is judged by AlpacaEval-style win rate, so "thinking quality" means usefulness of a trace to a fixed answerer, not correctness of reasoning.
- The shortcut explanation is not isolated from other causes, such as thinking traces being intrinsically less informative in open-ended tasks.
- The title's claim that RLVR does not improve GQA thinking is shown by comparing domains, not by training RLVR models and testing them on GQA in every setting.

## Related

- [[rlvr-answering-bias]] — another case where outcome reward moves the answer behaviour and not what one hoped for.
- [[reasoning-shortcut]] — shortcuts in reasoning that satisfy the reward without the intended process.
- [[separated-thinking-response-training]] — the remedy built on this finding.
- [[search-effort-accuracy-decoupling]] — a different decoupling of process effort from outcome quality.

[^c1]: arxiv-2603-20799 — "We first allow model X to generate the thinking trace, then this trace is provided as a fixed prefix (pre-filled context) to model Y , which is tasked to generate the final answer."
[^c2]: arxiv-2603-20799 — "Upgrading the thinking trace from a 1.7B-level to an 8B-level for a 1.7B answering model results in a massive performance surge, from 67.00% to 82.50%."
[^c3]: arxiv-2603-20799 — "the same 8B thinking trace paired with an 8B answering model jumps to 67.73%, a much larger leap than the gain provided by the thinking trace alone."
[^c4]: arxiv-2603-20799 — "the Reward only marginally increases from 0.1842 to 0.1849 (+0.0007)."
[^c5]: arxiv-2603-20799 — "This empirical evidence suggests a clear Thinking Stagnation where the RL process primarily optimizes the model’s ability to generate high-reward answers from existing thinking traces, rather than evolving the thinking process itself to provide better logical foundations."
[^c6]: arxiv-2603-20799 — "In Setting A, for instance, the Tpost + Apre configuration achieves a +19.29% reward increase, almost triple what the evolved thinking alone contributes."
[^c7]: arxiv-2603-20799 — "the thinking process acts as the decisive engine for performance: the Tpost + Apre configuration accounts for the vast majority of the total gain."
[^c8]: arxiv-2603-20799 — "GQA tasks often admit shortcuts to high rewards"
