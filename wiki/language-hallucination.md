---
description: "A reply in another language than the question's, despite an instruction to match it, is scored apart from factual error; the answer is realigned to the gold in its own language."
aliases: ["off-language response", "mis-language response", "wrong-language output"]
sources: ["arxiv-2512-01852"]
---
# Language hallucination

A model can be asked in one language and answer in another. BHRAM-IL, a benchmark for hallucination in Hindi, Gujarati, Marathi, Odia and English, gives this a class of its own, separate from getting the content wrong. Language hallucination is the case where the model responds in a language other than the prompt's, even though a system instruction told it to match the prompt, and any such reply is flagged.[^c1] Its complement is factual hallucination: the reply stays in the right language and still deviates from the gold reference.[^c2]

The two are kept apart in the scoring. Each prediction is first checked for the language it was given in. An off-language reply is realigned to the gold answer in the language it was in, when such a gold exists, and the primary metric is recomputed; the result is a language-corrected score (LCS).[^c3] A fuzzy variant (LCFS) adds normalized string similarity with a fixed threshold.[^c8] A single reply can therefore be a language failure, a content failure, or both, and the language rate is reported on its own. The pattern this exposes is that the switch is usually toward English, and that it depends on the model and the prompt. By my reading of Table 3, the reported language-hallucination rates run from about 16% to 47% across model and prompt pairs.

Native-language prompts lower the rate for most models: "Native prompting substantially reduces language hallucination rates across most models" is the paper's summary.[^c4] The exceptions and the extreme are small Gemma variants, which under English prompts frequently fall back to English, giving high language hallucination rates.[^c5] Scores stay modest even after correction: the best primary score is 0.44 and the language-corrected fuzzy score 0.61.[^c6][^c7]

The paper observes the switch but does not test why a model makes it. Its default-to-English pattern is a description of outputs, not an account of generation.

Why it matters for asking and answering. The language of a question is a constraint on the answer, in the same way the requested answer type is. A reply in the wrong language fails that constraint even when its content is right, and a benchmark that scores only content will credit or penalize it for the wrong reason. On the evaluation side, language fidelity is a separate axis that must be read before a factual score is trusted.

## Limits

- The sections read do not describe how a reply's language is identified, and the reliability of that flag is not reported there. Every rate in this note depends on it.
- Realignment exists only where a gold answer in the other language is available. Where none is, the reply cannot be corrected and the language failure stands alone.
- The gap between the primary score and the fuzzy score mixes language correction with fuzzy matching. The text does not separate the two, so the move from 0.44 to 0.61 is not a measure of language alone.[^c7]
- The non-NER items were machine-translated from English,[^c9] so a language switch is measured on translated questions. The translation share is not separated out here (see [[translation-confounded-language-gap]]).
- The measurement covers 14 models.[^c10] Nothing here shows the pattern for other models or for languages outside the five used.
- That forcing English reasoning changes the answer's quality is a result from another paper and another setting; linking it here as a cause of English defaulting is this wiki's inference, not a tested link.

## Related

- [[translation-confounded-language-gap]] — the same translation confound that clouds a language gap also clouds a language-switch rate
- [[reasoning-language-ue-bottleneck]] — another place where the language of the answer matters; there the English route helps, here the switch to English is the failure, so the two should not be merged without a test
- [[evidence-language-integration-gap]] — a language-dependent failure on the answerer's side, where the evidence rather than the reply is in the other language
- [[false-premise-question]] — the same benchmark's semantically incorrect category measures a different failure: accepting a false premise rather than answering in the wrong language

[^c1]: arxiv-2512-01852 — "the input prompt, despite a system instruction to output in the same language"
[^c2]: arxiv-2512-01852 — "correct language but deviate from the ground truth"
[^c3]: arxiv-2512-01852 — "If it responds in a different language, we realign the output to the corresponding gold answer in that language"
[^c4]: arxiv-2512-01852 — "Native prompting substantially reduces language hallucination rates across most models"
[^c5]: arxiv-2512-01852 — "1B) exhibit particularly high language hallucination when prompted in English, frequently defaulting to English responses"
[^c6]: arxiv-2512-01852 — "Notably, even the best primary score remains low at 0.44"
[^c7]: arxiv-2512-01852 — "fuzzy score reaching only 0.61"
[^c8]: arxiv-2512-01852 — "Fuzzy Match uses normalized string similarity with a fixed threshold"
[^c9]: arxiv-2512-01852 — "All non-NER categories are translated from EN"
[^c10]: arxiv-2512-01852 — "We evaluate 14 state-of-the-art multilingual LLMs"
