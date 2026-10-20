---
description: "Alternating each reasoning sentence with a retrieval keyed on it lets later hops fetch evidence the question alone cannot reach, measured on four multi-hop QA sets."
aliases: ["IRCoT", "interleaved retrieval with chain-of-thought", "CoT-guided retrieval", "retrieval-interleaved chain-of-thought"]
sources: ["doi-10-48550-arxiv-2212-10509"]
---
# Chain-of-thought-interleaved retrieval

A multi-hop question often cannot be answered by one lookup, because the page that answers the second hop cannot be reached from the question alone. The paper's example is "In what country was Lost Gravity manufactured?". The Wikipedia page retrieved with the question, about the roller coaster itself, "does not mention where Lost Gravity was" manufactured. The model has to infer a company first and then retrieve again with that company's name.[^c1] The authors state the dependence as a loop: "the retrieval and reasoning steps must inform each other". Without retrieved facts a model writes a wrong reasoning step "due to hallucination", and without the first reasoning step the text for the second hop has no clear link to the question, since there is no "even semantic overlap with the question".[^c2][^c3][^c4]

The method, named IRCoT, needs three ingredients: a base retriever, a language model capable of "zero/few-shot Chain-of-Thought (CoT) generation", and a few annotated questions with their reasoning chains and supporting paragraphs.[^c5] Retrieval starts with the question as the query and returns K paragraphs. Two steps then alternate. In the reason step the model writes the next chain sentence from "the question, the paragraphs collected thus far" and the sentences written so far.[^c6] In the retrieve step the newest sentence becomes the query: "use the last CoT sentence as a query to retrieve" more paragraphs, which join the pool.[^c7] The loop ends when the chain reports an answer or a step cap is reached; the whole pool is then returned as the retrieval result.[^c8] A separate reader answers from that pool.[^c9] The mechanism is the feedback the abstract names: "retrieval with CoT and in turn using retrieved" results improve the chain.[^c10]

Measured on open-domain versions of HotpotQA, 2WikiMultihopQA, MuSiQue and IIRC, with 500 sampled test questions per dataset,[^c11] the recall of gold paragraphs among the retrieved set[^c12] at a fixed budget of 15 paragraphs rose over one-step question retrieval. The reported gain is "by 11-21 recall points under a fixedbudget optimal recall setup".[^c13][^c14] With GPT3 (code-davinci-002) the per-dataset gains are 11.3, 22.6, 12.5 and 21.2 points: "For GPT3, this improvement is by 11.3, 22.6,".[^c15] With Flan-T5-XXL they are 7.9, 14.3, 3.5 and 10.2 points: "on HotpotQA by 7.9, on 2WikiMultihopQA".[^c16]

Retrieval gains carried into answers for most sets. With GPT3 the answer gain is absent on IIRC, "despite significantly improved retrieval".[^c17] Factual errors in chain-of-thought fell as well. On 40 questions per dataset, counted by hand, the paper reports that IRCoT reduces "the factual errors over OneR by 50% on HotpotQA".[^c18][^c19] The method also works at small scale: "with even the smallest model (0.2B) is better than" one-step retrieval on recall,[^c20] and "Flan-T5-XL (3B) with IRCoT even outperforms" a one-step pipeline on the 58X larger GPT3, "the 58X larger GPT3 with a one-step questionbased retrieval".[^c21][^c22] The out-of-distribution setting, with demonstrations from one dataset and testing on another, shows the same ordering: "IRCoT retrieval outperforms OneR (Fig. 5), and IRCoT QA".[^c23]

## Limits

- **Scope of data.** Each dataset gives 100 tuning questions and 500 test questions, and the CoT demonstrations were hand-written for "we wrote CoTs for 20 questions for all the" datasets.[^c24] Three of the four corpora were built by the authors from each dataset's own contexts, "we used the associated contexts to construct a", so the open-domain setting is the authors' construction, not a public benchmark.[^c25] The out-of-distribution figures cover only "HQ (HotpotQA), 2W (2WikiMultihopQA), MQ (MuSiQue)".[^c26]
- **Metric.** Recall is taken at a fixed budget of at most 15 paragraphs, "The reported metric can thus be viewed as the fixedbudget optimal recall", and retrieved documents are not ranked: "Note that our retrieved documents are not ranked, making standard information retrieval metrics such as MAP and". Recall here is not comparable to ranked recall@k elsewhere.[^c27][^c28]
- **Factual-error measure.** A hand count over 40 questions per dataset, and "model can generate a wrong answer despite all correct facts": a sound chain can still give a wrong answer, so the error count is not the accuracy.[^c18][^c29]
- **IIRC.** The GPT3 QA result on IIRC does not improve, the one place where the retrieval gain did not carry into answers.[^c17]
- **Model floor.** The method "relies on the base LM to have a zero or" few-shot CoT ability,[^c30] which "is not as common for small LMs (under 20B)", and it "relies on the base LM to support" long inputs.[^c31][^c32] At 0.2B, the answer gain fails: "IRCoT QA outperforms OneR QA for all model sizes except for the smallest".[^c33]
- **Cost.** "IRCoT makes a separate call to an (L)LM for each" chain sentence.[^c34] The authors name "dynamically deciding when to retrieve" as future work, not a tested variant.[^c35]
- **Retriever and reproducibility.** Only BM25 was used as the base retriever,[^c36] so dense retrievers are untested in the paper (my reading of the setup). The GPT3 model "was deprecated" and the authors say reproduction is hard for that reason.[^c37]
- **Comparisons.** The leaderboard-style comparison with other LLM-based open-domain QA systems is flagged by the authors: "Although these are not head-to-head".[^c38]

## Related

- [[knowledge-integration-decay]] — the same loop seen from the other side: when reasoning runs long before a search, the evidence is used worse. Per-sentence retrieval keeps the pre-search reasoning short (my inference; neither work tests the other).
- [[evidence-guided-query-reformulation]] — also revises a multi-hop query from retrieved passages, mixing in the question's own signal; IRCoT revises it from the newest generated reasoning sentence.
- [[self-ask-decomposition]] — an alternative prompt format for the same multi-hop loop, with explicit follow-up questions instead of chain sentences used as queries.
- [[recoverability-aware-selective-escalation]] — IRCoT is one of the routes a router chooses between by predicted F1 and token cost.
- [[structural-amplification-of-query-entity-corruption]] — reports that the IRCoT variants are among the pipelines a small corruption of entity names breaks.

[^c1]: doi-10-48550-arxiv-2212-10509 — "does not mention where Lost Gravity was"
[^c2]: doi-10-48550-arxiv-2212-10509 — "the retrieval and reasoning steps must inform each other"
[^c3]: doi-10-48550-arxiv-2212-10509 — "to generate an incorrect reasoning step due to hallucination."
[^c4]: doi-10-48550-arxiv-2212-10509 — "even semantic overlap with the question"
[^c5]: doi-10-48550-arxiv-2212-10509 — "zero/few-shot Chain-of-Thought (CoT) generation"
[^c6]: doi-10-48550-arxiv-2212-10509 — "use the question, the paragraphs collected thus far"
[^c7]: doi-10-48550-arxiv-2212-10509 — "use the last CoT sentence as a query to retrieve"
[^c8]: doi-10-48550-arxiv-2212-10509 — "We repeat these steps till the CoT reports an answer or we reach the maximum allowed number"
[^c9]: doi-10-48550-arxiv-2212-10509 — "these as the context for answering"
[^c10]: doi-10-48550-arxiv-2212-10509 — "retrieval with CoT and in turn using retrieved"
[^c11]: doi-10-48550-arxiv-2212-10509 — "randomly sampled questions as our test set."
[^c12]: doi-10-48550-arxiv-2212-10509 — "the recall of the gold paragraphs among the retrieved set of paragraphs"
[^c13]: doi-10-48550-arxiv-2212-10509 — "by 11-21 recall points under a fixedbudget optimal recall setup"
[^c14]: doi-10-48550-arxiv-2212-10509 — "more effective than the baseline, one-step, questionbased retrieval"
[^c15]: doi-10-48550-arxiv-2212-10509 — "For GPT3, this improvement is by 11.3, 22.6,"
[^c16]: doi-10-48550-arxiv-2212-10509 — "on HotpotQA by 7.9, on 2WikiMultihopQA"
[^c17]: doi-10-48550-arxiv-2212-10509 — "improve the QA score on IIRC, despite significantly improved retrieval"
[^c18]: doi-10-48550-arxiv-2212-10509 — "using GPT3 for 40 randomly sampled"
[^c19]: doi-10-48550-arxiv-2212-10509 — "the factual errors over OneR by 50% on HotpotQA"
[^c20]: doi-10-48550-arxiv-2212-10509 — "with even the smallest model (0.2B) is better than"
[^c21]: doi-10-48550-arxiv-2212-10509 — "Flan-T5-XL (3B) with IRCoT even outperforms"
[^c22]: doi-10-48550-arxiv-2212-10509 — "the 58X larger GPT3 with a one-step questionbased retrieval"
[^c23]: doi-10-48550-arxiv-2212-10509 — "IRCoT retrieval outperforms OneR (Fig. 5), and IRCoT QA"
[^c24]: doi-10-48550-arxiv-2212-10509 — "we wrote CoTs for 20 questions for all the"
[^c25]: doi-10-48550-arxiv-2212-10509 — "we used the associated contexts to construct a"
[^c26]: doi-10-48550-arxiv-2212-10509 — "HQ (HotpotQA), 2W (2WikiMultihopQA), MQ (MuSiQue)"
[^c27]: doi-10-48550-arxiv-2212-10509 — "The reported metric can thus be viewed as the fixedbudget optimal recall"
[^c28]: doi-10-48550-arxiv-2212-10509 — "Note that our retrieved documents are not ranked, making standard information retrieval metrics such as MAP and"
[^c29]: doi-10-48550-arxiv-2212-10509 — "model can generate a wrong answer despite all correct facts"
[^c30]: doi-10-48550-arxiv-2212-10509 — "IRCoT relies on the base LM to have a zero or"
[^c31]: doi-10-48550-arxiv-2212-10509 — "as common for small LMs (under 20B), which to"
[^c32]: doi-10-48550-arxiv-2212-10509 — "IRCoT also relies on the base LM to support"
[^c33]: doi-10-48550-arxiv-2212-10509 — "IRCoT QA outperforms OneR QA for all model sizes except for the smallest"
[^c34]: doi-10-48550-arxiv-2212-10509 — "IRCoT makes a separate call to an (L)LM for each"
[^c35]: doi-10-48550-arxiv-2212-10509 — "dynamically deciding when to retrieve"
[^c36]: doi-10-48550-arxiv-2212-10509 — "We use BM25 as its underlying retriever"
[^c37]: doi-10-48550-arxiv-2212-10509 — "by OpenAI after our submission making the reproduction of these experiments challenging"
[^c38]: doi-10-48550-arxiv-2212-10509 — "Although these are not head-to-head"
