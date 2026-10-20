---
description: "Classifies a failed search-agent run as a retrieval gap (evidence never surfaced) or a utilization gap (surfaced but misused), via gold-qrels."
aliases: ["retrieval gap", "utilization gap", "RG/UG decomposition", "context blindness", "P(Utilization | Retrieved)"]
sources: ["liu-2026-diagnosing", "doi-10-48550-arxiv-2407-12216", "arxiv-2603-04403", "arxiv-2512-15219", "arxiv-2601-03261", "arxiv-2512-05863", "arxiv-2512-05576", "arxiv-2512-01241", "doi-10-54254-2753-8818-2026-dl34055", "arxiv-2511-18931", "doi-10-4230-lipics-esem-2026-28", "arxiv-2511-15994"]
---
# Retrieval-utilization gap

> A wrong answer from a search agent has two, mutually exclusive causes —
> the evidence was never found, or it was found and still misused — and
> the fix for one does nothing for the other.

## Definition / Mechanism

For a trajectory $\xi$ answering question $q$, let $G^*(\xi)$ be the set
of gold-qrels documents the trajectory actually surfaced. A failed or
incomplete run is a **utilization gap** if $G^*(\xi) \neq \emptyset$ (the
sufficient evidence was in hand) and a **retrieval gap** if $G^*(\xi) =
\emptyset$ (it never was). "We call the first case a retrieval gap and the
second a utilization gap, then analyze their distribution and intervention
implications: retrieval-side fixes for RG, and a mix of reasoning and
evaluation fixes for UG." The split is deterministic — decided by
human-annotated document-level qrels, not an LLM judge — so it is not
confounded with answer-judging noise.[^c1]

## Why it matters

Across six agents on BrowseComp-Plus, "RG accounts for 51.6–64.1% of
errors for five agents. Kimi K2.6 is the exception, with 52.0% UG,
consistent with its high mean gold recall of 78.2%."[^c2]

The split does not track the leaderboard: "GLM 5.1 reaches 74.1% accuracy
and Tongyi-DR only 52.2%, yet their RG shares are within 6 pp... Kimi K2.6
and Deepseek V4 Pro land within a point of each other in accuracy yet on
opposite sides of the RG/UG split, so nearly identical leaderboard
positions can call for opposite fixes." A single accuracy number therefore
hides which of two opposite interventions — search better, or verify
better — a given agent needs.[^c3]

A structured-data benchmark adds a behavioural case of the same split. In FinRetrieval, Claude's web-search-only runs were often "failed to commit to an answer, instead continuing to search until timing out or explicitly declining to answer" after relevant results had been found.[^c7] The authors attribute about 35 points of Claude's 71-point tool-availability gap to this pattern, and a second part to its web tool returning search snippets, "not full document access or PDF parsing."[^c8][^c9] In the terms of this note, the first is evidence that was surfaced and not used, a utilization-side failure; the second is a retrieval-side limit. This mapping is mine: that paper has no gold qrels and does not use the RG/UG terms.

A knowledge-graph question-answering error analysis draws the same two families with a different balance. Mindful-RAG's authors "meticulously reviewed logs from around 435 error cases" of StructGPT on WebQSP.[^c5] One family is structural: knowledge "becomes inaccessible due to limitations in the structural design" of the knowledge base.[^c4] The other is reasoning, and there the paper concludes that "most failures stem from the LLMs’ inability to reason correctly."[^c6] Read this way, most of that system's failures sit on the utilization side, the reverse of the search-agent split above. The mapping of "structural" onto retrieval gap and "reasoning" onto utilization gap is my inference; the paper does not define its families through gold evidence.

The knowledge-graph paper RFKG-CoT pairs a retrieval-side change with a utilization-side one. Few-shot exemplars in a question-paths-answer format, with a think line that maps path elements to the answer, raised KG-CoT by +5.6 points on WebQSP and +6.2 on CompWebQ when used alone, and the paper describes this as "enhancing path utilization by teaching LLMs to interpret structured paths."[^c10][^c11] Gains peak at three exemplars: "Beyond this optimum, additional examples progressively degrade results."[^c12] The retrieval-side change, a relation mask over the traversal, is covered in [[relation-driven-hop-count-selection]]. Whether the exemplar gain is a utilization fix in this note's sense is my inference: the paper does not classify its errors into the two families. Its report that the correct answer appears in the generated paths for 92.3% of WebQSP would, if those paths are the retrieved evidence, put most of the remaining misses on the retrieval side; that reading is also mine.[^c13]

A remedy aimed at the utilization side, rather than at search, is proposed in DeepResearch-Slice. Its authors decompose accuracy as P(Correct) = P(Retrieved) × P(Utilization | Retrieved), and name the failure "where models fail to utilize gold evidence" once it is in context.[^c14] The fix is an explicit selection step: the model "predicts a small set of token-span indices that are most likely" to hold the answer, and a deterministic parser keeps only those spans before a frozen reasoner reads them.[^c15] The authors read this as a hard filter, since the parser "operation acts as a hard filter, physically removing" the other tokens.[^c16] Their toy model says that with N segments and one gold segment, implicit attention decays as noise grows: "as the volume of retrieved noise increases (N → ∞), the effective recall vanishes".[^c17] Selection is claimed to be "theoretically decoupled" from N.[^c18] On a frozen Qwen2.5-7B-Instruct, the paper reports that Slice "yields a dramatic +73% relative improvement (19.1% → 33.0%".[^c19] In this note's terms the remedy changes P(U | R) and leaves retrieval untouched, which fits the claim above that the two gaps need separate fixes.

A medical question-answering system gives a second, measured case, on
different terms. A retrieval-augmented LLaMA 2 model was checked by hand:
two medical professionals annotated 100 sampled test answers for factual
errors and unsupported claims, and retrieval lowered factual errors from
35% in the fine-tuned-only setting to 14%.[^c23] The abstract puts the drop
in unsupported content at about 60%.[^c24] The authors sort what remained
after retrieval into three kinds: misinterpretation of statistical findings
in the retrieved papers (32% of the remaining errors), overgeneralization
from specific study populations (28%), and outdated information from older
retrieved documents (25%).[^c25] Read against this note, the first two are
utilization failures, since the evidence was in context and was misread or
stretched. The third is an evidence-quality failure that neither gap names.
That mapping is mine; the paper does not use the RG/UG terms. Grounding did
not make answers checkable either: only 42% of answers gave clear source
attribution.[^c26]

A tool-using clinical agent gives a third measured split. The CURE-Bench authors sorted 73 failed multiple-choice cases of TxAgent, a small clinical model, drawn from a validation set of 413 questions.[^c35] Reasoning and retrieval failures make up 65.8% of them, and the authors call the bulk of that share a Context Utilization Failure: "the agent successfully gathers sufficient evidence but fails to ground its final diagnosis in this information, leading to hallucination."[^c31] Format failures sit outside the split: "Instruction Adherence Failures (12.3%) occur when the agent disregards formatting constraints", and output parsing accounts for a further 19.2%.[^c32] Against this note, the first family is on the utilization side, though the label is the paper's own and it does not use the RG/UG terms.

The paper's remedy is utilization-side in form. A long-context model, the Analyst, reads the evidence a tool agent, the Executor, has gathered. In the paper's Table 4 ablation, one Executor with one Analyst reached "single Analyst (74.701%), suppressing the isolated TxAgent baseline (69.325%)", and the standalone Gemini baseline was "Gemini baseline (63.104%)".[^c33][^c34] The comparison changes the backbone as well as adding a reader, so it does not show that the reading step alone was the fix.

The same split appears when the reader is a person. In a randomized crossover study of physicians given an AI chat tool, the authors coded the chat transcripts and found that "appropriate recommendations were surfaced by the AI but not included in the physician" response.[^c36][^c37] The surfacing side was done by the tool; the misuse was the physician's. The authors' counterfactual is that physicians who had taken up every surfaced recommendation "would have outscored both their own" responses and the assistant as used.[^c38] That is a recomputation on recorded outputs, not an observed arm. The mapping to a utilization gap is mine: the paper does not use the RG/UG terms and has no gold-evidence qrels, so it cannot separate a retrieval failure on the tool's side from a utilization failure on the physician's.

A 2026 review of hallucination in retrieval-augmented generation widens the split from two gaps to a pipeline. It names where errors arise, from the query onward: "Errors may arise during query formulation, document retrieval" and on through evidence aggregation and answer grounding.[^c39] Its frame puts the risk in the system rather than the generator: "Hallucination risk is then not solely a function of generation, but of the coupled system."[^c41] Read against this note, a retrieval fix and a utilization fix can each be wasted without the other, since "Grounded decoding without reliable retrieval amplifies bad evidence."[^c42] The review also adds an attribution stage that the RG/UG pair does not name: "Citation presence therefore should not be equated with evidential sufficiency."[^c40] Its four-stage table is offered because it "aligns mechanisms, symptoms, and likely intervention points."[^c43] Whether a citation failure is a separate class from a utilization failure is the review's classification, not a measurement; the RG/UG split cannot test it without gold evidence for each claim (my inference).

A three-stage split of failed internal web search refines the retrieval side without replacing the pair. In a study of four closed-source LLMs with built-in search, failed runs were sorted into query formulation failures, where the "search query underspecifies the information need, omits" critical entities or constraints; source quality failures, where the query is sound but "retrieved sources are outdated, low-quality," or insufficient; and evidence integration failures, where "the query is correctly formulated and relevant information is retrieved," but is misreflected in the answer.[^c45][^c46][^c47] On the static split query formulation was the largest class, "accounting for roughly half of" the failures; on the dynamic split source failures "increase substantially and become comparable to or exceed query formulation failures".[^c48][^c49] Integration failures "are consistently the least frequent".[^c50] Read against this note, query formulation sits on the retrieval-gap side, since the needed evidence was never requested; integration sits on the utilization side. Source failure is the unclear class: a retrieved but outdated source may leave the gold evidence out of the retrieved set, which would make it a retrieval gap, or leave it in, which would make it a utilization gap. The paper's classes are annotator judgments without gold evidence, so this placement is mine. The paper's own conclusion is that the primary bottlenecks "lie in query formulation and source selection" rather than in answer synthesis.[^c51]

A coding-agent benchmark measures the same split per element rather than per run. ContextBench logs every code region an agent inspects and asks how much of the gold context it saw is still in the final patch context. Its authors put the gap plainly: "agents may observe gold-relevant regions during exploration but fail to retain them" in the final patch.[^c54] The drop is "consistent" across the evaluated agents — "We also observe a consistent context usage drop across all evaluated agents" — and "Gemini 2.5 Pro and Devstral 2 exhibit the most severe context loss."[^c55][^c56] The authors take it as a cause of failure, since many gold contexts retrieved at intermediate steps are not "incorporated into the final reasoning process, leading to issue resolution failures despite retrieval."[^c57] Read against this note, the drop is a utilization-side loss of evidence that was in hand at some step (my inference, since the paper uses no RG/UG terms).

A clinical benchmark gives a case where the evidence is supplied rather than searched. CARE-RAG builds questions from the manual of a brief PTSD therapy and answers each one under a relevant-passage, a relevant-plus-noise and a misleading-passage condition. Its abstract reports that "errors persist even when authoritative passages are provided."[^c59] Its conclusion places the gap where the split above does: "models may retrieve the right content but still misinterpret clinical instructions."[^c60] The paper does not use the RG/UG terms and does not separate its failures into the two families, so reading the gap as utilization-side is my inference. The steps by which a reasoning trace is scored against its passages are in evidence-entailment-fidelity.

## Transfer

| | Home field (search-agent evaluation) | Here (asking, task-agnostic) | What survives | What does not |
|---|---|---|---|---|
| Object | a completed agent trajectory over a fixed retrieval corpus | any process that gathers constraints then commits to an answer | the binary split between "never obtained the needed input" and "obtained it, used it wrong" as two distinct, separately fixable failure classes | — |
| Ground truth | human-annotated, document-level gold-qrels per question | no equivalent gold set for general question-asking | — | the deterministic, judge-free classification; outside a qrels-style benchmark the split has to fall back on a noisier judge, which reintroduces the confound this method was built to avoid |

## Limits

The classification presupposes a fixed, exhaustively-annotated evidence
corpus with gold-qrels per question (BrowseComp-Plus); it identifies which
gap dominates only within that benchmark's six agents, and the paper does
not report whether the RG/UG balance is stable under a different retriever
or corpus.

The knowledge-graph split is weaker evidence. It rests on manual and LLM-assisted categorization of one system's error logs, not on gold evidence, and the portion of the paper read gives no count per family. Its "structural" family also covers inefficient processing, which the retrieval-gap test would not separate out.[^c4]

The DeepResearch-Slice evidence is narrower than its framing. Its pilot "fixed P (R) = 1 by injecting gold evidence into" a synthetic context, so it measures utilization under artificial distractors and says nothing about retrieval that failed to surface the evidence.[^c20] The slicer is "a slice head trained on frozen backbones using supervised oracle spans", so the gain assumes labelled evidence spans exist and is not a result about unlabelled search.[^c21] The headline result is one frozen backbone on open-domain QA benchmarks in the Clean retrieval setting; the noisy-retrieval tables were not in the part of the text read here. The paper's own note on its first page says "Ongoing work."[^c22] Whether span selection helps open-ended research questions, which the abstract names as its target, is not shown; that is my inference from the benchmark list.

The medical QA figures rest on one hand-annotated sample: 100 answers from
one fine-tuned model, LLaMA 2 13B, with a dense retriever returning the top
five passages.[^c30][^c29] The annotation agreed substantially, but the
error categories are the authors' own, and the 60% matches the arithmetic of
35% falling to 14% (a 60% relative drop) without the paper saying the two
counts are the same. The text read does not report whether gold evidence was
among the five passages, so this paper cannot say how much of its residual
error is retrieval-side and how much is utilization-side.[^c27]

The CURE-Bench split rests on the authors' own sort of 73 validation failures, with no gold evidence set. The paper does not check whether the answer was among the retrieved evidence, so its 65.8% cannot be read as a utilization share in the sense used above.[^c35] The Executor-Analyst gain is one ablation on one benchmark. Each baseline lacks one of the two components, and the Analyst runs on a different backbone from the tool agent, so the table does not isolate the reading step from the change of model.

The RAG review is an argument, not a measurement. Its loss-style equations are presented as design principles rather than fitted: "Equation (5) is not tied to a single model; it captures the design principle required by trustworthy RAG."[^c44] No experiment in it separates the stages, so the claim that they compose, and that the attribution stage is a failure of its own, is untested in that text. The four stages also lack the judge-free test that makes the RG/UG split deterministic; a stage such as query drift or citation support would need its own gold reference before it could be counted the same way (my inference).

The three-stage split rests on annotator judgment, not on a deterministic test. Two annotators coded "a random sample of 150 incorrect examples per model for the static" split and 75 for the dynamic split, so each share is a sample figure, and the paper does not run the split on gold evidence.[^c52] The paper evaluates "four models across two model families and scales," so the stage split is a per-run diagnosis for one benchmark's annotators, not a gold-qrels classification like the one above.[^c53]

The coding-agent drop is not a run-level classification. It is a share per element, where a higher drop means gold evidence "is frequently observed but discarded during consolidation."[^c58] The paper does not split its failed runs into retrieval gaps and utilization gaps, and a run can show a large drop and still be answered correctly, so the drop cannot be read as the failure rate of the utilization side. Its gold set is also annotated from the patch, so "seen but dropped" depends on what the annotators counted as gold (my inference).

## Related

[[search-effort-accuracy-decoupling]] · [[query-discipline]] · [[grounded-selective-pruning]]

- [[failure-mode-taxonomy]] — the same aim of locating a failure by stage, applied to research-agent logs rather than to RAG pipelines
- [[evidence-forgetting-rate]] — the same separation of retrieval recall from evidence use, as a rate over multi-hop RAG cases
- [[context-recall-precision-tradeoff]] — the recall side of the same coding-agent benchmark: broader gathering raises gold recall and lowers precision
- evidence-entailment-fidelity — scores whether a trace's steps are licensed by the passages it was given, the reference for the utilization side here

[^c1]: liu-2026-diagnosing — "We call the first case a retrieval gap and the second a utilization gap, then analyze their distribution and intervention implications: retrieval-side fixes for RG, and a mix of reasoning and evaluation fixes for UG."
[^c2]: liu-2026-diagnosing — "RG accounts for 51.6–64.1% of errors for five agents. Kimi K2.6 is the exception, with 52.0% UG, consistent with its high mean gold recall of 78.2%."
[^c3]: liu-2026-diagnosing
[^c4]: doi-10-48550-arxiv-2407-12216 — "becomes inaccessible due to limitations in the structural design"
[^c5]: doi-10-48550-arxiv-2407-12216 — "We meticulously reviewed logs from around 435 error cases"
[^c6]: doi-10-48550-arxiv-2407-12216 — "inability to reason correctly"
[^c7]: arxiv-2603-04403 — "failed to commit to an answer, instead continuing to search until timing out or explicitly declining to answer."
[^c8]: arxiv-2603-04403 — "This behavioral pattern accounts for approximately 35pp"
[^c9]: arxiv-2603-04403 — "not full document access or PDF parsing."
[^c10]: arxiv-2512-15219 — "yields balanced gains (+5.6 pp on WebQSP, +6.2 pp on CompWebQ)"
[^c11]: arxiv-2512-15219 — "enhancing path utilization by teaching LLMs to interpret structured paths"
[^c12]: arxiv-2512-15219 — "Beyond this optimum, additional examples progressively degrade results"
[^c13]: arxiv-2512-15219 — "the correct answer appears in generated reasoning paths for 92.3% of WebQSP"
[^c14]: arxiv-2601-03261 — "and the subsequent correct utilization of that evidence"
[^c15]: arxiv-2601-03261 — "a small set of token-span indices that are most likely"
[^c16]: arxiv-2601-03261 — "operation acts as a hard filter, physically removing"
[^c17]: arxiv-2601-03261 — "Critically, as the volume of retrieved noise increases (N → ∞), the effective recall vanishes"
[^c18]: arxiv-2601-03261 — "the Slice mechanism is theoretically decoupled"
[^c19]: arxiv-2601-03261 — "yields a dramatic +73% relative improvement (19.1% → 33.0%"
[^c20]: arxiv-2601-03261 — "we fixed P (R) = 1 by injecting gold evidence into"
[^c21]: arxiv-2601-03261 — "a slice head trained on frozen backbones using supervised oracle spans"
[^c22]: arxiv-2601-03261 — "Ongoing work."
[^c23]: arxiv-2512-05863 — "retrieval augmentation reduced factual errors from 35% in the fine-tuned-only"
[^c24]: arxiv-2512-05863 — "grounding answers in retrieved evidence reduces unsupported content by approximately 60%"
[^c25]: arxiv-2512-05863 — "misinterpretation of statistical findings from retrieved papers (32% of errors)"
[^c26]: arxiv-2512-05863 — "only 42% of answers including clear source attribution"
[^c27]: arxiv-2512-05863
[^c28]: arxiv-2512-05863 — "Inter-annotator agreement was substantial"
[^c29]: arxiv-2512-05863 — "We use k = 5, which provides sufficient context while balancing relevance"
[^c30]: arxiv-2512-05863 — "we manually evaluated 100 randomly sampled QA pairs from the test set"
[^c31]: arxiv-2512-05576 — "the agent successfully gathers sufficient evidence but fails to ground its final diagnosis in this information, leading to hallucination"
[^c32]: arxiv-2512-05576 — "Instruction Adherence Failures (12.3%) occur when the agent disregards formatting constraints"
[^c33]: arxiv-2512-05576 — "single Analyst (74.701%), suppressing the isolated TxAgent baseline (69.325%)"
[^c34]: arxiv-2512-05576 — "Gemini baseline (63.104%)"
[^c35]: arxiv-2512-05576 — "failure cases with ground truth in the validation set"
[^c36]: arxiv-2512-01241 — "crossover study of 101 board-certified attending physicians"
[^c37]: arxiv-2512-01241 — "appropriate recommendations were surfaced by the AI but not included in the physician"
[^c38]: arxiv-2512-01241 — "they would have outscored both their own"
[^c39]: doi-10-54254-2753-8818-2026-dl34055 — "Errors may arise during query formulation, document retrieval"
[^c40]: doi-10-54254-2753-8818-2026-dl34055 — "Citation presence therefore should not be equated with evidential sufficiency"
[^c41]: doi-10-54254-2753-8818-2026-dl34055 — "Hallucination risk is then not solely a function of generation, but of the coupled system"
[^c42]: doi-10-54254-2753-8818-2026-dl34055 — "Grounded decoding without reliable retrieval amplifies bad evidence"
[^c43]: doi-10-54254-2753-8818-2026-dl34055 — "This structure is preferable to a flat list because it aligns mechanisms, symptoms, and likely intervention points"
[^c44]: doi-10-54254-2753-8818-2026-dl34055 — "Equation (5) is not tied to a single model; it captures the design principle required by trustworthy RAG"
[^c45]: arxiv-2511-18931 — "search query underspecifies the information need, omits"
[^c46]: arxiv-2511-18931 — "retrieved sources are outdated, low-quality,"
[^c47]: arxiv-2511-18931 — "correctly formulated and relevant information is retrieved,"
[^c48]: arxiv-2511-18931 — "accounting for roughly half of"
[^c49]: arxiv-2511-18931 — "increase substantially and become comparable to or exceed query"
[^c50]: arxiv-2511-18931 — "Evidence integration failures are consistently the least frequent"
[^c51]: arxiv-2511-18931 — "lie in query formulation and source selection"
[^c52]: arxiv-2511-18931 — "a random sample of 150 incorrect examples per model for the static"
[^c53]: arxiv-2511-18931 — "We experiment across four models across two model families and scales"
[^c54]: doi-10-4230-lipics-esem-2026-28 — "agents may observe gold-relevant regions during exploration but fail to retain them"
[^c55]: doi-10-4230-lipics-esem-2026-28 — "We also observe a consistent context usage drop across all evaluated agents"
[^c56]: doi-10-4230-lipics-esem-2026-28 — "Gemini 2.5 Pro and Devstral 2 exhibit the most severe context loss"
[^c57]: doi-10-4230-lipics-esem-2026-28 — "incorporated into the final reasoning process, leading to issue resolution failures despite retrieval"
[^c58]: doi-10-4230-lipics-esem-2026-28 — "frequently observed but discarded during consolidation"
[^c59]: arxiv-2511-15994 — "errors persist even when authoritative passages are provided"
[^c60]: arxiv-2511-15994 — "models may retrieve the right content but still misinterpret clinical instructions"
