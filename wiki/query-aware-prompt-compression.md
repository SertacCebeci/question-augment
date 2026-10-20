---
description: "Compressing a prompt for a black-box LLM may or may not see the query; seeing it lowers the achievable distortion at a given rate, and varying the rate across queries never does worse."
aliases: ["query-aware compression", "query-conditioned prompt compression"]
sources: ["doi-10-48550-arxiv-2407-15504"]
---
# Query-aware prompt compression

A prompt compressor turns an input X into a shorter prompt M, which a black-box LLM then answers from together with the query Q. The compressor is **query-agnostic** when it sees X alone, and **query-aware** when it also sees Q, so it can keep what that query needs and drop the rest.[^c1] The paper scores both on the same two axes. Rate is the compressed length over the original, measured "to measure how much the prompt is compressed."[^c2] Distortion is the loss of the LLM's prediction, and the experiments are computed with "the log loss (left) and 0/1 loss (right) distortion metrics."[^c3]

The mechanism is that the query names the part of the prompt that bears on the answer. A token can be redundant for one question and essential for another, and only a compressor that sees the question can tell them apart. The synthetic experiments show the effect on the distortion-rate curves: "conditioning on the query allows for a significant improvement," seen in the query-aware QuerySelect against the query-agnostic LLMLingua-2.[^c4]

The sharper result concerns how rate is spent. One can fix the rate for each query, or fix only its average over queries. The paper's Remark 1 says the second allows more: "only the average rate over the queries is required to be R." The compressor can then give hard queries, those with high distortion, more tokens and easy ones fewer.[^c5] The paper states that "but we always have" the averaged distortion-rate function no larger than the per-query average. In its setup that is a proved inequality, not a measured one.[^c6] The method built on this idea, Adaptive QuerySelect, is a query-aware, variable-rate adaptation of LLMLingua-2. On the synthetic dataset it "is the only method to outperform the optimal query-agnostic strategy."[^c7]

The optimum itself is a linear program in the compressor's conditional probabilities, and the paper computes it through the dual: "the dual of the linear program can be" solved efficiently.[^c9]

## Limits

- The exact optimum is computed only on "a synthetic dataset consisting of prompts generated from a Markov chain," with binary prompts.[^c10] For the natural-language setup the paper says "the dimension of the linear program is too large," and it reports only search results, "our beam search upper bounds."[^c8][^c11] Those are bounds from a search, not the optimal curve.
- On NarrativeQA the paper finds that "the gap between existing methods and the query-aware case is quite large," even for methods that use the query.[^c12] That is a gap to a bound, measured on one dataset.
- Rate here is a token-length ratio. It is not an entropy or a count of bits, so the operational meaning of Shannon's rate does not carry over whole (see [[rate-distortion-theory]]).
- The comparisons assume one fixed black-box predictor and the two losses named above.[^c3] Whether a ranking of methods survives another judge is not tested here (my inference).
- The optimum needs the joint distribution of prompts, queries and answers. A deployed compressor would have to estimate the query distribution, and the paper does not measure how well such an estimate performs (my inference).
- The paper itself says "it is important to exhaustively study our proposed method on natural language datasets."[^c13] The natural-language evidence is small, and the claim that the variable-rate method beats the query-agnostic optimum is shown only on the synthetic data.

## Related

- [[rate-distortion-theory]] — the frame; the paper's distortion-rate function is its inverse, with rate as the free variable.
- [[query-relative-token-overflow]] — the same per-query question asked of a detector: whether one compressed token still serves a question. This paper asks it as an optimum over compressors.
- [[information-rate-per-token]] — a different rate, bits of mutual information per output token; the two are not interchangeable.
- [[structure-then-select-compression]] — query-conditioned selection inside context compression.
- [[information-bottleneck]] — the general framing of compression as keeping what bears on a target.

[^c1]: doi-10-48550-arxiv-2407-15504 — "the compressor also has access to the query"
[^c2]: doi-10-48550-arxiv-2407-15504 — "to measure how much the prompt is compressed"
[^c3]: doi-10-48550-arxiv-2407-15504 — "are computed with the log loss (left) and 0/1 loss (right) distortion metrics"
[^c4]: doi-10-48550-arxiv-2407-15504 — "conditioning on the query allows for a significant improvement"
[^c5]: doi-10-48550-arxiv-2407-15504 — "only the average rate over the queries is required to be R"
[^c6]: doi-10-48550-arxiv-2407-15504 — "but we always have"
[^c7]: doi-10-48550-arxiv-2407-15504 — "is the only method to outperform the optimal query-agnostic strategy"
[^c8]: doi-10-48550-arxiv-2407-15504 — "dimension of the linear program is too large"
[^c9]: doi-10-48550-arxiv-2407-15504 — "the dual of the linear program can be"
[^c10]: doi-10-48550-arxiv-2407-15504 — "a synthetic dataset consisting of prompts generated from a Markov chain"
[^c11]: doi-10-48550-arxiv-2407-15504 — "our beam search upper bounds"
[^c12]: doi-10-48550-arxiv-2407-15504 — "the gap between existing methods and the query-aware case is quite large"
[^c13]: doi-10-48550-arxiv-2407-15504 — "it is important to exhaustively study our proposed method on natural language datasets"
