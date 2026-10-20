---
description: "Attention regularisation trains a classifier to align its attention with human rationale masks as an auxiliary loss; its gain over the baseline depends on task and model."
aliases: ["attention regularisation", "attention regularization", "learning from rationales via attention", "rationale-regularised attention"]
sources: ["arxiv-2511-16353"]
---
# Attention regularisation from rationales

Attention regularisation is a way of putting human rationales into training without putting them into the input at test time. The classifier computes its usual task loss and a second term that optimises the attention weights toward a given rationale mask, often produced by feature attribution.[^a1] In the paper's form, the mask is binary: 1 for rationale tokens, 0 otherwise.[^a2] The regularised model is then optimised with a second loss term, a binary cross-entropy between the mask and the attention weights of the last layer.[^a3] The authors confine the experiment to the last layer because it is closest to the final prediction.[^a4]

The model is fine-tuned on "inputs that are rationalised during training only."[^a5] The learnability metric is a ratio: AR is the F1 of the regularised model R over the F1 of a baseline model M, both evaluated on the non-rationalised test set.[^a6] AR above one means that the rationale signal improved the baseline. The paper frames the two possible failure causes in its own terms: if regularisation does not help, the rationale may be redundant, since the model already relies on similar cues, or detrimental, since it steers the model away from dataset-specific shortcuts that had boosted the original results.[^a7]

The mechanism is the same across tasks, but its effect is not. Over 14 task settings, regularisation had a three-run average positive effect in 6 for BERT, 7 for Pythia, 8 for ModernBERT and 6 for GPT-Neo.[^a8] Bootstrap intervals were used to check consistency: lower bounds indicated consistent improvement in 83% of cases for BERT, but "for the other three models: 43%, 25% and 0%."[^a9] The authors conclude that "Regularisation is task- and model-dependent."[^a10] Regularisation also did not stabilise predictions across random seeds.[^a11]

The one clear positive is cross-domain argument mining. Only BERT benefits on both the in-domain and cross-domain settings, and the cross-domain gain is substantially larger.[^a12] The paper reads this as the auxiliary loss closing the gap between in- and cross-domain performance for BERT, which is the sense in which the authors call attention regularisation potential.[^a13] Earlier work reported in the same paper found that "attention regularisation outperforms the multi-task learning approach," in which a token classifier is trained jointly with the main classifier.[^a14]

## Limits

The evidence rests on three runs per model-task setup, and the authors say the intervals "must be interpreted with caution": "Given the small sample size of 3 runs per" setup.[^a15] Only the last layer's attention was regularised. For GPT-Neo, where no setting improved consistently, the authors explain the result by "relatively low AR overall, peaking at 1.04."[^a16] Hyperparameters were default, with only slight adaptations, so tuned models could behave differently.[^a17] The cross-domain gain is reported for one task and one model, BERT; the authors do not claim it transfers to others. Whether attention matching is the right target for an explanation at all is not tested here.

## Related

- [[contextual-impact-of-rationale]] — the sufficiency score the paper relates to AR; the two are measured on the same rationales and the paper finds only weak links between them.
- [[rationale-token-learnability]] — the other paradigm in the same work, which uses the same masks as token labels rather than as a loss on attention.

[^a1]: arxiv-2511-16353 — "a second term optimising the attention weights to a given input rationale mask"
[^a2]: arxiv-2511-16353 — "a binary rationale mask a (1 for important tokens, else 0)"
[^a3]: arxiv-2511-16353 — "then optimised with a second loss term"
[^a4]: arxiv-2511-16353 — "our experiments to the attention values of the last"
[^a5]: arxiv-2511-16353 — "inputs that are rationalised during training only"
[^a6]: arxiv-2511-16353 — "on the non-rationalised test set"
[^a7]: arxiv-2511-16353 — "redundant (the model would already rely on similar cues) or detrimental"
[^a8]: arxiv-2511-16353 — "has a three-run-average positive effect in 6/14 tasks for BERT"
[^a9]: arxiv-2511-16353 — "for the other three models: 43%, 25% and 0%"
[^a10]: arxiv-2511-16353 — "Regularisation is task- and model-dependent"
[^a11]: arxiv-2511-16353 — "regularisation does not guarantee a greater stability"
[^a12]: arxiv-2511-16353 — "only BERT benefits from attention regularisation on both settings"
[^a13]: arxiv-2511-16353 — "closes the gap between in- and crossdomain argument mining performance for BERT"
[^a14]: arxiv-2511-16353 — "attention regularisation outperforms the multi-task learning approach"
[^a15]: arxiv-2511-16353 — "Given the small sample size of 3 runs per"
[^a16]: arxiv-2511-16353 — "relatively low AR overall, peaking at 1.04"
[^a17]: arxiv-2511-16353 — "default hyperparameters were used with only slight adaptations"
