---
description: "Output stability has three levels (bitwise, distributional, semantic); judging a model by one greedy decode is argued to hide latent competence, brittleness and low-probability failures."
aliases: ["stability taxonomy", "deterministic inference critique", "single-greedy-run evaluation bias"]
sources: ["arxiv-2601-07239", "arxiv-2512-22258"]
---
# Distributional reproducibility versus bitwise determinism

The paper separates three notions of stability for LLM answers. Bitwise determinism means identical output at the bit level, which needs greedy decoding, reproducible kernels and a fixed environment. Distributional reproducibility means repeated runs approximate the same distribution p(y|x), so success rates and uncertainty profiles stay consistent. Semantic stability means the meaning or task outcome survives repeated queries or small perturbations.[^c1] The authors place determinism on a spectrum, not as a binary property.[^c2]

The claim for asking and answering is that a single deterministic answer is one draw from a distribution, not the model's competence. The paper argues that forcing one greedy path at T=0 can hide behaviours that depend on sampling several trajectories, such as self-consistency gains, and so underestimate latent competence.[^c3] It also argues the reverse for safety: a model that looks safe under greedy decoding can show low-probability, high-risk behaviour under modest stochasticity or paraphrased prompts.[^c4] A model can also score high on the original items under deterministic decoding while its robustness to paraphrase and perturbation is low. Aggregating over stochastic samples by majority vote is said to give a truer picture.[^c5]

The practical reading is that the question to ask of an answer is how stable it is across samples and phrasings, not only what the top answer is. Variability is a signal about model uncertainty, provided it comes from the model's distribution and not from uncontrolled numerical noise.[^c1]

The paper does not call determinism useless. It keeps deterministic modes for debugging, regression testing and exact on-policy RL, and objects only to making bitwise determinism the default norm for deployment and evaluation.[^c6]

## Limits

- The robustness heatmap is described only qualitatively ("a consistent pattern") in the text I read. I did not verify the numbers, the sample counts or any significance testing, so the empirical superiority of stochastic over greedy evaluation is the authors' claim, not something I confirmed.
- The comparison pairs greedy decoding with T=0.7, top-p 0.9 plus majority vote. This confounds sampling with aggregation: the gain may come from voting, not from stochasticity itself. That reading is mine.
- Semantic stability is defined loosely, with no operational test given in the passages read.
- Majority voting costs more compute per question. The paper does not weigh that cost here.
- A study can sit on the bitwise side of this distinction and still call itself deterministic. The LSP prompting paper sets the temperature to zero and disables top-p and top-k sampling "to eliminate stochastic variation in token generation."[^c7] Its own limits section then concedes that "complete end-to-end determinism is not guaranteed," and that "some condition evaluators may still rely on model-dependent components, such as semantic similarity judgments."[^c8][^c9] The passages read report no repeated runs, so distributional reproducibility was not measured there. The determinism it claims is that of a single greedy decode plus a validator, which is the bitwise sense this note sets apart. (My reading.)

## Related

- [[thinking-chain-entropy]] — entropy over sampled reasoning chains is one way to measure the spread this note treats as signal
- [[placebo-controlled-retry-evaluation]] — repeated-run evaluation, which needs the same care about what variance means

[^c1]: arxiv-2601-07239 — "the goal is not to produce the same answer every time, but to ensure that any variability reflects true model uncertainty"
[^c2]: arxiv-2601-07239 — "determinism in LLM inference is best understood as a spectrum, not a binary property"
[^c3]: arxiv-2601-07239 — "Forcing a single greedy path at T =0 can eliminate these behaviors, not because the underlying model lacks the capacity, but because the inference stack refuses to explore it."
[^c4]: arxiv-2601-07239 — "low-measure but high-risk behaviors emerge under modest stochasticity or paraphrased attack prompts"
[^c5]: arxiv-2601-07239 — "Deterministic evaluation, by design, hides both the latent diversity of correct behavior and the tails of failure"
[^c7]: arxiv-2512-22258 — "to eliminate stochastic variation in token generation"
[^c8]: arxiv-2512-22258 — "complete end-to-end determinism is not guaranteed"
[^c9]: arxiv-2512-22258 — "some condition evaluators may still rely on model-dependent components, such as semantic similarity judgments"
[^c6]: arxiv-2601-07239 — "deterministic modes remain indispensable for debugging, regression testing, and exact"
