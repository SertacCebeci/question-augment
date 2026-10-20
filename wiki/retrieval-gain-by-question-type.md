---
description: "Retrieval lifts a model's accuracy on questions whose answer is an entity fact absent from its parameters far more than on questions needing reasoning over facts it already holds."
aliases: ["factual versus contextual retrieval gain", "entity-recall versus reasoning split in RAG", "division of labor between retrieval and parameters"]
sources: ["arxiv-2512-05430"]
---
# Retrieval gain by question type

Retrieval augmentation is usually reported as one accuracy number. ArtistMus divides its questions into two kinds and reports the gain for each. Factual questions "target verifiable details such as dates, names, and events, whereas contextual questions require reasoning or synthesis across multiple pieces of information within the passage."[^c1] Each artist gets one question of each kind, both in multiple-choice form.

The mechanism the authors give concerns where the missing piece lives. Factual questions "often require precise entity recall (e.g., album names) that are absent from model parameters but directly retrievable from passages."[^c2] If the model does not hold the entity, reasoning does not recover it; a passage that holds it can supply it. Contextual questions ask the model to combine information it is given, and the paper's view is that the model already has the capacity for this once the facts are present. The consequence is put as "a division of labor: retrieval provides facts, while model parameters handle reasoning."[^c3]

The measured effect is lopsided, and the zero-shot baseline already shows the asymmetry: "Across all models, factual questions were notably more challenging than contextual ones."[^c4] With BM25 retrieval over the music Wikipedia index, the gain follows the same line: "The substantial factual accuracy gains from RAG (+40.4 pp on average) contrast with modest contextual improvements (+4.8 pp on average)."[^c5]

What the answerer gains from retrieval therefore depends on the kind of thing it lacks. If the missing item is a fact the model cannot produce from memory and a source can hand over, retrieval helps a great deal. If the missing item is a relation to be worked out from text already in view, the added passages add little, because the reasoning was never the bottleneck. This is a boundary about evidence, not about how hard a question looks. The same test appears in [[structural-versus-parametric-evidence]], where a tool over a musical score helps only when the fact lies in the object. Here the object is a text index rather than a notation. The ArtistMus paper does not connect the two; the link is my reading.

## Limits

- The split is the generator's own classification. GPT-4o wrote both kinds of question: "To construct these questions, we provided GPT4o" with the section text.[^c6] Validation checked music relevance and faithfulness to the passage. The text does not show that the contextual items need reasoning rather than some other kind of lookup, so the label "contextual" is a description of the generator's output, not a measured difficulty.
- The contextual baseline is near ceiling. For the Llama 3.1 8B model the zero-shot pair is "(39.0% / 84.8%)" for factual and contextual accuracy.[^c7] A small contextual gain from retrieval may reflect the ceiling rather than a finding that retrieval is useless for reasoning. This reading is mine.
- The main results come from one corpus (MusWikiDB, built from Wikipedia), mostly one first-stage retriever (BM25), and one benchmark of 500 artists per question type. The out-of-domain benchmark is not split by type: "For TrustMus, evaluation was conducted across four categories."[^c8] The split has no out-of-domain test in the text.
- The format is multiple choice. The paper says its benchmark "does not capture all aspects of music question answering"[^c9] and names "questions requiring multi-hop reasoning" among the excluded kinds.[^c10] A multi-hop question would test the boundary more sharply, since retrieval might supply each entity while the chaining stays with the model. That case is not measured here.
- "Division of labor" is the authors' reading of a gap between two averages. No experiment gives a model facts and reasoning tasks separately to isolate which component does what.

## Related

- [[structural-versus-parametric-evidence]] — the same boundary between evidence in the object and evidence in the reasoner, drawn there for a tool over a score
- [[two-stage-reranking]] — the second retrieval stage, which in this paper helped both question types and not only the factual one

[^c1]: arxiv-2512-05430 — "Factual questions target verifiable details such as dates, names, and events, whereas contextual questions require reasoning or synthesis across multiple pieces of information within the passage."
[^c2]: arxiv-2512-05430 — "Factual questions often require precise entity recall (e.g., album names) that are absent from model parameters but directly retrievable from passages."
[^c3]: arxiv-2512-05430 — "This suggests a division of labor: retrieval provides facts, while model parameters handle reasoning."
[^c4]: arxiv-2512-05430 — "Across all models, factual questions were notably more challenging than contextual ones."
[^c5]: arxiv-2512-05430 — "The substantial factual accuracy gains from RAG (+40.4 pp on average) contrast with modest contextual improvements (+4.8 pp on average)"
[^c6]: arxiv-2512-05430 — "To construct these questions, we provided GPT4o"
[^c7]: arxiv-2512-05430 — "Compared to the zero-shot baseline (39.0% / 84.8%)"
[^c8]: arxiv-2512-05430 — "For TrustMus, evaluation was conducted across four categories"
[^c9]: arxiv-2512-05430 — "does not capture all aspects of music question answering"
[^c10]: arxiv-2512-05430 — "questions requiring multi-hop reasoning"
