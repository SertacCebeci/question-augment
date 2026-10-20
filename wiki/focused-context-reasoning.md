---
description: "Extracting a question's essential facts into a structured block, then reasoning only over that block, cuts a reasoning model's output tokens 2–3x on arithmetic word problems at similar accuracy."
aliases: ["Focused Chain-of-Thought", "F-CoT", "two-step context extraction", "extract-then-reason"]
sources: ["arxiv-2511-22176"]
---
# Focused context reasoning

Separating the extraction of facts from the reasoning over them changes how much a reasoning model writes. The mechanism proposed in the work is two stages. First the model turns the question into a short block of the facts that bear on it. Then the reasoning step receives only that block, without the original question: "structured representation and performs standard chain-of-thought reasoning."[^c1] The block has a fixed shape, enumerated information items and one question field: "This structure contains two components: (1) enumerated information blocks".[^c2]

The reason offered is about entanglement. In ordinary prose the relevant and irrelevant material are mixed, and the authors hypothesise that this "blurs the boundaries between relevant and irrelevant" information, which adds unnecessary tokens.[^c3] The analogy is to a cognitive account in which "the representation and structuring of information" comes before higher-order reasoning.[^c4] That is an analogy the paper draws; it does not test the cognitive framework itself.

## What was measured

On Qwen3 reasoning models from 0.6B to 32B, over SVAMP, GSM-Hard and MATH-500, the reasoning over a pre-computed context used about a third of the zero-shot chain-of-thought tokens on the easy set: "one-third of 0-shot CoT across all model sizes."[^c5] On the harder sets the cut was smaller, "questions, token counts decrease by about half."[^c6] Accuracy was measured as Pass@5, and it stayed level: reasoning over the context gave "results comparable to 0-CoT across all three datasets, except for the smallest Qwen3 0.6B model,".[^c7]

The savings are located in the trace. A sentence-level labelling of Qwen3-14B traces on MATH-500 found the share of tokens per category unchanged, but F-CoT "halves the number of reasoning sentences and substantially reduces the number of filler sentences,"[^c8] and the authors conclude that the reduction "primarily results from fewer reasoning and filler sentences".[^c9] The overthinking score fell from 2.35 to 1.74 on the same setting.[^c10] So the change is in how many inferential and filler sentences are written, not in what kind of text fills the trace.

The context need not come from the answerer. In the main runs a larger model (GPT-5 mini) writes the block and a smaller model reasons over it. Self-generated blocks worked for the 14B model and up, but the 0.6B model produced a valid block in "fewer than 2% of generations".[^c11] The authors suggest the division of labour: the block "typically requires only a few tokens, using a larger, slower, and more expensive LLM, and then" a smaller model does the expensive step.[^c12]

Format mattered less than presence. A plain enumerated list gave "comparable performance, suggesting that the key benefit arises from structure".[^c13] Numbering the items lowered the count further: "information pieces, further decreases the token count."[^c19] Unstructured concatenation also cut tokens, though less than the structured variants. The reading is that the gain comes from separating and compressing the facts, not from one syntax.

## Limits

- The domain is arithmetic word problems. The AIME sets, whose questions are already condensed, showed fewer tokens with slightly lower correctness, and "Given the small dataset size (30 samples) and potential test-set" contamination the authors do not claim harm.[^c14]
- Extraction can lose information. The authors "observed rare cases in which instructions such as" a percentage format were dropped, and the answer came out as a decimal.[^c15]
- The baseline is not the best possible baseline: "0-CoT performance could likely match structured context" if the model is told to take numbers as given, which the authors did not test.[^c16]
- In an ablation on Qwen3-14B and MATH-500, removing the instructions on how to use the context pushed its token count up "to about 3.1k (+747 tokens" relative to the default F-CoT prompt,[^c20] yet a "gap of more than 1k tokens between the inference with and without the context, even" under the same prompt remained.[^c17] One model and one dataset carry that ablation.
- The labels and the overthinking score come from GPT-5 Mini. The text as read reports no human check of them.[^c10]
- The models were not trained on structured inputs: "Currently, the evaluated models were not trained with such" inputs, which may limit how well they use the format.[^c18]
- Efficiency is measured in generated tokens, not in wall-clock time, and the accuracy numbers are Pass@5 over sampled outputs.

For the asker's side (my inference, not tested here): the same facts laid out as an enumerated block and as connected prose may cost the answerer different amounts of reasoning. Whether human-written questions carry that difference is not established by this work.

## Related

- [[distractor-similarity-reasoning-inflation]] — irrelevant context that looks like the question inflates reasoning tokens; this note is the opposite move, removing the irrelevant detail before reasoning starts.
- [[context-register]] — a fixed-shape store that keeps agent reasoning state out of the raw trace; the same separation of structured state from raw text, on the agent side.
- [[structure-then-select-compression]] — structures a context and keeps query-relevant parts under a budget; it targets input length, where this note targets reasoning length.
- [[matched-budget-evidence-comparison]] — a structured packet against raw dialogue at a fixed word budget; there the structure wins on budget, here it wins on reasoning length.
- [[moderate-adaptive-reasoning-length]] — reasoning length has an optimum; the savings here come from dropping filler, not from a cap on thinking.

[^c1]: arxiv-2511-22176 — "structured representation and performs standard chain-of-thought reasoning."
[^c2]: arxiv-2511-22176 — "This structure contains two components: (1) enumerated information blocks"
[^c3]: arxiv-2511-22176 — "We hypothesize that this entanglement blurs the boundaries between relevant and irrelevant"
[^c4]: arxiv-2511-22176 — "the representation and structuring of information before higher-order reasoning."
[^c5]: arxiv-2511-22176 — "one-third of 0-shot CoT across all model sizes."
[^c6]: arxiv-2511-22176 — "questions, token counts decrease by about half."
[^c7]: arxiv-2511-22176 — "results comparable to 0-CoT across all three datasets, except for the smallest Qwen3 0.6B model,"
[^c8]: arxiv-2511-22176 — "halves the number of reasoning sentences and substantially reduces the number of filler sentences,"
[^c9]: arxiv-2511-22176 — "primarily results from fewer reasoning and filler sentences, while the"
[^c10]: arxiv-2511-22176 — "Incorporating the context reduces the score to 1.74"
[^c11]: arxiv-2511-22176 — "fewer than 2% of generations produce a valid context."
[^c12]: arxiv-2511-22176 — "typically requires only a few tokens, using a larger, slower, and more expensive LLM, and then"
[^c13]: arxiv-2511-22176 — "enumerated lists yield comparable performance, suggesting that the key benefit arises from structure"
[^c14]: arxiv-2511-22176 — "Given the small dataset size (30 samples) and potential test-set"
[^c15]: arxiv-2511-22176 — "we observed rare cases in which instructions such as"
[^c16]: arxiv-2511-22176 — "0-CoT performance could likely match structured context"
[^c17]: arxiv-2511-22176 — "gap of more than 1k tokens between the inference with and without the context, even"
[^c18]: arxiv-2511-22176 — "Currently, the evaluated models were not trained with such"
[^c19]: arxiv-2511-22176 — "information pieces, further decreases the token count."
[^c20]: arxiv-2511-22176 — "to about 3.1k (+747 tokens"
