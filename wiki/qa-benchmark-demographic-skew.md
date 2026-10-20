---
description: "Popular QA and reading-comprehension benchmarks skew male, Christian and North-American/Western European in the entities their questions mention, and their papers rarely report who wrote them."
aliases: ["social bias in QA benchmarks", "benchmark demographic representativeness", "QA dataset content skew"]
sources: ["doi-10-48550-arxiv-2505-15553"]
---
# QA benchmark demographic skew

The questions in a benchmark are a sample of the world, and the sample can be skewed in who and where it mentions. Kraft et al. define a socially biased QA or reading-comprehension benchmark as one with a statistical skew in demographic or geographic identifiers or names in its data, matching pre-existing societal gradients of power. They measure it against a uniform ideal distribution, an assumption they adopt because no benchmark paper stated any other target.[^c1] They read 30 popular benchmark papers and analysed the data of 20 benchmarks. Entities in the data were linked to Wikidata, then gender, religion and location properties were counted. The entity linker reached micro-F1 .73 (precision .63, recall .87) on 50 hand-annotated items per benchmark, so the counts are noisy.[^c2]

**Gender.** Only benchmarks with more than 30 gender entries were plotted. Non-binary genders were none or near none. Wikipedia-based sets such as DROP, SQuAD and TriviaQA show prominent gender gaps, and DROP draws on NFL game summaries.[^c3] Skew also appears where gender is irrelevant to the task. In CommonsenseQA a keyword count found 179 questions with "he", "man" or "his" against 49 with female terms, so creators defaulted to male subjects.[^c4] The most favorable ratios were in HellaSwag and WinoGrande, and WinoGrande was the only benchmark whose paper reported measuring and mitigating bias.[^c5]

**Religion.** Christianity or Catholicism is among the top three religion labels in 14 of 15 benchmarks with enough data.[^c6]

**Location.** Coordinates cluster around North America and Western Europe across encyclopedic, commonsense and scholarly sets. In BoolQ and StrategyQA the most named country is the United States, at 56% and 31%.[^c7] All but one benchmark are English only, and the exception, XQuAD, is translated from English.[^c8]

**Who made them.** Most papers give too little information about the people involved in creation, especially annotators.[^c9] The authors see the Western author affiliations as matching the geographic and linguistic skew, but they could not test the link statistically because annotator demographics were not reported.[^c10]

**Why it matters for questions.** Every benchmark comes with a training split, so the skew affects training as well as evaluation.[^c11] The authors theorize that a skewed set rewards models for biased inference heuristics. They did not test this. A question set therefore needs an explicit target distribution, stated before collection, to be audited against.

## Limits

- The ideal distribution is assumed uniform. The authors concede a skew can match real-world statistics, for example fewer female computer scientists, so "biased" here means "unequal", not "wrong".
- Entity linking is imperfect (precision .63) and depends on Wikidata coverage. Commonsense sets mention few real entities (COPA, under 100), so the per-benchmark counts are small.
- The link from creator demographics to content skew is correlational at best and untested. Harm to model behavior or users is argued, not measured.
- Only English-language, popular benchmarks were studied, and popularity was the selection criterion, not language.

## Related

- [[benchmark-labor-market-misalignment]] — the same audit idea, comparing a benchmark's coverage with an external population (occupations) instead of demographics
- [[subgroup-abstention-gap]] — how model behavior differs across demographic groups at answer time
- [[demographic-conditioned-mirage]] — demographic conditioning of answers, the downstream face of skewed content

[^c1]: doi-10-48550-arxiv-2505-15553 — "uniform ideal distributions in this study"
[^c2]: doi-10-48550-arxiv-2505-15553 — "(precision=.63, recall=.87)."
[^c3]: doi-10-48550-arxiv-2505-15553 — "In fact, DROP is only based on text"
[^c4]: doi-10-48550-arxiv-2505-15553 — "we also ran a keyword matching on its question set and found 179"
[^c5]: doi-10-48550-arxiv-2505-15553 — "The only benchmark that is explicitly"
[^c6]: doi-10-48550-arxiv-2505-15553 — "Christianity and/or Catholicism are among the top-3 religion labels for 14"
[^c7]: doi-10-48550-arxiv-2505-15553 — "and StrategyQA, the most frequently named locations are the United States (56% and 31%) and"
[^c8]: doi-10-48550-arxiv-2505-15553 — "(which is, however, based on translations from English)."
[^c9]: doi-10-48550-arxiv-2505-15553 — "Most benchmark papers analyzed provide insufficient information about those involved in"
[^c10]: doi-10-48550-arxiv-2505-15553 — "due to the lack of transparency in the reports."
[^c11]: doi-10-48550-arxiv-2505-15553 — "the benchmarks presented here come paired with"
