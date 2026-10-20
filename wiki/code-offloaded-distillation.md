---
description: "Per-document evidence is normalized into one shared JSON schema, induced from a sample and filled in batches, then a generated program, not the LLM's context, computes the final answer."
aliases: ["scalable code agent", "schema-then-code aggregation"]
sources: ["arxiv-2604-22239"]
---
# Code-offloaded distillation

> The model never reads the gathered evidence at once — it reads a schema, a
> few examples, and writes the program that reads the rest.[^c1]

## Definition / Mechanism

Given a global query answerable only by combining facts scattered across
hundreds or thousands of documents (Li et al. (2026)),
the compression step does not feed the combined evidence back into an LLM's
context. Two agents split the job.
First, a **normalization agent** converts each document's unstructured
extraction transcript into a structured JSON record. Because thousands of
transcripts would themselves overflow any context, the schema is not fixed
in advance: it is induced once from a small sample of the extracted
question-answer pairs, then every subsequent batch is normalized under that
one fixed schema — "a schema is defined from a small sample, and subsequent
records are normalized in batches under this unified schema."[^c2]

Second, a **code agent** never sees the full structured dataset either. It
is given only the schema and a handful of example records, plus a pointer to
where the full set has been saved: "Rather than feeding the entire extracted
information into the LLM, we provide the agent with the schema and some
examples. The agent synthesizes a program to perform analysis over the full
structured dataset J … yielding the final answer A." The program — not
the language model — performs the actual aggregation (filtering, joining,
counting, computing a ratio) over every record, and its output is the
distillate returned as the final answer.

The schema is what [[sufficient-statistic|a sufficient statistic]] is for a
parameter: the one summary through which every downstream computation is
allowed to pass, discarding the raw transcript once its fields are filled.
The two-agent split is an instance of [[compound-ai-systems|routing
distillation to a non-LLM component]] of the system rather than asking one
model call to hold and reduce everything.

## Why it matters

On a 332-question, 80,000-page multi-document financial-QA benchmark, the
paper's own diagnosis is that retrieval recall is not the bottleneck: "the
main bottleneck is not merely retrieval recall, but the model's ability to
synthesize fragmented evidence into a correct aggregated conclusion."[^c4]
Standard RAG's failure mode is exactly the one this mechanism targets —
compression left to the LLM's context window — and moving that step to
generated code, over normalized records, is what the paper reports as the
fix: "the proposed agentic workflow substantially outperforms direct RAG in
final-answer accuracy, demonstrating the value of decomposing extraction and
reasoning into modular stages."[^c5]

## Limits

The result is comparative, on one benchmark and one domain (financial
filings), with the workflow's own component models chosen for cost rather
than held fixed across conditions — `unverified` that the split generalizes
outside tabular/quantitative aggregation, where "compute a program over
records" is a natural fit and may not be for open-ended synthesis. The
mechanism still degrades under distractors: injecting irrelevant documents
"causes a noticeable drop in final-answer accuracy, especially on complex
questions, indicating that downstream aggregation and reasoning remain
important bottlenecks" — normalization and code do not make the earlier,
per-document extraction step immune to noise, and the paper reports the
workflow still trails human performance overall.

## Related

- [[compound-ai-systems]]
- [[sufficient-statistic]]
- [[information-bottleneck]]
- [[specification-mining]]

[^c1]: arxiv-2604-22239 — "A key feature of this approach is its ability to scale to processing hundreds or thousands of documents."
[^c2]: arxiv-2604-22239 — "Crucially, to avoid context overflow when processing thousands of documents, we adopt a batch-iterative strategy: a schema is defined from a small sample, and subsequent records are normalized in batches under this unified schema."
[^c4]: arxiv-2604-22239 — "This pattern suggests that the main bottleneck is not merely retrieval recall, but the model’s ability to synthesize fragmented evidence into a correct aggregated conclusion."
[^c5]: arxiv-2604-22239 — "The proposed agentic workflow substantially outperforms direct RAG in final-answer accuracy, demonstrating the value of decomposing extraction and reasoning into modular stages."
