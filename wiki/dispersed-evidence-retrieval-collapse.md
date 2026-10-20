---
description: "When a question needs aggregation over evidence scattered across a whole corpus, top-k retrieval fails sharply with scale while iterative memory consolidation degrades far more slowly."
aliases: ["sparse retrieval assumption failure", "corpus-level analysis", "high evidence dispersion"]
sources: ["arxiv-2601-14952"]
---
# Dispersed-evidence retrieval collapse

Retrieval-augmented answering presupposes that a question can be answered from a few retrieved chunks, the "sparse retrieval" assumption. Corpus-level questions break it: the CorpusQA authors define corpus-level analysis as tasks where evidence is "finely scattered across the entire repository" and the answer needs integration, comparison and statistical aggregation (for example, how many companies generated more net cash from financing than from operating activities).[^c1] The question's form, not its topic, decides whether retrieval can work: a lookup question ("What is the revenue of Apple?") is sparse; a counting or comparison question over many documents is not.

## What was measured

Using Gemini-2.5-Pro as the base, a memory agent (processing chunks while updating a fixed-size memory buffer) beat RAG already at 128K (67.58 vs 55.85). At 1M the memory agent held 44.95 while RAG dropped to 17.38; at 4M and 10M RAG "nearly fails" while the memory agent stays functional.[^c2] Plain long-context models also decay with length: GPT-5 scores 82.02 at 128K, and at 1M Gemini-2.5-Pro reaches 50.73 while MiniMax-M1 collapses to 11.63.[^c3] The authors attribute the RAG failure to retrieval being unable to capture evidence scattered across thousands of documents, and say memory gives "more robust aggregation, though still far from solving the task".[^c4]

The benchmark's answers are computed programmatically from a structured schema extracted from the documents, then the original unstructured text is shown to the model; this decouples the reasoning from the text and avoids LLM-written ground truth.[^c5] A pilot of 480 synthesized samples with 25 GRPO steps on Qwen3-4B-Thinking raised in-domain scores and also scores on FRAMES and LongBench V2.[^c6]

## Limits

- The RAG-versus-memory comparison is one base model (Gemini-2.5-Pro) and one RAG configuration; stronger retrieval (large k, iterative or agentic retrieval) was not shown to fail in the same way. That the RAG failure is caused by dispersion rather than by implementation is the authors' interpretation.
- Questions are computation-heavy, schema-derived queries over financial-style documents; whether naturally asked questions are this dispersed is not established.
- Scoring uses an LLM judge (DeepSeek-V3), so the "guaranteed" correctness covers the reference answers, not the grading.
- The training result is a small pilot (one model, 480 samples) with no repeated runs reported.
- The link between question type and the retrieval-versus-memory choice as a routing signal is my inference, not tested here.

## Related

- [[cross-retriever-reformulation-gain]] — query rewriting helps retrieval; here no rewrite fixes a question whose answer is not in a few chunks.
- [[coverage-driven-retrieval-control]] — coverage of the needed evidence as the control variable, the quantity that dispersion defeats.
- [[retrieval-utilization-gap]] — another point where retrieved evidence fails to become a correct answer.
- [[syntactic-complexity-routing-between-retrieval-paths]] — routing questions between retrieval paths by form.

[^c1]: arxiv-2601-14952 — "A defining characteristic of this paradigm is the high dispersion of evidence, where critical information is not concentrated in a few documents but is finely scattered across the entire repository."
[^c2]: arxiv-2601-14952 — "At 128K, Memory Agent already outperforms RAG (67.58 vs. 55.85)."
[^c3]: arxiv-2601-14952 — "with MiniMax-M1-80k collapsing to 11.63 at 1M"
[^c4]: arxiv-2601-14952 — "In contrast, memory mechanisms provide more robust ag"
[^c5]: arxiv-2601-14952 — "By first structuring the information, programmatically deriving ground-truth answers, and then re-presenting the original unstructured documents to the models being evaluated"
[^c6]: arxiv-2601-14952 — "We synthesized a new training set of 480 samples"
