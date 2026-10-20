---
description: "Choosing few-shot exemplars by semantic similarity to the test item does not reliably beat choosing them at random from the same pool, across models and clinical tasks."
aliases: ["KNN few-shot selection", "kNN dynamic few-shot", "similarity-based demonstration selection", "semantic exemplar retrieval for prompts"]
sources: ["arxiv-2512-22966", "arxiv-2512-19247", "arxiv-2512-12175", "arxiv-2512-09627", "arxiv-2512-04106", "arxiv-2511-19858", "arxiv-2511-15986"]
---
# Similarity-selected exemplars

A few-shot prompt is built from worked examples. One way to fill it is to take, for each test item, the stored examples whose embeddings are nearest to it (a K-nearest-neighbour rule). The intuition is that a close analogue carries the right content, so the model copies the right reasoning. The alternative is to draw the same number of examples at random from the same pool. The two differ only in the selection rule, so a comparison between them isolates whether similarity is doing work.

In the clinical benchmark, the selection rule was the only thing swapped between two otherwise identical variants of the MedPrompt package. Both drew three examples from a training pool of cases whose self-generated chain-of-thought had reached the correct answer. The KNN variant: "Three few-shot examples were then selected for each test question based on cosine similarity." The random variant: "the examples from the training dataset for each test question were selected randomly" (the random variant, drawn from the same pool).[^s1] The result was not a uniform winner. "KNN dynamic few-shot prompting did not consistently outperform random few-shot prompting."[^s2] Similarity helped in some cells: relevant diagnostic testing for ChatGPT-4o rose "from 30.8% to 50.7%" with KNN examples.[^s3] Random selection did better in others, and the one case where a model lost ground on relevant testing was "Gemini 2.5 Flash with random few-shot prompting."[^s4] The mixed direction is what matters: no selection rule won across models and tasks.

The authors' explanation is that similarity is not automatically the right criterion: "relying solely on semantic similarity to select few-shot examples may not always yield the best results for model performance."[^s5] Their conjecture is that "the presumed advantage of closely matched examples" can be offset by "the loss of broader contextual diversity or alternative reasoning strategies."[^s6] This is an account of the pattern, not something they isolate. The transferable point is that a retrieval rule for demonstrations is an assumption about what the model needs from them, and that assumption can fail.

A different comparison points the other way, though it is not the same test. In a logistics frame-detection study, exemplars retrieved by semantic similarity were set against a hand-written fixed set of the same size, and the retrieved set won: "GPT-4o mini improves from 83% (manual) to 88% (RAG-6-shot)".[^s7] "Manual 6-shot prompts generally underperform."[^s8] The authors read this as "selects more relevant demonstrations than handcrafted examples."[^s9] The contrast is fixed versus retrieved, not similarity versus chance, so it does not contradict the clinical result. It shows that a fixed hand-picked set can be the weaker option, which is a narrower claim than that similarity is the useful ingredient.

A code task gives the same kind of comparison a different outcome. Trad and Chehab set random few-shot examples against retrieved ones on a multi-label vulnerability task, with both arms drawn from the training data: the random arm is "sampled from the training pool for each test sample."[^s14] The retrieval arm ranks stored examples by embedding similarity, "which supports efficient cosine" search.[^s19] With Gemini-1.5-Flash, the retrieved arm leads on micro F1 at ten shots: "reaching 71.43% at 10 shots" against "Random Prompting follows at 65.69%."[^s15][^s16] The authors call the advantage consistent across metrics and shot counts,[^s17] and read it as "carefully selected in-context examples provide more informative" guidance.[^s18] The clinical null is therefore not general. One model and one task per side cannot say which conditions decide the sign.

In medical error detection on the MEDEC benchmark, the same swap shows a gain with the count held fixed (see [[in-context-example-count]]). The task asks a model whether a clinical note contains an error, which sentence holds it, and how to correct it. The retrieval arm takes "the n most semantically similar training cases to the input clinical note" and appends them to the zero-shot instructions.[^s24] The static arm appends "n randomly sampled exemplars from the training set" to the same instructions.[^s25] At one shot the retrieved arm wins, and the authors read the gap as "demonstrating that exemplar quality matters even when exemplar count is held constant."[^s26] Random exemplars added little from one shot to ten: "SPR ten-shot provided only modest additional improvements."[^s29] With ten retrieved exemplars, "nearly all models demonstrated consistent improvements" across the three subtasks, and GPT-4.1's error sentence detection rose "from 67.1% to 70.4% (+3.3 points)."[^s27][^s28] Retrieval also lowered false flags: "RDP ten-shot yielded the lowest FPR overall."[^s30]

## Limits

- One exemplar count (three) and one embedding model were used. No sweep over K, over embedding models, or over pool size was reported.
- The pool was about 30% of each task's cases, so pool size differed by task. For essential immediate steps the pool was very small (the study has 10 cases for that task). Whether similarity has enough neighbours to help in such pools is my inference, not tested.
- Most pairwise comparisons were not statistically significant: "Only a small number of pairwise comparisons were statistically significant." The directional reading is the finding, not a tested interaction.
- The comparison is against random exemplars from the same pool, not against zero exemplars without the chain-of-thought package. It says nothing about whether exemplars help at all in this setting.
- The contrast is in a closed-form clinical multiple-choice setting. Whether it holds for open-ended tasks or for retrieval over large corpora is not shown.
- The diversity explanation is the authors' conjecture and was not measured.
- The logistics contrast has no random-from-pool arm. Nothing there draws six examples at random from the same pool, so the gain over the hand-written set cannot be credited to similarity itself (my inference from the design).
- The logistics study uses one test set of about 225 messages (my reading of its split table) and reports no repeated runs or spread. Its real-world column is judged by domain experts, which the paper itself calls subjective. The table layout in the extracted text does not line up cleanly with the prose, so only the sentence-level figures above are used (my inference).
- Similarity does not fix label agreement. A transductive reading of ICL argues that the label of the chosen exemplars matters beyond their closeness: "the label consistency is not guaranteed during demonstration selection" under top-K retrieval.[^s10] That paper's accuracy link is correlational and comes from a different setup, so it is a second axis to check against this note's results, not a refutation of them. See [[demonstration-label-consistency]].

- A retriever trained on a different signal, the measured change in the frozen model's error when a candidate is added, beat random and kNN retrieval in three of four few-shot log transfers. The paper's own qualifier is that "the benefit is setting-dependent", and on the one transfer it lost, Random-ICL was ahead.[^s11][^s13] Its target-domain zero-shot runs did not include the kNN or random baselines.[^s12] This is a different domain (log anomaly detection, one frozen LLM), so it adds a comparison, not a replication of the clinical result. See pairwise-demonstration-utility.
- The vulnerability study uses one LLM, one embedding model and four CWE categories, after non-vulnerable functions were excluded: "using the Gemini-1.5-Flash model across three approaches"[^s20] and "we focus on the four specific CWE categories with clear definitions and consistent representation."[^s21] Its stored vectors include the labels, "its associated labels are included,"[^s22] while the query carries none. How much of the retrieved set's gain is label agreement rather than code similarity was not separated (my inference; see [[demonstration-label-consistency]]). The paper says "its stability ensures reproducible" results,[^s23] yet every reported cell is a single value, so the 6-point F1 gap at ten shots has no interval (my reading).
- The random arm is one seeded draw. "Random seeds were fixed across runs."[^s31] The significance test is a paired bootstrap over test items, so the spread across alternative random exemplar sets is not reported (my inference from the design).
- The label mix of retrieved exemplars is not reported. Stored cases carry "the annotated error sentence ID, and the gold-standard correction";[^s32] whether the neighbours share the query's error status is the second axis of [[demonstration-label-consistency]], and the paper does not separate it (my inference).
- Tuning used one model. The count was chosen with GPT-4.1, which "served as the representative system for selecting n";[^s33] the other eight models inherit that choice. Gemini 2.0 Flash "lagged behind across tasks," which the authors tie to retrieval use, "likely because its instruction-tuning and retrieval integration were less" effective.[^s34]

## Related

- pairwise-demonstration-utility — the per-pair score that a retriever is trained on when similarity is not the selection criterion
- [[demonstration-label-consistency]] — the share of exemplars sharing the query's label is a second property that similarity does not control
- [[task-conditional-prompt-gain]] — the same package gains and losses vary by task; the exemplar rule is one lever inside that variation
- [[exemplar-retrieval-grounded-grading]] — retrieving past graded essays as exemplars for grading; a similarity-style use in a different task, with a different claim
- [[instruction-tuning-exemplar-dependence]] — exemplars recover instruction-tuned models; this note concerns which exemplars to pick once some are given
- [[compact-exemplar-scaffold-over-verbose-reasoning]] — a short exemplar fixes label criteria in moral prompting; this note asks how the exemplar should be chosen
- [[retrieval-label-union]] — the same neighbours with no model reading them: copying their labels, which over-predicts as k grows
- [[in-context-example-count]] — the count is the knob this clinical study holds fixed while it swaps the selection rule; that note is about the knob itself
- [[exemplar-demographic-imbalance]] — a retrieval rule can also shift the sensitive-group mix of the exemplars; in a medical-image study the similarity arm had the highest accuracy and the largest ethnicity disparity, and the paper links that disparity to skewed exemplars[^s35][^s36]

[^s1]: arxiv-2512-22966 — "Three few-shot examples were then selected for each test question based on cosine similarity"
[^s2]: arxiv-2512-22966 — "consistently outperform random few-shot prompting"
[^s3]: arxiv-2512-22966 — "the accuracy of ChatGPT 4o for relevant diagnostic testing surged from 30.8% to 50.7%"
[^s4]: arxiv-2512-22966 — "except for Gemini 2.5 Flash with random few-shot prompting"
[^s5]: arxiv-2512-22966 — "relying solely on semantic similarity to select few-shot examples may not always yield"
[^s6]: arxiv-2512-22966 — "by the loss of broader contextual diversity or alternative reasoning strategies"
[^s7]: arxiv-2512-19247 — "GPT-4o mini improves from 83% (manual) to 88% (RAG-6-shot)"
[^s8]: arxiv-2512-19247 — "Manual 6-shot prompts generally underperform."
[^s9]: arxiv-2512-19247 — "selects more relevant demonstrations than handcrafted examples"
[^s10]: arxiv-2512-12175 — "the label consistency is not guaranteed during demonstration selection"
[^s11]: arxiv-2512-09627 — "In the few-shot setting, LogICL outperforms both Random-ICL and kNN-ICL in three of the four transfers"
[^s12]: arxiv-2512-09627 — "Random-ICL and kNN-ICL were not evaluated in this setting"
[^s13]: arxiv-2512-09627 — "although the benefit is setting-dependent"
[^s14]: arxiv-2512-04106 — "sampled from the training pool for each test sample"
[^s15]: arxiv-2512-04106 — "reaching 71.43% at 10 shots"
[^s16]: arxiv-2512-04106 — "Random Prompting follows at 65.69%"
[^s17]: arxiv-2512-04106 — "Overall, Retrieval-Augmented Few-Shot Prompting consistently outperforms both random prompting"
[^s18]: arxiv-2512-04106 — "carefully selected in-context examples provide more informative"
[^s19]: arxiv-2512-04106 — "which supports efficient cosine"
[^s20]: arxiv-2512-04106 — "using the Gemini-1.5-Flash model across three approaches"
[^s21]: arxiv-2512-04106 — "we focus on the four specific CWE categories with clear definitions and consistent representation"
[^s22]: arxiv-2512-04106 — "its associated labels are included"
[^s23]: arxiv-2512-04106 — "its stability ensures reproducible"
[^s24]: arxiv-2511-19858 — "the n most semantically similar training cases to the input clinical note are retrieved and appended to the instructions used in zero-shot prompting"
[^s25]: arxiv-2511-19858 — "n randomly sampled exemplars from the training set, appended to the same instructions used in zero-shot prompting"
[^s26]: arxiv-2511-19858 — "demonstrating that exemplar quality matters even when exemplar count is held constant"
[^s27]: arxiv-2511-19858 — "nearly all models demonstrated consistent improvements"
[^s28]: arxiv-2511-19858 — "error sentence detection accuracy from 67.1% to 70.4% (+3.3 points)"
[^s29]: arxiv-2511-19858 — "SPR ten-shot provided only modest additional improvements"
[^s30]: arxiv-2511-19858 — "RDP ten-shot yielded the lowest FPR overall"
[^s31]: arxiv-2511-19858 — "Random seeds were fixed across runs"
[^s32]: arxiv-2511-19858 — "the annotated error sentence ID, and the gold-standard correction"
[^s33]: arxiv-2511-19858 — "served as the representative system for selecting n"
[^s34]: arxiv-2511-19858 — "likely because its instruction-tuning and retrieval integration were less"
[^s35]: arxiv-2511-15986 — "the highest accuracy (65.3%) but also the largest Ethnicity"
[^s36]: arxiv-2511-15986 — "demographic skew from exemplars to model predictions"
