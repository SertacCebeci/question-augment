---
description: "A test-item generator conditioned on IRT difficulty and fine-tuned on items that miss the requested difficulty keeps questions at an examinee's ability boundary as models outgrow a static pool."
aliases: ["generative evolving testing", "GETA", "adaptive item generation with IRT"]
sources: ["doi-10-48550-arxiv-2406-14230", "arxiv-2512-18160"]
---
# Difficulty-conditioned evolving item generation

Static question pools fail twice as models improve: items leak into training data, and they saturate, so a strong model is overestimated because nothing in the pool is hard enough for it.[^c1] Computerized adaptive testing (CAT) picks items by estimated difficulty but still draws from that fixed pool, so it inherits the ceiling.[^c2]

The mechanism (GETA, Generative Evolving Testing) trains one model on two jobs. A variational item-response-theory estimator infers item parameters (difficulty, discrimination) from the responses of many LLMs and infers each examinee's ability from its response history. An LLM item generator, trained jointly through an evidence lower bound, writes new items given a target difficulty.[^c3] The generator is the "self-evolving item pool", so each examinee can be asked fresh items pitched at its own boundary.[^c4]

Evolution handles the case where the target difficulty lies outside the training data. After pretraining, the generator produces items for a target difficulty d*, all examinees answer them, and the true difficulty is re-estimated. Items whose estimated difficulty is within a small tolerance of d* update the examinee's ability estimate. Items that miss d* by a large margin show where the generator is wrong beyond its data, and they are collected to fine-tune the generator, stretching the difficulty range it can reach.[^c5] My reading: the miss between requested and measured difficulty is the training signal, so the question writer is corrected by examinee responses instead of by human labels.

A cruder label comes from self-play. In PSV, a proposer is conditioned on difficulty without any fitted item model: the difficulty of a question is the current solver's verified pass rate on it, over several samples, binned into easy, medium, hard and impossible by thresholds.[^c6] The proposer is shown sampled questions with their labels and asked for a new question at the target level.[^c7] Because the label is a prompt rather than an estimated parameter, the control is partial. Hard-targeted questions have mean pass rate 0.36 under the solver that produced them,[^c8] and the authors describe the control as partial.[^c10]

## Limits

- The abstract's claims (difficulty-tailored items, results consistent with existing benchmarks) were not re-checked here beyond the method description; I read the method section, not the experiments.
- The domain is value and moral-boundary conformity of LLMs; whether difficulty is as well-defined, and the generator as controllable, for factual or reasoning questions is not shown.
- Difficulty is relative to the examined LLM population, so it is not an intrinsic property of the question.
- The scheme needs several examinee LLMs to calibrate items, which a single-model setting lacks.
- The PSV variant has no item model: its labels are the solver's own sampled pass rates, and the bin edges are hyperparameters.[^c11] Its contribution is measured by removing the labels, which lowers the average across metrics by 5.6%,[^c9] and the labels are not a calibrated difficulty scale; the authors call the control "partial but incomplete".[^c10]

## Related

- [[rubric-difficulty-evolution]] — also raises difficulty iteratively, but through rubrics rather than IRT-calibrated items
- [[post-cutoff-corpus-benchmark-isolation]] — another route to leakage-free testing, by date rather than on-the-fly generation
- [[pairwise-confidence-adaptive-ranking]] — adaptive selection of what to ask next, based on current uncertainty
- [[sound-verifier-self-play]] — the same proposer-solver loop with a formal verifier's verdict as the pass/fail label behind the difficulty bins

[^c1]: doi-10-48550-arxiv-2406-14230 — "the rapidly advancing LLMs can"
[^c2]: doi-10-48550-arxiv-2406-14230 — "may lead to overestimation due to insufficiently challenging"
[^c3]: doi-10-48550-arxiv-2406-14230 — "Item Generator, pω (x|d), is trained to generate new test"
[^c4]: doi-10-48550-arxiv-2406-14230 — "serving as a self-evolving"
[^c5]: doi-10-48550-arxiv-2406-14230 — "further extending the item"
[^c6]: arxiv-2512-18160 — "We categorize problems into one of four classes based on"
[^c7]: arxiv-2512-18160 — "ask the proposer to output a question at a target"
[^c8]: arxiv-2512-18160 — "hard-targeted questions have mean 0.36"
[^c9]: arxiv-2512-18160 — "this -Difficulty ablation causes an average drop of 5.6%"
[^c10]: arxiv-2512-18160 — "partial but incomplete control over generated question"
[^c11]: arxiv-2512-18160 — "where the thresholds τE and τM are hyperparameters for"
