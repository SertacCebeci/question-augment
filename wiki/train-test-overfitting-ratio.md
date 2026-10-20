---
description: "A log ratio of training to held-out error, plus a fold-spread term, flags overfitting that one mean test score hides; the paper defines it but does not test it."
aliases: ["Logarithmic Overfitting Ratio", "LOR", "Composite Overfitting Ratio", "COS", "train-test error ratio", "overfitting score"]
sources: ["arxiv-2511-21354"]
---
# Train-test overfitting ratio

A model's error on the data it was fit to is compared with its error on held-out data, and the comparison is written as a log ratio. Michelucci and Venturini define the Logarithmic Overfitting Ratio as LOR = log(MAE_train / MAE_test), with MAE as the example metric.[^c1] Its sign carries the reading: zero means the two errors match, a negative value means the training error is the smaller and the model overfits, and a positive value means underfitting.[^c2] The authors then tell the reader to pick the model whose LOR is closest to zero, so the ratio works as a ranking aid across the model instances in a results table.[^c4]

The ratio sees only averages, and the authors' argument is that the averages can agree while the folds do not. "Overfitting rears its ugly head in subtle ways." Two models can have similar mean train and test errors while the spread of their fold scores differs. In overfitting regimes the test-fold standard deviation is expected to be much larger than the training one.[^c3] The Composite Overfitting Ratio (COS) adds that spread to the LOR: it combines the train and test errors, each divided by its standard deviation across folds, with weights α and β.[^c5] The authors suggest α = β = 1/2. They read COS = 1 as train and test errors that match with stable variance across folds, COS > 1 as overfitting with fold-to-fold instability, and COS < 1 as underfitting.[^c6]

The practical reading is that a model is not judged by one test score. A large train/test gap is a warning, and the paper says such a gap can mean either "data leakage or model variance," so the ratio does not say which.[^c7]

## Limits

- Nothing here is measured. The paper gives definitions, one example table with two rows, and a figure of a real project's table. It does not show that LOR or COS separates good generalization from bad across tasks. The choice of α = β = 1/2 is a suggestion: "I suggest you use" it, and the text says the weights "can, in principle, be freely chosen."[^c5]
- The COS formula, as extracted from the PDF, does not reproduce the paper's own numbers. This is my inference from the text. The example row reads "max = 1 3.4 ± 0.2 3.0 ± 0.3 0.054 0.9," i.e. train MAE 3.4 ± 0.2, test MAE 3.0 ± 0.3, LOR 0.054, COS 0.9.[^c8] The LOR figure matches log base 10 of 3.4/3.0 (about 0.054), but the COS formula with α = β = 1/2 gives about ½(3.4/0.2 + 3.0/0.3) ≈ 13.5, far from 0.9. Either the formula is garbled in the extraction or it uses a normalization the text does not state. The interpretation "COS = 1 means optimal" depends on that normalization, so it is not established by the text as read.
- The log is undefined when either error is zero, and it grows without bound as the training error approaches zero. The text does not discuss this. My inference: a very flexible model that nearly memorizes its training set will get a large negative LOR, and the ratio gives no separate signal for that case.
- Examples use MAE only. The text says the ratio "can also be defined with the MSE," but no MSE case is shown.
- The ratio is defined for cross-validation with fold or split statistics. It says nothing about whether the held-out set is itself a fair test of the question being asked.

## Related

- [[run-to-run-spread]] — spread across repeated runs of one system; COS uses spread across the folds of one protocol, a different source of variation that a single score also hides
- [[question-matched-split]] — which held-out set the test error comes from; a train/test ratio is only as informative as that split
- [[minimum-detectable-effect]] — the resolution needed before a small difference in LOR between two models counts as a difference

[^c1]: arxiv-2511-21354 — "The Logarithimic Overfitting Ratio (LOR) is defined by"
[^c2]: arxiv-2511-21354 — "LOR < 0: Overfitting is present."
[^c3]: arxiv-2511-21354 — "Typically, in overfitting regimes, we observe"
[^c4]: arxiv-2511-21354 — "You should choose the model with the LOR value closest to zero."
[^c5]: arxiv-2511-21354 — "The value of α and β can, in principle, be freely chosen"
[^c6]: arxiv-2511-21354 — "Train and test errors match, and the variance"
[^c7]: arxiv-2511-21354 — "indicate data leakage or model variance"
[^c8]: arxiv-2511-21354 — "max = 1 3.4 ± 0.2 3.0 ± 0.3 0.054 0.9"
