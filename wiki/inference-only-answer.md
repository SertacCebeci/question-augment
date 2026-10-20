---
description: "An answer is inference-only when its direct supporting fact is removed from the KG but rule-derivable paths to it remain, so recovering it measures reasoning rather than lookup."
aliases: ["hard answer", "answer under removed direct support", "incomplete-KG answerability"]
sources: ["arxiv-2512-14766"]
---
# Inference-only answer

Benchmarks for knowledge-graph question answering have usually been built on a complete graph. Every question then has its answer stated as a direct triple, and answering reduces to finding that triple. The GR-Agent paper puts the problem this way: "current datasets are constructed under the assumption that the KG is complete, i.e., every question has direct supporting triples in the KG".[^c1] The construction it proposes changes what the question tests. For each question the direct triple is deleted, so the answer can be reached only through other facts: "the direct supporting triples are removed from the KG, ensuring that the answer can only be inferred via high-confidence logical rules rather than shallow retrieval."[^c2]

The mechanism has three steps. First, high-confidence Horn rules are mined from the graph, "mining high-confidence Horn rules [Horn, 1951] from the original KG using the AMIE3 algorithm".[^c3] A rule has the form body ⇒ head, so that a set of facts implies one more fact. Second, for each rule up to 30 groundings are chosen where the body and the head both exist. The head triple is removed, and every body triple is kept: "The head triple is then removed while preserving all body triples, ensuring that each removed fact remains inferable and that no body triple required for other groundings is lost."[^c4] A question is then written from the removed triple. Third, the gold answers are the full set the original graph supports, and an answer whose direct support was removed is marked as needing inference: "mark the answers requiring inference (i.e., without direct supporting triples) as".[^c5]

The measure is what turns this into a test. The Hard Hits Rate "measures the fraction of correctly answered questions (i.e., Hits@Any) that include" the hard answer.[^c6] The paper reports that this rate "remains modest": a model can answer a question correctly and still miss the answer whose support was removed.[^c7] Training-free baselines are described as those that "degrade sharply once direct support triples are absent", while the proposed agent keeps a higher rate by following alternative paths.[^c8] The pattern the note carries is general: delete a conclusion, keep its premises, and a score on that conclusion says whether the answerer re-derived it or looked it up.

## What transfers

The rule-mining formalism comes from logic and knowledge-base mining. What survives the move to question writing is the pattern itself. If the premises of an answer remain and its direct form is absent, then an answer that is recovered is evidence of inference, not of retrieval. What does not survive automatically is the guarantee. A mined rule is a statistical regularity of one graph, not a proof that the answer is true. My inference: the same deletion idea could apply to any question source that carries explicit inference rules, but the paper tests only knowledge graphs.

## Limits

- The answerability guarantee holds only relative to the mined rules and the original graph. The gold set is "a complete set of correct answer entities derived from the original"[^c9] graph. An answer the original graph lacks is not counted, and a rule's confidence is a count over that same graph.
- Questions are written by an LLM from the removed triple: "For each removed triple, we prompt GPT-4"[^c10] to generate the question. The text reports no human check that these questions are natural, unambiguous, or answerable only through the intended path. That is untested here.
- The measure is conditional. The Hard Hits Rate is computed over correctly answered questions, so it says nothing about questions a method fails outright.[^c11]
- Two graphs (Family and FB15k-237) and one proposed method are tested. The claim that earlier deletion schemes, random or along shortest paths, "often leaves questions unanswerable" is made in related work and is not measured in this text.[^c12]
- The paper is a workshop contribution: "39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Scaling Environments".[^c13] The authors describe the work as "ongoing".[^c14]
- Whether an inference-only answer is the right thing for a human asker to want is not addressed. The note records what the construction measures, not that a question should be built this way.

## Related

- [[reverse-constructed-indirect-question]] — also builds a question from a source and removes a handle a search would use; here the removed item is the answer's own triple, and the path to it is kept.
- [[evidence-chain-question-generation]] — also makes the chain explicit before the question is written; there the chain is a requirement on the question, here it is what remains after deletion.
- [[evidence-forgetting-rate]] — also separates retrieval from use; that metric conditions on retrieved golden evidence, while this construction removes the direct evidence itself.

[^c1]: arxiv-2512-14766 — "current datasets are constructed under the assumption that the KG is complete, i.e., every question has direct supporting triples in the KG"
[^c2]: arxiv-2512-14766 — "the direct supporting triples are removed from the KG, ensuring that the answer can only be inferred via high-confidence logical rules rather than shallow retrieval"
[^c3]: arxiv-2512-14766 — "mining high-confidence Horn rules [Horn, 1951] from the original KG using the AMIE3 algorithm"
[^c4]: arxiv-2512-14766 — "The head triple is then removed while preserving all body triples,"
[^c5]: arxiv-2512-14766 — "mark the answers requiring inference (i.e., without direct supporting triples) as"
[^c6]: arxiv-2512-14766 — "measures the fraction of correctly answered questions (i.e., Hits@Any) that include"
[^c7]: arxiv-2512-14766 — "Across both datasets, the HHR remains modest"
[^c8]: arxiv-2512-14766 — "While other training-free approaches degrade sharply once direct support triples are absent"
[^c9]: arxiv-2512-14766 — "a complete set of correct answer entities derived from the original"
[^c10]: arxiv-2512-14766 — "For each removed triple, we prompt GPT-4"
[^c11]: arxiv-2512-14766 — "measures the fraction of correctly answered questions (i.e., Hits@Any) that include"
[^c12]: arxiv-2512-14766 — "but this often leaves questions unanswerable, conflating missing knowledge with model reasoning limits."
[^c13]: arxiv-2512-14766 — "39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Scaling Environments"
[^c14]: arxiv-2512-14766 — "This work is ongoing."
