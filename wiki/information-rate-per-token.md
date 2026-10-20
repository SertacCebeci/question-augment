---
description: "Bits of mutual information per output token, I/L, track a compressor's distortion: on the paper's setup, rate correlates with accuracy loss and with perplexity (r = -0.84)."
aliases: ["bit efficiency", "information rate", "MI per token", "information density"]
sources: ["arxiv-2512-21720", "arxiv-2512-09679"]
---
# Information rate per token

Take a compressor that writes L output tokens about a context X under a query Q. Its information rate is the [[mutual-information|mutual information]] I(X; Z | Q) divided by L, measured in bits per token: "for L output tokens (measured in bits of mutual information per token)."[^c1] The paper's point is that this single number, which needs no downstream task, tracks how well the compression will serve a predictor. Distortion is defined as one minus accuracy, "we define distortion as D = 1 − ACC(Z)" in the paper's notation, and the paper plots distortion against rate.[^c2]

The rate-distortion relation has the shape the paper expects from theory. The paper writes that "as rate increases, we expect distortion to converge towards a lower bound (irreducible error)."[^c3] The fitted curves are decaying exponentials, chosen by analogy to the classical rate-distortion function of a Gaussian source: "Motivated by the classical form of the rate-distortion function for a independent Gaussian source X, we fit decaying exponential functions to the rate-distortion data."[^c4] Predictor size shifts the curves, but past about 70B the shift is small, which matches the earlier finding that predictor scaling flattens.

The measured link to performance is strong. The introduction states that "information rate (MI per token) correlates strongly with downstream performance" and that rate "provid[es] a practical proxy for predicting system performance without full end-to-end evaluation."[^c5] The concrete figure is on FineWeb, where "mutual information is also strongly correlated with perplexity" (r = -0.84, R2 = 0.71), for extractive tasks.[^c6]

Why larger compressors score higher on rate is given a mechanism in the paper. They omit fewer of the needed tokens and carry more information per token: "fewer tokens, we find that larger compressors are more bit efficient."[^c7] The paper reads this as capacity appearing as "information density": "This suggests that increased model capacity and intelligence" shows up as more bits per token, not only more memorised content.[^c8]

The rate-distortion view also says the curve depends on the compressor's family as well as its size. The paper reports that "distortion is primarily dependent on model family and size." It adds that predictors "do not prefer compressors of the same family."[^c9] [^c10]

## Limits

- The perplexity correlation is measured on one setting, extractive tasks on FineWeb, with a linear fit. The QA correlation is stated as strong, but the paper's figures show it as curves per predictor size rather than one number.[^c11]
- Distortion is accuracy as judged by a model: "against the ground-truth using a GPT-4o-mini judge."[^c12] A rate-distortion curve is only as good as that judge.
- Rate divides by output length, so a compressor that writes fewer tokens for the same information gets a higher rate. That is the intended effect, but it also means rate is not a property of the information alone. This is my inference from the definition.
- Rate does not reach an intrinsic limit in the paper. Mutual information can saturate: "while Llama compressors are far from the theoretical maximum" holds on LongHealth, but on FinanceBench it saturates at small sizes.[^c13] Past saturation, rate stops separating compressors.
- The estimate of mutual information inherits the limits of its estimator, especially at 1–3B scale, where the paper flags variance and bias.[^c14]
- The Shannon rate-distortion function is a minimum over codes for a fixed source and distortion. The paper uses only the shape and the trade-off language. It computes no bound, and nothing here shows that a compressor's rate is near an optimum. What survives the transfer is the trade-off and the diminishing return; what does not is the claim of optimality.
- The same name, information density, is used for reasoning chains in arxiv-2512-09679, where the quantity is I(Y; C | X) per token: what a chain tells about the code beyond the problem. That paper calls its lens "conceptual rather than based on exact mutual information estimation," and it uses Pass@1 with token cost as the observable proxy.[^c15][^c16] The name carries over; the estimate does not. A chain is never estimated here, only read off accuracy per token (my inference).

## Related

- [[rate-distortion-theory]] — the formal frame whose trade-off the paper borrows; the paper's rate is an estimate per token, not the minimum rate of a code.
- [[mutual-information]] — the numerator, and the quantity whose estimator is treated separately.
- [[sampled-mutual-information-estimator]] — how the numerator is computed from sampled log-probabilities.
- [[compressor-predictor-scaling]] — the scaling result that rate is used to summarise.
- [[query-relative-token-overflow]] — a related question about whether a compressed token is adequate for a given query, which rate averages over all queries.

[^c1]: arxiv-2512-21720 — "for L output tokens (measured in bits of mutual information per token)."
[^c2]: arxiv-2512-21720 — "For simplicity, we define distortion"
[^c3]: arxiv-2512-21720 — "we expect distortion to converge towards a lower bound (irreducible error)."
[^c4]: arxiv-2512-21720 — "Motivated by the classical form of the rate-distortion"
[^c5]: arxiv-2512-21720 — "information rate (MI per token) correlates strongly with downstream performance"
[^c6]: arxiv-2512-21720 — "mutual information is also strongly correlated"
[^c7]: arxiv-2512-21720 — "fewer tokens, we find that larger compressors are more bit efficient"
[^c8]: arxiv-2512-21720 — "This suggests that increased model capacity and intelligence"
[^c9]: arxiv-2512-21720 — "distortion is primarily dependent on model family and size."
[^c10]: arxiv-2512-21720 — "Predictors do not prefer compressors of the same family."
[^c11]: arxiv-2512-21720 — "for extractive tasks on FineWeb"
[^c12]: arxiv-2512-21720 — "against the ground-truth using a GPT-4o-mini judge."
[^c13]: arxiv-2512-21720 — "while Llama compressors are far from the theoretical maximum"
[^c14]: arxiv-2512-21720 — "our MI estimator relies on proxy models and log probabilities, introducing potential"
[^c15]: arxiv-2512-09679 — "conceptual rather than based on exact mutual information estimation"
[^c16]: arxiv-2512-09679 — "Pass@1 with token cost for information density"
