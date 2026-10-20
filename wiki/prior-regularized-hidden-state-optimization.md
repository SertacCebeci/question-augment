---
description: "Gradient ascent on a classifier's log-likelihood minus an L2 penalty to the original hidden state; the penalty weight λ trades reasoning gain against text quality in a base LLM."
aliases: ["MAP hidden-state steering", "gradient-based activation optimization", "likelihood-prior latent steering", "penalised hidden-state optimisation"]
sources: ["arxiv-2511-19131"]
---
# Prior-regularized hidden-state optimization

A fixed steering vector pushes every input by the same offset. This method instead moves each input's hidden state by optimisation, under an objective with two parts. The paper's framing is that the hidden state h is the mediator between a condition c (here, a chain-of-thought mode) and the text: the text is decoded from h, so the hard step is finding an h that satisfies c.[^c1] Sampling such an h from the posterior is intractable, so the paper takes the maximum a posteriori point instead: "we employ Maximum Posterior (MAP)" estimation.[^c2]

The two terms are these. The likelihood is a small multi-layer perceptron classifier f(h) that estimates how likely a state is to belong to the target mode; it is trained on hidden states of CoT and non-CoT responses.[^c3] The prior is a penalty on distance from the original state h0, the state the input produces on its first forward pass. The prior is described as "constraining hidden states to remain proximate to the original" state.[^c4] The optimiser is gradient ascent on log f(h) minus λ times the L2 distance to h0. The step size is adaptive: it shrinks as the classifier output approaches the target τ. Gaussian noise is added at each step.[^c5] The loop stops once the classifier passes τ, which the paper's algorithm writes as "Stop when condition is satisfied".[^c6] In the reported configuration the maximum is 200 iterations, the initial step is 0.1, λ is 0.01 and τ is 0.9.[^c7] Algorithm 1 applies this loop at the chosen layers for each generated token and writes the optimised state back before the next token is decoded. That per-token reading is mine, from the algorithm's structure.

The weight λ is the knob that decides the outcome. The paper says it "controls the trade-off between the likelihood term and the prior distribution".[^c8] Too little prior is one failure: the paper warns that inappropriate values "may fail to reach the CoT mode or push hidden states" off the language manifold.[^c9] In the λ sweep the paper reports that below 0.01 accuracy rises "alongside decreasing language quality", which it reads as an operating region.[^c10] Above 0.01 both fall: "As λ exceeds 0.01, language quality drops significantly, and reasoning performance also decline".[^c11]

Against vector baselines (difference of means, PCA, logistic regression, SVM boundary projection, directional ablation), the paper reports that the vector methods "achieve only marginal improvements".[^c12] Its own method reaches gains "of up to 14.56% on" MultiArith with Gemma-7b.[^c13] Gains on commonsense and logical tasks are smaller, and the authors say these "remain consistent" but "more modest".[^c14]

The Bayesian decomposition is used as a design device. The prior p(h) ∝ exp(−d(h, h0)) is a chosen penalty, not a density fitted to hidden states. The classifier output is not tested as a calibrated probability. In this formulation the "posterior" is a name for a penalised objective. This is my reading of the construction, not a claim the paper makes.

The paper also derives bounds on λ. Lemma 1 gives an upper bound from keeping the update's gradient close to the classifier's gradient: "Lemma 1. Assume that the cosine similarity is larger than" a threshold near 1.[^c15] Lemma 2 gives a lower bound from step magnitude. The conclusion states the result as "theoretically guaranteed to activate reasoning without causing distribution shift".[^c16] The lemmas as stated are conditional on their assumptions, so that wording is stronger than the statements. I read the statements only; the proofs are in the appendix.

## Limits

- The method unlocks what the base model already has. The paper writes that "our method can only unlock intrinsic reasoning abilities rather" than adding capability.[^c17]
- Effectiveness "depends significantly on the classification performance related to representations and layer" selection.[^c18] The classifier was trained on "a dataset of 2000 response pairs" from Mistral-7b on GSM8K, labelled by GPT-4.[^c19][^c28] Transfer to the other three models is asserted: the classifiers "generalize well to other models, showing strong method" transfer.[^c20] Four base models and eight benchmarks is the whole test.
- One hyperparameter setting is reported.[^c7] The λ and τ sweeps were run on "Mistral-7b on the GSM8K dataset".[^c21] The text does not say whether the other models were tuned separately.
- Decoding is greedy: "the sampling strategy in text generation is set to greedy sampling".[^c22] Behaviour under sampling is not tested.
- Text quality is measured by proxies: n-gram entropy, perplexity, and a judge score. The judge is "GPT-4o to evaluate the reasoning content in generated text".[^c23] None of these is a human reading of the output.
- Compute cost is not in the main text: "More comprehensive overhead analysis is" deferred to the appendix.[^c24] The per-token inner loop of up to 200 steps is a cost I infer from the algorithm.
- The paper suggests the weaker commonsense and logic gains "may demand more domain-specific knowledge beyond pure reasoning ability".[^c25] That is offered as a suggestion, not tested here.
- Linear steering is criticised as having no objective and no bound: it "fails to adapt to instance-specific variations", and "applies unbounded steering strength".[^c26][^c27] The paper's comparison is against the baselines it ran at strength 1, so a tuned linear baseline is not shown.

## Related

- [[mean-difference-steering-vector]] — the fixed additive offset this method replaces with a per-state optimisation; the paper's difference-of-means baseline is that construction.
- [[test-time-prefix-steering]] — also optimises a test-time vector, but learned input prefixes tuned to minimise output entropy, with no distance penalty to an original state.
- [[topology-conditioned-activation-steering]] — rebuilds the steering direction per query from neighbours; this method keeps one state per input and moves it by gradient.

[^c1]: arxiv-2511-19131 — "serves as the causal mediator between CoT condition c and"
[^c2]: arxiv-2511-19131 — "we employ Maximum Posterior (MAP)"
[^c3]: arxiv-2511-19131 — "we implement a Multi-Layer Perceptron classifier"
[^c4]: arxiv-2511-19131 — "constraining hidden states to remain proximate to the original"
[^c5]: arxiv-2511-19131 — "we incorporate Gaussian noise"
[^c6]: arxiv-2511-19131 — "Stop when condition is satisfied"
[^c7]: arxiv-2511-19131 — "maximum iterations at 200, α0 at 0.1, λ at 0.01, and τ at 0.9"
[^c8]: arxiv-2511-19131 — "where λ is a hyperparameter that controls the trade-off between the likelihood term and the prior distribution"
[^c9]: arxiv-2511-19131 — "values may fail to reach the CoT mode or push hidden states"
[^c10]: arxiv-2511-19131 — "we observe an increase in performance alongside decreasing language quality"
[^c11]: arxiv-2511-19131 — "As λ exceeds 0.01, language quality drops significantly, and reasoning performance also decline"
[^c12]: arxiv-2511-19131 — "Control vector-based methods achieve only marginal improvements"
[^c13]: arxiv-2511-19131 — "achieving performance gains of up to 14.56% on"
[^c14]: arxiv-2511-19131 — "While improvements on commonsense and logical reasoning tasks are more modest, they remain consistent"
[^c15]: arxiv-2511-19131 — "Lemma 1. Assume that the cosine similarity is larger than"
[^c16]: arxiv-2511-19131 — "theoretically guaranteed to activate reasoning without causing distribution shift"
[^c17]: arxiv-2511-19131 — "our method can only unlock intrinsic reasoning abilities rather"
[^c18]: arxiv-2511-19131 — "depends significantly on the classification performance related to representations and layer"
[^c19]: arxiv-2511-19131 — "These responses are then classified by GPT-4 as either CoT"
[^c20]: arxiv-2511-19131 — "but generalize well to other models, showing strong method"
[^c21]: arxiv-2511-19131 — "observe its impact, using Mistral-7b on the GSM8K dataset"
[^c22]: arxiv-2511-19131 — "the sampling strategy in text generation is set to greedy sampling"
[^c23]: arxiv-2511-19131 — "We use GPT-4o to evaluate the reasoning content in generated text"
[^c24]: arxiv-2511-19131 — "More comprehensive overhead analysis is"
[^c25]: arxiv-2511-19131 — "domain-specific knowledge beyond pure reasoning ability"
[^c26]: arxiv-2511-19131 — "It fails to adapt to instance-specific variations"
[^c27]: arxiv-2511-19131 — "Furthermore, it applies unbounded steering strength"
[^c28]: arxiv-2511-19131 — "a dataset of 2000 response pairs"
