---
description: "A query performance predictor's correlation with measured retrieval effectiveness depends on the collection, the retrieval system and the correlation measure, so no single predictor wins everywhere."
aliases: ["predictor robustness across collections", "QPP generalization across scenarios", "cross-collection robustness of performance predictors"]
sources: ["doi-10-48550-arxiv-2302-10126"]
---
# Predictor generalization across scenarios

A query performance predictor is judged by how well its output tracks the measured effectiveness of the queries it is run on. That correlation is a property of a whole setting, not of the predictor alone. The setting has at least three parts: the collection the queries are run against, the retrieval system that produces the ranked list, and the statistic used to compare predicted with measured performance. Changing any one of them can change which predictor looks best.

The image benchmark shows the retrieval system mattering. The score-variance baseline "seems to be a suitable estimator for the system" of Revaud et al., but for the system of Radenović et al. "the predictions given by score variance for the system of Radenović et al. [50] are close to random."[^c1][^c2] The same kind of predictor, computed over the lists of two retrieval systems, carries a signal for one and none for the other. The text does not explain why. My guess is that the score scale differs between the two models, but that was not checked.

The collection matters too. On PASCAL VOC 2012 and Caltech-101 the authors report that "the two data sets have distinct top scoring pre-retrieval predictors," and conclude that "demonstrating that it is not sufficient to use a single data set to find" generic predictors.[^c3][^c4] A predictor that leads on one collection need not lead on the next.

The correlation measure matters as well. On PASCAL VOC, "image difficulty gives a better Pearson correlation," while the objects-per-area baseline gives the better Kendall value. The authors draw the lesson that "multiple correlation measures to better assess predictors’ behavior" are needed.[^c5][^c6]

None of this is new for text. The paper reports that Hauff et al. analysed 22 pre-retrieval predictors and found that "the performance of predictors depends on the test collection and the underlying retrieval model."[^c7] It also notes that individual predictors "are not robust across collections."[^c8] What the image benchmark adds is a second modality in which the same pattern holds. The authors' summary is that "most predictors do not generalize across evaluation scenarios."[^c9] Their conclusion for the field is that "it is difficult to find a single predictor that is consistently better over all scenarios."[^c10]

## Limits

- The evidence is four collections, two retrieval systems and two correlation measures. The authors say they intend to widen the pool, "expanding the pool of data sets and retrieval methods."[^c11] Until then, the claim is about this pool.
- The two landmark collections have few queries: the established ROxford5k and RParis6k sets "consist of 70 queries each."[^c12] A correlation over 70 queries carries wide uncertainty, and the rankings above are read from single cells.
- The result is about ranking across scenarios. It does not show that a predictor is useless in general; some predictors were significantly better than chance in some cells, as the paper's own significance marking shows.
- No mechanism is tested. Why a statistic tracks one system and not another is my inference, not a finding of the paper.
- The phenomenon was already reported for text retrieval. The image result confirms it in a new modality; it does not discover it.

## Related

- [[query-performance-prediction]] — the setting whose predictors are compared across scenarios here.
- [[saturated-performance-measure]] — the effectiveness measure chosen as the target is a further axis: under a ceiling, P@10 and P@100 can rank the same predictors differently.

[^c1]: doi-10-48550-arxiv-2302-10126 — "the predictions given by score variance for the system of Radenović et al. [50] are close to random"
[^c2]: doi-10-48550-arxiv-2302-10126 — "seems to be a suitable estimator for the system"
[^c3]: doi-10-48550-arxiv-2302-10126 — "the two data sets have distinct top scoring pre-retrieval predictors,"
[^c4]: doi-10-48550-arxiv-2302-10126 — "demonstrating that it is not sufficient to use a single data set to find"
[^c5]: doi-10-48550-arxiv-2302-10126 — "image difficulty gives a better Pearson correlation,"
[^c6]: doi-10-48550-arxiv-2302-10126 — "multiple correlation measures to better assess predictors’ behavior."
[^c7]: doi-10-48550-arxiv-2302-10126 — "They also observed that the performance of predictors depends on the test collection and the underlying retrieval model."
[^c8]: doi-10-48550-arxiv-2302-10126 — "are not robust across collections."
[^c9]: doi-10-48550-arxiv-2302-10126 — "most predictors do not generalize across evaluation scenarios."
[^c10]: doi-10-48550-arxiv-2302-10126 — "difficult to find a single predictor that is consistently better over all"
[^c11]: doi-10-48550-arxiv-2302-10126 — "expanding the pool of data sets and retrieval methods."
[^c12]: doi-10-48550-arxiv-2302-10126 — "consist of 70 queries each."
