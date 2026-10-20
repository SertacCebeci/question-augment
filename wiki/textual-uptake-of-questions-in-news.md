---
description: "In 1.2M French news articles, about 96% of interrogative sentences are followed by an answer-like span in the same article, mostly written by the journalist, not quoted; a heuristic upper bound."
aliases: ["answerability of interrogatives", "local textual uptake", "dialogicity of questions", "interrogative stance in news"]
sources: ["arxiv-2603-21823"]
---
# Textual uptake of questions in news

Written news questions are not left hanging. Bros et al. (2026) detect interrogative sentences in over a million French-language articles (2023 to mid-2024), type them into six stances (framing-procedural, information-seeking, echo-clarification, rhetorical, leading, tag), and search the rest of the article for an answer-like span. The answer search embeds sentences with CamemBERT, groups consecutive questions into one local issue, looks only at later sentences, and accepts the best contiguous span above a similarity threshold.[^c1]

## What was measured

- Uptake: 760,182 sentences were classified interrogative, and 726,911 of them got a later answer-like span in the same article, a 95.6% rate. The authors call it an upper bound on answerhood, not verified resolution.[^c2]
- By stance: information-seeking and echo-clarification questions match most often (97.2% and 97.4%), framing-procedural least (94.8%), and rhetorical, leading and tag questions sit near 95%.[^c3] So even evaluative or rhetorical questions are usually embedded in local question-answer sequences (see [[rhetorical-question]]).
- Voice of the answer: 4.4% of interrogatives stay unanswered, 80.3% are answered by the journalist in narrative text, and 15.4% through direct quotes or marked reported speech.[^c4] Quoted-source answers are commoner in Swiss and Belgian outlets (about 18%) and hyper-local outlets (20%) than in thematic verticals (about 13%).[^c5]
- Prevalence and function: interrogatives are sparse; framing-procedural questions make up around half to two-thirds of them across topics. Question-saturated domains are sports, local news and lifestyle. Rhetorical and leading questions are somewhat more frequent in politics and geopolitics.[^c6]
- Who is named: interrogative contexts are dense with named persons, organizations and places and thin on publics, which the authors read as personalization. Senegalese outlets show the highest share of questions mentioning a person (68.1%).[^c7]

A framing-procedural question works as a macro-structuring device: a Canadian explainer is built on a sequence of questions each followed by a short answer, and a single lone question can hinge a commentary toward evaluation.[^c8]

## Why it matters for asking and answering

The finding is that, in written discourse, the asker usually answers their own question. The question organizes the text and the answer follows within a few sentences. Unanswered "orphan" questions are a small residue, often suggestion-like (my reading of the authors' ashtray example).[^c9]

## Limits

- The 95.6% rate comes from semantic similarity, not from judged resolution. The threshold barely matters (unchanged from 0.05 to 0.80), which also suggests the measure is lenient.[^c10]
- A manual audit of 50 question groups found clear or partial local answers in 34 of 40 predicted-answered cases and confirmed all 10 predicted-unanswered ones; that is a small sample.[^c11]
- Classifier quality against human gold labels is modest: interrogative detection F1 0.78, six-way stance macro-F1 0.51, which the authors treat as adequate for corpus-level claims only, not sentence-level ones.[^c12]
- One language (French), one genre (digital news), one period. Whether the self-answering share holds for English, interviews, or human-to-LLM dialogue is untested here.
- Causal claims about power or gatekeeping are interpretive; the paper shows distributions, not effects on readers.

## Related

- [[rhetorical-question]] — a stance type here; the formal account explains why it still often gets answered in text
- [[conclusive-answer]] — a separate notion of what counts as an answer that settles a question

[^c1]: arxiv-2603-21823 — "search only"
[^c2]: arxiv-2603-21823 — "corresponding to a 95.6% rate of heuristic local textual uptake"
[^c3]: arxiv-2603-21823 — "framing-procedural questions the lowest (94.8%)"
[^c4]: arxiv-2603-21823 — "80.3% are answered internally by the journalist in narrative text"
[^c5]: arxiv-2603-21823 — "hyper-local outlets have the highest external"
[^c6]: arxiv-2603-21823 — "rhetorical and leading"
[^c7]: arxiv-2603-21823 — "Senegalese outlets have the highest personalization index (68.1% of questions mentioning at least one person)"
[^c8]: arxiv-2603-21823 — "Even in low-interrogative"
[^c9]: arxiv-2603-21823 — "A minority of “orphan” questions nonetheless remain."
[^c10]: arxiv-2603-21823 — "answerability is unchanged for cosine thresholds"
[^c11]: arxiv-2603-21823 — "a manual audit"
[^c12]: arxiv-2603-21823 — "the six-way stance classifier macro-F1 of 0.51"
