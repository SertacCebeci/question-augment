---
description: "Top-k uncertainty querying fails by class imbalance and redundant early picks; stratifying 66% of the budget by predicted class and decaying Gumbel score noise fixes both, beating improved random."
aliases: ["ClaSP PE", "Class-stratified Scheduled Power Predictive Entropy", "stratified power-noised uncertainty sampling"]
sources: ["arxiv-2601-13677"]
---
# Class-stratified scheduled-noise uncertainty sampling

Plain top-k uncertainty querying ranks every candidate by one score and takes the best. In 3D biomedical segmentation this has two failure modes: the picks pile onto the majority class, and early picks are near-duplicates. Two modifications to any uncertainty score address them, and the resulting method (ClaSP PE) is the only one in the benchmark that generally beats improved random baselines on segmentation quality while staying annotation efficient.[^c1]

## Mechanism

**Class stratification.** For each candidate x the uncertainty u(x) is multiplied by the model's predicted probability of class c, giving a class-specific score u_c(x) = p_c(x)·u(x). Candidates are ranked per class and an equal number N_c is taken from each class. No label information is needed, only the model's own predictions.[^c2] Only a fraction α of the budget is chosen this way (66% in the final method); the rest uses the plain uncertainty map so very uncertain items are kept whatever their class.[^c3]

**Scheduled power noising.** Before top-k selection the scores are perturbed on a log scale with Gumbel noise whose strength decays exponentially over active-learning cycles, from β0 = 1 to β_max = 100. Early cycles therefore explore (diverse picks) and later cycles exploit (pure uncertainty).[^c4] Both extensions are agnostic to the scoring function. The final method uses predictive entropy, which was the best method on the benchmark before this work.[^c5]

## What was measured

Across 24 experimental settings (four datasets, three label regimes, two patch sizes, four seeds), ClaSP PE ranked best on area under the budget curve and final Dice. It did not always have the top foreground efficiency but stayed among the most efficient.[^c6] Ablations in the paper attribute the avoidance of wasted annotation to the score perturbation, and report that decaying the noise raises segmentation performance at a slight efficiency cost.[^c7] The parameters were then fixed by written guidelines and applied unchanged to four unseen datasets, where the paper reports that it generalised without dataset-specific tuning.[^c8]

The conceptual point for asking: an informativeness score alone is a poor question-picker. It must be combined with coverage of rare categories and with diversity, and the weight of diversity should shrink as the learner's knowledge improves (my reading of the design, not a separately tested claim).

## Limits

- Evidence is confined to nnActive with nnU-Net and 3D patch queries; nothing is tested on language models or human questioning.
- The values α = 66%, β0 and β_max come from the authors' own analysis on this benchmark; transfer to other tasks is untested here.
- Stratification relies on the model's predicted classes, which are wrong early on, exactly when the stratification is most needed. The paper's evidence on this was not examined.
- Gains on single datasets can be small; the claim is at the aggregated level, as the paper itself notes.
- The baselines are random strategies adapted to 3D foreground oversampling, so "beats random" is relative to those.

## Related

- [[class-balanced-query-model-selection]] — another case where class balance of the queried set drives final performance
- [[oracle-best-of-strategies-batch-selection]] — also asks which selection strategy to use under a labeling budget
- [[active-testing]] — chooses which items to label under a budget

[^c1]: arxiv-2601-13677 — "ClaSP PE is the only method that generally outperforms improved random baselines in terms of both segmentation quality with statistically significant gains, whilst remaining annotation efficient."
[^c2]: arxiv-2601-13677 — "by leveraging the model predictions our approach does not require any additional label information."
[^c3]: arxiv-2601-13677 — "only a fraction α of the samples is selected using this stratified approach"
[^c4]: arxiv-2601-13677 — "in order to gradually shift the focus from exploration to exploitation"
[^c5]: arxiv-2601-13677 — "these extensions are agnostic to the specific uncertainty scoring function used"
[^c6]: arxiv-2601-13677 — "ClaSP PE achieves the best overall performance in terms of both AUBC and Final Dice"
[^c7]: arxiv-2601-13677 — "score perturbation is crucial for preventing such inefficiencies"
[^c8]: arxiv-2601-13677 — "The results confirm that ClaSP PE robustly generalizes to novel tasks without requiring dataset-specific tuning."
