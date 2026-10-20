---
description: "When an agentic RAG cannot answer, suggest a similar answerable query by masking values, retrieving labeled workflow templates as few-shot examples, then imputing values; beats static few-shot."
aliases: ["query suggestion for agentic RAG", "robust dynamic few-shot query suggestion", "no-workflow versus no-knowledge"]
sources: ["arxiv-2601-08105"]
---
# Workflow-templated answerable query suggestion

When a tool-calling RAG agent fails on a user question, the useful reply is a nearby question it can answer. Spaeh et al. (2026) require two things of a suggestion: it should be "semantically similar to the user query and carry the same intent as the original query", and it should be "answerable by the RAG".[^c1]

## Two kinds of unanswerable

The paper separates failure by cause. "No workflow": the question "cannot be transformed into an executable workflow given the RAG's purpose and tools" (out of scope, or tool missing). "No knowledge": the agent can build the tool calls, but "there is no data pertaining to the specific values in the query", for example a tool returning an empty result.[^c2] The first needs a different question; the second needs only different values. The authors note the line is not clean, since a dynamic workflow can depend on earlier tool results.[^c3]

## Mechanism

1. **Templating.** An LLM replaces every entity value that would become a tool argument with its entity name ("How many invoices were processed in [timespan]?"), so a template stands for a workflow. Templates "cannot have data issues and are therefore either answerable or not answerable".[^c4]
2. **Self-labeling.** After the agent runs, an LLM sees the query, tool calls, responses and final answer and assigns an answerability category with an explanation. Judging in hindsight is easier than predicting up front, because the visible information about tools and data is limited.[^c5] Only "no workflow" and "answerable" examples are stored; "no knowledge" ones are skipped because the right values might still make them answerable.[^c6]
3. **Robust retrieval.** Template embeddings retrieve up to 5 positive and 5 negative examples. Near-duplicate retrieved examples are clustered and their answerability labels vote through counters, approximating a local majority vote, because almost identical queries can get different outcomes from faulty multi-step runs.[^c7]
4. **Generation and value imputation.** The LLM writes an answerable template similar to the query, then fills masks in priority order: original values unless they caused a data issue, then alternatives a tool returned, then example values from tools. This keeps the suggestion as close to the original as answerability allows.[^c8]

## Measured effect

Evaluated on three agents (two invoice, one order) with about 2000 real user questions each, five-fold cross-validated, with GPT-4o as generator and judge. Dynamic few-shot beat both a static few-shot baseline and retrieval-only on answerability and cosine similarity. Static few-shot traded similarity against answerability, and produced few answerable queries on Orders without tool feedback.[^c9] Retrieval-only answerability fell as similarity rose, while dynamic few-shot showed little to no trade-off.[^c10] Dynamic few-shot even exceeded retrieval-only answerability, which the authors attribute to the LLM choosing "more conservative questions" after seeing positive and negative examples.[^c11] The authors conclude a mere tool description does not suffice.[^c12]

## Limits

- One proprietary copilot on invoice and order data; single vendor, GPT-4o only. Generalization to other agents is untested.
- Answerability and similarity are judged by an LLM and an embedding cosine; no human study of whether users find suggestions helpful. Only the first suggestion is scored.
- Labels come from the same agent that may hallucinate; the majority vote only mitigates this. Queries needing workflows the LLM cannot deduce are ignored by design.[^c3]
- The claim that dynamic retrieval "generalizes" and the explanation for beating retrieval-only are the authors' interpretation, not isolated by ablation.

## Related

- [[answerable-clarification-strategies]] — answerability of a clarifying question, judged against a hidden full specification, rather than by agent execution
- [[corpus-grounded-clarification-generation]] — grounding generated questions in what the corpus can supply
- [[active-in-context-learning]] — choosing which examples to place in context
- [[task-ambiguity]] — unanswerable or unclear queries as the trigger for a follow-up question

[^c1]: arxiv-2601-08105 — "The suggested query should be semantically similar to the user query and carry the same intent as the"
[^c2]: arxiv-2601-08105 — "there is no data pertaining to the specific values in the query"
[^c3]: arxiv-2601-08105 — "Note that this distinction is not clear-cut as a dynamic workflow can depend on the results of prior tool-calls."
[^c4]: arxiv-2601-08105 — "they cannot have data issues and are therefore either answerable or not answerable"
[^c5]: arxiv-2601-08105 — "it is possible to determine the answerability in hindsight after"
[^c6]: arxiv-2601-08105 — "We ignore queries for which there is no knowledge since we cannot say with certainty whether the"
[^c7]: arxiv-2601-08105 — "we make our retrieval approach robust by approximating a local majority vote"
[^c8]: arxiv-2601-08105 — "The steps ensure that the values picked are as close as possible to the original query, while keeping the"
[^c9]: arxiv-2601-08105 — "the LLM is able to generate only few answerable"
[^c10]: arxiv-2601-08105 — "Dynamic few-shot learning exhibits little to no tradeoff"
[^c11]: arxiv-2601-08105 — "the LLM decides on more conservative questions which can be answered"
[^c12]: arxiv-2601-08105 — "implying that a mere description of tools does not suffice for the complex task of query"
