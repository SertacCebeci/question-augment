---
description: "A small handcrafted test set covering span attributes exhaustively gives per-attribute recall that, reweighted by another dataset's attribute counts, predicts performance there (median r 0.85)."
aliases: ["attribute-covering test set", "diagnostic and predictive evaluation for sequence labeling", "BLAS methodology"]
sources: ["arxiv-2602-12759"]
---
# Attribute-stratified recall extrapolation

Standard evaluation reports one aggregate score on an in-distribution test set. That score says which system is better on average but not where to improve, and it does not anticipate behaviour on a different distribution. Álvarez-Mellado and Gonzalo propose instead to build the test set from the attributes of the target spans, not from whatever data is available.[^c1]

## Mechanism

1. Choose the span attributes that make retrieval easier or harder (shape, length, casing, sentence position, context cues).
2. Handcraft a small set of examples that covers the attribute combinations exhaustively. Real scraped text cannot do this when the phenomenon is sparse; the authors say anglicisms are only 1%-2% of the language. The instrument is a test set built "do not rely on gathering large amounts of real-world in-distribution scraped data, but consists in handcrafting a".[^c2]
3. Score each attribute combination separately, so a result is "ascribable to concrete" attributes. A failure can then be read as: would the model have succeeded with a more obvious context, or on a more prototypical span?[^c3]
4. To predict another dataset, count its spans per attribute type and multiply by the recall the model got on that type. Their example: 20 external spans of one type, recall 90 on that type, gives 18 expected hits and 2 misses.[^c4]

## What was measured

Six models (CRF, BETO, mBERT, two BiLSTMs, Llama3) were run on five external Spanish anglicism datasets (COALAS dev/test, CALCS dev/test A/B), which differ from the benchmark in their attribute distribution. The extrapolation predicted both recall and system ranking, with median Pearson correlation 0.85 on recall.[^c5]

The result is diagnostic (it names weak attributes), actionable (it indicates which model fits a scenario) and predictive in the sense above.[^c6]

My reading, not the paper's: the method is a stratified estimator. It works to the extent that per-attribute recall is stable across datasets and the attribute list captures what varies between them. That is why the distribution shift is carried by the counts rather than by the model scores.

## Limits

- Tested on one task (anglicism identification in Spanish journalistic text) and one benchmark; the span-identification scope is stated, and transfer to NER or other tasks is claimed but not measured here.
- Only recall was predicted directly; ranking by F1 is reported as correlated, and precision is not extrapolated this way.
- Attributes must be chosen by someone who already knows the phenomenon; missing attributes are invisible to the method.
- Prediction needs the external dataset's attribute counts, i.e. annotated spans with attributes.
- All external sets share genre with the benchmark, so cross-genre prediction is untested.

## Related

- [[attribute-exploration]] — enumerating attribute combinations systematically to cover a domain
- [[d2d-attribute-informativeness-score]] — scoring which attributes carry information about outcomes
- [[benchmark-contamination-convergent-audit]] — another critique of what a single benchmark score hides

[^c1]: arxiv-2602-12759 — "We propose an evaluation methodology for sequence labeling tasks grounded in error"
[^c2]: arxiv-2602-12759 — "do not rely on gathering large amounts of real-world in-distribution scraped data, but consists in handcrafting a"
[^c3]: arxiv-2602-12759 — "producing a result that is ascribable to concrete"
[^c4]: arxiv-2602-12759 — "spans that would be successfully retrieved by simply extrapolating from the recall results obtained"
[^c5]: arxiv-2602-12759 — "predicts both recall values (with a median Pearson"
[^c6]: arxiv-2602-12759 — "better suited for a given scenario) and predictive: our method predicts model performance on external datasets with"
