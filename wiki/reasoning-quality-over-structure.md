---
description: "Under one fixed template, a chain of thought from a strong generator beats one from a lightweight generator by 7.5 Pass@1 points; low-quality reasoning can fall below no reasoning."
aliases: ["reasoning quality", "quality over structure", "CoT quality versus template", "chain-of-thought quality effect"]
sources: ["arxiv-2512-09679"]
---
# Reasoning quality over structure

A chain of thought (CoT) placed before generated code is often treated as a template choice: pick a good structure and the reasoning follows. The paper separates the two. It holds the template fixed and varies only how the reasoning was generated. Both arms use the same sections, problem analysis, then algorithm design, then edge case handling, then implementation. "Both MSCoT and SCoT follow identical template structures." They differ in the generator and the output. The high-quality arm (SCoT) is written by GPT-5-Mini from three in-context exemplars, and the lightweight arm (MSCoT) by a fine-tuned 7B model, with "MSCoT: 150 tokens average, SCoT: 380 tokens average."[^c1]

Under that control the high-quality chain wins consistently. "Across all 12 model-type combinations, SCoT achieves higher Pass@1 than MSCoT," with "an average advantage of +7.50 percentage points."[^c2] The paper's H4 is that reasoning quality, not just paradigm structure, determines CoT effectiveness, and it reads the SCoT-minus-MSCoT difference as "a proxy for differences in" the information the chain carries about the code.[^c3]

The mechanism it gives is an information channel. The chain "functions as an auxiliary information channel transmitting task-relevant signals from input" to output.[^c4] The quantity of interest is the conditional mutual information I(Y; C | X) between the code Y and the chain C, given the problem X, which is the information the chain adds beyond the problem ([[mutual-information]] in its conditional form). A chain that carries useful signal lowers the uncertainty about the code. A poor chain can do the reverse. The paper's account of the lightweight arm is that it introduces misleading constraints: "low-quality structured reasoning can harm performance by introducing spurious constraints that mislead."[^c5]

The harm is real in the numbers. The lightweight arm "underperforms Zero-Shot baseline," at "-2.77% average compared to Zero-Shot across all models," and the largest drop is GPT-5 at -4.64%.[^c6] Naive prompting shows the same sign. The abstract says "naive Zero-Shot CoT can even degrade performance," and the paper attributes the drop to hallucinated reasoning: "unguided self-generated reasoning often degrades performance."[^c7][^c8]

The quality effect is not flat across models. "Quality gap widens in smaller models," and "GPT-3.5 and Qwen2.5-7B show the largest" gaps, while the largest model shows a smaller one. The paper's reading is that "smaller models depend more critically on reasoning quality," because they lack internal mechanisms to filter weak guidance.[^c9] The same gradient appears in the benefit of the high-quality chain itself, which is taken up in [[cot-capacity-responsiveness]].

## Limits

- The two arms are not a clean manipulation of quality. They differ in generator (GPT-5-Mini against a fine-tuned 7B), in exemplar use, and in length (380 against 150 tokens). "Quality" here is bundled with who wrote the chain and how long it is. The text read here does not separate these.
- Quality is not scored directly. As far as the text shows, a chain counts as high-quality because of the generator that produced it, not because a rater or a metric judged it so (my reading).
- The paper calls its lens "conceptual rather than based on exact mutual information estimation."[^c10] The SCoT-minus-MSCoT gap is a proxy for I(Y; C | X), not a measurement of it, and the paper's claim that reasoning "determines information gain" is its own interpretation.[^c11]
- The evidence is code generation on Pass@1 with test cases, across six Python benchmarks and HumanEval-XL. Nothing here shows the effect for reasoning tasks outside code.
- At the largest model the quality advantage nearly vanishes: GPT-5 "shows minimal benefit even from high-quality reasoning." So "quality matters" holds only below some capacity, and the threshold is model-specific. See [[cot-capacity-responsiveness]].
- One template family (three-shot structured CoT) was used. Whether another template changes the size of the gap was not tested.

## Related

- [[information-rate-per-token]] — the same chain-as-channel idea, per output token, measured on compressors rather than on reasoning chains.
- [[mutual-information]] — the conditional form I(Y; C | X) that the paper uses for the chain's contribution.
- [[pre-committed-answer-before-cot]] — a trace can be written after its answer is already fixed, so it carries no new signal; a route to the low-quality end of this axis.
- [[stepwise-self-qa-scaffold]] — another scaffold whose value depends on the quality of what fills each step.
- [[cot-capacity-responsiveness]] — the same comparison across model sizes; the quality gap is largest in the small models and nearly gone in the largest.

[^c1]: arxiv-2512-09679 — "Both MSCoT and SCoT follow identical template structures"
[^c2]: arxiv-2512-09679 — "Across all 12 model-type combinations, SCoT achieves higher Pass@1 than MSCoT"
[^c3]: arxiv-2512-09679 — "reasoning quality critically determines downstream effectiveness; the performance difference between SCoT and MSCoT under a fixed template serves as a proxy for differences in"
[^c4]: arxiv-2512-09679 — "functions as an auxiliary information channel transmitting task-relevant signals from input"
[^c5]: arxiv-2512-09679 — "This indicates that low-quality structured reasoning can harm performance by introducing spurious constraints that mislead"
[^c6]: arxiv-2512-09679 — "Lightweight reasoning (MSCoT) underperforms Zero-Shot baseline"
[^c7]: arxiv-2512-09679 — "naive Zero-Shot CoT can even degrade performance"
[^c8]: arxiv-2512-09679 — "unguided self-generated reasoning often degrades performance"
[^c9]: arxiv-2512-09679 — "smaller models depend more critically on reasoning quality"
[^c10]: arxiv-2512-09679 — "conceptual rather than based on exact mutual information estimation"
[^c11]: arxiv-2512-09679 — "Reasoning quality determines information gain"
