---
description: "The language of a factual prompt shifts which entities a model ranks highest, measured as the share of language-tied wrong answers in its top ten; the shift varies by topic."
aliases: ["inference bias", "language-induced factual bias", "prompt-language factual bias", "factual inference bias score"]
sources: ["arxiv-2512-11110"]
---
# Factual inference bias

When a factual question is put to a language model in one language, the answers it prefers can lean toward entities tied to the region where that language is spoken, even when those entities are not the true answers for the subject. The concept is the ranking-side version of what the literature calls inference bias. Kim and Kim describe inference bias as a "tendency to favor the language of the prompt when generating responses."[^f1] The FIBER paper moves the measurement from generated text to probabilities. It asks factual questions and evaluates "by the probability ranking of ground truth tokens."[^f2] The bias is then the case where the model "captures cases where the model assigns higher likelihoods to factual entities that are geographically aligned" with the prompt language.[^f3]

**How it is read.** For a topic and a set of subjects, the model is prompted in language l and its top answers are taken; the paper uses the top ten.[^f4] Each answer is checked against two sets. One is the truly related entities R(s). The other is a language-specific set Q(l, t) of "incorrect or biased associations unique to that language-topic pair." The bias is the proportion of Q that appears in the output, averaged over the subjects of a topic to give one score per topic.[^f5][^f6] English is left out of the score because it is tied to several regions, which makes it a poor probe for the pull of one language.[^f7]

**What was found.** The effect is real but uneven across topics. The paper reports that "31% of the topics exhibit factual inference bias score" above 0.5.[^f8] The high scores cluster on language-related subjects: "most of the topics with scores exceeding 0.5 are associated with language-related subjects."[^f9] Across languages the paper reports a mean of "with an average Factual Inference Bias of 0.312" for Italian, and says "Turkish prompts show higher bias" than Italian in most topics.[^f10][^f11] Model size did not change the picture; the paper finds it has no "significant effect to the factual inference bias."[^f12] The authors expected the degree of bias to depend on the prompt type, since it "may vary depending on the" format of the question.[^f13]

**What transfers from generation.** The original measure counts language-aligned words in generated text. The ranking version asks which candidate the model prefers when all candidates are scored, so it can register a preference that one greedy output would not show. That this matters for any particular model is my inference; the paper does not test it against generation on the same items.

## Limits

- The topics are few and mostly about countries, cities and languages. The paper concedes that this scope "limits the generalizability" of its findings to "broader or more diverse knowledge" domains.[^f15]
- The language-related topics score highest. That pattern is what one would expect if entities tied to a language are simply more frequent in text written in that language. The paper does not separate a preference from a frequency effect. My inference: this is the same confound that [[structural-priors-in-language-preference]] finds in multilingual retrieval, where the benchmark's data can look like a model's language preference.
- The Italian and Turkish entities were produced by translation: "subjects and entities into Italian and Turkish with Gemini" and then checked by native speakers.[^f14] How much translated surface forms move the score is not tested.
- Only two non-English languages are studied: "our experiments include only two" of them.[^f16]
- The score depends on the set Q, which the researchers choose. The candidate pool is "restricted to entities explicitly included in our" dataset.[^f17] A different Q would give a different score; the text I read does not show how sensitive the 0.5 threshold is to that choice.

## Related

- [[structural-priors-in-language-preference]] — the same confound logic, in multilingual retrieval: data distribution can look like a model's language preference.
- [[debiased-language-preference]] — a regression that removes such priors from a retrieval language-preference score; the text of FIBER offers no equivalent correction for its bias score.
- [[answer-format-dependent-bias-measurement]] — a bias score depends on the answer format it is posed in, which is the same worry FIBER raises for sentence completion versus question answering.
- [[candidate-ranking-average-precision]] — the ranking of candidate answers by log-probability, on which this bias score is read.

[^f1]: arxiv-2512-11110 — "tendency to favor the language of the prompt when generating responses."
[^f2]: arxiv-2512-11110 — "by the probability ranking of ground truth tokens"
[^f3]: arxiv-2512-11110 — "captures cases where the model assigns higher likelihoods to factual entities that are geographically aligned"
[^f4]: arxiv-2512-11110 — "are conducted using the top-10 ranked positions"
[^f5]: arxiv-2512-11110 — "incorrect or biased associations unique to that"
[^f6]: arxiv-2512-11110 — "proportion of these language-specific entities (Q) that"
[^f7]: arxiv-2512-11110 — "English is associated with multiple regions"
[^f8]: arxiv-2512-11110 — "31% of the topics exhibit factual inference bias score"
[^f9]: arxiv-2512-11110 — "most of the topics with scores exceeding 0.5 are associated with language-related subjects"
[^f10]: arxiv-2512-11110 — "Turkish prompts show higher bias"
[^f11]: arxiv-2512-11110 — "with an average Factual Inference Bias of 0.312"
[^f12]: arxiv-2512-11110 — "significant effect to the factual inference bias."
[^f13]: arxiv-2512-11110 — "Moreover, the degree of bias may vary depending on the"
[^f14]: arxiv-2512-11110 — "subjects and entities into Italian and Turkish with Gemini"
[^f15]: arxiv-2512-11110 — "of our findings to broader or more diverse knowledge"
[^f16]: arxiv-2512-11110 — "our experiments include only two"
[^f17]: arxiv-2512-11110 — "restricted to entities explicitly included in our"
