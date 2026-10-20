---
description: "Eliciting a supporting rationale for every answer option, each treated as correct, before one synthesis step picks the answer; measured only on 7B models under greedy decoding."
aliases: ["BiasPrompting", "option-wise rationale generation", "reasoning for every choice before agreement", "reasoning-guided agreement"]
sources: ["arxiv-2511-20086"]
---
# Per-option elaboration before choice

When a multiple-choice question is answered, the candidates on the page shape what gets retrieved. The premise of one prompting method is that a model given only the options fails to surface the facts that would separate them: the authors say LLMs struggle to retrieve relevant facts "when provided only with answer options."[^c1] The usual consequence, in their account, is that the model "often generates reasoning for its chosen option only, ignoring underexplored alternatives."[^c2]

The method, named BiasPrompting, changes the order of work in two stages. In the first, the model is asked for a reasoning for each option A_i, written so that it supports A_i "as if it were correct"[^c3] and "were the correct answer, regardless of its actual validity."[^c4] In the second, a new prompt carries the question, the options and all of the generated reasonings, and asks for one choice: "BiasPrompting constructs a final prompt that integrates the" question, options and reasonings.[^c5] The mechanism claimed is that the first stage makes the model explore every candidate before committing, "preventing premature dismissal of alternatives."[^c6] The reasonings need not be true for this to work, on the authors' account: "Even if some generated reasonings are incorrect" the step is said to enrich the model's context.[^c14]

Cost is the other side of the design. Every option gets its own generation, but the paper argues the whole thing runs as a single pass inside one model: the "single-pass design, which integrates reasoning for all answer choices within one prompt" avoids the multi-round chains of chain-of-thought.[^c7] Its token comparison is against chain-of-thought, not against a plain zero-shot prompt.

What was measured: accuracy on five commonsense multiple-choice sets (CommonsenseQA, StrategyQA, PIQA, and two BIG-Bench Hard tasks), with 2 to 6 options per question, on three 7B instruction models, all under greedy decoding.[^c17] The paper states that "BiasPrompting consistently achieves superior performance" and reports it against zero-shot and chain-of-thought baselines; its own table shows gains in most cells rather than all.[^c8] Its order-robustness result is the sharper one: across three random orderings of the options, median accuracy was higher and variance lower than zero-shot "in all cases," and the authors read this as a reduction in sensitivity to option order.[^c9] Adding chain-of-thought on top of the per-option stage did "not lead to significant improvements in final answer prediction," which the authors take to mean that "BiasPrompting alone is sufficient for improving performance."[^c10][^c15]

The idea transfers as a question about commitment rather than about one benchmark. Asking for a justification of each candidate before choosing is a way to delay the answer, which is what a candidate-set search needs; whether the gain comes from the elaboration itself or from the synthesis over several rationales is not separated by the paper (my inference).

## Limits

- The experiments are commonsense reasoning only: "our experiments primarily focus on commonsense reasoning tasks."[^c11] No math, code or open-ended generation was tested.
- The models are small: "our study is limited to 7B parameter models."[^c12] The text itself says the impact on larger models is still unexplored.[^c16]
- Every cell is a single greedy run ("employ greedy decoding"[^c13]). The significance test is a two-proportion z-test per dataset and model pair, and the order-robustness result uses three random orderings per model, with no seeds or spread reported in the text.[^c18]
- Table 1 is not uniformly positive. Where I read the printed numbers, at least one cell has BiasPrompting below zero-shot (48.5 against 50.1), and several gains are under one point (my reading of a garbled table).[^c19]
- The text has no ablation that separates the "as if correct, regardless of validity" framing from a neutral per-option explanation, or from simply listing the options. So the paper does not show that the adversarial framing, rather than per-option attention, does the work (my inference from the method and the experiments).
- The first stage costs one generation per option, so cost grows with the number of candidates. The efficiency claim is against chain-of-thought on these benchmarks, not against zero-shot.

## Related

- [[option-matching-shortcut]] — options can make reasoning models match candidates instead of deducing; per-option elaboration is one response that keeps the options visible.
- [[generate-then-verify-candidate-pipeline]] — another split between widening a candidate list and choosing from it, here by a recall-oriented generator and a precision-oriented verifier.
- [[permutation-consistency-training]] — the trained route to option-order robustness; the prompting route here reports a similar effect without training.
- [[pre-committed-answer-before-cot]] — the failure that committing early produces, which per-option elaboration may delay (my inference; the paper does not test this link).

[^c1]: arxiv-2511-20086 — "facts when provided only with answer options"
[^c2]: arxiv-2511-20086 — "for its chosen option only, ignoring underexplored alternatives"
[^c3]: arxiv-2511-20086 — "treating each as if it were correct"
[^c4]: arxiv-2511-20086 — "were the correct answer, regardless of its actual validity"
[^c5]: arxiv-2511-20086 — "BiasPrompting constructs a final prompt that integrates the"
[^c6]: arxiv-2511-20086 — "preventing premature dismissal of alternatives"
[^c7]: arxiv-2511-20086 — "single-pass design, which integrates reasoning for all answer choices within one prompt"
[^c8]: arxiv-2511-20086 — "BiasPrompting consistently achieves superior performance"
[^c9]: arxiv-2511-20086 — "In all cases, BiasPrompting yields higher median accuracy and lower variance than Zero-shot"
[^c10]: arxiv-2511-20086 — "not lead to significant improvements in final answer prediction"
[^c11]: arxiv-2511-20086 — "our experiments primarily focus on commonsense reasoning tasks"
[^c12]: arxiv-2511-20086 — "our study is limited to 7B parameter models"
[^c13]: arxiv-2511-20086 — "employ greedy decoding"
[^c14]: arxiv-2511-20086 — "Even if some generated reasonings are incorrect"
[^c15]: arxiv-2511-20086 — "BiasPrompting alone is sufficient for improving performance"
[^c16]: arxiv-2511-20086
[^c17]: arxiv-2511-20086
[^c18]: arxiv-2511-20086
[^c19]: arxiv-2511-20086
