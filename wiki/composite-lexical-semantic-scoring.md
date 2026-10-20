---
description: "A QA score mixes a sentence-level embedding similarity with a keyword score (exact match plus best n-gram embedding match to gold); the keyword half alone fares better than the semantic half."
aliases: ["SMILE", "hybrid lexical-semantic QA metric", "keyword-plus-sentence QA score", "lexical exactness score"]
sources: ["arxiv-2511-17432"]
---
# Composite lexical-semantic answer scoring

A reference-based answer score can be built from two parts that measure different things and then be mixed by one weight. The semantic part compares the whole response with the reference by sentence embedding. The lexical part asks whether the short gold answer is really present in the response. It first checks exact string match, then loosens the check to the best embedding match between any n-gram of the response and the gold answer. The SMILE metric is built this way: it "combines sentence-level semantic understanding with keyword-level semantic understanding and easy keyword matching."[^c1] The two parts are combined with a user-set weight, which "allows practitioners to express their preferences."[^c2]

The lexical part has two terms. The first is a binary exact match, which the paper calls "a preliminary check for lexical answer correctness."[^c3] The second is the maximum over the response's n-grams of the embedding similarity to the gold answer. The paper gives the reason for it: string matching "may be too stringent for synonym-like answers," so the maximum n-gram similarity "serves as a continuous-valued measure of lexical exactness."[^c4] The equation is only partly legible in the extracted text, so I describe its two terms and not their coefficients (my reading).

The reason to keep both parts is an observed failure of the semantic part alone. An embedding of a whole response can score a relevant but wrong answer highly, which the paper's figure labels as embedding metrics that "often overrate relevant but wrong answers."[^c5] In the ablation, removing the keyword part "significantly reduces Pearson correlation, underscoring the critical role of lexical exactness in QA evaluation."[^c6] The keyword part alone is not a weak fallback: "The keyword subscores alone exhibited relatively strong performance, while the semantic subscore fared worse."[^c7]

The mechanism transfers beyond this embedding model in one respect. Swapping the small embedding model for a model "substantially larger" gave "only a marginal performance gain of less than 2%."[^c8] So the gain comes from the split into two terms, not from model size. The weight is forgiving: "SMILE hyperparameter choice is relatively forgiving, with any choice of w that slightly upweights the keyword subscore likely to perform well."[^c9]

What the split does not give is a judgment of the answer in its question. The lexical term checks a string against a gold token, and a gold token that is not a single short phrase breaks the design. The paper states the typical gold answer as "e.g., a single word or short phrase."[^c10] Where the gold is a sentence, the exact-match term and the maximum n-gram match both lose their meaning (my inference, not tested in the paper).

## Limits

- The human-labelled test set is small: "a 225-sample human annotated test set from nine (text, image, video) QA datasets."[^c11] The sections I read give no confidence interval for the correlations, so a difference of a few points between SMILE and GPT-4o is not shown to be stable.
- The metric is source-free. It sees the reference and the response, not the question or the image. "Source-free evaluation may represent an easier evaluation setting."[^c12] A response that is right by accident is scored the same as one that is right for the right reason (my inference).
- The study is limited to one kind of task: "our study focuses on factoid QA tasks."[^c13] Whether the composite holds for explanations or multi-part answers is not tested here.
- The weight w is a single hyperparameter chosen on this benchmark. The stability claim is for these datasets.

## Related

- [[style-matched-synthetic-reference]] — the other half of the same metric: the semantic term is computed against a reference rewritten to match the response style
- [[alias-tolerant-answer-matching]] — the synonym-tolerant match; the lexical term replaces its alias list with a continuous embedding similarity
- [[exact-match-verbosity-penalty]] — the binary exact-match rule that the lexical term keeps as its first check, and whose verbose-response failure the semantic term is meant to cover
- [[llm-judge-biases]] — the LLM-as-judge alternative against which the paper measures its correlations with human labels

[^c1]: arxiv-2511-17432 — "combines sentence-level semantic understanding with keyword-level semantic understanding and easy keyword matching"
[^c2]: arxiv-2511-17432 — "allows practitioners to express their preferences"
[^c3]: arxiv-2511-17432 — "The easy match sub-score EM serves as a preliminary check for lexical answer correctness."
[^c4]: arxiv-2511-17432 — "we loosen the necessity for string matches via the maximum n-gram embedding similarity score, which serves as a continuous-valued measure of lexical exactness"
[^c5]: arxiv-2511-17432 — "relevant but wrong answers"
[^c6]: arxiv-2511-17432 — "underscoring the critical role of lexical exactness in QA evaluation"
[^c7]: arxiv-2511-17432 — "subscores alone exhibited relatively strong performance, while the semantic subscore fared worse"
[^c8]: arxiv-2511-17432 — "resulted in only a marginal performance gain of less than 2%"
[^c9]: arxiv-2511-17432 — "SMILE hyperparameter choice is relatively forgiving"
[^c10]: arxiv-2511-17432 — "e.g., a single word or short phrase"
[^c11]: arxiv-2511-17432 — "a 225-sample human annotated test set from nine (text, image, video) QA datasets"
[^c12]: arxiv-2511-17432 — "Source-free evaluation may represent an easier evaluation setting"
[^c13]: arxiv-2511-17432 — "our study focuses on factoid QA tasks"
