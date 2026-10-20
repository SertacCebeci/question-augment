---
description: "Reasoning models that already re-check their answers while solving gain little from an extra forced self-verification pass, the paper suggests; the link rests on a keyword-rate scan."
aliases: ["spontaneous self-verification", "in-solution self-checking", "self-verifying reasoning", "reasoning-model self-check"]
sources: ["arxiv-2512-02304"]
---
# Spontaneous self-verification

A solver that is asked for an answer can also, while it reasons, stop to check what it has written. It may say that it will verify a step, pause, or reconsider. The paper calls this spontaneous self-verification: the model checks its own work during generation, without being told to. It is distinct from forced self-verification, where a second prompt asks the same model to judge its finished solution.

The paper measures how often this happens. It scans solver outputs for self-verification keywords, "let me check," "wait," "reconsider," and "that's wrong" among them, across the 21 post-trained models and nine datasets.[^c1] The rates separate the families sharply: "Qwen3 and DeepSeek self-verify in 96% and 73% of outputs," while "Llama3 and Qwen2.5 self-verify in only 1–2%."[^c2]

The paper connects this rate to the gain from a forced verification pass. It "hypothesize[s] that stronger reasoning post-trained models like DeepSeek and Qwen3 show negligible gains in self-verification and limited gains in intra-family verification," because they "may already engage in spontaneous self-verification when used as solvers, reducing the benefit of an additional forced verification."[^c3] The mechanism is redundancy: a second check adds little where the first is already happening inside the solution. The same point is stated as a question for future work: "the relevant question is whether reasoning post-training introduces spontaneous self-verification."[^c4]

The link is then stated as a finding. Llama3 and Qwen2.5 "show some ability to self-improve," while DeepSeek and Qwen3 do not, "which we find is linked to the latter already spontaneously self-verifying during solving (73–96% vs. 1–2%)."[^c5] This matters for the verifier-gain account. The measured gain for self-verification is the smallest of the three settings, and the paper reads that as a consequence of this rate rather than of the verifier's accuracy (see [[verifier-gain]]).

The concept is therefore a candidate explanation for when forced verification pays. It is not a property the paper checks in isolation. It is a second axis beside the verifier's own quality: a verifier that is accurate can still add little if the solver has already done the checking inside its reasoning.

## Limits

- The measure is a keyword scan. The list is given in the paper's appendix, which is not read here. A word such as "wait" can appear in text that is not a check, so a rate is an upper estimate of genuine self-checking.
- The link is correlational and rests on four families. The paper does not vary spontaneous self-verification in one model (for example, by suppressing it) and measure the change in forced-verification gain.
- Spontaneous self-verification co-varies with post-training and with model family. The paper's observed link does not separate the rate from the training data or the family's other differences.
- The argument is about the forced pass adding less value. It does not say that a forced pass is harmful, and the paper's FPR results show a separate bias in self-verification.
- The paper's evidence is for reasoning models in one tested set of nine benchmarks. Whether a higher spontaneous rate lowers forced-verification gain on open-ended tasks is not tested.
- The phrase "already spontaneously self-verifying" describes the keyword rate. Whether the in-solution checks are correct, or only look like checks, is outside what the paper measures.

## Related

- [[verifier-gain]] — the gain measure in which the self-verification setting comes out smallest
- [[solver-verifier-similarity]] — a different account of why same-model verification adds little: the verifier accepts solutions that resemble its own
- [[same-model-self-verification-conditional-confidence]] — a same-model self-verification used as a confidence signal, which is a different use of the same kind of extra pass

[^c1]: arxiv-2512-02304 — "by scanning solver outputs for self-verification keywords"
[^c2]: arxiv-2512-02304 — "self-verify in only 1–2%"
[^c3]: arxiv-2512-02304 — "may already engage in spontaneous self-verification when used as solvers, reducing the benefit of an additional forced verification"
[^c4]: arxiv-2512-02304 — "whether reasoning post-training introduces spontaneous self-verification"
[^c5]: arxiv-2512-02304 — "which we find is linked to the latter already"
