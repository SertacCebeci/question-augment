---
description: "Proof of Quality checks an LLM output by averaging the scores of a few cheap evaluator models instead of proving the computation, and weighs quality against measured node latency."
aliases: ["Proof of Quality", "PoQ", "cost-aware Proof of Quality", "quality-consensus verification"]
sources: ["arxiv-2512-16317"]
---
# Quality-consensus verification

A model's output can be checked without checking the computation that produced it. Proof of Quality (PoQ) takes that route: it "replaces cryptographic verification of computation with consensus over" output quality.[^c1] The checkers are small learned evaluators, not the inference model, and the paper's motivation is cost: they "require orders of magnitude less computation than the original inference".[^c2]

The mechanism runs per round. The protocol picks one data record and one inference node, then draws a small set of evaluators (at most three in the paper's setting). "All selected evaluators have precomputed normalized scores" for that output.[^c3] The consensus quality is the average of those scores, a value that "lies in [0, 1] by construction" and "captures the average opinion of the sampled evaluators regarding the output quality".[^c4] The paper claims this reaches "consensus in seconds rather than hours", against optimistic and zero-knowledge proofs of inference.[^c5] The speed comes from the evaluators being much cheaper than inference; that link is my inference, not a measured result in the paper.

The paper's extension concerns cost. The original formulation rewards nodes on quality alone. The cost-aware version gives an inference node a reward equal to a quality term minus a cost term, where the cost is a value in [0, 1] derived from measured average latency. Only latency enters the reward: throughput and peak memory are "recorded for analysis in later sections", while only latency-based cost "is used inside the reward function."[^c6] The two weights "are tunable parameters that balance quality and efficiency objectives".[^c7] Raising the cost weight means that "high-latency models are penalized more strongly, so that" an efficient model can earn more with slightly lower quality.[^c8] Evaluator nodes are scored differently: "Evaluator nodes are rewarded based on how closely their scores agree with" the consensus, while their own cost is also counted.[^c9]

The reward behaviour is reported from a simulation. The abstract says "Monte Carlo simulations over 5 000 PoQ rounds demonstrate that the cost-aware reward scheme" gives higher average rewards to high-quality, low-cost models and to efficient evaluators.[^c10] The quality signal itself was measured on five instruction-tuned models, "ranging from TinyLlama-1.1B to" Llama-3.2-3B, on extractive question answering and abstractive summarization.[^c11] One finding cuts against the cost premise: "the largest models in the pool are also the most efficient in terms of quality" per unit latency.[^c12]

## Limits

- The reward result is a simulation over assumed inputs, not a live decentralized network. The abstract reports it only as Monte Carlo simulation.
- The quality term is only as good as its evaluators. The consensus is an average over at most three of them, so a bias that all evaluators share passes straight through the average. That is my inference; the paper does not test shared bias. Which evaluator architectures carry quality signal at all is a separate question, treated in [[evaluator-architecture-for-answer-quality]].
- Cost is latency only. The paper records other costs but does not put them in the reward.
- The paper's own scale is narrow: five models of 1.1 to 3.2 billion parameters, two task types, and GPT-4 used "as a proxy for human judgment".[^c13] The claim about large models being the most efficient is a measured trend on that pool, not a general law.
- The paper lists "setting, and adversarial resilience" among its design insights.[^c14] The text used for this note does not test adversarial behaviour, so nothing here relies on it.
- The baseline it improves on, the original PoQ, is described as one that "assumes homogeneous costs across nodes".[^c15] That is the paper's characterisation; the original work was not read here.

## Related

- [[evaluator-architecture-for-answer-quality]] — which evaluator architectures track quality at all; the quality term depends on that choice
- [[supervised-cross-model-consensus]] — learns which answer to trust from agreement features instead of averaging evaluator scores
- [[llm-judge-biases]] — the judge-model failure modes a PoQ evaluator pool would inherit
- [[cost-priced-joint-selection-and-stopping]] — the same quality-minus-cost linear trade-off, applied to choosing what to ask

[^c1]: arxiv-2512-16317 — "replaces cryptographic verification of computation with consensus over"
[^c2]: arxiv-2512-16317 — "require orders of magnitude less computation than the original inference"
[^c3]: arxiv-2512-16317 — "All selected evaluators have precomputed normalized scores"
[^c4]: arxiv-2512-16317 — "This value captures the average opinion of"
[^c5]: arxiv-2512-16317 — "achieving consensus in seconds rather than hours"
[^c6]: arxiv-2512-16317 — "is used inside the reward function."
[^c7]: arxiv-2512-16317 — "are tunable parameters that balance quality and efficiency objectives"
[^c8]: arxiv-2512-16317 — "high-latency models are penalized more strongly, so that"
[^c9]: arxiv-2512-16317 — "Evaluator nodes are rewarded based on how closely their scores agree with"
[^c10]: arxiv-2512-16317 — "Monte Carlo simulations over 5 000 PoQ rounds demonstrate that the cost-aware reward scheme"
[^c11]: arxiv-2512-16317 — "five instruction tuned LLMs ranging from TinyLlama-1.1B to"
[^c12]: arxiv-2512-16317 — "the largest models in the pool are also the most efficient in terms of quality"
[^c13]: arxiv-2512-16317 — "using GPT-4 as a proxy for human judgment"
[^c14]: arxiv-2512-16317 — "setting, and adversarial resilience."
[^c15]: arxiv-2512-16317 — "assumes homogeneous costs across nodes"
