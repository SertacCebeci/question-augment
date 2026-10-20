---
description: "Under causal attention a prompt token cannot see later tokens, so token order matters; repeating the prompt gives each token a view of all others and won 47 of 70 non-reasoning tests."
aliases: ["prompt repetition", "options-first versus question-first ordering", "token-order effect under causal attention"]
sources: ["arxiv-2512-14982"]
---
# Causal prompt-order dependence

A decoder-only model reads its input left to right, and the state at each position is built only from the positions before it. The paper starts from that constraint: "LLMs are often trained as causal language models, i.e. past tokens cannot attend to future tokens."[^c1] Its consequence for a prompt is that arrangement, not only content, fixes what each part of the input is conditioned on: "the order of the tokens in a user’s query can affect prediction performance."[^c2] In the paper's multiple-choice setting, the options-first layout makes the model process the options "without seeing the question in context",[^c3] so the same question and the same options can be encoded differently depending on which comes first. The same constraint, applied to where a retrieval query sits relative to its documents, is [[query-ahead-of-documents]].

The paper's intervention keeps the content and changes only what earlier tokens can see. The input goes from one copy of the query to two, and the stated effect is that "this enables each prompt token to attend to every other prompt token."[^c4] (My inference:) In the second copy every token is conditioned on the whole query, and the first copy's early tokens are followed by a copy of the later ones, so information that the causal mask forbids in one pass is available in the other. The repeated part is computed in the parallel prefill stage: "Prompt repetition is efficient, moving the repetition to the parallelizable prefill."[^c5]

## What was measured

Without reasoning, across seven models (Gemini 2.0 Flash and Flash Lite, GPT-4o-mini and GPT-4o, Claude 3 Haiku and 3.7 Sonnet, DeepSeek V3) and seven benchmark configurations, the paper reports that "Prompt repetition wins 47 out of 70 tests, with 0 losses."[^c6] A win was counted "according to the McNemar test [McNemar, 1947] with pvalue < 0.1 as wins."[^c7] The gain depends on layout: the paper expects "the multiple-choice benchmarks with question-first, and larger improvements with options-first."[^c8] On a custom task built to need order, "the model gets a list of N names and is asked to output the ith name on the list",[^c9] prompt repetition raised Gemini 2.0 Flash-Lite "from 21.33% to 97.33%".[^c10]

The output side was also measured: "prompt repetition improves the performance of LLMs (Figure 1) without increasing the lengths"[^c11] of the generated outputs, and the measured latencies did not rise in the reported runs. A padding control, which lengthens the input with periods to the same token count, "does not improve performance";[^c12] the padding method "pads the inputs with periods",[^c13] so the gain is not explained by input length alone.

With reasoning enabled, the picture changes: "When reasoning is enabled, prompt repetition is neutral to slightly positive."[^c14] The paper's explanation is that "reasoning models trained with RL often learn to repeat (parts"[^c15] of the request themselves, so the second copy adds little; the authors call the neutral result "expected given that the reasoning often starts with repeating".[^c16]

## Limits

- The attention account is the paper's explanation and was not measured. The authors list "(9) Further analyze the attention patterns due" to repetition as future work.[^c17] What is shown is the accuracy and length outcome; which attention paths carry the gain is not shown.
- The models were reached through provider APIs: "We ran all tests using each provider’s official API in Feb and Mar 2025."[^c18] The result is one snapshot of closed models at one date, with no open-weight model in the sample.
- The win criterion is a per-test McNemar test at p < 0.1. (My inference:) with 70 comparisons and no correction stated in the text, some of the 47 wins would be expected by chance at that threshold; the zero losses is the stronger part of the claim.
- Repeating only the question was tried earlier: Shaier (2024) "experimented with repeating just the question part of the prompt and found that it yields"[^c19] no gain, as the paper's related-work section reports. Repeating only parts of a prompt is listed as untested: "(5) Repeat only parts of the prompt (especially for"[^c20]. So whether the gain needs the whole input, or only the part a later token depends on, is open.
- The reasoning-on evidence is thin: a smaller set of benchmarks with "5 wins, 1 loss, 22 ties".[^c21]
- Long inputs are a separate limit. The Anthropic models' latency rose on the longest requests, "where the latencies increase (likely due to the prefill stage taking longer)";[^c22] the paper adds that "Prompt repetition can affect latency for long prompts, and might be impossible for very long ones."[^c23]

## Related

- [[query-ahead-of-documents]] — the same causal constraint applied to a retrieval query placed after its documents; there the lever is placement, here it is a second copy.
- [[permutation-consistency-training]] — option-order sensitivity in discrete choice handled by training over all orderings rather than by repeating the prompt.
- [[llm-judge-biases]] — position effects in judging, whose causal-attention origin the wiki records as suspected and not studied.

[^c1]: arxiv-2512-14982 — "LLMs are often trained as causal language models, i.e. past tokens cannot attend to future tokens."
[^c2]: arxiv-2512-14982 — "the order of the tokens in a user’s query can affect prediction performance"
[^c3]: arxiv-2512-14982 — "the latter making the model process the options without seeing the"
[^c4]: arxiv-2512-14982 — "This enables each prompt token to attend to every other prompt token"
[^c5]: arxiv-2512-14982 — "Prompt repetition is efficient, moving the repetition to the parallelizable prefill"
[^c6]: arxiv-2512-14982 — "Prompt repetition wins 47 out of 70 tests, with 0 losses"
[^c7]: arxiv-2512-14982 — "according to the McNemar test [McNemar, 1947] with pvalue < 0.1 as wins."
[^c8]: arxiv-2512-14982 — "the multiple-choice benchmarks with question-first, and larger improvements with options-first."
[^c9]: arxiv-2512-14982 — "the model gets a list of N names and is asked to output the ith name on the list"
[^c10]: arxiv-2512-14982 — "NameIndex from 21.33% to 97.33%"
[^c11]: arxiv-2512-14982 — "prompt repetition improves the performance of LLMs (Figure 1) without increasing the lengths"
[^c12]: arxiv-2512-14982 — "and, as expected, does not improve performance."
[^c13]: arxiv-2512-14982 — "which pads the inputs with periods"
[^c14]: arxiv-2512-14982 — "When reasoning is enabled, prompt repetition is neutral to slightly positive (Figure 4)."
[^c15]: arxiv-2512-14982 — "reasoning models trained with RL often learn to repeat (parts"
[^c16]: arxiv-2512-14982 — "which is expected given that the reasoning often starts with repeating"
[^c17]: arxiv-2512-14982 — "(9) Further analyze the attention patterns due"
[^c18]: arxiv-2512-14982 — "We ran all tests using each provider’s official API in Feb and Mar 2025."
[^c19]: arxiv-2512-14982 — "found that it yields"
[^c20]: arxiv-2512-14982 — "(5) Repeat only parts of the prompt (especially for"
[^c21]: arxiv-2512-14982 — "5 wins, 1 loss, 22 ties"
[^c22]: arxiv-2512-14982 — "where the latencies increase (likely due to the prefill stage taking longer)"
[^c23]: arxiv-2512-14982 — "Prompt repetition can affect latency for long prompts, and might be impossible for very long ones."
