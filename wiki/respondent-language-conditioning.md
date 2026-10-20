---
description: "Simulated survey respondents prompted in their native language matched real survey distributions more closely than English-only ones in 13 of 21 countries, mostly lower-resource languages."
aliases: ["native-language simulation", "multilingual persona simulation", "language-conditioned survey simulation", "prompt-language effect on simulated respondents"]
sources: ["arxiv-2512-07195"]
---
# Respondent-language conditioning

A simulated survey respondent is conditioned on a persona, and the language that persona is run in is a lever of its own. In the MAWM framework each persona carries a native language assigned from its country, and agents read and write in that language.[^c1] The same personas can also be run in English. The paper's abstract reports that "native-language simulation better reflects real survey data than English-only simulation."[^c12] The two conditions are compared with the real country-level answer distributions from the survey.

The comparison is the measured part. Alignment is a root-mean-square error between simulated and real answer distributions, averaged over countries and rounds, where "RMSE ranges from 0 (perfect match)" up to a maximum divergence that depends on the number of response choices.[^c5] Across the 21 non-English countries in the MAPS benchmark, the native-language condition gave the lower error in most countries. The paper reports that "native-language simulation matches the real distributions more closely in 13 of the 21 countries," with the largest gains (up to 0.18 RMSE) in lower-resource, largely non-Latin-script languages such as Ukrainian, Thai, Arabic and Bengali.[^c2]

The mechanism the authors give is that the model's expressed values depend on the language it is prompted in: "native-language prompting activating culture-specific perspectives that English suppresses."[^c3] This is the authors' explanation, supported by citations to prior work on language-conditioned values. The paper's own experiment compares outcomes, not the internal cause, so the mechanism is a claim the paper makes and does not test here.

Where English did better, the margin was small. The authors report English ahead only in some Spanish-speaking countries, with differences of at most 0.11 RMSE, and they read Spanish as close to English in training data, so "these small gaps are a weak test."[^c4] The evidence they treat as substantive is the gain for lower-resource languages. For a question-writer the practical reading is that the language a respondent is simulated in changes the answer distribution, and that the change is not uniform across languages.

## Limits

- The effect is measured as a country-level distribution error on opinion questions from GlobalOpinionQA and the Pew Global Attitudes Survey. It is not a per-person test. The paper notes that "persona-to-opinion mapping operates at the country level rather than the individual level," which may hide within-country variation.[^c10]
- The comparison in Figure 4 is confounded by the model. The caption says that four countries (Japan, South Korea, Brazil and Peru) use Llama-4-Maverick and "the rest use GPT-4o-mini."[^c6] The per-country differences therefore mix language with model.
- The native condition also changes the language of the content. It is defined as "native-language simulations (agents reading and writing posts in native languages)."[^c7] My inference: the calibration condition does not separate the language of the prompt from the language of the posts the agents see, so the effect cannot be attributed to the persona prompt alone.
- The paper reports that alignment "varies markedly across models and between native and English prompting of the same" population.[^c8] One model was then chosen as the best performer for later experiments.[^c13] My inference: that choice rests on the same calibration data, so the language effect is shown for that model and a limited set of countries.
- The personas are approximate. The authors say the simulated users are "inherently approximate simulacra of real-world users rather than faithful representations."[^c9] They cite prior work that "demographic attributes alone have limited power in aligning LLM role-playing with" human opinions, and they leave belief-level information to future work.[^c11]
- The sample is small: "our simulations use 100 agents due to".[^c14] The text read reports point differences in Figure 4 and does not report intervals for them, so the size of each per-country gap is not established.

## Related

- [[simulated-respondent-variance-deficit]] — persona-conditioned respondents match item means but spread less across people; respondent language moves the means, and the spread was not measured in this paper
- [[narrative-over-demographic-persona-conditioning]] — which person-level content moves simulated answers toward a given person's survey answers; a second lever on the same respondent, judged by agreement rather than by distribution error
- [[monolingual-query-document-alignment]] — multilingual retrievers also prefer material in the query's own language; a parallel preference for the native language, in a different task, and not the same measurement

[^c1]: arxiv-2512-07195 — "a native language is assigned to each interviewee"
[^c2]: arxiv-2512-07195 — "native-language simulation matches the real distributions more closely in 13 of the 21 countries"
[^c3]: arxiv-2512-07195 — "native-language prompting activating culture-specific perspectives that English suppresses"
[^c4]: arxiv-2512-07195 — "so these small gaps are a weak test"
[^c5]: arxiv-2512-07195 — "RMSE ranges from 0 (perfect match)"
[^c6]: arxiv-2512-07195 — "the rest use GPT-4o-mini"
[^c7]: arxiv-2512-07195 — "native-language simulations (agents reading and writing posts in native languages)"
[^c8]: arxiv-2512-07195 — "varies markedly across models and between native and English prompting of the same"
[^c9]: arxiv-2512-07195 — "which are inherently approximate simulacra of real-world users rather than faithful representations"
[^c10]: arxiv-2512-07195 — "persona-to-opinion mapping operates at the country level rather than the individual level"
[^c11]: arxiv-2512-07195 — "demographic attributes alone have limited power in aligning LLM role-playing with"
[^c12]: arxiv-2512-07195 — "native-language simulation better reflects real survey data than English-only simulation"
[^c13]: arxiv-2512-07195 — "we choose the best-performer, Llama-4-Maverick, for"
[^c14]: arxiv-2512-07195 — "our simulations use 100 agents due to"
