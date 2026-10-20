---
description: "A retrieve-or-not gate trained on features computed before inference, such as entity popularity, graph counts and question type, instead of the answering LLM's own uncertainty."
aliases: ["LLM-independent adaptive retrieval", "external-information retrieval gate", "pre-computed feature retrieval trigger"]
sources: ["doi-10-48550-arxiv-2505-04253"]
---
# LLM-independent retrieval gate

A retrieve-or-not decision can be made from features that are looked up or pre-computed, so the answering model is never asked for an uncertainty signal. The paper trains a classifier on each group of such features to predict whether retrieval is needed: "to train a classifier to predict retrieval needs"[^c1]. The features are organized into seven groups, with 27 features in all.[^c2]

The groups carry different kinds of evidence about the question and the entities it names:

- **Graph**: the minimum, maximum and mean number of knowledge-graph triples per subject and object, for the entities in the question.[^c3]
- **Popularity**: "Popularity features include the minimum, maximum, and mean number of Wikipedia page views" per entity in the question.[^c4]
- **Knowledgability**: a score per entity "reflecting the LLM’s verbalized uncertainty about its knowledge."[^c5] The scores are computed in advance for entities in the Wikidata knowledge graph, so "retrieval decisions can be made without querying the LLM at inference time."[^c6]
- **Question type**: probabilities over "nine categories: ordinal, count, generic, superlative, difference, intersection, multihop, comparative, and yes/no."[^c7]
- **Question complexity**: "Question Complexity reflects the difficulty of a" question, counted in the reasoning steps it requires.[^c8]
- **Context relevance**: "Context Relevance features include the minimum, maximum and mean probabilities that a context is relevant to the question", along with the context length.[^c9]

Frequency features (corpus counts of the entities and of the rarest n-gram in the question) form a seventh group. Hybrids combine the groups; one of them drops frequency and popularity because they are "correlated with graph features."[^c10]

## Mechanism

What makes the gate LLM-independent is where its inputs come from. The features are lookups or classifiers that run before the answering model. The paper says: "Since external information features are pre-computed, no" additional LLM call "are required during inference."[^c11] The uncertainty baselines pay for their gate in calls: the efficiency metric LM Calls counts "the average number of LLM calls per question, including uncertainty estimation."[^c21]

## What was measured

On six QA datasets, using LLaMA 3.1-8B-Instruct with BM25 retrieval, "at least one external feature matches the performance of" the uncertainty estimation methods on each dataset.[^c12] External features "significantly reduce LLM calls"[^c13], at the cost of "slightly more conservative" behaviour with more retrieval calls, still fewer than the multi-step methods.[^c14] The authors claim that "Our approach outperforms uncertainty-based methods for complex" questions.[^c15]

The split between the two families depends on the dataset. On the simple TriviaQA set the top features are uncertainty-based; on the complex sets question type and context relevance rise.[^c16] The paper reads the two families as substitutes rather than complements: "hybrids with uncertainty features do not outperform any external feature combinations", so adding the uncertainty signal to the external one adds nothing measured.[^c17]

## Relation to the wiki

The gate idea is the same as in [[uncertainty-guided-retrieval-triggering]]: retrieve only when the question calls for it. What changes is the signal. There the signal is the answerer's own likelihood; here it is a property of the question and its entities. My inference, not the paper's claim: the frequency group is the same kind of corpus-count signal that [[corpus-statistics-retrieval-trigger]] uses, though the paper counts a reference collection rather than a pre-training corpus.

## Limits

- One answering model and one retriever. "Our study focuses on the LLaMA3.1-8BInstruct model"[^c18], with "the BM25 retriever"[^c20]. Dense retrieval and other architectures were not tested.
- Six QA datasets, scored by InAccuracy, which checks whether the output contains the gold answer.[^c19] Nothing here on long-form answers or on tasks without a short gold answer.
- "LLM-independent" describes the gate, not the system. The knowledgability group is built from an LLM's verbalized uncertainty, computed once offline, and the answer is still produced by the LLM. Whether the table goes stale when the answering model changes is my inference, not tested.
- Popularity and graph features are tied to Wikipedia page views and Wikidata triples. Whether they carry any signal over a private corpus is my inference and was not measured.
- "Outperforms ... for complex questions" is the authors' summary. This reading did not check the per-dataset table behind it.
- Because frequency and popularity are correlated with graph features, the gain from the full feature set is not separated cleanly from the gain of any one group.

## Related

- [[uncertainty-guided-retrieval-triggering]] — the LLM-based gate whose signal this note replaces with question-side features
- [[corpus-statistics-retrieval-trigger]] — another model-free retrieve-or-not gate, using pre-training corpus counts
- [[recoverability-aware-selective-escalation]] — uses a rule-assigned question type as one of several no-LLM features, but after a first retrieve-and-answer pass rather than before it

[^c1]: doi-10-48550-arxiv-2505-04253 — "to train a classifier to predict retrieval needs"
[^c2]: doi-10-48550-arxiv-2505-04253 — "information features, encompassing 27 features, for LLM-independent adaptive retrieval."
[^c3]: doi-10-48550-arxiv-2505-04253 — "entities in question from a knowledge graph, including the minimum, maximum, and mean number of"
[^c4]: doi-10-48550-arxiv-2505-04253 — "Popularity features include the minimum, maximum, and mean number of Wikipedia page views"
[^c5]: doi-10-48550-arxiv-2505-04253 — "reflecting the LLM’s verbalized uncertainty about its knowledge."
[^c6]: doi-10-48550-arxiv-2505-04253 — "querying the LLM at inference time."
[^c7]: doi-10-48550-arxiv-2505-04253 — "nine categories: ordinal, count, generic, superlative, difference, intersection, multihop, comparative, and yes/no."
[^c8]: doi-10-48550-arxiv-2505-04253 — "Question Complexity reflects the difficulty of a"
[^c9]: doi-10-48550-arxiv-2505-04253 — "Context Relevance features include the minimum, maximum and mean probabilities that a context is relevant to the question"
[^c10]: doi-10-48550-arxiv-2505-04253 — "correlated with graph features."
[^c11]: doi-10-48550-arxiv-2505-04253 — "Since external information features are pre-computed, no"
[^c12]: doi-10-48550-arxiv-2505-04253 — "at least one external feature matches the performance of"
[^c13]: doi-10-48550-arxiv-2505-04253 — "External features significantly reduce LLM calls, addressing a key efficiency bottleneck that worsens with LLM scaling."
[^c14]: doi-10-48550-arxiv-2505-04253 — "they lead to slightly more conservative"
[^c15]: doi-10-48550-arxiv-2505-04253 — "Our approach outperforms uncertainty-based methods for complex"
[^c16]: doi-10-48550-arxiv-2505-04253 — "Figure 2 shows that for the simple TriviaQA dataset, the Top-5 features are uncertaintybased"
[^c17]: doi-10-48550-arxiv-2505-04253 — "hybrids with uncertainty features do not outperform any external feature combinations"
[^c18]: doi-10-48550-arxiv-2505-04253 — "Our study focuses on the LLaMA3.1-8BInstruct model"
[^c19]: doi-10-48550-arxiv-2505-04253 — "We evaluate model performance using six"
[^c20]: doi-10-48550-arxiv-2505-04253 — "the BM25 retriever (Robertson et al.,"
[^c21]: doi-10-48550-arxiv-2505-04253 — "LM Calls (LMC) – the average number of LLM calls per question, including uncertainty estimation."
