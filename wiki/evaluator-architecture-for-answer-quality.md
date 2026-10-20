---
description: "A bi-encoder similarity scorer tracked token F1 and GPT judgments of small-LLM outputs while two cross-encoders scored near zero or below, making evaluator architecture a design choice."
aliases: ["evaluator architecture choice", "bi-encoder vs cross-encoder evaluator", "learned quality metric selection"]
sources: ["arxiv-2512-16317"]
---
# Evaluator architecture for answer quality

A learned model that scores an answer against a reference can be built in more than one way, and the paper compares two families. A cross-encoder reads the reference and the candidate together, and its scorers in this paper were "trained on relevance and textual entailment data".[^c1] A bi-encoder encodes each text separately and compares them by similarity: "Reference and candidate sentences are encoded with the STS model, cosine similarity".[^c2] The paper's scorer of this kind was trained "on the STS Benchmark and related semantic similarity corpora".[^c3]

The measurement is a Pearson correlation between each evaluator's scores and two reference signals, token-level F1 against ground-truth answers and GPT-based judgments, averaged over question answering and summarization.[^c4] The bi-encoder's scores reach about 0.66 correlation with truth F1, and 0.29 with GPT scores.[^c5][^c15] The two cross-encoders "show correlations close to zero or even negative."[^c6] The worse of them, CE–MiniLM, "exhibits moderately negative correlations of about −0.24 and −0.17" with F1 and GPT scores respectively.[^c7]

The paper draws the design conclusion directly. "These results indicate that not all learned quality metrics are equally suitable" as evaluators, and "the cross encoders fail to provide stable quality signals for the LLM outputs" studied.[^c8] The bi-encoder "yields more consistent rankings across tasks and reference types".[^c9] The abstract states the same point as "a critical design choice for PoQ".[^c10] The cross-encoders are kept only "as diversity sources" in multi-evaluator configurations.[^c11]

Why the bi-encoder would track quality better is not tested in the paper. My inference is that a similarity objective trained on graded overlap is closer to what a quality score measures than a relevance or entailment label is. Token F1 is itself an overlap with a reference, so part of the agreement may be built in on both sides. That reading is mine, not the paper's.

## Limits

- Three evaluators. The architecture comparison confounds architecture with training objective: the bi-encoder is also the only one trained on similarity data, so the result does not separate the two.
- Averaged correlations. The values are "averaged over question answering and summarization tasks", and the text read does not give per-task numbers.[^c12]
- Weak reference signals. The "objective" reference is token F1, and the subjective one is GPT-4 used "as a proxy for human judgment".[^c13] No human judgments are involved.
- Modest agreement with GPT. A correlation of 0.29 explains under a tenth of the variance. The paper's phrase that similarity "captures much of the variance in both objective and subjective quality assessments" is generous on the GPT side.[^c14]
- Narrow output pool. The outputs came from five small models, 1.1 to 3.2 billion parameters. Whether the ranking holds for stronger models or other tasks is untested.
- Correlation is not a decision rule. The paper shows which evaluator tracks the references, not how much a reward should depend on it.

## Related

- [[quality-consensus-verification]] — the protocol whose quality term rests on this choice
- [[interaction-vs-encoding-bias]] — the bi-encoder versus query-document interaction split, in retrieval rather than output scoring
- [[llm-judge-biases]] — the GPT-judge reference this paper treats as a stand-in for human judgment

[^c1]: arxiv-2512-16317 — "Despite being trained on relevance and textual entailment"
[^c2]: arxiv-2512-16317 — "Reference and candidate sentences are encoded with the STS model, cosine similarity"
[^c3]: arxiv-2512-16317 — "on the STS Benchmark and related semantic similarity corpora"
[^c4]: arxiv-2512-16317 — "summarizes the Pearson correlation between scores from the three"
[^c5]: arxiv-2512-16317 — "Its scores reach approximately 0.66 correlation with ground"
[^c6]: arxiv-2512-16317 — "show correlations close to zero or even negative."
[^c7]: arxiv-2512-16317 — "exhibits moderately negative correlations of about −0.24 and −0.17"
[^c15]: arxiv-2512-16317 — "truth F1 and 0.29 correlation with GPT scores"
[^c8]: arxiv-2512-16317 — "These results indicate that not all learned quality metrics are equally suitable"
[^c9]: arxiv-2512-16317 — "consistent rankings across tasks and reference types"
[^c10]: arxiv-2512-16317 — "a critical design choice for PoQ"
[^c11]: arxiv-2512-16317 — "cross encoders serving mainly as diversity sources"
[^c12]: arxiv-2512-16317 — "averaged over question answering and summarization tasks."
[^c13]: arxiv-2512-16317 — "using GPT-4 as a proxy for human judgment"
[^c14]: arxiv-2512-16317 — "captures much of the variance in both objective and subjective quality assessments"
