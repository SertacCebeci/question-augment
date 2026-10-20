---
description: "A small open model learns to rewrite a black-box LLM's reasoning by contrasting correct and incorrect reasonings; pair selection alone did not help."
aliases: ["learned correction of black-box reasoning", "black-box adaptation by contrastive likelihood", "CoBB-style reasoning corrector"]
sources: ["doi-10-48550-arxiv-2406-18695"]
---
# Contrastive reasoning correction

A black-box LLM returns an output without exposing its token probabilities.[^c1] A second, smaller open model can still be trained to take that output, together with the question, and produce a better reasoning. The training material comes from the black-box model itself. For each question, several chain-of-thought reasonings are sampled and each is labelled correct or incorrect against a ground-truth answer.[^c2] The corrector is then a seq2seq model: it maps an imperfect reasoning to a correct one.

What makes the corrector learn from errors, and not only imitate correct text, is the objective. Plain supervised training raises the likelihood of the correct reasoning and nothing else. The paper's training adds a term over pairs: the correct reasoning is treated as preferred and the incorrect one as dispreferred, using odds-ratio preference optimization, which "enables single-stage learning from pair-wise preference data, without the reference models" in the sense that no frozen reference model is needed.[^c3] The corrector is "trained by contrasting the likelihoods of positive and negative reasonings."[^c4]

The contrast is not decorative. In the paper's ablation, supervised training on the positive reasoning alone let the likelihood of the negative reasoning rise above its starting value: "even increased compared to the initial stage, when" only the cross-entropy term was used. Adding the contrastive term resolved this.[^c5] The same ablation found that the proposed subsampling of training pairs was not effective without the contrast: "dataset construction is not effective without the" contrastive objective, while with it, more representative pairs gave further gains.[^c6]

The pair selection is a separate mechanism. For each question the possible pairs of correct and incorrect reasonings grow as the product of the two set sizes. The method chooses a subset whose distribution of likelihood differences matches the full set, measured by a 2-Wasserstein-type distance over means and variances, and searches for it with a genetic algorithm.[^c7] The authors note the selection problem is NP-hard, which is why a search heuristic is used.[^c8]

Reported effect: averaged over four QA benchmarks, the adapted reasoning of gpt-3.5-turbo improved on the original by 6.2% in accuracy, and by 2.2% over the best earlier adaptation baseline.[^c9] The corrector also transferred: a model trained against gpt-3.5-turbo improved the reasonings of other black-box and open-source models.[^c10] The cost comparison is with BBox-Adapter, which verifies candidates through sampling and beam search; the paper's corrector directly learns the seq2seq mapping, and it reports about 20% of the baseline's training cost and about 7% of its test-time inference cost.[^c11]

For the question-and-answer side, the relevant point is the shape of the correction: the answerer does not get a better prompt or a second sample. It gets a learned map from its own wrong reasonings to right ones, and the signal that teaches the map is the contrast between the two kinds.

## Limits

- The label is the bottleneck: the method needs ground-truth correctness for every training question, and the paper names this as a cost for large datasets.[^c12]
- The quality of the corrector depends on the initial open model and on the sampled reasonings. The authors say the initial reasonings may be biased or insufficiently diverse, and that the framework's effect depends on which open model initializes the corrector.[^c13]
- Transfer across target models is not uniform: "may vary based on the specific characteristics and" the pre-training knowledge of the target model.[^c14]
- The gain shrinks when the target is already strong. The paper reports that the average accuracy on GSM8K "is slightly decreased when the target LLM already exhibits a stronger performance."[^c15]
- The ablation uses a single target model, gpt-3.5-turbo, and the choice of the Wasserstein-type distance over KL divergence is an empirical observation, not a derivation.[^c16]
- All tasks are QA reasoning benchmarks with short gold answers. Whether the contrast carries over to open-ended answers, where correctness is not a label, is not tested here. This is my inference from the setup, not a claim of the paper.

## Related

- [[knowledge-distillation]] — also trains a student against a teacher's output; here the teacher is only sampled and labelled, and the contrast term pushes the corrector away from wrong reasonings rather than matching a soft distribution.
- [[execution-verified-preference-pairs]] — also forms preference pairs by checking sampled outputs against a gold result; there the pairs train the sampler's own policy, here they train a separate corrector for another model's output.
- [[reflection-token-error-injection]] — another way to teach a model to revise a wrong output; there the errors are injected at pretraining, here they are observed from a black-box model.

[^c1]: doi-10-48550-arxiv-2406-18695 — "without access to detailed information such as output token probabilities."
[^c2]: doi-10-48550-arxiv-2406-18695 — "label their correctness using ground-truth human"
[^c3]: doi-10-48550-arxiv-2406-18695 — "Odds Ratio Preference Optimization (ORPO) (Hong et al.,"
[^c4]: doi-10-48550-arxiv-2406-18695 — "adaptation model is trained by contrasting the likelihoods of positive and negative reasonings."
[^c5]: doi-10-48550-arxiv-2406-18695 — "even increased compared to the initial stage, when"
[^c6]: doi-10-48550-arxiv-2406-18695 — "dataset construction is not effective without the"
[^c7]: doi-10-48550-arxiv-2406-18695 — "that this 2-Wasserstein distance is better than other"
[^c8]: doi-10-48550-arxiv-2406-18695 — "as this selection of representative samples problem is NP-hard"
[^c9]: doi-10-48550-arxiv-2406-18695 — "accuracy improvements of 6.2% and 2.2%, compared to the original black-box gpt-3.5-turbo"
[^c10]: doi-10-48550-arxiv-2406-18695 — "could generalize to adapt other LLMs, including"
[^c11]: doi-10-48550-arxiv-2406-18695 — "while BBox-Adapter learns to verify through the"
[^c12]: doi-10-48550-arxiv-2406-18695 — "labels to judge the correctness of reasonings, which"
[^c13]: doi-10-48550-arxiv-2406-18695 — "on the quality of the training pairs and the capability of the initial open-source LLM."
[^c14]: doi-10-48550-arxiv-2406-18695 — "may vary based on the specific characteristics and"
[^c15]: doi-10-48550-arxiv-2406-18695 — "average accuracy on GSM8K is slightly decreased when the target LLM already exhibits a stronger performance"
[^c16]: doi-10-48550-arxiv-2406-18695 — "We empirically observe that this 2-Wasserstein distance is better than other possible metrics such as KL divergence."
