---
description: "Prompt search as Bayesian optimization: a surrogate fitted to past (prompt, tests-passed) pairs picks the next prompt to try, so fewer prompts are tried before code passes its tests."
aliases: ["BODE-GEN", "Bayesian optimization for prompt search", "BO for code generation prompts", "surrogate-guided prompt search"]
sources: ["arxiv-2512-15076"]
---
# Bayesian prompt optimization

Treat a prompt as the input to an expensive black box. One evaluation means: give the prompt to a base model, generate code, run the tests, and record a score. The problem is which prompt to try next. Bayesian optimization answers with two parts. A surrogate model is fitted to all the (input, outcome) pairs so far, and an acquisition function scores each untried input by its utility, trading exploitation of the current best estimate against exploration of what is uncertain.[^c1] The paper's claim is that this choice is what makes the search sample-efficient: "BO is sample-efficient because it makes a data-driven decision to select the next input to query the"[^c2] objective, instead of drawing prompts at random or by trial and error.

The obstacle is that a prompt is discrete text, and a surrogate needs a space in which nearness means something. The paper's device is to search over continuous vectors in the embedding space of an auxiliary language model, which "bridge[s] the gap between continuous embedding space and discrete prompt space."[^c3] A candidate vector is concatenated with the embedding of a fixed rephrasing instruction and of the initial prompt; the auxiliary model then generates "a human-interpretable discrete prompt" from it. That prompt goes to the base model, the code is run on the tests, and "the percentage of test cases passed by the code is used as the objective function value."[^c4] The loop is: propose a vector, decode a prompt, generate and test code, update the surrogate, propose again.

## The high-dimensional surrogate

Gaussian process surrogates are the usual choice, and they "work well in low dimensions"; the auxiliary embedding here is 4096-dimensional, and a standard GP "struggle[s] to generalize" on such a space with little data.[^c5] The paper uses two devices together. The first is a random projection. Each embedding is projected to a lower dimension, so that "We randomly project each embedding to a 64 dimensional space resulting in a overall search space of 256" dimensions for four embeddings.[^c6] The stated reason is that the projection keeps pairwise distances, so the GP works on a space where similarity is preserved (the paper cites the Johnson-Lindenstrauss lemma for this).

The second device is a prior on the kernel lengthscales, scaled by the dimension. The paper "consider[s] the recently proposed idea of scaling" the lengthscale prior "with the square root of the input dimensionality of the search space," as a LogNormal whose mean is the log of the square root of the dimension.[^c7] The lengthscale sets how fast the surrogate's predicted score may change between nearby inputs, so in a small-data, high-dimensional setting the prior does much of the work of deciding what counts as nearby. The paper calls this prior specification "critical to achieve good performance on high-dimensional" inputs.[^c8] Acquisition is expected improvement, taken "due to its practical success without any hyper-parameters" and maximized over a discrete set of 10K candidates.[^c9]

## What was measured

On HumanEval+ with ChatGPT-3.5 Turbo as the base model, the paper reports that BODE-GEN "achieves an average code generation accuracy of 0.89 on ChatGPT-3.5Turbo[7], which is higher"[^c10] "than that of initial prompts (0.61), CoT (0.63), and OPRO (0.78)."[^c11] For CodeLlama-7b it reports that BODE-GEN "archives an average code generation accuracy of 0.5 on CodeLlama-7b[28], which is higher" than the initial prompts, CoT and OPRO.[^c12] The sample-efficiency claim is stated as "requiring relatively few iterations of BO to"[^c13] reach these gains; the curves are over 70 iterations, with "multiple seeds (five)" and mean and error bars.[^c14]

## Limits

- **The objective is the tests.** The score is the fraction of tests a generated program passes, so the search can only optimize what the tests check. The authors list the open problem as "reducing the dependency of" the method "on the requirement of test cases for coding tasks."[^c15]
- **Discrete spaces resist surrogates.** The paper itself says that "modeling of combinatorial objects (e.g., sequences) is quite challenging,"[^c16] which is why the search is moved to embeddings. The surrogate therefore models distances between embedding vectors, not between prompts. Two vectors close in embedding space can decode to very different prompts, and the reverse (my inference: the decoding is many-to-one and the paper does not measure its smoothness).
- **Determinism is set, not shown.** To limit hallucination in the decoder, the paper "set[s] the temperature of the auxiliary LLM to zero in our experiments,"[^c17] and it notes that developers "may need slightly more iterations to get the same improvement as shown in our evaluation."[^c18] The run-to-run stability of the gains is therefore not established beyond the seeds reported.
- **The projection and the prior are not isolated.** In the sections read, no ablation separates the random projection from the scaled prior, so it is not measured which one carries the sample efficiency (my reading of the text read).
- **Benchmark and model breadth.** "Yet the prompts in it may not represent real-world code-synthesis prompts,"[^c19] and "With the rapid evolution of LLMs, more advanced models may not" necessarily gain as much.[^c20] Only three base models and one benchmark appear in the results.
- **Cost is not in the slices read.** Iterations are counted, but the dollar or compute cost of the auxiliary decoding plus the base-model calls is not compared against the baselines in the parts read.

## Related

- [[evolutionary-prompt-search]] — the same search over wordings by a score, with no surrogate: a population is recombined by a model and the best are kept. Bayesian optimization instead fits a model to every past score and picks the next candidate by an acquisition rule.
- [[bayesian-experimental-design]] — the same one-step move, choosing the next query by expected value before the answer is heard; here the query is a prompt and the answer is a pass fraction.
- [[surrogate-uncertainty-sharpness-for-query-selection]] — an acquisition rule is only as good as the surrogate's uncertainty ranking, and the lengthscale prior is one place where that ranking is set here.

[^c1]: arxiv-2512-15076 — "to learn a surrogate model from the past evaluations (prompt and code accuracy pairs) and use it to"
[^c2]: arxiv-2512-15076 — "BO is sample-efficient because it makes a data-driven decision to select the next input to query the"
[^c3]: arxiv-2512-15076 — "to bridge the gap between continuous embedding space and discrete prompt space."
[^c4]: arxiv-2512-15076 — "The percentage of test cases passed by the code is used as the objective function value"
[^c5]: arxiv-2512-15076 — "well in low dimensions, but the embedding dimension for auxiliary LLM such as LLama2 is 4096"
[^c6]: arxiv-2512-15076 — "We randomly project each embedding to a 64 dimensional space resulting in a overall search space of 256"
[^c7]: arxiv-2512-15076 — "the prior on the lengthscale hyper-parameters of the GP kernel with the square root of the"
[^c8]: arxiv-2512-15076 — "specification for this parameter is critical to achieve good performance on high-dimensional"
[^c9]: arxiv-2512-15076 — "due to its practical success without any hyper-parameters"
[^c10]: arxiv-2512-15076 — "achieves an average code generation accuracy of 0.89 on ChatGPT-3.5Turbo[7], which is higher"
[^c11]: arxiv-2512-15076 — "than that of initial prompts (0.61), CoT (0.63), and OPRO (0.78)."
[^c12]: arxiv-2512-15076 — "archives an average code generation accuracy of 0.5 on CodeLlama-7b[28], which is higher"
[^c13]: arxiv-2512-15076 — "requiring relatively few iterations of BO to"
[^c14]: arxiv-2512-15076 — "We ran BO for multiple seeds (five) and present results with mean"
[^c15]: arxiv-2512-15076 — "Future work includes reducing the dependency of"
[^c16]: arxiv-2512-15076 — "modeling of combinatorial objects (e.g., sequences) is quite challenging"
[^c17]: arxiv-2512-15076 — "we set the temperature of the auxiliary LLM to zero in our experiments"
[^c18]: arxiv-2512-15076 — "they may need slightly more iterations to get the same improvement as shown in our evaluation"
[^c19]: arxiv-2512-15076 — "Yet the prompts in it may not represent real-world code-synthesis prompts"
[^c20]: arxiv-2512-15076 — "With the rapid evolution of LLMs, more advanced models may not"
