---
description: "Distilling the search over candidate clarification questions into one LLM finetuned to condition on the retriever's belief distribution and generate rank-improving questions."
aliases: ["CLARINET", "retrieval-conditioned question selection", "rank-improvement training objective"]
sources: ["chi-2024", "arxiv-2512-13102"]
---
# Retrieval-conditioned question selection

> Instead of scoring candidate questions at inference time, train the
> question generator on the encoded retrieval distribution itself, so the
> search over questions happens once, at training time, not on every turn.

## Definition / Mechanism

Chi, Lin, Lin & Klein (2024) present CLARINET, a system for
asking clarification questions in information retrieval (a "tip of the
tongue" book-search task). At each turn the retriever's current top
candidates, each concatenated with the interaction history, are encoded
separately and fed to a Fusion-in-Decoder (FiD) decoder that generates the
next clarification question — the retrieval distribution is an input to
generation, not a post-hoc filter over generated candidates.[^c1]

Training data is constructed by simulating multi-turn interactions with a
GPT-3 user-proxy over real initial queries, sampling a pool of 20-50
candidate questions per turn, and keeping only the questions that would have
placed the target book in the top 10 of the retriever's ranking or increased
its rank by at least 10 places ("delta") had they been asked; a Flan-T5-base
model is then finetuned on (interaction history, kept question) pairs. At
inference the model samples a question directly — no candidate pool, no
per-question scoring.[^c2]

On a real-world dataset of 784 book-search interactions (Bhargav et al.
2022, 1877-document corpus), CLARINET outperforms a purely dialogue-based
LLM baseline (no retriever conditioning) by 39% relative top-1 retrieval
accuracy after ten turns, and outperforms explicit per-turn scoring by
expected information gain or [[kl-divergence|KL divergence]] by 17% relative, while being
cheaper at inference — those baselines must score every candidate question
against every retrieval candidate at every turn, CLARINET does not.[^c3]

## Why it matters

This is a concrete instance of the wiki's stall-2 tension between
[[expected-information-gain|EIG]]-style inference-time scoring and a
cheaper, learned alternative: CLARINET's training signal *is* an
EIG-adjacent quantity (rank improvement under the retriever posterior), but
the search over "which question scores best" is amortized into gradient
descent once, rather than run per turn. The ablation the paper reports (the
"delta" objective beating a "top-10-only" objective) shows the target is not
merely "reach a good absolute rank" but "improve rank by a margin" —
i.e. the training label already encodes a comparative, not absolute,
information criterion.[^c4]

## Transfer

| | |
|---|---|
| **Home field** | [[bayesian-experimental-design|Bayesian experimental design]] / information theory: EIG and KL-divergence question scoring, computed explicitly per candidate at inference time |
| **Here** | a text-generation model trained end-to-end so that the scoring is implicit in which questions survive the training filter |
| **What survives** | the target the scoring criteria are proxies for — moving probability mass onto the true candidate — is kept as the training label (rank improvement), not discarded |
| **What does not** | the explicit posterior computation. A parallel result in the same paper: replacing the retriever's explicit Bayesian posterior update with a single LLM-generated natural-language summary of the interaction ("language posterior") outperforms the explicit-posterior variant, because single-turn evidence is out-of-distribution for the retriever and compounds errors under exact [[bayesian-estimation|Bayesian updating]] — see [[language-posterior]] |

The same selection principle appears on the reasoning side. In Socratic Students, each candidate question is scored by the student's own downstream outcome after the teacher's reply: the candidate "is scored using the student’s downstream Pass@k performance on the problem."[^c6] The best-scoring candidate becomes a preferred example and the lower-scoring ones contrasts, so the questioning policy is trained on preference pairs rather than on a keep-filter.[^c7] The candidate pool can come from the student itself or from a peer model.[^c8] Here the outcome is the answerer's success rate on the original problem, not a retriever's rank; the training target is the same kind of comparative gain that the "delta" objective above encodes.

## Limits

- Evaluated with a simulated user (a prompted GPT-3 model with oracle access
  to the target), not humans; the paper's own Limitations section states the
  system "has not been evaluated by humans."[^c5]
- Single domain (book retrieval, one 1877-document corpus, 784 interactions
  split 156 train / 628 eval) and one retriever (DPR); generalization to
  other retrieval domains is asserted, not shown.
- The 17%/39% figures are relative gains on top-1 retrieval accuracy in this
  one setting; they do not establish that rank-improvement training
  dominates EIG/KL scoring in general, only in this benchmark and retriever.
- The reasoning-side variant uses the answerer's own Pass@k as the outcome, which the paper itself says "may conflate good questioning with favorable answer sampling."[^c9]

## Related

[[expected-information-gain]] · [[language-posterior]] · [[clarification-request]] · [[value-of-information]]

[^c1]: chi-2024
[^c2]: chi-2024 — "Only the questions that help the system to rank the target book as top 10, or help increase the rank by 10 will be used in the training."
[^c3]: chi-2024 — "our system outperforms traditional heuristics such as information gain on retrieval success by 17% and vanilla prompted LLMs by 39% relative."
[^c4]: chi-2024
[^c5]: chi-2024 — "The interactive retrieval system has not been evaluated by humans, so the retrieval performance could be different from a more realistic environment."
[^c6]: arxiv-2512-13102 — "is scored using the student’s downstream Pass@k performance on the problem."
[^c7]: arxiv-2512-13102 — "The highest-scoring candidate is treated as a preferred"
[^c8]: arxiv-2512-13102 — "is sampled from a more capable peer model."
[^c9]: arxiv-2512-13102 — "this may conflate good questioning with favorable"
