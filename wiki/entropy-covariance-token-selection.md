---
description: "A token's pull on policy entropy is its covariance between log-probability and advantage; low-entropy tokens with high covariance are where a KL penalty should be strongest."
aliases: ["covariance-based token selection", "high-covariance low-entropy tokens", "log-probability advantage covariance", "token-selective KL regularisation"]
sources: ["arxiv-2512-04359"]
---
# Entropy-covariance token selection

Under a policy-gradient update, the effect of one token on the policy's entropy is a covariance. The paper takes this from earlier analysis: "policy entropy changes are proportional to the covariance between action probabilities and their gradient magnitudes."[^v1] Its working form computes, for each token, the deviation of that token's log-probability from the batch mean, multiplied by the deviation of its advantage from the mean advantage, "where N is a batch of rollout tokens."[^v2] A positive value means a token the policy already favours also carries a high advantage. Updates on such tokens sharpen the distribution, so entropy falls.

The criterion is a selector. The paper first keeps only low-entropy tokens, since these are the ones it judges "most vulnerable to entropy collapse."[^v3] Within that set, tokens whose covariance is above a threshold get the strongest KL penalty toward the reference model, the others a weaker one, and high-entropy tokens none. The KL term matters because it is the part of the objective that counteracts the fall. The paper's reading is that "the KL term acts to pull the policy back toward the reference distribution, reducing the magnitude of policy updates."[^v4]

The paper contrasts this with masking. Earlier work "masks 80% of low-entropy tokens during optimization," and the paper argues instead that "instead of masking all low-entropy tokens which may lead to instability, we apply targeted KL constraints on these tokens."[^v5][^v6] So the same token set is handled by a penalty rather than by removing it from the gradient. The selector and the penalty are separable: the covariance says which tokens, the KL coefficient says how hard.

The ablation gives the only measured evidence for the covariance step. Its authors write that "jointly constraining high-covariance tokens with low-entropy tokens yields superior learning dynamics during training compared to constraining low-entropy tokens in isolation."[^v7] They also report that the two constraints "independently demonstrate performance improvements over the GRPO baseline."[^v8]

## Limits

- The covariance is a sample statistic over one batch of rollout tokens. With a small batch it is noisy, and the rule for which tokens fall above the threshold can change from batch to batch (my inference).
- The sign argument is first order: it says what one step does to entropy, given the logit change, and does not follow entropy over a run.
- The two thresholds, on entropy and on covariance, are chosen by the authors. They are analysed in a section I did not read, so I cannot say how sensitive the selection is to them.
- The covariance uses advantages from group normalisation. Whether the sign relation survives other advantage estimators is not addressed in the parts I read (my inference).
- The ablation compares constraints on and off, not against a random selection of the same number of tokens. So it does not separate the value of the covariance criterion from the value of constraining some low-entropy tokens at all.
- Entropy is not correctness. Keeping a token's distribution broad does not make the answer right, and the paper's gains are reported on accuracy metrics that the entropy argument does not by itself predict.

## Related

- [[rlvr-entropy-collapse]] — the collapse this selector is meant to slow, and the covariance identity it rests on
- [[kl-divergence]] — the penalty whose coefficient is set per token here
- [[semantic-entropy-curriculum]] — the data-side half of the same method, which orders questions rather than tokens
- [[solver-token-entropy]] — a per-token entropy read used as a difficulty signal, not as a regularisation target
- [[rollout-dispersion-curriculum]] — weights prompt groups by dispersion, where this note weights tokens

[^v1]: arxiv-2512-04359 — "policy entropy changes are proportional to the covariance between action probabilities and their gradient magnitudes"
[^v2]: arxiv-2512-04359 — "where N is a batch of rollout tokens"
[^v3]: arxiv-2512-04359 — "low-entropy tokens are most vulnerable to entropy collapse"
[^v4]: arxiv-2512-04359 — "The KL term acts to pull the policy back toward the reference distribution, reducing the magnitude of policy updates."
[^v5]: arxiv-2512-04359 — "while that work masks 80% of low-entropy tokens during optimization"
[^v6]: arxiv-2512-04359 — "instead of masking all low-entropy tokens which may lead to instability, we apply targeted KL constraints on these tokens"
[^v7]: arxiv-2512-04359 — "jointly constraining high-covariance tokens with low-entropy tokens yields superior learning dynamics during training compared to constraining low-entropy tokens in isolation"
[^v8]: arxiv-2512-04359 — "independently demonstrate performance improvements over the GRPO baseline"
