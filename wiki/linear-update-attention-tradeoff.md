---
description: "A linear weight update that pushes attention down on irrelevant tokens can also distort the relative attention among relevant ones, so fine-tuning for noise filtering trades off against reasoning."
aliases: ["linear update trade-off", "noise filtering versus reasoning trade-off", "attention update trade-off in fine-tuning"]
sources: ["arxiv-2601-01896"]
---
# Linear-update attention trade-off

Standard fine-tuning changes a model's attention by adding a low-rank update to the query-key product. The attention score between query token i and key token j becomes x_i^T (W + ΔW) x_j, so the change to the score is linear in the input pair. The paper's argument is that this linearity is what blocks noise filtering. "To filter noise, the learned parameter update must apply a strong negative adjustment to the attention scores of irrelevant tokens."[^c1] The same update, though, is applied to every token, and "this same linear adjustment is applied across all tokens, which can inadvertently distort the nuanced, relative attention patterns among the relevant tokens."[^c2] The model is then "forced to choose between effective noise filtering and preserving its reasoning capacity."[^c3]

The paper makes this precise with an approximation claim. Suppose the goal is for the fine-tuned attention, after softmax, to stay within a factor of 1 ± ε of the attention the model would have if noise were removed. Let ξ_r be the spread of the update x_i^T ΔW x_j across the relevant tokens. The condition on that spread is ξ_r ≲ ln((1+ε)/(1−ε)), which is near zero for small ε. "This implies that for all tokens to be retained" the update must stay nearly constant, while the update on noise tokens must be strongly negative.[^c4] A single linear term has to satisfy both, and the paper takes this as the reason that standard fine-tuning cannot approximate the noise-free attention pattern.

The paper's response is to change the shape of the update, not its size: it "introduces a nonlinear rectification function to the attention update," with one regime that saturates for irrelevant tokens and a nearly linear regime for relevant ones.[^c5] The method itself is not recorded in this note; what matters for the concept is the diagnosis that a linear term cannot serve both regimes.

## Limits

- The approximation result is for a single attention head and a linear update. The paper says that using separate heads for filtering and for reasoning would be "ideal," but it does not analyse that case: "This is indeed ideal, but fine-tuning based on existing LLMs fails."[^c6]
- The claim that a single linear term cannot serve both aims is a sufficient-condition argument. It shows the linear update must satisfy a near-constancy condition to approximate the noise-free pattern; it does not show that no update of any kind could satisfy it with a trained, high-rank change.
- The empirical comparison is with LoRA fine-tuning, which the paper sets at rank 64 on three 7–8B models. It does not isolate the linear-update step from other differences, and the Table 1 gains are measured with gold documents added to the context, which the paper says is "mainly because we add gold documents to the context."[^c7]
- Catastrophic forgetting is cited as a reason to avoid large changes to the existing weights, but the paper does not measure forgetting in its own runs.
- The argument concerns attention scores before softmax. How a nonlinear rectification interacts with the rest of the network, including the feed-forward layers the paper mentions only briefly, is not analysed.

## Related

- [[triple-wise-relevance-judgment]] — the pairwise limit of attention that leaves fine-tuning as the place where noise has to be filtered.
- [[neuron-guided-robustness-localization]] — another route to separating relevant from irrelevant context: localize neurons that respond to each and train them apart, rather than reshape the attention update.
- [[distractor-similarity-reasoning-inflation]] — look-alike distractors are where a linear update is most likely to be pulled in both directions.

[^c1]: arxiv-2601-01896 — "To filter noise, the learned parameter update must apply a strong negative adjustment to the attention scores of irrelevant tokens."
[^c2]: arxiv-2601-01896 — "this same linear adjustment is applied across all tokens, which can inadvertently distort the nuanced, relative attention patterns among the relevant tokens"
[^c3]: arxiv-2601-01896 — "the model is forced to choose between effective noise filtering and preserving its reasoning capacity."
[^c4]: arxiv-2601-01896 — "This implies that for all tokens to be retained"
[^c5]: arxiv-2601-01896 — "introduces a nonlinear rectification function to the attention update"
[^c6]: arxiv-2601-01896 — "This is indeed ideal, but fine-tuning based on existing LLMs fails"
[^c7]: arxiv-2601-01896 — "this is mainly because we add gold documents to the context"
