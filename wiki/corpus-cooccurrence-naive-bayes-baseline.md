---
description: "A smoothed Naive Bayes over pretraining-corpus co-occurrence counts of clinical concepts and diagnoses matches LLM accuracy on MedQA diagnosis items, with no clinical model involved."
aliases: ["Frequency-Based Probabilistic Ranker", "FBPR", "frequency-based naive Bayes baseline", "concept-diagnosis co-occurrence scorer"]
sources: ["arxiv-2512-12868"]
---
# Corpus co-occurrence naive Bayes baseline

A multiple-choice answer can be scored by counting, not by reasoning over the case. Take each candidate answer and each concept extracted from the question, count how often they occur together in the text a model was pretrained on, and combine those counts under a Naive Bayes rule. The highest-scoring candidate is the answer. Jia et al. call this the Frequency-Based Probabilistic Ranker (FBPR), and on five-option MedQA diagnosis items it is a small, fully inspectable program.

The pipeline has three stages. First, an external LLM extracts concepts from the scenario: "we prompt the GPT-4o to extract k concise (each" clinical concept, and "The prompt omits any mention of diagnosis" so that the concepts are presenting features rather than labels.[^c1] Second, the counts come from Infini-gram over Dolma or RedPajama: the frequency of each candidate diagnosis and of each candidate-concept pair, with spacing and capitalisation variants added.[^c2] Third, each candidate is scored by summing log-smoothed co-occurrence ratios over its concepts, under the stated assumption: "Assuming concept independence and their conditional independence given each candidate diagnosis".[^c3] The highest score is the chosen diagnosis.

What the count-only method reaches is the point of the paper. On a 719-question diagnosis subset, "We found that Dolma-based FBPR achieved an accuracy (46.7%) substantially above random chance" of 20%, and it "closely matched OLMo Instruct (44.1%)."[^c4] With RedPajama counts, FBPR reaches "on RedPajama (44.5%) and LLaMA 65B (47.0%)."[^c5] The abstract's summary is that FBPR "achieves comparable performance to the corresponding LLMs pretrained on that same corpus."[^c6] My reading, not the paper's: this makes the count-only score a floor that any clinical-QA accuracy should be compared against, since a score that a co-occurrence table already reaches says little about clinical reasoning on its own. The authors frame the baseline more modestly, as "a meaningful performance reference point and a complementary signal for potential hybridization."[^c7]

The two methods are not the same mechanism. Their correct sets barely overlap beyond chance: "Direct LLM inference and FBPR largely get different questions correct, with an overlap only" slightly above random.[^c8] Dolma-based FBPR and OLMo are both correct on 24.8% of questions, against about 20.6% under independence, so "the methods are only mildly correlated."[^c9] The authors read the LLM as exploiting "different mechanisms over the same corpus", which is their inference from these overlaps, not a measured mechanism.[^c10]

## Limits

- The match is accuracy parity on one split: a diagnosis subset of MedQA, five options, two corpus-model pairs. The paper states "Neither is state-of-the-art on this benchmark".[^c11] Whether parity survives on the full benchmark or on stronger models is not tested.
- The method is weaker on the reasoning-heavy part of the same subset. "Dolma-based FBPR correctly identified the most likely diagnosis for 51% of Step 1 questions but only 44.3% of Step 2&3 questions", and the authors offer only a tentative cause: "This difference likely reflects the heavier multi-step reasoning demands of Step 2&3".[^c12]
- Sensitivity to the front end is untested. The concept set comes from GPT-4o under one prompt, and "Our baseline in this work is quite naive", with no synonym or semantic normalisation.[^c13]
- Counts are occurrence-level, not document-level: Infini-gram "returns occurrence-level (rather than document-level)" counts, and document-level co-occurrence was deferred.[^c14]
- The paper does not separate memorised pattern retrieval from reasoning. Its own next step is "developing probes that can better distinguish memorized pattern retrieval from genuine reasoning."[^c15]
- The claim that the test items were absent from the pretraining corpora is taken from the paper: the subset is said to be one "which was not included in Dolma".[^c16]
- The independence assumption is not relaxed in the paper. My inference, not the paper's: correlated concepts (a symptom and the finding that usually comes with it) would be counted more than once, and the paper does not measure how much that moves the ranking.

## Related

- [[answer-option-surface-cue]] — a second route to a keyed answer that bypasses the tested content, here through option wording rather than corpus counts
- [[corpus-cooccurrence-question-ranking]] — the same co-occurrence statistic used to order which questions to ask, not to score answers
- [[corpus-statistics-retrieval-trigger]] — the same Infini-gram counting tool, used to decide when to retrieve rather than to score a candidate

[^c1]: arxiv-2512-12868 — "we prompt the GPT-4o to extract k concise (each"
[^c2]: arxiv-2512-12868 — "the number of co-occurrences of candidate diagnosis d along with extracted concept xi as"
[^c3]: arxiv-2512-12868 — "Assuming concept independence and their conditional independence given each candidate diagnosis"
[^c4]: arxiv-2512-12868 — "We found that Dolma-based FBPR achieved an accuracy (46.7%) substantially above random chance"
[^c5]: arxiv-2512-12868 — "on RedPajama (44.5%) and LLaMA 65B (47.0%)."
[^c6]: arxiv-2512-12868 — "achieves comparable performance to the corresponding LLMs pretrained on that same corpus."
[^c7]: arxiv-2512-12868 — "meaningful performance reference point and a"
[^c8]: arxiv-2512-12868 — "Direct LLM inference and FBPR largely get different questions correct, with an overlap only"
[^c9]: arxiv-2512-12868 — "the methods are only mildly correlated."
[^c10]: arxiv-2512-12868 — "Despite similar accuracy, the LLM appears to exploit different"
[^c11]: arxiv-2512-12868 — "Neither is state-of-the-art on this benchmark"
[^c12]: arxiv-2512-12868 — "likely diagnosis for 51% of Step 1 questions but"
[^c13]: arxiv-2512-12868 — "Our baseline in this work is quite naive"
[^c14]: arxiv-2512-12868 — "which returns occurrence-level (rather than document-level)"
[^c15]: arxiv-2512-12868 — "developing probes that can better distinguish memorized pattern retrieval from genuine reasoning."
[^c16]: arxiv-2512-12868 — "which was not included in Dolma"
