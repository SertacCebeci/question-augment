---
description: "A model scores well in training by keying on a cue correlated with the label; the Clever Hans effect is that reliance, which fails once the correlation breaks at test time."
aliases: ["shortcut learning", "spurious correlation reliance", "Clever Hans behavior", "background bias"]
sources: ["doi-10-3389-frai-2025-1692454", "arxiv-2512-21711", "arxiv-2512-20924", "arxiv-2512-17953", "arxiv-2512-05937", "arxiv-2511-22787"]
---
# Clever Hans effect

A model can score well on its training data by keying on a cue that happens to predict the label there, rather than on the feature the task is about. The review that frames this effect takes the name from a horse that seemed to do arithmetic: psychologist Oskar Pfungst found Hans "responding to subtle, unintentional cues from his handler" rather than solving the problems.[^c1] The analogy carries a mechanism, and the review gives it a minimal form. If a spurious feature z, a part of the input x, correlates with the label y in the training distribution, then "the model may minimize the loss by learning" a function of z, not of the causal features.[^c2] The fit on training data is real, but it is borrowed from the cue. When the test distribution breaks the cue-label correlation, the same function degrades, and the review reads the cost as a gap between test and training performance.[^c3]

The effect is a relation between three things, not a property of a model alone: the model, a cue, and a shift. A model that uses the cue cannot be told apart from one that uses the intended feature for as long as the cue stays correlated with the label. That is why accuracy on a held-out split drawn from the same source does not settle the question. The review lists several contributors, among them data artifacts that serve as shortcuts, absence of causal supervision, imbalanced data with hidden confounders, insufficient evaluation pipelines, and lack of robust interpretability tools.[^c4] The evaluation point is the one that makes the effect hard to see. Evaluation on splits that "preserve the same biases across training and testing sets, thereby masking shortcut reliance" cannot separate the cue from the feature, because both sets carry the same cue.[^c5] Explanation methods can hide it as well, since they "often produce plausible but misleading attributions."[^c6] The review states that the effect "goes undetected by standard validation methods."[^c7]

The examples span domains. Vision models "may learn background textures" correlated with object class rather than the objects themselves.[^c8] Language models show the same structure: "large language models (LLMs) display shortcut behavior by mimicking prompt formats and token distributions."[^c9] The review also uses "also referred to as spurious correlations and shortcut learning" for the same phenomenon, so the three names are treated here as one concept.[^c10]

What the concept changes is the question asked of a benchmark score. "Does the model do the task?" has no answer from a high score alone, because the score is equally produced by the cue. The sharper question is which cue the answer tracks, and on which shift that cue stops predicting the label. The review's claim is that models "may perform well on in-house data but often fail to bridge the gaps when the model encounters real-world variations and distribution shifts in data."[^c3]

What survives the move from the horse is the inference structure: a cue correlated with the answer where it was observed, and absent where the answer is needed. What does not survive is the agency. Hans had a human handler whose cues were unintentional but produced in a live exchange; a dataset has no communicator, so its cue is a statistical byproduct of how it was collected (my inference, not the review's claim).

A measured case, unlike the review's survey, comes from training a latent-reasoning model. Zhang et al. fine-tune COCONUT on data where the answer distribution is biased, and report that the shortcut reliance the review describes appears. With about 75% of correct MMLU answers set to option C, the share of wrong predictions that choose C rises to about 70%, against roughly 30% for the original model.[^c15] On HotpotQA, with shortcuts injected into the context, a model trained with shortcuts scores near 100% when the shortcut favours the correct answer, about 13% on the original set, and near 0% when it favours a wrong one.[^c16] The authors read the pattern as heavy reliance on the cue rather than reasoning.[^c17] This is an experiment on one model family, so it shows the effect appearing under this training, not how often it appears in practice (see [[latent-token-causal-insensitivity]]).

A measured case in video action recognition uses the name background bias. Models "rely on background cues rather than human movement and pose to make predictions, a behavior known as background bias".[^c18] The test places "the human from class A" on a mismatched scene, and the errors that land on the scene's class count as reliance on the background.[^c19] The paper reports that "all models display background bias", across classifiers, CLIP and SigLIP2, and video language models.[^c20] The bias is highest "when backgrounds are distinctive and consistently paired with actions".[^c21] Adding parameters does not remove it, "larger model capacity alone is insufficient for robust action understanding", while more frames help: temporal input "helps the model focus more on the human motion than the background context".[^c22][^c23] The mitigation shows the cue is also informative in ordinary data. Removing the background lowers the swap error but costs accuracy where the two are correlated, since "useful context is lost".[^c24] That is the case where a correlate is both shortcut and signal; see [[dual-use-context-cue]].

A still-image case with a cultural cue comes from [[culture-mixing]]. In a synthetic food benchmark, adding a background that carries a second culture's cues moved a food's country answer far more than adding a second food did. The retention figures are reported as "SFB yields lower retention (20-40%)" against higher retention when a second food was added, and the work reads the gap as "background cues provide stronger cultural signals than food items alone."[^c26] This is a test-time pull on a model that was not trained on the shortcut; the paper does not describe it as a training artifact, so it sits beside the swap cases above rather than among them.

## Limits

- The source is a mini review. It reports examples from cited studies and runs no experiments of its own. Its Table 1 maps examples across domains; it does not estimate how common the effect is, and no prevalence is established here.
- The formal account is a one-line sketch of empirical risk minimization with a feature z that is part of x. It says the shift breaks the cue, but it gives no test that tells from data alone whether a learned cue is spurious rather than causal. The review's detection methods are described, not evaluated across domains, and it judges that "these approaches often require manual intervention, extensive domain knowledge, and focused infrastructure."[^c11]
- The review's analogy is also a claim: AI systems "cannot separate causally relevant features from spurious ones without human interventions and validation."[^c12] That is asserted, with a citation, not shown here. The analogy is also offered as a warning "against interpreting high-performing models as showing genuine understanding or reasoning."[^c13]
- The synonymy of Clever Hans, shortcut learning and spurious correlation is the review's choice. A literature that separates a true artifact of collection from a correlation the task itself contains would split this note; the review does not separate them.
- The word "shortcut" is also used in the wiki for a different thing, a constraint set with several valid concept mappings; see [[reasoning-shortcut]]. The sense here is a spurious input cue.
- The review states that "current methods remain inconsistent, often tailored to specific datasets, and lack rigorous cross-domain validation."[^c14] The claims about detection and mitigation therefore rest on single-dataset evidence in the works it cites, and this note does not re-check them.
- The video case is a measured instance of the split the bullet above asks for: background is informative on ordinary clips and a trap under swap. It does not show whether that correlation is a property of the task or of how the benchmark was collected, so the split stays open here (see [[dual-use-context-cue]]).
- An attribution check for this effect can misread the cue in both directions. In a synthetic traffic-sign study, the share of saliency on the background moved with the correlation built into the training data, so a low share is not by itself a sign of absent cue reliance. The authors conclude that "Background attention should not inherently be interpreted as detrimental to performance."[^c25] The measure and its limits are in [[background-attribution-share]]. The study runs on one use case and two saliency methods, so this is a single measured instance, not a general rate.

## Related

- [[reasoning-shortcut]] — a different sense of shortcut: several constraint-satisfying mappings, not a spurious input cue
- [[refusal-shortcut-learning]] — the same cue-for-intent structure in safety refusals, bound to templates and trigger words
- [[option-matching-shortcut]] — a choice-format cue that lets a reasoning model match options instead of deducing
- [[ood-confounded-removal-evaluation]] — an evaluation step that itself moves inputs out of distribution and opens a spurious path
- [[provenance-cue-leakage]] — the same reliance where the cue is who produced the labelled data; measured on ChEMBL bioactivity, with a source-only model near a structure baseline
- [[dual-use-context-cue]] — the video case where a background cue is a trap under swap and evidence on ordinary clips
- [[instruction-steered-cue-reliance]] — the same cue reliance moved by the wording of the question
- [[background-attribution-share]] — the saliency share on background pixels, read as a health signal; it tracks the training data's correlation, so it does not separate cue reliance from legitimate use
- [[culture-mixing]] — the same background reliance where the background carries a second culture's cues in a still image; the pull is graded by cultural distance

[^c1]: doi-10-3389-frai-2025-1692454 — "responding to subtle, unintentional cues from his handler"
[^c2]: doi-10-3389-frai-2025-1692454 — "the model may minimize the loss by learning"
[^c3]: doi-10-3389-frai-2025-1692454 — "may perform well on in-house data but often fail to bridge the gaps when the model encounters real-world variations and distribution shifts in data"
[^c4]: doi-10-3389-frai-2025-1692454 — "Several factors are responsible for the emergence of the CH effect in AI systems"
[^c5]: doi-10-3389-frai-2025-1692454 — "preserve the same biases across training and testing sets, thereby masking shortcut reliance"
[^c6]: doi-10-3389-frai-2025-1692454 — "explainable AI methods often produce plausible but misleading attributions"
[^c7]: doi-10-3389-frai-2025-1692454 — "The Clever Hans effect goes undetected by standard validation methods"
[^c8]: doi-10-3389-frai-2025-1692454 — "vision models trained on ImageNet may learn background textures"
[^c9]: doi-10-3389-frai-2025-1692454 — "large language models (LLMs) display shortcut behavior by mimicking prompt formats and token distributions"
[^c10]: doi-10-3389-frai-2025-1692454 — "also referred to as spurious correlations and shortcut learning"
[^c11]: doi-10-3389-frai-2025-1692454 — "these approaches often require manual intervention, extensive domain knowledge, and focused infrastructure"
[^c12]: doi-10-3389-frai-2025-1692454 — "cannot separate causally relevant features from spurious ones without human interventions and validation"
[^c13]: doi-10-3389-frai-2025-1692454 — "The term is used to warn against interpreting high-performing models as showing genuine understanding or reasoning"
[^c14]: doi-10-3389-frai-2025-1692454 — "current methods remain inconsistent, often tailored to specific datasets, and lack rigorous cross-domain validation"
[^c15]: arxiv-2512-21711 — "70% versus roughly 30% for the original model,"
[^c16]: arxiv-2512-21711 — "accuracy approaches 100% when shortcuts favor the correct answer, drops to 13% on the"
[^c17]: arxiv-2512-21711 — "COCONUT encourages heavy shortcut reliance rather than"
[^c18]: arxiv-2512-17953 — "a behavior known as background bias"
[^c19]: arxiv-2512-17953 — "where the human from class A is placed on a mismatched background of class B"
[^c20]: arxiv-2512-17953 — "We find that all models display background"
[^c21]: arxiv-2512-17953 — "Bias is highest when backgrounds are distinctive and consistently paired with actions"
[^c22]: arxiv-2512-17953 — "larger model capacity alone is insufficient for robust action understanding"
[^c23]: arxiv-2512-17953 — "helps the model focus more on the human motion than the background context"
[^c24]: arxiv-2512-17953 — "useful context is lost"
[^c25]: arxiv-2512-05937 — "Background attention should not inherently be interpreted as detrimental to performance."
[^c26]: arxiv-2511-22787 — "background cues provide stronger cultural signals than food items alone"
