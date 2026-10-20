---
description: "Summing each generated token's direct influence on the prompt drops paths through earlier generations; marginalizing a row-stochastic influence graph over those paths keeps them."
aliases: ["context attribution via graph explanations", "CAGE", "attribution graph marginalization", "influence propagation across generations"]
sources: ["arxiv-2512-15663"]
---
# Inter-generational context attribution

A context attribution asks how much of a generated output traces back to the prompt. The common recipe applies a base attribution method to each generated token and sums the prompt-facing parts over the tokens of interest. That keeps only the direct influence of prompt tokens on each token and drops the influence that runs through earlier generated tokens.[^c1] In a chain of reasoning the later steps depend on the earlier ones, so the sum treats every intermediate token as contributing equally.[^c2]

The replacement is an attribution graph over all tokens, prompt and generated alike. Edges point forward in time only, so the graph is acyclic and its sources are the prompt tokens.[^c3] The incoming weights of each generated token are nonnegative and sum to one.[^c4] They come from the base attribution applied to that token, normalized so that each generated token distributes one unit of influence over the tokens before it.[^c5] The influence reaching the prompt is then not one direct edge but a sum over paths: each step adds the weighted attributions of a token's predecessors, and the paper extends this one-step calculation to the full matrix in closed form.[^c6] The context attribution of an output is obtained by "marginalizing the influences of all prior generations", which is the operation the method is named for.[^c7]

The part that carries over to asking and answering is bookkeeping, and this is my inference rather than the paper's claim. An account of why an answer holds should route through the intermediate steps the answer actually used. An account that cites the question directly can credit the wrong constraint, because it never sees the step that consumed it. The paper's own example is about reuse of prompt facts: the plain row sum "Does not capture fact reuse tracking", while the graph does.[^c8] The normalization also borrows a conservation assumption from attention rollout; the paper says the row-stochastic property "provides a probabilistic normalization aligned with attention rollout".[^c9] Whether this helps a human judge an explanation is not tested.

## What the paper measures

The evaluation uses Llama 3 (3B, 8B) and Qwen 3 (4B, 8B).[^c10] The datasets are chosen because they "require the model to use both multi-step information retrieval and chain-of-thought reasoning".[^c11] Against row attribution, CAGE wins all 40 faithfulness tests, with an average improvement of 11% and a maximum of 30%.[^c12][^c13] The abstract states the headline as "CAGE improves context attribution faithfulness, achieving average gains of up to 40%".[^c14] The body attaches the 134% maximum and 40% average to a different quantity, "AC".[^c15] The text does not define AC in one line; from the surrounding coverage discussion it reads as a ground-truth coverage measure (my reading). So the 40% is not the faithfulness average, which is 11%.

## Limits

The graph is offered as a model of influence, not as the model's computation: "The CAGE framework is designed as a structured abstraction for tracing influence propagation through autoregressive generations".[^c16] Propagation is linear by construction, and the paper says so: "We do not intend to approximate the full nonlinearity of the transformer architecture".[^c17] Interactions that a transformer computes nonlinearly are therefore absent from the sums.

The nonnegative, row-stochastic normalization is a choice with a stated reason: allowing negative values through the graph would "produce unstable magnitudes, oscillating signs, and result in information cancellation".[^c18] The ablation shows the cost of relaxing it, "substantially degrades faithfulness and interpretability";[^c19] signed graphs and alternative normalizations are left to future work. Inhibitory effects, which a signed account would keep, are thus excluded by design.

The method is trivial for single-token outputs: explaining one generation "would be a degenerate case where it is equivalent to row attribution".[^c20] Any gain therefore depends on the output containing several generated steps that depend on one another.

Faithfulness is scored by input perturbation, "Following prior LLM attribution work", so the score inherits that family's weakness.[^c21] Removing parts of an input pushes it out of distribution, and the removal-based scoring is confounded in the way [[ood-confounded-removal-evaluation]] describes. The paper does not test that confound (my inference).

Coverage is narrow: two model families, three datasets, all retrieval or reasoning tasks, and no human reader of the explanations. Nothing in the text supports the claim for open-ended answers.

## Related

- [[causal-model-of-explanation]] — explanation as giving causes; the attribution graph is a causally ordered structure, but the paper calls it an abstraction rather than a causal account of the model.
- [[attribution-narration-bottleneck]] — the other place an attribution meets language: there a fixed attribution is narrated by an LLM; here the attribution itself is the object being computed.
- [[ood-confounded-removal-evaluation]] — the removal-based scoring that this paper's faithfulness metric belongs to, and the confound that note identifies.

[^c1]: arxiv-2512-15663 — "relating generated tokens to the prompt, discarding inter-generational influence in the process"
[^c2]: arxiv-2512-15663 — "when explaining an output, context attributions aggregate scores by summation, implicitly assuming that all intermediate tokens contribute equally"
[^c3]: arxiv-2512-15663 — "Causality: Edges point forward in time, from earlier tokens to later generated tokens"
[^c4]: arxiv-2512-15663 — "incoming edge weights are nonnegative and sum to 1"
[^c5]: arxiv-2512-15663 — "We then construct the adjacency matrix A of G, by normalizing the values of T to be row stochastic"
[^c6]: arxiv-2512-15663 — "we can extend this calculation to solve for the full matrix Y as"
[^c7]: arxiv-2512-15663 — "the influence of the prompt tokens on any generated token can be computed by marginalizing the influences of all prior generations"
[^c8]: arxiv-2512-15663 — "Does not capture fact reuse tracking"
[^c9]: arxiv-2512-15663 — "the row stochasticity property provides a probabilistic normalization aligned with attention rollout"
[^c10]: arxiv-2512-15663 — "Across two variants of Llama 3 (3B, 8B)"
[^c11]: arxiv-2512-15663 — "we employ three datasets which require the model to use both multi-step information retrieval and chain-of-thought reasoning"
[^c12]: arxiv-2512-15663 — "graph approach wins 40/40 faithfulness tests"
[^c13]: arxiv-2512-15663 — "row attribution of 30% and 11%, respectively"
[^c14]: arxiv-2512-15663 — "CAGE improves context attribution faithfulness, achieving average gains of up to 40%"
[^c15]: arxiv-2512-15663 — "CAGE achieves a maximum and average improvement in AC of 134% and 40%"
[^c16]: arxiv-2512-15663 — "The CAGE framework is designed as a structured abstraction for tracing influence propagation through autoregressive generations"
[^c17]: arxiv-2512-15663 — "We do not intend to approximate the full nonlinearity of the transformer architecture"
[^c18]: arxiv-2512-15663 — "propagating these values through the graph will produce unstable magnitudes, oscillating signs, and result in information cancellation"
[^c19]: arxiv-2512-15663 — "relaxing non-negativity or row stochasticity substantially degrades faithfulness and interpretability"
[^c20]: arxiv-2512-15663 — "would be a degenerate case where it is equivalent to row attribution"
[^c21]: arxiv-2512-15663 — "Following prior LLM attribution work (Li et al., 2024; Zhao & Shan, 2024), we evaluate faithfulness"
