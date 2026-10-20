---
description: "An answer's surprisal given the question minus its surprisal alone, rather than raw perplexity, strips the word-frequency prior; in video RL it trained better than raw perplexity."
aliases: ["calibrated surprisal", "conditional-minus-unconditional NLL", "question-conditioned answer surprisal"]
sources: ["arxiv-2601-00887"]
---
# Calibrated surprisal

Surprisal of an answer under a language model, the negative log-likelihood of its tokens, is the usual cheap difficulty proxy: an item whose answer the model finds unlikely is read as hard. The VideoCuRL paper argues that for reasoning items this reading mislabels answers. Raw NLL is "biased by the language prior": an answer with rare words scores as hard whatever the reasoning, since "answers containing low-frequency vocabulary yield high NLL scores, even if the reasoning is trivial."[^c1] The authors name the failure: "linguistically rare" is mistaken for "logically hard."

The repair subtracts the prior. For answer A = w_1 … w_n and question Q, the paper takes the conditional surprisal, the sum of −log π(w_t | w_<t, Q), and subtracts the unconditional surprisal, the same sum without Q. The difference is what the question changes about the answer's predictability, so the score is "the reduction in uncertainty" that Q buys, and it "effectively isolates the reasoning requirement from inherent linguistic unpredictability."[^c2] The raw scores are then quantile-normalized to [0, 1] (see [[orthogonal-difficulty-decomposition]]).[^c3]

The computation needs only a text model. The paper stresses that it reads question–answer pairs and so avoids "the overhead of video encoding or autoregressive video" decoding.[^c4]

Information-theoretically the difference is the pointwise mutual information between question and answer under the model, the quantity behind [[information-gain-reward]]. The formalism transfers: the subtraction of the marginal is what removes a shared frequency effect. What does not transfer is the reading of the score as "reasoning". The subtraction removes word-frequency effects, but it does not check that the answer needs the video or the question's reasoning steps.

## Measured

In the ablation, replacing calibrated surprisal with raw perplexity hurts, "particularly on VSI-Bench (-1.8%) and VideoMMMU (-1.5%)." The authors read this as showing "raw NLL is biased toward linguistic frequency."[^c5] Figure-level validation is weaker: against training-set accuracy the cognitive axis shows "a general downward trajectory", with local fluctuations that the authors attribute to the stochastic nature of generation "persist due to the stochastic nature of autoregressive generation".[^c6]

## Limits

- The sign convention is unclear in the text as extracted. The formula is written as conditional minus unconditional NLL, which makes the score the negative of the information gain, yet the text calls it "the reduction in uncertainty" and says that "A high Scog indicates that the answer A is not easily predictable from the question Q alone."[^c7] These readings point in opposite directions. My reading is that the intended quantity is the information the question gives about the answer; the paper's own sign is not settled by the sections I read.
- Two benchmark deltas (1.5 and 1.8 points) from one ablation on one base model. No variance across seeds is reported in the parts read.
- The score is judged by a text-only model. A question-plus-answer pair that a language model can guess from wording will read as easy even when the video is essential to the answer. This is my inference; the paper does not test it.
- The cognitive axis is the less clean of the two validation plots: the text describes its accuracy trend as general, with fluctuations, against the visual axis's "stabilized inverse trend."[^c8]

## Related

- [[surprisal]] — the raw quantity this score corrects by subtracting the prior
- [[mutual-information]] — the identity behind the difference, and the sign question above
- [[information-gain-reward]] — the same question-to-answer information used as a reward for asking, here as a difficulty proxy for training items
- [[orthogonal-difficulty-decomposition]] — the grid this score is the cognitive axis of

[^c1]: arxiv-2601-00887 — "high NLL scores, even if the reasoning is trivial."
[^c2]: arxiv-2601-00887 — "which effectively isolates the reasoning requirement from inherent linguistic unpredictability"
[^c3]: arxiv-2601-00887 — "uniform distribution via Quantile Normalization to"
[^c4]: arxiv-2601-00887 — "overhead of video encoding or autoregressive video"
[^c5]: arxiv-2601-00887 — "raw NLL is biased toward linguistic frequency"
[^c6]: arxiv-2601-00887 — "persist due to the stochastic nature of autoregressive generation"
[^c7]: arxiv-2601-00887 — "A high Scog indicates that the answer A is not easily predictable from the question Q alone"
[^c8]: arxiv-2601-00887 — "a stabilized inverse trend"
