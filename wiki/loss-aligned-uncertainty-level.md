---
description: "A rejection score must measure uncertainty at the level of the decision's loss; in structure retrieval, retrieval-level scores beat fingerprint- and input-level ones, whatever their epistemic label."
aliases: ["task-aligned uncertainty", "uncertainty level matters more than type"]
sources: ["arxiv-2603-10950"]
---
# Loss-aligned uncertainty level

In selective prediction a system abstains when a score says its answer is likely wrong. The score can be computed at different levels of the pipeline. Here it is measured on retrieving molecular structures from mass spectra, at three levels: the input's distance in the learned representation, the predicted fingerprint, and the ranking of candidates.[^c1] The loss being controlled is the miss rate among accepted predictions, defined as 1 − Hit@K.[^c2]

The finding is that the level matters more than the label. Fingerprint-level scores reached relAURC of about 0.9 or higher, which is close to random rejection. The authors' explanation is that retrieval success depends on how the correct candidate compares with its competitors, not on the absolute quality of the fingerprint. A confident fingerprint can still miss when several candidates look alike. A vague one can suffice when the right candidate stands apart.[^c3] Input-distance scores were also weak. The representation is trained for fingerprint prediction or retrieval and need not be organised by retrieval difficulty.[^c4]

Among retrieval-level scores, total uncertainty beat both its aleatoric and epistemic parts across all three posterior approximations and retrieval cutoffs. Epistemic uncertainty alone, which is disagreement between posterior samples, was consistently the weakest.[^c5] This matches the task-alignment principle that the optimal rejection criterion is total predictive uncertainty.[^c6] The same fingerprint-level scores become informative when the target loss measures fingerprint similarity, so alignment is relative to the loss, not a property of the score.[^c3]

For top-1 retrieval the relevant uncertainty is how peaked the candidate distribution is, which confidence captures. For K > 1 it becomes a question of how stable the set's composition is, which rank variance captures.[^c7]

My inference, not the paper's: an asker deciding whether to trust an answer should first name the loss that an error would incur. Then they should pick the uncertainty signal that is computed at that level, not the one that is easiest to read off.

## Limits

One domain (MassSpecGym, formula-filtered candidates) and two architectures, an MLP and a transformer. The paper reports that the ordering of rank variance versus total uncertainty is qualified by architecture. Transfer to language-model question answering is untested here. Even good scores cannot rescue hard tasks: at K = 1 a risk-controlled procedure can only guarantee risk on a small subset, because most predictions are wrong.[^c8]

## Related

- [[abstention]] — the act this score serves
- [[uncertainty-decomposition]] — the aleatoric/epistemic split that this note finds less decisive than the level
- [[confidently-wrong-low-entropy-regime]] — confident scores that fail to track error

[^c1]: arxiv-2603-10950 — "we introduce a selective prediction framework for molecular structure retrieval from MS/MS spectra,"
[^c2]: arxiv-2603-10950 — "we define"
[^c3]: arxiv-2603-10950 — "Fingerprint-level uncertainty is therefore poorly aligned with the retrieval loss."
[^c4]: arxiv-2603-10950 — "need not be organized"
[^c5]: arxiv-2603-10950 — "total retrieval uncertainty outperforms both its aleatoric and epistemic components."
[^c6]: arxiv-2603-10950 — "the optimal rejection criterion for selective prediction is total predictive"
[^c7]: arxiv-2603-10950 — "the relevant uncertainty concerns the stability of the predicted set’s composition."
[^c8]: arxiv-2603-10950 — "any"
