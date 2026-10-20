---
description: "The intention state is the hidden state at the last prompt position, read before the first token is chosen; prompt wording alone can reshape it, with no thinking tokens."
aliases: ["intention state", "intention collapse", "pre-collapse state"]
sources: ["arxiv-2601-01011"]
---
# Pre-collapse intention state

Vera fixes one object for a transformer language model: the intention state I, the collection of hidden representations at the first decoding step, "immediately before the first output token is selected". Concretely it is one hidden vector per selected layer, read at the final prompt position.[^c1] The collapse is the step that turns this state into a discrete choice for the first token, by greedy selection or by sampling.[^c2] The paper names the whole gap intention collapse, and describes the map from state to text as "many-to-one and inherently lossy".[^c3]

The point of fixing the moment is that it is the same in every condition. The state is taken after the full prompt, whatever the instruction says, and "The same extraction point is used for all experimental regimes".[^c4] Differences in I can then be read as effects of prompt conditioning, not of tokens emitted during generation. This is the claim that matters for chain-of-thought: a step-by-step instruction is said to act on I without any hidden thinking tokens, since it "can reshape I purely through prompt conditioning, which" changes the state before the first token is selected.[^c5] Tokens emitted after the first token are post-collapse and are analysed separately.

The definition rests on ordinary layer-wise computation. Even a model that emits its first token at once, "a model emits its first token immediately, it still performs a nontrivial internal" computation over the prompt, and the paper counts that forward pass as the pre-collapse processing.[^c6] So a prompt that asks for a longer or differently structured answer is, on this view, already a change to the state before any output exists.

What was measured. In a 3 × 3 study (Mistral-7B-Instruct, Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct; GSM8K, ARC-Challenge, AQUA-RAT; baseline, chain-of-thought and a babble control; n = 200 items per cell), "CoT increases average accuracy from 34.2% to 47.3%", with the gain concentrated on free-response math. On ARC-Challenge, "CoT consistently degrades performance on ARC-Challenge for" all three models.[^c7][^c8] Three readouts are taken from I: the entropy of the first-token distribution (see [[first-token-entropy]]), a linear probe's AUROC for eventual correctness, and a participation-ratio dimensionality. The paper's most consistent finding concerns the first of these, where the CoT shift runs in opposite directions for different model families. The probe result is the one that separates the state from the answer: probe AUROC is above chance in some cells and can be high where CoT accuracy is low, "high AUROC can co-occur with degraded CoT accuracy in multiple-choice regimes".[^c9] The dimensionality is defined in the paper per layer as "is the participation ratio of the PCA eigenvalue spectrum", aggregated over layers with variance weights.[^c15] In the sections I read, its values are not reported, so nothing in this note rests on it.

## Limits

- The state is taken at one position under one decoding policy. The paper holds decoding fixed "holding decoding parameters constant (greedy decoding, temperature T = 0)" to isolate prompting, so nothing here says the state behaves the same under sampling at the moment of collapse.[^c10]
- The study covers three 7–8B instruct checkpoints, text only, and the author notes that "quantization can alter activation statistics", so absolute values may move across setups.[^c11] "but it does not address scaling", to larger models, base checkpoints or other architectures.[^c12]
- The paper presents the framework as a lens, "not as a complete theory of LLM reasoning".[^c13] It disclaims any claim that models have intentions "in the conscious or phenomenological sense".
- The state-dependent decoding and early-exit proposals are untested: the author describes "extensions that remain as forward-looking protocols for scaling the agenda".[^c14]
- My inference: a state that is linearly separable for correctness does not show that the collapse policy will use it. The paper reports the same gap and does not close it.

## Related

- [[first-token-entropy]] — the entropy readout taken at this position
- [[pre-generation-success-probe]] — a linear probe on the same pre-generation state, scored against success
- [[format-induced-answer-collapse]] — a different collapse: which answer a format request yields, measured on answer surprisal rather than on any hidden state

[^c1]: arxiv-2601-01011 — "collection of hidden representations at the first decoding step, immediately before the first output token is selected"
[^c2]: arxiv-2601-01011 — "Collapse begins when the model converts this state into a discrete choice for"
[^c3]: arxiv-2601-01011 — "The mapping is many-to-one and inherently lossy"
[^c4]: arxiv-2601-01011 — "The same extraction point is used for all experimental regimes"
[^c5]: arxiv-2601-01011 — "they can reshape I purely through prompt conditioning, which"
[^c6]: arxiv-2601-01011 — "a model emits its first token immediately, it still performs a nontrivial internal"
[^c7]: arxiv-2601-01011 — "CoT increases average accuracy from 34.2% to 47.3%"
[^c8]: arxiv-2601-01011 — "CoT consistently degrades performance on ARC-Challenge for"
[^c9]: arxiv-2601-01011 — "high AUROC can co-occur with degraded CoT accuracy in multiple-choice regimes"
[^c10]: arxiv-2601-01011 — "holding decoding parameters constant (greedy decoding, temperature T = 0)"
[^c11]: arxiv-2601-01011 — "quantization can alter activation statistics"
[^c12]: arxiv-2601-01011 — "but it does not address scaling"
[^c13]: arxiv-2601-01011 — "not as a complete theory of LLM reasoning"
[^c14]: arxiv-2601-01011 — "extensions that remain as forward-looking protocols for scaling the agenda"
[^c15]: arxiv-2601-01011 — "is the participation ratio of the PCA eigenvalue spectrum"
