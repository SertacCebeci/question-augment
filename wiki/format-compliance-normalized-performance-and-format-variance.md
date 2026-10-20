---
description: "Scoring accuracy only on format-compliant outputs confounds skill with format following; dividing by the compliance rate and taking variance across formats gives a format-bias metric."
aliases: ["output format bias", "EstTrue", "Bias_Fo", "format-following-normalized score", "LLM format bias"]
sources: ["doi-10-48550-arxiv-2408-08656"]
---
# Format-compliance-normalized performance and format variance

When a model is told to wrap its answer in a given way (bold, brackets, quotes, a placeholder), an automatic extractor can only read answers that obey the wrapping. The measured score therefore mixes two things: whether the model knew the answer, and whether it followed the format. Ding et al. separate them.

## The estimator

Let FI_C be the fraction of generations that satisfy the format constraint C. The systematic evaluation score SysE is accuracy over only those compliant generations. SysE misses correct answers that break the format, so it "may not accurately reflect the actual performance" of the model.[^c1] The target quantity is the True Evaluation Score, which "measures the performance of M on task" T over all generations, regardless of format satisfaction.[^c2] Because it needs an oracle extractor, it cannot be computed directly. The practical estimate, EstTrue, normalises SysE by FI_C. This "prevents skewing comparisons of how different formats affect the LLM due to F IC".[^c3] The estimator is consistent, and the paper gives a reliability condition: the estimate is trustworthy only when FI_C is high enough (a bound that depends on the confidence margin and the sample variance).[^c4]

## The bias metric and two criteria

Format bias of a model across k formats is the variance of its EstTrue scores over those formats. A lower variance means a less format-biased model. Since the variance is built from estimators, a mitigation must meet two criteria: "reducing BiasFo , indicating less formatFo -bias in M; (ii) Increase the format-following" scores of all formats, so the variance itself is reliable.[^c5] My inference: a method that lowers the variance by pushing every format's compliance toward zero would pass the first criterion and fail the second, which is why both are required.

## What was found

The evaluation covered four format families (multiple-choice answer styles, wrapping, lists, and others; 15 formats) on eight generation tasks. For the seven wrapping formats, Llama "exhibits the highest bias towards different formats" and ChatGPT the lowest.[^c6] Some format and model pairs were close to unusable: Gemma "follows instructions only" about 0 to 4% of the time on quoting and parenthesis wrapping, yielding near-zero performance.[^c7] Bias appeared on every task, and was lowest on the task the models already did well.

The authors' hypothesis for the cause is token bias: models assign different prior probability to different format-instruction tokens, "causing final predictions non-uniformly distributed across formats".[^c8]

## Mitigations tested

The test case was ChatGPT on MMLU with wrapping formats.

- Demonstrations raised the average FI score, from 72.99% to 79.19% with one and 85.31% with five.[^c9]
- Repeating the format instruction three times raised FI for most formats and lowered the variance metric. Placeholder was the exception, where repetition confused the model about where the placeholder was.[^c10]
- Fine-tuning on a small format-data mixture (6,500 samples, with formats sampled in inverse proportion to their zero-shot scores) brought the average FI score to "nearly perfect at 99.58%" and cut the variance metric from 235.33 to 0.71.[^c11] The authors read this as evidence for the token-bias account and say fine-tuning "largely eliminates format bias".[^c12]

## Limits

- The authors state that the metrics "are estimators, not exact measures", since the oracle extractor is infeasible at scale.[^c13] How well EstTrue tracks TrueE is argued by a consistency theorem, not shown against human-extracted ground truth in this text.
- Normalising by compliance assumes that compliant and non-compliant generations are equally hard. If models comply mainly on easy items, EstTrue is inflated. This is my inference; the paper does not test it.
- The variance metric weights all formats equally and is scale-dependent, so it is not comparable across tasks with different accuracy levels.
- Mitigation was run on one strong model (with a check on a second, smaller one), on one task and one format family. The token-bias cause is a hypothesis supported by the fine-tuning result, not isolated; architecture and training factors were not explored.
- Fine-tuning on MMLU-style formats may teach the formats of the test distribution rather than reduce a general bias.

## Related

- [[answer-format-dependent-bias-measurement]] — the same lesson for social-bias scores: the format is part of the instrument
- [[capacity-dependent-format-tax]] — format cost in accuracy, there driven by model capacity rather than compliance
- [[format-induced-answer-collapse]] — another way a format request changes the answer produced
- [[model-dependent-benchmark-difficulty]] — benchmark scores depend on the model and the protocol

[^c1]: doi-10-48550-arxiv-2408-08656 — "may not accurately reflect the actual performance"
[^c2]: doi-10-48550-arxiv-2408-08656 — "T rueE measures the performance of M on task"
[^c3]: doi-10-48550-arxiv-2408-08656 — "by F IC prevents skewing comparisons of how different formats affect the LLM due to F IC ."
[^c4]: doi-10-48550-arxiv-2408-08656 — "EstT rueE is consistent. Moreover, EstT rueE"
[^c5]: doi-10-48550-arxiv-2408-08656 — "reducing BiasFo , indicating less formatFo -bias in M; (ii) Increase the format-following"
[^c6]: doi-10-48550-arxiv-2408-08656 — "Llama exhibits the highest bias towards different formats"
[^c7]: doi-10-48550-arxiv-2408-08656 — "the Gemma follows instructions only"
[^c8]: doi-10-48550-arxiv-2408-08656 — "causing final predictions non-uniformly distributed across"
[^c9]: doi-10-48550-arxiv-2408-08656 — "(from 72.99% to 79.19% and 85.31%)"
[^c10]: doi-10-48550-arxiv-2408-08656 — "By repeating the wrapping instructions of ChatGPT"
[^c11]: doi-10-48550-arxiv-2408-08656 — "the average FI score across all formats is nearly perfect at 99.58%"
[^c12]: doi-10-48550-arxiv-2408-08656 — "finetuning largely eliminates format bias."
[^c13]: doi-10-48550-arxiv-2408-08656 — "are estimators, not exact measures"
