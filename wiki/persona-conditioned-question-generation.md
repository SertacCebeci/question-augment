---
description: "Conditioning question generation on a sampled asker profile (profession and goal) gave more mutually different questions, better matched to each profile, than unconditioned generation."
aliases: ["persona-based suggested questions", "personalized question generation", "profile-conditioned question generation"]
sources: ["doi-10-48550-arxiv-2412-12445"]
---
# Persona-conditioned question generation

Suggested questions are the first thing a reader sees when a document opens in an AI reading tool. A generator that sees only the document tends to return the same questions whoever is reading. Persona-SQ changes the input rather than the generator: it adds a profile of a likely asker, a profession and a set of reading goals, and generates questions under that profile. The profile is "synthetically injecting user profile information, in the form of their" profession and goals into the generation.[^p1]

The pipeline is a chain of generations with filters. An LLM proposes professions for each document, and a second LLM pass merges near-duplicate professions such as "accountants" and "financial accountants." Goals are scored for how likely that persona would pursue them, and "Goals scoring below 4 are" eliminated. Five goals are then drawn at random for each persona-document pair.[^p2] Questions are generated per persona, and "whose scores are below 4 are excluded" after a judge scores each question for relevance to the persona and to the document.[^p3]

The claim the paper tests is that the profile moves the questions. It measures this in two ways. The first is semantic diversity: cosine similarity between questions generated for different personas on the same document, where the result is that "incorporating personas leads to more differentiated questions targeting" different interests.[^p4] The second is question-persona alignment, a coverage ratio computed with a reverse-ranking step in which an LLM "ranks personas based on their relevance to each" generated question, and the score is how often the intended persona comes out on top. Persona-conditioned questions "achieve significantly higher coverage ratios compared to" the unconditioned baseline.[^p5]

The same pipeline, run with GPT-4o over 250 documents, was reported to produce questions that are "more diverse and higher quality" than the baseline.[^p6] The paper then uses the generated data to fine-tune models of 360 million parameters, which "outperform models fine-tuned on an SQ dataset without persona" in its evaluations.[^p7]

My reading, not the paper's: a sampled profile works as a source of variation that the document alone does not supply. The generator's most likely question about a document is roughly the same for every call. A profile changes which part of the document the likely question comes from, so different profiles reach different parts. The paper does not isolate this mechanism; it shows the outcome on two metrics.

## Limits

- The profiles are not real users. The authors say that "Persona-SQ uses synthetically generated personas" and that this "does not yet achieve true personalization."[^p8] Whether a sampled profession and goal match what a real reader wants is not tested.
- The diversity metric is embedding cosine similarity, which measures difference in wording and topic, not whether two questions would be useful to different readers. Two questions can differ in embedding and still ask for the same thing. The paper does not check this.
- The coverage ratio depends on an LLM ranker. I did not find a report of whether the ranker shares a model family with the generator; if it does, the alignment score could partly reflect shared phrasing habits. This is my concern, not a result of the paper.
- The human evaluation is on "evaluation on a small set of documents in Section," so the quality claim rests mainly on an LLM judge and automatic metrics.[^p9]
- The corpus is three domains (finance, legal and academia). Other reading domains, and single-document use, where the corpus-level steps are dropped, are not measured.
- The pipeline adds cost: the paper notes that it "introduces additional computation from persona generation and multiple quality control steps."[^p10]

## Related

- [[persona-inference-before-ask-answer]] — the reverse direction: an inferred persona conditions the ask-or-answer decision, while here a sampled persona conditions which questions are produced
- [[narrative-over-demographic-persona-conditioning]] — a persona prompt that conditions a simulated respondent's answers; here the persona conditions the asker's questions, and its content is profession and goal, not interview material
- [[user-response-persona-simulation]] — the simulated-user side of the same synthetic-persona problem: the persona is written by a generator, so recovery of real users is not shown

[^p1]: doi-10-48550-arxiv-2412-12445 — "by synthetically injecting user profile information, in the form of their"
[^p2]: doi-10-48550-arxiv-2412-12445 — "randomly select five goals from the refined goal"
[^p3]: doi-10-48550-arxiv-2412-12445 — "whose scores are below 4 are excluded"
[^p4]: doi-10-48550-arxiv-2412-12445 — "incorporating personas leads to more differentiated questions targeting"
[^p5]: doi-10-48550-arxiv-2412-12445 — "questions generated by Persona-SQ achieve significantly higher coverage ratios compared to"
[^p6]: doi-10-48550-arxiv-2412-12445 — "consistently produces more diverse and higher quality SQs than"
[^p7]: doi-10-48550-arxiv-2412-12445 — "using the Persona-SQ dataset outperform models"
[^p8]: doi-10-48550-arxiv-2412-12445 — "does not yet achieve true personalization"
[^p9]: doi-10-48550-arxiv-2412-12445 — "evaluation on a small set of documents in Section"
[^p10]: doi-10-48550-arxiv-2412-12445 — "introduces additional computation from persona generation and multiple quality control steps"
